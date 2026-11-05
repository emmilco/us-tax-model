# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-04); see Line-scoped reviews |
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
Reviewed in: pass 82f67b365891

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

Ruling: scope; same reply and project as the round-2 ruling: the reply adds boxes G and J to the reported-basis boxes; boxes G to L are refused at the transaction by sales.digital at sales.one. Scratch run of triage.mjs on the round-3 reply (.transcription/sales.deepseek.lines-ceb969c79173) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 476 partial records; 1,762 comparisons per line): 1,755 agree; the 7 value differences are on refused returns. Project stands.
Reviewed in: pass 82f67b365891

### (g) — Column (g): net adjustments
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.reported_basis"}, "op": "subtract", "take": {"input": "sales.correct_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "sales.correct_basis"}, "op": "subtract", "take": {"input": "sales.reported_basis"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "A"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "D"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "G"}, {"input": "sales.box"}], "test": "ne"}, {"args": [{"const": "J"}, {"input": "sales.box"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "B"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "ne"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "BW"}, {"input": "sales.code"}], "test": "eq"}, {"args": [{"const": "W"}, {"input": "sales.code"}], "test": "eq"}], "test": "any"}, "then": {"input": "sales.wash_loss"}}], "op": "choose"}], "op": "sum"}
```

Second transcription's note: The tool computes the code B basis adjustment and the code W wash-sale adjustment, including BW. Any other adjustment code is refused because its adjustment amount is not supplied.

Ruling: scope; i8949 p. 8, code B, and p. 10, code W. The reply computes the code B correction and the code W adjustment and refuses any other code, as the project does: codes other than B and W are refused at sales.one on sales.bad_code ("Only applicable B and W adjustments are supported"). On every transaction the tool completes, the values are the project's.
Reviewed in: pass 82f67b365891

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**
Reviewed in: pass f71b3c0cac42

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (g) | sales.code_other | sales.code_other |
| (h) | sales.h_code_other | sales.h_code_other |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sales.one | a70b7497279033c84a840775fe2abf33e7dc779b790b06545bb95616abb2a372 |
| (e) | 928d0501e109c53449f47130796703fdca3be62e5ad5cfa8a75b4e411545cce6 |
| (g) | e345be671a45479e4277d1d58ae8e8cb4073bac0b4df3cb8d74cc84d48424fa9 |
| (h) | 99ee2a26d2615b358c59742db7fe5cb7211304df3fd2300bdc0b375bc504b241 |
| (rest of the document) | d66e458afa5745f8eec417fb8e25dc768244f7e1dca0d2d0114dfbf47d7cba76 |

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

#### Pass 82f67b365891

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sales.one, (e), (g) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 82f67b365891364aa417b7fd4e8a4b577ea4bb726391d9f2e2b747f0daef7293 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 047e2ddce85a8f2dd998a938dc30003faa470ea2cc1d1ab2be73309c059f1242 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 10e81b0fbbbbf993304fc7fb28ca20036c90e081855ba9d3d71412ee85a9bc3c |
| receipt | .transcription/sales.deepseek.lines-efadd99d9686 |
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
            eq: [sales.basis_reported, {const: true}]
          then: sales.reported_basis
        - guard:
            op: test
            eq: [sales.basis_reported, {const: false}]
          then: sales.correct_basis

  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr:
      op: sum
      of: [sales.g_basis, sales.g_wash]
    refuses: [sales.code_other]
    note: "The tool computes the code B basis adjustment and the code W wash-sale adjustment, including BW. Any other adjustment code is refused because its adjustment amount is not supplied."

  - id: sales.one
    printed: "(helper)"
    label: "One sale transaction"
    type: Count
    expr: {op: param, ref: sales.one}

  - id: sales.basis_reported
    printed: "(helper)"
    label: "Basis was reported to the IRS on the broker statement"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sales.code_b
    printed: "(helper)"
    label: "Adjustment code is B or BW"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.code_w
    printed: "(helper)"
    label: "Adjustment code is W or BW"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.code_other
    printed: "(helper)"
    label: "Adjustment code is other"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}

  - id: sales.g_zero
    printed: "(helper)"
    label: "Zero adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.g_basis_diff
    printed: "(helper)"
    label: "Correct basis minus reported basis"
    type: Dollars
    expr: {op: subtract, from: sales.correct_basis, take: sales.reported_basis}

  - id: sales.g_basis
    printed: "(helper)"
    label: "Code B basis adjustment"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sales.code_b, {const: true}]}
              - {op: test, eq: [sales.basis_reported, {const: true}]}
          then: sales.g_basis_diff
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sales.code_b, {const: true}]}
                - {op: test, eq: [sales.basis_reported, {const: true}]}
          then: sales.g_zero

  - id: sales.g_wash
    printed: "(helper)"
    label: "Code W wash-sale adjustment"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.code_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.code_w, {const: false}]}
          then: sales.g_zero
```

#### Pass f71b3c0cac42

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines sales.one, (e), (g), (h) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | cd390cff7bf21b1e217b7e738e711569f4310fcc5dbebbf0fe9d5e00bf242be0 |
| receipt | .transcription/sales.deepseek.lines-ceb969c79173 |
| printed lines compared | 4 |
| agree / disagree / missing | 2 / 2 / 0 |
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
lines:
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. See the Note below and see Column (e) in the separate instructions."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_basis_reported, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_basis_reported, {const: false}]}
          then: sales.correct_basis
    note: "Column (e) uses the basis shown on the broker report for boxes A, D, G and J, where basis was reported to the IRS; otherwise it uses the correct basis from records."
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.code, {const: "none"}]}
          then: sales.h_g_zero
        - guard: {op: test, eq: [sales.code, {const: "B"}]}
          then: sales.h_basis_adjust
        - guard: {op: test, eq: [sales.code, {const: "W"}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.code, {const: "BW"}]}
          then: sales.h_g_bw
        - guard: {op: test, eq: [sales.code, {const: "other"}]}
          then: sales.h_g_zero
    refuses: [sales.h_code_other]
    note: "Code other, such as code E for an unreflected selling expense or option premium, needs an adjustment amount not supplied by this interface; the line refuses when sales.code is other."
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr:
      op: sum
      of: [sales.h_before_adjustment, sales.g]
    refuses: [sales.h_code_other]
  - id: sales.one
    printed: "(helper)"
    label: "One sale"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "Per-sale count of one, used to count sales entries in a collection."
  - id: sales.h_basis_reported
    printed: "(helper)"
    label: "Basis was reported to the IRS for this box"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sales.h_code_other
    printed: "(helper)"
    label: "Adjustment code is other"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_g_zero
    printed: "(helper)"
    label: "Zero adjustment"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_basis_adjust
    printed: "(helper)"
    label: "Basis adjustment"
    type: Dollars
    expr:
      op: subtract
      from: sales.reported_basis
      take: sales.correct_basis
  - id: sales.h_g_bw
    printed: "(helper)"
    label: "Basis and wash-sale adjustment"
    type: Dollars
    expr:
      op: sum
      of: [sales.h_basis_adjust, sales.wash_loss]
  - id: sales.h_before_adjustment
    printed: "(helper)"
    label: "Proceeds minus cost or other basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.proceeds
      take: sales.e
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
