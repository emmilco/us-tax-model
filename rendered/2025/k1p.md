# Schedule K-1 (Form 1065) — one partner's share from one partnership

- Document: `k1p` (form, tax year 2025)
- Collection: keyed entries within person; [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)
- Note: One entry per Schedule K-1 (Form 1065) a person received. Boxes 1 to 3 are each one activity; box 1 is passive unless the partner materially participated (tests 1, 2, 3 or 5), boxes 2 and 3 are passive, and box 2 goes in Part IV of Form 8582 when a general partner actively participated and owned a tenth. The Form 8582 columns (a) to (c) and (e) of each activity, the Schedule E line 28 columns (h), (i) and (k), and the portfolio, self-employment, withholding and section 199A amounts are figured here and totalled on the person. Refused: publicly traded partnerships, boxes 4b, 7, 10 to 13 (other than 13 AE), 14 B and C, 15 (other than O), 16, 17, 20 (codes other than A, B, N, Z, AG), 21, 22 and 23, foreign partnerships, a sale of the interest, property distributions and distributions above basis, trading partnerships, material participation by tests 4, 6 or 7, losses above basis or not at risk, losses carried from earlier years by the basis or at-risk limits, the held-back losses Form 8582 does not take here, unreimbursed partnership expenses, interest on money borrowed to buy into the partnership, a fuel tax credit from it claimed in 2024, a real estate professional's box 2 when no rental of the filer's own is listed (Schedule E Part I asks it then), and a rented home a partner used personally.

## (helper) — `k1p.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1065sk1] p. 1, Part III, "Partner’s Share of Current Year Income" (2025; sha256 66098d4d)

## (helper) — `k1p.no`

- **Authored helper label:** No (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [f1065sk1] p. 1, Part III, "Partner’s Share of Current Year Income" (2025; sha256 66098d4d)

## (helper) — `k1p.yes`

- **Authored helper label:** Yes (true)
- **Encoded (Bool):** Enter true (hsa.yes).
- Expr: `{"op":"param","ref":"hsa.yes"}`
- Cite: [f1065sk1] p. 1, Part III, "Partner’s Share of Current Year Income" (2025; sha256 66098d4d)

## (helper) — `k1p.one`

- **Authored helper label:** One Schedule K-1
- **Encoded (Count):** Enter 1 (person.one).
- Expr: `{"op":"param","ref":"person.one"}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `k1p.ptp`

- **Authored helper label:** Publicly traded partnership (item D checked)
- **Encoded (Bool):** Input — Is the box in item D checked, for a publicly traded partnership (PTP)?
- Expr: `{"op":"input","source":"Is the box in item D checked, for a publicly traded partnership (PTP)?"}`
- Cite: [i1065sk1] p. 11, Item D, "If the box in item D is checked, you’re a partner in a PTP" (2025; sha256 659063e0)

## (helper) — `k1p.general`

- **Authored helper label:** General partner or LLC member-manager (item G)
- **Encoded (Bool):** Input — In item G, is the first box checked: general partner or LLC member-manager?
- Expr: `{"op":"input","source":"In item G, is the first box checked: general partner or LLC member-manager?"}`
- Cite: [i1065sk1] p. 2, General Partner, "A general partner is a partner who is personally liable for partnership debts" (2025; sha256 659063e0)

## (helper) — `k1p.is_llc`

- **Authored helper label:** The partnership is a limited liability company (LLC), asked when item G's first box is not checked
- **Encoded (Bool):** Input — Is this partnership a limited liability company (LLC)?
- Interpretation: amb.2025.k1p_llc_member
- Expr: `{"op":"input","source":"Is this partnership a limited liability company (LLC)?"}`
- Cite: [i1065sk1] p. 2, Limited Partner, "Some members of other entities, such as domestic or foreign business trusts or limited liability companies (LLCs) that are classified as partnerships, may be treated as limited partners for certain purposes" (2025; sha256 659063e0)

## (gate) — `k1p.is_llc_if_not_gp`

- **Authored helper label:** Asked only when item G's first box (general partner or LLC member-manager) is not checked (false otherwise)
- **Encoded (Bool):** Choose — [helper "General partner or LLC member-manager (item G)" = false → helper "The partnership is a limited liability company (LLC), asked when item G's first box is not checked"] [helper "General partner or LLC member-manager (item G)" = true → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.general",{"const":false}],"op":"test"},"then":"k1p.is_llc"},{"guard":{"eq":["k1p.general",{"const":true}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 2, Limited Partner, "Some members of other entities, such as domestic or foreign business trusts or limited liability companies (LLCs) that are classified as partnerships, may be treated as limited partners for certain purposes" (2025; sha256 659063e0)

## (helper) — `k1p.has_b1`

- **Authored helper label:** Box 1 shows an amount: ordinary business income (loss)
- **Encoded (Bool):** Input — Does box 1 (ordinary business income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 1 (ordinary business income or loss) show an amount?"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership" (2025; sha256 659063e0)

## 1 — `k1p.box1`

- **IRS:** Ordinary business income (loss)
- **Encoded (Dollars):** Input — The amount in box 1, ordinary business income (loss). Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 1, ordinary business income (loss). Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership" (2025; sha256 659063e0)

## (gate) — `k1p.box1_if_any`

- **Authored helper label:** Box 1, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 1 shows an amount: ordinary business income (loss)" = true → line 1] [helper "Box 1 shows an amount: ordinary business income (loss)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b1",{"const":true}],"op":"test"},"then":"k1p.box1"},{"guard":{"eq":["k1p.has_b1",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.has_b2`

- **Authored helper label:** Box 2 shows an amount: net rental real estate income (loss)
- **Encoded (Bool):** Input — Does box 2 (net rental real estate income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 2 (net rental real estate income or loss) show an amount?"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## 2 — `k1p.box2`

- **IRS:** Net rental real estate income (loss)
- **Encoded (Dollars):** Input — The amount in box 2, net rental real estate income (loss). Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 2, net rental real estate income (loss). Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (gate) — `k1p.box2_if_any`

- **Authored helper label:** Box 2, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 2 shows an amount: net rental real estate income (loss)" = true → line 2] [helper "Box 2 shows an amount: net rental real estate income (loss)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b2",{"const":true}],"op":"test"},"then":"k1p.box2"},{"guard":{"eq":["k1p.has_b2",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.has_b3`

- **Authored helper label:** Box 3 shows an amount: other net rental income (loss)
- **Encoded (Bool):** Input — Does box 3 (other net rental income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 3 (other net rental income or loss) show an amount?"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (gate) — `k1p.llc_member_active`

- **Authored helper label:** A member of an LLC who is not a manager, with an amount in box 1 or box 2 (whether the member counts as a limited partner decides the tests)
- **Encoded (Bool):** helper "Asked only when item G's first box (general partner or LLC member-manager) is not checked (false otherwise)" = true and (helper "Box 1 shows an amount: ordinary business income (loss)" = true or helper "Box 2 shows an amount: net rental real estate income (loss)" = true)
- Interpretation: amb.2025.k1p_llc_member
- Expr: `{"all":[{"eq":["k1p.is_llc_if_not_gp",{"const":true}],"op":"test"},{"any":[{"eq":["k1p.has_b1",{"const":true}],"op":"test"},{"eq":["k1p.has_b2",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 2, Limited Partner, "Some members of other entities, such as domestic or foreign business trusts or limited liability companies (LLCs) that are classified as partnerships, may be treated as limited partners for certain purposes" (2025; sha256 659063e0)

## 3 — `k1p.box3`

- **IRS:** Other net rental income (loss)
- **Encoded (Dollars):** Input — The amount in box 3, other net rental income (loss). Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 3, other net rental income (loss). Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (gate) — `k1p.box3_if_any`

- **Authored helper label:** Box 3, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 3 shows an amount: other net rental income (loss)" = true → line 3] [helper "Box 3 shows an amount: other net rental income (loss)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b3",{"const":true}],"op":"test"},"then":"k1p.box3"},{"guard":{"eq":["k1p.has_b3",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.has_b4a`

- **Authored helper label:** Box 4a shows an amount: guaranteed payments for services
- **Encoded (Bool):** Input — Does box 4a (guaranteed payments for services) show an amount?
- Expr: `{"op":"input","source":"Does box 4a (guaranteed payments for services) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 4a. Guaranteed Payments for Services, "you should report them in column (k) of Schedule E (Form 1040), line 28" (2025; sha256 659063e0)

## 4a — `k1p.box4a`

- **IRS:** Guaranteed payments for services
- **Encoded (NonNegDollars):** Input — The amount in box 4a, guaranteed payments for services.
- Expr: `{"op":"input","source":"The amount in box 4a, guaranteed payments for services."}`
- Cite: [i1065sk1] p. 15, Box 4a. Guaranteed Payments for Services, "you should report them in column (k) of Schedule E (Form 1040), line 28" (2025; sha256 659063e0)

## (gate) — `k1p.box4a_if_any`

- **Authored helper label:** Box 4a, asked only when the box shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 4a shows an amount: guaranteed payments for services" = true → line 4a] [helper "Box 4a shows an amount: guaranteed payments for services" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b4a",{"const":true}],"op":"test"},"then":"k1p.box4a"},{"guard":{"eq":["k1p.has_b4a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 4a. Guaranteed Payments for Services, "you should report them in column (k) of Schedule E (Form 1040), line 28" (2025; sha256 659063e0)

## (helper) — `k1p.has_b5`

- **Authored helper label:** Box 5 shows an amount: interest income
- **Encoded (Bool):** Input — Does box 5 (interest income) show an amount?
- Expr: `{"op":"input","source":"Does box 5 (interest income) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 5. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 659063e0)

## 5 — `k1p.box5`

- **IRS:** Interest income
- **Encoded (NonNegDollars):** Input — The amount in box 5, interest income.
- Expr: `{"op":"input","source":"The amount in box 5, interest income."}`
- Cite: [i1065sk1] p. 15, Box 5. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 659063e0)

## (gate) — `k1p.box5_if_any`

- **Authored helper label:** Box 5, asked only when the box shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 5 shows an amount: interest income" = true → line 5] [helper "Box 5 shows an amount: interest income" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b5",{"const":true}],"op":"test"},"then":"k1p.box5"},{"guard":{"eq":["k1p.has_b5",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 5. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 659063e0)

## (helper) — `k1p.has_b6a`

- **Authored helper label:** Box 6a shows an amount: ordinary dividends
- **Encoded (Bool):** Input — Does box 6a (ordinary dividends) show an amount?
- Expr: `{"op":"input","source":"Does box 6a (ordinary dividends) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 6a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 659063e0)

## 6a — `k1p.box6a`

- **IRS:** Ordinary dividends
- **Encoded (NonNegDollars):** Input — The amount in box 6a, ordinary dividends.
- Expr: `{"op":"input","source":"The amount in box 6a, ordinary dividends."}`
- Cite: [i1065sk1] p. 15, Box 6a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 659063e0)

## (gate) — `k1p.box6a_if_any`

- **Authored helper label:** Box 6a, asked only when the box shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 6a shows an amount: ordinary dividends" = true → line 6a] [helper "Box 6a shows an amount: ordinary dividends" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b6a",{"const":true}],"op":"test"},"then":"k1p.box6a"},{"guard":{"eq":["k1p.has_b6a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 6a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 659063e0)

## (helper) — `k1p.has_b8`

- **Authored helper label:** Box 8 shows an amount: net short-term capital gain (loss)
- **Encoded (Bool):** Input — Does box 8 (net short-term capital gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 8 (net short-term capital gain or loss) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 8. Net Short-Term Capital Gain (Loss), "Report the net short-term capital gain (loss) on Schedule D (Form 1040), line 5" (2025; sha256 659063e0)

## 8 — `k1p.box8`

- **IRS:** Net short-term capital gain (loss)
- **Encoded (Dollars):** Input — The amount in box 8, net short-term capital gain (loss). Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 8, net short-term capital gain (loss). Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 15, Box 8. Net Short-Term Capital Gain (Loss), "Report the net short-term capital gain (loss) on Schedule D (Form 1040), line 5" (2025; sha256 659063e0)

## (gate) — `k1p.box8_if_any`

- **Authored helper label:** Box 8, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 8 shows an amount: net short-term capital gain (loss)" = true → line 8] [helper "Box 8 shows an amount: net short-term capital gain (loss)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b8",{"const":true}],"op":"test"},"then":"k1p.box8"},{"guard":{"eq":["k1p.has_b8",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 8. Net Short-Term Capital Gain (Loss), "Report the net short-term capital gain (loss) on Schedule D (Form 1040), line 5" (2025; sha256 659063e0)

## (helper) — `k1p.has_b9a`

- **Authored helper label:** Box 9a shows an amount: net long-term capital gain (loss)
- **Encoded (Bool):** Input — Does box 9a (net long-term capital gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 9a (net long-term capital gain or loss) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 9a. Net Long-Term Capital Gain (Loss), "Report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 659063e0)

## 9a — `k1p.box9a`

- **IRS:** Net long-term capital gain (loss)
- **Encoded (Dollars):** Input — The amount in box 9a, net long-term capital gain (loss). Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 9a, net long-term capital gain (loss). Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 15, Box 9a. Net Long-Term Capital Gain (Loss), "Report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 659063e0)

## (gate) — `k1p.box9a_if_any`

- **Authored helper label:** Box 9a, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 9a shows an amount: net long-term capital gain (loss)" = true → line 9a] [helper "Box 9a shows an amount: net long-term capital gain (loss)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b9a",{"const":true}],"op":"test"},"then":"k1p.box9a"},{"guard":{"eq":["k1p.has_b9a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 9a. Net Long-Term Capital Gain (Loss), "Report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 659063e0)

## (helper) — `k1p.has_b14a`

- **Authored helper label:** Box 14 shows an amount with code A: net earnings from self-employment
- **Encoded (Bool):** Input — Does box 14 show an amount with code A (net earnings from self-employment)?
- Expr: `{"op":"input","source":"Does box 14 show an amount with code A (net earnings from self-employment)?"}`
- Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)

## 14 A — `k1p.box14a`

- **IRS:** Net earnings from self-employment
- **Encoded (Dollars):** Input — The amount in box 14 with code A, net earnings (loss) from self-employment. Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"The amount in box 14 with code A, net earnings (loss) from self-employment. Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)

## (gate) — `k1p.box14a_if_any`

- **Authored helper label:** Box 14 A, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 14 shows an amount with code A: net earnings from self-employment" = true → line 14 A] [helper "Box 14 shows an amount with code A: net earnings from self-employment" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b14a",{"const":true}],"op":"test"},"then":"k1p.box14a"},{"guard":{"eq":["k1p.has_b14a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)

## (helper) — `k1p.has_b15o`

- **Authored helper label:** Box 15 shows an amount with code O: backup withholding
- **Encoded (Bool):** Input — Does box 15 show an amount with code O (backup withholding)?
- Expr: `{"op":"input","source":"Does box 15 show an amount with code O (backup withholding)?"}`
- Cite: [i1065sk1] p. 23, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 659063e0)

## 15 O — `k1p.box15o`

- **IRS:** Backup withholding
- **Encoded (NonNegDollars):** Input — The amount in box 15 with code O, backup withholding.
- Expr: `{"op":"input","source":"The amount in box 15 with code O, backup withholding."}`
- Cite: [i1065sk1] p. 23, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 659063e0)

## (gate) — `k1p.box15o_if_any`

- **Authored helper label:** Box 15 O, asked only when the box shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 15 shows an amount with code O: backup withholding" = true → line 15 O] [helper "Box 15 shows an amount with code O: backup withholding" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b15o",{"const":true}],"op":"test"},"then":"k1p.box15o"},{"guard":{"eq":["k1p.has_b15o",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 23, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 659063e0)

## (helper) — `k1p.has_b18a`

- **Authored helper label:** Box 18 shows an amount with code A: tax-exempt interest income
- **Encoded (Bool):** Input — Does box 18 show an amount with code A (tax-exempt interest income)?
- Expr: `{"op":"input","source":"Does box 18 show an amount with code A (tax-exempt interest income)?"}`
- Cite: [i1065sk1] p. 25, Code A. Tax-exempt interest income, "Individual partners include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 659063e0)

## 18 A — `k1p.box18a`

- **IRS:** Tax-exempt interest income
- **Encoded (NonNegDollars):** Input — The amount in box 18 with code A, tax-exempt interest income.
- Expr: `{"op":"input","source":"The amount in box 18 with code A, tax-exempt interest income."}`
- Cite: [i1065sk1] p. 25, Code A. Tax-exempt interest income, "Individual partners include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 659063e0)

## (gate) — `k1p.box18a_if_any`

- **Authored helper label:** Box 18 A, asked only when the box shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 18 shows an amount with code A: tax-exempt interest income" = true → line 18 A] [helper "Box 18 shows an amount with code A: tax-exempt interest income" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b18a",{"const":true}],"op":"test"},"then":"k1p.box18a"},{"guard":{"eq":["k1p.has_b18a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 25, Code A. Tax-exempt interest income, "Individual partners include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 659063e0)

## (helper) — `k1p.has_b20z`

- **Authored helper label:** Box 20 shows code Z: section 199A information
- **Encoded (Bool):** Input — Does box 20 show code Z (section 199A information)?
- Expr: `{"op":"input","source":"Does box 20 show code Z (section 199A information)?"}`
- Cite: [i1065sk1] p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction" (2025; sha256 659063e0)

## 20 Z — `k1p.box20z`

- **IRS:** Section 199a information
- **Encoded (Dollars):** Input — From the statement for box 20, code Z (section 199A information): the qualified business income (QBI) or loss, all trades or businesses together. Enter a loss as a negative amount.
- Expr: `{"op":"input","source":"From the statement for box 20, code Z (section 199A information): the qualified business income (QBI) or loss, all trades or businesses together. Enter a loss as a negative amount."}`
- Cite: [i1065sk1] p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction" (2025; sha256 659063e0)

## (gate) — `k1p.box20z_if_any`

- **Authored helper label:** Box 20 Z, asked only when the box shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 20 shows code Z: section 199A information" = true → line 20 Z] [helper "Box 20 shows code Z: section 199A information" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b20z",{"const":true}],"op":"test"},"then":"k1p.box20z"},{"guard":{"eq":["k1p.has_b20z",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction" (2025; sha256 659063e0)

## 6b — `k1p.box6b`

- **IRS:** Qualified dividends
- **Encoded (NonNegDollars):** Input — The amount in box 6b, qualified dividends (0 if the box is blank).
- Expr: `{"op":"input","source":"The amount in box 6b, qualified dividends (0 if the box is blank)."}`
- Cite: [i1065sk1] p. 15, Box 6b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 659063e0)

## (gate) — `k1p.box6b_if_any`

- **Authored helper label:** Box 6b, asked only when box 6a shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 6a shows an amount: ordinary dividends" = true → line 6b] [helper "Box 6a shows an amount: ordinary dividends" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b6a",{"const":true}],"op":"test"},"then":"k1p.box6b"},{"guard":{"eq":["k1p.has_b6a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 15, Box 6b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 659063e0)

## (helper) — `k1p.has_b9bc`

- **Authored helper label:** Box 9b or 9c shows an amount
- **Encoded (Bool):** Input — Does box 9b (collectibles 28% gain or loss) or box 9c (unrecaptured section 1250 gain) show an amount?
- Expr: `{"op":"input","source":"Does box 9b (collectibles 28% gain or loss) or box 9c (unrecaptured section 1250 gain) show an amount?"}`
- Cite: [i1065sk1] p. 16, Box 9b. Collectibles (28%) Gain (Loss), "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 659063e0)

## (gate) — `k1p.has_b9bc_if_9a`

- **Authored helper label:** Asked only when box 9a shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 9a shows an amount: net long-term capital gain (loss)" = true → helper "Box 9b or 9c shows an amount"] [helper "Box 9a shows an amount: net long-term capital gain (loss)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b9a",{"const":true}],"op":"test"},"then":"k1p.has_b9bc"},{"guard":{"eq":["k1p.has_b9a",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 16, Box 9b. Collectibles (28%) Gain (Loss), "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 659063e0)

## 9b — `k1p.box9b`

- **IRS:** Collectibles (28%) gain (loss)
- **Encoded (Dollars):** Input — The amount in box 9b, collectibles (28%) gain or loss (a loss as a negative number; 0 if the box is blank).
- Expr: `{"op":"input","source":"The amount in box 9b, collectibles (28%) gain or loss (a loss as a negative number; 0 if the box is blank)."}`
- Cite: [i1065sk1] p. 16, Box 9b. Collectibles (28%) Gain (Loss), "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 659063e0)

## (gate) — `k1p.box9b_if_any`

- **Authored helper label:** Box 9b, asked only when box 9b or 9c shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Asked only when box 9a shows an amount (false otherwise)" = true → line 9b] [helper "Asked only when box 9a shows an amount (false otherwise)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b9bc_if_9a",{"const":true}],"op":"test"},"then":"k1p.box9b"},{"guard":{"eq":["k1p.has_b9bc_if_9a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 16, Box 9b. Collectibles (28%) Gain (Loss), "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 659063e0)

## 9c — `k1p.box9c`

- **IRS:** Unrecaptured section 1250 gain
- **Encoded (NonNegDollars):** Input — The amount in box 9c, unrecaptured section 1250 gain (0 if the box is blank).
- Expr: `{"op":"input","source":"The amount in box 9c, unrecaptured section 1250 gain (0 if the box is blank)."}`
- Cite: [i1065sk1] p. 16, Box 9c. Unrecaptured Section 1250 Gain, "If the partnership reports only unrecaptured section 1250 gain from the sale or exchange of its business assets, it’ll enter a dollar amount in box 9c" (2025; sha256 659063e0)

## (gate) — `k1p.box9c_if_any`

- **Authored helper label:** Box 9c, asked only when box 9b or 9c shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Asked only when box 9a shows an amount (false otherwise)" = true → line 9c] [helper "Asked only when box 9a shows an amount (false otherwise)" = false → helper "Zero"]
- Interpretation: amb.2025.k1p_box9c_business
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b9bc_if_9a",{"const":true}],"op":"test"},"then":"k1p.box9c"},{"guard":{"eq":["k1p.has_b9bc_if_9a",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 16, Box 9c. Unrecaptured Section 1250 Gain, "If the partnership reports only unrecaptured section 1250 gain from the sale or exchange of its business assets, it’ll enter a dollar amount in box 9c" (2025; sha256 659063e0)

## (helper) — `k1p.has_b19`

- **Authored helper label:** Box 19 shows an amount: distributions
- **Encoded (Bool):** Input — Does box 19 (distributions) show an amount?
- Expr: `{"op":"input","source":"Does box 19 (distributions) show an amount?"}`
- Cite: [i1065sk1] p. 25, Box 19. Distributions, "Code A. Cash and marketable securities other than for services" (2025; sha256 659063e0)

## (helper) — `k1p.has_b20ab`

- **Authored helper label:** Box 20 shows code A or B: investment income or expenses
- **Encoded (Bool):** Input — Does box 20 show code A (investment income) or code B (investment expenses)?
- Expr: `{"op":"input","source":"Does box 20 show code A (investment income) or code B (investment expenses)?"}`
- Cite: [i1065sk1] p. 27, Code A. Investment income, "Report this amount on Form 4952, Part II, line 4a" (2025; sha256 659063e0)

## (helper) — `k1p.r_b4b`

- **Authored helper label:** Box 4b shows an amount: guaranteed payments for capital
- **Encoded (Bool):** Input — Does box 4b (guaranteed payments for capital) show an amount?
- Expr: `{"op":"input","source":"Does box 4b (guaranteed payments for capital) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 4b. Guaranteed Payments for Capital, "These are guaranteed payments other than for services" (2025; sha256 659063e0)

## (helper) — `k1p.r_b7`

- **Authored helper label:** Box 7 shows an amount: royalties
- **Encoded (Bool):** Input — Does box 7 (royalties) show an amount?
- Expr: `{"op":"input","source":"Does box 7 (royalties) show an amount?"}`
- Cite: [i1065sk1] p. 15, Box 7. Royalties, "Report royalties on Schedule E (Form 1040), line 4" (2025; sha256 659063e0)

## (helper) — `k1p.r_b10`

- **Authored helper label:** Box 10 shows an amount: net section 1231 gain (loss)
- **Encoded (Bool):** Input — Does box 10 (net section 1231 gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 10 (net section 1231 gain or loss) show an amount?"}`
- Cite: [i1065sk1] p. 16, Box 10. Net Section 1231 Gain (Loss), "report it in column (g) of Form 4797, line 2" (2025; sha256 659063e0)

## (helper) — `k1p.r_b11`

- **Authored helper label:** Box 11 shows an amount: other income (loss)
- **Encoded (Bool):** Input — Does box 11 (other income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 11 (other income or loss) show an amount?"}`
- Cite: [i1065sk1] p. 16, Box 11. Other Income (Loss), "Code A. Other portfolio income (loss)" (2025; sha256 659063e0)

## (helper) — `k1p.r_b12`

- **Authored helper label:** Box 12 shows an amount: section 179 deduction
- **Encoded (Bool):** Input — Does box 12 (section 179 deduction) show an amount?
- Expr: `{"op":"input","source":"Does box 12 (section 179 deduction) show an amount?"}`
- Cite: [i1065sk1] p. 18, Box 12. Section 179 Deduction, "to complete Part I of Form 4562" (2025; sha256 659063e0)

## (helper) — `k1p.r_b13`

- **Authored helper label:** Box 13 shows an amount with a code other than AE
- **Encoded (Bool):** Input — Does box 13 (other deductions) show an amount with any code other than AE?
- Expr: `{"op":"input","source":"Does box 13 (other deductions) show an amount with any code other than AE?"}`
- Cite: [i1065sk1] p. 18, Box 13. Other Deductions, "Codes A through G" (2025; sha256 659063e0)

## (helper) — `k1p.r_b14bc`

- **Authored helper label:** Box 14 shows an amount with code B or C
- **Encoded (Bool):** Input — Does box 14 show an amount with code B (gross farming or fishing income) or code C (gross nonfarm income)?
- Expr: `{"op":"input","source":"Does box 14 show an amount with code B (gross farming or fishing income) or code C (gross nonfarm income)?"}`
- Cite: [i1065sk1] p. 22, Code B. Gross farming or fishing income, "Also use this amount to figure net earnings from self-employment under the farm optional method" (2025; sha256 659063e0)

## (helper) — `k1p.r_b15`

- **Authored helper label:** Box 15 shows an amount with a code other than O
- **Encoded (Bool):** Input — Does box 15 (credits) show an amount with any code other than O?
- Expr: `{"op":"input","source":"Does box 15 (credits) show an amount with any code other than O?"}`
- Cite: [i1065sk1] p. 22, Box 15. Credits, "you must complete Form 8582-CR" (2025; sha256 659063e0)

## (helper) — `k1p.r_b16`

- **Authored helper label:** Box 16 is checked: Schedule K-3 is attached
- **Encoded (Bool):** Input — Is box 16 checked, showing that a Schedule K-3 is attached, or did you get a Schedule K-3 from the partnership?
- Expr: `{"op":"input","source":"Is box 16 checked, showing that a Schedule K-3 is attached, or did you get a Schedule K-3 from the partnership?"}`
- Cite: [i1065sk1] p. 24, Box 16. International Transactions, "If the partnership checked the box, see the attached Schedule K-3" (2025; sha256 659063e0)

## (helper) — `k1p.r_b17`

- **Authored helper label:** Box 17 shows an amount: alternative minimum tax items
- **Encoded (Bool):** Input — Does box 17 (alternative minimum tax items) show an amount?
- Expr: `{"op":"input","source":"Does box 17 (alternative minimum tax items) show an amount?"}`
- Cite: [i1065sk1] p. 24, Box 17. Alternative Minimum Tax (AMT) Items, "to prepare your Form 6251" (2025; sha256 659063e0)

## (helper) — `k1p.r_b20`

- **Authored helper label:** Box 20 shows a code other than A, B, N, Z or AG
- **Encoded (Bool):** Input — Does box 20 show any code other than A, B, N, Z or AG?
- Expr: `{"op":"input","source":"Does box 20 show any code other than A, B, N, Z or AG?"}`
- Cite: [i1065sk1] p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction" (2025; sha256 659063e0)

## (helper) — `k1p.r_b21`

- **Authored helper label:** Box 21 shows an amount: foreign taxes paid or accrued
- **Encoded (Bool):** Input — Does box 21 (foreign taxes paid or accrued) show an amount?
- Expr: `{"op":"input","source":"Does box 21 (foreign taxes paid or accrued) show an amount?"}`
- Cite: [i1065sk1] p. 32, Box 21. Foreign Taxes Paid or Accrued, "Foreign taxes paid or accrued reduce a partner’s basis" (2025; sha256 659063e0)

## (helper) — `k1p.r_b2223`

- **Authored helper label:** Box 22 or box 23 is checked: more than one activity
- **Encoded (Bool):** Input — Is box 22 or box 23 checked, showing more than one activity (with a statement attached)?
- Expr: `{"op":"input","source":"Is box 22 or box 23 checked, showing more than one activity (with a statement attached)?"}`
- Cite: [i1065sk1] p. 9, Material participation, "If the partnership had more than one activity, it’ll attach a statement to your Schedule K-1 that identifies each activity" (2025; sha256 659063e0)

## (helper) — `k1p.r_foreign`

- **Authored helper label:** The partnership is a foreign partnership
- **Encoded (Bool):** Input — Is it a foreign partnership (one not created or organized in the United States; one organized in Puerto Rico or another U.S. territory is foreign)?
- Expr: `{"op":"input","source":"Is it a foreign partnership (one not created or organized in the United States; one organized in Puerto Rico or another U.S. territory is foreign)?"}`
- Cite: [i1040se] p. 9, Foreign Partnerships, "you may have to file Form 8865" (2025; sha256 ad71de35)

## (helper) — `k1p.r_disposed`

- **Authored helper label:** You sold or gave up any of your share in 2025
- **Encoded (Bool):** Input — In 2025, did you sell, trade or give up any of your share of this partnership?
- Expr: `{"op":"input","source":"In 2025, did you sell, trade or give up any of your share of this partnership?"}`
- Cite: [i1065sk1] p. 2, Sale or Exchange of Partnership Interest, "Generally, a partner who sells or exchanges a partnership interest" (2025; sha256 659063e0)

## (helper) — `k1p.upe`

- **Authored helper label:** Unreimbursed partnership expenses paid under the partnership agreement
- **Encoded (Bool):** Input — Did you pay, without being paid back, partnership expenses that the partnership agreement required you to pay?
- Expr: `{"op":"input","source":"Did you pay, without being paid back, partnership expenses that the partnership agreement required you to pay?"}`
- Cite: [i1040se] p. 10, Unreimbursed Partnership Expenses, "You can deduct unreimbursed ordinary and necessary partnership expenses you paid on behalf of the partnership on Schedule E if you were required to pay these expenses under the partnership agreement" (2025; sha256 ad71de35)

## (helper) — `k1p.interest_buy`

- **Authored helper label:** Interest on money borrowed to buy the interest or put capital into the partnership (debt-financed acquisition)
- **Encoded (Bool):** Input — Did you pay interest in 2025 on money borrowed to buy your share or put money into the partnership?
- Expr: `{"op":"input","source":"Did you pay interest in 2025 on money borrowed to buy your share or put money into the partnership?"}`
- Cite: [i1040se] p. 9, Domestic Partnerships, "If you used loan proceeds to buy an interest in, or make a contribution to the capital of, a partnership (debt-financed acquisition), report your share of deductible partnership interest expense on either Schedule A or Schedule E" (2025; sha256 ad71de35)

## (helper) — `k1p.fiscal`

- **Authored helper label:** The K-1 is for a tax year other than calendar year 2025 (a fiscal year)
- **Encoded (Bool):** Input — Is the tax year at the top of this Schedule K-1 something other than the calendar year 2025 (a fiscal year)?
- Expr: `{"op":"input","source":"Is the tax year at the top of this Schedule K-1 something other than the calendar year 2025 (a fiscal year)?"}`
- Cite: [i1065sk1] p. 13, "If you file your tax return on a calendar-year basis, but your partnership files a return for a fiscal year, report the amounts on your tax return for the year in which the partnership's fiscal year ends"; p. 9, "All determinations of material participation are based on your participation during the partnership’s tax year" (2025; sha256 659063e0)

## (helper) — `k1p.oil_gas_gp`

- **Authored helper label:** A working interest in oil or gas wells held through the partnership as a general partner (nonpassive)
- **Encoded (Bool):** Input — As a general partner, do you hold a working interest in oil or gas wells through this partnership?
- Expr: `{"op":"input","source":"As a general partner, do you hold a working interest in oil or gas wells through this partnership?"}`
- Cite: [i1065sk1] p. 8, Passive activities don't include the following, "Working interests in oil or gas wells if you were a general partner" (2025; sha256 659063e0)

## (gate) — `k1p.oil_gas_gp_if_gp`

- **Authored helper label:** Asked only when item G's first box (general partner or LLC member-manager) is checked (false otherwise)
- **Encoded (Bool):** Choose — [helper "General partner or LLC member-manager (item G)" = true → helper "A working interest in oil or gas wells held through the partnership as a general partner (nonpassive)"] [helper "General partner or LLC member-manager (item G)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.general",{"const":true}],"op":"test"},"then":"k1p.oil_gas_gp"},{"guard":{"eq":["k1p.general",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 8, Passive activities don't include the following, "Working interests in oil or gas wells if you were a general partner" (2025; sha256 659063e0)

## (helper) — `k1p.b19_other`

- **Authored helper label:** Box 19 shows a code other than A
- **Encoded (Bool):** Input — Does box 19 show any code other than A (cash and marketable securities)?
- Expr: `{"op":"input","source":"Does box 19 show any code other than A (cash and marketable securities)?"}`
- Cite: [i1065sk1] p. 25, Box 19. Distributions, "Code A. Cash and marketable securities other than for services" (2025; sha256 659063e0)

## (gate) — `k1p.b19_other_if_any`

- **Authored helper label:** Asked only when box 19 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 19 shows an amount: distributions" = true → helper "Box 19 shows a code other than A"] [helper "Box 19 shows an amount: distributions" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b19",{"const":true}],"op":"test"},"then":"k1p.b19_other"},{"guard":{"eq":["k1p.has_b19",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 25, Box 19. Distributions, "Code A. Cash and marketable securities other than for services" (2025; sha256 659063e0)

## (helper) — `k1p.dist_over`

- **Authored helper label:** Distributions more than basis
- **Encoded (Bool):** Input — Was the money or marketable securities you took out of it in 2025 (box 19), with any fall in your share of its debts (item K), more than your basis in it just before you took it out?
- Expr: `{"op":"input","source":"Was the money or marketable securities you took out of it in 2025 (box 19), with any fall in your share of its debts (item K), more than your basis in it just before you took it out?"}`
- Cite: [i1065sk1] p. 25, Box 19. Distributions, "exceed the adjusted basis of your partnership interest immediately before the distribution, the excess is treated as gain from the sale or exchange of your partnership interest" (2025; sha256 659063e0)

## (gate) — `k1p.dist_over_if_any`

- **Authored helper label:** Asked only when box 19 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 19 shows an amount: distributions" = true → helper "Distributions more than basis"] [helper "Box 19 shows an amount: distributions" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b19",{"const":true}],"op":"test"},"then":"k1p.dist_over"},{"guard":{"eq":["k1p.has_b19",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 25, Box 19. Distributions, "exceed the adjusted basis of your partnership interest immediately before the distribution, the excess is treated as gain from the sale or exchange of your partnership interest" (2025; sha256 659063e0)

## (helper) — `k1p.z_other`

- **Authored helper label:** Section 199A statement shows section 199A dividends or a cooperative
- **Encoded (Bool):** Input — Does the statement for code Z show section 199A dividends, or anything about a farm or garden (agricultural or horticultural) cooperative, such as payments from it or a section 199A(g) deduction?
- Expr: `{"op":"input","source":"Does the statement for code Z show section 199A dividends, or anything about a farm or garden (agricultural or horticultural) cooperative, such as payments from it or a section 199A(g) deduction?"}`
- Cite: [i1065sk1] p. 30, Section 199A dividends, "The amount reported reflects your distributive share of the partnership’s net section 199A dividends" (2025; sha256 659063e0)

## (gate) — `k1p.z_other_if_z`

- **Authored helper label:** Asked only when box 20 shows code Z (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 20 shows code Z: section 199A information" = true → helper "Section 199A statement shows section 199A dividends or a cooperative"] [helper "Box 20 shows code Z: section 199A information" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b20z",{"const":true}],"op":"test"},"then":"k1p.z_other"},{"guard":{"eq":["k1p.has_b20z",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 30, Section 199A dividends, "The amount reported reflects your distributive share of the partnership’s net section 199A dividends" (2025; sha256 659063e0)

## (helper) — `k1p.trader`

- **Authored helper label:** The partnership's business is trading investments
- **Encoded (Bool):** Input — Is the partnership's business trading stocks, commodities or other investments for its owners?
- Expr: `{"op":"input","source":"Is the partnership's business trading stocks, commodities or other investments for its owners?"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "Trading personal property for the account of owners of interests in the activity" (2025; sha256 659063e0)

## (gate) — `k1p.trader_if_b1`

- **Authored helper label:** Asked only when box 1 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows an amount: ordinary business income (loss)" = true → helper "The partnership's business is trading investments"] [helper "Box 1 shows an amount: ordinary business income (loss)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b1",{"const":true}],"op":"test"},"then":"k1p.trader"},{"guard":{"eq":["k1p.has_b1",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "Trading personal property for the account of owners of interests in the activity" (2025; sha256 659063e0)

## (helper) — `k1p.work`

- **Authored helper label:** Worked in the business in 2025
- **Encoded (Bool):** Input — In 2025, did you (or your spouse, whether or not you file jointly) do any work in the partnership's business?
- Expr: `{"op":"input","source":"In 2025, did you (or your spouse, whether or not you file jointly) do any work in the partnership's business?"}`
- Cite: [i1065sk1] p. 9, Work counted toward material participation, "any work that you or your spouse does in connection with an activity held through a partnership" (2025; sha256 659063e0)

## (gate) — `k1p.work_if_b1`

- **Authored helper label:** Asked only when box 1 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows an amount: ordinary business income (loss)" = true → helper "Worked in the business in 2025"] [helper "Box 1 shows an amount: ordinary business income (loss)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.has_b1",{"const":true}],"op":"test"},"then":"k1p.work"},{"guard":{"eq":["k1p.has_b1",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Work counted toward material participation, "any work that you or your spouse does in connection with an activity held through a partnership" (2025; sha256 659063e0)

## (helper) — `k1p.hours500`

- **Authored helper label:** More than 500 hours (test 1)
- **Encoded (Bool):** Input — Did that work add up to more than 500 hours in 2025?
- Expr: `{"op":"input","source":"Did that work add up to more than 500 hours in 2025?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 659063e0)

## (gate) — `k1p.hours500_if_work`

- **Authored helper label:** Asked only of a partner who worked in the business (false otherwise)
- **Encoded (Bool):** Choose — [helper "Asked only when box 1 shows an amount (false otherwise)" = true → helper "More than 500 hours (test 1)"] [helper "Asked only when box 1 shows an amount (false otherwise)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.work_if_b1",{"const":true}],"op":"test"},"then":"k1p.hours500"},{"guard":{"eq":["k1p.work_if_b1",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 659063e0)

## (helper) — `k1p.under500`

- **Authored helper label:** Worked in the business, 500 hours or less
- **Encoded (Bool):** helper "Asked only when box 1 shows an amount (false otherwise)" = true and helper "Asked only of a partner who worked in the business (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1p.work_if_b1",{"const":true}],"op":"test"},{"eq":["k1p.hours500_if_work",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Material participation, "You must determine if you materially participated (a) in each trade or business activity held through the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.gp_under500`

- **Authored helper label:** A general partner who worked 500 hours or less
- **Encoded (Bool):** helper "Worked in the business, 500 hours or less" = true and helper "General partner or LLC member-manager (item G)" = true
- Expr: `{"all":[{"eq":["k1p.under500",{"const":true}],"op":"test"},{"eq":["k1p.general",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Limited partners, "If you’re a limited partner, you must meet item 1, 5, or 6 above to qualify as having materially participated" (2025; sha256 659063e0)

## (helper) — `k1p.most_hours`

- **Authored helper label:** More than 100 hours and no one worked more (test 3)
- **Encoded (Bool):** Input — Did you (or your spouse, whether or not you file jointly) work in it more than 100 hours in 2025, and at least as many hours as anyone else, employees included?
- Expr: `{"op":"input","source":"Did you (or your spouse, whether or not you file jointly) work in it more than 100 hours in 2025, and at least as many hours as anyone else, employees included?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You participated in the activity for more than 100 hours during the tax year, and your participation in the activity for the tax year wasn’t less than the participation in the activity of any other individual" (2025; sha256 659063e0)

## (gate) — `k1p.most_hours_if_gp`

- **Authored helper label:** Asked only of a general partner who worked 500 hours or less (false otherwise)
- **Encoded (Bool):** Choose — [helper "A general partner who worked 500 hours or less" = true → helper "More than 100 hours and no one worked more (test 3)"] [helper "A general partner who worked 500 hours or less" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.gp_under500",{"const":true}],"op":"test"},"then":"k1p.most_hours"},{"guard":{"eq":["k1p.gp_under500",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You participated in the activity for more than 100 hours during the tax year, and your participation in the activity for the tax year wasn’t less than the participation in the activity of any other individual" (2025; sha256 659063e0)

## (helper) — `k1p.ask_nearly_all`

- **Authored helper label:** A general partner who worked 500 hours or less and less than someone else
- **Encoded (Bool):** helper "A general partner who worked 500 hours or less" = true and helper "Asked only of a general partner who worked 500 hours or less (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1p.gp_under500",{"const":true}],"op":"test"},{"eq":["k1p.most_hours_if_gp",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "constituted substantially all the participation in the activity of all individuals" (2025; sha256 659063e0)

## (helper) — `k1p.nearly_all`

- **Authored helper label:** Substantially all the work (test 2)
- **Encoded (Bool):** Input — Did you (and your spouse, whether or not you file jointly) do nearly all of the work in it in 2025, counting the work of employees and anyone else?
- Expr: `{"op":"input","source":"Did you (and your spouse, whether or not you file jointly) do nearly all of the work in it in 2025, counting the work of employees and anyone else?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "constituted substantially all the participation in the activity of all individuals" (2025; sha256 659063e0)

## (gate) — `k1p.nearly_all_if_asked`

- **Authored helper label:** Asked only when test 3 is not met (false otherwise)
- **Encoded (Bool):** Choose — [helper "A general partner who worked 500 hours or less and less than someone else" = true → helper "Substantially all the work (test 2)"] [helper "A general partner who worked 500 hours or less and less than someone else" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_nearly_all",{"const":true}],"op":"test"},"then":"k1p.nearly_all"},{"guard":{"eq":["k1p.ask_nearly_all",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "constituted substantially all the participation in the activity of all individuals" (2025; sha256 659063e0)

## (helper) — `k1p.ask_five`

- **Authored helper label:** Box 1 shows an amount and tests 1, 2 and 3 are not met (no work in 2025 is needed for tests 5 and 6)
- **Encoded (Bool):** helper "Box 1 shows an amount: ordinary business income (loss)" = true and helper "Asked only of a partner who worked in the business (false otherwise)" = false and helper "Asked only of a general partner who worked 500 hours or less (false otherwise)" = false and helper "Asked only when test 3 is not met (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1p.has_b1",{"const":true}],"op":"test"},{"eq":["k1p.hours500_if_work",{"const":false}],"op":"test"},{"eq":["k1p.most_hours_if_gp",{"const":false}],"op":"test"},{"eq":["k1p.nearly_all_if_asked",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year" (2025; sha256 659063e0)

## (helper) — `k1p.five_of_ten`

- **Authored helper label:** Materially participated in 5 of the 10 preceding years (test 5)
- **Encoded (Bool):** Input — In at least 5 of the years 2015 to 2024, did you (or your spouse, whether or not you file jointly) materially participate in this business?
- Expr: `{"op":"input","source":"In at least 5 of the years 2015 to 2024, did you (or your spouse, whether or not you file jointly) materially participate in this business?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year" (2025; sha256 659063e0)

## (gate) — `k1p.five_of_ten_if_asked`

- **Authored helper label:** Asked only when box 1 shows an amount and tests 1 to 3 are not met (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows an amount and tests 1, 2 and 3 are not met (no work in 2025 is needed for tests 5 and 6)" = true → helper "Materially participated in 5 of the 10 preceding years (test 5)"] [helper "Box 1 shows an amount and tests 1, 2 and 3 are not met (no work in 2025 is needed for tests 5 and 6)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_five",{"const":true}],"op":"test"},"then":"k1p.five_of_ten"},{"guard":{"eq":["k1p.ask_five",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year" (2025; sha256 659063e0)

## (helper) — `k1p.ask_other`

- **Authored helper label:** Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met
- **Encoded (Bool):** helper "Box 1 shows an amount and tests 1, 2 and 3 are not met (no work in 2025 is needed for tests 5 and 6)" = true and helper "Asked only when box 1 shows an amount and tests 1 to 3 are not met (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1p.ask_five",{"const":true}],"op":"test"},{"eq":["k1p.five_of_ten_if_asked",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Material participation, "You must determine if you materially participated (a) in each trade or business activity held through the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.t6`

- **Authored helper label:** Personal service activity, 3 earlier years (test 6)
- **Encoded (Bool):** Input — Is it a service business (health, law, engineering, architecture, accounting, actuarial science, performing arts, consulting, or any other business in which capital is not a major source of income) in which you (or your spouse, whether or not you file jointly) materially participated in any 3 earlier years?
- Expr: `{"op":"input","source":"Is it a service business (health, law, engineering, architecture, accounting, actuarial science, performing arts, consulting, or any other business in which capital is not a major source of income) in which you (or your spouse, whether or not you file jointly) materially participated in any 3 earlier years?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a personal service activity and you materially participated in the activity for any 3 tax years" (2025; sha256 659063e0)

## (gate) — `k1p.t6_if_asked`

- **Authored helper label:** Asked only when tests 1, 2, 3 and 5 are not met (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met" = true → helper "Personal service activity, 3 earlier years (test 6)"] [helper "Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_other",{"const":true}],"op":"test"},"then":"k1p.t6"},{"guard":{"eq":["k1p.ask_other",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a personal service activity and you materially participated in the activity for any 3 tax years" (2025; sha256 659063e0)

## (helper) — `k1p.ask_other_gp`

- **Authored helper label:** A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5
- **Encoded (Bool):** helper "Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met" = true and helper "Asked only when box 1 shows an amount (false otherwise)" = true and helper "General partner or LLC member-manager (item G)" = true
- Expr: `{"all":[{"eq":["k1p.ask_other",{"const":true}],"op":"test"},{"eq":["k1p.work_if_b1",{"const":true}],"op":"test"},{"eq":["k1p.general",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Limited partners, "If you’re a limited partner, you must meet item 1, 5, or 6 above to qualify as having materially participated" (2025; sha256 659063e0)

## (helper) — `k1p.t4`

- **Authored helper label:** Significant participation activities over 500 hours (test 4)
- **Encoded (Bool):** Input — In 2025, did your work (with your spouse's, whether or not you file jointly) in it and in other businesses where you worked over 100 hours add up to over 500 hours?
- Expr: `{"op":"input","source":"In 2025, did your work (with your spouse's, whether or not you file jointly) in it and in other businesses where you worked over 100 hours add up to over 500 hours?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a significant participation activity for the tax year" (2025; sha256 659063e0)

## (gate) — `k1p.t4_if_gp`

- **Authored helper label:** Asked only of a general partner who worked in the business and met none of tests 1, 2, 3 and 5 (false otherwise)
- **Encoded (Bool):** Choose — [helper "A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5" = true → helper "Significant participation activities over 500 hours (test 4)"] [helper "A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_other_gp",{"const":true}],"op":"test"},"then":"k1p.t4"},{"guard":{"eq":["k1p.ask_other_gp",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a significant participation activity for the tax year" (2025; sha256 659063e0)

## (helper) — `k1p.t7`

- **Authored helper label:** Regular, continuous and substantial participation (test 7)
- **Encoded (Bool):** Input — Did you (or your spouse, whether or not you file jointly) work in it in 2025 on a regular, continuous and substantial basis, for more than 100 hours?
- Expr: `{"op":"input","source":"Did you (or your spouse, whether or not you file jointly) work in it in 2025 on a regular, continuous and substantial basis, for more than 100 hours?"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "Based on all the facts and circumstances, you participated in the activity on a regular, continuous, and substantial basis during the tax year" (2025; sha256 659063e0)

## (gate) — `k1p.t7_if_gp`

- **Authored helper label:** Asked only of a general partner who worked in the business and met none of tests 1, 2, 3 and 5 (false otherwise)
- **Encoded (Bool):** Choose — [helper "A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5" = true → helper "Regular, continuous and substantial participation (test 7)"] [helper "A general partner who worked in the business in 2025 and met none of tests 1, 2, 3 and 5" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_other_gp",{"const":true}],"op":"test"},"then":"k1p.t7"},{"guard":{"eq":["k1p.ask_other_gp",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "Based on all the facts and circumstances, you participated in the activity on a regular, continuous, and substantial basis during the tax year" (2025; sha256 659063e0)

## (helper) — `k1p.over100`

- **Authored helper label:** More than 100 hours in the business without material participation (a significant participation activity)
- **Encoded (Bool):** Input — Did you (or your spouse, whether or not you file jointly) work in it more than 100 hours in 2025?
- Expr: `{"op":"input","source":"Did you (or your spouse, whether or not you file jointly) work in it more than 100 hours in 2025?"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "If you have net income subject to recharacterization under Temporary Regulations section 1.469-2T(f) and Regulations sections 1.469-2(f)(5) and (6), report such amounts according to the Instructions for Form 8582"; p. 9, "A significant participation activity is any trade or business activity in which you participated for more than 100 hours during the year and in which you didn’t materially participate" (2025; sha256 659063e0)

## (gate) — `k1p.ask_sp`

- **Authored helper label:** Box 1 shows income, the partner worked in the business, and none of tests 1, 2, 3 and 5 is met
- **Encoded (Bool):** helper "Box 1 shows an amount and none of tests 1, 2, 3 and 5 is met" = true and helper "Asked only when box 1 shows an amount (false otherwise)" = true and helper "Box 1, asked only when the box shows an amount (zero otherwise)" > $0
- Expr: `{"all":[{"eq":["k1p.ask_other",{"const":true}],"op":"test"},{"eq":["k1p.work_if_b1",{"const":true}],"op":"test"},{"gt":["k1p.box1_if_any",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "If you have net income subject to recharacterization under Temporary Regulations section 1.469-2T(f) and Regulations sections 1.469-2(f)(5) and (6), report such amounts according to the Instructions for Form 8582"; p. 9, "A significant participation activity is any trade or business activity in which you participated for more than 100 hours during the year and in which you didn’t materially participate" (2025; sha256 659063e0)

## (gate) — `k1p.over100_if_income`

- **Authored helper label:** Asked only when box 1 shows income from a business the partner worked in without meeting tests 1, 2, 3 or 5 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows income, the partner worked in the business, and none of tests 1, 2, 3 and 5 is met" = true → helper "More than 100 hours in the business without material participation (a significant participation activity)"] [helper "Box 1 shows income, the partner worked in the business, and none of tests 1, 2, 3 and 5 is met" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_sp",{"const":true}],"op":"test"},"then":"k1p.over100"},{"guard":{"eq":["k1p.ask_sp",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "If you have net income subject to recharacterization under Temporary Regulations section 1.469-2T(f) and Regulations sections 1.469-2(f)(5) and (6), report such amounts according to the Instructions for Form 8582"; p. 9, "A significant participation activity is any trade or business activity in which you participated for more than 100 hours during the year and in which you didn’t materially participate" (2025; sha256 659063e0)

## (helper) — `k1p.material`

- **Authored helper label:** Materially participated in the trade or business (box 1) by test 1, 2, 3 or 5
- **Encoded (Bool):** (helper "Asked only of a partner who worked in the business (false otherwise)" = true or helper "Asked only of a general partner who worked 500 hours or less (false otherwise)" = true or helper "Asked only when test 3 is not met (false otherwise)" = true or helper "Asked only when box 1 shows an amount and tests 1 to 3 are not met (false otherwise)" = true)
- Interpretation: amb.2025.k1p_material_tests
- Expr: `{"any":[{"eq":["k1p.hours500_if_work",{"const":true}],"op":"test"},{"eq":["k1p.most_hours_if_gp",{"const":true}],"op":"test"},{"eq":["k1p.nearly_all_if_asked",{"const":true}],"op":"test"},{"eq":["k1p.five_of_ten_if_asked",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Material participation, "You must determine if you materially participated (a) in each trade or business activity held through the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.ask_active`

- **Authored helper label:** Box 2 shows an amount and the partner is a general partner
- **Encoded (Bool):** helper "Box 2 shows an amount: net rental real estate income (loss)" = true and helper "General partner or LLC member-manager (item G)" = true
- Expr: `{"all":[{"eq":["k1p.has_b2",{"const":true}],"op":"test"},{"eq":["k1p.general",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 11, Special allowance for a rental real estate activity, "Limited partners can’t actively participate unless future regulations provide an exception" (2025; sha256 659063e0)

## (helper) — `k1p.decisions`

- **Authored helper label:** Helped make management decisions for the rental real estate
- **Encoded (Bool):** Input — Did you (or your spouse, whether or not you file jointly) help make decisions for its rental real estate in 2025, such as approving tenants, rents or repairs?
- Expr: `{"op":"input","source":"Did you (or your spouse, whether or not you file jointly) help make decisions for its rental real estate in 2025, such as approving tenants, rents or repairs?"}`
- Cite: [i1065sk1] p. 11, Special allowance for a rental real estate activity, "Management decisions that can count as active participation include approving new tenants, deciding rental terms, approving capital or repair expenditures" (2025; sha256 659063e0)

## (gate) — `k1p.decisions_if_asked`

- **Authored helper label:** Asked only of a general partner with an amount in box 2 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 2 shows an amount and the partner is a general partner" = true → helper "Helped make management decisions for the rental real estate"] [helper "Box 2 shows an amount and the partner is a general partner" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_active",{"const":true}],"op":"test"},"then":"k1p.decisions"},{"guard":{"eq":["k1p.ask_active",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 11, Special allowance for a rental real estate activity, "Management decisions that can count as active participation include approving new tenants, deciding rental terms, approving capital or repair expenditures" (2025; sha256 659063e0)

## (helper) — `k1p.tenth`

- **Authored helper label:** Owned at least 10% by value all year
- **Encoded (Bool):** Input — All through 2025, did you (and your spouse, whether or not you file jointly) own at least a tenth (by value) of all the interests in that rental real estate?
- Expr: `{"op":"input","source":"All through 2025, did you (and your spouse, whether or not you file jointly) own at least a tenth (by value) of all the interests in that rental real estate?"}`
- Cite: [i1065sk1] p. 11, Special allowance for a rental real estate activity, "your interest (including your spouse’s interest) in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 659063e0)

## (gate) — `k1p.tenth_if_decisions`

- **Authored helper label:** Asked only when the partner helped make management decisions (false otherwise)
- **Encoded (Bool):** Choose — [helper "Asked only of a general partner with an amount in box 2 (false otherwise)" = true → helper "Owned at least 10% by value all year"] [helper "Asked only of a general partner with an amount in box 2 (false otherwise)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.decisions_if_asked",{"const":true}],"op":"test"},"then":"k1p.tenth"},{"guard":{"eq":["k1p.decisions_if_asked",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 11, Special allowance for a rental real estate activity, "your interest (including your spouse’s interest) in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 659063e0)

## (helper) — `k1p.active`

- **Authored helper label:** Actively participated in the rental real estate activity (box 2): Part IV of Form 8582
- **Encoded (Bool):** helper "Asked only of a general partner with an amount in box 2 (false otherwise)" = true and helper "Asked only when the partner helped make management decisions (false otherwise)" = true
- Expr: `{"all":[{"eq":["k1p.decisions_if_asked",{"const":true}],"op":"test"},{"eq":["k1p.tenth_if_decisions",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1p.re_pro`

- **Authored helper label:** Real estate professional (box 2 may be nonpassive)
- **Encoded (Bool):** Input — Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all your work time?
- Expr: `{"op":"input","source":"Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all your work time?"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity if you were a real estate professional (defined earlier) and you materially participated in the activity" (2025; sha256 659063e0)

## (helper) — `k1p.ask_re_pro`

- **Authored helper label:** Box 2 shows an amount and no rental or royalty of your own is listed
- **Encoded (Bool):** helper "Box 2 shows an amount: net rental real estate income (loss)" = true and scope helper "In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?" = false
- Expr: `{"all":[{"eq":["k1p.has_b2",{"const":true}],"op":"test"},{"eq":["scope.rental",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity if you were a real estate professional (defined earlier) and you materially participated in the activity" (2025; sha256 659063e0)

## (gate) — `k1p.re_pro_if_b2`

- **Authored helper label:** Asked only when box 2 shows an amount and no rental or royalty of your own is listed (false otherwise; Schedule E Part I asks it then, and a Yes there refuses the return)
- **Encoded (Bool):** Choose — [helper "Box 2 shows an amount and no rental or royalty of your own is listed" = true → helper "Real estate professional (box 2 may be nonpassive)"] [helper "Box 2 shows an amount and no rental or royalty of your own is listed" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_re_pro",{"const":true}],"op":"test"},"then":"k1p.re_pro"},{"guard":{"eq":["k1p.ask_re_pro",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity if you were a real estate professional (defined earlier) and you materially participated in the activity" (2025; sha256 659063e0)

## (helper) — `k1p.dwelling`

- **Authored helper label:** A rented home used personally by a partner beyond the greater of 14 days or 10% of the fair-rental days
- **Encoded (Bool):** Input — In 2025, did you or another partner use one of its rental homes personally for over 14 days and over a tenth of the days it was rented at a fair price?
- Expr: `{"op":"input","source":"In 2025, did you or another partner use one of its rental homes personally for over 14 days and over a tenth of the days it was rented at a fair price?"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "The rental of a dwelling unit any partner used for personal purposes during the year for more than the greater of 14 days or 10% of the number of days that the residence was rented at fair rental value" (2025; sha256 659063e0)

## (helper) — `k1p.ask_dwelling`

- **Authored helper label:** Box 2 or box 3 shows an amount
- **Encoded (Bool):** (helper "Box 2 shows an amount: net rental real estate income (loss)" = true or helper "Box 3 shows an amount: other net rental income (loss)" = true)
- Expr: `{"any":[{"eq":["k1p.has_b2",{"const":true}],"op":"test"},{"eq":["k1p.has_b3",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "The rental of a dwelling unit any partner used for personal purposes during the year for more than the greater of 14 days or 10% of the number of days that the residence was rented at fair rental value" (2025; sha256 659063e0)

## (gate) — `k1p.dwelling_if_rent`

- **Authored helper label:** Asked only when box 2 or box 3 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 2 or box 3 shows an amount" = true → helper "A rented home used personally by a partner beyond the greater of 14 days or 10% of the fair-rental days"] [helper "Box 2 or box 3 shows an amount" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_dwelling",{"const":true}],"op":"test"},"then":"k1p.dwelling"},{"guard":{"eq":["k1p.ask_dwelling",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 11, Special rules for certain other activities, "The rental of a dwelling unit any partner used for personal purposes during the year for more than the greater of 14 days or 10% of the number of days that the residence was rented at fair rental value" (2025; sha256 659063e0)

## (helper) — `k1p.prior_any`

- **Authored helper label:** A loss from this partnership held back on an earlier return
- **Encoded (Bool):** Input — Was a loss from this partnership held back (not deducted) on your 2024 return or an earlier one, because of the passive activity rules?
- Interpretation: amb.2025.k1p_prior_with_activity
- Expr: `{"op":"input","source":"Was a loss from this partnership held back (not deducted) on your 2024 return or an earlier one, because of the passive activity rules?"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b1_any`

- **Authored helper label:** Held-back loss from the business (box 1)
- **Encoded (Bool):** Input — Was any of that held-back loss from the business (box 1)?
- Expr: `{"op":"input","source":"Was any of that held-back loss from the business (box 1)?"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b1_any_if`

- **Authored helper label:** Asked only when a loss was held back (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss from this partnership held back on an earlier return" = true → helper "Held-back loss from the business (box 1)"] [helper "A loss from this partnership held back on an earlier return" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_any",{"const":true}],"op":"test"},"then":"k1p.prior_b1_any"},{"guard":{"eq":["k1p.prior_any",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b1`

- **Authored helper label:** Prior years unallowed loss, the business (box 1)
- **Encoded (NonNegDollars):** Input — The loss held back from the business (box 1), from your 2024 Form 8582, Part VII, column (c)
- Expr: `{"op":"input","source":"The loss held back from the business (box 1), from your 2024 Form 8582, Part VII, column (c)"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b1_if`

- **Authored helper label:** Asked only when a loss was held back from it (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Asked only when a loss was held back (false otherwise)" = true → helper "Prior years unallowed loss, the business (box 1)"] [helper "Asked only when a loss was held back (false otherwise)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_b1_any_if",{"const":true}],"op":"test"},"then":"k1p.prior_b1"},{"guard":{"eq":["k1p.prior_b1_any_if",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b2_any`

- **Authored helper label:** Held-back loss from rental real estate (box 2)
- **Encoded (Bool):** Input — Was any of that held-back loss from rental real estate (box 2)?
- Expr: `{"op":"input","source":"Was any of that held-back loss from rental real estate (box 2)?"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b2_any_if`

- **Authored helper label:** Asked only when a loss was held back (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss from this partnership held back on an earlier return" = true → helper "Held-back loss from rental real estate (box 2)"] [helper "A loss from this partnership held back on an earlier return" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_any",{"const":true}],"op":"test"},"then":"k1p.prior_b2_any"},{"guard":{"eq":["k1p.prior_any",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b2`

- **Authored helper label:** Prior years unallowed loss, rental real estate (box 2)
- **Encoded (NonNegDollars):** Input — The loss held back from rental real estate (box 2), from your 2024 Form 8582, Part VII, column (c)
- Expr: `{"op":"input","source":"The loss held back from rental real estate (box 2), from your 2024 Form 8582, Part VII, column (c)"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b2_if`

- **Authored helper label:** Asked only when a loss was held back from it (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Asked only when a loss was held back (false otherwise)" = true → helper "Prior years unallowed loss, rental real estate (box 2)"] [helper "Asked only when a loss was held back (false otherwise)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_b2_any_if",{"const":true}],"op":"test"},"then":"k1p.prior_b2"},{"guard":{"eq":["k1p.prior_b2_any_if",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b3_any`

- **Authored helper label:** Held-back loss from other rentals (box 3)
- **Encoded (Bool):** Input — Was any of that held-back loss from other rentals (box 3)?
- Expr: `{"op":"input","source":"Was any of that held-back loss from other rentals (box 3)?"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b3_any_if`

- **Authored helper label:** Asked only when a loss was held back (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss from this partnership held back on an earlier return" = true → helper "Held-back loss from other rentals (box 3)"] [helper "A loss from this partnership held back on an earlier return" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_any",{"const":true}],"op":"test"},"then":"k1p.prior_b3_any"},{"guard":{"eq":["k1p.prior_any",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.prior_b3`

- **Authored helper label:** Prior years unallowed loss, other rentals (box 3)
- **Encoded (NonNegDollars):** Input — The loss held back from other rentals (box 3), from your 2024 Form 8582, Part VII, column (c)
- Expr: `{"op":"input","source":"The loss held back from other rentals (box 3), from your 2024 Form 8582, Part VII, column (c)"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `k1p.prior_b3_if`

- **Authored helper label:** Asked only when a loss was held back from it (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Asked only when a loss was held back (false otherwise)" = true → helper "Prior years unallowed loss, other rentals (box 3)"] [helper "Asked only when a loss was held back (false otherwise)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.prior_b3_any_if",{"const":true}],"op":"test"},"then":"k1p.prior_b3"},{"guard":{"eq":["k1p.prior_b3_any_if",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.former_passive`

- **Authored helper label:** A held-back loss from a business (box 1) the partner now materially participates in
- **Encoded (Bool):** helper "Asked only when a loss was held back (false otherwise)" = true and helper "Materially participated in the trade or business (box 1) by test 1, 2, 3 or 5" = true
- Expr: `{"all":[{"eq":["k1p.prior_b1_any_if",{"const":true}],"op":"test"},{"eq":["k1p.material",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 8, Former Passive Activities, "A prior-year unallowed loss from a former passive activity is allowed to the extent of current year income from the activity" (2025; sha256 76787e11)

## (helper) — `k1p.ask_prior_active`

- **Authored helper label:** A held-back rental real estate loss with active participation this year
- **Encoded (Bool):** helper "Asked only when a loss was held back (false otherwise)" = true and helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true
- Expr: `{"all":[{"eq":["k1p.prior_b2_any_if",{"const":true}],"op":"test"},{"eq":["k1p.active",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year" (2025; sha256 76787e11)

## (helper) — `k1p.prior_not_active`

- **Authored helper label:** Part of the held-back rental loss arose in a year without active participation
- **Encoded (Bool):** Input — Did any of the held-back rental real estate loss come from a year when you did not help make decisions for it, owned less than a tenth of it at any time that year, or held your share as a limited partner?
- Expr: `{"op":"input","source":"Did any of the held-back rental real estate loss come from a year when you did not help make decisions for it, owned less than a tenth of it at any time that year, or held your share as a limited partner?"}`
- Cite: [i8582] p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year" (2025; sha256 76787e11)

## (gate) — `k1p.prior_not_active_if`

- **Authored helper label:** Asked only of a held-back rental loss with active participation (false otherwise)
- **Encoded (Bool):** Choose — [helper "A held-back rental real estate loss with active participation this year" = true → helper "Part of the held-back rental loss arose in a year without active participation"] [helper "A held-back rental real estate loss with active participation this year" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.ask_prior_active",{"const":true}],"op":"test"},"then":"k1p.prior_not_active"},{"guard":{"eq":["k1p.ask_prior_active",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year" (2025; sha256 76787e11)

## (helper) — `k1p.any_loss`

- **Authored helper label:** A loss in box 1, 2, 3, 8, 9a or 14 (code A)
- **Encoded (Bool):** (helper "Box 1, asked only when the box shows an amount (zero otherwise)" < $0 or helper "Box 2, asked only when the box shows an amount (zero otherwise)" < $0 or helper "Box 3, asked only when the box shows an amount (zero otherwise)" < $0 or helper "Box 8, asked only when the box shows an amount (zero otherwise)" < $0 or helper "Box 9a, asked only when the box shows an amount (zero otherwise)" < $0 or helper "Box 14 A, asked only when the box shows an amount (zero otherwise)" < $0)
- Expr: `{"any":[{"lt":["k1p.box1_if_any",{"const":0}],"op":"test"},{"lt":["k1p.box2_if_any",{"const":0}],"op":"test"},{"lt":["k1p.box3_if_any",{"const":0}],"op":"test"},{"lt":["k1p.box8_if_any",{"const":0}],"op":"test"},{"lt":["k1p.box9a_if_any",{"const":0}],"op":"test"},{"lt":["k1p.box14a_if_any",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 3, Limitations on Losses, Deductions, and Credits, "the basis limitations, the at-risk limitations, the passive activity limitations, and the excess business loss limitations" (2025; sha256 659063e0)

## (helper) — `k1p.basis_short`

- **Authored helper label:** Losses more than basis
- **Encoded (Bool):** Input — Were your 2025 losses from it more than your basis in it at the end of its year? Basis is what you put in, plus your share of its income (taxable and tax-exempt) and debts, less losses, nondeductible expenses, money and marketable securities taken out, and any fall in your share of its debts.
- Expr: `{"op":"input","source":"Were your 2025 losses from it more than your basis in it at the end of its year? Basis is what you put in, plus your share of its income (taxable and tax-exempt) and debts, less losses, nondeductible expenses, money and marketable securities taken out, and any fall in your share of its debts."}`
- Cite: [i1065sk1] p. 3, Basis Limitations, "a partner may only claim their share of a partnership loss (including a capital loss) to the extent it doesn’t exceed their adjusted basis in the partnership" (2025; sha256 659063e0)

## (gate) — `k1p.basis_short_if_loss`

- **Authored helper label:** Asked only when the K-1 shows a loss (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss in box 1, 2, 3, 8, 9a or 14 (code A)" = true → helper "Losses more than basis"] [helper "A loss in box 1, 2, 3, 8, 9a or 14 (code A)" = false → helper "No (false)"]
- Interpretation: amb.2025.k1p_basis_by_filer
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.any_loss",{"const":true}],"op":"test"},"then":"k1p.basis_short"},{"guard":{"eq":["k1p.any_loss",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 3, Basis Limitations, "a partner may only claim their share of a partnership loss (including a capital loss) to the extent it doesn’t exceed their adjusted basis in the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.not_at_risk`

- **Authored helper label:** Some investment not at risk
- **Encoded (Bool):** Input — Was any of what you have in it borrowed on a loan you are not personally liable for (other than a qualified real estate loan), covered by a guarantee, stop-loss agreement or similar arrangement, or borrowed from anyone with an interest in the business (other than as a lender) or someone related to one; or does item K show nonrecourse debts (other than qualified real estate loans)?
- Expr: `{"op":"input","source":"Was any of what you have in it borrowed on a loan you are not personally liable for (other than a qualified real estate loan), covered by a guarantee, stop-loss agreement or similar arrangement, or borrowed from anyone with an interest in the business (other than as a lender) or someone related to one; or does item K show nonrecourse debts (other than qualified real estate loans)?"}`
- Cite: [i1065sk1] p. 8, At-Risk Limitations, "you’ll have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 659063e0)

## (gate) — `k1p.not_at_risk_if_loss`

- **Authored helper label:** Asked only when the K-1 shows a loss (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss in box 1, 2, 3, 8, 9a or 14 (code A)" = true → helper "Some investment not at risk"] [helper "A loss in box 1, 2, 3, 8, 9a or 14 (code A)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.any_loss",{"const":true}],"op":"test"},"then":"k1p.not_at_risk"},{"guard":{"eq":["k1p.any_loss",{"const":false}],"op":"test"},"then":"k1p.no"}],"op":"choose"}`
- Cite: [i1065sk1] p. 8, At-Risk Limitations, "you’ll have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 659063e0)

## (helper) — `k1p.basis_carry`

- **Authored helper label:** Losses from this partnership not allowed in an earlier year because of the basis limitation
- **Encoded (Bool):** Input — Was a loss from this partnership held back on an earlier return because your basis was too low?
- Expr: `{"op":"input","source":"Was a loss from this partnership held back on an earlier return because your basis was too low?"}`
- Cite: [i1065sk1] p. 13, "If you have losses, deductions, or credits from a prior year that weren’t deductible or usable because of certain limitations, such as the basis limitations or the at-risk limitations, take them into account in determining your net income, loss, or credits for this year" (2025; sha256 659063e0)

## (helper) — `k1p.risk_carry`

- **Authored helper label:** A loss from this partnership not allowed in an earlier year because of the at-risk limitation
- **Encoded (Bool):** Input — Was a loss from this partnership held back on an earlier return by the at-risk rules (Form 6198)?
- Expr: `{"op":"input","source":"Was a loss from this partnership held back on an earlier return by the at-risk rules (Form 6198)?"}`
- Cite: [i1065sk1] p. 13, "If you have losses, deductions, or credits from a prior year that weren’t deductible or usable because of certain limitations, such as the basis limitations or the at-risk limitations, take them into account in determining your net income, loss, or credits for this year" (2025; sha256 659063e0)

## (helper) — `k1p.fuel_prior_year`

- **Authored helper label:** A credit for federal tax on fuels claimed on the 2024 return from this partnership's information
- **Encoded (Bool):** Input — Did your 2024 return claim a credit for federal tax on gasoline or other fuels, using this partnership's information?
- Expr: `{"op":"input","source":"Did your 2024 return claim a credit for federal tax on gasoline or other fuels, using this partnership's information?"}`
- Cite: [i1040se] p. 9, Domestic Partnerships, "If you claimed a credit for federal tax on gasoline or other fuels on your 2024 Form 1040, 1040-SR, or 1040-NR based on information received from the partnership, enter as income in column (h) or column (k), whichever applies, the amount of the credit claimed for 2024" (2025; sha256 ad71de35)

## (helper) — `k1p.se_loss_not_material`

- **Authored helper label:** A self-employment loss (box 14, code A) without material participation in box 1
- **Encoded (Bool):** helper "Box 14 A, asked only when the box shows an amount (zero otherwise)" < $0 and helper "Materially participated in the trade or business (box 1) by test 1, 2, 3 or 5" = false
- Expr: `{"all":[{"lt":["k1p.box14a_if_any",{"const":0}],"op":"test"},{"eq":["k1p.material",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)

## (helper) — `k1p.b1_passive`

- **Authored helper label:** Box 1 is passive (no material participation)
- **Encoded (Bool):** helper "Materially participated in the trade or business (box 1) by test 1, 2, 3 or 5" = false
- Expr: `{"eq":["k1p.material",{"const":false}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Effect of determination, "If you determine that you didn’t materially participate in a trade or business activity of the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.b1_pos`

- **Authored helper label:** Box 1 income
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Box 1, asked only when the box shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1p.box1_if_any","op":"subtract_floor0","take":"k1p.zero"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.b1_neg`

- **Authored helper label:** Box 1 loss
- **Encoded (NonNegDollars):** Subtract helper "Box 1, asked only when the box shows an amount (zero otherwise)" from helper "Zero". If zero or less, enter -0-.
- Expr: `{"from":"k1p.zero","op":"subtract_floor0","take":"k1p.box1_if_any"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership" (2025; sha256 659063e0)

## (helper) — `k1p.b2_pos`

- **Authored helper label:** Box 2 income
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Box 2, asked only when the box shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1p.box2_if_any","op":"subtract_floor0","take":"k1p.zero"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.b2_neg`

- **Authored helper label:** Box 2 loss
- **Encoded (NonNegDollars):** Subtract helper "Box 2, asked only when the box shows an amount (zero otherwise)" from helper "Zero". If zero or less, enter -0-.
- Expr: `{"from":"k1p.zero","op":"subtract_floor0","take":"k1p.box2_if_any"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.b3_pos`

- **Authored helper label:** Box 3 income
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Box 3, asked only when the box shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1p.box3_if_any","op":"subtract_floor0","take":"k1p.zero"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.b3_neg`

- **Authored helper label:** Box 3 loss
- **Encoded (NonNegDollars):** Subtract helper "Box 3, asked only when the box shows an amount (zero otherwise)" from helper "Zero". If zero or less, enter -0-.
- Expr: `{"from":"k1p.zero","op":"subtract_floor0","take":"k1p.box3_if_any"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## V (a) — `k1p.b1_net_income`

- **IRS:** Box 1 passive net income: Form 8582 column (a)
- **Encoded (NonNegDollars):** Choose — [helper "Box 1 is passive (no material participation)" = true → helper "Box 1 income"] [helper "Box 1 is passive (no material participation)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.b1_passive",{"const":true}],"op":"test"},"then":"k1p.b1_pos"},{"guard":{"eq":["k1p.b1_passive",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h)" (2025; sha256 659063e0)

## V (b) — `k1p.b1_net_loss`

- **IRS:** Box 1 passive net loss: Form 8582 column (b)
- **Encoded (NonNegDollars):** Choose — [helper "Box 1 is passive (no material participation)" = true → helper "Box 1 loss"] [helper "Box 1 is passive (no material participation)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.b1_passive",{"const":true}],"op":"test"},"then":"k1p.b1_neg"},{"guard":{"eq":["k1p.b1_passive",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h)" (2025; sha256 659063e0)

## IV/V (a) — `k1p.b2_net_income`

- **IRS:** Box 2 net income: Form 8582 column (a)
- **Encoded (NonNegDollars):** Enter the amount from helper "Box 2 income".
- Expr: `{"from":"k1p.b2_pos","op":"copy"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## IV/V (b) — `k1p.b2_net_loss`

- **IRS:** Box 2 net loss: Form 8582 column (b)
- **Encoded (NonNegDollars):** Enter the amount from helper "Box 2 loss".
- Expr: `{"from":"k1p.b2_neg","op":"copy"}`
- Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners" (2025; sha256 659063e0)

## V (a) — `k1p.b3_net_income`

- **IRS:** Box 3 net income: Form 8582 column (a)
- **Encoded (NonNegDollars):** Enter the amount from helper "Box 3 income".
- Expr: `{"from":"k1p.b3_pos","op":"copy"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## V (b) — `k1p.b3_net_loss`

- **IRS:** Box 3 net loss: Form 8582 column (b)
- **Encoded (NonNegDollars):** Enter the amount from helper "Box 3 loss".
- Expr: `{"from":"k1p.b3_neg","op":"copy"}`
- Cite: [i1065sk1] p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners" (2025; sha256 659063e0)

## (helper) — `k1p.b1_loss_sum`

- **Authored helper label:** Box 1 activity: net loss plus prior years unallowed loss
- **Encoded (NonNegDollars):** Add line V (b) (k1p.b1_net_loss) and helper "Asked only when a loss was held back from it (zero otherwise)".
- Expr: `{"of":["k1p.b1_net_loss","k1p.prior_b1_if"],"op":"sum"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## (e) — `k1p.b1_overall_loss`

- **Authored helper label:** Box 1 activity: overall loss, Form 8582 column (e)
- **Encoded (NonNegDollars):** Subtract line V (a) (k1p.b1_net_income) from helper "Box 1 activity: net loss plus prior years unallowed loss". If zero or less, enter -0-.
- Expr: `{"from":"k1p.b1_loss_sum","op":"subtract_floor0","take":"k1p.b1_net_income"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## (helper) — `k1p.b2_loss_sum`

- **Authored helper label:** Box 2 activity: net loss plus prior years unallowed loss
- **Encoded (NonNegDollars):** Add line IV/V (b) and helper "Asked only when a loss was held back from it (zero otherwise)".
- Expr: `{"of":["k1p.b2_net_loss","k1p.prior_b2_if"],"op":"sum"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## (e) — `k1p.b2_overall_loss`

- **Authored helper label:** Box 2 activity: overall loss, Form 8582 column (e)
- **Encoded (NonNegDollars):** Subtract line IV/V (a) from helper "Box 2 activity: net loss plus prior years unallowed loss". If zero or less, enter -0-.
- Expr: `{"from":"k1p.b2_loss_sum","op":"subtract_floor0","take":"k1p.b2_net_income"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## (helper) — `k1p.b3_loss_sum`

- **Authored helper label:** Box 3 activity: net loss plus prior years unallowed loss
- **Encoded (NonNegDollars):** Add line V (b) (k1p.b3_net_loss) and helper "Asked only when a loss was held back from it (zero otherwise)".
- Expr: `{"of":["k1p.b3_net_loss","k1p.prior_b3_if"],"op":"sum"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## (e) — `k1p.b3_overall_loss`

- **Authored helper label:** Box 3 activity: overall loss, Form 8582 column (e)
- **Encoded (NonNegDollars):** Subtract line V (a) (k1p.b3_net_income) from helper "Box 3 activity: net loss plus prior years unallowed loss". If zero or less, enter -0-.
- Expr: `{"from":"k1p.b3_loss_sum","op":"subtract_floor0","take":"k1p.b3_net_income"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## IV (a) — `k1p.p4_income`

- **IRS:** Part IV column (a): box 2 net income with active participation
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → line IV/V (a)] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.b2_net_income"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## IV (b) — `k1p.p4_loss`

- **IRS:** Part IV column (b): box 2 net loss with active participation
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → line IV/V (b)] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.b2_net_loss"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## IV (c) — `k1p.p4_prior`

- **IRS:** Part IV column (c): box 2 prior years unallowed loss with active participation
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → helper "Asked only when a loss was held back from it (zero otherwise)"] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.prior_b2_if"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## VI (a) — `k1p.p6_loss`

- **IRS:** Part VI column (a): box 2 overall loss with active participation
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → column (e) (k1p.b2_overall_loss)] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.b2_overall_loss"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.zero"}],"op":"choose"}`
- Cite: [i8582] p. 12, Part VI, "Enter the overall loss from column (e) of Part IV for each activity" (2025; sha256 76787e11)

## (helper) — `k1p.p5_b2_income`

- **Authored helper label:** Box 2 net income without active participation (Part V)
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → helper "Zero"] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → line IV/V (a)]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.zero"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.b2_net_income"}],"op":"choose"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## (helper) — `k1p.p5_b2_loss`

- **Authored helper label:** Box 2 net loss without active participation (Part V)
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → helper "Zero"] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → line IV/V (b)]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.zero"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.b2_net_loss"}],"op":"choose"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## (helper) — `k1p.p5_b2_prior`

- **Authored helper label:** Box 2 prior years unallowed loss without active participation (Part V)
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = true → helper "Zero"] [helper "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582" = false → helper "Asked only when a loss was held back from it (zero otherwise)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.active",{"const":true}],"op":"test"},"then":"k1p.zero"},{"guard":{"eq":["k1p.active",{"const":false}],"op":"test"},"then":"k1p.prior_b2_if"}],"op":"choose"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## V (a) — `k1p.p5_income`

- **IRS:** Part V column (a): net income of the passive activities other than Part IV
- **Encoded (NonNegDollars):** Add line V (a) (k1p.b1_net_income), helper "Box 2 net income without active participation (Part V)", and line V (a) (k1p.b3_net_income).
- Interpretation: amb.2025.k1p_activity_per_box
- Expr: `{"of":["k1p.b1_net_income","k1p.p5_b2_income","k1p.b3_net_income"],"op":"sum"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## V (b) — `k1p.p5_loss`

- **IRS:** Part V column (b): net loss of the passive activities other than Part IV
- **Encoded (NonNegDollars):** Add line V (b) (k1p.b1_net_loss), helper "Box 2 net loss without active participation (Part V)", and line V (b) (k1p.b3_net_loss).
- Expr: `{"of":["k1p.b1_net_loss","k1p.p5_b2_loss","k1p.b3_net_loss"],"op":"sum"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## V (c) — `k1p.p5_prior`

- **IRS:** Part V column (c): prior years unallowed loss of the passive activities other than Part IV
- **Encoded (NonNegDollars):** Add helper "Asked only when a loss was held back from it (zero otherwise)", helper "Box 2 prior years unallowed loss without active participation (Part V)", and helper "Asked only when a loss was held back from it (zero otherwise)".
- Expr: `{"of":["k1p.prior_b1_if","k1p.p5_b2_prior","k1p.prior_b3_if"],"op":"sum"}`
- Cite: [i8582] p. 9, Part V, "Use Part V for all other passive activities" (2025; sha256 76787e11)

## (helper) — `k1p.prior_total`

- **Authored helper label:** Prior years unallowed losses of this K-1
- **Encoded (NonNegDollars):** Add helper "Asked only when a loss was held back from it (zero otherwise)", helper "Asked only when a loss was held back from it (zero otherwise)", and helper "Asked only when a loss was held back from it (zero otherwise)".
- Expr: `{"of":["k1p.prior_b1_if","k1p.prior_b2_if","k1p.prior_b3_if"],"op":"sum"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `k1p.passive_loss`

- **Authored helper label:** A passive activity of this K-1 has a net loss or a prior years unallowed loss
- **Encoded (Bool):** (helper "Box 1 activity: net loss plus prior years unallowed loss" > $0 or helper "Box 2 activity: net loss plus prior years unallowed loss" > $0 or helper "Box 3 activity: net loss plus prior years unallowed loss" > $0)
- Expr: `{"any":[{"gt":["k1p.b1_loss_sum",{"const":0}],"op":"test"},{"gt":["k1p.b2_loss_sum",{"const":0}],"op":"test"},{"gt":["k1p.b3_loss_sum",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1065sk1] p. 9, Effect of determination, "If you have an overall loss (the excess of deductions and losses, including any prior-year unallowed loss, over income) or credits from a passive activity" (2025; sha256 659063e0)

## 28 (h) — `k1p.col_h`

- **IRS:** Passive income from Schedule K-1: Schedule E line 28 column (h)
- **Encoded (NonNegDollars):** Add line V (a) (k1p.b1_net_income), line IV/V (a), and line V (a) (k1p.b3_net_income).
- Expr: `{"of":["k1p.b1_net_income","k1p.b2_net_income","k1p.b3_net_income"],"op":"sum"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h)" (2025; sha256 659063e0)

## (helper) — `k1p.np_b1_income`

- **Authored helper label:** Box 1 income with material participation
- **Encoded (NonNegDollars):** Choose — [helper "Box 1 is passive (no material participation)" = true → helper "Zero"] [helper "Box 1 is passive (no material participation)" = false → helper "Box 1 income"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.b1_passive",{"const":true}],"op":"test"},"then":"k1p.zero"},{"guard":{"eq":["k1p.b1_passive",{"const":false}],"op":"test"},"then":"k1p.b1_pos"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k)" (2025; sha256 659063e0)

## 28 (k) — `k1p.col_k`

- **IRS:** Nonpassive income from Schedule K-1: Schedule E line 28 column (k)
- **Encoded (NonNegDollars):** Add helper "Box 1 income with material participation" and helper "Box 4a, asked only when the box shows an amount (zero otherwise)".
- Expr: `{"of":["k1p.np_b1_income","k1p.box4a_if_any"],"op":"sum"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k)" (2025; sha256 659063e0)

## 28 (i) — `k1p.col_i`

- **IRS:** Nonpassive loss allowed: Schedule E line 28 column (i) (as a positive amount)
- **Encoded (NonNegDollars):** Choose — [helper "Box 1 is passive (no material participation)" = true → helper "Zero"] [helper "Box 1 is passive (no material participation)" = false → helper "Box 1 loss"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1p.b1_passive",{"const":true}],"op":"test"},"then":"k1p.zero"},{"guard":{"eq":["k1p.b1_passive",{"const":false}],"op":"test"},"then":"k1p.b1_neg"}],"op":"choose"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k)" (2025; sha256 659063e0)

## (helper) — `k1p.nonpassive_net`

- **Authored helper label:** Nonpassive income less nonpassive loss (column (k) less column (i))
- **Encoded (Dollars):** Subtract line 28 (i) from line 28 (k).
- Expr: `{"from":"k1p.col_k","op":"subtract","take":"k1p.col_i"}`
- Cite: [i1065sk1] p. 14, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k)" (2025; sha256 659063e0)

## (helper) — `k1p.sche_row`

- **Authored helper label:** The K-1 puts a row on Schedule E line 28 (an amount in box 1, 2, 3 or 4a, or a held-back loss)
- **Encoded (Bool):** (helper "Box 1, asked only when the box shows an amount (zero otherwise)" ≠ $0 or helper "Box 2, asked only when the box shows an amount (zero otherwise)" ≠ $0 or helper "Box 3, asked only when the box shows an amount (zero otherwise)" ≠ $0 or helper "Box 4a, asked only when the box shows an amount (zero otherwise)" > $0 or helper "Prior years unallowed losses of this K-1" > $0)
- Interpretation: amb.2025.k1p_portfolio_no_sche
- Expr: `{"any":[{"ne":["k1p.box1_if_any",{"const":0}],"op":"test"},{"ne":["k1p.box2_if_any",{"const":0}],"op":"test"},{"ne":["k1p.box3_if_any",{"const":0}],"op":"test"},{"gt":["k1p.box4a_if_any",{"const":0}],"op":"test"},{"gt":["k1p.prior_total",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1040se] p. 10, Line 28, "For nonpassive income or loss and passive income or losses for which you are not filing Form 8582" (2025; sha256 ad71de35)

## (helper) — `k1p.se_pos`

- **Authored helper label:** Positive net earnings from self-employment (box 14, code A)
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Box 14 A, asked only when the box shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1p.box14a_if_any","op":"subtract_floor0","take":"k1p.zero"}`
- Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)

## (gate) — `k1p.screened`

- **Authored helper label:** This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)
- **Encoded (Bool):** Enter the amount from helper "Yes (true)".
- **Refusal:** when k1p.ptp is true, cannot complete Publicly traded partnership (Schedule K-1 item D). A Schedule K-1 from a publicly traded partnership is outside this tool. Cite: [i1065sk1] p. 10, Publicly traded partnerships (PTPs), "Don’t report passive income, gains, or losses from a PTP on Form 8582" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b4b is true, cannot complete Schedule K-1 (Form 1065) box 4b (guaranteed payments for capital). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 15, Box 4b. Guaranteed Payments for Capital, "These are guaranteed payments other than for services" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b7 is true, cannot complete Schedule K-1 (Form 1065) box 7 (royalties on Schedule E, line 4). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 15, Box 7. Royalties, "Report royalties on Schedule E (Form 1040), line 4" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b10 is true, cannot complete Schedule K-1 (Form 1065) box 10 (Form 4797). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 16, Box 10. Net Section 1231 Gain (Loss), "report it in column (g) of Form 4797, line 2" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b11 is true, cannot complete Schedule K-1 (Form 1065) box 11 (other income or loss). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 16, Box 11. Other Income (Loss), "Code A. Other portfolio income (loss)" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b12 is true, cannot complete Schedule K-1 (Form 1065) box 12 (section 179 deduction, Form 4562). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 18, Box 12. Section 179 Deduction, "to complete Part I of Form 4562" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b13 is true, cannot complete Schedule K-1 (Form 1065) box 13 (other deductions). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 18, Box 13. Other Deductions, "Codes A through G" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b14bc is true, cannot complete Schedule K-1 (Form 1065) box 14, codes B and C (optional methods of Schedule SE). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 22, Code B. Gross farming or fishing income, "Also use this amount to figure net earnings from self-employment under the farm optional method" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b15 is true, cannot complete Schedule K-1 (Form 1065) box 15 (credits; Form 8582-CR, Form 3800). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 22, Box 15. Credits, "you must complete Form 8582-CR" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b16 is true, cannot complete Schedule K-3 (international items). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 24, Box 16. International Transactions, "If the partnership checked the box, see the attached Schedule K-3" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b17 is true, cannot complete Schedule K-1 (Form 1065) box 17 (Form 6251). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 24, Box 17. Alternative Minimum Tax (AMT) Items, "to prepare your Form 6251" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b20 is true, cannot complete Schedule K-1 (Form 1065) box 20, other information. A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b21 is true, cannot complete Schedule K-1 (Form 1065) box 21 (foreign taxes; Form 1116). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 32, Box 21. Foreign Taxes Paid or Accrued, "Foreign taxes paid or accrued reduce a partner’s basis" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_b2223 is true, cannot complete A partnership with more than one activity (boxes 22 and 23). A Schedule K-1 with this item is outside this tool. Cite: [i1065sk1] p. 9, Material participation, "If the partnership had more than one activity, it’ll attach a statement to your Schedule K-1 that identifies each activity" (2025; sha256 659063e0)
- **Refusal:** when k1p.r_foreign is true, cannot complete Schedule E, line 28, column (c) (foreign partnership; Form 8865). A Schedule K-1 from a foreign partnership is outside this tool. Cite: [i1040se] p. 9, Foreign Partnerships, "you may have to file Form 8865" (2025; sha256 ad71de35)
- **Refusal:** when k1p.r_disposed is true, cannot complete Sale or other disposition of a partnership interest (Form 8949, section 751). A sale or other disposition of a partnership interest is outside this tool. Cite: [i1065sk1] p. 2, Sale or Exchange of Partnership Interest, "Generally, a partner who sells or exchanges a partnership interest" (2025; sha256 659063e0)
- **Refusal:** when k1p.upe is true, cannot complete Schedule E, line 28, unreimbursed partnership expenses (and box 14, code A reduced by them). Partnership expenses you paid yourself under the partnership agreement are outside this tool. Cite: [i1040se] p. 10, Unreimbursed Partnership Expenses, "You can deduct unreimbursed ordinary and necessary partnership expenses you paid on behalf of the partnership on Schedule E if you were required to pay these expenses under the partnership agreement" (2025; sha256 ad71de35)
- **Refusal:** when k1p.interest_buy is true, cannot complete Schedule E, line 28, interest on money borrowed to buy into a partnership (debt-financed acquisition). Interest on money borrowed to buy into a partnership is outside this tool. Cite: [i1040se] p. 9, Domestic Partnerships, "If you used loan proceeds to buy an interest in, or make a contribution to the capital of, a partnership (debt-financed acquisition), report your share of deductible partnership interest expense on either Schedule A or Schedule E" (2025; sha256 ad71de35)
- **Refusal:** when k1p.fiscal is true, cannot complete Schedule K-1 (Form 1065) for a partnership's fiscal year. A Schedule K-1 for a tax year other than the calendar year 2025 is outside this tool. Cite: [i1065sk1] p. 13, "If you file your tax return on a calendar-year basis, but your partnership files a return for a fiscal year, report the amounts on your tax return for the year in which the partnership's fiscal year ends"; p. 9, "All determinations of material participation are based on your participation during the partnership’s tax year" (2025; sha256 659063e0)
- **Refusal:** when k1p.oil_gas_gp_if_gp is true, cannot complete Schedule E, line 28, column (k), a working interest in oil or gas wells held as a general partner (nonpassive). A working interest in oil or gas wells held through a partnership as a general partner is outside this tool. Cite: [i1065sk1] p. 8, Passive activities don't include the following, "Working interests in oil or gas wells if you were a general partner" (2025; sha256 659063e0)
- **Refusal:** when k1p.llc_member_active is true, cannot complete Material and active participation of an LLC member who is not a manager (Form 8582). Whether an LLC member who is not a manager is treated as a limited partner is outside this tool. Cite: [i1065sk1] p. 2, Limited Partner, "Some members of other entities, such as domestic or foreign business trusts or limited liability companies (LLCs) that are classified as partnerships, may be treated as limited partners for certain purposes" (2025; sha256 659063e0)
- **Refusal:** when k1p.b19_other_if_any is true, cannot complete Schedule K-1 (Form 1065) box 19, codes other than A (distributions of property). A distribution of property other than money is outside this tool. Cite: [i1065sk1] p. 25, Box 19. Distributions, "Code A. Cash and marketable securities other than for services" (2025; sha256 659063e0)
- **Refusal:** when k1p.dist_over_if_any is true, cannot complete Gain on a distribution above basis (Form 8949). Money taken out of a partnership above your basis is outside this tool. Cite: [i1065sk1] p. 25, Box 19. Distributions, "exceed the adjusted basis of your partnership interest immediately before the distribution, the excess is treated as gain from the sale or exchange of your partnership interest" (2025; sha256 659063e0)
- **Refusal:** when k1p.z_other_if_z is true, cannot complete Section 199A dividends or cooperative items from a partnership (Form 8995-A). Section 199A dividends or cooperative items from a partnership are outside this tool. Cite: [i1065sk1] p. 30, Section 199A dividends, "The amount reported reflects your distributive share of the partnership’s net section 199A dividends" (2025; sha256 659063e0)
- **Refusal:** when k1p.trader_if_b1 is true, cannot complete A partnership trading investments for its owners (nonpassive trading activity). A partnership that trades investments for its owners is outside this tool. Cite: [i1065sk1] p. 11, Special rules for certain other activities, "Trading personal property for the account of owners of interests in the activity" (2025; sha256 659063e0)
- **Refusal:** when k1p.t6_if_asked is true, cannot complete Material participation by test 6 (personal service activity). Material participation by the personal service test is outside this tool. Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a personal service activity and you materially participated in the activity for any 3 tax years" (2025; sha256 659063e0)
- **Refusal:** when k1p.t4_if_gp is true, cannot complete Material participation by test 4 (significant participation activities). Material participation by the significant participation test is outside this tool. Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "The activity was a significant participation activity for the tax year" (2025; sha256 659063e0)
- **Refusal:** when k1p.t7_if_gp is true, cannot complete Material participation by test 7 (facts and circumstances). Material participation by the facts and circumstances test is outside this tool. Cite: [i1065sk1] p. 9, Individuals (other than limited partners), "Based on all the facts and circumstances, you participated in the activity on a regular, continuous, and substantial basis during the tax year" (2025; sha256 659063e0)
- **Refusal:** when k1p.over100_if_income is true, cannot complete Form 8582, income from a significant participation activity (recharacterized as nonpassive). Income from a business you worked in for more than 100 hours without materially participating is outside this tool. Cite: [i1065sk1] p. 11, Special rules for certain other activities, "If you have net income subject to recharacterization under Temporary Regulations section 1.469-2T(f) and Regulations sections 1.469-2(f)(5) and (6), report such amounts according to the Instructions for Form 8582"; p. 9, "A significant participation activity is any trade or business activity in which you participated for more than 100 hours during the year and in which you didn’t materially participate" (2025; sha256 659063e0)
- **Refusal:** when k1p.re_pro_if_b2 is true, cannot complete Schedule K-1 (Form 1065) box 2 of a real estate professional (Schedule E, line 43). Rental real estate from a partnership held by a real estate professional is outside this tool. Cite: [i1065sk1] p. 14, Box 2. Net Rental Real Estate Income (Loss), "the income (loss) in box 2 isn’t from a passive activity if you were a real estate professional (defined earlier) and you materially participated in the activity" (2025; sha256 659063e0)
- **Refusal:** when k1p.dwelling_if_rent is true, cannot complete Rental of a home a partner used personally (nonpassive; Form 8582 does not apply). A partnership's rental of a home a partner used personally for more than the limit is outside this tool. Cite: [i1065sk1] p. 11, Special rules for certain other activities, "The rental of a dwelling unit any partner used for personal purposes during the year for more than the greater of 14 days or 10% of the number of days that the residence was rented at fair rental value" (2025; sha256 659063e0)
- **Refusal:** when k1p.basis_short_if_loss is true, cannot complete Partnership losses above basis (basis limitation). Losses from a partnership above your basis in it are outside this tool. Cite: [i1065sk1] p. 3, Basis Limitations, "a partner may only claim their share of a partnership loss (including a capital loss) to the extent it doesn’t exceed their adjusted basis in the partnership" (2025; sha256 659063e0)
- **Refusal:** when k1p.not_at_risk_if_loss is true, cannot complete Form 6198 (at-risk limitations). A partnership loss with an amount not at risk is outside this tool. Cite: [i1065sk1] p. 8, At-Risk Limitations, "you’ll have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 659063e0)
- **Refusal:** when k1p.basis_carry is true, cannot complete Schedule E, line 28, column (i), a loss carried from an earlier year by the basis limitation. A partnership loss carried from an earlier year by the basis limitation is outside this tool. Cite: [i1065sk1] p. 13, "If you have losses, deductions, or credits from a prior year that weren’t deductible or usable because of certain limitations, such as the basis limitations or the at-risk limitations, take them into account in determining your net income, loss, or credits for this year" (2025; sha256 659063e0)
- **Refusal:** when k1p.risk_carry is true, cannot complete Form 6198 (at-risk limitations), a loss carried from an earlier year. A partnership loss carried from an earlier year by the at-risk limitation is outside this tool. Cite: [i1065sk1] p. 13, "If you have losses, deductions, or credits from a prior year that weren’t deductible or usable because of certain limitations, such as the basis limitations or the at-risk limitations, take them into account in determining your net income, loss, or credits for this year" (2025; sha256 659063e0)
- **Refusal:** when k1p.fuel_prior_year is true, cannot complete Schedule E, line 28, a 2024 fuel tax credit from the partnership taken into income. A fuel tax credit from a partnership claimed on your 2024 return is outside this tool. Cite: [i1040se] p. 9, Domestic Partnerships, "If you claimed a credit for federal tax on gasoline or other fuels on your 2024 Form 1040, 1040-SR, or 1040-NR based on information received from the partnership, enter as income in column (h) or column (k), whichever applies, the amount of the credit claimed for 2024" (2025; sha256 ad71de35)
- **Refusal:** when k1p.se_loss_not_material is true, cannot complete Schedule K-1 box 14, code A loss without material participation. A self-employment loss from a partnership business you did not materially participate in is outside this tool. Cite: [i1065sk1] p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE" (2025; sha256 659063e0)
- **Refusal:** when k1p.former_passive is true, cannot complete Form 8582, former passive activity (held-back loss from a business you now materially participate in). A held-back loss from a business you now materially participate in is outside this tool. Cite: [i8582] p. 8, Former Passive Activities, "A prior-year unallowed loss from a former passive activity is allowed to the extent of current year income from the activity" (2025; sha256 76787e11)
- **Refusal:** when k1p.prior_not_active_if is true, cannot complete Form 8582, Part IV (prior-year loss from a year without active participation). A held-back rental loss from a year without active participation is outside this tool. Cite: [i8582] p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year" (2025; sha256 76787e11)
- Expr: `{"from":"k1p.yes","op":"copy"}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)
