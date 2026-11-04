# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-04); see Line-scoped reviews |
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
| agree / disagree / missing | 1 / 3 / 0 |
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
Reviewed in: pass 7e9bbf084234

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

Second transcription's note: For boxes A, D, G and J (including transactions aggregated on Schedule D line 1a or 8a, which require basis reported to the IRS) the reported basis is entered; for boxes B, C, E, F, H, I, K and L the correct basis is entered (the text for boxes B/E/H/K says to enter the correct basis, and boxes C/F/I/L have no broker report). A known mismatch between the reported basis and the correct basis on a box A/D/G/J transaction without code B is a consistency failure.

Ruling: scope; same reply and project as the round-2 ruling. f8949 p. 1, box G; i8949 p. 8, code B. The reply adds boxes G and J to the reported-basis boxes, but boxes G to L are refused at the transaction by sales.digital at sales.one. Scratch run of triage.mjs on the round-3 reply (.transcription/sales.lines-ceb969c79173) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 476 partial records; 1,762 comparisons per line): 1,755 agree; the 7 value differences are all on refused returns (boxes G and J). Project stands.
Reviewed in: pass 7e9bbf084234

### (g) — Column (g): net adjustments
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second transcription's note: Only codes B and W are computed; their adjustments are netted as the text directs for more than one code. Any other code (code other) and sales with collectibles, QSB stock, section 1250 property or such pass-through interests (sales.special) are refused rather than written as zero. Column (g) is left blank when no code applies; its value is then zero.

Ruling: model error and scope; i8949 p. 10, code W, "enter the amount of the nondeductible loss as a positive number in column (g)", and p. 8, code B. Values are the project's (the code B correction on boxes A and D plus the wash-sale loss for W or BW); the boxes G and J and route conditions are the round-2 ruling's scope points. New evidence on the same reply: its wash-excess gate (h_wash_excess: code W and the wash-sale loss above correct basis less proceeds) refuses completed returns the project computes, because it measures the loss from the correct basis where column (e) on box A or D is the reported basis, and fires on a $0 wash-sale loss on a row with a gain; the project refuses only a positive wash-sale loss above the loss after any code B correction (sales.wash_bad; the sales.wash_loss question, "It cannot be more than the loss on this sale (column (e) less column (d), after any code B basis correction)"). Scratch run of triage.mjs on the round-3 reply (.transcription/sales.lines-ceb969c79173) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 476 partial records; 1,762 comparisons per line): 1,379 agree; on completed returns 42 candidate refusals, all h_wash_excess (e.g. classm.clcw26.2.deepseek s2, box A, code W, wash-sale loss $0.00, project $0.00); the rest are on refused or incomplete returns. The round-3 sales.wash_loss wording fix (the definition and "0 if no part of the loss is from a wash sale") does not cause it. Project stands.
Reviewed in: pass 7e9bbf084234

### (h) — Column (h): proceeds less basis plus adjustments
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"of": [{"line": "(g)"}, {"from": {"input": "sales.proceeds"}, "op": "subtract", "take": {"line": "(e)"}}], "op": "sum"}}
```

Second:

```json
{"shown_when": {"args": [{"const": "detail"}, {"input": "sales.route"}], "test": "eq"}, "value": {"of": [{"line": "(g)"}, {"from": {"input": "sales.proceeds"}, "op": "subtract", "take": {"line": "(e)"}}], "op": "sum"}}
```

Ruling: representation and model error; i8949 p. 11, column (h). The value is the project's ((d) less (e) plus (g)); the reply shows the line only on the detail route, but the transaction's column (h) amount is read on both routes (sd.line1a.h and sd.line8a.h for the aggregate route), and the project's sheet is a values sheet, so the display condition changes no value. Its candidate refusals are column (g)'s h_wash_excess gate (see (g)). Scratch run of triage.mjs on the round-3 reply (.transcription/sales.lines-ceb969c79173) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 476 partial records; 1,762 comparisons per line): 1,380 agree; on completed returns 42 candidate refusals, the column (g) records; 4 value differences, all on refused returns. Project stands.
Reviewed in: pass f71b3c0cac42

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.h_basis_unflagged | sales.h_basis_unflagged |
| (g) | sales.h_aggregate_conflict, sales.h_other_code, sales.h_wash_excess, sales.special | sales.h_aggregate_conflict, sales.h_other_code, sales.h_wash_excess, sales.special |
| (h) | sales.h_aggregate_bad, sales.h_code_other, sales.h_wash_excess, sales.special | sales.h_aggregate_bad, sales.h_code_other, sales.h_wash_excess, sales.special |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sales.one | 8d309a85773acad1d8f9f0453e3400fb80ca91c66e7944158af7d92d8570a680 |
| (e) | b5aa5d9a4d36bf71ecf78f83633261dc52993ba401e88fb994c932bb3f2b9c4d |
| (g) | b1541c54f3b892c126800524284890e3d6ec0599d13dac66cf78f8d9d2d7f0f7 |
| (h) | 2422451df8e177d55abe45d3f471d4c89063e2ddde31e6b78d028783cf6be82d |
| (rest of the document) | bd65df118805874cff9360e29b8978e3a8b739647bd7439342d356bc47841505 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sales.one | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (e) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (g) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (h) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 7e9bbf084234

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sales.one, (e), (g) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 7e9bbf084234ed1962d2fbc197020bdfd9e63acded0a6aba4a565720c660e186 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 49e497583fd21cee47f88d789ecff463f1a9c57f1bf24ca2f81e8fd1f7211c78 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4be36125cb6b9bcb6108997ac32d18f6cbbfa3fd060bfc6879a56bd8af531746 |
| receipt | .transcription/sales.lines-efadd99d9686 |
| printed lines compared | 3 |
| agree / disagree / missing | 1 / 2 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6, 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, div, f1040, household, person, retirement, s1, s3, sa, sc, scope, scveh, sdtw |
| named line | f5329 |
| shared page | clcw, clcw26, g28, sd, u1250 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sales.h_basis_reported_box
    printed: "(helper)"
    label: "Transaction reported on Part I with box A or box G checked, or on Part II with box D or box J checked (basis shown and reported to the IRS)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e). If this transaction is reported on Part I with box A or box G checked or on Part II with box D or box J checked, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect. If reported with box B, E, H or K checked, enter the correct basis in column (e); for transactions not reported to you on Form 1099-B or Form 1099-DA, enter the correct basis."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_basis_reported_box, {const: false}]}
          then: sales.correct_basis
    refuses:
      - {when: sales.h_basis_unflagged, when_known: true}
    note: "For boxes A, D, G and J (including transactions aggregated on Schedule D line 1a or 8a, which require basis reported to the IRS) the reported basis is entered; for boxes B, C, E, F, H, I, K and L the correct basis is entered (the text for boxes B/E/H/K says to enter the correct basis, and boxes C/F/I/L have no broker report). A known mismatch between the reported basis and the correct basis on a box A/D/G/J transaction without code B is a consistency failure."

  - id: sales.h_code_b
    printed: "(helper)"
    label: "Code B entered in column (f) (alone or with W)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_code_w
    printed: "(helper)"
    label: "Code W entered in column (f) (alone or with B)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_basis_unflagged
    printed: "(helper)"
    label: "Consistency check: the basis was reported to the IRS (box A, D, G or J), no code B is entered, but the correct basis differs from the reported basis"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
        - {op: test, eq: [sales.h_code_b, {const: false}]}
        - {op: test, ne: [sales.reported_basis, sales.correct_basis]}

  - id: sales.h_other_code
    printed: "(helper)"
    label: "An adjustment code other than B or W applies (for example C, E, H, L, M, N, O, P, Q, R, S, T, X, Y or Z)"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}

  - id: sales.h_aggregate_conflict
    printed: "(helper)"
    label: "Consistency check: the transaction is reported directly on Schedule D (Exception 1) but an adjustment code applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - {op: test, ne: [sales.code, {const: "none"}]}

  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.h_basis_adj
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g): line 1 (basis shown on Form 1099-B or 1099-DA) minus line 2 (correct basis); positive is line 4, negative is line 3 entered as a negative number"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}

  - id: sales.h_b_amount
    printed: "(helper)"
    label: "Code B adjustment in column (g): the worksheet amount for box A, D, G or J; -0- for box B, E, H or K (correct basis entered in column (e))"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sales.h_code_b, {const: true}]}
              - {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
          then: sales.h_basis_adj
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sales.h_code_b, {const: true}]}
                - {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
          then: sales.h_zero

  - id: sales.h_w_amount
    printed: "(helper)"
    label: "Code W adjustment in column (g): the amount of the nondeductible wash sale loss as a positive number (-0- if no part of the loss is from a wash sale)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_code_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_code_w, {const: false}]}
          then: sales.h_zero

  - id: sales.h_loss_after_b
    printed: "(helper)"
    label: "Loss on this sale after any code B basis correction: correct basis minus proceeds"
    type: Dollars
    expr: {op: subtract, from: sales.correct_basis, take: sales.proceeds}

  - id: sales.h_wash_excess
    printed: "(helper)"
    label: "Consistency check: the nondeductible wash sale loss entered is more than the loss on this sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_code_w, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss_after_b]}

  - id: sales.h_show_g
    printed: "(helper)"
    label: "A code is entered in column (f), so column (g) is completed"
    type: Bool
    expr: {op: test, ne: [sales.code, {const: "none"}]}

  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment. Enter in this column any necessary adjustments to gain (or loss). Enter negative amounts in parentheses. If more than one code is entered in column (f) on the same row, enter the net adjustment in column (g)."
    type: Dollars
    expr: {op: sum, of: [sales.h_b_amount, sales.h_w_amount]}
    shown_when: sales.h_show_g
    refuses:
      - sales.special
      - sales.h_other_code
      - {when: sales.h_aggregate_conflict, when_known: true}
      - {when: sales.h_wash_excess, when_known: true}
    note: "Only codes B and W are computed; their adjustments are netted as the text directs for more than one code. Any other code (code other) and sales with collectibles, QSB stock, section 1250 property or such pass-through interests (sales.special) are refused rather than written as zero. Column (g) is left blank when no code applies; its value is then zero."

  - id: sales.one
    printed: "(helper)"
    label: "One, for counting this transaction"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface; read as the per-transaction count of one (for counting the transactions entered), taken from the year parameter sales.one."
```
```

#### Pass f71b3c0cac42

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sales.one, (e), (g), (h) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f71b3c0cac42c7977ebfa3f53bf613a55de0133abee16f7768673fc380bf8442 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 75f20c3a68aafd18390449b3d497c433223e6e8b959aa98ff1ff0856eec5d757 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cd390cff7bf21b1e217b7e738e711569f4310fcc5dbebbf0fe9d5e00bf242be0 |
| receipt | .transcription/sales.lines-ceb969c79173 |
| printed lines compared | 4 |
| agree / disagree / missing | 1 / 3 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6, 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 60, 61, 81, 82, 86, 87 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 60, 61, 81, 82, 86, 87 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, div, f1040, household, person, retirement, s1, s3, sa, sc, scope, scveh, sdtw |
| named line | f5329 |
| shared page | clcw, clcw26, g28, sd, u1250 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sales.h_basis_reported
    printed: "(helper)"
    label: "Transaction reported on Part I with box A or box G checked, or on Part II with box D or box J checked (basis shown and reported to the IRS)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sales.h_on_8949
    printed: "(helper)"
    label: "Transaction is reported in detail on Form 8949 (not aggregated directly on Schedule D, line 1a or 8a, under Exception 1)"
    type: Bool
    expr: {op: test, eq: [sales.route, {const: "detail"}]}

  - id: sales.h_g_shown
    printed: "(helper)"
    label: "Columns (f) and (g) are completed (a code applies); otherwise leave columns (f) and (g) blank"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_on_8949, {const: true}]}
        - {op: test, ne: [sales.code, {const: "none"}]}

  - id: sales.h_code_b
    printed: "(helper)"
    label: "Code B applies (basis shown on Form 1099-B or Form 1099-DA is incorrect)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_code_w
    printed: "(helper)"
    label: "Code W applies (nondeductible loss from a wash sale)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_code_other
    printed: "(helper)"
    label: "A code other than B or W applies (for example E, H, L, M, N, O, Q, R, S, T, X, Y or Z)"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
    note: "The tool computes only codes B and W. Any other code is answered as 'other', and the tool refuses columns (g) and (h) rather than writing those adjustments as zero."

  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Aggregated on Schedule D line 1a/8a although Exception 1 does not apply (basis not reported, adjustments or codes required, or conditions not confirmed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, ne: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.h_basis_reported, {const: false}]}

  - id: sales.h_zero
    printed: "(helper)"
    label: "-0-"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. For box A, D, G or J, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement), even if incorrect; otherwise enter the correct basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_basis_reported, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_basis_reported, {const: false}]}
          then: sales.correct_basis
    shown_when: sales.h_on_8949
    note: "For box A/D/G/J (and the Exception 1 aggregate route, which requires reported basis with no adjustments), column (e) is the reported basis. For box B/E/H/K and C/F/I/L, it is the correct basis ('enter the correct basis in column (e), and enter -0- in column (g)')."

  - id: sales.h_ws3_4
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3 and 4: line 1 (basis shown) minus line 2 (correct basis); positive on line 4, negative on line 3"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}

  - id: sales.h_b_part
    printed: "(helper)"
    label: "Code B adjustment: the worksheet amount for box A, D, G or J; -0- for box B, E, H or K; none if code B does not apply"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sales.h_code_b, {const: true}]}
              - {op: test, eq: [sales.h_basis_reported, {const: true}]}
          then: sales.h_ws3_4
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sales.h_code_b, {const: true}]}
                - {op: test, eq: [sales.h_basis_reported, {const: true}]}
          then: sales.h_zero

  - id: sales.h_w_part
    printed: "(helper)"
    label: "Code W adjustment: the nondeductible wash sale loss as a positive number (-0- if no part of the loss is from a wash sale)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_code_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_code_w, {const: false}]}
          then: sales.h_zero

  - id: sales.h_loss
    printed: "(helper)"
    label: "Loss on the sale: correct basis minus proceeds (after any code B basis correction)"
    type: Dollars
    expr: {op: subtract, from: sales.correct_basis, take: sales.proceeds}

  - id: sales.h_wash_excess
    printed: "(helper)"
    label: "Wash sale loss entered is more than the loss on the sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_code_w, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss]}

  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment. If more than one code is entered in column (f), enter the net adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_b_part, sales.h_w_part]}
    refuses:
      - sales.special
      - sales.h_code_other
      - sales.h_aggregate_bad
      - {when: sales.h_wash_excess, when_known: true}
    shown_when: sales.h_g_shown
    note: "Net adjustment for codes B and W. Code B for box A/D/G/J is the worksheet amount: reported basis minus correct basis. Code W adds the nondeductible wash sale loss as a positive number. sales.special is refused because the section 1202 exclusion (code Q) is an adjustment in column (g) that this tool does not compute."

  - id: sales.h_de
    printed: "(helper)"
    label: "Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}

  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sales.h_de, sales.g]}
    shown_when: sales.h_on_8949

  - id: sales.one
    printed: "(helper)"
    label: "One (this transaction counted once)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface. It is read as a per-entry count of 1, so that other forms can count transactions with sum_over. It is supplied from the year parameter sales.one."
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
