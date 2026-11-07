# Transcription agreement — sli

Second transcription of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` by an isolated model (spec 6.5), compared line by line with `forms/2025/sli.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

Second transcription's note: The line 21 instructions allow the deduction only if 'your filing status is any status except married filing separately'. For MFS the deduction is zero; otherwise it is worksheet line 9. The modified AGI limit ($100,000 / $200,000) is enforced by worksheet lines 5 to 8, where the ratio reaches 1.000 and line 9 becomes zero. The instructions also require that you (or your spouse if filing jointly) are not claimed as a dependent on someone else's 2025 return. The only related input, sa.dependent, asks whether someone 'can claim' you, which is broader than 'claimed', so it is not used. That condition is not encoded and is recorded here as a limitation.

Ruling: model error; same reply and project as the round-2 and round-3 rulings. i1040gi p. 98, Line 21: "You, or your spouse if filing jointly, aren't claimed as a dependent on someone else's ... 2025 tax return." The reply refuses on sa.dependent (who can be claimed) where the source and the project (sli.claimed_count, person.sav_claimed) test being claimed. Triage executable-triage-v2 (reviews/2025/transcription/triage/sli.json; 1,638 fixtures, 500 generated returns seed 20261026, 40 partial records): the candidate declaration is invalid on this pass's scoped interface (candidate-invalid on all 2,178 records), so no value is compared. The R3 restructuring of sli.interest kept its words (word check: none lost). Project stands.
Reviewed in: pass 147f25f1166e

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **AGREE**
Reviewed in: pass 147f25f1166e

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
| sli.deduction | sa.excluded_income | - |
| 1 | sa.excluded_income | - |
| 9 | sa.excluded_income | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sli.deduction | e510e998d17fa197cdf50db53efa20d06379788a84dcbfc8776a2fd9176bb10f |
| 1 | 14f6e6e5ef6247b19ad2cc842ee75ae62cc347165052596c02dafcd1794de6d7 |
| 2 | 03b76842d0b2c01ed25446bb350441f94e4e87fe6f19ca18a3ea8ee9d0f06a4d |
| 3 | 3a2f5cd698d5de7f0de48e3a76ddcbbd07c2f0b49b90c745ef539cc95ad9986d |
| 4 | 7525f5f108db9d3ec62d4c245aeea6b7186ca4e6c389a61b6e16750c48e330f2 |
| 5 | 20c8ee35cb8da865b0bf308195f8641c250b33a3f63a3bdbf99bfcaefb21ed7d |
| 6 | a77e5ff66b75bc33b649dc4f50a40614a840ae63e3bc5db7725797dbf0141e82 |
| 8 | 68e05b5c4fcce5f4405fc5b1812ce224725cb97279f98d9586daca9df7f883f0 |
| 9 | 7274f8a4ef90caae8b570f37c9581f7075be8d799b18248edab0c8a8e1d75673 |
| (rest of the document) | cdbf85c374e333f356e978a01b3319b841c43b9a1e74b210b748829916056fb7 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sli.deduction | 5e71e09486b3638eef1ca7ad68c53ea93594179c3192bf31e4e4b3916035bc7d |
| 1 | 858fe29eeecfc7e735a4186d6ac0601622fb726b32d175e564be98b0c47a1478 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 147f25f1166e

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines sli.deduction, 1 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 147f25f1166e8f1a863ff8ec6e69821b163a6b712b552b828d544e55211b208b |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9759c4963136f3ba645f147b0fc946a9253f5996f15a60e999413c3394a8db8d |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | eeb8294e1e9aee10b8887a58bcfa3b94381c081e71f47e7b6d76ee479b20af5a |
| receipt | .transcription/sli.lines-b2eae3131c48 |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p4681 | 2025 | 5 | pages named by another document's citation | c280f0029d95f9f4186840c73600efd2af4bd3370a86a31fb4f2a9391887b2b6 | 5 | 21875d96efa2d4d7885584db3cf06d5830154aeff1eaf3370efad4fab5cc3a17 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.line9, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | f8960, interest, s8812, sc |
| shared page | ira, person, s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sli.h_max
    printed: "(helper)"
    label: "Don't enter more than $2,500"
    type: NonNegDollars
    expr: {op: param, ref: sli.max}
  - id: sli.line1
    printed: "1"
    label: "Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don't enter more than $2,500"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sli.interest, sli.h_max]}
    refuses: [sa.excluded_income]
    note: "The Exception in the line 21 instructions sends filers of Form 2555 or 4563, and those excluding income from sources within Puerto Rico, to Pub. 970 instead of this worksheet. The screening input sa.excluded_income asks exactly that question, so line 1 refuses on it."
  - id: sli.h_zero
    printed: "(helper)"
    label: "Zero (no student loan interest deduction)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "No zero-valued sli parameter is supplied. This uses the zero-valued money parameter ss.zero."
  - id: sli.deduction
    printed: "(helper)"
    label: "Student loan interest deduction (worksheet line 9, entered on Schedule 1, line 21)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: sli.h_zero
        - guard: {op: test, ne: [f1040.status, {const: "mfs"}]}
          then: sli.line9
    refuses: [sa.excluded_income]
    note: "The line 21 instructions allow the deduction only if 'your filing status is any status except married filing separately'. For MFS the deduction is zero; otherwise it is worksheet line 9. The modified AGI limit ($100,000 / $200,000) is enforced by worksheet lines 5 to 8, where the ratio reaches 1.000 and line 9 becomes zero. The instructions also require that you (or your spouse if filing jointly) are not claimed as a dependent on someone else's 2025 return. The only related input, sa.dependent, asks whether someone 'can claim' you, which is broader than 'claimed', so it is not used. That condition is not encoded and is recorded here as a limitation."
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
