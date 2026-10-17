# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c2a1e43c0e63ab2758a092460cdcb5cff4d7f34f3fc44383a7b145fcd727f970 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 14 / 32 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a covers short-term transactions "reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments." The sum takes only classification 'A', so aggregate digital-asset entries (class G) are left out, and no refusal excludes digital assets.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(e) — Line 1a, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a includes transactions "reported on Form 1099-B or Form 1099-DA," but the sum takes only classification 'A'. Aggregate digital-asset entries (G) are omitted, and no refusal excludes them.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(g) — Line 1a, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a includes "Form 1099-B or Form 1099-DA" transactions, but only classification 'A' is summed. Digital-asset class G is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1a(h) — Line 1a, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 1a includes "Form 1099-B or Form 1099-DA" transactions, but only classification 'A' is summed. Digital-asset class G is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(d) — Line 1b, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line is "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked." The restatement sums only classification 'A' and omits Box G, with no refusal for digital assets.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(e) — Line 1b, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box A or Box G checked." Only classification 'A' is summed, so Box G is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(g) — Line 1b, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box A or Box G checked." Only classification 'A' is summed, so Box G is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 1b(h) — Line 1b, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box A or Box G checked." Only classification 'A' is summed, so Box G is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(d) — Line 2, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box B or Box H checked." Only classification 'B' is summed, so Box H is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(e) — Line 2, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box B or Box H checked." Only classification 'B' is summed, so Box H is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(g) — Line 2, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box B or Box H checked." Only classification 'B' is summed, so Box H is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 2(h) — Line 2, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box B or Box H checked." Only classification 'B' is summed, so Box H is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(d) — Line 3, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box C or Box I checked." Only classification 'C' is summed, so Box I is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(e) — Line 3, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box C or Box I checked." Only classification 'C' is summed, so Box I is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(g) — Line 3, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box C or Box I checked." Only classification 'C' is summed, so Box I is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 3(h) — Line 3, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box C or Box I checked." Only classification 'C' is summed, so Box I is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(d) — Line 8a, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a covers long-term transactions "reported on Form 1099-B or Form 1099-DA for which basis was reported." Only classification 'D' is summed, so aggregate digital-asset entries (J) are omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(e) — Line 8a, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes "Form 1099-B or Form 1099-DA" transactions, but only classification 'D' is summed. Digital-asset class J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(g) — Line 8a, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes "Form 1099-B or Form 1099-DA" transactions, but only classification 'D' is summed. Digital-asset class J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8a(h) — Line 8a, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 8a includes "Form 1099-B or Form 1099-DA" transactions, but only classification 'D' is summed. Digital-asset class J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(d) — Line 8b, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box D or Box J checked." Only classification 'D' is summed, so Box J is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(e) — Line 8b, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box D or Box J checked." Only classification 'D' is summed, so Box J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(g) — Line 8b, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box D or Box J checked." Only classification 'D' is summed, so Box J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 8b(h) — Line 8b, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box D or Box J checked." Only classification 'D' is summed, so Box J is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(d) — Line 9, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box E or Box K checked." Only classification 'E' is summed, so Box K is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(e) — Line 9, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box E or Box K checked." Only classification 'E' is summed, so Box K is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(g) — Line 9, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box E or Box K checked." Only classification 'E' is summed, so Box K is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 9(h) — Line 9, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box E or Box K checked." Only classification 'E' is summed, so Box K is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(d) — Line 10, column (d) totals
Status: **MISMATCH**

Restated: Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box F or Box L checked." Only classification 'F' is summed, so Box L is omitted without a refusal.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(e) — Line 10, column (e) totals
Status: **MISMATCH**

Restated: Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box F or Box L checked." Only classification 'F' is summed, so Box L is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(g) — Line 10, column (g) totals
Status: **MISMATCH**

Restated: Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box F or Box L checked." Only classification 'F' is summed, so Box L is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 10(h) — Line 10, column (h) totals
Status: **MISMATCH**

Restated: Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS line covers "Box F or Box L checked." Only classification 'F' is summed, so Box L is omitted.

Ruling: scope; project retained. Boxes G–L (digital assets reported on Form 1099-DA; f8949 p. 1: "(G) Short-term transactions reported on Form(s) 1099-DA showing basis was reported to the IRS") are refused at the transaction: `sales.one` refuses when `sales.digital` is true, the refusal propagates through `sd.count` to `sd.screen`, and every Schedule D total refuses on `sd.screen` before any box filter runs. Within the supported boxes A–F the filter reads as the line does. The filters must widen to boxes G–L when digital assets come into scope (recorded in the transcription rulings). No change to the data.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. The other-forms refusal excludes those forms, so $0 is correct in the supported cases.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 reports Schedule K-1 short-term gain or loss. The other-forms refusal covers Schedule K-1, so $0 is correct otherwise.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 6 is the short-term capital loss carryover. The carryover refusal excludes prior-year carryovers, so $0 is correct otherwise.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. All are excluded by the other-forms refusal, so $0 is correct otherwise.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 reports Schedule K-1 long-term gain or loss. It is excluded by the other-forms refusal, so $0 is correct otherwise.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 14 is the long-term capital loss carryover. It is excluded by the carryover refusal, so $0 is correct otherwise.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 is "Capital gain distributions." The restatement enters Form 1099-DIV box 2a, with refusals covering the special distribution components.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: This matches "Combine lines 1a through 6 in column (h)."

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: This matches "Combine lines 8a through 14 in column (h)."

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: This matches "Combine lines 7 and 15."

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: This matches "Are lines 15 and 16 both gains?"

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: This matches "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?" Lines 18 and 19 are taken from worksheet line 7 and worksheet line 18, as the form directs.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: The IRS text says to enter "the smaller of" the loss or ($3,000)/($1,500 MFS), treating both as positive. Taking the larger of the two signed negative amounts gives the same result, and the line is $0 when there is no loss.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: This matches "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MISMATCH
    reason: "Line 1a covers short-term transactions \"reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments.\" The sum takes only classification 'A', so aggregate digital-asset entries (class G) are left out, and no refusal excludes digital assets."
  - key: "1a(e)"
    status: MISMATCH
    reason: "Line 1a includes transactions \"reported on Form 1099-B or Form 1099-DA,\" but the sum takes only classification 'A'. Aggregate digital-asset entries (G) are omitted, and no refusal excludes them."
  - key: "1a(g)"
    status: MISMATCH
    reason: "Line 1a includes \"Form 1099-B or Form 1099-DA\" transactions, but only classification 'A' is summed. Digital-asset class G is omitted without a refusal."
  - key: "1a(h)"
    status: MISMATCH
    reason: "Line 1a includes \"Form 1099-B or Form 1099-DA\" transactions, but only classification 'A' is summed. Digital-asset class G is omitted without a refusal."
  - key: "1b(d)"
    status: MISMATCH
    reason: "The IRS line is \"Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked.\" The restatement sums only classification 'A' and omits Box G, with no refusal for digital assets."
  - key: "1b(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box A or Box G checked.\" Only classification 'A' is summed, so Box G is omitted."
  - key: "1b(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box A or Box G checked.\" Only classification 'A' is summed, so Box G is omitted."
  - key: "1b(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box A or Box G checked.\" Only classification 'A' is summed, so Box G is omitted."
  - key: "2(d)"
    status: MISMATCH
    reason: "The IRS line covers \"Box B or Box H checked.\" Only classification 'B' is summed, so Box H is omitted without a refusal."
  - key: "2(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box B or Box H checked.\" Only classification 'B' is summed, so Box H is omitted."
  - key: "2(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box B or Box H checked.\" Only classification 'B' is summed, so Box H is omitted."
  - key: "2(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box B or Box H checked.\" Only classification 'B' is summed, so Box H is omitted."
  - key: "3(d)"
    status: MISMATCH
    reason: "The IRS line covers \"Box C or Box I checked.\" Only classification 'C' is summed, so Box I is omitted without a refusal."
  - key: "3(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box C or Box I checked.\" Only classification 'C' is summed, so Box I is omitted."
  - key: "3(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box C or Box I checked.\" Only classification 'C' is summed, so Box I is omitted."
  - key: "3(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box C or Box I checked.\" Only classification 'C' is summed, so Box I is omitted."
  - key: "8a(d)"
    status: MISMATCH
    reason: "Line 8a covers long-term transactions \"reported on Form 1099-B or Form 1099-DA for which basis was reported.\" Only classification 'D' is summed, so aggregate digital-asset entries (J) are omitted without a refusal."
  - key: "8a(e)"
    status: MISMATCH
    reason: "Line 8a includes \"Form 1099-B or Form 1099-DA\" transactions, but only classification 'D' is summed. Digital-asset class J is omitted."
  - key: "8a(g)"
    status: MISMATCH
    reason: "Line 8a includes \"Form 1099-B or Form 1099-DA\" transactions, but only classification 'D' is summed. Digital-asset class J is omitted."
  - key: "8a(h)"
    status: MISMATCH
    reason: "Line 8a includes \"Form 1099-B or Form 1099-DA\" transactions, but only classification 'D' is summed. Digital-asset class J is omitted."
  - key: "8b(d)"
    status: MISMATCH
    reason: "The IRS line covers \"Box D or Box J checked.\" Only classification 'D' is summed, so Box J is omitted without a refusal."
  - key: "8b(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box D or Box J checked.\" Only classification 'D' is summed, so Box J is omitted."
  - key: "8b(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box D or Box J checked.\" Only classification 'D' is summed, so Box J is omitted."
  - key: "8b(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box D or Box J checked.\" Only classification 'D' is summed, so Box J is omitted."
  - key: "9(d)"
    status: MISMATCH
    reason: "The IRS line covers \"Box E or Box K checked.\" Only classification 'E' is summed, so Box K is omitted without a refusal."
  - key: "9(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box E or Box K checked.\" Only classification 'E' is summed, so Box K is omitted."
  - key: "9(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box E or Box K checked.\" Only classification 'E' is summed, so Box K is omitted."
  - key: "9(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box E or Box K checked.\" Only classification 'E' is summed, so Box K is omitted."
  - key: "10(d)"
    status: MISMATCH
    reason: "The IRS line covers \"Box F or Box L checked.\" Only classification 'F' is summed, so Box L is omitted without a refusal."
  - key: "10(e)"
    status: MISMATCH
    reason: "The IRS line covers \"Box F or Box L checked.\" Only classification 'F' is summed, so Box L is omitted."
  - key: "10(g)"
    status: MISMATCH
    reason: "The IRS line covers \"Box F or Box L checked.\" Only classification 'F' is summed, so Box L is omitted."
  - key: "10(h)"
    status: MISMATCH
    reason: "The IRS line covers \"Box F or Box L checked.\" Only classification 'F' is summed, so Box L is omitted."
  - key: "4"
    status: MATCH
    reason: "Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. The other-forms refusal excludes those forms, so $0 is correct in the supported cases."
  - key: "5"
    status: MATCH
    reason: "Line 5 reports Schedule K-1 short-term gain or loss. The other-forms refusal covers Schedule K-1, so $0 is correct otherwise."
  - key: "6"
    status: MATCH
    reason: "Line 6 is the short-term capital loss carryover. The carryover refusal excludes prior-year carryovers, so $0 is correct otherwise."
  - key: "11"
    status: MATCH
    reason: "Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. All are excluded by the other-forms refusal, so $0 is correct otherwise."
  - key: "12"
    status: MATCH
    reason: "Line 12 reports Schedule K-1 long-term gain or loss. It is excluded by the other-forms refusal, so $0 is correct otherwise."
  - key: "14"
    status: MATCH
    reason: "Line 14 is the long-term capital loss carryover. It is excluded by the carryover refusal, so $0 is correct otherwise."
  - key: "13"
    status: MATCH
    reason: "Line 13 is \"Capital gain distributions.\" The restatement enters Form 1099-DIV box 2a, with refusals covering the special distribution components."
  - key: "7"
    status: MATCH
    reason: "This matches \"Combine lines 1a through 6 in column (h).\""
  - key: "15"
    status: MATCH
    reason: "This matches \"Combine lines 8a through 14 in column (h).\""
  - key: "16"
    status: MATCH
    reason: "This matches \"Combine lines 7 and 15.\""
  - key: "17"
    status: MATCH
    reason: "This matches \"Are lines 15 and 16 both gains?\""
  - key: "20"
    status: MATCH
    reason: "This matches \"Are lines 18 and 19 both zero or blank and you are not filing Form 4952?\" Lines 18 and 19 are taken from worksheet line 7 and worksheet line 18, as the form directs."
  - key: "21"
    status: MATCH
    reason: "The IRS text says to enter \"the smaller of\" the loss or ($3,000)/($1,500 MFS), treating both as positive. Taking the larger of the two signed negative amounts gives the same result, and the line is $0 when there is no loss."
  - key: "22"
    status: MATCH
    reason: "This matches \"Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?\""
```
```
