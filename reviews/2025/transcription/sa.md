# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 4841ad6117034069e3611c615a8e96c7255cd9fa9417b770e8d823e858091780 |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | aa714bfc67d922bc0889d04176a4cd318e0a35c47af460b9e9fb5565a936a359 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | d19ac55850f1d8ef60a44b84476defa0db233b903176f18c1991c4688f0f7c68 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d10c9467bfa24ad06502ce549bd3362049153559d5a74950ef5289f3973ec7c1 |
| printed lines compared | 22 |
| agree / disagree / missing | 17 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
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
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "any"}
```

Second transcription's note: Open point: the pages do not define this interface. Chosen reading: true when any age box on line 12d (born before January 2, 1961) is checked for you or for a counted spouse. Blindness boxes are excluded.

Ruling: model error; f1040s1a, line 36a: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35", with the spouse on line 36b ("If you are married filing jointly, your spouse has a valid social security number ... and your spouse was born before January 2, 1961"); i1040gi p. 33, line 12d, likewise separates the boxes for you and for your spouse. sa.age65 is the question "Were you born before January 2, 1961?" for you alone (Schedule 1-A line 36a reads it); the candidate also counts the spouse (on a joint return, or MFS with spouse boxes). Triage executable-triage-v1 (triage/sa.json): 2,070 of 2,120 agree; all 50 differences are value, project False against candidate True, on joint returns where only the spouse was born before January 2, 1961 (classm.asset.1: taxpayer age65 false, spouse true; classm.otjob.1, classm.s1a.1, classm.sc.1, classm.scveh.4, classm.se.1), where the candidate would put the taxpayer's senior deduction on line 36a. The reviewer did not receive f1040s1a, but the interface label "Were you born before January 2, 1961?" and i1040gi p. 33 (given), which separates the boxes for you and for your spouse, decide the reading. Project stands.

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The instructions say the tax is in most cases less with the larger deduction. When the two are equal, the standard deduction is chosen unless the filer elects to itemize. The deduction amount is the same either way.

Ruling: model error; i1040sca p. 11, Other Itemized Deductions: "Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b", and Schedule A line 18: "If you elect to itemize deductions even though they are less than your standard deduction, check this box". The comparison itself matches the project (line 17 more than the standard deduction, or the election); the difference is in the line 17 the candidate builds, whose line 16 is smaller_of(sa.gambling_losses, s1.line8b) with no guard, so it needs the losses even when there are no winnings and the source fixes line 16 at zero (ruled at line 16). Triage executable-triage-v1 (triage/sa.json): 1,270 of 2,120 agree; the 790 candidate-unknown records stop on sa.gambling_losses with zero winnings (classm.f2441.1.deepseek to classm.f2441.6.deepseek recorded); the 59 candidate-refuses come from the candidate evaluating line 17 and the standard deduction where the project's election or the married-filing-separately rule decides first: on classm.carloan.4 (sb.line8) and classm.s1.3 (sb.unsupported) the project refuses sa.deduction through the same gates, and classm.f4952.3 and classm.tax_on_amount.2 (sa.dependent) are married filing separately with an itemizing spouse, a status every interview refuses (scope.ready, s3.mfs, i1040gi p. 14); the 1 project-refuses (stage4.refuse.standard.spouse_extra) is also MFS. Not exercised by the sample: the candidate counts the age box for a taxpayer who died in 2025 before reaching 65, which p501 p. 23 excludes ("the taxpayer isn't considered 65 or older at the end of 2025 unless the taxpayer was 65 or older at the time of death"); the project applies person.died_before_65 to every person. Project stands.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}], "op": "sum"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 34, Line 12e: "In most cases, your federal income tax will be less if you take the larger of your standard deduction or itemized deductions"; i1040sca p. 11: gambling losses "only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b". The choice between line 17 and the standard deduction is the same as the project's; the candidate's deduction depends on its own line 16, which needs sa.gambling_losses when the winnings are zero, so line 12e is unknown on returns the source fixes. Triage executable-triage-v1 (triage/sa.json): 1,285 of 2,120 agree; 799 candidate-unknown records stop on sa.gambling_losses (classm.f2441.1.deepseek: project $23,625.00; classm.f2441.2.deepseek: project $31,500.00); the 35 candidate-refuses are married filing separately with an itemizing spouse (classm.f4952.3, classm.tax_on_amount.2: project $50,000.00 against sa.dependent refusal), MFS being refused by every interview (scope.ready, s3.mfs), or stage-16 fixtures that omit sa.elect_itemize (stage16.cleanup.refuse.f4952_unsupported), and partial records the project also cannot finish; the 1 project-refuses is MFS (stage4.refuse.standard.spouse_extra). No value differences. Also not exercised: the candidate's age box for a taxpayer who died before 65 (p501 p. 23). Project stands.

### 2 — Amount from sa.agi_floor
Status: **AGREE**

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"param": "sa.salt_floor"}}, {"param": "sa.salt_floor"}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, "op": "subtract_floor0", "take": {"param": "sa.salt_floor"}}, {"param": "sa.salt_floor"}], "op": "sum"}}], "op": "choose"}], "op": "smaller_of"}
```

Second transcription's note: Worksheet line 1 enters $40,000 for every filing status and line 10 halves line 9 for MFS. This reproduces $20,000 and $5,000 for MFS. When line 11b is not above the threshold, the worksheet gives the smaller of line 5d or $40,000 ($20,000 MFS), which is the line 5e instruction, so a single computation serves both paths. The 'before you begin' shortcut (line 5d ≤ $10,000/$5,000) also gives the same result. Products are rounded half-up to the cent.

Ruling: scope; i1040sca p. 7, State and Local Tax Deduction Worksheet: "1. ... Enter $40,000", "5. Enter $500,000 ($250,000 if married filing separately)", "6. ... Skip lines 7 and 8 and enter the amount from line 1 on line 9", line 9 the larger of line 8 or $10,000. The candidate writes larger_of(line 8, $10,000) as $10,000 plus the excess of a signed line 8 over $10,000, which is the same amount, and halves it for MFS as the project does; the formulas agree on every return. The differences are refusals the candidate places on lines 5d and 5e (sa.unsupported, sa.excluded_income) where the project places them on lines 16 and 17 and sa.deduction. Triage executable-triage-v1 (triage/sa.json): 2,006 of 2,120 agree, no value differences; 52 candidate-refuses on sa.excluded_income (classm.retirement.3, classm.s179.3, stage12.excluded_income_no_claim) are returns on which the project refuses sa.line17 and Form 1040 line 12e through the same cited gate (checked on stage12.excluded_income_no_claim); 53 candidate-unknown are partial records withholding sa.unsupported, which every interview asks for line 17 (bases classm.f2441.1.deepseek, classm.f8889.2.deepseek, classm.f4952.2); 9 project-refuses are foreign cited gates reached through f1040.line11b (f8889 unsupported, retirement special, sales digital, sb.form8938) on records that omit or withhold sa.excluded_income, where the candidate stops first on its own gate. Project stands.

### 6 — Amount from sa.zero
Status: **AGREE**

### 8b — Amount from sa.zero
Status: **AGREE**

### 8c — Amount from sa.zero
Status: **AGREE**

### 13 — Amount from sa.zero
Status: **AGREE**

### 15 — Amount from sa.zero
Status: **AGREE**

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

Second transcription's note: Only gambling losses are supported: 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b.' Other line 16 items and a net qualified disaster loss are screened by sa.unsupported.

Ruling: model error; i1040sca p. 11, Other Itemized Deductions: "Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b". With no winnings line 16 is zero whatever the losses, so sa.gambling_losses is not needed; the project asks it only when s1.gambling_winnings is positive, the reading chosen in amb.2025.gambling_losses ("with no winnings it is zero and the losses are not asked"). The candidate's unguarded smaller_of needs the losses on every return; complete-record arithmetic agrees, availability does not. Triage executable-triage-v1 (triage/sa.json): 879 of 2,120 agree; 1,116 candidate-unknown records have no winnings and no losses answer (classm.f2441.1.deepseek to .6.deepseek recorded, project $0.00); 91 project-refuses and 34 project-unknown come from the project also declaring sa.charity_limited and sa.excluded_income on line 16 (classm.f8606.1, classm.refund.1: charity_limited; classm.s179.3: excluded_income; partials withholding those screens from classm.f8889.2.deepseek, classm.f5695.3), screens line 17 declares too, so Schedule A and line 12e are refused on the same returns either way (scope). Project stands.

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **AGREE**

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits
Status: **AGREE**

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sa.itemizes | sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | - |
| sa.deduction | sa.charity_limited, sa.dependent, sa.excluded_income, sa.unsupported | - |
| 5d | sa.unsupported | sa.unsupported |
| 5e | sa.excluded_income, sa.unsupported | sa.unsupported |
| 6 | sa.unsupported | - |
| 8b | sa.unsupported | - |
| 8c | sa.unsupported | - |
| 13 | sa.charity_limited | - |
| 15 | sa.unsupported | - |
| 16 | sa.unsupported | - |
| 7 | sa.excluded_income, sa.unsupported | - |
| 8e | sa.unsupported | - |
| 10 | sa.unsupported | - |
| 14 | sa.charity_limited | - |
| 17 | sa.charity_limited, sa.excluded_income, sa.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.agi
    printed: "(helper)"
    label: "Amount from Form 1040 or 1040-SR, line 11b (adjusted gross income)"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
    note: "Interface sa.agi is read as the Form 1040 line 11b amount that Schedule A line 2 and the SALT worksheet line 2 tell the filer to enter."

  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {const: 0}}
    note: "Open point: the form says to copy line 11b, which can be negative, but this line must be NonNegDollars. Chosen reading: a negative line 11b is entered as zero, so line 3 is zero and line 4 equals line 1."

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
    note: "The sales-tax election on line 5a is outside scope. It is screened by sa.unsupported."

  - id: sa.h_salt_threshold
    printed: "(helper)"
    label: "SALT worksheet line 5: Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}

  - id: sa.h_salt_excess
    printed: "(helper)"
    label: "SALT worksheet line 6: If line 4 is more than line 5, subtract line 5 from line 4 (otherwise skip lines 7 and 8)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_threshold}
    note: "Worksheet line 4 is line 2 plus line 3e. Lines 3a to 3d are excluded income from Puerto Rico, Form 2555 and Form 4563, which are refused at line 5e (sa.excluded_income), so line 3e is zero here. Skipping lines 7 and 8 and entering line 1 on line 9 gives the same result as a zero excess, because larger_of(line 1, $10,000) equals line 1."

  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "SALT worksheet line 7: Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_excess, rate: {param: sa.salt_rate}}

  - id: sa.h_salt_line1
    printed: "(helper)"
    label: "SALT worksheet line 1: Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}

  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT worksheet line 8: Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_salt_line1, take: sa.h_salt_line7}

  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT worksheet line 9 floor: $10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}

  - id: sa.h_salt_over_floor
    printed: "(helper)"
    label: "Excess of worksheet line 8 over $10,000, if any"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_line8, take: sa.h_salt_floor}

  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT worksheet line 9: Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_salt_floor, sa.h_salt_over_floor]}
    note: "The sum $10,000 + max(line 8 − $10,000, 0) is written instead of larger_of so the result is provably nonnegative. It equals the larger of line 8 or $10,000."

  - id: sa.h_salt_line9_half
    printed: "(helper)"
    label: "Half the amount on worksheet line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}

  - id: sa.h_salt_cap
    printed: "(helper)"
    label: "SALT worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9_half
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9

  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.h_salt_cap]}
    refuses: [sa.excluded_income]
    note: "Worksheet line 1 enters $40,000 for every filing status and line 10 halves line 9 for MFS. This reproduces $20,000 and $5,000 for MFS. When line 11b is not above the threshold, the worksheet gives the smaller of line 5d or $40,000 ($20,000 MFS), which is the line 5e instruction, so a single computation serves both paths. The 'before you begin' shortcut (line 5d ≤ $10,000/$5,000) also gives the same result. Products are rounded half-up to the cent."

  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "Line 6 items (foreign income taxes, GST) are outside scope and screened by sa.unsupported. In the supported case the amount is zero."

  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]

  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]

  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.charity_limited]

  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]

  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "Only gambling losses are supported: 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b.' Other line 16 items and a net qualified disaster loss are screened by sa.unsupported."

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

  - id: sa.line9
    printed: "9"
    label: "Investment interest. Attach Form 4952 if required. See instructions"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line8}
    note: "The Schedule A pages given do not state the source amount. Chosen reading: the investment interest expense deduction figured on Form 4952 (line 8)."

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

  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: sa.h_age_tp
    printed: "(helper)"
    label: "Line 12d box checked: You were born before January 2, 1961"
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

  - id: sa.h_blind_tp
    printed: "(helper)"
    label: "Line 12d box checked: You are blind"
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

  - id: sa.h_age_sp
    printed: "(helper)"
    label: "Line 12d box checked: Spouse was born before January 2, 1961 (not checked if the spouse died in 2025 before reaching age 65)"
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
          - {op: test, eq: [person.died_before_65, {const: false}]}
    note: "The died-before-65 rule is applied to the spouse box only, as the text states it. For a deceased taxpayer the text refers to Pub. 501, which is not provided."

  - id: sa.h_blind_sp
    printed: "(helper)"
    label: "Line 12d box checked: Spouse is blind"
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

  - id: sa.h_spouse_counted
    printed: "(helper)"
    label: "Spouse boxes on line 12d may be counted (joint return, or married filing separately with a spouse who had no income, isn't filing and can't be claimed as a dependent)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfs"}]}
            - {op: test, eq: [sa.spouse_extra, {const: true}]}
    note: "Spouse boxes are not counted for head of household ('Don't check any boxes for your spouse'), nor for qualifying surviving spouse, whose chart rows stop at 2 boxes."

  - id: sa.age65
    printed: "(helper)"
    label: "A line 12d box for birth before January 2, 1961 is checked (you, or your spouse where spouse boxes count)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.h_age_tp, {const: 0, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [sa.h_spouse_counted, {const: true}]}
            - {op: test, gt: [sa.h_age_sp, {const: 0, type: Count}]}
    note: "Open point: the pages do not define this interface. Chosen reading: true when any age box on line 12d (born before January 2, 1961) is checked for you or for a counted spouse. Blindness boxes are excluded."

  - id: sa.h_extra
    printed: "(helper)"
    label: "Additional amount per box checked on line 12d ($2,000 single or head of household; $1,600 otherwise)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}

  - id: sa.h_amt_age_tp
    printed: "(helper)"
    label: "Additional amount for your age box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_extra, count: sa.h_age_tp}

  - id: sa.h_amt_blind_tp
    printed: "(helper)"
    label: "Additional amount for your blindness box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_extra, count: sa.h_blind_tp}

  - id: sa.h_amt_age_sp
    printed: "(helper)"
    label: "Additional amount for spouse age box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_extra, count: sa.h_age_sp}

  - id: sa.h_amt_blind_sp
    printed: "(helper)"
    label: "Additional amount for spouse blindness box"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_extra, count: sa.h_blind_sp}

  - id: sa.h_sp_extra
    printed: "(helper)"
    label: "Additional amounts for spouse boxes"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_amt_age_sp, sa.h_amt_blind_sp]}

  - id: sa.h_sp_counted_amt
    printed: "(helper)"
    label: "Additional amounts for spouse boxes, where spouse boxes may be checked"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_spouse_counted, {const: true}]}
          then: sa.h_sp_extra
        - guard: {op: test, eq: [sa.h_spouse_counted, {const: false}]}
          then: sa.h_zero

  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for filing status ($15,750 single or MFS; $31,500 MFJ or QSS; $23,625 HOH)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}

  - id: sa.h_std_figured
    printed: "(helper)"
    label: "Standard deduction from the amounts by line 12e or the Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_amt_age_tp, sa.h_amt_blind_tp, sa.h_sp_counted_amt]}
    note: "The chart is reproduced as base + boxes × per-box amount. This was checked against every chart row (for example single 1 box $17,750, MFJ 4 boxes $37,900, MFS 4 boxes $22,150, HOH 2 boxes $27,625)."

  - id: sa.h_standard
    printed: "(helper)"
    label: "Standard deduction (zero if line 12b is checked: married filing separately and spouse itemizes)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [f1040.status, {const: "mfs"}]}
              - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [f1040.status, {const: "mfs"}]}
                - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_std_figured
    refuses: [sa.dependent, sa.unsupported]
    note: "Exceptions 1 and 3 (a dependent, which uses the dependent worksheet, and a dual-status alien) are screened by sa.dependent. Exception 5 (net qualified disaster loss) is screened by sa.unsupported."

  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize: itemized deductions (line 17) are larger than the standard deduction, or line 18 election to itemize"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sa.line17, sa.h_standard]}
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
    note: "The instructions say the tax is in most cases less with the larger deduction. When the two are equal, the standard deduction is chosen unless the filer elects to itemize. The deduction amount is the same either way."

  - id: sa.deduction
    printed: "(helper)"
    label: "Form 1040 line 12e: standard deduction or itemized deductions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_standard
```
```
