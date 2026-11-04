# Transcription agreement — sli

Second transcription of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` by an isolated model (spec 6.5), compared line by line with `forms/2025/sli.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4ba7aa15f66ede9994f45c36c46d6906223df273c128f02daa15a0f90fef6db0 |
| subject sha256 | ff76da6d126a9abdc6f51becc98940ac3a40b516122237f06b10ea1df0276faf |
| printed lines compared | 9 |
| agree / disagree / missing | 4 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sli.deduction — Student loan interest deduction (Schedule 1, line 21)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "sli.interest"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"input": "sli.interest"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.sav_claimed"}], "test": "eq"}}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.sav_claimed"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"line": "9"}}], "op": "choose"}
```

Second transcription's note: The line 21 instructions allow the deduction only if the filing status is not married filing separately, so this result is zero for MFS and line 9 otherwise. The instructions also require that neither you nor your spouse (if filing jointly) is claimed as a dependent on someone else's return. No interface input says whether the filer is actually claimed. The closest screening input, sa.dependent, asks whether someone can claim you or your spouse, and it excludes a person who could claim you but does not file or files only for a refund. I chose to refuse on it rather than invent an input. This is broader than the IRS condition: it also refuses a filer who could be claimed but is not. The modified AGI limit ($100,000, or $200,000 MFJ) needs no separate test, because lines 4 to 8 already reduce the deduction to zero at those amounts.

Ruling: model error; i1040gi p. 98, Line 21: "You, or your spouse if filing jointly, aren’t claimed as a dependent on someone else's (such as your parent’s) 2025 tax return." The condition is being claimed, not being claimable. The reply's note says no interface input says whether the filer is actually claimed and refuses on sa.dependent (who can claim you) instead; but person.sav_claimed ("Are you claimed as a dependent on someone else's 2025 tax return?") was in the request (collection person, entry fields), and the project counts it (sli.claimed_count, BUG-0402/T-215 round-2 change). The reply therefore refuses a filer who could be claimed but is not, whom the project computes, and enters line 9 instead of zero for no return (an actually claimed filer is also claimable, so the reply refuses). The dropped interest-above-zero guard changes no value (line 9 is zero without interest). Project stands.
Reviewed in: pass bf573de94e42

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **AGREE**
Reviewed in: pass bf573de94e42

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **AGREE**

### 4 — Subtract line 3 from line 2
Status: **AGREE**

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "sli.base_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.base_joint"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.base_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sli.base_other"}}], "op": "choose"}
```

Second transcription's note: Open: the line 5 table lists no amount for married filing separately. Chosen: every status other than married filing jointly uses $85,000. A married filing separately filer gets no deduction, which sli.deduction enforces, so this amount does not affect the result for that filer.

Ruling: representation; project retained. The worksheet gives no amount for married filing separately, which cannot take the deduction; the project enters zero there and the second enters $85,000. Neither reaches Schedule 1 line 21: sli.deduction is zero for married filing separately.

### 6 — Subtract line 5 from line 4
Status: **DISAGREE**

Project:

```json
{"from": {"line": "4"}, "op": "subtract", "take": {"line": "5"}}
```

Second:

```json
{"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "5"}}
```

Second transcription's note: The text says: 'Is the amount on line 4 more than the amount on line 5? No. Skip lines 6 and 7, enter -0- on line 8.' Chosen: line 6 is floored at zero. A zero line 6 makes the prorated line 8 zero, which matches the No branch.

Ruling: equivalent; project retained. Line 6 is used only when line 4 is more than line 5 (line 8 skips it otherwise), where the signed difference and the floored one are the same.

### 8 — Multiply line 1 by line 7
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "4"}, {"line": "5"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "5"}, {"line": "4"}], "test": "lt"}, "then": {"amount": {"line": "1"}, "op": "prorate", "part": {"line": "6"}, "places": 3, "whole": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "sli.divisor_other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.divisor_joint"}}], "op": "choose"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "1"}, "op": "prorate", "part": {"line": "6"}, "places": 3, "whole": {"alternatives": [{"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "sli.divisor_joint"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "sli.divisor_other"}}], "op": "choose"}}
```

Second transcription's note: Line 7 ('Divide line 6 by $15,000 ($30,000 if married filing jointly). Enter the result as a decimal (rounded to at least three places). If the result is 1.000 or more, enter 1.000') is folded into this prorate. Open: 'at least three places' does not fix the number of places. Chosen: exactly three places, rounded half-up.

Ruling: equivalent; project retained. The project skips to zero when line 4 is not more than line 5, as the worksheet says; the second always applies the ratio, which then has a part of zero or less, and prorate keeps the ratio at 0 or more, so it also gives zero (the same argument as the classified mutant on sli.line8).

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **DISAGREE**

Project:

```json
{"from": {"line": "1"}, "op": "subtract_floor0", "take": {"line": "8"}}
```

Second:

```json
{"from": {"line": "1"}, "op": "subtract", "take": {"line": "8"}}
```

Second transcription's note: The Exception says to use Pub. 970 instead of this worksheet if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico. The tool refuses at this line on screening input sa.excluded_income.

Ruling: equivalent; project retained. Line 8 never exceeds line 1: prorate's ratio is at most 1.000 (Lean lemma prorate_le_amount), so the floor at zero never applies.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sli.deduction | sa.dependent, sa.excluded_income | sa.dependent |
| 1 | sa.excluded_income | - |
| 9 | sa.excluded_income | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sli.deduction | 5dc3bc4b5657270a8a63c809ebf0defda8260efc682ae6a295e635fe8b92cf09 |
| 1 | 9b632db546bab24340697ef374a897d9698c216ccb8b93e5846732a6e18c6cb1 |
| 2 | 15ebca49b82ea0ae3cf755e0eb28d25ad933c055f37a808b67670a19a74f58f1 |
| 3 | 4be66246618cf1e7c9e0d68e53afc47d42cd6e8f9ae47ed623990aa08f669938 |
| 4 | 0a12f16437423be4047991e4de990d68f3d404b3a72951ce03c5b55cfb53f3e7 |
| 5 | f001a24c3d30610253a45be4a49495231cf2dd5fcc9b724be33b8cd5bf5e61fc |
| 6 | 762453cc63a7d9e7a683eb56cc07dee3d62fa8ed23cdf3f1f1fbf9b3148da363 |
| 8 | 047e92e0e2de34e255cfc50ebc39a056183d87f4aa7e395c00f883174a007a82 |
| 9 | e1b832d1d41301a4108d3bbf0de6dbf1afe43718787a9e871d45c94ef1f6e84d |
| (rest of the document) | f609488fedc80a710439a4e78c1579962a31f901a5d1f647b4ec0a725e858393 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sli.deduction | 5e71e09486b3638eef1ca7ad68c53ea93594179c3192bf31e4e4b3916035bc7d |
| 1 | 858fe29eeecfc7e735a4186d6ac0601622fb726b32d175e564be98b0c47a1478 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass bf573de94e42

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sli.deduction, 1 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bf573de94e42f23c6c2a7ac44c06362048bf06c14fcf009271878b7135b8448b |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ca7eb86377ebe60f31f76105f4f0e66b5dba7707f71b13d581ccef6976f0d88e |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7b50929e44b5fcc7287996ec8b42c58a0071256e63acb4d22f10acaabe2ea312 |
| receipt | .transcription/sli.lines-b2eae3131c48 |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, f8606, household, sa, scope |
| named line | f8960, interest, s8812, sc |
| shared page | ira, person, s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sli.h_max
    printed: "(helper)"
    label: "Maximum amount for line 1 ($2,500)"
    type: NonNegDollars
    expr: {op: param, ref: sli.max}

  - id: sli.line1
    printed: "1"
    label: "Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don't enter more than $2,500"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sli.interest, sli.h_max]}
    refuses: [sa.excluded_income]
    note: "The Exception says to use Pub. 970 instead of this worksheet if the filer files Form 2555 or 4563 or excludes income from sources within Puerto Rico. The screening input sa.excluded_income asks exactly that question, so this line refuses when it is true."

  - id: sli.h_zero
    printed: "(helper)"
    label: "Zero (no deduction allowed)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: sli.h_mfs
    printed: "(helper)"
    label: "Filing status is married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}

  - id: sli.deduction
    printed: "(helper)"
    label: "Student loan interest deduction (Schedule 1, line 21)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sli.h_mfs, {const: true}]}
          then: sli.h_zero
        - guard: {op: test, eq: [sli.h_mfs, {const: false}]}
          then: sli.line9
    refuses: [sa.dependent, sa.excluded_income]
    note: >-
      The line 21 instructions allow the deduction only if the filing status is not married filing separately, so this
      result is zero for MFS and line 9 otherwise. The instructions also require that neither you nor your spouse
      (if filing jointly) is claimed as a dependent on someone else's return. No interface input says whether the
      filer is actually claimed. The closest screening input, sa.dependent, asks whether someone can claim you or your
      spouse, and it excludes a person who could claim you but does not file or files only for a refund. I chose to
      refuse on it rather than invent an input. This is broader than the IRS condition: it also refuses a filer who
      could be claimed but is not. The modified AGI limit ($100,000, or $200,000 MFJ) needs no separate test, because
      lines 4 to 8 already reduce the deduction to zero at those amounts.
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: sli.h_max
    printed: "(helper)"
    label: "Year parameter sli.max ($2,500)"
    type: NonNegDollars
    expr: {op: param, ref: sli.max}

  - id: sli.line1
    printed: "1"
    label: "Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don't enter more than $2,500"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sli.interest, sli.h_max]}

  - id: sli.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9"
    type: Dollars
    expr: {op: copy, from: f1040.line9}

  - id: sli.line3
    printed: "3"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25"
    type: NonNegDollars
    expr: {op: sum, of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line20, s1.line25]}
    note: "Open: the text names Schedule 1 lines 11 through 20, 23 and 25, but no ids exist for lines 12, 14 or 23. Chosen: sum the Schedule 1 lines in this range that exist (11, 13, 15, 16, 17, 18, 19a, 20, 25). The lines without ids are treated as outside the tool's scope, which is screened by scope.schedule1."

  - id: sli.line4
    printed: "4"
    label: "Subtract line 3 from line 2"
    type: Dollars
    expr: {op: subtract, from: sli.line2, take: sli.line3}

  - id: sli.h_mfj
    printed: "(helper)"
    label: "Married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: sli.h_base_joint
    printed: "(helper)"
    label: "Year parameter sli.base_joint ($170,000)"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_joint}

  - id: sli.h_base_other
    printed: "(helper)"
    label: "Year parameter sli.base_other ($85,000)"
    type: NonNegDollars
    expr: {op: param, ref: sli.base_other}

  - id: sli.line5
    printed: "5"
    label: "Enter the amount shown below for your filing status. Single, head of household, or qualifying surviving spouse—$85,000. Married filing jointly—$170,000"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sli.h_mfj, {const: true}]}, then: sli.h_base_joint}
        - {guard: {op: test, eq: [sli.h_mfj, {const: false}]}, then: sli.h_base_other}
    note: "Open: the line 5 table lists no amount for married filing separately. Chosen: every status other than married filing jointly uses $85,000. A married filing separately filer gets no deduction, which sli.deduction enforces, so this amount does not affect the result for that filer."

  - id: sli.line6
    printed: "6"
    label: "Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sli.line4, take: sli.line5}
    note: "The text says: 'Is the amount on line 4 more than the amount on line 5? No. Skip lines 6 and 7, enter -0- on line 8.' Chosen: line 6 is floored at zero. A zero line 6 makes the prorated line 8 zero, which matches the No branch."

  - id: sli.h_divisor_joint
    printed: "(helper)"
    label: "Year parameter sli.divisor_joint ($30,000)"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_joint}

  - id: sli.h_divisor_other
    printed: "(helper)"
    label: "Year parameter sli.divisor_other ($15,000)"
    type: NonNegDollars
    expr: {op: param, ref: sli.divisor_other}

  - id: sli.h_divisor
    printed: "(helper)"
    label: "Line 7 divisor: $15,000 ($30,000 if married filing jointly)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sli.h_mfj, {const: true}]}, then: sli.h_divisor_joint}
        - {guard: {op: test, eq: [sli.h_mfj, {const: false}]}, then: sli.h_divisor_other}

  - id: sli.line8
    printed: "8"
    label: "Multiply line 1 by line 7"
    type: NonNegDollars
    expr: {op: prorate, amount: sli.line1, part: sli.line6, whole: sli.h_divisor, places: 3}
    ambiguity: amb.2025.sli_ratio_places
    note: "Line 7 ('Divide line 6 by $15,000 ($30,000 if married filing jointly). Enter the result as a decimal (rounded to at least three places). If the result is 1.000 or more, enter 1.000') is folded into this prorate. Open: 'at least three places' does not fix the number of places. Chosen: exactly three places, rounded half-up."

  - id: sli.line9
    printed: "9"
    label: "Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on Schedule 1, line 21"
    type: NonNegDollars
    expr: {op: subtract, from: sli.line1, take: sli.line8}
    refuses: [sa.excluded_income]
    note: "The Exception says to use Pub. 970 instead of this worksheet if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico. The tool refuses at this line on screening input sa.excluded_income."

  - id: sli.h_mfs
    printed: "(helper)"
    label: "Married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}

  - id: sli.h_ineligible
    printed: "(helper)"
    label: "Married filing separately, or you (or your spouse if filing jointly) are claimed as a dependent on someone else's 2025 return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sli.h_mfs, {const: true}]}
        - {op: test, eq: [sli.claimed, {const: true}]}

  - id: sli.h_zero
    printed: "(helper)"
    label: "Year parameter sales.zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sli.deduction
    printed: "(helper)"
    label: "Student loan interest deduction (Schedule 1, line 21)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sli.h_ineligible, {const: true}]}, then: sli.h_zero}
        - {guard: {op: test, eq: [sli.h_ineligible, {const: false}]}, then: sli.line9}
    note: "The instructions allow the deduction only if your filing status is not married filing separately and you (or your spouse if filing jointly) are not claimed as a dependent on someone else's 2025 return; otherwise the deduction is zero. The condition that modified AGI is under $100,000 ($200,000 MFJ) is not coded separately: at those amounts line 7 reaches 1.000, so line 8 equals line 1 and line 9 is zero."
```
```
