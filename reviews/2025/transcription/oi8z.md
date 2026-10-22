# Transcription agreement — oi8z

Second transcription of `Schedule 1, line 8z — other income, one entry per item listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/oi8z.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2f958a72b7b2cb4bc24fc82202aba6652f5f70c9d6f61a5ec738313bf16b1a6c |
| subject sha256 | 0a3972a97621761568f216084d2c414b170914aa8b5e5d68ee32d22416a36b94 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### oi8z.taxable — The amount of this item included on line 8z
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| oi8z.taxable | oi8z.h_education_refused, oi8z.h_recapture_refused, oi8z.h_recovery_refused | oi8z.h_education_refused, oi8z.h_recapture_refused, oi8z.h_recovery_refused |

## Raw second transcription

```yaml
```yaml
lines:
  - id: oi8z.h_is_recovery
    printed: "(helper)"
    label: "Reimbursements or other amounts received for items deducted in an earlier year, such as medical expenses, real estate taxes, general sales taxes, or home mortgage interest"
    type: Bool
    expr: {op: test, eq: [oi8z.kind, {const: "recovery"}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, p. 92"
  - id: oi8z.h_recovery_refused
    printed: "(helper)"
    label: "A recovery item, when the filer has answered that they received another refund, reimbursement or recovery of an amount deducted in an earlier year (see Recoveries in Pub. 525 for how to figure the amount to report)"
    type: Bool
    expr:
      op: test
      all:
        - oi8z.h_is_recovery
        - {op: test, eq: [refund.other, {const: true}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, p. 92"
  - id: oi8z.h_is_recapture
    printed: "(helper)"
    label: "Recapture of a charitable contribution deduction (fractional interest in tangible personal property, or disposal by the organization within 3 years)"
    type: Bool
    expr: {op: test, eq: [oi8z.kind, {const: "charitable_recapture"}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, p. 92"
  - id: oi8z.h_recapture_refused
    printed: "(helper)"
    label: "Recapture of a charitable contribution deduction when an amount is also due on Schedule 2 (interest and an additional 10% tax apply to the amount of the recapture, Schedule 2, line 17g)"
    type: Bool
    expr:
      op: test
      all:
        - oi8z.h_is_recapture
        - {op: test, eq: [s2.other, {const: true}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, p. 92"
  - id: oi8z.h_is_education
    printed: "(helper)"
    label: "Taxable distributions from a Coverdell education savings account (ESA) or a qualified tuition program (QTP)"
    type: Bool
    expr: {op: test, eq: [oi8z.kind, {const: "education_distribution"}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, pp. 92-93"
  - id: oi8z.h_education_refused
    printed: "(helper)"
    label: "A taxable Coverdell ESA or QTP distribution when an additional tax applies (see the Instructions for Form 5329)"
    type: Bool
    expr:
      op: test
      all:
        - oi8z.h_is_education
        - {op: test, eq: [s2.other, {const: true}]}
    cite: "i1040gi 2025, Schedule 1, Line 8z, p. 93"
  - id: oi8z.taxable
    printed: "(helper)"
    label: "Other income. List type and amount of income (the amount of this item included on line 8z)"
    type: NonNegDollars
    expr: {op: copy, from: oi8z.amount}
    cite: "i1040gi 2025, Schedule 1, Line 8z, pp. 92-93; Pub. 525 (2025), Kickbacks, p. 34"
    refuses: [oi8z.h_recovery_refused, oi8z.h_recapture_refused, oi8z.h_education_refused]
    note: >-
      The text says to list the type and amount of each item and to report only taxable income.
      It says the taxable amount is figured elsewhere: Recoveries in Pub. 525, the taxable part of
      disaster relief per Pub. 525, and taxable Coverdell/QTP distributions per Pub. 970.
      Reading chosen: the filer enters the already-figured taxable amount (oi8z.amount), and it is
      carried over unchanged. Nontaxable income is not entered.
      "Loss on certain corrective distributions of excess deferrals" could be a negative amount.
      Because oi8z.amount and this line are NonNegDollars, a loss cannot be expressed here; that
      case is left to the existing input's type.
      Refusals are limited to the kinds whose instructions point to additional tax or interest
      (Schedule 2 line 17g, Form 5329) or to the separate recovery screen.
```
```
