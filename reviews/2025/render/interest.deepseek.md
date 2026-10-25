# Render comparison — interest

The rendered English of every printed line of `Schedule B — interest payer entries` (`rendered/2025/interest.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b70d19fd9713b243b0227ea6cc403624d8510e9cf062d90156ea5cc39f73cb40 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 56bd4a9fffb4cc71c572b1867bbafd7440eb9065cc71a7b1afabf1a12279b207 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| i1040gi | 2025; printed date 2026-02-25 | 95 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 95 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099int | January 2024 (continuous-use form) | 5 | pages named by another document's citation | c4514fa301d16db6abe795e8493b92425cffbf37ac4c39a754b06be677f4a115 | 5 | b47750922f8b8b3274e9efb422b49fb83b89ea5ce9f68e24fb860381516355a2 |

## Lines

### amount — Taxable interest from this payer, including Treasury interest; exclude tax-exempt interest
Status: **MATCH**

Model: Schedule B line 1 says to report all taxable interest and not report tax-exempt interest, and the Form 1099-INT instructions show Treasury interest separately; the helper captures taxable interest from the payer while excluding tax-exempt interest.

### penalty — Early withdrawal penalty charged by this payer (Form 1099-INT box 2, or the penalty shown 
Status: **MATCH**

Model: The IRS instructions state that Form 1099-INT or Form 1099-OID shows any penalty charged for early withdrawal of savings, and Box 2 is the early-withdrawal forfeiture amount; the helper records that penalty separately.

## Raw response

```yaml
lines:
  - key: "amount"
    status: MATCH
    reason: "Schedule B line 1 says to report all taxable interest and not report tax-exempt interest, and the Form 1099-INT instructions show Treasury interest separately; the helper captures taxable interest from the payer while excluding tax-exempt interest."
  - key: "penalty"
    status: MATCH
    reason: "The IRS instructions state that Form 1099-INT or Form 1099-OID shows any penalty charged for early withdrawal of savings, and Box 2 is the early-withdrawal forfeiture amount; the helper records that penalty separately."
```
