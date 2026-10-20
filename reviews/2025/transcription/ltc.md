# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d37a9ecba7a2ba3a2d394c831302ca7bfe8be4102a07492c53f109cb02c9ed81 |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### ltc.amount — The smaller of (a) or (b)
Status: **AGREE**

### 2(b) — The amount for that person's age
Status: **DISAGREE**

Project:

```json
{"keys": [{"input": "ltc.age"}], "op": "keyed_lookup", "table": "ltc_limit"}
```

Second:

```json
{"keys": [{"input": "ltc.age"}], "op": "keyed_lookup", "table": "ltc.age_limit"}
```

Second transcription's note: Open point: the year-parameter list has no parameters for the five age amounts. Choice: look them up in a pinned printed table, ltc.age_limit, keyed by Enum(ltc_age). Its rows, in cents, are: to40 -> 48000; to50 -> 90000; to60 -> 180000; to70 -> 481000; over70 -> 602000. These match the printed amounts on Form 7206 line 2(b) and in the i7206 list.

Ruling: representation; project retained. The same lookup of the age-band amount by ltc.age; the second names its own table (ltc.age_limit) and lists its rows ($480, $900, $1,800, $4,810, $6,020), which are the project's ltc_limit rows (f7206 line 2(b); i7206 pp. 1–2).

## Raw second transcription

```yaml
```yaml
lines:
  - id: ltc.line2(b)
    printed: "2(b)"
    label: "The amount shown below. Use the person's age at the end of the tax year. $480— if that person is age 40 or younger; $900— if age 41 to 50; $1,800— if age 51 to 60; $4,810— if age 61 to 70; $6,020— if age 71 or older"
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: ltc.age_limit
      keys: [ltc.age]
    cite: "Form 7206 (2025), line 2(b); Instructions for Form 7206 (2025), Qualified long-term care insurance, item 2"
    note: "Open point: the year-parameter list has no parameters for the five age amounts. Choice: look them up in a pinned printed table, ltc.age_limit, keyed by Enum(ltc_age). Its rows, in cents, are: to40 -> 48000; to50 -> 90000; to60 -> 180000; to70 -> 481000; over70 -> 602000. These match the printed amounts on Form 7206 line 2(b) and in the i7206 list."
  - id: ltc.amount
    printed: "(helper)"
    label: "For coverage under a qualified long-term care insurance contract, enter for each person covered the smaller of (a) or (b)."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [ltc.payments, ltc.line2(b)]
    cite: "Form 7206 (2025), line 2; Instructions for Form 7206 (2025), Qualified long-term care insurance"
    note: "Open point: the i7206 says that when a person's long-term care premiums are spread over plans under more than one business, the total entered on line 2 of all Forms 7206 for that person can't be more than the line 2 limit. This line only applies the limit within one Form 7206, so it does not combine entries across businesses. Choice: per-entry smaller of (a) or (b), as line 2 prints it. Line 2 itself (the total over persons) is the sum over this collection on the Schedule C entry (sc.f7206_line2)."
```
```
