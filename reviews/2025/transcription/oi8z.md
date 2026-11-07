# Transcription agreement — oi8z

Second transcription of `Schedule 1, line 8z — other income, one entry per item listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/oi8z.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2f958a72b7b2cb4bc24fc82202aba6652f5f70c9d6f61a5ec738313bf16b1a6c |
| subject sha256 | 0a3972a97621761568f216084d2c414b170914aa8b5e5d68ee32d22416a36b94 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### oi8z.taxable — The amount of this item included on line 8z
Status: **DISAGREE**

Project:

```json
{"line": "8z (amount)"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "corrective_distribution"}, {"line": "8z (type)"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "corrective_distribution"}, {"line": "8z (type)"}], "test": "ne"}, "then": {"line": "8z (amount)"}}], "op": "choose"}
```

Second transcription's note: Open point: what the interface oi8z.taxable means. The IRS text says to list the type and amount of each taxable income item on line 8z. The input oi8z.amount is already the amount to include in income, so the taxable amount of a positive item is that amount. Pub. 525 governs how to figure a recovery or the taxable part of disaster relief, and the filer applies those rules before entering the amount. One kind, "loss on certain corrective distributions of excess deferrals", is a loss. A loss reduces line 8z rather than adding to it. A NonNegDollars result cannot carry a negative amount, so I read oi8z.taxable as the item's positive taxable income and set it to zero for that kind. Schedule 1 line 8z must therefore subtract the corrective-distribution losses separately, by summing oi8z.amount where oi8z.kind is corrective_distribution. If the interface was meant to be the signed contribution to line 8z, it would need the type Dollars and a subtraction from zero, which the declared type does not allow.

Ruling: scope; i1040gi p. 92, Line 8z, "List the type and amount of each item of other income". The reply zeroes the corrective-distribution kind, reading it as a loss; the project copies the item's amount and computes only RTAA payments and kickbacks: every other kind, the corrective distribution included, is refused at oi8z.figured ("a corrective distribution, disaster relief payments, insurance dividends, or any other kind") or oi8z.additional_tax. Triage executable-triage-v2 (reviews/2025/transcription/triage/oi8z.json; 1,638 fixtures, 500 generated returns seed 20261026, 44 partial records): 109 of 180 comparisons agree; 49 project-refuses and 22 project-unknown, all on refused or incomplete returns; no completed return differs. The R3 restructuring of the oi8z.kind question kept each kind's words (word check: none lost). Project stands.
Reviewed in: pass dd6b6292bb45

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| oi8z.taxable | a5d72d82366bd7b6155acbee656cdf1ae81a8a937da73a21b23e20401fb8c511 |
| (rest of the document) | 9b11cc29785845924b626fad6f7f0a62bdf1f9b626cc1aab9a2c543ecad4736e |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| oi8z.taxable | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass dd6b6292bb45

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines oi8z.taxable |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | dd6b6292bb456de6c0792669d7988fcb5889ac7699af1bd05bce0122d553c45b |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | b56a61b58788cb5c3e5b03d0c5fcf2de86754947436cbadb4b8b19e2797021d3 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 932eff95e003b50204b0725d8dd3c385c260666e430efd80051d13569518f6eb |
| receipt | .transcription/oi8z.lines-191e65963821 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: f1040.line1a, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: refund.box8, refund.exc_tax, refund.exc_who, refund.itemized, refund.line17_2024, refund.line5d_2024, refund.line5e_2024, refund.mfs_spouse_itemized, refund.not_2024, refund.received, refund.sales, refund.spouse_blind, refund.spouse_born, refund.status, refund.you_blind, refund.you_born | refund |
| named form, inputs and named lines: s2.amt, s2.other | s2 |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named form, inputs and named lines: sd.carryover, sd.distributions, sd.other_forms | sd |
| named line | eic, s8812 |
| named lines: sc.f7206_line13, sc.line13 | sc |
| shared page | person, s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: oi8z.h_is_loss
    printed: "(helper)"
    label: "Is this item a loss on certain corrective distributions of excess deferrals?"
    type: Bool
    expr:
      op: test
      eq: ["oi8z.kind", {const: "corrective_distribution"}]
  - id: oi8z.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: oi8z.taxable
    printed: "(helper)"
    label: "Use line 8z to report any taxable income not reported elsewhere on your return or other schedules. List the type and amount of income."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["oi8z.h_is_loss", {const: false}]}
          then: "oi8z.amount"
        - guard: {op: test, eq: ["oi8z.h_is_loss", {const: true}]}
          then: "oi8z.h_zero"
    note: >-
      Open point: what the interface oi8z.taxable means. The IRS text says to list the type and
      amount of each taxable income item on line 8z. The input oi8z.amount is already the amount
      to include in income, so the taxable amount of a positive item is that amount. Pub. 525
      governs how to figure a recovery or the taxable part of disaster relief, and the filer
      applies those rules before entering the amount.
      One kind, "loss on certain corrective distributions of excess deferrals", is a loss. A loss
      reduces line 8z rather than adding to it. A NonNegDollars result cannot carry a negative
      amount, so I read oi8z.taxable as the item's positive taxable income and set it to zero
      for that kind.
      Schedule 1 line 8z must therefore subtract the corrective-distribution losses separately,
      by summing oi8z.amount where oi8z.kind is corrective_distribution. If the interface was
      meant to be the signed contribution to line 8z, it would need the type Dollars and a
      subtraction from zero, which the declared type does not allow.
```
```

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
