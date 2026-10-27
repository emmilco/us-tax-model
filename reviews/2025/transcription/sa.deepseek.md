# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 26b6b60f8c435820d64b82520f456c27306e4a1f90d81884709f51834760742c |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | aa714bfc67d922bc0889d04176a4cd318e0a35c47af460b9e9fb5565a936a359 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | acb075f8352feaa2f85ed1ec513962a391814d7d26b3f7e77fea7b3671e4261a |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d10c9467bfa24ad06502ce549bd3362049153559d5a74950ef5289f3973ec7c1 |
| printed lines compared | 22 |
| agree / disagree / missing | 15 / 7 / 0 |
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
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}], "test": "lt"}
```

Second transcription's note: Counts person.age65 entries in the person collection; an MFS spouse covered only by sa.spouse_extra is not counted.

Ruling: model error; f1040s1a, line 36a: "If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35", with the spouse on line 36b ("If you are married filing jointly, your spouse has a valid social security number ... and your spouse was born before January 2, 1961"); i1040gi p. 33, line 12d, likewise separates the boxes for you and for your spouse. sa.age65 is the question "Were you born before January 2, 1961?" for you alone (Schedule 1-A line 36a reads it); the candidate also counts the spouse, counting any person entry with person.age65. Triage executable-triage-v1 (triage/sa.deepseek.json): 2,066 of 2,120 agree; all 54 differences are value, project False against candidate True, on joint returns where only the spouse was born before January 2, 1961 (classm.asset.1, classm.otjob.1, classm.s1a.1, classm.sc.1, classm.scveh.4, classm.se.1). The reviewer did not receive f1040s1a, but the interface label "Were you born before January 2, 1961?" and i1040gi p. 33 (given), which separates the boxes for you and for your spouse, decide the reading. Project stands.

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
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Ruling: model error; i1040gi p. 33, Line 12d: check "the appropriate box(es)" for each of you and your spouse born before January 2, 1961 or blind, and "Death of spouse in 2025. If your spouse was born before January 2, 1961, but died in 2025 before reaching age 65, don't check the box" (p501 p. 23 says the same of a deceased taxpayer). The candidate's standard deduction counts people with age65 or blind rather than boxes (one amount for a person who is both), ignores person.died_before_65, and is compared with its own line 17, whose line 9 copies Form 4952 line 7 (the carryforward), whose line 12 is zero and whose line 16 needs gambling losses with no winnings (each ruled at its line). It also declares sa.dependent on this line even when the filer elects to itemize. Triage executable-triage-v1 (triage/sa.deepseek.json): 1,178 of 2,120 agree; 13 value differences; the recorded ones trace to the candidate's line 17 (generated 7: candidate line 9 $9,504.86 from f4952.line7 makes itemized $38,468.43 exceed the $33,100.00 standard, project False against candidate True; generated 27: line 9 again; generated 15 and 277: candidate line 12 zero leaves line 14 at $0.02 and $11,303.63, project True against candidate False); 814 candidate-unknown stop on sa.gambling_losses (classm.f2441.1.deepseek and others); 43 candidate-refuses are sa.dependent (classm.carloan.4, classm.f4952.3, classm.s1.3, generated 53, 131); 69 project-refuses are cited gates on noncash gifts and Schedule B reached through the project's line 12 or line 17 that the candidate never reads (classm.asset.3 sb.unsupported, classm.ltc.2 gift section_b, classm.eic.5 gift special), and the project-unknown 3 are partials withholding screens every interview asks (classm.dependent.2). Project stands.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_extra"}], "test": "eq"}, "then": {"param": "sa.standard_extra"}}], "op": "choose"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}], "test": "any"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 34, Line 12e: "your federal income tax will be less if you take the larger of your standard deduction or itemized deductions", with the line 12d box rules (p. 33) setting the standard deduction. The selection mirrors the project's, but both of the candidate's amounts are wrong as ruled at sa.itemizes (box count by person, no died-before-65 rule, its own lines 9, 12 and 16). Triage executable-triage-v1 (triage/sa.deepseek.json): 987 of 2,120 agree; 226 value differences (classm.f8889.1.deepseek: project $48,700.40 against $47,246.40, the candidate's line 12 dropping $1,454.00 of noncash gifts; classm.f8889.2.deepseek $59,201.00 against $55,572.00; classm.f5695.1 $56,191.00 against $57,565.00 from its line 9); 823 candidate-unknown on sa.gambling_losses; 32 candidate-refuses on sa.dependent or screens withheld in partial records; 52 project-refuses are cited noncash-gift gates (stage4.refuse.gift.sectionB, stage4.refuse.gift.special, generated 24) and MFS (stage4.refuse.standard.spouse_extra). Project stands.

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
{"alternatives": [{"guard": {"args": [{"ref": "f1040.line11b"}, {"param": "sa.salt_threshold"}], "test": "le"}, "then": {"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"param": "sa.salt_threshold"}, {"ref": "f1040.line11b"}], "test": "lt"}, "then": {"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"param": "sa.salt_base"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sa.salt_base"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: The worksheet's excluded-income lines 3a-3d are unavailable; sa.excluded_income true refuses. Otherwise line 4 is AGI.

Ruling: model error; i1040sca p. 7, State and Local Tax Deduction Worksheet: "1. ... Enter $40,000" for every filing status, with the halving for married filing separately applied once to the line 9 result. For MFS the candidate halves $40,000 at line 1 and then halves line 9 again, so an MFS filer over $250,000 is held to $5,000. For every other status the candidate's formula equals the project's (smaller of line 5d and $40,000 at or below $500,000; larger of $40,000 less 30% of the excess and $10,000 above). Triage executable-triage-v1 (triage/sa.deepseek.json): 2,032 of 2,120 agree; the 4 value differences are all MFS (stage4.salt.mfs: project $12,500.00 against $5,000.00; generated 129: $9,163.45 against $5,000.00; generated 157: $15,932.15 against $5,932.15; generated 308: $10,863.04 against $6,991.08), a status every interview refuses (scope.ready, s3.mfs, i1040gi p. 14), so no in-scope printed amount differs; 51 candidate-refuses on sa.excluded_income are returns the project refuses at line 17 and line 12e through the same gate; 24 candidate-unknown are partials withholding sa.excluded_income, asked by every interview; 9 project-refuses are foreign cited gates reached through f1040.line11b on records that omit or withhold sa.excluded_income. Project stands.

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

Second transcription's note: Only gambling losses are supported, limited to gambling winnings on Schedule 1 line 8b; other line 16 items are refused by sa.unsupported.

Ruling: model error; i1040sca p. 11, Other Itemized Deductions: "Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b". With no winnings line 16 is zero whatever the losses; the project asks sa.gambling_losses only when s1.gambling_winnings is positive (amb.2025.gambling_losses, chosen reading: "with no winnings it is zero and the losses are not asked"), while the candidate's unguarded smaller_of needs it on every return. Triage executable-triage-v1 (triage/sa.deepseek.json): 879 of 2,120 agree; 1,116 candidate-unknown records have no winnings (classm.f2441.1.deepseek to .6.deepseek recorded, project $0.00); 91 project-refuses and 34 project-unknown come from the project's line 16 also declaring sa.charity_limited and sa.excluded_income (classm.f8606.1, classm.s179.3; partials from classm.f8889.2.deepseek, classm.f5695.3), screens line 17 declares too, so Schedule A is refused on the same returns either way (scope). Project stands.

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **DISAGREE**

Project:

```json
{"ref": "f4952.line8"}
```

Second:

```json
{"ref": "f4952.line7"}
```

Second transcription's note: The archived text only says attach Form 4952; the amount is taken from Form 4952 line 7 as the investment interest deduction.

Ruling: interface gap; f4952 (2025): line 7, "Disallowed investment interest expense to be carried forward to 2026. Subtract line 6 from line 3"; line 8, "Investment interest expense deduction. Enter the smaller of line 3 or line 6"; i1040sca p. 9, Line 9: "Complete and attach Form 4952 to figure your deduction". The deduction on Schedule A line 9 is Form 4952 line 8, as the project has it; the candidate copies line 7, the carryforward. The log's Source pages table shows the reviewer received f1040sa p. 1, i1040gi pp. 33–35, i1040sca pp. 1, 7, 11 and p525 p. 33: no Form 4952 page and not i1040sca p. 9, and the published interface lists f4952.line7 and f4952.line8 with no labels, so the text that decides between them was not available to the candidate (its note: "The archived text only says attach Form 4952"). Triage executable-triage-v1 (triage/sa.deepseek.json): 1,485 of 2,120 agree; all 635 differences are value (classm.f8889.2.deepseek: project $3,629.00 against $0.00; classm.f4952.1: $0.00 against $2,691.00; classm.f4562.1: $7,843.00 against $0.00; classm.f5695.2: $64.00 against $4,928.00). The candidate reading is wrong on the source; the gap is in the review packet (missing page and unlabeled interface entries). Project stands.

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits
Status: **DISAGREE**

Project:

```json
{"collection": "gift", "field": "gift.allowed", "op": "sum_over", "where": null}
```

Second:

```json
{"const": 0}
```

Second transcription's note: No noncash charitable gift input is provided in this closed interface; entered as zero.

Ruling: model error; i1040sca p. 10, Line 12: "Enter on line 12 the total value of your contributions of property other than by cash or check unless a limit on deducting gifts applies to you". The published interface the candidate received includes the gift collection (one entry per Form 8283 group, with gift.deduction and gift.allowed), so its note that no noncash gift input exists is wrong and its constant zero drops every noncash gift. Triage executable-triage-v1 (triage/sa.deepseek.json): 1,367 of 2,120 agree; 401 value differences, project positive against candidate $0.00 (classm.f8889.1.deepseek $1,454.00; classm.asset.2 $7,480.00; classm.f5695.3 $9,258.00); 197 project-refuses are cited gift and Schedule A screens (gift section_b, gift special, sa.unsupported, sa.charity_limited, sa.excluded_income: classm.carloan.4, classm.f8606.1, classm.dcprov.1); 155 project-unknown are fixtures omitting sa.unsupported, which every interview asks for line 17 (classm.f8889.3, stage16.cleanup.refuse.f1040_line16). i1040sca p. 10 was not among the pages given, but the printed Schedule A line 12 and the published gift collection were, so this is not an interface gap. Project stands.

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
| 5e | sa.excluded_income | - |
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
lines:
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: {const: 0}}
    note: "AGI is copied as Dollars; line 2 is declared NonNegDollars, so a negative AGI is floored at zero."
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
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.h_salt_over, {const: true}]}
          then: sa.h_salt_worksheet
        - guard: {op: test, eq: [sa.h_salt_over, {const: false}]}
          then: sa.h_salt_simple
    refuses: [sa.excluded_income]
    note: "The worksheet's excluded-income lines 3a-3d are unavailable; sa.excluded_income true refuses. Otherwise line 4 is AGI."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount:"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "The screening input sa.unsupported combines several unsupported Schedule A items; any yes refuses here. Otherwise no other taxes are in this slice."
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098. See instructions if limited. If paid to the person from whom you bought the home, see instructions and show that person’s name, identifying no., and address"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "No non-1098 mortgage interest input; unsupported by sa.unsupported."
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098. See instructions for special rules"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "No non-1098 points input; unsupported by sa.unsupported."
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.charity_limited]
    note: "Carryover is outside the supported slice; zero when sa.charity_limited is false."
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form. See instructions"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sa.unsupported]
    note: "Casualty losses are unsupported; zero otherwise."
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount:"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "Only gambling losses are supported, limited to gambling winnings on Schedule 1 line 8b; other line 16 items are refused by sa.unsupported."
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
    expr: {op: copy, from: f4952.line7}
    note: "The archived text only says attach Form 4952; the amount is taken from Form 4952 line 7 as the investment interest deduction."
  - id: sa.line10
    printed: "10"
    label: "Add lines 8e and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8e, sa.line9]}
  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made a gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "No noncash charitable gift input is provided in this closed interface; entered as zero."
  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}
  - id: sa.agi
    printed: "(helper)"
    label: "Adjusted gross income from Form 1040 line 11b"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.age65
    printed: "(helper)"
    label: "Any person in the person collection is age 65 or older"
    type: Bool
    expr: {op: test, gt: [sa.h_age65_count, {const: 0, type: Count}]}
    note: "Counts person.age65 entries in the person collection; an MFS spouse covered only by sa.spouse_extra is not counted."
  - id: sa.itemizes
    printed: "(helper)"
    label: "Whether the taxpayer itemizes deductions"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_std]}
    refuses: [sa.dependent]
  - id: sa.deduction
    printed: "(helper)"
    label: "Deduction amount, either itemized deductions or the standard deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.itemizes, {const: true}]}
          then: sa.line17
        - guard: {op: test, eq: [sa.itemizes, {const: false}]}
          then: sa.h_std
    refuses: [sa.dependent]
  - id: sa.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: sa.h_salt_base_full
    printed: "(helper)"
    label: "SALT worksheet line 1 base amount before MFS halving"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
  - id: sa.h_salt_base_mfs
    printed: "(helper)"
    label: "SALT worksheet line 1 base amount for MFS"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_base_full, rate: {param: sa.half}}
  - id: sa.h_salt_base_status
    printed: "(helper)"
    label: "SALT worksheet line 1 base amount for the filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_base_mfs
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_base_full
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "SALT worksheet line 9 minimum floor"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt_threshold
    printed: "(helper)"
    label: "SALT worksheet line 5 threshold for the filing status"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
  - id: sa.h_salt_simple
    printed: "(helper)"
    label: "SALT limit when AGI does not exceed the threshold"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.h_salt_base_status]}
  - id: sa.h_salt_line6
    printed: "(helper)"
    label: "SALT worksheet line 6, excess of AGI over threshold"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.agi, take: sa.h_salt_threshold}
  - id: sa.h_salt_line7
    printed: "(helper)"
    label: "SALT worksheet line 7, 30% of line 6"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line6, rate: {param: sa.salt_rate}}
  - id: sa.h_salt_line8
    printed: "(helper)"
    label: "SALT worksheet line 8, line 1 reduced by line 7, not below zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt_base_status, take: sa.h_salt_line7}
  - id: sa.h_salt_line9
    printed: "(helper)"
    label: "SALT worksheet line 9, larger of line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt_line8, sa.h_salt_floor]}
  - id: sa.h_salt_line9_half
    printed: "(helper)"
    label: "Half of SALT worksheet line 9 for MFS"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt_line9, rate: {param: sa.half}}
  - id: sa.h_salt_line9_status
    printed: "(helper)"
    label: "SALT worksheet line 9 amount after MFS halving"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9_half
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sa.h_salt_line9
  - id: sa.h_salt_worksheet
    printed: "(helper)"
    label: "SALT worksheet line 10 limit"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.h_salt_line9_status, sa.line5d]}
  - id: sa.h_salt_over
    printed: "(helper)"
    label: "Whether AGI exceeds the SALT worksheet threshold"
    type: Bool
    expr: {op: test, gt: [sa.agi, sa.h_salt_threshold]}
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction base amount for the filing status"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}
  - id: sa.h_std_extra_per
    printed: "(helper)"
    label: "Standard deduction additional amount per age or blindness box"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
  - id: sa.h_box_count
    printed: "(helper)"
    label: "Number of age 65 or blind boxes in the person collection"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        any:
          - {op: test, eq: [person.age65, {const: true}]}
          - {op: test, eq: [person.blind, {const: true}]}
  - id: sa.h_age65_count
    printed: "(helper)"
    label: "Number of age 65 persons in the person collection"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.age65, {const: true}]}
  - id: sa.h_std_extra_amount
    printed: "(helper)"
    label: "Standard deduction additional amount for person-collection boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra_per, count: sa.h_box_count}
  - id: sa.h_spouse_extra_amount
    printed: "(helper)"
    label: "Standard deduction additional amount for an MFS spouse"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_extra, {const: true}]}
          then: sa.h_std_extra_per
        - guard: {op: test, eq: [sa.spouse_extra, {const: false}]}
          then: sa.h_zero
    note: "sa.spouse_extra is a single Bool; when true, one extra amount is added. If the spouse has both age and blindness boxes, an additional extra amount may be required."
  - id: sa.h_std_before_spouse_itemizes
    printed: "(helper)"
    label: "Standard deduction before applying the spouse-itemizes exception"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_extra_amount, sa.h_spouse_extra_amount]}
  - id: sa.h_std
    printed: "(helper)"
    label: "Standard deduction for comparison with itemized deductions"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}
          then: sa.h_zero
        - guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}
          then: sa.h_std_before_spouse_itemizes
    refuses: [sa.dependent]
    note: "Dependent or dual-status cases are refused via sa.dependent; the dependent standard deduction worksheet is not computed."
```
