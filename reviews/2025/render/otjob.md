# Render comparison — otjob

The rendered English of every printed line of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` (`rendered/2025/otjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e625ac4a03d54c3b124d721cbbbc7084bc5cd64bd8fa7a06e582d75f7964c9e3 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e2721cf8506da1b69c5a83dee7008cdd3fdeb8551f04a26a506a965f68659361 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### 1(b) — Qualified overtime reported on Form W-2, box 1
Status: **MATCH**

Model: The text requires an FLSA-eligible employee ('Qualified overtime must be paid to a covered, nonexempt employee under the FLSA'), so $0 for a non-eligible employee is correct. For an eligible employee, the employer-reported or requested amount and methods 1–4 (÷3, ×1/2, ×1/4 at double time) match paragraphs 1–4 and Examples 1–3, and the input includes deferred overtime and excludes tips and weekend/holiday pay as the instructions direct; reasonable-method estimates, other rates or adjustments, and special section 7 rules are excluded by a refusal that names them.
Reviewed in: pass 1239ee51011d

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1(b) | a8322f22511cef38197b67220aa7ab0402ecad234c81556e2849582bccb470d7 |
| (rest of the document) | f07c6baaff7adbcac4cab13c35e31d4096b1b8e3b07ebb63065b80d476899bec |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 1239ee51011d

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1(b) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1239ee51011d471402ee376cf6f7fc45c994c752da380181d8485e07764aba5f |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 5595f85fc3e392241eb3285367b089de5adaa58954a433eea5a627e42669881b |
| receipt | .transcription/otjob.render.lines-57b9202763e7 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

##### Raw response

```yaml
```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The text requires an FLSA-eligible employee ('Qualified overtime must be paid to a covered, nonexempt employee under the FLSA'), so $0 for a non-eligible employee is correct. For an eligible employee, the employer-reported or requested amount and methods 1–4 (÷3, ×1/2, ×1/4 at double time) match paragraphs 1–4 and Examples 1–3, and the input includes deferred overtime and excludes tips and weekend/holiday pay as the instructions direct; reasonable-method estimates, other rates or adjustments, and special section 7 rules are excluded by a refusal that names them."
```
```

## Raw response

```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The text says qualified overtime must be paid to an FLSA-eligible employee, so entering $0 when the filer is not eligible is right. For an eligible filer, the program allows the employer's box 14 or on-request amount, the separately shown FLSA Overtime Premium (method 1), total overtime pay ÷ 3 (method 2), and the double-time fractions of one-half and one-fourth (methods 3 and 4). It also includes overtime not in box 1 (\"enter that amount here\"). The refusal names the cases it leaves out: reasonable-method estimates, other overtime rates and special section 7 rules."
```
