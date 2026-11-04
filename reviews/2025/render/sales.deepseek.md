# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f060738f207fba5a8b02602760fd1393eceab283f4c36c09f35ddf1997ab97bf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 0b9ec9f65641ab9ee08de46c173cbf25107f1f889dcf640bfe9e63ae434562ff |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records (for inherited property shown on a Schedule A (Form 8971) as increasing the estate tax, starting from no more than its final estate tax value)"]

Model: The IRS says "Box A or Box G" and "Box D or Box J" cover transactions with an amount shown for cost or other basis reported to the IRS; the program's "Basis reported to IRS" helper is only boxes A or D, so for boxes G/J it would enter the correct adjusted basis instead of the reported basis.

Ruling: scope; same as the refresh-round ruling: boxes G to L are refused at the transaction by sales.digital at sales.one, so the correct-basis branch is never used for them. Project stands.
Reviewed in: pass 0845778b81ca

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The IRS says "Enter in this column any necessary adjustments to gain (or loss)" and, for multiple codes, "enter the net adjustment in column (g)"; the restatement only adds code B and code W adjustments, omitting other necessary adjustments such as codes E, H, or L.

Ruling: scope; the model names other codes (E, H, L); codes other than B and W are refused at sales.one on sales.bad_code ("Only applicable B and W adjustments are supported"), and boxes G and J with every digital-asset box, so on a completed return column (g) is the code B correction plus the code W adjustment. Project stands.
Reviewed in: pass 0845778b81ca

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: The form and Schedule D instructions say to subtract column (e) from column (d) and combine the result with column (g); the restatement does that by adding 'Proceeds less column (e)' and column (g).

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (e) | a3b4334e08d3611cf8f8349137afa279c9654770eafa9c32228c7a574b9926d6 |
| (g) | cf6116d2fb9f040bc5769c5ed47067fcbd8c86a495774d4cec8ce77de6ba6224 |
| (h) | d2faff0dc9a5bf174d1054ce0c9e3f82d26b6e89cc5d7782def754bd47f4f988 |
| (rest of the document) | 173d9d26e48e7de243e42df8a66476933ccaf441a5d2d8dd3a5d3a9677bc158c |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 0845778b81ca

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (e), (g) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 0845778b81ca5ea27c0a41d92c9831f1ab3ddbedd1af8c2ecbfb4839fbbaac15 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 58233cc66194913d2c2c2f683c230a91c126ebcbdb27c02ada234bda0f73f108 |
| receipt | .transcription/sales.deepseek.render.lines-e48cb2ddc847 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Raw response

```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The IRS says \"Box A or Box G\" and \"Box D or Box J\" cover transactions with an amount shown for cost or other basis reported to the IRS; the program's \"Basis reported to IRS\" helper is only boxes A or D, so for boxes G/J it would enter the correct adjusted basis instead of the reported basis."
  - key: "(g)"
    status: MISMATCH
    reason: "The IRS says \"Enter in this column any necessary adjustments to gain (or loss)\" and, for multiple codes, \"enter the net adjustment in column (g)\"; the restatement only adds code B and code W adjustments, omitting other necessary adjustments such as codes E, H, or L."
```

## Raw response

```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The helper treats only boxes A and D as basis-reported, but the form note says for box A or box G with incorrect reported basis, enter the basis as reported in column (e), and the instructions likewise say box D or box J; G/J would wrongly use the correct-basis branch."
  - key: "(g)"
    status: MISMATCH
    reason: "Because the basis-reported gate omits box G and box J, no code B adjustment is made for those reported-basis transactions; the IRS code B instruction says for box A or box G (and box D or box J) enter the reported basis in column (e) and 'Correct the error by entering an adjustment in column (g).'"
  - key: "(h)"
    status: MATCH
    reason: "The form and Schedule D instructions say to subtract column (e) from column (d) and combine the result with column (g); the restatement does that by adding 'Proceeds less column (e)' and column (g)."
```
