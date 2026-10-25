# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7809735ae620520e6c7c4fa787d6504e4855451331bbb665da02a2a436a2708d |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 230f7f25833346d7ea24794a35a3697e5a891a4537c9f5860d68aed1fdde6487 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: IRS line 1a totals short-term transactions with basis reported and no adjustments; the restatement sums column (d) proceeds over classification A aggregate entries, with unsupported transactions excluded by the stated screening refusal.

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: IRS line 1a column (e) is cost or other basis; the restatement sums sales.e, which for covered A entries is the basis shown on the broker report, over the same A aggregate population.

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: IRS line 1a column (g) is adjustments; for aggregate-eligible A entries the program's sales.g is zero, so the sum matches the no-adjustments line.

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h, which is proceeds less basis plus adjustments.

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: IRS line 1b totals Form 8949 Box A or G transactions; the restatement sums column (d) over classification A detail entries, with digital Box G excluded by the stated screening refusal.

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: IRS line 1b column (e) is cost or other basis; the restatement sums sales.e (reported basis for covered A entries) over the A detail population.

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: IRS line 1b column (g) is the Form 8949 Part I adjustment total; the restatement sums sales.g, which combines the basis-correction and wash-sale adjustments.

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h, which is proceeds less basis plus adjustments.

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: IRS line 2 totals Form 8949 Box B or H transactions; the restatement sums column (d) proceeds over classification B detail entries, with digital Box H excluded by the stated screening refusal.

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: IRS line 2 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered B entries is the correct adjusted basis.

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: IRS line 2 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments.

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the B detail entries.

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: IRS line 3 totals Form 8949 Box C or I transactions; the restatement sums column (d) proceeds over classification C detail entries, with digital Box I excluded by the stated screening refusal.

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: IRS line 3 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered C entries is the correct adjusted basis.

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: IRS line 3 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments.

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the C detail entries.

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: IRS line 8a totals long-term transactions with basis reported and no adjustments; the restatement sums column (d) proceeds over classification D aggregate entries, with unsupported transactions excluded by the stated screening refusal.

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: IRS line 8a column (e) is cost or other basis; the restatement sums sales.e, which for covered D entries is the basis shown on the broker report.

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: IRS line 8a column (g) is adjustments; for aggregate-eligible D entries the program's sales.g is zero, so the sum matches the no-adjustments line.

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the D aggregate entries.

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: IRS line 8b totals Form 8949 Box D or J transactions; the restatement sums column (d) proceeds over classification D detail entries, with digital Box J excluded by the stated screening refusal.

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: IRS line 8b column (e) is cost or other basis; the restatement sums sales.e (reported basis for covered D entries) over the D detail population.

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: IRS line 8b column (g) is the Form 8949 Part II adjustment total; the restatement sums sales.g, which combines the basis-correction and wash-sale adjustments.

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the D detail entries.

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: IRS line 9 totals Form 8949 Box E or K transactions; the restatement sums column (d) proceeds over classification E detail entries, with digital Box K excluded by the stated screening refusal.

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: IRS line 9 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered E entries is the correct adjusted basis.

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: IRS line 9 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments.

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the E detail entries.

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: IRS line 10 totals Form 8949 Box F or L transactions; the restatement sums column (d) proceeds over classification F detail entries, with digital Box L excluded by the stated screening refusal.

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: IRS line 10 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered F entries is the correct adjusted basis.

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: IRS line 10 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments.

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the F detail entries.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 4 is for short-term gains from Forms 6252, 4684, 6781, and 8824; the program enters $0 when those source forms are absent and refuses when they exist, naming the excluded source forms.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 5 is for Schedule K-1 short-term gains from partnerships, S corporations, estates, and trusts; the program enters $0 when no such K-1 items exist and refuses via the named additional-source-forms gate.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 6 is the short-term capital loss carryover from the Capital Loss Carryover Worksheet; the program enters $0 when there is no carryover and refuses when there is, naming the carryover worksheet.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 11 is for gains from Forms 4797, 2439, 6252, 4684, 6781, and 8824; the program enters $0 when those forms are absent and refuses when they exist, naming the excluded source forms.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 12 is for Schedule K-1 long-term gains from partnerships, S corporations, estates, and trusts; the program enters $0 when absent and refuses via the named additional-source-forms gate.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: IRS line 14 is the long-term capital loss carryover from the Capital Loss Carryover Worksheet; the program enters $0 when there is no carryover and refuses when there is, naming the carryover worksheet.

### 13 — Capital gain distributions
Status: **MATCH**

Model: IRS line 13 is capital gain distributions; the restatement adds the distribution input and a zero scope-check helper whose refusals name the unsupported distribution treatments.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: IRS line 7 says combine lines 1a through 6 in column (h); the restatement adds the column (h) amounts and lines 4, 5, and 6.

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: IRS line 15 says combine lines 8a through 14 in column (h); the restatement adds the column (h) amounts and lines 11, 12, 13, and 14.

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: IRS line 16 says combine lines 7 and 15; the restatement adds line 7 and line 15.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: IRS line 17 asks whether lines 15 and 16 are both gains; the restatement tests line 15 greater than zero and line 16 greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: IRS line 20 asks whether lines 18 and 19 are both zero or blank and Form 4952 is not being filed; the restatement tests both worksheet-result helpers equal $0 and the Form 4952 filing helper false.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: IRS line 21 says if line 16 is a loss, enter the smaller of the loss or $3,000 ($1,500 MFS), treating both as positive; the restatement takes the larger (less negative) of line 16 and the signed annual limit, which is equivalent, and enters $0 otherwise.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the restatement tests Form 1040 line 3a greater than zero.

## Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "IRS line 1a totals short-term transactions with basis reported and no adjustments; the restatement sums column (d) proceeds over classification A aggregate entries, with unsupported transactions excluded by the stated screening refusal."
  - key: "1a(e)"
    status: MATCH
    reason: "IRS line 1a column (e) is cost or other basis; the restatement sums sales.e, which for covered A entries is the basis shown on the broker report, over the same A aggregate population."
  - key: "1a(g)"
    status: MATCH
    reason: "IRS line 1a column (g) is adjustments; for aggregate-eligible A entries the program's sales.g is zero, so the sum matches the no-adjustments line."
  - key: "1a(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h, which is proceeds less basis plus adjustments."
  - key: "1b(d)"
    status: MATCH
    reason: "IRS line 1b totals Form 8949 Box A or G transactions; the restatement sums column (d) over classification A detail entries, with digital Box G excluded by the stated screening refusal."
  - key: "1b(e)"
    status: MATCH
    reason: "IRS line 1b column (e) is cost or other basis; the restatement sums sales.e (reported basis for covered A entries) over the A detail population."
  - key: "1b(g)"
    status: MATCH
    reason: "IRS line 1b column (g) is the Form 8949 Part I adjustment total; the restatement sums sales.g, which combines the basis-correction and wash-sale adjustments."
  - key: "1b(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h, which is proceeds less basis plus adjustments."
  - key: "2(d)"
    status: MATCH
    reason: "IRS line 2 totals Form 8949 Box B or H transactions; the restatement sums column (d) proceeds over classification B detail entries, with digital Box H excluded by the stated screening refusal."
  - key: "2(e)"
    status: MATCH
    reason: "IRS line 2 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered B entries is the correct adjusted basis."
  - key: "2(g)"
    status: MATCH
    reason: "IRS line 2 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments."
  - key: "2(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the B detail entries."
  - key: "3(d)"
    status: MATCH
    reason: "IRS line 3 totals Form 8949 Box C or I transactions; the restatement sums column (d) proceeds over classification C detail entries, with digital Box I excluded by the stated screening refusal."
  - key: "3(e)"
    status: MATCH
    reason: "IRS line 3 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered C entries is the correct adjusted basis."
  - key: "3(g)"
    status: MATCH
    reason: "IRS line 3 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments."
  - key: "3(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the C detail entries."
  - key: "8a(d)"
    status: MATCH
    reason: "IRS line 8a totals long-term transactions with basis reported and no adjustments; the restatement sums column (d) proceeds over classification D aggregate entries, with unsupported transactions excluded by the stated screening refusal."
  - key: "8a(e)"
    status: MATCH
    reason: "IRS line 8a column (e) is cost or other basis; the restatement sums sales.e, which for covered D entries is the basis shown on the broker report."
  - key: "8a(g)"
    status: MATCH
    reason: "IRS line 8a column (g) is adjustments; for aggregate-eligible D entries the program's sales.g is zero, so the sum matches the no-adjustments line."
  - key: "8a(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the D aggregate entries."
  - key: "8b(d)"
    status: MATCH
    reason: "IRS line 8b totals Form 8949 Box D or J transactions; the restatement sums column (d) proceeds over classification D detail entries, with digital Box J excluded by the stated screening refusal."
  - key: "8b(e)"
    status: MATCH
    reason: "IRS line 8b column (e) is cost or other basis; the restatement sums sales.e (reported basis for covered D entries) over the D detail population."
  - key: "8b(g)"
    status: MATCH
    reason: "IRS line 8b column (g) is the Form 8949 Part II adjustment total; the restatement sums sales.g, which combines the basis-correction and wash-sale adjustments."
  - key: "8b(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the D detail entries."
  - key: "9(d)"
    status: MATCH
    reason: "IRS line 9 totals Form 8949 Box E or K transactions; the restatement sums column (d) proceeds over classification E detail entries, with digital Box K excluded by the stated screening refusal."
  - key: "9(e)"
    status: MATCH
    reason: "IRS line 9 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered E entries is the correct adjusted basis."
  - key: "9(g)"
    status: MATCH
    reason: "IRS line 9 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments."
  - key: "9(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the E detail entries."
  - key: "10(d)"
    status: MATCH
    reason: "IRS line 10 totals Form 8949 Box F or L transactions; the restatement sums column (d) proceeds over classification F detail entries, with digital Box L excluded by the stated screening refusal."
  - key: "10(e)"
    status: MATCH
    reason: "IRS line 10 column (e) is cost or other basis; the restatement sums sales.e, which for non-covered F entries is the correct adjusted basis."
  - key: "10(g)"
    status: MATCH
    reason: "IRS line 10 column (g) is adjustments; the restatement sums sales.g, combining the applicable basis-correction and wash-sale adjustments."
  - key: "10(h)"
    status: MATCH
    reason: "IRS column (h) is column (d) less column (e) plus column (g); the restatement sums sales.h for the F detail entries."
  - key: "4"
    status: MATCH
    reason: "IRS line 4 is for short-term gains from Forms 6252, 4684, 6781, and 8824; the program enters $0 when those source forms are absent and refuses when they exist, naming the excluded source forms."
  - key: "5"
    status: MATCH
    reason: "IRS line 5 is for Schedule K-1 short-term gains from partnerships, S corporations, estates, and trusts; the program enters $0 when no such K-1 items exist and refuses via the named additional-source-forms gate."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 is the short-term capital loss carryover from the Capital Loss Carryover Worksheet; the program enters $0 when there is no carryover and refuses when there is, naming the carryover worksheet."
  - key: "11"
    status: MATCH
    reason: "IRS line 11 is for gains from Forms 4797, 2439, 6252, 4684, 6781, and 8824; the program enters $0 when those forms are absent and refuses when they exist, naming the excluded source forms."
  - key: "12"
    status: MATCH
    reason: "IRS line 12 is for Schedule K-1 long-term gains from partnerships, S corporations, estates, and trusts; the program enters $0 when absent and refuses via the named additional-source-forms gate."
  - key: "14"
    status: MATCH
    reason: "IRS line 14 is the long-term capital loss carryover from the Capital Loss Carryover Worksheet; the program enters $0 when there is no carryover and refuses when there is, naming the carryover worksheet."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 is capital gain distributions; the restatement adds the distribution input and a zero scope-check helper whose refusals name the unsupported distribution treatments."
  - key: "7"
    status: MATCH
    reason: "IRS line 7 says combine lines 1a through 6 in column (h); the restatement adds the column (h) amounts and lines 4, 5, and 6."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 says combine lines 8a through 14 in column (h); the restatement adds the column (h) amounts and lines 11, 12, 13, and 14."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 says combine lines 7 and 15; the restatement adds line 7 and line 15."
  - key: "17"
    status: MATCH
    reason: "IRS line 17 asks whether lines 15 and 16 are both gains; the restatement tests line 15 greater than zero and line 16 greater than zero."
  - key: "20"
    status: MATCH
    reason: "IRS line 20 asks whether lines 18 and 19 are both zero or blank and Form 4952 is not being filed; the restatement tests both worksheet-result helpers equal $0 and the Form 4952 filing helper false."
  - key: "21"
    status: MATCH
    reason: "IRS line 21 says if line 16 is a loss, enter the smaller of the loss or $3,000 ($1,500 MFS), treating both as positive; the restatement takes the larger (less negative) of line 16 and the signed annual limit, which is equivalent, and enters $0 otherwise."
  - key: "22"
    status: MATCH
    reason: "IRS line 22 asks whether there are qualified dividends on Form 1040 line 3a; the restatement tests Form 1040 line 3a greater than zero."
```
