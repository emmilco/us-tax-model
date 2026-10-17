# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 8082730ab16fd59795665c1288b5462d6b1d6ee37bc0b50c11bc99fa5dabb904 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 13 / 32 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | f265dc3989a82f04fbea0f04cf8495b9b5ff8f18335d395176aa06773cc8072f |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 12 | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a covers short-term transactions 'reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments'. The filter keeps only class 'A' and so drops basis-reported digital-asset (Form 1099-DA) transactions classed in G–L, and no refusal excludes them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(e) — Line 1a, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a includes transactions 'reported on Form 1099-B or Form 1099-DA', but filtering on class 'A' alone omits digital-asset transactions classed G–L, and no refusal covers them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(g) — Line 1a, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: The class 'A' filter omits the Form 1099-DA digital-asset transactions that line 1a includes ('reported on Form 1099-B or Form 1099-DA'), and no refusal excludes them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(h) — Line 1a, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: The class 'A' filter omits the Form 1099-DA digital-asset transactions that line 1a includes ('reported on Form 1099-B or Form 1099-DA'), and no refusal excludes them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(d) — Line 1b, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 1b is 'Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked'. The restatement sums only class 'A', omitting Box G, and no refusal excludes it.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(e) — Line 1b, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(g) — Line 1b, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(h) — Line 1b, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(d) — Line 2, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 2 is 'Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked'. The restatement includes class 'B' only, omitting Box H.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(e) — Line 2, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(g) — Line 2, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(h) — Line 2, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(d) — Line 3, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 3 is 'Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked'. The restatement includes class 'C' only, omitting Box I.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(e) — Line 3, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(g) — Line 3, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(h) — Line 3, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(d) — Line 8a, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a covers long-term transactions 'reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS'. The filter keeps only class 'D' and so omits digital-asset transactions classed G–L, and no refusal covers them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(e) — Line 8a, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(g) — Line 8a, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(h) — Line 8a, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(d) — Line 8b, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 8b is 'Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked'. The restatement includes class 'D' only, omitting Box J.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(e) — Line 8b, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(g) — Line 8b, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(h) — Line 8b, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(d) — Line 9, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 9 is 'Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked'. The restatement includes class 'E' only, omitting Box K.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(e) — Line 9, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(g) — Line 9, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(h) — Line 9, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(d) — Line 10, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 10 is 'Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked'. The restatement includes class 'F' only, omitting Box L.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(e) — Line 10, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(g) — Line 10, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(h) — Line 10, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 takes amounts from Forms 6252, 4684, 6781 and 8824. The other-forms refusal excludes all of these, so $0 is correct within the supported cases.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 takes amounts from Schedule(s) K-1. The other-forms refusal names Schedule K-1, so $0 is correct within scope.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 6 is the short-term capital loss carryover. The carryover refusal excludes that case, so $0 is correct within scope.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 takes amounts from Forms 4797, 2439, 6252, 4684, 6781 and 8824. The other-forms refusal names all of them, so $0 is correct within scope.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 takes amounts from Schedule(s) K-1. The other-forms refusal excludes K-1 amounts, so $0 is correct within scope.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 14 is the long-term capital loss carryover. The carryover refusal excludes that case, so $0 is correct within scope.

### 13 — Capital gain distributions
Status: **UNCLEAR**

Restated: Add helper "Capital gain distributions, generally Form 1099-DIV box 2a" and div helper "Zero only after distribution scope checks".

Model: Line 13 says only 'Capital gain distributions. See the instructions', and the line 13 instruction points to 'Capital Gain Distributions, earlier', which is not in the pages given. Whether Form 1099-DIV box 2a alone, with no other sources, is the full amount cannot be confirmed.

Ruling: representation; project retained. 'Enter on Schedule D, line 13, the total capital gain distributions paid to you during the year' (i1040sd, Capital Gain Distributions), which Form 1099-DIV reports in box 2a; distributions from other sources (Form 2439, Schedule K-1) are refused through `sd.other_forms`. No change to the data.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: This matches 'Combine lines 1a through 6 in column (h)'.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: This matches 'Combine lines 8a through 14 in column (h)'.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: This matches 'Combine lines 7 and 15 and enter the result'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: This matches 'Are lines 15 and 16 both gains?' as both greater than $0.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?', using the 28% worksheet line 7 result, the section 1250 worksheet line 18 result and the Form 4952 filing test.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: The IRS text asks for 'the smaller of' the line 16 loss or ($3,000)/($1,500 MFS), comparing them 'as positive numbers'. That equals the larger of the two signed values, and the line is applied only when line 16 is a loss.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: This matches 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?'.

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MISMATCH
    reason: "Line 1a covers short-term transactions 'reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments'. The filter keeps only class 'A' and so drops basis-reported digital-asset (Form 1099-DA) transactions classed in G–L, and no refusal excludes them."
  - key: "1a(e)"
    status: MISMATCH
    reason: "Line 1a includes transactions 'reported on Form 1099-B or Form 1099-DA', but filtering on class 'A' alone omits digital-asset transactions classed G–L, and no refusal covers them."
  - key: "1a(g)"
    status: MISMATCH
    reason: "The class 'A' filter omits the Form 1099-DA digital-asset transactions that line 1a includes ('reported on Form 1099-B or Form 1099-DA'), and no refusal excludes them."
  - key: "1a(h)"
    status: MISMATCH
    reason: "The class 'A' filter omits the Form 1099-DA digital-asset transactions that line 1a includes ('reported on Form 1099-B or Form 1099-DA'), and no refusal excludes them."
  - key: "1b(d)"
    status: MISMATCH
    reason: "IRS line 1b is 'Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked'. The restatement sums only class 'A', omitting Box G, and no refusal excludes it."
  - key: "1b(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only."
  - key: "1b(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only."
  - key: "1b(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box A or Box G checked', but the restatement filters on class 'A' only."
  - key: "2(d)"
    status: MISMATCH
    reason: "IRS line 2 is 'Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked'. The restatement includes class 'B' only, omitting Box H."
  - key: "2(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only."
  - key: "2(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only."
  - key: "2(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box B or Box H checked', but the restatement filters on class 'B' only."
  - key: "3(d)"
    status: MISMATCH
    reason: "IRS line 3 is 'Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked'. The restatement includes class 'C' only, omitting Box I."
  - key: "3(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only."
  - key: "3(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only."
  - key: "3(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box C or Box I checked', but the restatement filters on class 'C' only."
  - key: "8a(d)"
    status: MISMATCH
    reason: "Line 8a covers long-term transactions 'reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS'. The filter keeps only class 'D' and so omits digital-asset transactions classed G–L, and no refusal covers them."
  - key: "8a(e)"
    status: MISMATCH
    reason: "Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets."
  - key: "8a(g)"
    status: MISMATCH
    reason: "Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets."
  - key: "8a(h)"
    status: MISMATCH
    reason: "Line 8a includes Form 1099-DA transactions ('reported on Form 1099-B or Form 1099-DA'), but the class 'D' filter omits digital assets."
  - key: "8b(d)"
    status: MISMATCH
    reason: "IRS line 8b is 'Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked'. The restatement includes class 'D' only, omitting Box J."
  - key: "8b(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only."
  - key: "8b(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only."
  - key: "8b(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box D or Box J checked', but the restatement filters on class 'D' only."
  - key: "9(d)"
    status: MISMATCH
    reason: "IRS line 9 is 'Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked'. The restatement includes class 'E' only, omitting Box K."
  - key: "9(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only."
  - key: "9(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only."
  - key: "9(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box E or Box K checked', but the restatement filters on class 'E' only."
  - key: "10(d)"
    status: MISMATCH
    reason: "IRS line 10 is 'Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked'. The restatement includes class 'F' only, omitting Box L."
  - key: "10(e)"
    status: MISMATCH
    reason: "IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only."
  - key: "10(g)"
    status: MISMATCH
    reason: "IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only."
  - key: "10(h)"
    status: MISMATCH
    reason: "IRS text says 'with Box F or Box L checked', but the restatement filters on class 'F' only."
  - key: "4"
    status: MATCH
    reason: "Line 4 takes amounts from Forms 6252, 4684, 6781 and 8824. The other-forms refusal excludes all of these, so $0 is correct within the supported cases."
  - key: "5"
    status: MATCH
    reason: "Line 5 takes amounts from Schedule(s) K-1. The other-forms refusal names Schedule K-1, so $0 is correct within scope."
  - key: "6"
    status: MATCH
    reason: "Line 6 is the short-term capital loss carryover. The carryover refusal excludes that case, so $0 is correct within scope."
  - key: "11"
    status: MATCH
    reason: "Line 11 takes amounts from Forms 4797, 2439, 6252, 4684, 6781 and 8824. The other-forms refusal names all of them, so $0 is correct within scope."
  - key: "12"
    status: MATCH
    reason: "Line 12 takes amounts from Schedule(s) K-1. The other-forms refusal excludes K-1 amounts, so $0 is correct within scope."
  - key: "14"
    status: MATCH
    reason: "Line 14 is the long-term capital loss carryover. The carryover refusal excludes that case, so $0 is correct within scope."
  - key: "13"
    status: UNCLEAR
    reason: "Line 13 says only 'Capital gain distributions. See the instructions', and the line 13 instruction points to 'Capital Gain Distributions, earlier', which is not in the pages given. Whether Form 1099-DIV box 2a alone, with no other sources, is the full amount cannot be confirmed."
  - key: "7"
    status: MATCH
    reason: "This matches 'Combine lines 1a through 6 in column (h)'."
  - key: "15"
    status: MATCH
    reason: "This matches 'Combine lines 8a through 14 in column (h)'."
  - key: "16"
    status: MATCH
    reason: "This matches 'Combine lines 7 and 15 and enter the result'."
  - key: "17"
    status: MATCH
    reason: "This matches 'Are lines 15 and 16 both gains?' as both greater than $0."
  - key: "20"
    status: MATCH
    reason: "This matches 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?', using the 28% worksheet line 7 result, the section 1250 worksheet line 18 result and the Form 4952 filing test."
  - key: "21"
    status: MATCH
    reason: "The IRS text asks for 'the smaller of' the line 16 loss or ($3,000)/($1,500 MFS), comparing them 'as positive numbers'. That equals the larger of the two signed values, and the line is applied only when line 16 is a loss."
  - key: "22"
    status: MATCH
    reason: "This matches 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?'."
```
```
