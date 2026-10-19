# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 17c5c01937ae2c35484eb37c6de922aa24db32bf0ac9251aab782a61a0fed045 |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
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
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.h_refused | otjob.h_refused |

## Raw second transcription

```yaml
```yaml
lines:
  - id: otjob.one
    printed: "(helper)"
    label: "One employer entry (one row, lines 1A through 1E, of the Qualified Overtime Compensation From More Than One Employer Worksheet)"
    type: Count
    expr: {op: param, ref: sales.one}
    note: "No worksheet-specific parameter for the constant 1 is listed; the year parameter sales.one (value 1) is used, as other collections use sales.zero."

  - id: otjob.h_zero
    printed: "(helper)"
    label: "No qualified overtime from this employer"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: otjob.h_refused
    printed: "(helper)"
    label: "Overtime from an FLSA-eligible job that must be figured under a section 7 rule other than section 7(a), or by a reasonable method other than paragraphs 1 through 4 or an employer-provided amount"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [otjob.flsa, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [otjob.special_rule, {const: true}]}
            - {op: test, eq: [otjob.method, {const: "other"}]}
    note: "The instructions say an employer covered by a different section 7 overtime rule requires computing overtime under that rule, using any method that 'produces a reasonable result'. Paragraph 5 also allows any 'reasonable method'. The tool cannot check either case, so both are refused rather than computed."

  - id: otjob.h_by_third
    printed: "(helper)"
    label: "Paragraph 2. Divide the total of all wages for the overtime hours (FLSA Overtime Premium plus regular wages) by three (3)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}
    note: "The text gives no rounding rule for dividing by 3. The multiply_rate atom rounds half-up to the cent, and that is used here."

  - id: otjob.h_by_half
    printed: "(helper)"
    label: "Paragraph 3. Multiply the portion of overtime earnings more than your regular wage rate by the appropriate fraction (one-half when overtime is paid at double the regular rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
    note: "The instructions say only 'the appropriate fraction'. Notice 2025-69 (C) gives one-half for double time. Only the double-time case is computed. Other rates fall under method 'other', which is refused."

  - id: otjob.h_by_quarter
    printed: "(helper)"
    label: "Paragraph 4. Multiply the total of all pay for the overtime hours by the appropriate fraction (one-fourth when overtime is paid at double the regular rate)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
    note: "Notice 2025-69 (D) gives one-fourth for double time. Only double time is computed. Other rates are refused through method 'other'."

  - id: otjob.h_figured
    printed: "(helper)"
    label: "Qualified overtime compensation from this employer by the method chosen"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.method, {const: "employer_reported"}]}
          then: otjob.statement
        - guard: {op: test, eq: [otjob.method, {const: "premium"}]}
          then: otjob.statement
        - guard: {op: test, eq: [otjob.method, {const: "total_time_and_half"}]}
          then: otjob.h_by_third
        - guard: {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_by_half
        - guard: {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_by_quarter
        - guard: {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.h_zero
    note: "An amount the employer reports in box 14, or gives on request, may be relied on (employer_reported). Paragraph 1 uses the separately shown FLSA Overtime Premium as is. The 'other' branch exists only so the guards are exhaustive. For an FLSA-eligible employee it is never reached as a computed value, because line 1(b) refuses it."

  - id: otjob.line1(b)
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.flsa, {const: true}]}
          then: otjob.h_figured
        - guard: {op: test, eq: [otjob.flsa, {const: false}]}
          then: otjob.h_zero
    refuses: [otjob.h_refused]
    note: "The text says qualified overtime must be paid to a covered, nonexempt (FLSA-eligible) employee. It also says overtime paid to FLSA-ineligible employees is not qualified overtime compensation. So the entry is zero when the employee is not FLSA-eligible, including when the employer reported an amount in box 14. The instructions say the employer amount 'can generally' be relied on, and that point is left open; this transcription reads the eligibility rule as controlling. The statement amount is taken as covering the entire year (Notice 2025-69 (A) to (D))."
```
```
