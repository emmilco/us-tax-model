# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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
{"alternatives": [{"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, "then": {"input": "sales.correct_basis"}}, {"guard": {"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.reported_basis"}}], "op": "choose"}
```

Second transcription's note: For box A/D/G/J the reported basis is entered even if incorrect (corrected in column (g)); for box B/E/H/K the correct basis is entered with -0- in (g); for box C/F/I/L there is no reported basis, so the correct basis from records is used. Aggregate (Exception 1) transactions also use the reported basis, which is correct by the exception's conditions.

Ruling: scope; same line and candidate as the refresh-round ruling. f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. The reply adds boxes G and J to the reported-basis boxes, the source's reading, but boxes G to L are refused at the transaction by sales.digital at sales.one. Project stands.
Reviewed in: pass 518207396655

### (g) — Column (g): net adjustments
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"input": "sales.route"}], "test": "eq"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "detail"}, {"input": "sales.route"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"input": "sales.route"}], "test": "eq"}], "test": "all"}, "then": {"input": "sales.wash_loss"}}, {"guard": {"args": [{"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "detail"}, {"input": "sales.route"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Second transcription's note: Net adjustment = code B correction (reported basis minus correct basis, only for box A/D/G/J; -0- for box B/E/H/K where the correct basis goes in column (e)) plus code W nondeductible wash sale loss as a positive number. Codes other than B and W, and collectibles/QSB/section 1250 sales, are refused. Column (g) is left blank when no code applies; aggregate (Exception 1) transactions carry no adjustment.

Ruling: representation and scope; i8949 p. 8, code B: "Correct the error by entering an adjustment in column (g)"; i8949 p. 10, code W. Values: reported less correct basis for code B or BW on boxes A and D, plus the wash-sale loss for W or BW, as the project. The reply adds boxes G and J (refused by sales.digital) and a sales.route detail condition: a Schedule D aggregate transaction with any code is refused by sales.bad_aggregate (route aggregate and code not none), so the condition changes no supported return. Project stands.
Reviewed in: pass 518207396655

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.h_aggregate_bad | sales.h_aggregate_bad |
| (g) | sales.h_aggregate_bad, sales.h_other_code, sales.h_wash_excess, sales.special | sales.h_aggregate_bad, sales.h_other_code, sales.h_wash_excess, sales.special |
| (h) | sales.h_aggregate_bad, sales.h_other_code, sales.h_wash_excess, sales.special | sales.h_aggregate_bad, sales.h_other_code, sales.h_wash_excess, sales.special |

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
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 3b1a4ea2ede17f5645e224baa60e90d69171458986b0e64202d66334c9b6e0d6 |
| receipt | .transcription/sales.lines-efadd99d9686 |
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
```yaml
lines:
  - id: sales.h_reported_box
    printed: "(helper)"
    label: "Transaction reported on Part I with box A or box G checked, or on Part II with box D or box J checked (basis reported to the IRS)"
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
    label: "Transaction is reported in detail on Form 8949 (not aggregated directly on Schedule D line 1a or 8a under Exception 1)"
    type: Bool
    expr: {op: test, eq: [sales.route, {const: "detail"}]}
  - id: sales.h_has_b
    printed: "(helper)"
    label: "Code B in column (f): basis shown on Form 1099-B or Form 1099-DA is incorrect"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W in column (f): nondeductible loss from a wash sale"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_other_code
    printed: "(helper)"
    label: "A column (f) code other than B or W applies (outside this tool)"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Aggregate reporting chosen for a transaction that does not meet Exception 1 (basis reported to the IRS, no adjustments or codes, conditions confirmed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, ne: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.h_reported_box, {const: false}]}
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. If you checked Box A, D, G or J but the basis reported to the IRS was incorrect, enter in column (e) the basis as reported to the IRS; otherwise enter the correct basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_reported_box, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, not: {op: test, eq: [sales.h_reported_box, {const: true}]}}
          then: sales.correct_basis
    refuses: [sales.h_aggregate_bad]
    shown_when: sales.h_detail
    note: "For box A/D/G/J the reported basis is entered even if incorrect (corrected in column (g)); for box B/E/H/K the correct basis is entered with -0- in (g); for box C/F/I/L there is no reported basis, so the correct basis from records is used. Aggregate (Exception 1) transactions also use the reported basis, which is correct by the exception's conditions."
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_b_case
    printed: "(helper)"
    label: "Code B adjustment required in column (g): box A, D, G or J, detail reporting, incorrect reported basis"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_reported_box, {const: true}]}
        - {op: test, eq: [sales.h_has_b, {const: true}]}
        - {op: test, eq: [sales.h_detail, {const: true}]}
  - id: sales.h_basis_diff
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3 and 4: line 1 (basis shown on Form 1099-B or 1099-DA) minus line 2 (correct basis); positive on line 4, negative (in parentheses) on line 3"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
  - id: sales.h_b_adj
    printed: "(helper)"
    label: "Code B part of the column (g) adjustment"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_b_case, {const: true}]}
          then: sales.h_basis_diff
        - guard: {op: test, not: {op: test, eq: [sales.h_b_case, {const: true}]}}
          then: sales.h_zero
  - id: sales.h_w_case
    printed: "(helper)"
    label: "Code W adjustment reported in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_has_w, {const: true}]}
        - {op: test, eq: [sales.h_detail, {const: true}]}
  - id: sales.h_w_adj
    printed: "(helper)"
    label: "Code W part of the column (g) adjustment: the nondeductible wash sale loss as a positive number"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_w_case, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, not: {op: test, eq: [sales.h_w_case, {const: true}]}}
          then: sales.h_zero
  - id: sales.h_loss
    printed: "(helper)"
    label: "Loss on this sale before adjustment: correct basis minus proceeds"
    type: Dollars
    expr: {op: subtract, from: sales.correct_basis, take: sales.proceeds}
  - id: sales.h_wash_excess
    printed: "(helper)"
    label: "Consistency check: nondeductible wash sale loss is more than the loss on this sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_w_case, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss]}
  - id: sales.h_g_shown
    printed: "(helper)"
    label: "Column (g) completed: detail reporting with a code in column (f)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_detail, {const: true}]}
        - {op: test, ne: [sales.code, {const: "none"}]}
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment. Enter in this column any necessary adjustments to gain (or loss). Enter negative amounts in parentheses. If more than one code, enter the net adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_b_adj, sales.h_w_adj]}
    refuses:
      - sales.special
      - sales.h_other_code
      - sales.h_aggregate_bad
      - {when: sales.h_wash_excess, when_known: true}
    shown_when: sales.h_g_shown
    note: "Net adjustment = code B correction (reported basis minus correct basis, only for box A/D/G/J; -0- for box B/E/H/K where the correct basis goes in column (e)) plus code W nondeductible wash sale loss as a positive number. Codes other than B and W, and collectibles/QSB/section 1250 sales, are refused. Column (g) is left blank when no code applies; aggregate (Exception 1) transactions carry no adjustment."
  - id: sales.one
    printed: "(helper)"
    label: "One transaction (count of this entry)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface; read as a per-transaction count of 1 so that other forms can count the transactions (e.g., whether Form 8949 or Schedule D has any entries) by sum_over."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.one
    printed: "(helper)"
    label: "One transaction (a count of 1 for this row)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface. Reading chosen: a per-entry count of 1, used by other forms to count the transactions entered. The value comes from the year parameter sales.one."

  - id: sales.h_reported_box
    printed: "(helper)"
    label: "Box A, D, G or J: basis shown on Form 1099-B or Form 1099-DA was reported to the IRS"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sales.h_has_b
    printed: "(helper)"
    label: "Code B entered in column (f)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W entered in column (f)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_other_code
    printed: "(helper)"
    label: "An adjustment code other than B or W applies"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}

  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Reported directly on Schedule D line 1a or 8a without meeting Exception 1"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, ne: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, eq: [sales.h_reported_box, {const: false}]}
    note: "Exception 1 applies only to transactions that are reported with basis reported to the IRS (boxes A, D, G, J) and that need no adjustments or codes. A transaction routed to aggregate that fails any of these conditions is refused rather than recomputed."

  - id: sales.h_show_g
    printed: "(helper)"
    label: "Columns (f) and (g) completed for this row"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ne: [sales.code, {const: "none"}]}
        - {op: test, eq: [sales.route, {const: "detail"}]}

  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. See the Note below and see Column (e) in the separate instructions."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_reported_box, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_reported_box, {const: false}]}
          then: sales.correct_basis
    note: "For boxes A, D, G and J, column (e) is the basis as reported to the IRS, even if incorrect; code B corrects it in column (g). For the other boxes, column (e) is the correct basis: noncovered securities, basis not reported to the IRS, or no Form 1099-B or 1099-DA. Where no correction is needed, the reported basis is taken to equal the correct basis."

  - id: sales.h_basis_adj
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3 and 4: line 1 (basis shown on Form 1099-B or 1099-DA) minus line 2 (correct basis); positive if line 1 is larger, negative if line 2 is larger"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}

  - id: sales.h_b_amount
    printed: "(helper)"
    label: "Code B adjustment in column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sales.h_has_b, {const: true}]}
              - {op: test, eq: [sales.h_reported_box, {const: true}]}
          then: sales.h_basis_adj
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sales.h_has_b, {const: true}]}
                - {op: test, eq: [sales.h_reported_box, {const: true}]}
          then: sales.h_zero
    note: "Code B with box B, E, H or K: enter the correct basis in column (e) and -0- in column (g). Code B with box C, F, I or L has no reported basis to correct and is likewise taken as -0-."

  - id: sales.h_w_amount
    printed: "(helper)"
    label: "Code W: nondeductible wash sale loss entered as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_has_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_has_w, {const: false}]}
          then: sales.h_zero

  - id: sales.h_d_minus_e
    printed: "(helper)"
    label: "Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}

  - id: sales.h_pre_w
    printed: "(helper)"
    label: "Gain or (loss) after any code B basis correction, before the wash sale adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_d_minus_e, sales.h_b_amount]}

  - id: sales.h_loss
    printed: "(helper)"
    label: "Loss on this sale (column (e) less column (d), after any code B basis correction); zero if none"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sales.h_zero, take: sales.h_pre_w}

  - id: sales.h_wash_excess
    printed: "(helper)"
    label: "Nondeductible wash sale loss is more than the loss on the sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_has_w, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss]}

  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment. If you enter an amount in column (g), enter a code in column (f). See the separate instructions."
    type: Dollars
    expr: {op: sum, of: [sales.h_b_amount, sales.h_w_amount]}
    refuses:
      - sales.special
      - sales.h_other_code
      - sales.h_aggregate_bad
      - {when: sales.h_wash_excess, when_known: true}
    shown_when: sales.h_show_g
    note: "When code BW applies, column (g) is the net of the code B and code W adjustments (More than one code). Collectibles (code C), QSB stock (code Q) and every other code are outside this slice and are refused."

  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr: {op: sum, of: [sales.h_d_minus_e, sales.g]}
    refuses:
      - sales.special
      - sales.h_other_code
      - sales.h_aggregate_bad
      - {when: sales.h_wash_excess, when_known: true}
```
```
