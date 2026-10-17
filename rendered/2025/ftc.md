# Foreign tax credit — election without Form 1116

- Document: `ftc` (form, tax year 2025)
- Note: Creditable foreign tax is a supplied amount after reductions; this slice does not determine foreign-tax law or automate holdings/related-payment tests. The election is an explicit user choice. NIIT is excluded from regular tax.

## (helper) — `ftc.taxes`

- **Authored helper label:** Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7
- **Encoded (NonNegDollars):** Input — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7
- Expr: `{"op":"input","source":"Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.all_passive`

- **Authored helper label:** Was all foreign-source gross income passive category income under the small-tax election rules?
- **Encoded (Bool):** Input — Was all foreign-source gross income passive category income under the small-tax election rules?
- Expr: `{"op":"input","source":"Was all foreign-source gross income passive category income under the small-tax election rules?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.statements`

- **Authored helper label:** Were all foreign income and taxes reported on qualified payee statements?
- **Encoded (Bool):** Input — Were all foreign income and taxes reported on qualified payee statements?
- Expr: `{"op":"input","source":"Were all foreign income and taxes reported on qualified payee statements?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.eligible`

- **Authored helper label:** Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?
- **Encoded (Bool):** Input — Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?
- Expr: `{"op":"input","source":"Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.elect`

- **Authored helper label:** Elect the credit without Form 1116, with no carryover to or from this election year?
- **Encoded (Bool):** Input — Elect the credit without Form 1116, with no carryover to or from this election year?
- Expr: `{"op":"input","source":"Elect the credit without Form 1116, with no carryover to or from this election year?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limit`

- **Authored helper label:** Year parameter ftc.limit
- **Encoded (NonNegDollars):** Enter single $300; mfj $600; mfs $300; hoh $300; qss $300 (ftc.limit).
- Expr: `{"op":"param","ref":"ftc.limit"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.has_tax`

- **Authored helper label:** Positive foreign taxes
- **Encoded (Bool):** helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" > $0
- Expr: `{"gt":["ftc.taxes",{"const":0}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.needs1116`

- **Authored helper label:** Fails a condition of the election
- **Encoded (Bool):** helper "Positive foreign taxes" = true and (helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" > helper "Year parameter ftc.limit" or helper "Was all foreign-source gross income passive category income under the small-tax election rules?" = false or helper "Were all foreign income and taxes reported on qualified payee statements?" = false or helper "Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?" = false or helper "Elect the credit without Form 1116, with no carryover to or from this election year?" = false)
- Expr: `{"all":[{"eq":["ftc.has_tax",{"const":true}],"op":"test"},{"any":[{"gt":["ftc.taxes","ftc.limit"],"op":"test"},{"eq":["ftc.all_passive",{"const":false}],"op":"test"},{"eq":["ftc.statements",{"const":false}],"op":"test"},{"eq":["ftc.eligible",{"const":false}],"op":"test"},{"eq":["ftc.elect",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limited`

- **Authored helper label:** Smaller of ftc.taxes, f1040.line16
- **Encoded (Dollars):** Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.
- Expr: `{"of":["ftc.taxes","f1040.line16"],"op":"smaller_of"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.credit`

- **Authored helper label:** Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign tax
- **Encoded (Dollars):** Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]
- **Refusal:** when ftc.needs1116 is true, cannot complete Form 1116. The small-tax election is unavailable or not chosen. Form 1116 is deferred, not dropped; prepare it separately. Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.limited"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.zero"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)
