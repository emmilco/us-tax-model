# Render comparison — tipjob

The rendered English of every printed line of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` (`rendered/2025/tipjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 91e4143328bcda598b3d2de95a9a55b02e2742e2e99743702cd9fda29d8c3d64 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 3 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1(b) — Amount of qualified tips reported by this employer on Form W-2, or reported by you to this
Status: **MATCH**

Model: Column (b) is 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. Methods 1–3 allow W-2 box 7, the Forms 4070 total (possibly more accurate if box 1 or box 5 exceeds $176,100), or box 14 or a separate statement. The refusal for tips that are not all qualified narrows the line, consistent with 'Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c.'

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **MATCH**

Model: Column (c) is 'Qualified tips reported on Form 4137, column 1(c), for this employer'. The program refuses whenever Schedule 2 has other amounts, which the gate says include 'tax on unreported tips (Form 4137)'. So within the supported cases no Form 4137 tips exist and $0 is correct.

### 1(d) — Enter the greater of column (b) or column (c)
Status: **MATCH**

Model: Column (d) says 'Enter the greater of column (b) or column (c)', which matches the restatement.

## Raw response

```yaml
```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "Column (b) is 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. Methods 1–3 allow W-2 box 7, the Forms 4070 total (possibly more accurate if box 1 or box 5 exceeds $176,100), or box 14 or a separate statement. The refusal for tips that are not all qualified narrows the line, consistent with 'Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c.'"
  - key: "1(c)"
    status: MATCH
    reason: "Column (c) is 'Qualified tips reported on Form 4137, column 1(c), for this employer'. The program refuses whenever Schedule 2 has other amounts, which the gate says include 'tax on unreported tips (Form 4137)'. So within the supported cases no Form 4137 tips exist and $0 is correct."
  - key: "1(d)"
    status: MATCH
    reason: "Column (d) says 'Enter the greater of column (b) or column (c)', which matches the restatement."
```
```
