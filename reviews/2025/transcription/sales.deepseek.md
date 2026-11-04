# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a8cd34c6fb7d1b8d595b5e7c8e5b1274c7ac36118dff9fea922fe4cb09695ede |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f92e2cebe15b275f8548d9ec717c576dc10c17d269616952633fa6f2369a62b7 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 526da6484d7cf5571478ec088110c6d248f80db63e86557756d94644e6b90e97 |
| printed lines compared | 4 |
| agree / disagree / missing | 2 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### sales.one — Screen this transaction before any aggregation
Status: **AGREE**

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

Ruling: scope; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. executable-triage-v2 (`reviews/2025/transcription/triage/sales.deepseek.json`, written by triage.py this round; 1,495 fixtures, 500 generated returns seed 20261026, 510 partial records from 40 bases; 1,837 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, /tmp/adj-bklg-income/full/, same counts): 1,828 of 1,837 agree; 7 value, 1 candidate-unknown, 1 project-unknown, all on refused returns, none on a completed return. The reply adds boxes G and J to the reported-basis boxes; the 7 values are all box G or J entries (generated 8 sales[s1] $2,853.86 against $2,224.76, 21 s2, 92 s1, 160 s2, 256 s3, 357 s1, 470 s1), every one refused: Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (fixture sales.refuse.digital.G passes: Form 1040 lines 7a and 16 refused on sales.digital). The unknowns are partials of stage14.sep.step1_other_se_income withholding reported_basis (candidate) or correct_basis (project), on a refused return. The fix-round-2 finding F1 (an unanswered sales.special or sales.aggregate_eligible let the return complete) is fixed as BUG-0257: no candidate-unknown witness is now on a completed return (29 in fix round 2). Project stands.

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

Ruling: scope; i8949 p. 10, code W; i8949 p. 8, code B. executable-triage-v2 (`reviews/2025/transcription/triage/sales.deepseek.json`, written by triage.py this round; 1,495 fixtures, 500 generated returns seed 20261026, 510 partial records from 40 bases; 1,837 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, /tmp/adj-bklg-income/full/, same counts): 1,827 of 1,837 agree; 3 project-refuses, 1 candidate-refuses, 6 project-unknown; none on a completed return. The 3 project-refuses are the new gate sales.wash_bad at sales.w (sales.refuse.wash_over_loss: proceeds $1,000, basis $1,200, wash $449, candidate (g) $449.00; generated 256 sales[s2], candidate $121.39; generated 310 sales[s3], candidate $26.75); the reply declares the same limit on column (h) (h_wash_too_big: wash-sale loss above max(0, basis less proceeds), with the corrected basis for code B), so it refuses the same entries one line later and the return is refused either way. The candidate-refuses is h_code_other on sales.refuse.code, which the project refuses at sales.one (sales.bad_code). The project-unknown are the partials of classm.asset.1 and classm.sdtw.4 withholding box, proceeds or correct_basis, answers asked of every sale. The income package's gate sales.wash_bad (code W, wash-sale loss above zero, and sales.wash_over = columns (d) less (e) plus the code B correction plus the wash-sale loss above zero) refuses at sales.w when the entered loss is larger than the loss on the sale: i8949 p. 10, code W, "You have a nondeductible loss from a wash sale" and "enter the amount of the nondeductible loss as a positive number in column (g)"; p550 p. 86, "A wash sale occurs when you sell or trade stock or securities at a loss". sales.wash_over is column (h), so the gate refuses exactly when column (h) would exceed zero; a wash-sale loss equal to the loss gives (h) $0 and is accepted (sales.adjust.A.W.equal_loss: (g) $200.00, (h) $0.00, line 7a $0.00, evaluated), and the code B correction counts toward the loss (sales.adjust.D.BW.wash_within_corrected_loss: (g) $500.00, (h) -$500.00, evaluated). It neither refuses an allowable entry nor admits an over-large one; no error introduced. Project stands.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (g) | sales.h_code_other | sales.h_code_other |
| (h) | sales.h_code_other, sales.h_wash_too_big, sales.special | sales.h_code_other, sales.h_wash_too_big, sales.special |

## Raw second transcription

```yaml
lines:
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. See the Note below and see Column (e) in the separate instructions."
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
  - id: sales.g
    printed: "(g)"
    label: "Adjustment, if any, to gain or loss — Amount of adjustment"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sales.code, {const: "none"}]
          then: sales.h_zero
        - guard:
            op: test
            eq: [sales.code, {const: "W"}]
          then: sales.wash_loss
        - guard:
            op: test
            eq: [sales.code, {const: "B"}]
          then: sales.h_basis_adj
        - guard:
            op: test
            eq: [sales.code, {const: "BW"}]
          then: sales.h_g_BW_sum
        - guard:
            op: test
            eq: [sales.code, {const: "other"}]
          then: sales.h_zero
    refuses: [sales.h_code_other]
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr:
      op: sum
      of: [sales.h_raw, sales.g]
    refuses:
      - sales.special
      - when: sales.h_wash_too_big
        when_known: true
  - id: sales.one
    printed: "(helper)"
    label: "One transaction"
    type: Count
    expr: {op: param, ref: sales.one}
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_basis_reported
    printed: "(helper)"
    label: "Basis was reported to the IRS"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.box, {const: "A"}]}
        - {op: test, eq: [sales.box, {const: "G"}]}
        - {op: test, eq: [sales.box, {const: "D"}]}
        - {op: test, eq: [sales.box, {const: "J"}]}
  - id: sales.h_code_other
    printed: "(helper)"
    label: "Adjustment code other than none, B, W or BW"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_basis_diff
    printed: "(helper)"
    label: "Reported basis less correct basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.reported_basis
      take: sales.correct_basis
  - id: sales.h_basis_adj
    printed: "(helper)"
    label: "Basis adjustment (zero when basis was not reported to the IRS)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sales.h_basis_reported, {const: true}]
          then: sales.h_basis_diff
        - guard:
            op: test
            eq: [sales.h_basis_reported, {const: false}]
          then: sales.h_zero
  - id: sales.h_g_BW_sum
    printed: "(helper)"
    label: "Combined basis and wash-sale adjustments"
    type: Dollars
    expr:
      op: sum
      of: [sales.h_basis_adj, sales.wash_loss]
  - id: sales.h_raw
    printed: "(helper)"
    label: "Column (d) less column (e)"
    type: Dollars
    expr:
      op: subtract
      from: sales.proceeds
      take: sales.e
  - id: sales.h_basis_for_loss
    printed: "(helper)"
    label: "Basis after any code B correction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sales.code, {const: "B"}]
          then: sales.correct_basis
        - guard:
            op: test
            eq: [sales.code, {const: "BW"}]
          then: sales.correct_basis
        - guard:
            op: test
            eq: [sales.code, {const: "none"}]
          then: sales.e
        - guard:
            op: test
            eq: [sales.code, {const: "W"}]
          then: sales.e
        - guard:
            op: test
            eq: [sales.code, {const: "other"}]
          then: sales.e
  - id: sales.h_loss_pos
    printed: "(helper)"
    label: "Loss on the sale after code B correction, not below zero"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sales.h_basis_for_loss
      take: sales.proceeds
  - id: sales.h_wash_too_big
    printed: "(helper)"
    label: "Wash-sale loss exceeds the loss on the sale"
    type: Bool
    expr:
      op: test
      gt: [sales.wash_loss, sales.h_loss_pos]
```
