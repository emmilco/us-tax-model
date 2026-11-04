# Render comparison — tipjob

The rendered English of every printed line of `Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` (`rendered/2025/tipjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 91e4143328bcda598b3d2de95a9a55b02e2742e2e99743702cd9fda29d8c3d64 |
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

Model: Column 1(b) is the 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. The instructions name W-2 box 7 (method 1), Forms 4070 or a similar monthly form, more accurate if box 1 or box 5 exceeds $176,100 (method 2), and box 14 or a separate statement (method 3) as ways to figure employee qualified tips, which the restatement follows. The mixed-tips refusal properly excludes splitting out tips not received in a listed occupation.
Reviewed in: pass 87df60e71a0e

### 1(c) — Qualified tips reported on Form 4137, column 1(c), for this employer
Status: **MATCH**

Model: Column (c) is 'Qualified tips reported on Form 4137, column 1(c), for this employer'. The program refuses whenever Schedule 2 has other amounts, which the gate says include 'tax on unreported tips (Form 4137)'. So within the supported cases no Form 4137 tips exist and $0 is correct.

### 1(d) — Enter the greater of column (b) or column (c)
Status: **MATCH**

Model: Column (d) says 'Enter the greater of column (b) or column (c)', which matches the restatement.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1(b) | 78252a1c7a5b8e25882900e48073e0e375f046a6d1d1353aa9ea968802966782 |
| 1(c) | dc81b1fdb2e434e71f49b139aec5466fef26bb4ba5c68d165e439ad08b6aa1e3 |
| 1(d) | 75ed0b95689bdb06499d0392551b4bcd32a543b9f194be357438a21599f26e1c |
| (rest of the document) | c37992897a314480e61bbf3608e11b869900af62a9097269e5f2adb60c7e7d11 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 87df60e71a0e

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1(b) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 87df60e71a0ed456fdc5bb59c4e3cde15e06067226a1f162e528432f243bd060 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c7ae92777c2904ff4d7771a5349694fa7659b27bd01c14095c27e034f843a26a |
| receipt | .transcription/tipjob.render.lines-57b9202763e7 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Raw response

```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "Column 1(b) is the 'Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070'. The instructions name W-2 box 7 (method 1), Forms 4070 or a similar monthly form, more accurate if box 1 or box 5 exceeds $176,100 (method 2), and box 14 or a separate statement (method 3) as ways to figure employee qualified tips, which the restatement follows. The mixed-tips refusal properly excludes splitting out tips not received in a listed occupation."
```

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
