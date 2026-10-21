# Form 7206, line 2 — qualified long-term care insurance, one per person covered

- Document: `ltc` (form, tax year 2025)
- Collection: keyed entries within sc; [f7206] Form 7206 (2025), line 2, "If more than one person is covered, figure separately the amount to enter for each person"; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)
- Note: One entry per person covered by qualified long-term care insurance established under the business.

## 2(a) — `ltc.payments`

- **IRS:** Total payments made for that person during the year
- **Encoded (NonNegDollars):** Input — The qualified long-term care insurance premiums paid in 2025 for this person under a policy established under this business (not for any month the person was eligible for a long-term care plan subsidized by an employer)
- Expr: `{"op":"input","source":"The qualified long-term care insurance premiums paid in 2025 for this person under a policy established under this business (not for any month the person was eligible for a long-term care plan subsidized by an employer)"}`
- Cite: [f7206] Form 7206 (2025), line 2(a) (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `ltc.age`

- **Authored helper label:** That person's age at the end of 2025
- **Encoded (Enum(ltc_age)):** Input — This person's age at the end of 2025: 40 or younger (to40), 41 to 50 (to50), 51 to 60 (to60), 61 to 70 (to70), or 71 or older (over70)
- Expr: `{"op":"input","source":"This person's age at the end of 2025: 40 or younger (to40), 41 to 50 (to50), 51 to 60 (to60), 61 to 70 (to70), or 71 or older (over70)"}`
- Cite: [f7206] Form 7206 (2025), line 2(b), "Use the person's age at the end of the tax year" (2025; created 2025-10-02; sha256 822203c9)

## 2(b) — `ltc.limit`

- **IRS:** The amount for that person's age
- **Encoded (NonNegDollars):** Find the entry in Qualified long-term care premium limit by age (Form 7206, line 2(b)) for age helper "That person's age at the end of 2025".
- Expr: `{"keys":["ltc.age"],"op":"keyed_lookup","table":"ltc_limit"}`
- Cite: [f7206] Form 7206 (2025), line 2(b) (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `ltc.amount`

- **Authored helper label:** The smaller of (a) or (b)
- **Encoded (NonNegDollars):** Enter the smaller of line 2(a) or line 2(b).
- Expr: `{"of":["ltc.payments","ltc.limit"],"op":"smaller_of"}`
- Cite: [f7206] Form 7206 (2025), line 2, "enter for each person covered the smaller of (a) or (b)"; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)
