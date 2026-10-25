# Render comparison — dcprov

The rendered English of every printed line of `Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` (`rendered/2025/dcprov.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 689f9b46fc314aac0f9f004bcae475e1c35ee09bf227bfec2e8f1930c8b9a336 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 43a6afe47ff5632c92d31c2f8cddd7a184c37adea366c4a0e00df00d0ca0f393 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 3 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i2441 | 2025 | 2, 3 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 2, 3 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p503 | For use in preparing 2025 returns | 8 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 8 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### 1(c) — Identifying number (SSN or EIN)
Status: **MATCH**

Model: The IRS text says to enter the provider's SSN/ITIN if an individual or EIN otherwise, “Tax-Exempt” for a tax-exempt organization, “LAFCP” for a qualifying foreign provider, “See Attached Statement” when information is missing, and to leave column (c) blank for employer-furnished care.

### 1(d) — Was the care provider your household employee in 2025?
Status: **MATCH**

Model: The IRS text says to check Yes or No for whether the provider was a household employee during the year and gives the same control-based/nanny/daycare guidance.

### 1(e) — Amount paid
Status: **MATCH**

Model: The IRS text says to enter the total actually paid in 2025 to the provider, include amounts the employer paid to a third party on the filer's behalf, not reduce by reimbursements, and enter -0- when the employer furnished the care.

## Raw response

```yaml
lines:
  - key: "1(c)"
    status: MATCH
    reason: The IRS text says to enter the provider's SSN/ITIN if an individual or EIN otherwise, “Tax-Exempt” for a tax-exempt organization, “LAFCP” for a qualifying foreign provider, “See Attached Statement” when information is missing, and to leave column (c) blank for employer-furnished care.
  - key: "1(d)"
    status: MATCH
    reason: The IRS text says to check Yes or No for whether the provider was a household employee during the year and gives the same control-based/nanny/daycare guidance.
  - key: "1(e)"
    status: MATCH
    reason: The IRS text says to enter the total actually paid in 2025 to the provider, include amounts the employer paid to a third party on the filer's behalf, not reduce by reimbursements, and enter -0- when the employer furnished the care.
```
