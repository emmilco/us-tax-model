# Transcription agreement — ny_it2

Second transcription of `Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2` by an isolated model (spec 6.5), compared line by line with `forms/ny/2025/ny_it2.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4a85573cc2981a52278ca5581efcad4378e4208d0ca34bd4529ffd87c7338fef |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 7f2af62453301563ccca405c41501a1d61e4f5e74ff41a027933d3b112263a37 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 88a8a75553864c5ea7b4b1ea54e570455bcb7850416c70cb9be29a56e86b77e3 |
| printed lines compared | 2 |
| agree / disagree / missing | 0 / 2 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it2 | Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26 | 1, 2 | whole document | 4884d0d4403f8d1f3bd71a6834951e51fca1ca288ff3ecbab3c6866a286c10b8 | 2 | a6e61a9d7a0cd5464a36232dae9d0f4d5ca5380323f1117a2077f7e621049739 |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 17, 21 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 17, 21 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_rs, ny_tcw, ny_tcw_first |
| named lines: f1040.line11a, f1040.line27a | f1040 |
| named lines: person.sep_s3 | person |
| named lines: s2.line4 | s2 |
| shared page | ny_it201 |

## Lines

### 17a (whole dollars) — NYS income tax withheld, in whole dollars
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"of": {"line": "17a"}, "op": "round", "rule": "half_up", "unit": 100}}
```

Second:

```json
{"shown_when": {"args": [{"const": 0}, {"line": "17a"}], "test": "lt"}, "value": {"of": {"line": "17a"}, "op": "round", "rule": "half_up", "unit": 100}}
```

Second transcription's note: Rounding rule from 'Entering whole dollar amounts': amounts below 50 cents are dropped, and 50 to 99 cents go up to the next dollar. This is half-up rounding to the dollar. The rounded amounts from all IT-2 records go into Form IT-201, line 72.

Ruling: model error on shown_when; the reply shows the whole-dollar line only when the amount is more than zero. The project shows it on every record, as the source requires a record for every W-2: IT-201-I p. 21, "You must complete a W-2 record for each W-2 you receive, even if it does not show any New York State, New York City (NYC), or Yonkers wages or tax withheld." The value expressions are the same (half-up to the dollar; IT-2 p. 2, "drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar").

### 19 (whole dollars) — Local income tax withheld (New York City), in whole dollars
Status: **DISAGREE**

Project:

```json
{"shown_when": null, "value": {"of": {"line": "19"}, "op": "round", "rule": "half_up", "unit": 100}}
```

Second:

```json
{"shown_when": {"args": [{"const": 0}, {"line": "19"}], "test": "lt"}, "value": {"of": {"line": "19"}, "op": "round", "rule": "half_up", "unit": 100}}
```

Second transcription's note: On the form, box 19 holds either NYC or Yonkers withholding (in Locality a or b). This line is the NYC amount, which goes to Form IT-201, line 73. The Yonkers amount (ny_it2.yonkers_withheld, for line 74) was not requested here as a separate whole-dollar line. Rounding is half-up to the dollar, as for box 17a.

Ruling: model error on shown_when; the reply shows the whole-dollar line only when the amount is more than zero. The project shows it on every record, as the source requires a record for every W-2: IT-201-I p. 21, "You must complete a W-2 record for each W-2 you receive, even if it does not show any New York State, New York City (NYC), or Yonkers wages or tax withheld." The value expressions are the same (half-up to the dollar; IT-2 p. 2, "drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar").

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 17a (whole dollars) | 3667ce6499586d9d8e6f29a97233246ebab0656c3c25f67e0b1a9acd2f3aa4d8 |
| 19 (whole dollars) | 2640222756230b06d2f34c5434d92c4c9a248dd23ed8065a732af1567a054ba4 |
| (rest of the document) | 563acf0600ec1c8f1741f1d64d2bad8c9b36d45c64ada15fec51979356f9b8d0 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 17a (whole dollars) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 19 (whole dollars) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ny_it2.h_state_shown
    printed: "(helper)"
    label: "Box 17a is completed: New York State income tax withheld is shown on this Form W-2"
    type: Bool
    expr:
      op: test
      gt: [ny_it2.state_withheld, {const: 0}]
    note: "The IT-2 instructions say to leave boxes 16a and 17a blank if you have no New York State wages or withholding. The interface has no New York State wages input. So box 17a is shown only when New York State withholding (W-2 box 17 for NY) is more than zero. A blank box and a zero box carry the same amount."
  - id: ny_it2.state_whole
    printed: "17a (whole dollars)"
    label: "Box 17a NYS income tax withheld (enter whole dollar amounts only; drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar)"
    type: NonNegDollars
    expr:
      op: round
      of: ny_it2.state_withheld
      unit: 100
      rule: half_up
    shown_when: ny_it2.h_state_shown
    note: "Rounding rule from 'Entering whole dollar amounts': amounts below 50 cents are dropped, and 50 to 99 cents go up to the next dollar. This is half-up rounding to the dollar. The rounded amounts from all IT-2 records go into Form IT-201, line 72."
  - id: ny_it2.h_city_shown
    printed: "(helper)"
    label: "Box 19 (NYC locality) is completed: New York City income tax withheld is shown on this Form W-2"
    type: Bool
    expr:
      op: test
      gt: [ny_it2.city_withheld, {const: 0}]
    note: "The instructions say to complete locality boxes 18 through 20 only for NYC or Yonkers wages and withholding, if reported on the federal Form W-2. There is no locality-wages input. So the NYC box 19 amount is shown only when NYC withholding is more than zero."
  - id: ny_it2.city_whole
    printed: "19 (whole dollars)"
    label: "Box 19 Local income tax withheld, locality NYC (enter whole dollar amounts only; drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar)"
    type: NonNegDollars
    expr:
      op: round
      of: ny_it2.city_withheld
      unit: 100
      rule: half_up
    shown_when: ny_it2.h_city_shown
    note: "On the form, box 19 holds either NYC or Yonkers withholding (in Locality a or b). This line is the NYC amount, which goes to Form IT-201, line 73. The Yonkers amount (ny_it2.yonkers_withheld, for line 74) was not requested here as a separate whole-dollar line. Rounding is half-up to the dollar, as for box 17a."
```
```
