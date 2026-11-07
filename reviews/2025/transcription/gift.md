# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ab0dce2ada634630031cdde007b054ee4001c4f585d6d1ef74994bf07a8798bd |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 17f0390430f197eddd9b19e05e554095927961d367b72e478fc9b34a139f48e6 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 552efdd648d6ffb4d143f26826653ffd98575fe9d5c262afa5feee4a1c97f29d |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### gift.allowed — Amount from gift.deduction
Status: **AGREE**
Reviewed in: pass f5b4b175109a

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| gift.allowed | gift.h_over_5000_unflagged, gift.special | gift.h_over_5000_unflagged |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| gift.allowed | 9f6d6615d42b166da141ae78c5a205745c428e73b54142a7072ce3730fb0622f |
| (rest of the document) | ddbcf2f1a297aa931cad1239e9a5fd1dd8e5972b3c96439aab19e487bc291084 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| gift.allowed | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass f5b4b175109a

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines gift.allowed |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f5b4b175109a4188f5f92f4e8bcea323edab5f54e28f81653f8466237de6b6e2 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | f0d15280a9a5844f23555c255bf8ab9bdb995ba2f5efbf9f3e448eef0c6efd34 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 701abacdf2425bb06de743729df7d04bbbad2be98671821a098b1193c185f06e |
| receipt | .transcription/gift.lines-81339da9de9f |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: f1040.line11b, f1040.line12e, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: s1.alimony, s1.alimony_paid, s1.alimony_received, s1.alimony_unsupported, s1.cod_amount, s1.cod_any, s1.cod_unsupported, s1.gambling_pro, s1.gambling_winnings, s1.jury_to_employer, s1.line8_other, s1.line8b, s1.line8g, s1.line8h, s1.line8i, s1.line8j, s1.line8r, s1.uc_paid, s1.uc_repaid, s1.uc_unsupported | s1 |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | eic |
| shared page | sa |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: gift.h_over_5000_unflagged
    printed: "(helper)"
    label: "Consistency check: the deduction for this item or group of similar items is more than $5,000, the group is not publicly traded securities, and it was not reported as needing an appraisal (Section B)"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          gt: [gift.deduction, {const: 500000}]
        - op: test
          eq: [gift.public_securities, {const: false}]
        - op: test
          eq: [gift.special, {const: false}]
    note: "i8283 'Which Sections To Complete' and 'Section B': a deduction of more than $5,000 for an item or group of similar items, counting all donees together and other than publicly traded securities, belongs in Section B and needs a qualified appraisal. The gift.special question covers this case, so a 'No' answer together with such a deduction is contradictory. This line flags that contradiction and does not compute anything."
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount of your deduction for this noncash contribution (item or group of similar items), before applying any income limits"
    type: NonNegDollars
    expr:
      op: copy
      from: gift.deduction
    refuses:
      - gift.special
      - {when: gift.h_over_5000_unflagged, when_known: true}
    note: "Form 8283 is not used to figure the deduction ('do not use Form 8283 to figure your charitable contribution deduction'). The figure it reports is the 'amount of your deduction' before income limits, after the required reductions to the contribution. That figure is the supplied gift.deduction. Clothing and household items not in good used condition, and gifts of $250 or more without a contemporaneous written acknowledgment, are already excluded by that input's definition (i1040sca). Groups that need Section B, an appraisal or other special treatment are refused through gift.special. Publicly traded securities are reported in Section A at any amount, so gift.public_securities does not change the amount; it is used only in the consistency check. Income limits and carryovers belong to Schedule A and Pub. 526 (screened by sa.charity_limited), not to this per-group result. Open point: the interface name 'allowed' could mean a figure after income limits. The pages do not support that, so the before-limits amount was chosen."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: gift.h_nonpublic_over_5000
    printed: "(helper)"
    label: "Section B. Donated Property Over $5,000 (Except Publicly Traded Securities, Vehicles, Intellectual Property or Inventory Reportable in Section A): the deduction claimed for this item or group of similar items is more than $5,000 and the group is not publicly traded securities"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [gift.deduction, {const: 500000}]}
        - {op: test, eq: [gift.public_securities, {const: false}]}
    note: "Consistency check between supplied figures. i8283 says to use Section B, which requires a qualified appraisal, for a deduction of more than $5,000 per item or group of similar items, except for publicly traded securities and the other items reportable in Section A. A group that is not publicly traded securities and has a deduction over $5,000 must therefore have gift.special answered yes. The test uses $5,000 (500000 cents) and 'more than', following the printed text."
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount of your deduction for this item or group of similar items (your deduction before applying any income limits that could result in a carryover), reported in Form 8283 Section A"
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    refuses:
      - gift.special
      - {when: gift.h_nonpublic_over_5000, when_known: true}
    note: "The IRS text does not define a result named 'allowed'. Form 8283 does not figure the deduction ('do not use Form 8283 to figure your charitable contribution deduction'). It reports the deduction before income limits, which the filer supplies as gift.deduction after the required reductions and exclusions. I read gift.allowed as that amount, for groups the tool supports. These are groups reportable in Section A: more than $500 and not more than $5,000, or publicly traded securities in any amount. Groups needing Section B, an appraisal, or other special treatment are refused through gift.special. Income limits and carryovers (Pub. 526) are outside this form and are screened by sa.charity_limited. Under i1040sca, clothing and household items not in good used condition are left out of gift.deduction unless they are a single item over $500 with an appraisal; that case is refused by gift.special."
```
```
