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
| match / mismatch / unclear / missing | 2 / 1 / 0 / 0 |
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
Status: **MATCH**

Model: Column (e) instructions require using the basis shown on the broker report when basis was reported to the IRS, and the correct basis when it was not; the restatement makes that choice.
Reviewed in: pass ba40592cdf31

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The restatement adds only a code B basis correction and a code W wash-sale adjustment, but IRS column (g) says 'Enter in this column any necessary adjustments to gain (or loss)' and, for multiple codes, 'enter the net adjustment in column (g),' so it omits other adjustments such as code E selling expenses or option premiums.

Ruling: scope; as the earlier ruling of this round, the same objection. same objection as the round-2 ruling (other codes, here code E). Codes other than B and W are refused at sales.one on sales.bad_code ("Only applicable B and W adjustments are supported"), and the round-3 sales.code and sales.proceeds wording sends an unreflected selling expense or option premium to code E (choose other), so on a completed return column (g) is the code B correction plus the code W adjustment. Project stands.
Reviewed in: pass ba40592cdf31

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: IRS column (h) says to subtract column (e) from column (d) and then take column (g) adjustments into account; proceeds less basis plus column (g) is that computation.
Reviewed in: pass ba40592cdf31

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (e) | dfac2e90636fbda28674e38934c7333d91b2893dd89181ebf478993377890fb4 |
| (g) | d9e0a724804d2c20e5122687a5d95e38583a7706bc5d9ecf18b8d7f2fe83d79f |
| (h) | 2478528525171d6f13225a6f4ef4eec3f9b7fa92f6869221628e8b2282792bf9 |
| (rest of the document) | 173d9d26e48e7de243e42df8a66476933ccaf441a5d2d8dd3a5d3a9677bc158c |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass ba40592cdf31

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (e), (g), (h) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ba40592cdf31435a0cc0283ea075d73793a5be0ce3a50c686ce883d2b5defc66 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 6c6416a375a750604730f18b0e13ba0731e3355152a2dd7d426151cda3d862fe |
| receipt | .transcription/sales.deepseek.render.lines-c7ffad017c60 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 2 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6 | pages named by another document's citation | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

##### Raw response

```yaml
lines:
  - key: "(e)"
    status: MATCH
    reason: "Column (e) instructions require using the basis shown on the broker report when basis was reported to the IRS, and the correct basis when it was not; the restatement makes that choice."
  - key: "(g)"
    status: MISMATCH
    reason: "The restatement adds only a code B basis correction and a code W wash-sale adjustment, but IRS column (g) says 'Enter in this column any necessary adjustments to gain (or loss)' and, for multiple codes, 'enter the net adjustment in column (g),' so it omits other adjustments such as code E selling expenses or option premiums."
  - key: "(h)"
    status: MATCH
    reason: "IRS column (h) says to subtract column (e) from column (d) and then take column (g) adjustments into account; proceeds less basis plus column (g) is that computation."
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
