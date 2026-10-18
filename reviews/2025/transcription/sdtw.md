# Transcription agreement — sdtw

Second transcription of `Schedule D Tax Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/sdtw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 65ff58f9adbbc5d464076085e1b3f04c5a9c2fb76e9f31048f1f591b5d4b37d1 |
| printed lines compared | 47 |
| agree / disagree / missing | 29 / 18 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Taxable income
Status: **AGREE**

### 2 — Qualified dividends
Status: **AGREE**

### 3 — Form 4952 line 4g election
Status: **AGREE**

### 4 — Form 4952 line 4e, default capital-gain-first allocation
Status: **AGREE**

### 5 — Subtract line 4 from line 3; floor at zero
Status: **AGREE**

### 6 — Subtract line 5 from line 2; floor at zero
Status: **AGREE**

### 7 — Smaller of Schedule D lines 15 and 16
Status: **AGREE**

### 8 — Smaller of lines 3 and 4
Status: **AGREE**

### 9 — Subtract line 8 from line 7; floor at zero
Status: **AGREE**

### 10 — Add lines 6 and 9
Status: **AGREE**

### 11 — Add Schedule D lines 18 and 19
Status: **AGREE**

### 12 — Smaller of lines 9 and 11
Status: **AGREE**

### 13 — Subtract line 12 from line 10
Status: **AGREE**

### 14 — Subtract line 13 from line 1; floor at zero
Status: **AGREE**

### 15 — Zero-rate ceiling by filing status
Status: **AGREE**

### 16 — Smaller of lines 1 and 15
Status: **AGREE**

### 17 — Smaller of lines 14 and 16
Status: **AGREE**

### 18 — Subtract line 10 from line 1; floor at zero
Status: **AGREE**

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **AGREE**

### 20 — Smaller of lines 14 and 19
Status: **AGREE**

### 21 — Larger of lines 18 and 20
Status: **AGREE**

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **AGREE**

### 23 — Smaller of lines 1 and 13
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "1"}, {"line": "13"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "1"}, {"line": "13"}], "op": "smaller_of"}
```

Second transcription's note: This line is computed even when skipped. Its value reaches line 45 only through gated lines 30, 33, 39 and 42, which are zero when skipped.

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 24 — Amount from line 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"line": "22"}}], "op": "choose"}
```

Second:

```json
{"line": "22"}
```

Second transcription's note: Line 22 is always computed, so it is never blank here.

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"from": {"line": "23"}, "op": "subtract_floor0", "take": {"line": "24"}}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "23"}, "op": "subtract_floor0", "take": {"line": "24"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 26 — 15-percent ceiling by filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"param": "qdcg.fifteen_rate_ceiling"}}], "op": "choose"}
```

Second:

```json
{"param": "qdcg.fifteen_rate_ceiling"}
```

Second transcription's note: The parameter is keyed by filing status (f1040.status).

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 27 — Smaller of lines 1 and 26
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "1"}, {"line": "26"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "1"}, {"line": "26"}], "op": "smaller_of"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 28 — Add lines 21 and 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "21"}, {"line": "22"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "21"}, {"line": "22"}], "op": "sum"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"from": {"line": "27"}, "op": "subtract_floor0", "take": {"line": "28"}}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "27"}, "op": "subtract_floor0", "take": {"line": "28"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 30 — Smaller of lines 25 and 29
Status: **AGREE**

### 31 — Multiply line 30 by 15 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "30"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate15"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 32 — Add lines 24 and 30
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, "then": {"of": [{"line": "24"}, {"line": "30"}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "24"}, {"line": "30"}], "op": "sum"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 33 — Subtract line 32 from line 23
Status: **AGREE**

### 34 — Multiply line 33 by 20 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate20"}}}, {"guard": {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "33"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate20"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "9"}, {"ref": "u1250.line18"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "9"}, {"ref": "u1250.line18"}], "op": "smaller_of"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 36 — Add lines 10 and 21
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"line": "10"}, {"line": "21"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "10"}, {"line": "21"}], "op": "sum"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 37 — Amount from line 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, "then": {"line": "1"}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "1"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "36"}, "op": "subtract_floor0", "take": {"line": "37"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"line": "36"}, "op": "subtract_floor0", "take": {"line": "37"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **AGREE**

### 40 — Multiply line 39 by 25 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "39"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate25"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"of": [{"line": "21"}, {"line": "22"}, {"line": "30"}, {"line": "33"}, {"line": "39"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"args": [{"ref": "g28.line7"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "21"}, {"line": "22"}, {"line": "30"}, {"line": "33"}, {"line": "39"}], "op": "sum"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 42 — Subtract line 41 from line 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}}, {"guard": {"args": [{"args": [{"args": [{"ref": "g28.line7"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "1"}, "op": "subtract", "take": {"line": "41"}}}, {"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}, {"args": [{"ref": "g28.line7"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 43 — Multiply line 42 by 28 percent
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "ne"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "g28.line7"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}}, {"guard": {"args": [{"args": [{"args": [{"ref": "g28.line7"}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"ref": "u1250.line18"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"line": "1"}, {"line": "16"}], "test": "eq"}, {"args": [{"line": "1"}, {"line": "32"}], "test": "eq"}], "test": "any"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"amount": {"line": "42"}, "op": "multiply_rate", "rate": {"param": "sdtw.rate28"}}
```

Ruling: representation of the skip rules; project retained; equivalence argued, not proved. The worksheet says to skip lines 23–43 when lines 1 and 16 are the same, lines 33–43 when lines 1 and 32 are the same, lines 35–40 when Schedule D line 19 is zero or blank, and lines 41–43 when Schedule D line 18 is zero or blank (i1040sd pp. 15–16, Schedule D Tax Worksheet). The project encodes each skip as a zero-valued alternative on every skipped line; the second transcription computes every line unconditionally and treats a skipped line as blank only where a later line reads it. The two agree in value when the skipped lines are zero anyway: with lines 1 and 16 equal, line 17 equals line 1 less line 13 and line 22 equals line 13, so lines 25 and 29, hence 30–34, are zero; with Schedule D line 19 zero, line 35 and so 39–40 are zero; with Schedule D line 18 zero, line 42 is the remainder of line 1 after the ordinary, 0%, 15%, 20% and 25% portions (lines 21, 22, 30, 33, 39) and is zero. That argument is recorded here, not machine-checked; it is a candidate property for the data-level property tests of spec 6.3 (a skipped line evaluates to zero under the project's reading and under unconditional computation). No change to the data.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **AGREE**

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **AGREE**

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **AGREE**

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | sa.excluded_income | - |
| 4 | f4952.alternative_allocation | f4952.alternative_allocation |
| 5 | f4952.alternative_allocation | - |
| 6 | f4952.alternative_allocation, sa.excluded_income | sa.excluded_income |
| 8 | f4952.alternative_allocation | - |
| 9 | f4952.alternative_allocation, sa.excluded_income | sa.excluded_income |
| 10 | f4952.alternative_allocation, sa.excluded_income | sa.excluded_income |
| 11 | sa.excluded_income | sa.excluded_income |
| 12 | f4952.alternative_allocation, sa.excluded_income | sa.excluded_income |
| 13 | f4952.alternative_allocation, sa.excluded_income | sa.excluded_income |
| 14 | f4952.alternative_allocation, sa.excluded_income | - |
| 16 | sa.excluded_income | - |
| 17 | f4952.alternative_allocation, sa.excluded_income | - |
| 18 | f4952.alternative_allocation, sa.excluded_income | - |
| 19 | sa.excluded_income | - |
| 20 | f4952.alternative_allocation, sa.excluded_income | - |
| 21 | f4952.alternative_allocation, sa.excluded_income | - |
| 22 | f4952.alternative_allocation, sa.excluded_income | - |
| 23 | f4952.alternative_allocation, sa.excluded_income | - |
| 24 | f4952.alternative_allocation, sa.excluded_income | - |
| 25 | f4952.alternative_allocation, sa.excluded_income | - |
| 27 | sa.excluded_income | - |
| 28 | f4952.alternative_allocation, sa.excluded_income | - |
| 29 | f4952.alternative_allocation, sa.excluded_income | - |
| 30 | f4952.alternative_allocation, sa.excluded_income | - |
| 31 | f4952.alternative_allocation, sa.excluded_income | - |
| 32 | f4952.alternative_allocation, sa.excluded_income | - |
| 33 | f4952.alternative_allocation, sa.excluded_income | - |
| 34 | f4952.alternative_allocation, sa.excluded_income | - |
| 35 | f4952.alternative_allocation, sa.excluded_income | - |
| 36 | f4952.alternative_allocation, sa.excluded_income | - |
| 37 | sa.excluded_income | - |
| 38 | f4952.alternative_allocation, sa.excluded_income | - |
| 39 | f4952.alternative_allocation, sa.excluded_income | - |
| 40 | f4952.alternative_allocation, sa.excluded_income | - |
| 41 | f4952.alternative_allocation, sa.excluded_income | - |
| 42 | f4952.alternative_allocation, sa.excluded_income | - |
| 43 | f4952.alternative_allocation, sa.excluded_income | - |
| 44 | f4952.alternative_allocation, sa.excluded_income | - |
| 45 | f4952.alternative_allocation, sa.excluded_income | - |
| 46 | sa.excluded_income | - |
| 47 | f4952.alternative_allocation, sa.excluded_income | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sdtw.line1
    printed: "1"
    label: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line15}
    refuses: [sa.excluded_income]
    note: "The Form 2555 substitution is not computed. The tool refuses through the screening input that covers Form 2555."

  - id: sdtw.line2
    printed: "2"
    label: "Enter your qualified dividends from Form 1040, 1040-SR, or 1040-NR, line 3a"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3a}

  - id: sdtw.line3
    printed: "3"
    label: "Enter the amount from Form 4952 (used to figure investment interest expense deduction), line 4g"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
    note: "The text does not say what to enter when Form 4952 is not filed. Chosen reading: f4952.line4g carries zero in that case."

  - id: sdtw.line4
    printed: "4"
    label: "Enter the amount from Form 4952, line 4e* (* If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952.)"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4e}
    refuses: [f4952.alternative_allocation]
    note: "The footnote's dotted-line smaller amount applies only under an alternative allocation election. That case is refused, so only the default line 4e is used."

  - id: sdtw.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line3, take: sdtw.line4}

  - id: sdtw.line6
    printed: "6"
    label: "Subtract line 5 from line 2. If zero or less, enter -0-**"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line2, take: sdtw.line5}
    refuses: [sa.excluded_income]
    note: "The ** footnote (Form 2555) is not computed and is refused."

  - id: sdtw.line7
    printed: "7"
    label: "Enter the smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}

  - id: sdtw.line8
    printed: "8"
    label: "Enter the smaller of line 3 or line 4"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line3, sdtw.line4]}

  - id: sdtw.line9
    printed: "9"
    label: "Subtract line 8 from line 7. If zero or less, enter -0-**"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line7, take: sdtw.line8}
    refuses: [sa.excluded_income]

  - id: sdtw.line10
    printed: "10"
    label: "Add lines 6 and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sdtw.line6, sdtw.line9]}

  - id: sdtw.line11
    printed: "11"
    label: "Add lines 18 and 19 of Schedule D**"
    type: NonNegDollars
    expr: {op: sum, of: [sd.line18, sd.line19]}
    refuses: [sa.excluded_income]

  - id: sdtw.line12
    printed: "12"
    label: "Enter the smaller of line 9 or line 11"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line9, sdtw.line11]}

  - id: sdtw.line13
    printed: "13"
    label: "Subtract line 12 from line 10"
    type: Dollars
    expr: {op: subtract, from: sdtw.line10, take: sdtw.line12}

  - id: sdtw.line14
    printed: "14"
    label: "Subtract line 13 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line1, take: sdtw.line13}

  - id: sdtw.line15
    printed: "15"
    label: "Enter: $48,350 if single or married filing separately; $96,700 if married filing jointly or qualifying surviving spouse; or $64,750 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: qdcg.zero_rate_ceiling}
    note: "The parameter is keyed by filing status (f1040.status)."

  - id: sdtw.line16
    printed: "16"
    label: "Enter the smaller of line 1 or line 15"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line15]}

  - id: sdtw.line17
    printed: "17"
    label: "Enter the smaller of line 14 or line 16"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line14, sdtw.line16]}

  - id: sdtw.line18
    printed: "18"
    label: "Subtract line 10 from line 1. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line1, take: sdtw.line10}

  - id: sdtw.h_ordinary_ceiling
    printed: "(helper)"
    label: "$197,300 if single or married filing separately; $394,600 if married filing jointly or qualifying surviving spouse; or $197,300 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: sdtw.ordinary_ceiling}
    note: "The parameter is keyed by filing status (f1040.status)."

  - id: sdtw.line19
    printed: "19"
    label: "Enter the smaller of line 1 or: $197,300 if single or married filing separately; $394,600 if married filing jointly or qualifying surviving spouse; or $197,300 if head of household"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.h_ordinary_ceiling]}

  - id: sdtw.line20
    printed: "20"
    label: "Enter the smaller of line 14 or line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line14, sdtw.line19]}

  - id: sdtw.line21
    printed: "21"
    label: "Enter the larger of line 18 or line 20"
    type: NonNegDollars
    expr: {op: larger_of, of: [sdtw.line18, sdtw.line20]}

  - id: sdtw.line22
    printed: "22"
    label: "Subtract line 17 from line 16. This amount is taxed at 0%"
    type: Dollars
    expr: {op: subtract, from: sdtw.line16, take: sdtw.line17}

  - id: sdtw.h_zero
    printed: "(helper)"
    label: "Zero entered for a skipped (blank) line"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sdtw.h_skip23
    printed: "(helper)"
    label: "If lines 1 and 16 are the same, skip lines 23 through 43 and go to line 44"
    type: Bool
    expr: {op: test, eq: [sdtw.line1, sdtw.line16]}

  - id: sdtw.line23
    printed: "23"
    label: "Enter the smaller of line 1 or line 13"
    type: Dollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line13]}
    note: "This line is computed even when skipped. Its value reaches line 45 only through gated lines 30, 33, 39 and 42, which are zero when skipped."

  - id: sdtw.line24
    printed: "24"
    label: "Enter the amount from line 22. (If line 22 is blank, enter -0-.)"
    type: Dollars
    expr: {op: copy, from: sdtw.line22}
    note: "Line 22 is always computed, so it is never blank here."

  - id: sdtw.line25
    printed: "25"
    label: "Subtract line 24 from line 23. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line23, take: sdtw.line24}

  - id: sdtw.line26
    printed: "26"
    label: "Enter: $533,400 if single; $300,000 if married filing separately; $600,050 if married filing jointly or qualifying surviving spouse; or $566,700 if head of household"
    type: NonNegDollars
    expr: {op: param, ref: qdcg.fifteen_rate_ceiling}
    note: "The parameter is keyed by filing status (f1040.status)."

  - id: sdtw.line27
    printed: "27"
    label: "Enter the smaller of line 1 or line 26"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line1, sdtw.line26]}

  - id: sdtw.line28
    printed: "28"
    label: "Add lines 21 and 22"
    type: Dollars
    expr: {op: sum, of: [sdtw.line21, sdtw.line22]}

  - id: sdtw.line29
    printed: "29"
    label: "Subtract line 28 from line 27. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line27, take: sdtw.line28}

  - id: sdtw.h_line30_raw
    printed: "(helper)"
    label: "Smaller of line 25 or line 29, before the skip instruction"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line25, sdtw.line29]}

  - id: sdtw.line30
    printed: "30"
    label: "Enter the smaller of line 25 or line 29"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip23, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip23, {const: false}]}
          then: sdtw.h_line30_raw
    note: "A skipped line is treated as blank, which is zero."

  - id: sdtw.line31
    printed: "31"
    label: "Multiply line 30 by 15% (0.15)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line30, rate: {param: sdtw.rate15}}

  - id: sdtw.line32
    printed: "32"
    label: "Add lines 24 and 30"
    type: Dollars
    expr: {op: sum, of: [sdtw.line24, sdtw.line30]}

  - id: sdtw.h_skip33_self
    printed: "(helper)"
    label: "If lines 1 and 32 are the same, skip lines 33 through 43 and go to line 44"
    type: Bool
    expr: {op: test, eq: [sdtw.line1, sdtw.line32]}

  - id: sdtw.h_skip33
    printed: "(helper)"
    label: "Line 33 skipped, by the line 22 instruction or the line 32 instruction"
    type: Bool
    expr: {op: test, any: [sdtw.h_skip23, sdtw.h_skip33_self]}

  - id: sdtw.h_line33_raw
    printed: "(helper)"
    label: "Subtract line 32 from line 23, before the skip instruction"
    type: Dollars
    expr: {op: subtract, from: sdtw.line23, take: sdtw.line32}

  - id: sdtw.line33
    printed: "33"
    label: "Subtract line 32 from line 23"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip33, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip33, {const: false}]}
          then: sdtw.h_line33_raw

  - id: sdtw.line34
    printed: "34"
    label: "Multiply line 33 by 20% (0.20)"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line33, rate: {param: sdtw.rate20}}

  - id: sdtw.h_line19_zero
    printed: "(helper)"
    label: "If Schedule D, line 19, is zero or blank, skip lines 35 through 40 and go to line 41"
    type: Bool
    expr: {op: test, eq: [sd.line19, {const: 0}]}
    note: "A blank line 19 is treated as zero."

  - id: sdtw.h_skip35
    printed: "(helper)"
    label: "Lines 35 through 40 skipped, by an earlier skip instruction or because Schedule D line 19 is zero or blank"
    type: Bool
    expr: {op: test, any: [sdtw.h_skip33, sdtw.h_line19_zero]}

  - id: sdtw.line35
    printed: "35"
    label: "Enter the smaller of line 9 above or Schedule D, line 19"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sdtw.line9, sd.line19]}

  - id: sdtw.line36
    printed: "36"
    label: "Add lines 10 and 21"
    type: NonNegDollars
    expr: {op: sum, of: [sdtw.line10, sdtw.line21]}

  - id: sdtw.line37
    printed: "37"
    label: "Enter the amount from line 1 above"
    type: NonNegDollars
    expr: {op: copy, from: sdtw.line1}

  - id: sdtw.line38
    printed: "38"
    label: "Subtract line 37 from line 36. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line36, take: sdtw.line37}

  - id: sdtw.h_line39_raw
    printed: "(helper)"
    label: "Subtract line 38 from line 35, floor at zero, before the skip instruction"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sdtw.line35, take: sdtw.line38}

  - id: sdtw.line39
    printed: "39"
    label: "Subtract line 38 from line 35. If zero or less, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip35, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip35, {const: false}]}
          then: sdtw.h_line39_raw
    note: "When lines 35 through 40 are skipped, line 39 is blank and enters line 41 as zero."

  - id: sdtw.line40
    printed: "40"
    label: "Multiply line 39 by 25% (0.25)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sdtw.line39, rate: {param: sdtw.rate25}}

  - id: sdtw.h_line18_zero
    printed: "(helper)"
    label: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44"
    type: Bool
    expr: {op: test, eq: [sd.line18, {const: 0}]}

  - id: sdtw.h_skip41
    printed: "(helper)"
    label: "Lines 41 through 43 skipped, by an earlier skip instruction or because Schedule D line 18 is zero or blank"
    type: Bool
    expr: {op: test, any: [sdtw.h_skip33, sdtw.h_line18_zero]}

  - id: sdtw.line41
    printed: "41"
    label: "Add lines 21, 22, 30, 33, and 39"
    type: Dollars
    expr: {op: sum, of: [sdtw.line21, sdtw.line22, sdtw.line30, sdtw.line33, sdtw.line39]}

  - id: sdtw.h_line42_raw
    printed: "(helper)"
    label: "Subtract line 41 from line 1, before the skip instruction"
    type: Dollars
    expr: {op: subtract, from: sdtw.line1, take: sdtw.line41}

  - id: sdtw.line42
    printed: "42"
    label: "Subtract line 41 from line 1"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sdtw.h_skip41, {const: true}]}
          then: sdtw.h_zero
        - guard: {op: test, eq: [sdtw.h_skip41, {const: false}]}
          then: sdtw.h_line42_raw

  - id: sdtw.line43
    printed: "43"
    label: "Multiply line 42 by 28% (0.28)"
    type: Dollars
    expr: {op: multiply_rate, amount: sdtw.line42, rate: {param: sdtw.rate28}}

  - id: sdtw.line44
    printed: "44"
    label: "Figure the tax on the amount on line 21. If the amount on line 21 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 21 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line21, status: f1040.status}, line: tax}}

  - id: sdtw.line45
    printed: "45"
    label: "Add lines 31, 34, 40, 43, and 44"
    type: Dollars
    expr: {op: sum, of: [sdtw.line31, sdtw.line34, sdtw.line40, sdtw.line43, sdtw.line44]}

  - id: sdtw.line46
    printed: "46"
    label: "Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet"
    type: NonNegDollars
    expr: {op: copy, from: {def: tax_on_amount, bind: {amount: sdtw.line1, status: f1040.status}, line: tax}}

  - id: sdtw.line47
    printed: "47"
    label: "Tax on all taxable income (including capital gains and qualified dividends). Enter the smaller of line 45 or line 46. Also, include this amount on Form 1040, 1040-SR, or 1040-NR, line 16. (If you are filing Form 2555, don't enter this amount on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet in the Instructions for Form 1040.)"
    type: Dollars
    expr: {op: smaller_of, of: [sdtw.line45, sdtw.line46]}
    refuses: [sa.excluded_income]
```
```
