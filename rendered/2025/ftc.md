# Foreign tax credit — election without Form 1116

- Document: `ftc` (form, tax year 2025)
- Note: Creditable foreign tax is a supplied amount after reductions; this slice does not determine foreign-tax law or automate holdings/related-payment tests. The election is an explicit user choice. NIIT is excluded from regular tax.

## (helper) — `ftc.taxes`

- **Authored helper label:** Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7
- **Encoded (NonNegDollars):** Input — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7
- Expr: `{"op":"input","source":"Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.all_passive`

- **Authored helper label:** Was all foreign-source gross income passive category income under the small-tax election rules?
- **Encoded (Bool):** Input — Was all foreign-source gross income passive category income under the small-tax election rules?
- Expr: `{"op":"input","source":"Was all foreign-source gross income passive category income under the small-tax election rules?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.statements`

- **Authored helper label:** Were all foreign income and taxes reported on qualified payee statements?
- **Encoded (Bool):** Input — Were all foreign income and taxes reported on qualified payee statements?
- Expr: `{"op":"input","source":"Were all foreign income and taxes reported on qualified payee statements?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.eligible`

- **Authored helper label:** Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?
- **Encoded (Bool):** Input — Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?
- Expr: `{"op":"input","source":"Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.elect`

- **Authored helper label:** Elect the credit without Form 1116, with no carryover to or from this election year?
- **Encoded (Bool):** Input — Elect the credit without Form 1116, with no carryover to or from this election year?
- Expr: `{"op":"input","source":"Elect the credit without Form 1116, with no carryover to or from this election year?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limit`

- **Authored helper label:** Year parameter ftc.limit
- **Encoded (NonNegDollars):** Enter single $300; mfj $600; mfs $300; hoh $300; qss $300 (ftc.limit).
- Expr: `{"op":"param","ref":"ftc.limit"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.has_tax`

- **Authored helper label:** Positive foreign taxes
- **Encoded (Bool):** helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" > $0
- Expr: `{"gt":["ftc.taxes",{"const":0}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.no`

- **Authored helper label:** Year parameter ftc.no (false)
- **Encoded (Bool):** Enter false (ftc.no).
- Expr: `{"op":"param","ref":"ftc.no"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.all_passive_if_tax`

- **Authored helper label:** Whether all foreign-source gross income was passive category income, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Was all foreign-source gross income passive category income under the small-tax election rules?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.all_passive"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.statements_if_tax`

- **Authored helper label:** Whether all foreign income and taxes were reported on qualified payee statements, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Were all foreign income and taxes reported on qualified payee statements?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.statements"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.eligible_if_tax`

- **Authored helper label:** Whether the creditability, holding-period, related-payment and reduction rules are met, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Have creditability, holding-period, related-payment and required foreign-tax reduction rules been satisfied?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.eligible"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.elect_if_tax`

- **Authored helper label:** Whether the election without Form 1116 is made, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Elect the credit without Form 1116, with no carryover to or from this election year?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.elect"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.needs1116`

- **Authored helper label:** Fails a condition of the election
- **Encoded (Bool):** helper "Positive foreign taxes" = true and (helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" > helper "Year parameter ftc.limit" or helper "Whether all foreign-source gross income was passive category income, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether all foreign income and taxes were reported on qualified payee statements, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether the creditability, holding-period, related-payment and reduction rules are met, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether the election without Form 1116 is made, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false)
- Expr: `{"all":[{"eq":["ftc.has_tax",{"const":true}],"op":"test"},{"any":[{"gt":["ftc.taxes","ftc.limit"],"op":"test"},{"eq":["ftc.all_passive_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.statements_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.eligible_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.elect_if_tax",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.regular_tax`

- **Authored helper label:** Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)
- **Encoded (Dollars):** Add f1040 line 16 and s2 line 1z.
- Expr: `{"of":["f1040.line16","s2.line1z"],"op":"sum"}`
- Cite: [i1116] p. 25, Line 20, "Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limited`

- **Authored helper label:** Smaller of ftc.taxes, ftc.regular_tax
- **Encoded (Dollars):** Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or helper "Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)".
- Expr: `{"of":["ftc.taxes","ftc.regular_tax"],"op":"smaller_of"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.credit`

- **Authored helper label:** Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign tax
- **Encoded (Dollars):** Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, ftc.regular_tax"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]
- **Refusal:** when ftc.needs1116 is true, cannot complete Form 1116. The small-tax election is unavailable or not chosen. Form 1116 is deferred, not dropped; prepare it separately. Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.limited"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.zero"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)
