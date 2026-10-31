# Transcription agreement — sales

Second transcription of `Form 8949 and Schedule D — manually classified securities transactions` by an isolated model (spec 6.5), compared line by line with `forms/2025/sales.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
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

Ruling: scope and finding (F1); i8949 p. 8, code B: "You received a Form 1099-B or Form 1099-DA (or substitute statement) and the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i1040sd p. 11, line 18: "Collectibles include works of art, rugs, antiques, metals (such as gold, silver, and platinum bullion), gems, stamps, coins, alcoholic beverages, and certain other tangible property. Include on the worksheet any gain (but not loss) from the sale or exchange of an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles.". executable-triage-v2 (`reviews/2025/transcription/triage/sales.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 630 partial records from 40 bases; 2,245 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,166 of 2,245 agree; 70 candidate-unknown (28 completed), 7 value (none completed), 2 candidate-refuses (none completed). (1) The reply adds boxes G and J to the reported-basis boxes; the 7 values are all box G or J entries (generated 8, 21, 92, 160, 256, 357, 470), every one refused; Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (checked: sales.refuse.digital.G and generated 8, 21, 92, 160, 256, 357, 470 refuse Form 1040 lines 7a and 16 on sales.digital). (2) The 28 completed candidate-unknown are partial records withholding sales.special, which the reply declares on the line: Finding F1 (SCREEN-UNANSWERED-PASSES, `sales.findings.md`): with sales.special or sales.aggregate_eligible unanswered, sales.one is unknown, but sd.screen (sd.count < 0) evaluates false through the engine's Count lower-bound shortcut, so the return completes as if the screen were answered no; the candidate correctly needs the answer. Witnesses: partial(classm.f8889.1.deepseek -special), project Form 1040 line 16 $18,089.13 computed, candidate unknown; with special true the return refuses. (3) The candidate-refuses on special are on refused returns (sales.refuse.special, generated 380): scope. BUG-0231 widened only the sales.special question (shares of an exchange-traded fund or trust holding gold, silver, platinum or other metals), which matches i1040sd p. 11 ("metals" and an interest in a "trust ... attributable to unrealized appreciation of collectibles"); a wider reading of it can only refuse. Project stands on this line.

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

Ruling: scope and finding (F1); i8949 p. 8, code B: "You received a Form 1099-B or Form 1099-DA (or substitute statement) and the basis shown in box 1e on Form 1099-B or box 1g on Form 1099-DA is incorrect"; f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 10, code W: "You have a nondeductible loss from a wash sale ... enter the amount of the nondeductible loss as a positive number in column (g)". executable-triage-v2 (`reviews/2025/transcription/triage/sales.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 630 partial records from 40 bases; 2,245 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,172 of 2,245 agree; 70 candidate-unknown (28 completed), 3 candidate-refuses (none completed). The reply's code B correction also covers boxes G and J; Boxes G and J (and H, I, K, L) are refused for the return by sales.digital at sales.one (checked: sales.refuse.digital.G and generated 8, 21, 92, 160, 256, 357, 470 refuse Form 1040 lines 7a and 16 on sales.digital). No value differs. The 28 completed candidate-unknown are the F1 partial records withholding sales.special: Finding F1 (SCREEN-UNANSWERED-PASSES, `sales.findings.md`): with sales.special or sales.aggregate_eligible unanswered, sales.one is unknown, but sd.screen (sd.count < 0) evaluates false through the engine's Count lower-bound shortcut, so the return completes as if the screen were answered no; the candidate correctly needs the answer. Witnesses: partial(classm.f8889.1.deepseek -special), project Form 1040 line 16 $18,089.13 computed, candidate unknown; with special true the return refuses. The candidate-refuses (special, h_code_other) are on refused returns, where the project refuses at sales.one on special and bad_code: scope. BUG-0231 widened only the sales.special question (shares of an exchange-traded fund or trust holding gold, silver, platinum or other metals), which matches i1040sd p. 11 ("metals" and an interest in a "trust ... attributable to unrealized appreciation of collectibles"); a wider reading of it can only refuse. Project stands on this line.

### (h) — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| (e) | sales.special | sales.special |
| (g) | sales.h_code_other, sales.special | sales.h_code_other, sales.special |
| (h) | sales.h_code_other, sales.special | sales.h_code_other, sales.special |

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
    refuses: [sales.special]
  - id: sales.g
    printed: "(g)"
    label: "Amount of adjustment"
    type: Dollars
    expr:
      op: sum
      of: [sales.h_basis_adjust, sales.h_wash_adjust]
    refuses: [sales.h_code_other, sales.special]
  - id: sales.h
    printed: "(h)"
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)."
    type: Dollars
    expr:
      op: sum
      of: [sales.h_net, sales.g]
    refuses: [sales.h_code_other, sales.special]
  - id: sales.one
    printed: "(helper)"
    label: "One transaction (count)"
    type: Count
    expr:
      op: param
      ref: sales.one
  - id: sales.h_basis_reported
    printed: "(helper)"
    label: "Basis reported to the IRS (box A, D, G, or J)"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.box, {const: "A"}]
        - op: test
          eq: [sales.box, {const: "D"}]
        - op: test
          eq: [sales.box, {const: "G"}]
        - op: test
          eq: [sales.box, {const: "J"}]
  - id: sales.h_code_has_b
    printed: "(helper)"
    label: "Adjustment code includes B"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.code, {const: "B"}]
        - op: test
          eq: [sales.code, {const: "BW"}]
  - id: sales.h_code_has_w
    printed: "(helper)"
    label: "Adjustment code includes W"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sales.code, {const: "W"}]
        - op: test
          eq: [sales.code, {const: "BW"}]
  - id: sales.h_code_other
    printed: "(helper)"
    label: "Adjustment code is other"
    type: Bool
    expr:
      op: test
      eq: [sales.code, {const: "other"}]
  - id: sales.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: sales.h_basis_diff
    printed: "(helper)"
    label: "Reported basis minus correct basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.reported_basis
      take: sales.correct_basis
  - id: sales.h_basis_adjust
    printed: "(helper)"
    label: "Basis adjustment for code B"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [sales.h_code_has_b, {const: true}]
              - op: test
                eq: [sales.h_basis_reported, {const: true}]
          then: sales.h_basis_diff
        - guard:
            op: test
            not:
              op: test
              all:
                - op: test
                  eq: [sales.h_code_has_b, {const: true}]
                - op: test
                  eq: [sales.h_basis_reported, {const: true}]
          then: sales.h_zero
  - id: sales.h_wash_adjust
    printed: "(helper)"
    label: "Wash-sale adjustment for code W"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sales.h_code_has_w, {const: true}]
          then: sales.wash_loss
        - guard:
            op: test
            eq: [sales.h_code_has_w, {const: false}]
          then: sales.h_zero
  - id: sales.h_net
    printed: "(helper)"
    label: "Proceeds minus cost or other basis"
    type: Dollars
    expr:
      op: subtract
      from: sales.proceeds
      take: sales.e
```
