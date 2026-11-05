# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d281c181cd4cae12c0c4e7892b05584c811c2200a5b0cc3fc1e4e7849ec8fd01 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | edf01867c3eb7f9d68ae0e8d453ccc8889f3e440839bcffcaa42e8a46215fe0a |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### otjob.one — One employer entry
Status: **AGREE**

### 1(b) — Qualified overtime reported on Form W-2, box 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "employer_reported"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "premium"}, {"input": "otjob.method"}], "test": "eq"}], "test": "any"}, "then": {"input": "otjob.statement"}}, {"guard": {"args": [{"const": "other"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "premium_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_half"}}}, {"guard": {"args": [{"const": "total_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_quarter"}}}, {"guard": {"args": [{"const": "total_time_and_half"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_third"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "employer_reported"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "premium"}, {"input": "otjob.method"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"input": "otjob.statement"}}, {"guard": {"args": [{"args": [{"const": "premium_double"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_half"}}}, {"guard": {"args": [{"args": [{"const": "total_double"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_quarter"}}}, {"guard": {"args": [{"args": [{"const": "total_time_and_half"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_third"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "other"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Qualified overtime must be paid to an FLSA-eligible employee, so the amount is zero when otjob.flsa is false. Paragraph 1 and an employer-reported amount are used as stated. Paragraph 2 divides by three. For paragraphs 3 and 4, the text says only 'the appropriate fraction'. The interface's enum is limited to double time, so I used the fractions the Notice gives for double time: one-half (paragraph C) and one-fourth (paragraph D). The method 'other' branch is there only so the alternatives cover every case. That case is refused through otjob.h_refused and never takes the zero. The instructions also tell you to include overtime not in box 1, such as amounts deferred under a qualified retirement plan. That is already part of the otjob.statement input.

Ruling: representation; same line and candidate as the refresh-round ruling. i1040gi pp. 106-108 (Schedule 1-A, Part III) and Notice 2025-69 section III.B.2 give the employer-reported or premium amount and the one-third, one-half and one-quarter conversions. Both give zero when otjob.flsa is false, the statement amount for employer_reported and premium, the three fractions for the double-time and time-and-a-half totals, and zero for method other (which otjob.h_refused refuses in both). The reply flattens the FLSA and method guards into one choice; no return differs. Project stands.
Reviewed in: pass df6496817fcc

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.h_refused | otjob.h_refused |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| otjob.one | e7838e18a06ea1557e24647d8e8d5758f1dfb5aa7312dbe9c799c9bf240c2849 |
| 1(b) | 2ebb919e0e5b2f7a2d30ef1013c4ef754f808c522d781c87dd475cda5265d0a6 |
| (rest of the document) | 5f0e2ac2178da2fba490ba4af97d9a79fe7483433bb4466a6d27d9210dcf2cad |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 1(b) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass df6496817fcc

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1(b) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | df6496817fccdadaad6c10c797a6d64b01c7e02824f3913b3284e5bf4d0725d9 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 17a49a3fa183e3c37e23a22194e33a15602f1a5e16b5418f97fc690586d3dfe5 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 31d3bfa8101118b5b4c6dd076709dabfd57c76c173cfd4997c84f2d663b51705 |
| receipt | .transcription/otjob.lines-57b9202763e7 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | sa |
| shared page | household, person, s1, s1a, sc |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: otjob.h_zero
    printed: "(helper)"
    label: "Zero (no qualified overtime compensation from this employer)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: otjob.h_third
    printed: "(helper)"
    label: "Total of all wages for the overtime hours (FLSA Overtime Premium plus regular wages) divided by three (3)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}
  - id: otjob.h_half
    printed: "(helper)"
    label: "Portion of the overtime earnings that is more than your regular wage rate for the overtime hours, multiplied by the appropriate fraction (one-half when overtime is paid at two times the regular rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
  - id: otjob.h_quarter
    printed: "(helper)"
    label: "Total of all pay for the overtime hours, multiplied by the appropriate fraction (one-fourth when overtime is paid at two times the regular rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
  - id: otjob.h_refused
    printed: "(helper)"
    label: "This employer's qualified overtime is figured by a method this tool does not compute (paragraph 5, a reasonable method, or an adjusted method), or the employer is covered by a different overtime rule in section 7 of the FLSA and the amount is not one the employer reported"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [otjob.flsa, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [otjob.method, {const: "other"}]}
            - op: test
              all:
                - {op: test, eq: [otjob.special_rule, {const: true}]}
                - {op: test, ne: [otjob.method, {const: "employer_reported"}]}
    note: "The instructions say an employee whose employer is covered by a different overtime rule in section 7 of the FLSA 'must compute your overtime compensation using the rule that applies to you and may use any of the following methods so long as it produces a reasonable result under the rule that applies to you'. The tool cannot judge whether a result is reasonable. I treated an amount the employer reported (W-2 box 14 or on request), which the instructions say you can rely on, as computable, and refused every other method for these employers. Paragraph 5 ('a reasonable method') and the adjustment the TIP allows to paragraphs 2 and 4 (method 'other') are also refused, because the closed input interface has no amount for them."
  - id: otjob.col_b
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.flsa, {const: false}]}
          then: otjob.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - op: test
                any:
                  - {op: test, eq: [otjob.method, {const: "employer_reported"}]}
                  - {op: test, eq: [otjob.method, {const: "premium"}]}
          then: otjob.statement
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_time_and_half"}]}
          then: otjob.h_third
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_half
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_quarter
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.h_zero
    refuses: [otjob.h_refused]
    note: "Qualified overtime must be paid to an FLSA-eligible employee, so the amount is zero when otjob.flsa is false. Paragraph 1 and an employer-reported amount are used as stated. Paragraph 2 divides by three. For paragraphs 3 and 4, the text says only 'the appropriate fraction'. The interface's enum is limited to double time, so I used the fractions the Notice gives for double time: one-half (paragraph C) and one-fourth (paragraph D). The method 'other' branch is there only so the alternatives cover every case. That case is refused through otjob.h_refused and never takes the zero. The instructions also tell you to include overtime not in box 1, such as amounts deferred under a qualified retirement plan. That is already part of the otjob.statement input."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: otjob.one
    printed: "(helper)"
    label: "One employer (counts this row of the Qualified Overtime Compensation From More Than One Employer Worksheet, lines 1A through 1E)"
    type: Count
    expr: {op: param, ref: person.one}
    note: "The IRS pages do not define this interface. Read as the count of one for this employer row, used to count the worksheet's employer rows (lines 1A to 1E). No otjob-specific count parameter is supplied, so the value 1 comes from the Count parameter person.one."
  - id: otjob.h_zero
    printed: "(helper)"
    label: "Zero (no qualified overtime compensation from this employer)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: otjob.h_refused
    printed: "(helper)"
    label: "The tool cannot figure this employer's qualified overtime: the employer is covered by an FLSA overtime rule other than section 7(a), or a method other than paragraphs 1 to 4 (or an employer-reported amount) is used"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [otjob.flsa, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [otjob.special_rule, {const: true}]}
            - {op: test, eq: [otjob.method, {const: "other"}]}
    note: "Under the instructions, an employer covered by a section 7 rule other than 7(a) requires computing overtime under that rule. The paragraph methods may be used only 'so long as it produces a reasonable result under the rule that applies to you' (Notice 2025-69 (G)). Paragraph 5 is a 'reasonable method' based on the regular rate and hours (Notice (F)), and so is the adjustment in the TIP and Notice (E). The tool cannot verify any of these, so it refuses them. This applies only for FLSA-eligible employees, because for anyone else the amount is not qualified overtime compensation at all."
  - id: otjob.h_third
    printed: "(helper)"
    label: "Total of all wages for the overtime hours divided by three (paragraph 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}
  - id: otjob.h_half
    printed: "(helper)"
    label: "Portion of overtime earnings above the regular wage rate, overtime paid at double time, multiplied by the appropriate fraction, one-half (paragraph 3)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
    note: "The instructions say 'the appropriate fraction' and Notice 2025-69 (C) gives one-half for double time. Example 2 is consistent: $10,000 of premium gives $5,000. The tool supports only double time; other rates fall under 'other' and are refused."
  - id: otjob.h_quarter
    printed: "(helper)"
    label: "Total of all pay for the overtime hours, overtime paid at double time, multiplied by the appropriate fraction, one-fourth (paragraph 4)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
    note: "Notice 2025-69 (D) gives one-fourth for double time. Example 3 is consistent: $20,000 of total pay gives $5,000."
  - id: otjob.col_b
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1 (including qualified overtime compensation not included in box 1 of Form W-2, for example overtime amounts deferred under a qualified retirement plan)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.flsa, {const: false}]}
          then: otjob.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - op: test
                any:
                  - {op: test, eq: [otjob.method, {const: "employer_reported"}]}
                  - {op: test, eq: [otjob.method, {const: "premium"}]}
          then: otjob.statement
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_time_and_half"}]}
          then: otjob.h_third
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_half
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_quarter
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.h_zero
    refuses: [otjob.h_refused]
    note: "Qualified overtime must be paid to an FLSA-eligible employee. Overtime paid to an FLSA-ineligible employee 'is not qualified overtime compensation', so that case is zero. An employer-reported amount (Form W-2 box 14, or an amount given on request) 'can generally rely on', and the paragraph 1 premium, are used as shown. The 'other' branch is zero only to keep the guards exhaustive; that case is always refused through otjob.h_refused and never used. The worksheet heading says 'reported on Form W-2, box 1', but the line 14a text adds overtime not included in box 1 (for example deferred overtime). The statement input includes that amount, so it is read as included."
```
```
