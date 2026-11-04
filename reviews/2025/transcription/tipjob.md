# Transcription agreement — tipjob

Second transcription of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/tipjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8ec4413d6c8b93df5480033150128189a2d89b533295b5c8c1491beaaf7039c |
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
| subject sha256 | 2a7723b9953e4329f2d8ffa0fd83943ff543a87316e13e7101d7b84b8aa7ea1d |
| printed lines compared | 3 |
| agree / disagree / missing | 3 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tipjob.one — One employer
Status: **AGREE**

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **AGREE**

### 1(d) — Enter the greater of column (b) or column (c)
Status: **AGREE**
Reviewed in: pass 803749002b5c

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| tipjob.one | 89714a0cb67ca33c33d5d021e3ea7c093359afc1825e22eef5e9e6c2a3f8101b |
| 1(c) | 77fbe1f702739598adba88692198eea2d36a6235f56316db3ccdd3b150d8936c |
| 1(d) | eca25e28e7ef2dc31b1fb06bfc57a9d03b2bfd63cfaecfcbf7800a8ef79efa13 |
| (rest of the document) | 20acc5f91a6d8939245104a61352ad2f9665689d8cbe4cf8240cfecb7fd1c18f |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| 1(d) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 803749002b5c

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1(d) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 803749002b5c0f075f53c97e0531406e16383001d09aaaf342a379899ea08f9d |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ec9b07fe053c2c27db685bf3b84338a8c6423d39ad3e48c874370d3620d11349 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 447f9ddefdb690f273cfc01016a6c7cfbd5d03893b076a5532d46a4fa2e5edd8 |
| receipt | .transcription/tipjob.lines-655771a99dda |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | dependent, f1040, f8995a, qbi, sa, scope, scveh |
| shared page | household, person, s1, s1a, sc |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: tipjob.col_d
    printed: "1(d)"
    label: "Enter the greater of column (b) or column (c)"
    type: NonNegDollars
    expr:
      op: larger_of
      of: [tipjob.amount, tipjob.col_c]
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: tipjob.one
    printed: "(helper)"
    label: "One (this employer counts as one row of the Qualified Tips From More Than One Employer Worksheet, lines 1A through 1E)"
    type: Count
    expr: {op: param, ref: person.one}
    note: "The IRS pages do not define this interface. The reading chosen is a per-row count of 1, so other forms can count the employers listed on the worksheet. That count tells line 4a (more than one employer: enter -0-) apart from line 4c. The value comes from the year parameter person.one (Count 1), because no tipjob-specific parameter exists."
  - id: tipjob.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: tipjob.col_c
    printed: "1(c)"
    label: "Qualified tips reported on Form 4137, column 1(c), for this employer"
    type: NonNegDollars
    expr: {op: copy, from: tipjob.h_zero}
    note: "The closed input interface gives no input for Form 4137, column 1(c). Form 4137 (tips not reported to the employer) is outside the tool's scope, as the f8959.unsupported and s2.other screening questions show. The tool therefore computes only the case with no Form 4137 amount, so column (c) is zero. A filer with Form 4137 tips is stopped by those screening inputs."
  - id: tipjob.h_greater
    printed: "(helper)"
    label: "The greater of column (b) or column (c)"
    type: NonNegDollars
    expr: {op: larger_of, of: [tipjob.amount, tipjob.col_c]}
  - id: tipjob.col_d
    printed: "1(d)"
    label: "Enter the greater of column (b) or column (c)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [tipjob.qualified, {const: true}]}
          then: tipjob.h_greater
        - guard: {op: test, eq: [tipjob.qualified, {const: false}]}
          then: tipjob.h_zero
    note: "The IRS text says 'Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c.' It also requires tips to be cash, voluntary, not negotiated, customer-determined, and not for an unlawful service. When the filer answers that this employer's tips do not meet all of these conditions, this row is entered as zero. The text leaves partly qualifying amounts open. The reading chosen relies on column (b) being entered as qualified tips only, and treats a 'no' answer as no qualified tips from this employer."
```
```
