# Transcription agreement — div

Second transcription of `Form 1099-DIV — distribution components and scope screening` by an isolated model (spec 6.5), compared line by line with `forms/2025/div.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4bd9b6b65b1a70f6d88bba25152777efc8b49b7cc665c961da2cf3016f850865 |
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
| subject sha256 | 42b78e5376ee4a1dfb47c58ddb1d582b614f006924582ead17ed6327920c53fa |
| printed lines compared | 5 |
| agree / disagree / missing | 4 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### div.has_ordinary — Ordinary dividends (box 1a) are above zero
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "div.any"}], "test": "eq"}, {"args": [{"const": 0}, {"ref": "sb.ordinary_dividends"}], "test": "lt"}], "test": "all"}
```

Second transcription's note: The IRS text does not define this interface. I read it as: the filer received dividends (the div.any gate) and box 1a total ordinary dividends (sb.ordinary_dividends) is more than zero. It is left open whether the interface is meant to include the div.any gate. I included it so that a filer with no dividends reads false.

Ruling: representation; the candidate's all[div.any = true, box 1a > 0] is the project's test written out: the project's operand sb.ordinary_dividends_if_dividends is box 1a when div.any is yes and zero when it is no, so both are true exactly when dividends were received and box 1a is above zero. Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass a9b21525bc5e

### div.zero — No amount in a box whose condition does not hold
Status: **AGREE**
Reviewed in: pass a9b21525bc5e

### div.box2b_if_capital_gain — Unrecaptured section 1250 gain, box 2b, when capital gain distributions (box 2a) are above
Status: **AGREE**
Reviewed in: pass a9b21525bc5e

### div.box2d_if_capital_gain — Collectibles (28%) gain, box 2d, when capital gain distributions (box 2a) are above zero;
Status: **AGREE**
Reviewed in: pass a9b21525bc5e

### div.box12_if_dividends — Exempt-interest dividends, box 12, when you or your spouse received dividends or other dis
Status: **AGREE**
Reviewed in: pass a9b21525bc5e

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| div.box2b_if_capital_gain | div.h_box2b_over_2a | div.h_box2b_over_2a |
| div.box2d_if_capital_gain | div.h_box2d_over_2a | div.h_box2d_over_2a |
| div.box12_if_dividends | div.h_box13_over_12 | div.h_box13_over_12 |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| div.has_ordinary | 51c58c1de7464bc47824ab0732e2e7831ea30d020938580b7f2bd8eee2826ad4 |
| div.zero | 023fca92bb2ca85c42b5ddf6296460a606a9efbc6b93efb54dd6aa7da46b1887 |
| div.box2b_if_capital_gain | d037b9cb7d43cab62280380d52b31c7076837f085745fbc7d567bb1bdb2e2821 |
| div.box2d_if_capital_gain | f0f73fe697c3e65e8a82d138affaeb3b54cd208ee43548636fb0794a7dab5dbf |
| div.box12_if_dividends | a5dfd6825e6b28b269a3a9ee79dcdb95d6803af033b1f5b53856a0d8879cb82a |
| (rest of the document) | ab9ea5065d1d3f1a23ab77de1d140198c1b1c4bc6363087c360e4f5384b11029 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| div.has_ordinary | 79fe0ced00bb0018af4444279cf97e3103af48b98b71dbe246eb7345eb7a1d4b |
| div.zero | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| div.box2b_if_capital_gain | e66df5ffb01429da4dbe373a716a5b03ac1f814676c023182c27b8da224a0c25 |
| div.box2d_if_capital_gain | e66df5ffb01429da4dbe373a716a5b03ac1f814676c023182c27b8da224a0c25 |
| div.box12_if_dividends | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass a9b21525bc5e

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines div.has_ordinary, div.zero, div.box2b_if_capital_gain, div.box2d_if_capital_gain, div.box12_if_dividends |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a9b21525bc5e044ebb3920c6183e2f62076cf7f6a0da9d241eb7c21f1b3e6563 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | e6b04fa8d903fc9aa1a86b168322cab913533e59d9e609aabd910172cd84a66b |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7ed65f2620ebaa5b60aa160345af7e5bb83bd1b2b2a2874e683e2066f5c5c63e |
| receipt | .transcription/div.lines-f5037c256590 |
| printed lines compared | 5 |
| agree / disagree / missing | 4 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: sb.fbar_required, sb.form5471, sb.form8938, sb.line7a, sb.line8, sb.ordinary_dividends, sb.unsupported | sb |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| shared page | qbi, sd |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: div.zero
    printed: "(helper)"
    label: "Zero (no amount from Form 1099-DIV for this purpose)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The IRS text has no line for this. It is a zero-valued money constant used as the 'no amount' alternative of the gated results below. It reads the zero-valued parameter sales.zero because the catalog has no div-specific zero parameter."

  - id: div.has_ordinary
    printed: "(helper)"
    label: "Box 1a. Shows total ordinary dividends that are taxable. Include this amount on the \"Ordinary dividends\" line of Form 1040 or 1040-SR."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [div.any, {const: true}]}
        - {op: test, gt: [sb.ordinary_dividends, {const: 0}]}
    note: "The IRS text does not define this interface. I read it as: the filer received dividends (the div.any gate) and box 1a total ordinary dividends (sb.ordinary_dividends) is more than zero. It is left open whether the interface is meant to include the div.any gate. I included it so that a filer with no dividends reads false."

  - id: div.h_box2b_over_2a
    printed: "(helper)"
    label: "Consistency: box 2b (a portion of the amount in box 2a) is more than box 2a"
    type: Bool
    expr: {op: test, gt: [div.box2b, sd.distributions_if_dividends]}

  - id: div.h_box2d_over_2a
    printed: "(helper)"
    label: "Consistency: box 2d (a portion of the amount in box 2a) is more than box 2a"
    type: Bool
    expr: {op: test, gt: [div.box2d, sd.distributions_if_dividends]}

  - id: div.h_box13_over_12
    printed: "(helper)"
    label: "Consistency: box 13 (included in box 12) is more than box 12"
    type: Bool
    expr: {op: test, gt: [div.box13, div.box12]}

  - id: div.box2b_if_capital_gain
    printed: "(helper)"
    label: "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain from certain depreciable real property. See the Unrecaptured Section 1250 Gain Worksheet in the Instructions for Schedule D (Form 1040)."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.distributions_if_dividends, {const: 0}]}
          then: div.box2b
        - guard: {op: test, le: [sd.distributions_if_dividends, {const: 0}]}
          then: div.zero
    refuses:
      - {when: div.h_box2b_over_2a, when_known: true}
    note: "Box 2b is a portion of box 2a. I read 'if capital gain' as: box 2b counts only when there are capital gain distributions (box 2a, through sd.distributions_if_dividends, which carries the dividends gate) more than zero. Otherwise the result is zero. A box 2b larger than box 2a contradicts 'portion of the amount in box 2a' and is refused as a consistency check."

  - id: div.box2d_if_capital_gain
    printed: "(helper)"
    label: "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles. If required, use this amount when completing the 28% Rate Gain Worksheet in the Instructions for Schedule D (Form 1040)."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.distributions_if_dividends, {const: 0}]}
          then: div.box2d
        - guard: {op: test, le: [sd.distributions_if_dividends, {const: 0}]}
          then: div.zero
    refuses:
      - {when: div.h_box2d_over_2a, when_known: true}
    note: "This uses the same reading as box 2b. Box 2d is a portion of box 2a and counts only when box 2a is more than zero. A box 2d larger than box 2a is refused as a consistency check."

  - id: div.box12_if_dividends
    printed: "(helper)"
    label: "Box 12. Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year. See the Instructions for Form 1040 for where to report."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.any, {const: true}]}
          then: div.box12
        - guard: {op: test, eq: [div.any, {const: false}]}
          then: div.zero
    refuses:
      - {when: div.h_box13_over_12, when_known: true}
    note: "I read 'if dividends' as the div.any gate: box 12 when the filer received dividends or distributions, and zero otherwise. Box 13 'is included in box 12', so a box 13 larger than box 12 is refused as a consistency check."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: div.h_zero
    printed: "(helper)"
    label: "Zero (no unsupported nondividend distribution)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: div.h_box3_unhandled
    printed: "(helper)"
    label: "Box 3. Shows a return of capital. To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain. See Pub. 550."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.basis_reconciled, {const: true}]}
          then: div.h_zero
        - guard: {op: test, eq: [div.basis_reconciled, {const: false}]}
          then: div.box3
    note: "Box 3 is not taxable up to basis; any excess is capital gain (Pub. 550). The tool handles box 3 only when the filer confirms the basis reductions have been made and no distribution is more than basis. Otherwise the box 3 amount counts in the screen."
  - id: div.screen
    printed: "(helper)"
    label: "Form 1099-DIV amounts outside the computed scope (boxes 2c, 2e, 2f, 9, 10, and box 3 not reconciled to basis)"
    type: NonNegDollars
    expr:
      op: sum
      of: [div.box2c, div.box2e, div.box2f, div.box9, div.box10, div.h_box3_unhandled]
    note: "The IRS pages do not define this result. I read it as the total of the 1099-DIV amounts the tool does not compute; any amount above zero should send the filer elsewhere. The amounts included are: box 2c (the section 1202 exclusion needs a Form 8949 'Q' entry, i1040sd p.8); boxes 2e and 2f (for foreign persons, effectively connected income); boxes 9 and 10 (liquidation distributions, for which no reporting is given); and box 3 not reconciled to basis. Left out: boxes 2b and 2d, because the Unrecaptured Section 1250 Gain and 28% Rate Gain Worksheets (u1250, g28) exist in the catalog; and boxes 12 and 13, because exempt-interest dividends go on line 2a and AMT is screened separately by s2.amt. Box 13 is part of box 12. These choices are open."
```
```
