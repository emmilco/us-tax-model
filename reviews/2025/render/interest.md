# Render comparison — interest

The rendered English of every printed line of `Schedule B — interest payer entries` (`rendered/2025/interest.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b14ee638548dd1e8db3a36002f28b8c3ee35038867e49df3910e35600992a563 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 |

## Lines

### amount — Taxable interest from this payer, including Treasury interest; exclude tax-exempt interest
Status: **MATCH**

Model: Line 1 instructions say to 'Report on line 1 all of your taxable interest', to 'Include interest from series EE, H, HH, and I U.S. savings bonds' and to 'List each payer's name and the amount'. They also say 'Don't report on line 1 any tax-exempt interest', so a per-payer taxable amount that includes Treasury interest and excludes tax-exempt interest matches.

## Raw response

```yaml
lines:
  - key: "Taxable interest from this payer, including Treasury interest; exclude tax-exempt interest"
    status: MATCH
    reason: "Line 1 instructions say to 'Report on line 1 all of your taxable interest', to 'Include interest from series EE, H, HH, and I U.S. savings bonds' and to 'List each payer's name and the amount'. They also say 'Don't report on line 1 any tax-exempt interest', so a per-payer taxable amount that includes Treasury interest and excludes tax-exempt interest matches."
```
