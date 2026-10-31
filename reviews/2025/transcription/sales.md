# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5117a362888b3152c18cc46ad0dc2b4f386694e69ccb6d4dab7797bb216f241f |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 48fd04b4cb62f464c46ee96edcfca2e5ace1cedfad39e8a717d194924162bfcb |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | c177a67ab70473e97cf0386866ab53d29cf069a64bd59c531f548e1350c1924e |
| printed lines compared | 4 |
| agree / disagree / missing | 2 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |

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

Second transcription's note: Boxes A, D, G and J enter the basis shown on the statement, even if incorrect. Boxes B, E, H and K enter the correct basis, and boxes C, F, I and L, which have no statement, are read as also entering the correct basis.

Ruling: model error, finding (F1) and scope; i8949 p. 8, code B: "You received a Form 1099-B or Form 1099-DA (or substitute statement) and the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i1040sd p. 11, line 18: "Collectibles include works of art, rugs, antiques, metals (such as gold, silver, and platinum bullion), gems, stamps, coins, alcoholic beverages, and certain other tangible property. Include on the worksheet any gain (but not loss) from the sale or exchange of an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles.". executable-triage-v2 (`reviews/2025/transcription/triage/sales.json`; 1,382 fixtures, 500 generated returns seed 20261026, 630 partial records from 40 bases; 2,245 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,739 of 2,245 agree; 298 candidate-refuses (70 completed), 208 candidate-unknown (29 completed). (1) The reply adds boxes G and J to the reported-basis boxes, the source's reading; Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (checked: sales.refuse.digital.G and generated 8, 21, 92, 160, 256, 357, 470 refuse Form 1040 lines 7a and 16 on sales.digital), so the difference cannot reach a completed return. (2) The 70 completed candidate-refuses are the reply's own consistency check h_basis_uncoded (box A or D, code none or W, reported basis different from correct basis): on such an entry the project reads only the reported basis, and the interview never asks sales.correct_basis (checked on classm.s3.2 sales[s1], box D code none: withheld, the interview completes), so every witness supplies an answer the interview cannot ask (classm.s3.2, classm.f1040.6, classm.f5695.2, classm.u1250.2, classm.clcw26.2 and partials; generated 236, 287, 453). The source routes an incorrect reported basis through code B, which the interview asks; no tax reading is at stake. (3) The 29 completed candidate-unknown are partial records withholding sales.special (28) or sales.aggregate_eligible (1): Finding F1 (SCREEN-UNANSWERED-PASSES, `sales.findings.md`): with sales.special or sales.aggregate_eligible unanswered, sales.one is unknown, but sd.screen (sd.count < 0) evaluates false through the engine's Count lower-bound shortcut, so the return completes as if the screen were answered no; the candidate correctly needs the answer. Witnesses: partial(classm.f8889.1.deepseek -special), project Form 1040 line 16 $18,089.13 computed, candidate unknown; with special true the return refuses. (4) The candidate-refuses on refused returns (special, h_aggregate_bad, h_code_other) are gates the project also has at sales.one; the incomplete-return unknowns are partial records: scope. BUG-0231 widened only the sales.special question (shares of an exchange-traded fund or trust holding gold, silver, platinum or other metals), which matches i1040sd p. 11 ("metals" and an interest in a "trust ... attributable to unrealized appreciation of collectibles"); a wider reading of it can only refuse. Project stands on this line.

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

Second transcription's note: With more than one code, column (g) is the net adjustment. For code BW, the basis adjustment and wash sale loss are added, each with its own sign.

Ruling: model error, finding (F1) and scope; i8949 p. 8, code B: "You received a Form 1099-B or Form 1099-DA (or substitute statement) and the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 10, code W: "You have a nondeductible loss from a wash sale ... enter the amount of the nondeductible loss as a positive number in column (g)"; i8949 p. 10: "If no part of the loss is a nondeductible loss from a wash sale transaction, enter -0- in column (g)." executable-triage-v2 (`reviews/2025/transcription/triage/sales.json`; 1,382 fixtures, 500 generated returns seed 20261026, 630 partial records from 40 bases; 2,245 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,742 of 2,245 agree; 361 candidate-refuses (87 completed), 142 candidate-unknown (29 completed). (1) Boxes G and J take the code B correction in the reply; Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (checked: sales.refuse.digital.G and generated 8, 21, 92, 160, 256, 357, 470 refuse Form 1040 lines 7a and 16 on sales.digital). (2) 70 completed candidate-refuses are h_basis_uncoded, as on column (e): the correct basis is an answer the interview does not ask on a box A or D entry without code B. (3) 17 completed candidate-refuses are h_wash_excess, a limit the reply's own note says the instructions "do not state": classm.s3.2 sales[s3] (box C, code W, proceeds $55,549, basis $20,475, a gain, wash loss $449: project (g) $449.00) and its twin and partials, and generated 20, 73, 226, 346, 429, 433. The source names no such refusal; a wash-sale loss entered on a gain sale is an inconsistent record (observation O1 in `sales.findings.md`), not a tax reading. (4) The 29 completed candidate-unknown are the F1 partials (special 28, aggregate_eligible 1). Finding F1 (SCREEN-UNANSWERED-PASSES, `sales.findings.md`): with sales.special or sales.aggregate_eligible unanswered, sales.one is unknown, but sd.screen (sd.count < 0) evaluates false through the engine's Count lower-bound shortcut, so the return completes as if the screen were answered no; the candidate correctly needs the answer. Witnesses: partial(classm.f8889.1.deepseek -special), project Form 1040 line 16 $18,089.13 computed, candidate unknown; with special true the return refuses. (5) The other candidate-refuses (h_wash_uncoded, special, h_aggregate_bad, h_code_other) are on refused or incomplete returns: scope. BUG-0231 widened only the sales.special question (shares of an exchange-traded fund or trust holding gold, silver, platinum or other metals), which matches i1040sd p. 11 ("metals" and an interest in a "trust ... attributable to unrealized appreciation of collectibles"); a wider reading of it can only refuse. Project stands on this line.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.special | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.special |
| (g) | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.h_wash_excess, sales.h_wash_uncoded, sales.special | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.h_wash_excess, sales.h_wash_uncoded, sales.special |
| (h) | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.h_wash_excess, sales.h_wash_uncoded, sales.special | sales.h_aggregate_bad, sales.h_basis_uncoded, sales.h_code_other, sales.h_wash_excess, sales.h_wash_uncoded, sales.special |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sales.one
    printed: "(helper)"
    label: "One transaction (a count of 1 for this entry)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "The IRS pages do not define this interface. Read from its name, type and the sales.one parameter as a per-entry count of 1 for totals over the collection."
  - id: sales.h_zero
    printed: "(helper)"
    label: "Enter -0-"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sales.h_basis_reported_box
    printed: "(helper)"
    label: "Box A, D, G or J: transaction reported on a statement showing basis was reported to the IRS"
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
    label: "An adjustment code other than B or W applies"
    type: Bool
    expr: {op: test, eq: [sales.code, {const: "other"}]}
  - id: sales.h_aggregate_bad
    printed: "(helper)"
    label: "Reported directly on Schedule D, line 1a or 8a, but the conditions of Exception 1 are not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.route, {const: "aggregate"}]}
        - op: test
          any:
            - {op: test, eq: [sales.aggregate_eligible, {const: false}]}
            - {op: test, eq: [sales.h_basis_reported_box, {const: false}]}
            - {op: test, ne: [sales.code, {const: "none"}]}
    note: "Exception 1 applies only where basis was reported to the IRS and no adjustments are needed, so this route is limited to boxes A, D, G and J with no code."
  - id: sales.h_basis_uncoded
    printed: "(helper)"
    label: "The basis reported to the IRS is incorrect, but code B was not entered"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [sales.code, {const: "none"}]}
            - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, ne: [sales.reported_basis, sales.correct_basis]}
  - id: sales.h_uses_basis_adjustment
    printed: "(helper)"
    label: "Code B on a transaction whose basis was reported to the IRS: correct the error by an adjustment in column (g)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [sales.code, {const: "B"}]}
            - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_not_basis_adjustment
    printed: "(helper)"
    label: "No basis adjustment is entered in column (g)"
    type: Bool
    expr:
      op: test
      not: {op: test, eq: [sales.h_uses_basis_adjustment, {const: true}]}
  - id: sales.h_uses_wash
    printed: "(helper)"
    label: "Code W: you have a nondeductible loss from a wash sale"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sales.code, {const: "W"}]}
        - {op: test, eq: [sales.code, {const: "BW"}]}
  - id: sales.h_not_wash
    printed: "(helper)"
    label: "No wash sale adjustment is entered in column (g)"
    type: Bool
    expr:
      op: test
      not: {op: test, eq: [sales.h_uses_wash, {const: true}]}
  - id: sales.h_wash_uncoded
    printed: "(helper)"
    label: "A nondeductible wash sale loss was entered, but code W was not entered"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_not_wash, {const: true}]}
        - {op: test, gt: [sales.wash_loss, {const: 0}]}
  - id: sales.h_loss_before_wash
    printed: "(helper)"
    label: "Loss on the sale figured with the correct basis, if any"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sales.correct_basis, take: sales.proceeds}
  - id: sales.h_wash_excess
    printed: "(helper)"
    label: "The nondeductible wash sale loss is more than the loss on the sale"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sales.h_uses_wash, {const: true}]}
        - {op: test, gt: [sales.wash_loss, sales.h_loss_before_wash]}
    note: "The instructions do not state this limit directly. It is inferred from code W describing a nondeductible part of a loss, and is used only as a consistency check."
  - id: sales.e
    printed: "(e)"
    label: "Cost or other basis"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_basis_reported_box, {const: true}]}
          then: sales.reported_basis
        - guard: {op: test, eq: [sales.h_basis_reported_box, {const: false}]}
          then: sales.correct_basis
    refuses:
      - sales.special
      - sales.h_code_other
      - sales.h_aggregate_bad
      - {when: sales.h_basis_uncoded, when_known: true}
    note: "Boxes A, D, G and J enter the basis shown on the statement, even if incorrect. Boxes B, E, H and K enter the correct basis, and boxes C, F, I and L, which have no statement, are read as also entering the correct basis."
  - id: sales.h_basis_difference
    printed: "(helper)"
    label: "Worksheet for Basis Adjustments in Column (g): line 1 less line 2 (positive for line 4, negative for line 3)"
    type: Dollars
    expr: {op: subtract, from: sales.reported_basis, take: sales.correct_basis}
  - id: sales.h_basis_adjustment
    printed: "(helper)"
    label: "Basis adjustment to include in column (g)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_uses_basis_adjustment, {const: true}]}
          then: sales.h_basis_difference
        - guard: {op: test, eq: [sales.h_not_basis_adjustment, {const: true}]}
          then: sales.h_zero
  - id: sales.h_wash_adjustment
    printed: "(helper)"
    label: "Amount of the nondeductible wash sale loss as a positive number in column (g)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sales.h_uses_wash, {const: true}]}
          then: sales.wash_loss
        - guard: {op: test, eq: [sales.h_not_wash, {const: true}]}
          then: sales.h_zero
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr: {op: sum, of: [sales.h_basis_adjustment, sales.h_wash_adjustment]}
    refuses:
      - sales.special
      - sales.h_code_other
      - sales.h_aggregate_bad
      - {when: sales.h_basis_uncoded, when_known: true}
      - {when: sales.h_wash_uncoded, when_known: true}
      - {when: sales.h_wash_excess, when_known: true}
    note: "With more than one code, column (g) is the net adjustment. For code BW, the basis adjustment and wash sale loss are added, each with its own sign."
  - id: sales.h_proceeds_less_basis
    printed: "(helper)"
    label: "Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)"
    type: Dollars
    expr: {op: subtract, from: sales.proceeds, take: sales.e}
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr: {op: sum, of: [sales.h_proceeds_less_basis, sales.g]}
    refuses:
      - sales.special
      - sales.h_code_other
      - sales.h_aggregate_bad
```
```
