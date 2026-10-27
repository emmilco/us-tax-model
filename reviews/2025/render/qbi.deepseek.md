# Render comparison — qbi

The rendered English of every printed line of `Qualified business income and section 199A dividends — amounts and the choice of Form 8995` (`rendered/2025/qbi.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e86d5771f84cf8553d61d7af5c4533519e5ac805fa51838fe5d2cab37fbaeda3 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 50f6069b0fc66b0331df115f52f02af9cf49ab51a4e9839ceb291f8371ad2f69 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 0 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 1, 3, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 1, 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| f8995a | 2025; created 2025-09-12 | 1, 2 | whole document | 240927847d55e46348a41276d2bb81438c6fecae38b8106523444e56688c95b1 | - | c6abd31f2fb127536ba771d57a44e1487beebf502d934a3ebb8614e0508370d4 |
| i8995a | 2025; printed date 2026-01-26 | 1 | cited pages | 83411868381d4f5edbb455d348b480a63d96586bcb4f821f67acc0e027d5401d | 1 | 1843d02e5f17b6a3f1ba9d1ab3304a5c0b6862916c5ff0e622e3ccb411a89af3 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |

## Lines

### 3 — Qualified business net (loss) carryforward from the prior year (as a positive amount)
Status: **MISMATCH**

Restated: Input — The qualified business loss carryforward from line 16 of your 2024 Form 8995 (or the corresponding line of your 2024 Form 8995-A), entered as a positive amount (zero if none)

Model: IRS line 3 is "Qualified business net (loss) carryforward from the prior year" shown with parentheses, and line 4 says "Combine lines 2 and 3," so the carryforward is a negative amount; the restatement instead says "entered as a positive amount." The line 3 instructions also require the "qualified portion" allowed in calculating taxable income in the current year, not merely prior-year line 16.

Ruling: model error; on the sign: f8995 p. 1, line 3 "Qualified business net (loss) carryforward from the prior year" is printed in parentheses and line 4 says "Combine lines 2 and 3". The qbi line 3 is an input entered as a positive amount, and the form line that prints it negates it (f8995.line3: "Subtract qbi line 3 from qbi helper 'Year parameter sales.zero'"), so lines 4 and 16 combine a negative amount as the form requires; the model read the input's sign convention as the printed amount. On the second point (the "qualified portion" allowed this year, i8995 p. 4, Line 3: "Include here the qualified portion of trade or business (loss) carryforward allowed in calculating taxable income in the current year"; i8995 p. 3: previously suspended losses allowed are "treated as a qualified net loss carryforward ... See Line 3"): scope, refused by qbi.unsupported ("losses or deductions suspended in an earlier year by another provision and allowed this year") on qbi.eligible. Incidental citation-only finding on this line: findings.md F2.

## Raw response

```yaml
lines:
  - key: "3"
    status: MISMATCH
    reason: 'IRS line 3 is "Qualified business net (loss) carryforward from the prior year" shown with parentheses, and line 4 says "Combine lines 2 and 3," so the carryforward is a negative amount; the restatement instead says "entered as a positive amount." The line 3 instructions also require the "qualified portion" allowed in calculating taxable income in the current year, not merely prior-year line 16.'
```
