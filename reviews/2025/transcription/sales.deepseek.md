# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7ebb11051957508a149e0de206648592aa48bab9171dff751280d40798e419e4 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | e649c20872e55382aa9703fb15d0eb8be1088ec78901843140f64b7036e792b5 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7555ba030958f03545c2e7c204caccd806775cdf44cd59cc8f0ba649d4b68626 |
| printed lines compared | 4 |
| agree / disagree / missing | 2 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, div, f1040, f4952, f5329, f8960, household, interest, person, refund, retirement, s1, s2, s3, sa, sb, sc, scope, scveh, sdtw |
| named line | ftc |
| shared page | clcw, clcw26, g28, sd, u1250 |
| worksheet | qdcg |

## Lines

### sales.one — Screen this transaction before any aggregation
Status: **AGREE**
Reviewed in: pass 518207396655

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"input": "sales.correct_basis"}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.reported_basis"}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"input": "sales.correct_basis"}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.reported_basis"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: scope; as the refresh-round ruling: the reply adds boxes G and J to the reported-basis boxes (and a zero floor, which changes nothing on nonnegative inputs); boxes G to L are refused at the transaction by sales.digital at sales.one. Project stands.
Reviewed in: pass 518207396655

### (g) — Column (g): net adjustments
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, "then": {"of": [{"input": "sales.wash_loss"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}
```

Ruling: representation and scope; i8949 p. 8, code B, and p. 10, code W. The reply chooses by code: zero for none or other (other is refused by sales.bad_code), the basis correction for B on boxes A, D, G and J, the wash-sale loss plus the correction for BW, the wash-sale loss for W; on boxes A and D this is the project's sum. Boxes G and J are refused by sales.digital. Project stands.
Reviewed in: pass 518207396655

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (g) | sales.h_code_other | sales.h_code_other |
| (h) | sales.h_aggregate_bad, sales.h_other_code, sales.special | sales.h_aggregate_bad, sales.h_other_code, sales.special |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sales.one | e1e85ca4388491fb8bf231ea82242d2111df3b2a9190167acdaf05aac548a36c |
| (e) | 9dc6fb75298af6a777c12ce49fbab9c65c6f6aa5559a92af0191ecfaeb377478 |
| (g) | d2035b934965f6f006dab70da6f410bd9ebaacb69f0db48f949130c02d9f814e |
| (h) | 917089919b3402501d4bded41fb0b939aacf1a51c54bf484f4db81ef3358e59a |
| (rest of the document) | bd65df118805874cff9360e29b8978e3a8b739647bd7439342d356bc47841505 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sales.one | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (e) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (g) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 518207396655

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sales.one, (e), (g) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 51820739665572dc532424b2856f030ab29f618109e2c1f76d3c713cf1f1a958 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 5cb3e8829a8a94c88e8d681e1612649e37bd8bd5c027a82d451520bde669ebf7 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 3b1a4ea2ede17f5645e224baa60e90d69171458986b0e64202d66334c9b6e0d6 |
| receipt | .transcription/sales.deepseek.lines-efadd99d9686 |
| printed lines compared | 3 |
| agree / disagree / missing | 1 / 2 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, div, f1040, household, person, retirement, s1, sa, scope, sdtw |
| named line | f5329, scveh |
| shared page | clcw, clcw26, g28, sd, u1250 |

##### Raw second transcription

```yaml
lines:
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sales.h_e_selected, take: {const: 0}}
    shown_when: sales.h_detail
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.code, {const: "B"}]}
          then: sales.h_basis_adjustment
        - guard: {op: test, eq: [sales.code, {const: "W"}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.code, {const: "BW"}]}
          then: sales.h_bw_adjustment
        - guard: {op: test, eq: [sales.code, {const: "none"}]}
          then: sales.h_zero
        - guard: {op: test, eq: [sales.code, {const: "other"}]}
          then: sales.h_zero
    refuses: [sales.h_code_other]
    shown_when: sales.h_detail
  - id: sales.one
    printed: "(helper)"
    label: "Constant one"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not determine this count; it is the supplied parameter sales.one."
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_box_reported
    printed: "(helper)"
    label: "Whether basis was reported to the IRS"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sales.h_detail
    printed: "(helper)"
    label: "Whether the transaction is reported in detail on Form 8949"
    type: Bool
    expr: {op: test, eq: [sales.route, {const: "detail"}]}
  - id: sales.h_code_other
    printed: "(helper)"
    label: "Whether an unsupported additional adjustment code applies"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_e_selected
    printed: "(helper)"
    label: "Cost or other basis selected for column (e)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_box_reported, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_box_reported, {const: false}]}
          then: sales.correct_basis
  - id: sales.h_basis_diff
    printed: "(helper)"
    label: "Reported basis less correct basis"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
  - id: sales.h_basis_adjustment
    printed: "(helper)"
    label: "Basis correction adjustment for column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_box_reported, {const: true}]}
          then: sales.h_basis_diff
        - guard: {op: test, eq: [sales.h_box_reported, {const: false}]}
          then: sales.h_zero
  - id: sales.h_bw_adjustment
    printed: "(helper)"
    label: "Combined basis and wash-sale adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_basis_adjustment, sales.wash_loss]}
```

## Raw second transcription

```yaml
lines:
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sales.h_basis_reported, {const: true}]
          then: sales.reported_basis
        - guard:
            op: test
            eq: [sales.h_basis_reported, {const: false}]
          then: sales.correct_basis
    refuses: [sales.special, sales.h_other_code, sales.h_aggregate_bad]
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr:
      op: sum
      of: [sales.h_basis_adj, sales.h_wash_adj]
    refuses: [sales.special, sales.h_other_code, sales.h_aggregate_bad]
    note: "Only adjustment codes none, B, W and BW are computed; any other code is refused."
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss)"
    type: Dollars
    expr:
      op: sum
      of: [sales.h_gain_before_adj, sales.g]
    refuses: [sales.special, sales.h_other_code, sales.h_aggregate_bad]
  - id: sales.one
    printed: "(helper)"
    label: "One sale transaction"
    type: Count
    expr: {op: param, ref: sales.one}
  - id: sales.h_basis_reported
    printed: "(helper)"
    label: "Basis was reported to the IRS for this Form 8949 box"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sales.h_basis_code
    printed: "(helper)"
    label: "Basis-adjustment code applies"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_wash_code
    printed: "(helper)"
    label: "Wash-sale code applies"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_other_code
    printed: "(helper)"
    label: "An unsupported adjustment code applies"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Aggregate reporting was chosen without all aggregate conditions"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero dollars"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_basis_adj_applies
    printed: "(helper)"
    label: "A basis correction belongs in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_basis_reported, {const: true}]}
        - {op: test, eq: [sales.h_basis_code, {const: true}]}
  - id: sales.h_basis_adj_raw
    printed: "(helper)"
    label: "Reported basis less correct basis"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
  - id: sales.h_basis_adj
    printed: "(helper)"
    label: "Basis adjustment for column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_basis_adj_applies, {const: true}]}
          then: sales.h_basis_adj_raw
        - guard: {op: test, eq: [sales.h_basis_adj_applies, {const: false}]}
          then: sales.h_zero
  - id: sales.h_wash_adj
    printed: "(helper)"
    label: "Wash-sale adjustment for column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_wash_code, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_wash_code, {const: false}]}
          then: sales.h_zero
  - id: sales.h_gain_before_adj
    printed: "(helper)"
    label: "Proceeds less column (e) basis"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}
```
