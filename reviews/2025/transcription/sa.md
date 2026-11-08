# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 14be893889613c275e411636a9c4f8908e0bbbd991bb3b1aa4077f5205b9fbaf |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a639d4ae5c2d954fccfb674084c9dfe7a2e82e43ef242236dda33dfe89d83724 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | db1543ebd2f331ad735d7efc1b1ec2f167dca06d6045bc946d2835324faaefa0 |
| printed lines compared | 23 |
| agree / disagree / missing | 19 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### sa.age65 — Were you born before January 2, 1961?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The pages do not define this interface. Read as Exception 4: whether any line 12d box (age or blindness) is checked, which is what selects the Standard Deduction Chart. Spouse boxes count only on a joint return. They are not checked for HOH, the QSS chart has no spouse rows, and MFS spouse boxes are refused (sa.spouse_extra).

Ruling: model error; f1040s1a (2025), line 36a: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35", with the spouse on line 36b; i1040gi p. 33, Line 12d, separates the boxes for you and for your spouse. sa.age65 is the published question "Were you born before January 2, 1961?" for you alone (its consumer is Schedule 1-A line 36a); the candidate reads it as whether any line 12d box (age or blindness, yours or a joint spouse's) is checked. The 17 completed-return value differences (project false, candidate true) are returns where you were not born before January 2, 1961 but your joint spouse was, or (classm.tcw.16) your spouse is blind: classm.f8962.5.deepseek (spouse age 65 or older, you not), classm.f8962.5.gpt, classm.scveh.1, classm.tcw.16, mutation.t2.f8962_months_asset3, generated returns 208, 254, 255, 290, 366, 373, 395 and 476, and four partial records of classm.f8962.5.gpt (sa.spouse_extra, sa.spouse_itemizes, sa.elect_itemize or sa.gambling_losses withheld). Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.json`; 1,495 fixtures, 500 generated returns seed 20261026, 526 partial records from 40 bases; 2,521 comparisons): 2,427 agree; differences 17 candidate-unknown, 77 value; on completed returns 17 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### sa.agi — Form 1040 line 11b adjusted gross income
Status: **AGREE**

### sa.itemizes — Itemize if elected, required, or itemized total exceeds standard
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The text says to take the larger of the standard or itemized deductions, or to itemize by election (line 18). When the two are equal the result is the same either way; the standard deduction is chosen. A MFS filer whose spouse itemizes is treated as itemizing, since that filer's standard deduction is zero.

Ruling: model error; i1040gi p. 33, Line 12b: "If your filing status is married filing separately and your spouse itemizes deductions on their return, check the box on line 12b"; p. 14: "You also can’t take the standard deduction if your spouse itemizes deductions" (Married Filing Separately); i1040sca p. 11, Line 16: "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets) but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." The candidate's selection applies sa.spouse_itemizes without the married-filing-separately condition, and its line 17 carries its line 16, which needs sa.gambling_losses without gambling winnings. On completed returns the differences are 170 candidate-unknown (sa.gambling_losses on 100 records with no gambling winnings, sa.spouse_itemizes on 53 and sa.spouse_extra on 13 non-MFS records, sa.elect_itemize on 4 partials where line 17 is unknown on the candidate's side), 3 candidate-refuses at sa.spouse_extra on single returns whose record answers it Yes (classm.clcw.2, classm.clcw.2.deepseek, mutation.t2.no_senior_part5), and 3 value records, all of the one shape: classm.f5695.8.deepseek is a single return whose record answers sa.spouse_itemizes Yes ("Married filing separately with a spouse who itemizes?"); the project's sa.mfs_spouse_itemizes requires married filing separately, so it takes the $15,750.00 standard deduction against line 17 of $7,874.00, where the candidate itemizes. The interview cannot produce that record (a single filer answers No to a question that opens "Married filing separately"), and married filing separately is itself refused (s3.mfs). The other two value records are partials of classm.f5695.8.deepseek. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.json`; 1,495 fixtures, 500 generated returns seed 20261026, 526 partial records from 40 bases; 2,521 comparisons): 1,392 agree; differences 23 candidate-refuses, 1082 candidate-unknown, 9 project-refuses, 11 project-unknown, 4 value; on completed returns 3 candidate-refuses, 170 candidate-unknown, 3 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"of": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.died_before_65"}], "test": "ne"}], "test": "all"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}], "op": "sum"}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 33, Line 12b: "If your filing status is married filing separately and your spouse itemizes deductions on their return, check the box on line 12b"; p. 14: "You also can’t take the standard deduction if your spouse itemizes deductions" (Married Filing Separately); i1040gi p. 34, Line 12e: "your federal income tax will be less if you take the larger of your standard deduction or itemized deductions". Inherited from sa.itemizes and line 16. The 2 completed-return value records are classm.f5695.8.deepseek and its partial withholding sa.spouse_extra: classm.f5695.8.deepseek is a single return whose record answers sa.spouse_itemizes Yes ("Married filing separately with a spouse who itemizes?"); the project's sa.mfs_spouse_itemizes requires married filing separately, so it takes the $15,750.00 standard deduction against line 17 of $7,874.00, where the candidate itemizes. The interview cannot produce that record (a single filer answers No to a question that opens "Married filing separately"), and married filing separately is itself refused (s3.mfs). The completed-return candidate-unknown (sa.gambling_losses, sa.spouse_itemizes, sa.spouse_extra, sa.elect_itemize) and candidate-refuses (sa.spouse_extra on single records) are as at sa.itemizes. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.json`; 1,495 fixtures, 500 generated returns seed 20261026, 526 partial records from 40 bases; 2,521 comparisons): 1,388 agree; differences 30 candidate-refuses, 1096 candidate-unknown, 2 project-refuses, 2 project-unknown, 3 value; on completed returns 3 candidate-refuses, 171 candidate-unknown, 2 value; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 11 — Gifts by cash or check (zero when you and your spouse gave nothing to charity and have no
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 2 — Amount from sa.agi_floor
Status: **AGREE**

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**
Reviewed in: pass 07eff69e6904

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**
Reviewed in: pass 07eff69e6904

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **AGREE**

### 6 — Amount from sa.zero
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 8b — Amount from sa.zero
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 8c — Amount from sa.zero
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 13 — Amount from sa.zero
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 15 — Amount from sa.zero
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 16 — Other—from list in instructions. List type and amount:
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "s1.gambling_winnings"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "s1.gambling_winnings"}], "test": "lt"}, "then": {"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}
```

Second transcription's note: The only supported item from the line 16 list is gambling losses. The instructions limit them to the gambling winnings reported on Schedule 1 (Form 1040), line 8b. Every other line 16 item, and any net qualified disaster loss or increased standard deduction reporting, is refused through sa.unsupported.

Ruling: model error; same reply and project expression as the earlier rulings; the line was reopened only because its refusal gate sa.charity_limited became a gate line behind sa.gifts. i1040sca p. 11, Line 16: "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets) but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." The project enters zero without gambling winnings and the smaller of sa.gambling_losses and Schedule 1 line 8b otherwise; the candidate always takes the smaller, so it needs sa.gambling_losses on every return though the amount is zero without winnings. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/sa.json`; 1,638 fixtures, 500 generated returns seed 20261026, 539 partial records; 2,677 comparisons): 972 agree; 1,594 candidate-unknown (184 on completed returns, all sa.gambling_losses), 67 project-refuses (the cited screens sa.unsupported, sa.charity_limited, sa.excluded_income), 44 project-unknown (withheld screen answers). Project stands.
Reviewed in: pass f56e521f4163

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **AGREE**

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits (zero when you and your spouse gave
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**
Reviewed in: pass f56e521f4163

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**
Reviewed in: pass f56e521f4163

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sa.itemizes | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| sa.deduction | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| 11 | sa.charity_limited | sa.charity_limited |
| 5e | sa.excluded_income, sa.unsupported | sa.unsupported |
| 6 | sa.unsupported | - |
| 8b | sa.unsupported | - |
| 8c | sa.unsupported | - |
| 13 | sa.charity_limited | sa.charity_limited |
| 15 | sa.unsupported | - |
| 16 | sa.unsupported | - |
| 7 | sa.excluded_income, sa.unsupported | - |
| 8e | sa.unsupported | - |
| 10 | sa.unsupported | - |
| 12 | sa.charity_limited | sa.charity_limited |
| 14 | sa.charity_limited | sa.charity_limited |
| 17 | sa.charity_limited, sa.unsupported | sa.charity_limited |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sa.age65 | 768f14dd86250bfb0df776167739722ee3b518315715c3b6282afb7074c8541b |
| sa.agi | 7ac40a0d224f103b5668b2d9b355ac1ecb9b68c3d5235bd8ae09b20888315bc8 |
| sa.itemizes | ad4db0f95ab83183ecdedb3a2b0d58c4d33534be64ba6ab315ad5cad220949be |
| sa.deduction | cadc70373beef251c7ce5e4a979aafa7485532c86652393a759e1036cc0ef0cc |
| 11 | f8772dd5aa4985305b4739b6595be648f180d2a91b1daf3ffeb754bf1634652b |
| 2 | 6ed9e8826b6917afade8428ad8ba0ef06fdbb723500482b53bce904f69e95014 |
| 3 | 4606a9bdca74892e9959452bafe144fe3a9c24d25b48c83ee961469221a4b4c3 |
| 4 | d6e7773c6a0320691ca4144299791249ce57839562905a9d2bf42783fba57b83 |
| 5d | e982db8b9a85a024643b90e1fd4ff9aa0bae6b0ae062976ded4ca6ac6ad90608 |
| 5e | 0762d68e00b9d72f8d0f0038205ed4ce3626ba29164c5743fb3d673cc4d286ef |
| 6 | cad5a8bc0186e5a8328d9258c8a59cf3c753e62139bbfa95bd1401f678c6ae9f |
| 8b | f37ae7398aeaf36cf6ae9c174f25eddea2a86520a9ebae710e9409ebdd492e16 |
| 8c | f3927965feffe5c4d545a8d22aa875f48c50dca2d93ac46b48927ae119914afc |
| 13 | 5ec0b95d053f64618438ffa170eb5d773bc79cca124dbc1894ba8cf15c5eb177 |
| 15 | c6bb971dc7274078a55bc63751971df545fef2da4dc66bef5bc451a43efaf514 |
| 16 | 80d2c5b8b5ff902688a6bcd2e62b2e8cb6714f9bd7a33369a99c44e1cd7f783d |
| 7 | f01dc441865ba4d227e6810328f38376b883f341b25679842cfe8a31fbf9aee0 |
| 8e | 5f6bb65fc20292add3f19c02137e4eab05e81a61f2a1e8da6bec29434b678658 |
| 9 | 6afefd4a342b5f5749c93d7aab8c5b7494cd95445e619cb164a79b29df97b69b |
| 10 | 320b71964696452137d0967c5995c1f6bc29fe3f800b4d8feff670ecdcf79f8a |
| 12 | 1bee613c59581de9dd126ac727c3517b6454fa12b56b5e4a76c0ec394a275b76 |
| 14 | d6f3486eacb02f6ccf83c804d55d314bc5451cf021becb040590566561e4e551 |
| 17 | f96a5dc36b9b3f79c767e4f47dc7def6aa85ad8444e5ae9d391c13b1faa7f15e |
| (rest of the document) | 4ab44412ed063c2bc602f385d7b58b759dbf415cd3a4e78f694db4b2cde08b0a |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 11 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 4 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 5d | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 6 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 8b | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 8c | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 13 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 15 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| 16 | 4f1feac5d6e8d0c8ced014ec9ec1c0520d621c094bff69b87ae11909945e2a46 |
| 12 | 415ba62a12f11e3e93618cc40ce554ccffc204554a9cb6ccc8d1c504bfc18800 |
| 14 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 17 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 07eff69e6904

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 4, 5d |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 07eff69e69040509d8fa2f28cbb87086de388dcfb5606a0c7b8c884520eec447 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f49e02aa20631125954867a4f0d29be66054e1f29b85b06f0270db173ed57c0c |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 572fdd13b89830690582e15658e1bfad745237ba6f497f7bdc97f0a52df8a507 |
| receipt | .transcription/sa.lines-d86999fd34e0 |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line11b, f1040.line12e, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: f2441.benefits, f2441.care, f2441.employer_care, f2441.line13, f2441.line14, f2441.nondependent, f2441.paid_2026, f2441.plan_max, f2441.plans_differ, f2441.prior_year, f2441.spouse_died, f2441.student_disabled | f2441 |
| named form, inputs and named lines: f4952.alternative_allocation, f4952.carryover, f4952.line1, f4952.line4g, f4952.prior_7, f4952.unsupported | f4952 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: s1.alimony, s1.alimony_paid, s1.alimony_received, s1.alimony_unsupported, s1.cod_amount, s1.cod_any, s1.cod_unsupported, s1.gambling_pro, s1.gambling_winnings, s1.jury_to_employer, s1.line1, s1.line17, s1.line21, s1.line8_other, s1.line8g, s1.line8h, s1.line8i, s1.line8j, s1.line8r, s1.line8z, s1.uc_paid, s1.uc_repaid, s1.uc_unsupported | s1 |
| named form, inputs and named lines: s1a.carloan, s1a.overtime, s1a.tips | s1a |
| named form, inputs and named lines: s3.line10, s3.line12, s3.line14 | s3 |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | eic, f8960, ltc, sli |
| shared page | f1095a, f8962, person, refund |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sa.line1
      take: sa.line3
  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr:
      op: sum
      of: [sa.line5a, sa.line5b, sa.line5c]
    note: "Line 5a on the form may hold either income taxes or general sales taxes (with the box checked). The supplied sa.line5a input covers income taxes only, and the sales-tax election is screened by sa.unsupported where line 5a is defined. Line 5d therefore adds the three supplied inputs and adds no refusal of its own."
```
```

#### Pass f56e521f4163

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 11, 6, 8b, 8c, 13, 15, 16, 12, 14, 17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f56e521f4163ee6d69adb3458698612214c289abdbd80cf7ddd3caeff819c7b6 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a4a61e01d3c14ae99d788bd3b4eb67402e6ec946ac8dc384922628841c44ac82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ff285ed95e2e80be2f82edc5fa8ade4696f8e7af4055996800e139385f1dcb81 |
| receipt | .transcription/sa.lines-c710487fe69e |
| printed lines compared | 10 |
| agree / disagree / missing | 9 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sca | 2025; printed date 2025-12-08 | 7, 9, 10, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 9, 10, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line11b, f1040.line12e, f1040.line1a, f1040.line25b, f1040.line25c, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: f4952.alternative_allocation, f4952.carryover, f4952.has_interest, f4952.line1, f4952.line4g, f4952.prior_7, f4952.unsupported | f4952 |
| named form, inputs and named lines: f8863.ban, f8863.paid | f8863 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: s3.line10, s3.line12, s3.line14 | s3 |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | eic, f5329, sli |
| shared page | gift, person, refund, s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero (no amount on the line for the supported cases)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sa.line11_if_gifts
    printed: "11"
    label: "Gifts by cash or check. If you made any gift of $250 or more, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.gifts, {const: true}]}
          then: sa.line11
        - guard: {op: test, eq: [sa.gifts, {const: false}]}
          then: sa.h_zero
    refuses: [sa.charity_limited]
    note: "The instructions say to enter the total value of cash or check gifts unless a limit on deducting gifts applies. If a limit applies, Pub. 526 figures the amount. This encoding supports only the unlimited case and refuses when sa.charity_limited is true. With no charitable contributions (sa.gifts false) the line is zero."

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "The instructions say line 6 holds foreign income taxes and generation-skipping tax. Both are outside scope (sa.unsupported), so the supported case is zero."

  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098. See instructions if limited. If paid to the person from whom you bought the home, see instructions and show that person's name, identifying no., and address"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "Mortgage interest not on Form 1098 is outside scope (sa.unsupported), so the supported case is zero."

  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098. See instructions for special rules"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "Points not on Form 1098 are outside scope (sa.unsupported), so the supported case is zero."

  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.charity_limited]
    note: "A charitable carryover from a prior year is covered by the sa.charity_limited screen. That screen asks about deductions reduced by income limits or carried over. The supported case is therefore zero."

  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form. See instructions"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "Any casualty or theft loss is outside scope (sa.unsupported), so the supported case is zero."

  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "The only supported item from the line 16 list is gambling losses. The instructions limit them to the gambling winnings reported on Schedule 1 (Form 1040), line 8b. Every other line 16 item, and any net qualified disaster loss or increased standard deduction reporting, is refused through sa.unsupported."

  - id: sa.h_gift_noncash_total
    printed: "(helper)"
    label: "Total deductible value of contributions of property other than by cash or check (Form 8283 groups)"
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}

  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made any gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.gifts, {const: true}]}
          then: sa.h_gift_noncash_total
        - guard: {op: test, eq: [sa.gifts, {const: false}]}
          then: sa.h_zero
    refuses: [sa.charity_limited]
    note: "The instructions say to enter the total value of contributions of property other than by cash or check unless a limit applies. This encoding reads each group's allowed amount (gift.allowed) and handles only the unlimited case. When a limit applies, sa.charity_limited refuses the line."

  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11_if_gifts, sa.line12, sa.line13]}

  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}
    note: "The far right column for lines 4 through 16 holds lines 4, 7, 10, 14, 15 and 16."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.agi
    printed: "(helper)"
    label: "Amount from Form 1040 or 1040-SR, line 11b (adjusted gross income)"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
    note: "Schedule A line 2 and the State and Local Tax Deduction Worksheet line 2 both read Form 1040 line 11b. This helper keeps the signed amount."

  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {const: 0}}
    note: "The IRS text does not say what to do when line 11b is negative. The required type is NonNegDollars, so a negative AGI is entered as zero. With a negative AGI the 7.5% floor on line 3 is then zero."

  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}

  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.line1, take: sa.line3}

  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5a, sa.line5b, sa.line5c]}
    refuses: [sa.unsupported]
    note: "The general sales tax election on line 5a is outside this tool (sa.unsupported). Line 5a is therefore always state and local income taxes."

  - id: sa.h_ws1
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
    note: "The worksheet is applied in every case. When line 5d is $10,000 or less ($5,000 MFS), the result is still line 5d, which matches the 'Before you begin' and line 1 'No' stops. When line 11b is not over the threshold, the result is still the smaller of line 5d or $40,000 ($20,000 MFS), which matches the line 5e instruction."

  - id: sa.h_ws4
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 4: Add lines 2 and 3e"
    type: Dollars
    expr: {op: copy, from: sa.agi}
    note: "Line 3e (excluded Puerto Rico, Form 2555 and Form 4563 income) is zero in scope, because those cases are refused (sa.excluded_income) on line 5e."

  - id: sa.h_ws5
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}

  - id: sa.h_ws6
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 6: If line 4 is more than line 5, subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_ws4, take: sa.h_ws5}
    note: "When line 4 is not more than line 5, the worksheet skips lines 7 and 8 and uses line 1. A zero here gives the same line 8."

  - id: sa.h_ws7
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_ws6, rate: {param: sa.salt_rate}}

  - id: sa.h_ws8
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 8: Subtract line 7 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_ws1, take: sa.h_ws7}
    note: "The worksheet prints a plain subtraction. Flooring at zero does not change line 9, which takes the larger of line 8 and $10,000."

  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_ws9
    printed: "(helper)"
    label: "SALT Deduction Worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_ws8, sa.h_salt_floor]}

  - id: sa.h_ws9_half
    printed: "(helper)"
    label: "Half the amount on line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_ws9, rate: {param: sa.half}}

  - id: sa.h_ws10_cap
    printed: "(helper)"
    label: "Amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_ws9_half
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_ws9

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.h_ws10_cap, sa.line5d]}
    refuses: [sa.excluded_income]
    note: "This is SALT Deduction Worksheet line 10: the smaller of line 9 (halved if MFS) or line 5d."

  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The catalog has no Schedule A zero parameter, so the declared zero-valued money parameter sales.zero is used."

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]
    note: "The only line 6 items in the text are foreign income taxes and the generation-skipping tax. Both are refused (sa.unsupported), so the computed case is zero."

  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.charity_limited]

  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form"
    type: NonNegDollars
    expr: {op: copy, from: sa.h_zero}
    refuses: [sa.unsupported]

  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions (gambling losses, but only to the extent of gambling winnings reported on Schedule 1, line 8b)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]

  - id: sa.line7
    printed: "7"
    label: "Add lines 5e and 6"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5e, sa.line6]}

  - id: sa.line8e
    printed: "8e"
    label: "Add lines 8a through 8c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8a, sa.line8b, sa.line8c]}
    refuses: [sa.unsupported]

  - id: sa.line9
    printed: "9"
    label: "Investment interest. Attach Form 4952 if required"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line8}
    note: "The Schedule A text supplied here says only 'Attach Form 4952 if required'. The deduction is read from Form 4952 line 8 (investment interest expense deduction). How investment interest is figured when Form 4952 is not required is not in the supplied pages."

  - id: sa.line10
    printed: "10"
    label: "Add lines 8e and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8e, sa.line9]}

  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made any gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}
    refuses: [sa.charity_limited]

  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
    refuses: [sa.charity_limited]

  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}

  - id: sa.h_tp_age
    printed: "(helper)"
    label: "Line 12d box: You were born before January 2, 1961"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, not: {op: test, eq: [person.died_before_65, {const: true}]}}
    note: "The text states the died-before-65 rule for a spouse and refers to Pub. 501 for a deceased taxpayer. The same rule (a person is not age 65 unless they reached it before death) is applied to the taxpayer's own box."

  - id: sa.h_tp_blind
    printed: "(helper)"
    label: "Line 12d box: You are blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.blind, {const: true}]}

  - id: sa.h_sp_age
    printed: "(helper)"
    label: "Line 12d box: Spouse was born before January 2, 1961"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, not: {op: test, eq: [person.died_before_65, {const: true}]}}

  - id: sa.h_sp_blind
    printed: "(helper)"
    label: "Line 12d box: Spouse is blind"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.blind, {const: true}]}

  - id: sa.h_tp_boxes
    printed: "(helper)"
    label: "Number of line 12d boxes checked for you"
    type: Count
    expr: {op: sum, of: [sa.h_tp_age, sa.h_tp_blind]}

  - id: sa.h_sp_boxes
    printed: "(helper)"
    label: "Number of line 12d boxes checked for your spouse"
    type: Count
    expr: {op: sum, of: [sa.h_sp_age, sa.h_sp_blind]}

  - id: sa.age65
    printed: "(helper)"
    label: "Any box checked on Form 1040 line 12d (born before January 2, 1961, or blind)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.h_tp_boxes, {const: 0, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, gt: [sa.h_sp_boxes, {const: 0, type: Count}]}
    note: "The pages do not define this interface. Read as Exception 4: whether any line 12d box (age or blindness) is checked, which is what selects the Standard Deduction Chart. Spouse boxes count only on a joint return. They are not checked for HOH, the QSS chart has no spouse rows, and MFS spouse boxes are refused (sa.spouse_extra)."

  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount per box checked ($2,000 single or head of household; $1,600 otherwise)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}

  - id: sa.h_tp_extra
    printed: "(helper)"
    label: "Additional standard deduction for your boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_tp_boxes}

  - id: sa.h_sp_extra_amt
    printed: "(helper)"
    label: "Additional standard deduction for your spouse's boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_sp_boxes}

  - id: sa.h_sp_extra
    printed: "(helper)"
    label: "Spouse's boxes counted (married filing jointly only)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfj"}]}
          then: sa.h_sp_extra_amt
        - guard: {op: test, ne: [f1040.status, {const: "mfj"}]}
          then: sa.h_zero
    refuses: [sa.spouse_extra]

  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for your filing status"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}

  - id: sa.h_std_chart
    printed: "(helper)"
    label: "Standard deduction (amount to the left of line 12e, or Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_tp_extra, sa.h_sp_extra]}
    note: "Base plus a per-box amount reproduces every row of the printed chart (for example single, 1 box: 15,750 + 2,000 = 17,750; MFS, 4 boxes: 15,750 + 6,400 = 22,150)."

  - id: sa.h_std
    printed: "(helper)"
    label: "Standard deduction (zero if your spouse itemizes on a separate return)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_std_chart
    refuses: [sa.dependent, sa.unsupported]
    note: "Exception 1 (dependent worksheet) and Exception 3 (dual-status alien) are refused by sa.dependent. Exception 5 (net qualified disaster loss) is refused by sa.unsupported."

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize deductions (Schedule A line 17 used on Form 1040 line 12e)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_std]}
    note: "The text says to take the larger of the standard or itemized deductions, or to itemize by election (line 18). When the two are equal the result is the same either way; the standard deduction is chosen. A MFS filer whose spouse itemizes is treated as itemizing, since that filer's standard deduction is zero."

  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions (Form 1040, line 12e)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_std
```
```
