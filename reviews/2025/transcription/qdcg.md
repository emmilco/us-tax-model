# Transcription agreement — qdcg

Second transcription of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/qdcg.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | 40fc2376a6e1a9a2d7729b4689f0af01df0e88777dc6578f08bed3cccbef1c76 |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 81d2f1dd22ed930c869f4c72dfaede472cb7aa0aeceefbe5d68a09b628d819b5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 6100db164f445104624c5ab49f073f2d2b4eb2678169223aa3bbcc859f9a3f82 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0ec80da435463402c2d8e70745618a3a4b8e2d8949ed1b76192d41f26ba57324 |
| printed lines compared | 26 |
| agree / disagree / missing | 22 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (question) — Are you filing Schedule D?
Status: **AGREE**

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555
Status: **AGREE**

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}], "test": "lt"}, "then": {"ref": "f1040.line3a"}}], "op": "choose"}
```

Second:

```json
{"ref": "f1040.line3a"}
```

Second transcription's note: The footnote sends Form 2555 filers to the Foreign Earned Income Tax Worksheet footnote. That text is not supplied here, so only the line 3a amount is encoded.

Ruling: model error; the candidate reads f1040.line3a whatever box 1a is above zero, so it needs that answer where the source does not: i1040gi p. 25, Line 3a, "Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b": with box 1a (line 3b) zero, line 3a is zero. The project reads the gate line f1040.line3a_if_ordinary, which takes f1040.line3a when box 1a is above zero holds and zero otherwise; the interview asks f1040.line3a only then (gated_by f1040.line3a_if_ordinary), so on every return the interview can produce with the condition true the two sides agree. Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass 4b5ad4d24360

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sd.distributions"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"ref": "f1040.line7a"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": true}, {"line": "(question)"}], "test": "eq"}, "then": {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Ruling: equivalent representation; project retained. The No branch reads “Enter the amount from Form 1040 or 1040-SR, line 7a” (i1040gi p. 38). When Schedule D is not required, line 7a carries the total capital gain distributions from Form 1099-DIV box 2a (i1040gi p. 33, line 7a, Exception 1), the value the project references directly through its gate line sd.distributions_if_dividends (box 2a when dividends or distributions were received, zero otherwise); the candidate references line 7a literally, as in the earlier ruling of this line.
Reviewed in: pass 4b5ad4d24360

### 4 — Add lines 2 and 3
Status: **AGREE**

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **DISAGREE**

Project:

```json
{"param": "qdcg.zero_rate_ceiling"}
```

Second:

```json
{"from": {"param": "qdcg.zero_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged.

Ruling: representation; i1040gi p.38 line6 prints positive filing-status ceilings. The matching year parameter is always positive in every declared status; subtract_floor0(parameter,0) leaves that amount unchanged and adds no missing filer input. The extra floor does not change the printed quantity.

### 7 — Enter the smaller of line 1 or line 6
Status: **AGREE**

### 8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **AGREE**

### 10 — Enter the smaller of line 1 or line 4
Status: **AGREE**

### 11 — Enter the amount from line 9
Status: **AGREE**

### 12 — Subtract line 11 from line 10
Status: **AGREE**

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **DISAGREE**

Project:

```json
{"param": "qdcg.fifteen_rate_ceiling"}
```

Second:

```json
{"from": {"param": "qdcg.fifteen_rate_ceiling"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged.

Ruling: representation; i1040gi p.38 line13 prints positive filing-status ceilings. The matching year parameter is always positive in every declared status; subtract_floor0(parameter,0) leaves that amount unchanged and adds no missing filer input. The extra floor does not change the printed quantity.

### 14 — Enter the smaller of line 1 or line 13
Status: **AGREE**

### 15 — Add lines 5 and 9
Status: **AGREE**

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **AGREE**

### 17 — Enter the smaller of line 12 or line 16
Status: **AGREE**

### 18 — Multiply line 17 by 15% (0.15)
Status: **AGREE**

### 19 — Add lines 9 and 17
Status: **AGREE**

### 20 — Subtract line 19 from line 10
Status: **AGREE**

### 21 — Multiply line 20 by 20% (0.20)
Status: **AGREE**

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **AGREE**

### 23 — Add lines 18, 21, and 22
Status: **AGREE**

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **AGREE**

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | sa.excluded_income | - |
| 5 | sa.excluded_income | - |
| 7 | sa.excluded_income | - |
| 8 | sa.excluded_income | - |
| 9 | sa.excluded_income | - |
| 10 | sa.excluded_income | - |
| 11 | sa.excluded_income | - |
| 12 | sa.excluded_income | - |
| 14 | sa.excluded_income | - |
| 15 | sa.excluded_income | - |
| 16 | sa.excluded_income | - |
| 17 | sa.excluded_income | - |
| 18 | sa.excluded_income | - |
| 19 | sa.excluded_income | - |
| 20 | sa.excluded_income | - |
| 21 | sa.excluded_income | - |
| 22 | sa.excluded_income | - |
| 23 | sa.excluded_income | - |
| 24 | sa.excluded_income | - |
| 25 | sa.excluded_income | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (question) | 1755ec95f96d6eb16f557ff0a764d3d65b5157c931ac2508fe5f174cb87a6914 |
| 1 | 0db46a35a7ee0b04e336416534a77d24631506703e686767755693e5b114ed17 |
| 2 | 73762dce96c5e41a836d5c04db6fb29183c2e4df99c9040514217a98bfd805a0 |
| 3 | ee97d5c467e589a343409725373430584bc811b0f4e10d4f5bc2cf4bfbfe62b9 |
| 4 | ea387178ae2e311c71bf20912a1681a1f6324608dc0529a8502b8e753aa36941 |
| 5 | cc7d7bc947fc103adac4f6807d45ef453f6aa98d5632dfff37f022d407f94cd6 |
| 6 | 3325b82c831e9576c61ad9ca15b708c1f6fc590b5e6227244f0313c680c3f18f |
| 7 | 81fd8ad61b3d859886500d87b412fac0d0a4665f2ee2c8083c7ac180f7fe5a9f |
| 8 | 8f8209fc9dedc28ae4c57bd2829db6acd8354385f0363b93b9cc9aba4259a5cb |
| 9 | a71fb2fa2af20d4b027ff72016bcc678905c797455386aa4e3cd8084ccf8cf8f |
| 10 | 0aca8c826da32b53c036e2fc95747a749906c880291ddb1d72b8af3f0571d4d8 |
| 11 | cc077139375e81580bad261fe23589134ce681f6a63385a2570b9de62cfa83d9 |
| 12 | 0c3775c87c750552313eff14ae10f2a2c0540b1ee0d4973d5cbd914c6871c78a |
| 13 | 784f95c29779d0e62974162f9b1a765efc10df7f73544f988b70761d42dc650c |
| 14 | cae008834460034435e10929b28c654030c519848ef317b809d40d2e73cfcc4c |
| 15 | fbc76078beb08d12e98b267eb10aa2ad1ba46326092382b26b1c9aabebe4112c |
| 16 | abc12ba448b2bcbd56b96c450ea5875c11f8924feb1e4b7876418dab957c9fb3 |
| 17 | 2e7b1fd7747e64956f7455597adedcf6391d217e600e29acfb314018b27355ac |
| 18 | ed0588125b2bd474f5e5d051447162eba1e1d81bd9cd82dd49f9ec2a348ae852 |
| 19 | 29d596d6c096ec7a9142b728e1596a0fccdd86448d0561b741c1b95f1e8e07c4 |
| 20 | e3a34369ea4f665e221a8372d4e15b15355ea18fcbe23c6168b9a8ae58970e86 |
| 21 | 196c5ae69fe73dc044f61b060814d285f7b62c5cb6b1f29766b9a7f96b186187 |
| 22 | aac12abda31affeaf4beba3db03f3f76ad9601d4ecbdbea4ec5cc8c19c985f97 |
| 23 | d2f12f8595e91923be5ad26cca163469d14a8e53cff91a16eda5c851477b6fb3 |
| 24 | e4a4ecd32352388e6c216bc638565fc1f768110914080a3baea7a45a0ff79b9f |
| 25 | 1edbfd1c114c0bf78e12023c6c9044af482dd524cf15b40a369a6877fb3f17da |
| (rest of the document) | 9834d8f9eaa00f8ff7494eee1cdbaf5394af2f0de2d80b1eca9f8c02c95934e4 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 2 | 5d5fac7682b7a2fa13c2250bae25effb6239a504e9095246e6b2c15009ed77b2 |
| 3 | 0b46ad0c66365fc911ceac5efb8f7b20969dca09cb954900c5d3bce78c348634 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 4b5ad4d24360

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 2, 3 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4b5ad4d243603762dc3af92f3a745de3975384e9cd79ec4fba9b786298e60b52 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | 54bc879230953cc6aea184849ad44cf1bffce16be1bc91ccf878bcb4ad733566 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7ea2d588ac542def30c0e9b6e6c078c7b71e40cd5de41427ec3ff3cbe061190d |
| receipt | .transcription/qdcg.lines-46584c88c62d |
| printed lines compared | 2 |
| agree / disagree / missing | 0 / 2 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: f1040.line15, f1040.line16, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.line7a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named form, inputs and named lines: u1250.line16 | u1250 |
| named line | f4952, ftc |
| shared page | sd, sdtw |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: qdcg.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}
    note: "The footnote sends Form 2555 filers to the Foreign Earned Income Tax Worksheet footnote. That text is not supplied here, so only the line 3a amount is encoded."
  - id: qdcg.h_sd_smaller
    printed: "(helper)"
    label: "Smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}
  - id: qdcg.h_sd_amount
    printed: "(helper)"
    label: "Smaller of Schedule D line 15 or line 16; if either line 15 or line 16 is blank or a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_sd_smaller, take: {param: sales.zero}}
    note: "If either line is a loss, the smaller of the two is zero or less, so flooring the smaller amount at zero gives the -0- the text calls for. A blank line is read as zero."
  - id: qdcg.h_no_sd_amount
    printed: "(helper)"
    label: "Amount from Form 1040 or 1040-SR, line 7a"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line7a, take: {param: sales.zero}}
    note: "The No branch says to enter line 7a and gives no zero floor. Without Schedule D, line 7a holds only capital gain distributions, which cannot be negative. The floor at zero is there only so the NonNegDollars type can be proved; it does not change any value."
  - id: qdcg.line3
    printed: "3"
    label: "Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: true}]}
          then: qdcg.h_sd_amount
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: false}]}
          then: qdcg.h_no_sd_amount
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: qdcg.schedule_d_filed
    printed: "(question)"
    label: "Are you filing Schedule D?"
    type: Bool
    expr: {op: copy, from: sd.filed}
    note: "The interface is closed, so this question is not a new input. It is read from the project's Schedule D filing determination (sd.filed)."

  - id: qdcg.line1
    printed: "1"
    label: "Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    refuses: [sa.excluded_income]
    note: "The Form 2555 case (Foreign Earned Income Tax Worksheet, also the footnote to lines 2 and 3) is not computed. The screening input sa.excluded_income (filing Form 2555) refuses it instead."

  - id: qdcg.line2
    printed: "2"
    label: "Enter the amount from Form 1040 or 1040-SR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}

  - id: qdcg.h_sd15_pos
    printed: "(helper)"
    label: "Schedule D, line 15; -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: {const: 0}}

  - id: qdcg.h_sd16_pos
    printed: "(helper)"
    label: "Schedule D, line 16; -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line16, take: {const: 0}}

  - id: qdcg.h_sd_smaller
    printed: "(helper)"
    label: "Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.h_sd15_pos, qdcg.h_sd16_pos]}

  - id: qdcg.h_line7a_pos
    printed: "(helper)"
    label: "No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line7a, take: {const: 0}}
    note: "Without Schedule D, line 7a holds only capital gain distributions, which cannot be negative. The zero floor only proves the type and does not change any value on that path."

  - id: qdcg.line3
    printed: "3"
    label: "Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: true}]}
          then: qdcg.h_sd_smaller
        - guard: {op: test, eq: [qdcg.schedule_d_filed, {const: false}]}
          then: qdcg.h_line7a_pos

  - id: qdcg.line4
    printed: "4"
    label: "Add lines 2 and 3"
    type: NonNegDollars
    expr: {op: sum, of: [qdcg.line2, qdcg.line3]}

  - id: qdcg.line5
    printed: "5"
    label: "Subtract line 4 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.line1, take: qdcg.line4}

  - id: qdcg.h_zero_ceiling
    printed: "(helper)"
    label: "$48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}

  - id: qdcg.line6
    printed: "6"
    label: "Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_zero_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged."

  - id: qdcg.line7
    printed: "7"
    label: "Enter the smaller of line 1 or line 6"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line6]}

  - id: qdcg.line8
    printed: "8"
    label: "Enter the smaller of line 5 or line 7"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line5, qdcg.line7]}

  - id: qdcg.line9
    printed: "9"
    label: "Subtract line 8 from line 7. This amount is taxed at 0%"
    type: Dollars
    expr: {op: subtract, from: qdcg.line7, take: qdcg.line8}

  - id: qdcg.line10
    printed: "10"
    label: "Enter the smaller of line 1 or line 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line4]}

  - id: qdcg.line11
    printed: "11"
    label: "Enter the amount from line 9"
    type: Dollars
    expr: {op: copy, from: qdcg.line9}

  - id: qdcg.line12
    printed: "12"
    label: "Subtract line 11 from line 10"
    type: Dollars
    expr: {op: subtract, from: qdcg.line10, take: qdcg.line11}

  - id: qdcg.h_fifteen_ceiling
    printed: "(helper)"
    label: "$533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household"
    type: Dollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}

  - id: qdcg.line13
    printed: "13"
    label: "Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.h_fifteen_ceiling, take: {const: 0}}
    note: "The parameter is declared Dollars. The zero floor only proves the result is nonnegative; every printed amount is positive, so the value is unchanged."

  - id: qdcg.line14
    printed: "14"
    label: "Enter the smaller of line 1 or line 13"
    type: NonNegDollars
    expr: {op: smaller_of, of: [qdcg.line1, qdcg.line13]}

  - id: qdcg.line15
    printed: "15"
    label: "Add lines 5 and 9"
    type: Dollars
    expr: {op: sum, of: [qdcg.line5, qdcg.line9]}

  - id: qdcg.line16
    printed: "16"
    label: "Subtract line 15 from line 14. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qdcg.line14, take: qdcg.line15}

  - id: qdcg.line17
    printed: "17"
    label: "Enter the smaller of line 12 or line 16"
    type: Dollars
    expr: {op: smaller_of, of: [qdcg.line12, qdcg.line16]}

  - id: qdcg.line18
    printed: "18"
    label: "Multiply line 17 by 15% (0.15)"
    type: Dollars
    expr: {op: multiply_rate, amount: qdcg.line17, rate: {param: qdcg.rate_15}}

  - id: qdcg.line19
    printed: "19"
    label: "Add lines 9 and 17"
    type: Dollars
    expr: {op: sum, of: [qdcg.line9, qdcg.line17]}

  - id: qdcg.line20
    printed: "20"
    label: "Subtract line 19 from line 10"
    type: Dollars
    expr: {op: subtract, from: qdcg.line10, take: qdcg.line19}

  - id: qdcg.line21
    printed: "21"
    label: "Multiply line 20 by 20% (0.20)"
    type: Dollars
    expr: {op: multiply_rate, amount: qdcg.line20, rate: {param: qdcg.rate_20}}

  - id: qdcg.line22
    printed: "22"
    label: "Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 5 is $100,000 or more, use the Tax Computation Worksheet"
    type: Dollars
    expr:
      op: copy
      from: {def: tax_on_amount, bind: {amount: qdcg.line5, status: f1040.status}, line: tax}
    note: "The shared tax_on_amount definition applies the $100,000 boundary: the Tax Table below it, the Tax Computation Worksheet at or above it."

  - id: qdcg.line23
    printed: "23"
    label: "Add lines 18, 21, and 22"
    type: Dollars
    expr: {op: sum, of: [qdcg.line18, qdcg.line21, qdcg.line22]}

  - id: qdcg.line24
    printed: "24"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet"
    type: Dollars
    expr:
      op: copy
      from: {def: tax_on_amount, bind: {amount: qdcg.line1, status: f1040.status}, line: tax}

  - id: qdcg.line25
    printed: "25"
    label: "Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amount on the entry space on Form 1040 or 1040-SR, line 16. If you are filing Form 2555, don't enter this amount on the entry space on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet"
    type: Dollars
    expr: {op: smaller_of, of: [qdcg.line23, qdcg.line24]}
    note: "The Form 2555 routing is not computed; it is refused at line 1 through sa.excluded_income. Whether this worksheet applies at all is decided on Form 1040 (f1040.gate.qdcg_applies), not here."
```
```
