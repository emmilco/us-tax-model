# Render comparison — tipjob

The rendered English of every printed line of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` (`rendered/2025/tipjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d16df68e6acdb3193db8569daabc919c39883124485a1178c5b7484d45c548d1 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 2 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1(b) — Amount of qualified tips reported by this employer on Form W-2, or reported by you to this
Status: **MATCH**

Model: Column (b) asks for the 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. The instructions allow W-2 box 7, the Forms 4070 total (noting it 'may be more accurate if the amount in box 1 or box 5 is more than $176,100'), or the amount in box 14 or on a separate statement, and the refusal excludes employers where only some tips are qualified.

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **MISMATCH**

Restated: Enter $0 (sales.zero).

Model: The worksheet column (c) is 'Qualified tips reported on Form 4137, column 1(c), for this employer', and method 4 says to 'use the amount of qualified tips included for the employer in column 1(c) of Form 4137'. Always entering $0 drops this amount, and no refusal excludes filers who submit Form 4137.

Ruling: adopted. Column (c) now carries the refusal of Form 4137 (s2.other); within scope it is zero.

### 1(d) — Enter the greater of column (b) or column (c)
Status: **MATCH**

Model: The worksheet says 'Enter the greater of column (b) or column (c)', which the restatement follows.

## Raw response

```yaml
```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "Column (b) asks for the 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. The instructions allow W-2 box 7, the Forms 4070 total (noting it 'may be more accurate if the amount in box 1 or box 5 is more than $176,100'), or the amount in box 14 or on a separate statement, and the refusal excludes employers where only some tips are qualified."
  - key: "1(c)"
    status: MISMATCH
    reason: "The worksheet column (c) is 'Qualified tips reported on Form 4137, column 1(c), for this employer', and method 4 says to 'use the amount of qualified tips included for the employer in column 1(c) of Form 4137'. Always entering $0 drops this amount, and no refusal excludes filers who submit Form 4137."
  - key: "1(d)"
    status: MATCH
    reason: "The worksheet says 'Enter the greater of column (b) or column (c)', which the restatement follows."
```
```
