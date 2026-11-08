# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d2c505cbc097fbee4ffcf21b5afec5ff0babcc0050a4d00257e10075cc7824c9 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a4ce3487d66ecb85d66e609fa07731ce64dbd9dd38ddc8074e69f61161ceeadc |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ffe5a4e74bb1183dfab3be1ef94ed1938c33867886cfb8518e6775439cb6f86b |
| printed lines compared | 5 |
| agree / disagree / missing | 3 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### sb.ordinary_dividends_if_dividends — Total ordinary dividends, Form 1099-DIV box 1a, when you or your spouse received dividends
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"line": "6"}}], "op": "choose"}
```

Second transcription's note: The Schedule B pages do not define this interface. My reading is that it is the line 6 amount carried to Form 1040 line 3b when the filer received dividends (div.any is yes), and zero when the filer received none. This reading is chosen from the interface name and the dividend gate. The IRS text does not state it.

Ruling: representation; the candidate takes line 6 when div.any is yes and zero when it is no; the project takes box 1a (sb.ordinary_dividends) when div.any is yes and zero otherwise, and line 6 is a copy of this gate line with the Schedule B refusals, so the two agree on every return where line 6 is not refused (a refused line 6 refuses the return either way). Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass a084cfa2e80b

### 2 — Total taxable interest from all payers
Status: **AGREE**
Reviewed in: pass a084cfa2e80b

### 3 — Amount from sb.zero
Status: **AGREE**
Reviewed in: pass a084cfa2e80b

### 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

### 6 — Amount from sb.ordinary_dividends_if_dividends
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}
```

Second:

```json
{"input": "sb.ordinary_dividends"}
```

Second transcription's note: Line 5 reports all ordinary dividends (Form 1099-DIV box 1a), supplied here as the total input sb.ordinary_dividends. The IRS text also allows a nominee distribution to be subtracted before line 6. That case is covered by sb.unsupported, which refuses this line, so line 6 is the box 1a total.

Ruling: model error; the candidate reads sb.ordinary_dividends whatever the filer received dividends or other distributions (div.any), so it needs that answer where the source does not: i1040sb p. 2, Line 5, "Report on line 5 all of your ordinary dividends. This amount should be shown in box 1a of your Forms 1099-DIV or substitute statements": a filer who received no dividends has none to report. The project reads the gate line sb.ordinary_dividends_if_dividends, which takes sb.ordinary_dividends when the filer received dividends or other distributions (div.any) holds and zero otherwise; the interview asks sb.ordinary_dividends only then (gated_by sb.ordinary_dividends_if_dividends), so on every return the interview can produce with the condition true the two sides agree. Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass a084cfa2e80b

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sb.ordinary_dividends_if_dividends | sb.unsupported | sb.unsupported |
| 2 | sb.unsupported | sb.unsupported |
| 3 | sb.unsupported | sb.unsupported |
| 4 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |
| 6 | sb.unsupported | sb.unsupported |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sb.ordinary_dividends_if_dividends | b1d271d8d849b7c1efeca53defa98c7bd54ccc1decc43a9cac93006238a8ca45 |
| 2 | c2b650684ceb34df8615b05b853364172e30d7ba59937c04127f531c8ed61b4a |
| 3 | 1c76ab65b96979369ebb8017a12a4cece2ea2d7eb8d0c715b871937b0071643c |
| 4 | d225f28e9701cf230747bff686459225d04bd398ce08e2040a616fb8958167c4 |
| 6 | e809b51c44b136b040bc80da353c594902708b11e4cef581dd48ab7d213290ce |
| (rest of the document) | 013e58d3d274e971cd170d48794200b98ac690d600b9af1e38e8133de7ae11db |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sb.ordinary_dividends_if_dividends | 6c48c72035307b8bd1ab9c5771777c8b178c3509cec1b4d6aa030c43e1a415f8 |
| 2 | 31e4161f21912b241e1de23fe5f89c504cead2e99f9ac4d8aced189ce6e5cdde |
| 3 | 31e4161f21912b241e1de23fe5f89c504cead2e99f9ac4d8aced189ce6e5cdde |
| 6 | 31e4161f21912b241e1de23fe5f89c504cead2e99f9ac4d8aced189ce6e5cdde |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass a084cfa2e80b

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines sb.ordinary_dividends_if_dividends, 2, 3, 6 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a084cfa2e80b54386baa88ef06ee390bfcb11e6a28d1806fb0d99383a0366955 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | 8c2be2ec8cbc01853c2407aa476ad10dd4684c52b030829046136ec3ff6b6202 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 8f9e0ed1b7f2beda5be7efde5187ff04fcb02b8f33b7befc06ccf07bb52044a8 |
| receipt | .transcription/sb.lines-1c313dd37d49 |
| printed lines compared | 4 |
| agree / disagree / missing | 2 / 2 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: div.any, div.basis_reconciled, div.box10, div.box12, div.box13, div.box2b, div.box2c, div.box2d, div.box2e, div.box2f, div.box3, div.box9 | div |
| named form, inputs and named lines: f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line2a, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: qbi.carryforward, qbi.dividends, qbi.unsupported | qbi |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named form, inputs and named lines: sd.carryover, sd.distributions, sd.other_forms | sd |
| shared page | interest |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Add the amounts on line 1"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    refuses: [sb.unsupported]
    note: "Line 1 lists each payer's taxable interest, and line 2 adds those amounts. The IRS text also lets the filer enter a subtotal and subtract amounts for a nominee distribution, accrued interest, an OID adjustment or an ABP adjustment before line 2. Those adjustments are covered by the screening input sb.unsupported, which refuses this line. Line 2 is therefore the total of the payer amounts."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
    refuses: [sb.unsupported]
    note: "The exclusion is figured on Form 8815, which this tool does not compute. A savings bond interest exclusion is a case covered by sb.unsupported, so the line refuses when it applies. Otherwise no exclusion is claimed and the line is zero. The zero comes from the only zero-valued money parameter in the catalog (ss.zero)."
  - id: sb.line6
    printed: "6"
    label: "Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    refuses: [sb.unsupported]
    note: "Line 5 reports all ordinary dividends (Form 1099-DIV box 1a), supplied here as the total input sb.ordinary_dividends. The IRS text also allows a nominee distribution to be subtracted before line 6. That case is covered by sb.unsupported, which refuses this line, so line 6 is the box 1a total."
  - id: sb.h_zero
    printed: "(helper)"
    label: "Zero (no dividends)"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
  - id: sb.ordinary_dividends_if_dividends
    printed: "(helper)"
    label: "Ordinary dividends (Schedule B line 6) when any dividends were received; otherwise zero"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.any, {const: true}]}
          then: sb.line6
        - guard: {op: test, eq: [div.any, {const: false}]}
          then: sb.h_zero
    note: "The Schedule B pages do not define this interface. My reading is that it is the line 6 amount carried to Form 1040 line 3b when the filer received dividends (div.any is yes), and zero when the filer received none. This reading is chosen from the interface name and the dividend gate. The IRS text does not state it."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Total of all taxable interest listed on line 1 (subtotal of line 1, less any amount subtracted under the Nominee, Accrued Interest, OID Adjustment or ABP Adjustment rules)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    refuses: [sb.unsupported, sb.fbar_required, sb.form8938, sb.line8]
    note: "Subtractions from the line 1 subtotal (nominee, accrued interest, OID adjustment, ABP adjustment) and the other special cases are outside the tool and refused by sb.unsupported, so line 2 is the plain total of the payer amounts. The supplied text does not say where to enforce the Part III screens (FBAR, Form 8938, foreign trust), and Part III has no requested money line. I chose to list them on lines 2 and 6, the two Schedule B lines fed directly by inputs. sb.line7a is not used in a refusal because the instructions make a Yes to Question 1 reportable even if FinCEN Form 114 is not required."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989 (Form 8815)"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
    refuses: [sb.unsupported]
    note: "The savings bond interest exclusion (Form 8815) is refused by sb.unsupported, so the only case the tool computes has no exclusion and the line is zero. The catalog has no zero parameter specific to Schedule B, so I used the zero-valued money parameter ss.zero."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2"
    type: Dollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
    note: "The supplied instructions have no entry for line 4 and do not include the face of the form. I read it as line 2 minus line 3, because line 3 is described as an exclusion from the interest totalled on line 2. The label is my wording, not quoted IRS text."
  - id: sb.line6
    printed: "6"
    label: "Total of all ordinary dividends listed on line 5 (subtotal of line 5, less any nominee distribution)"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    refuses: [sb.unsupported, sb.fbar_required, sb.form8938, sb.line8]
    note: "Line 5 reports the ordinary dividends shown in box 1a of Forms 1099-DIV. The interface supplies that total as sb.ordinary_dividends, and the nominee subtraction is refused by sb.unsupported, so line 6 equals that total. The Part III screens are repeated here so that a return with dividends but no interest entries still stops on them."
```
```
