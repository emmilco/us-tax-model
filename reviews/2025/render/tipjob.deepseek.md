# Render comparison — tipjob

The rendered English of every printed line of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` (`rendered/2025/tipjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1638dd13792e823cc11b3d37b407b7e31738d960715615e7ab7eebfacba39996 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | dd1cd95f3a144f5a654662ca694fc405f1e99bd27873da582895e59c7d0153c4 |
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

Model: The worksheet column (b) is the qualified tips from this employer, and the instructions allow using Form W-2 box 7, the total reported on Forms 4070 or similar monthly reports, or an amount reported in box 14 or on a separate statement. The mixed-tips refusal correctly excludes splitting one employer’s tips between qualified and nonqualified tips.

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **MATCH**

Model: IRS line 1(c) is for qualified tips reported on Form 4137; the program enters $0 when Form 4137 is unsupported and its refusal states that Form 4137 tips are outside the tool. Within the supported cases, $0 is correct.

### 1(d) — Enter the greater of column (b) or column (c)
Status: **MATCH**

Model: IRS says to enter the greater of column (b) or column (c); the restatement says the larger of line 1(b) or line 1(c), which is equivalent for the row.

## Raw response

```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The worksheet column (b) is the qualified tips from this employer, and the instructions allow using Form W-2 box 7, the total reported on Forms 4070 or similar monthly reports, or an amount reported in box 14 or on a separate statement. The mixed-tips refusal correctly excludes splitting one employer’s tips between qualified and nonqualified tips."
  - key: "1(c)"
    status: MATCH
    reason: "IRS line 1(c) is for qualified tips reported on Form 4137; the program enters $0 when Form 4137 is unsupported and its refusal states that Form 4137 tips are outside the tool. Within the supported cases, $0 is correct."
  - key: "1(d)"
    status: MATCH
    reason: "IRS says to enter the greater of column (b) or column (c); the restatement says the larger of line 1(b) or line 1(c), which is equivalent for the row."
```
