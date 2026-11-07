# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f060738f207fba5a8b02602760fd1393eceab283f4c36c09f35ddf1997ab97bf |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records (cost; the donor's basis for a gift; for inherited property, value at death or on an elected alternate valuation date or special-use value, within the Schedule A (Form 8971) final estate tax value where it applies; the basis of property from a trade, from a spouse or incident to divorce, or received for services), with the adjustments to basis"]

Model: The helper "Basis reported to IRS" is true only for boxes A and D, so G and J digital-asset rows with basis reported get the correct basis in column (e). The IRS says that for a transaction reported "on Part I with box A or box G checked ... or ... on Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect." For boxes B/E/H/K and C/F/I/L, entering the correct basis matches the instructions.

Ruling: scope; same objection as the earlier rulings (boxes G and J). f8949 p. 1, box G: "Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS"; i8949 p. 8, code B. The helper is true only for boxes A and D because boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Digital asset box G–L"), and the refusal reaches every Schedule D total and Form 1040 line 7a (fixture sales.refuse.digital.G). Within boxes A to F the condition reads as the instructions do. The R3 restructuring of the sales questions changed the glossary text, not this line. Project stands on the English.
Reviewed in: pass 2198e305c991

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The sum of the code B difference (reported minus correct, matching worksheet lines 3–4) and the positive wash-sale loss matches "enter the net adjustment in column (g)." But the code B part is gated on "Basis reported to IRS", which leaves out boxes G and J, so those rows get $0 instead of the adjustment. The IRS requires: "box A or box G ... box D or box J ... Correct the error by entering an adjustment in column (g)."

Ruling: scope; same objection as the earlier rulings (boxes G and J). i8949 p. 8, code B: "Correct the error by entering an adjustment in column (g)". The code B part is gated on boxes A and D because boxes G to L are refused at the transaction: sales.one refuses when sales.digital ("Digital asset box G–L"), and the refusal reaches every Schedule D total and Form 1040 line 7a (fixture sales.refuse.digital.G); the sum of the code B correction and the code W wash-sale loss is the net adjustment the model accepts. Project stands on the English.
Reviewed in: pass 2198e305c991

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: The restatement matches the IRS instruction: "First, subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d). Then take into account any adjustments in column (g)."
Reviewed in: pass ba40592cdf31

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (e) | 35b4dd45acfb89238962c5f6cf689bca4b8ca5756c6cb69685d5cb4d95ea73f6 |
| (g) | 7b0533993727aec41a91a4c468aef48839a1294bf2597f97afa329d9530fc7db |
| (h) | 2478528525171d6f13225a6f4ef4eec3f9b7fa92f6869221628e8b2282792bf9 |
| (rest of the document) | 173d9d26e48e7de243e42df8a66476933ccaf441a5d2d8dd3a5d3a9677bc158c |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass ba40592cdf31

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines (e), (g), (h) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ba40592cdf31435a0cc0283ea075d73793a5be0ce3a50c686ce883d2b5defc66 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 6c6416a375a750604730f18b0e13ba0731e3355152a2dd7d426151cda3d862fe |
| receipt | .transcription/sales.render.lines-c7ffad017c60 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6 | pages named by another document's citation | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

##### Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The gate \"Basis reported to IRS\" is true only for box 'A' or 'D', so a digital-asset transaction in box G or J gets the correct basis in column (e). The IRS text says: \"If this transaction is reported on Part I with box A or box G checked at the top or ... on Part II with box D or box J checked at the top, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\" Within boxes A–F the restatement matches the instructions."
  - key: "(g)"
    status: MISMATCH
    reason: "Because the same A/D-only gate controls the code B correction, a box G or J transaction with an incorrect reported basis gets no basis adjustment. The IRS text says to enter the reported basis for box G or J as well and \"Correct the error by entering an adjustment in column (g)\" using the Worksheet for Basis Adjustments, where reported minus correct basis is entered as a positive or negative amount. The restatement also returns no amount for the 'other' adjustment code (for example code E), and no refusal is shown for that case; otherwise B plus W matches \"enter the net adjustment in column (g).\""
  - key: "(h)"
    status: MATCH
    reason: "The restatement matches the IRS instruction: \"First, subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d). Then take into account any adjustments in column (g).\""
```
```

#### Pass 2198e305c991

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines (e), (g) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2198e305c991508c5d7c7a3adde2635e0a08ed5e7be18280b08326f14b1c54da |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7791cfee9a5f0f7c49f3917bc48c62519adcee84acfb8e7762ca5bc2ee3b78b7 |
| receipt | .transcription/sales.render.lines-e48cb2ddc847 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6 | pages named by another document's citation | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

##### Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The helper \"Basis reported to IRS\" is true only for boxes A and D, so G and J digital-asset rows with basis reported get the correct basis in column (e). The IRS says that for a transaction reported \"on Part I with box A or box G checked ... or ... on Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect.\" For boxes B/E/H/K and C/F/I/L, entering the correct basis matches the instructions."
  - key: "(g)"
    status: MISMATCH
    reason: "The sum of the code B difference (reported minus correct, matching worksheet lines 3–4) and the positive wash-sale loss matches \"enter the net adjustment in column (g).\" But the code B part is gated on \"Basis reported to IRS\", which leaves out boxes G and J, so those rows get $0 instead of the adjustment. The IRS requires: \"box A or box G ... box D or box J ... Correct the error by entering an adjustment in column (g).\""
```
```

## Raw response

```yaml
```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The program uses the broker-reported basis only for boxes A and D. For digital-asset boxes G and J it enters the correct basis instead, but the IRS says \"If this transaction is reported on Part I with box A or box G checked ... or on Part II with box D or box J checked ... enter the basis shown on Form 1099-B or Form 1099-DA ... in column (e), even though that basis is incorrect.\""
  - key: "(g)"
    status: MISMATCH
    reason: "The code B adjustment applies only to boxes A and D, so a box G or J transaction with an incorrect basis gets no column (g) correction, although the IRS says for box A, G, D or J to \"Correct the error by entering an adjustment in column (g).\" Also, choosing \"other\" for an additional code gives $0 with no refusal, although the IRS requires the adjustment for codes such as E, H, L and Q (for example \"enter the amount of the nondeductible loss as a positive number in column (g)\")."
  - key: "(h)"
    status: MATCH
    reason: "The program takes column (d) minus column (e), plus column (g). This matches the IRS: \"subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d). Then take into account any adjustments in column (g).\""
```
```
