# Review record c5a29f6ba958 — transcription asset

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "asset",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v2",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "1a6cc33f5c1b65a6fbe5bfea204a207616309d6c532a1868657a5d2b533dc1b4",
 "response_sha256": "18982af9cbd3bfe99c37e42237cb5e5c80ae3908be5c81a8ab327af3505bb71b",
 "scope": [
  "asset.s179_2025",
  "asset.mq_q4",
  "asset.mq_total",
  "asset.cost179",
  "(d)",
  "(c)",
  "14",
  "26(i)",
  "19(c)",
  "19(g)",
  "17"
 ],
 "subjects": {
  "(c)": "bc9de339fc485275d7156c04bee4569a5fba391be6c61599d5ddb69a0b588fff",
  "(d)": "bf97394c0e6baab938fcd0e3d20a43fbde9be75543375088439981eb869fffbd",
  "14": "f0b3ee6fdcdf3f0510b462afe146a14650fd5a3f89dfa400e47bc1c7bed13afb",
  "17": "15055efa46a9a94503cec45d406a31b8c776bbc51856d9c6e24c3f04f79ab845",
  "19(c)": "e50cd4ebbf48a226e858fe9d5772e30f2adf8b6f32684123b987276d9325d2ae",
  "19(g)": "72b10ee69008989e999a67afed25a2f35c1715a89bffcdcb46ea407b4f9bbb8f",
  "26(i)": "bfa4f5427351d355d49391efa8d6a1f51bbb645321ca6d40f03a8963fac8ea36",
  "asset.cost179": "41f30e93582149a59b2d6f10c20abd7a09226ee7d3ed678ac0684f8fe63f5d46",
  "asset.mq_q4": "b6c84a078ff224029085f928d76a1067ad9961fb9a0cae8f268f91ac4f93c99f",
  "asset.mq_total": "3b0891ec90ebbf0c72602103ff506731602554c0d32cbfa0c643fcbf8a67bde4",
  "asset.s179_2025": "55d15cfd0c53f715096654a72bd72e6e0e3d7bcf7c358df0c4e9b33b0de7f7b8"
 }
}
```

<!-- part block -->
#### Pass 1a6cc33f5c1b

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines asset.s179_2025, asset.mq_q4, asset.mq_total, asset.cost179, (d), (c), 14, 26(i), 19(c), 19(g), 17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1a6cc33f5c1b65a6fbe5bfea204a207616309d6c532a1868657a5d2b533dc1b4 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a483087e885a3b0266f9a4dbe6d46cf79453754249da1412d90affce50688806 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 56881f98779dba292d7a1f71e479f46b4962455ced12f63b0a9d1d15f38bd1ff |
| receipt | .transcription/asset.lines-3b3c9e0f5ac1 |
| printed lines compared | 11 |
| agree / disagree / missing | 2 / 9 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 31, 32, 33, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 32, 33, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line1a, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | s1 |
| shared page | f4562, mq, person, s179, sc, scveh |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: asset.period
    printed: "(d)"
    label: "Recovery period (GDS recovery period from the Table of Class Lives and Recovery Periods, Pub. 946 Appendix B)"
    type: Enum(macrs_period)
    expr: {op: keyed_lookup, table: class_lives, keys: [asset.class]}
    refuses: [asset.screen]

  - id: asset.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: asset.h_cent
    printed: "(helper)"
    label: "One cent (to express the business use percentage as money)"
    type: NonNegDollars
    expr: {op: param, ref: sc.one_cent}

  - id: asset.h_pct_c
    printed: "(helper)"
    label: "Business/investment use percentage, as a number of cents"
    type: NonNegDollars
    expr: {op: multiply_count, amount: asset.h_cent, count: asset.pct}

  - id: asset.h_bus_cost
    printed: "(helper)"
    label: "Multiply the cost or other basis of the property by the percentage of business/investment use"
    type: NonNegDollars
    expr: {op: prorate, amount: asset.cost, part: asset.h_pct_c, whole: {param: sc.hundred_cents}, places: 2}
    refuses: [asset.screen]

  - id: asset.h_is2025
    printed: "(helper)"
    label: "Placed in service during the tax year beginning in 2025"
    type: Bool
    expr: {op: test, eq: [asset.placed, {const: "y2025"}]}

  - id: asset.h_on19
    printed: "(helper)"
    label: "Reported on lines 19a through 19h (placed in service in 2025, not listed property)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: false}]}

  - id: asset.h_on17
    printed: "(helper)"
    label: "Reported on line 17 (placed in service before 2025, not listed property)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: false}]}
        - {op: test, eq: [asset.listed, {const: false}]}

  - id: asset.h_on26
    printed: "(helper)"
    label: "Reported on line 26 (listed property placed in service in 2025)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.listed, {const: true}]}

  - id: asset.h_outside
    printed: "(helper)"
    label: "Recovery period is not one of 3, 5, 7, 10, 15 or 20 years under the percentage tables"
    type: Bool
    expr: {op: test, eq: [asset.period, {const: "outside"}]}

  - id: asset.h_s179_over
    printed: "(helper)"
    label: "Elected section 179 cost is more than the business cost of the property"
    type: Bool
    expr: {op: test, gt: [asset.s179, asset.h_bus_cost]}

  - id: asset.h_s179_inelig
    printed: "(helper)"
    label: "Section 179 cost elected for property that does not qualify (not section 179 property, or not used more than 50% in the business)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [asset.s179, {const: 0}]}
        - op: test
          any:
            - {op: test, eq: [asset.not179, {const: true}]}
            - {op: test, le: [asset.pct, {const: 50, type: Count}]}

  - id: asset.h_bonus_mixed
    printed: "(helper)"
    label: "Special allowance choice differs within the same class of 2025 property"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.bonus_same, {const: false}]}

  - id: asset.h_bonus_base
    printed: "(helper)"
    label: "Depreciable basis for the special depreciation allowance: business/investment portion of cost minus the section 179 expense deduction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.s179}
    note: "The basis is reduced by the elected section 179 cost (line 6(c) / 26(i)) for this property, not by an allocated share of the business-income-limited line 12; the text says to reduce by 'the section 179 expense deduction' without allocating line 12 among properties."

  - id: asset.h_bonus40
    printed: "(helper)"
    label: "40% special depreciation allowance"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.h_bonus_base, rate: {param: sc.bonus_rate_40}}

  - id: asset.h_bonus_2025
    printed: "(helper)"
    label: "Special depreciation allowance for this property placed in service in 2025 (depreciable basis times the applicable percentage)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "none"}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "forty"}]}
          then: asset.h_bonus40
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: true}]}
          then: asset.h_bonus_base
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_is2025, {const: true}]}
              - {op: test, eq: [asset.bonus_choice, {const: "full"}]}
              - {op: test, eq: [asset.after_jan19, {const: false}]}
          then: asset.h_bonus40
    refuses: [asset.h_bonus_mixed, asset.h_outside]
    note: "Property acquired after September 27, 2017 and before January 20, 2025 is limited to 40% whether the answer is 'full' or 'forty'; property acquired after January 19, 2025 gets 100% unless the 40% election was made."

  - id: asset.s179_2025
    printed: "(helper)"
    label: "Elected section 179 cost of this property placed in service in 2025 (line 6(c) or line 26(i))"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses:
      - asset.screen
      - {when: asset.h_s179_over, when_known: true}
      - {when: asset.h_s179_inelig, when_known: true}

  - id: asset.bonus
    printed: "14"
    label: "Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_on19, {const: true}]}
          then: asset.h_bonus_2025
        - guard: {op: test, eq: [asset.h_on19, {const: false}]}
          then: asset.h_zero
    shown_when: asset.h_on19

  - id: asset.f26i
    printed: "26(i)"
    label: "Elected section 179 cost (listed property used more than 50% in a qualified business use)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_on26, {const: true}]}
          then: asset.s179
        - guard: {op: test, eq: [asset.h_on26, {const: false}]}
          then: asset.h_zero
    refuses:
      - {when: asset.h_s179_over, when_known: true}
      - {when: asset.h_s179_inelig, when_known: true}
    shown_when: asset.h_on26

  - id: asset.h_prior_base
    printed: "(helper)"
    label: "Business/investment portion of cost minus the section 179 deduction elected in the year placed in service"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_bus_cost, take: asset.prior_179}

  - id: asset.h_base_pre
    printed: "(helper)"
    label: "Business/investment portion of cost minus the section 179 expense deduction"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_base
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_prior_base

  - id: asset.h_bonus_taken
    printed: "(helper)"
    label: "Special depreciation allowance taken on the property (line 14, line 25, or in the year placed in service)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.prior_bonus
        - guard: {op: test, eq: [asset.h_on19, {const: true}]}
          then: asset.bonus
        - guard: {op: test, eq: [asset.h_on26, {const: true}]}
          then: asset.f25

  - id: asset.basis
    printed: "(c)"
    label: "Basis for depreciation (business/investment use only): cost or other basis multiplied by the percentage of business/investment use, minus the section 179 expense deduction and any special depreciation allowance"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: asset.h_base_pre, take: asset.h_bonus_taken}
    refuses: [asset.screen, asset.h_outside]
    note: "Unadjusted basis to which the percentage-table rates apply each year; for property placed in service before 2025 it uses the section 179 amount and special allowance of the year placed in service."

  - id: asset.col19c
    printed: "19(c)"
    label: "Basis for depreciation (business/investment use only), lines 19a through 19h"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_on19, {const: true}]}
          then: asset.basis
        - guard: {op: test, eq: [asset.h_on19, {const: false}]}
          then: asset.h_zero
    shown_when: asset.h_on19

  - id: asset.h_hy
    printed: "(helper)"
    label: "Half-year convention"
    type: Enum(macrs_convention)
    expr: {op: param, ref: sc.conv_hy}

  - id: asset.h_year1
    printed: "(helper)"
    label: "First year of recovery"
    type: Count
    expr: {op: param, ref: sc.year1}

  - id: asset.h_qconv
    printed: "(helper)"
    label: "Mid-quarter convention for the quarter placed in service"
    type: Enum(macrs_convention)
    expr: {op: keyed_lookup, table: quarter_convention, keys: [asset.quarter]}

  - id: asset.h_rate_hy
    printed: "(helper)"
    label: "Table A-1 rate, half-year convention, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_hy, asset.h_year1]}

  - id: asset.h_rate_mq
    printed: "(helper)"
    label: "Tables A-2 to A-5 rate, mid-quarter convention for the quarter placed in service, year 1"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.h_qconv, asset.h_year1]}

  - id: asset.h_dep_hy
    printed: "(helper)"
    label: "Column (c) times the half-year rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_hy}

  - id: asset.h_dep_mq
    printed: "(helper)"
    label: "Column (c) times the mid-quarter rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.col19c, rate: asset.h_rate_mq}

  - id: asset.macrs2025
    printed: "19(g)"
    label: "Depreciation deduction: multiply column (c) by the applicable rate from the appropriate table"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_on19, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_on19, {const: true}]}
              - {op: test, eq: [mq.applies, {const: true}]}
          then: asset.h_dep_mq
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_on19, {const: true}]}
              - {op: test, eq: [mq.applies, {const: false}]}
          then: asset.h_dep_hy
    refuses: [asset.h_outside]
    shown_when: asset.h_on19

  - id: asset.h_ry
    printed: "(helper)"
    label: "Year of recovery in 2025"
    type: Count
    expr: {op: keyed_lookup, table: recovery_year, keys: [asset.placed]}

  - id: asset.h_last
    printed: "(helper)"
    label: "Last year of recovery for the recovery period"
    type: Count
    expr: {op: keyed_lookup, table: macrs_last_year, keys: [asset.period]}

  - id: asset.h_done
    printed: "(helper)"
    label: "Recovery period ended before 2025"
    type: Bool
    expr: {op: test, gt: [asset.h_ry, asset.h_last]}

  - id: asset.h_rate_prior
    printed: "(helper)"
    label: "Percentage-table rate for the 2025 year of recovery, with the convention used in the year placed in service"
    type: Rate
    expr: {op: keyed_lookup, table: macrs_gds, keys: [asset.period, asset.prior_conv, asset.h_ry]}

  - id: asset.h_dep_prior
    printed: "(helper)"
    label: "Basis for depreciation times the 2025 table rate"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: asset.basis, rate: asset.h_rate_prior}

  - id: asset.macrs_prior
    printed: "17"
    label: "MACRS deductions for assets placed in service in tax years beginning before 2025"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_on17, {const: false}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_on17, {const: true}]}
              - {op: test, eq: [asset.h_done, {const: true}]}
          then: asset.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [asset.h_on17, {const: true}]}
              - {op: test, eq: [asset.h_done, {const: false}]}
          then: asset.h_dep_prior
    refuses: [asset.h_outside]
    shown_when: asset.h_on17

  - id: asset.h_q4
    printed: "(helper)"
    label: "Placed in service in 2025 during the last 3 months of the tax year"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.quarter, {const: "q4"}]}

  - id: asset.mq_total
    printed: "(helper)"
    label: "Depreciable basis (reduced by section 179 and personal use, not by any special allowance) of MACRS property placed in service during the year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_is2025, {const: true}]}
          then: asset.h_bonus_base
        - guard: {op: test, eq: [asset.h_is2025, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]

  - id: asset.mq_q4
    printed: "(helper)"
    label: "Depreciable basis (reduced by section 179 and personal use, not by any special allowance) of MACRS property placed in service during the last 3 months of the tax year"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_q4, {const: true}]}
          then: asset.h_bonus_base
        - guard: {op: test, eq: [asset.h_q4, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]

  - id: asset.h_eligible179
    printed: "(helper)"
    label: "Section 179 property placed in service in 2025 and used more than 50% in the business"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [asset.h_is2025, {const: true}]}
        - {op: test, eq: [asset.not179, {const: false}]}
        - {op: test, gt: [asset.pct, {const: 50, type: Count}]}

  - id: asset.cost179
    printed: "(helper)"
    label: "Cost of section 179 property placed in service during the tax year (Form 4562 line 2; total eligible cost, not just the elected amount)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [asset.h_eligible179, {const: true}]}
          then: asset.h_bus_cost
        - guard: {op: test, eq: [asset.h_eligible179, {const: false}]}
          then: asset.h_zero
    refuses: [asset.screen]
    note: "Open: line 2 says 'total cost' and column 6(b) says 'cost (business use only)'; chose the business-use cost. Property used 50% or less in the business is left out, reading 'eligible section 179 property' (Worksheet 1 footnote) with Part I's 'used predominantly (more than 50%)'."
```
```
<!-- part section asset.s179_2025 -->
asset.s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**
Reviewed in: pass 1a6cc33f5c1b

<!-- part section asset.mq_q4 -->
asset.mq_q4 — Mid-quarter test basis, fourth quarter
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "q1"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q2"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "q3"}, {"input": "asset.quarter"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"const": "q4"}, {"input": "asset.quarter"}], "test": "ne"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section asset.mq_total -->
asset.mq_total — Mid-quarter test basis, all of 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section asset.cost179 -->
asset.cost179 — Cost of section 179 property placed in service in 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, {"param": "sc.fifty_cents"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sc.fifty_cents"}, {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}], "test": "lt"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": 0}, {"line": "6(c)"}], "test": "lt"}, {"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "cqip"}, {"line": "(a)"}], "test": "eq"}, {"args": [{"line": "6(c)"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "eq"}, {"args": [{"const": 50, "type": "Count"}, {"input": "asset.pct"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}}, {"guard": {"args": [{"args": [{"input": "asset.pct"}, {"const": 50, "type": "Count"}], "test": "le"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.not179"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: line 2 says 'total cost' and column 6(b) says 'cost (business use only)'; chose the business-use cost. Property used 50% or less in the business is left out, reading 'eligible section 179 property' (Worksheet 1 footnote) with Part I's 'used predominantly (more than 50%)'.

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section (d) -->
(d) — Recovery period under GDS for the asset class
Status: **AGREE**
Reviewed in: pass 1a6cc33f5c1b

<!-- part section (c) -->
(c) — Basis for depreciation (business/investment use only), before section 179 and the special
Status: **DISAGREE**

Project:

```json
{"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 6, "whole": {"param": "sc.hundred_cents"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "14"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "25"}}, {"guard": {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, "then": {"input": "asset.prior_bonus"}}], "op": "choose"}}
```

Second transcription's note: Unadjusted basis to which the percentage-table rates apply each year; for property placed in service before 2025 it uses the section 179 amount and special allowance of the year placed in service.

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section 14 -->
14 — Special depreciation allowance for this property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"amount": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}, "then": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}, "then": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "forty"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "full"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.after_jan19"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"amount": {"from": {"amount": {"input": "asset.cost"}, "op": "prorate", "part": {"amount": {"const": 1}, "count": {"input": "asset.pct"}, "op": "multiply_count"}, "places": 2, "whole": {"param": "sc.hundred_cents"}}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "multiply_rate", "rate": {"param": "sc.bonus_rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "none"}, {"input": "asset.bonus_choice"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section 26(i) -->
26(i) — Elected section 179 cost of this listed property (column (i))
Status: **DISAGREE**

Project:

```json
{"line": "6(c)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "6(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": true}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section 19(c) -->
19(c) — Basis for depreciation (business/investment use only), column (c), after the section 179 d
Status: **DISAGREE**

Project:

```json
{"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, "then": {"line": "(c)"}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section 19(g) -->
19(g) — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"line": "6(c)"}}, "op": "subtract_floor0", "take": {"line": "14"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"param": "sc.conv_hy"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}], "test": "all"}, {"args": [{"amount": {"collection": "person", "field": "person.mq_total", "op": "sum_over", "where": null}, "count": {"param": "sc.count2"}, "op": "multiply_count"}, {"amount": {"collection": "person", "field": "person.mq_q4", "op": "sum_over", "where": null}, "count": {"param": "sc.count5"}, "op": "multiply_count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "19(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"keys": [{"input": "asset.quarter"}], "op": "keyed_lookup", "table": "quarter_convention"}, {"const": 1, "type": "Count"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part section 17 -->
17 — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}, "then": {"amount": {"from": {"from": {"line": "(c)"}, "op": "subtract_floor0", "take": {"input": "asset.prior_179"}}, "op": "subtract_floor0", "take": {"input": "asset.prior_bonus"}}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}, {"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(c)"}, "op": "multiply_rate", "rate": {"keys": [{"line": "(d)"}, {"line": "(e)"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "op": "keyed_lookup", "table": "macrs_gds"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "asset.listed"}], "test": "eq"}, {"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "ne"}], "test": "all"}, {"args": [{"keys": [{"line": "(d)"}], "op": "keyed_lookup", "table": "macrs_last_year"}, {"keys": [{"line": "(b)"}], "op": "keyed_lookup", "table": "recovery_year"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": "y2025"}, {"line": "(b)"}], "test": "eq"}, {"args": [{"const": false}, {"input": "asset.listed"}], "test": "ne"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: open
Reviewed in: pass 1a6cc33f5c1b

<!-- part gate asset.s179_2025 -->
| asset.s179_2025 | asset.h_s179_inelig, asset.h_s179_over, asset.screen | asset.h_s179_inelig, asset.h_s179_over, asset.screen |
<!-- part gate asset.mq_q4 -->
| asset.mq_q4 | asset.screen | asset.screen |
<!-- part gate asset.mq_total -->
| asset.mq_total | asset.screen | asset.screen |
<!-- part gate asset.cost179 -->
| asset.cost179 | asset.screen | asset.screen |
<!-- part gate (d) -->
| (d) | asset.screen | asset.screen |
<!-- part gate (c) -->
| (c) | asset.h_bonus_mixed, asset.h_outside, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.screen |
<!-- part gate 14 -->
| 14 | asset.h_bonus_mixed, asset.h_outside, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.screen |
<!-- part gate 26(i) -->
| 26(i) | asset.h_s179_inelig, asset.h_s179_over | asset.h_s179_inelig, asset.h_s179_over |
<!-- part gate 19(c) -->
| 19(c) | asset.h_bonus_mixed, asset.h_outside, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.screen |
<!-- part gate 19(g) -->
| 19(g) | asset.h_bonus_mixed, asset.h_outside, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.screen |
<!-- part gate 17 -->
| 17 | asset.h_bonus_mixed, asset.h_outside, asset.screen | asset.h_bonus_mixed, asset.h_outside, asset.screen |
<!-- end -->
