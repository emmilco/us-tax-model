# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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

Second transcription's note: For box A, D, G or J the Note says to enter the basis as reported to the IRS (corrected through column (g) with code B). For box B, E, H or K the instructions say to enter the correct basis (code B, -0- in column (g)); for box C, F, I or L no broker basis exists, so the correct basis from records is entered. Collectibles (code C) and other codes are outside this slice and refused.

Ruling: model error and scope; i8949 p. 8, code B: "You received a Form 1099-B or Form 1099-DA (or substitute statement) and the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"; f8949 p. 1, box G; i1040sd p. 11, line 18 (collectibles). executable-triage-v2 (`reviews/2025/transcription/triage/sales.json`, written by triage.py this round; 1,495 fixtures, 500 generated returns seed 20261026, 510 partial records from 40 bases; 1,837 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, /tmp/adj-bklg-income/full/, same counts): 1,423 of 1,837 agree; 225 candidate-refuses, 188 candidate-unknown, 1 project-unknown; no value differences. (1) The reply adds boxes G and J to the reported-basis boxes, the source's reading; Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (fixture sales.refuse.digital.G passes: Form 1040 lines 7a and 16 refused on sales.digital), so it cannot reach a completed return. (2) All 44 completed-return differences are candidate-refuses on the reply's own consistency check h_basis_bad (box A, D, G or J, no code B, reported basis different from correct basis): classm.u1250.2 and its DeepSeek twin, classm.clcw26.2 (.deepseek), classm.f1040.2, .3 and .6 (and .deepseek), classm.s8812.2.deepseek, classm.f5695.2.deepseek, generated 20, 22, 89 (two sales), 90, 143, 145, 179, 188, 199, 236, 257, 269, 287, 312, 314, 345, 366, 402, 403, 411, 412, 429, 445, 453, 485, and six partials of classm.f1040.2 and classm.s8812.2.deepseek. On such an entry the project reads only the reported basis and the interview never asks sales.correct_basis (checked: classm.f1040.2 sales[s1], box A code none, reported $30,899, correct basis held $0; with correct_basis withheld, column (e) $30,899.00, Form 1040 line 7a $50,930.00 and line 16 $39,507.39 are unchanged). So every witness supplies an answer the interview cannot ask; the source routes an incorrect reported basis through code B, which the interview asks. (3) The other candidate-refuses (h_basis_bad 166, h_aggregate_bad 12, h_other 1, special 2) and the candidate-unknown (special, route, code, aggregate_eligible, reported_basis withheld) are on refused or incomplete records; the project refuses the same entries at sales.one (special, bad_aggregate, bad_code) or needs the same answers at the return: scope. The project-unknown is a partial of stage14.sep.step1_other_se_income withholding correct_basis on a refused return. The fix-round-2 finding F1 (an unanswered sales.special or sales.aggregate_eligible let the return complete) is fixed as BUG-0257: no candidate-unknown witness is now on a completed return (29 in fix round 2). The income package changed only the sales.special wording (PENDING-6: an interest in a partnership, S corporation or trust, including S corporation stock, that holds collectibles or section 1250 property), which matches i1040sd p. 11, line 18, "an interest in a partnership, S corporation, or trust ... attributable to unrealized appreciation of collectibles", and p. 12, line 19; a wider reading can only refuse. Project stands.

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

Second transcription's note: Net of the code B basis adjustment (Worksheet for Basis Adjustments, only for box A, D, G or J; -0- otherwise) and the code W nondeductible wash sale loss, per 'More than one code'. With code none the columns are left blank, held as zero.

Ruling: representation; i8949 p. 10, code W: "enter the amount of the nondeductible loss as a positive number in column (g)"; i8949 p. 8, code B. executable-triage-v2 (`reviews/2025/transcription/triage/sales.json`, written by triage.py this round; 1,495 fixtures, 500 generated returns seed 20261026, 510 partial records from 40 bases; 1,837 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, /tmp/adj-bklg-income/full/, same counts): 1,831 of 1,837 agree; the 6 differences are project-unknown on incomplete partial records withholding sales[].box, proceeds or correct_basis (partials of classm.asset.1 sales[s1], candidate $861.00, and classm.sdtw.4 sales[s2], candidate $361.00), answers the interview asks of every sale; the project's column (g) now reads them through its wash-sale check, the candidate's only when it needs them. No completed-return difference. The reply's own refusal h_wash_bad (code W or BW and wash-sale loss above max(0, correct basis less proceeds)) is the project's new gate within the interview: with no code B the interview does not ask the correct basis and the project uses the reported basis, the only basis it has. The income package's gate sales.wash_bad (code W, wash-sale loss above zero, and sales.wash_over = columns (d) less (e) plus the code B correction plus the wash-sale loss above zero) refuses at sales.w when the entered loss is larger than the loss on the sale: i8949 p. 10, code W, "You have a nondeductible loss from a wash sale" and "enter the amount of the nondeductible loss as a positive number in column (g)"; p550 p. 86, "A wash sale occurs when you sell or trade stock or securities at a loss". sales.wash_over is column (h), so the gate refuses exactly when column (h) would exceed zero; a wash-sale loss equal to the loss gives (h) $0 and is accepted (sales.adjust.A.W.equal_loss: (g) $200.00, (h) $0.00, line 7a $0.00, evaluated), and the code B correction counts toward the loss (sales.adjust.D.BW.wash_within_corrected_loss: (g) $500.00, (h) -$500.00, evaluated). It neither refuses an allowable entry nor admits an over-large one; no error introduced. Project stands.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.h_aggregate_bad, sales.h_basis_bad, sales.h_other, sales.special | sales.h_aggregate_bad, sales.h_basis_bad, sales.h_other, sales.special |
| (g) | sales.h_wash_bad | sales.h_wash_bad |
| (h) | sales.h_aggregate_bad, sales.h_basis_bad, sales.h_other, sales.h_wash_bad, sales.special | sales.h_aggregate_bad, sales.h_basis_bad, sales.h_other, sales.h_wash_bad, sales.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero (enter -0-)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sales.h_reported
    printed: "(helper)"
    label: "Box A, D, G or J: transaction reported on Form 1099-B or Form 1099-DA showing basis was reported to the IRS"
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
    label: "Code B in column (f): the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "B"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_has_w
    printed: "(helper)"
    label: "Code W in column (f): you have a nondeductible loss from a wash sale"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}

  - id: sales.h_other
    printed: "(helper)"
    label: "A code other than B or W applies (adjustment not computed by this tool)"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}

  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Reported directly on Schedule D line 1a or 8a (Exception 1) although the transaction does not meet its conditions: basis reported to the IRS, no adjustments or codes required"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, ne: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.h_reported, {const: false}]}

  - id: sales.h_basis_bad
    printed: "(helper)"
    label: "Basis reported to the IRS differs from the correct basis but code B is not entered"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_reported, {const: true}]}
        - {op: test, eq: [sales.h_has_b, {const: false}]}
        - {op: test, ne: [sales.reported_basis, sales.correct_basis]}

  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis. See the Note below and see Column (e) in the separate instructions."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_reported, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_reported, {const: false}]}
          then: sales.correct_basis
    refuses:
      - sales.special
      - sales.h_other
      - sales.h_aggregate_bad
      - {when: sales.h_basis_bad, when_known: true}
    note: "For box A, D, G or J the Note says to enter the basis as reported to the IRS (corrected through column (g) with code B). For box B, E, H or K the instructions say to enter the correct basis (code B, -0- in column (g)); for box C, F, I or L no broker basis exists, so the correct basis from records is entered. Collectibles (code C) and other codes are outside this slice and refused."

  - id: sales.h_basis_diff
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g), lines 3 and 4: basis shown on Form 1099-B or 1099-DA minus correct basis (positive if line 1 is larger, negative if line 2 is larger)"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}

  - id: sales.h_badj
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
              - {op: test, eq: [sales.h_reported, {const: true}]}
          then: sales.h_basis_diff
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sales.h_has_b, {const: true}]}
                - {op: test, eq: [sales.h_reported, {const: true}]}
          then: sales.h_zero

  - id: sales.h_loss
    printed: "(helper)"
    label: "Loss on this sale: column (e) after any code B correction less column (d); if zero or less, -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sales.correct_basis, take: sales.proceeds}

  - id: sales.h_wash_bad
    printed: "(helper)"
    label: "Nondeductible wash sale loss entered is more than the loss on the sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_has_w, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss]}

  - id: sales.h_wadj
    printed: "(helper)"
    label: "Code W adjustment: the amount of the nondeductible loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_has_w, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_has_w, {const: false}]}
          then: sales.h_zero

  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment. If more than one code in column (f), enter the net adjustment in column (g)."
    type: Dollars
    expr: {op: sum, of: [sales.h_badj, sales.h_wadj]}
    refuses:
      - {when: sales.h_wash_bad, when_known: true}
    note: "Net of the code B basis adjustment (Worksheet for Basis Adjustments, only for box A, D, G or J; -0- otherwise) and the code W nondeductible wash sale loss, per 'More than one code'. With code none the columns are left blank, held as zero."

  - id: sales.h_de
    printed: "(helper)"
    label: "Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}

  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr: {op: sum, of: [sales.h_de, sales.g]}

  - id: sales.one
    printed: "(helper)"
    label: "One (this transaction counted once)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface; read as a per-entry count of one so other forms can count transactions with sum_over. Taken from the year parameter sales.one (Count 1)."
```
```
