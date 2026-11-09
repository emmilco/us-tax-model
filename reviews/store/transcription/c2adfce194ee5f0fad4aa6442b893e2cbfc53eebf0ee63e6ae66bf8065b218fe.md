# Review record c2adfce194ee — transcription f4952

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f4952",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v1",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "93d89df66bc52f77e3445bc8d7b6d15748cfd694b738dbbcbdd49474c4a9d21a",
 "response_sha256": "7f9fb5b5418d16ec7285a113a23b47d6ff738d15211f5e02dc3f44ae523edb7f",
 "scope": [
  "f4952.required",
  "4h",
  "8"
 ],
 "subjects": {
  "4h": "e11b98c2f91ad7e550f9e7349bb55f54fbe3169235120aa7f30f681ea607aa70"
 }
}
```

<!-- part block -->
#### Pass 93d89df66bc5

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines f4952.required, 4h, 8 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 93d89df66bc52f77e3445bc8d7b6d15748cfd694b738dbbcbdd49474c4a9d21a |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | efeeafe2e899ee3b399e7f71c6416707b276924d967b4521d893ab0e11b1036f |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | c26d4b274566f86df5f381a78b6c7c78cc3d6128ca86170b6ed53a18e4cd363b |
| receipt | .transcription/f4952.lines-a00ac5b69f6a |
| printed lines compared | 3 |
| agree / disagree / missing | 0 / 3 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, f1040, ftc, g28, household, person, sa, scope, sd, sdtw, u1250 |
| named line | qdcg |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: f4952.line4h
    printed: "4h"
    label: "Investment income. Add lines 4c, 4f, and 4g"
    type: Dollars
    expr:
      op: sum
      of: [f4952.line4c, f4952.line4f, f4952.line4g]
  - id: f4952.line8
    printed: "8"
    label: "Investment interest expense deduction. Enter the smaller of line 3 or line 6. See instructions"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [f4952.line3, f4952.line6]
    refuses: [f4952.unsupported]
    note: "The line 8 instructions send parts of the deduction attributable to royalties (Schedule E), a nonpassive trade or business, or an at-risk activity (Form 6198) elsewhere. Only the case where the whole amount goes to Schedule A, line 9 is computed. The other cases are refused through f4952.unsupported."
  - id: f4952.h_exception
    printed: "(helper)"
    label: "Exception: you don't have to file Form 4952 if all of the following apply. Your investment income from interest and ordinary dividends minus any qualified dividends is more than your investment interest expense; you don't have any other deductible investment expenses; you don't have any carryover of disallowed investment interest expense from 2024"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [f4952.line4c, f4952.line1]}
        - {op: test, eq: [f4952.line5, {const: 0}]}
        - {op: test, eq: [f4952.carryover, {const: false}]}
    note: "Line 4c (line 4a minus qualified dividends) is used for 'investment income from interest and ordinary dividends minus any qualified dividends'. Under the f4952.unsupported screen, line 4a holds only interest and ordinary dividends. Line 1 (2025 investment interest expense) is used for 'your investment interest expense', because the 2024 carryover is tested separately. Line 5 equal to zero is used for 'no other deductible investment expenses'."
  - id: f4952.required
    printed: "(helper)"
    label: "If you are an individual, an estate, or a trust, you must file Form 4952 to claim a deduction for your investment interest expense, unless the exception applies"
    type: Bool
    expr:
      op: test
      not: {op: test, eq: [f4952.h_exception, {const: true}]}
    note: "Open point: the text says you must file Form 4952 'to claim a deduction', so filing is only required when a deduction is claimed. This result is true whenever the exception does not apply. It does not separately test whether any investment interest is claimed (for example, whether line 1 is more than zero); callers decide whether a deduction is being claimed."
```
```
<!-- part section 4h -->
4h — Add lines 4c, 4f and 4g
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "4c"}, {"line": "4f"}, {"alternatives": [{"guard": {"args": [{"line": "4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "4g"}], "test": "lt"}, "then": {"line": "4g"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"line": "4c"}, {"line": "4f"}, {"line": "4g"}], "op": "sum"}
```

Ruling: open
Reviewed in: pass 93d89df66bc5

<!-- end -->
