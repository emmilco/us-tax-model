# Render comparison — interest

The rendered English of every printed line of `Schedule B — interest payer entries` (`rendered/2025/interest.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b568c64494f81cf82762124f5f5e77f3867771057f62b0bb8cd0bc3b92158b1d |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### amount — Taxable interest from this payer, including Treasury interest; exclude tax-exempt interest
Status: **MATCH**

Model: Line 1 says "Report on line 1 all of your taxable interest... List each payer's name and the amount. Don't report on line 1 any tax-exempt interest" and to "Include interest from series EE, H, HH, and I U.S. savings bonds." Those bonds are Treasury interest, so the per-payer input of taxable interest, with Treasury interest included and tax-exempt interest left out, matches the line.

## Raw response

```yaml
```yaml
lines:
  - key: "amount"
    status: MATCH
    reason: "Line 1 says \"Report on line 1 all of your taxable interest... List each payer's name and the amount. Don't report on line 1 any tax-exempt interest\" and to \"Include interest from series EE, H, HH, and I U.S. savings bonds.\" Those bonds are Treasury interest, so the per-payer input of taxable interest, with Treasury interest included and tax-exempt interest left out, matches the line."
```
```
