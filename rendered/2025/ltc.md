# Form 7206, line 2 — qualified long-term care insurance, one per person covered

- Document: `ltc` (form, tax year 2025)
- Collection: keyed entries within sc; [f7206] Form 7206 (2025), line 2, "If more than one person is covered, figure separately the amount to enter for each person"; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)
- Note: One entry per person covered by qualified long-term care insurance established under the business.

## 2(a) — `ltc.payments`

- **IRS:** Total payments made for that person during the year
- **Encoded (NonNegDollars):** Input — The qualified long-term care insurance premiums paid in 2025 for this person under a policy established under this business (not for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of your dependent or of your child under age 27 at the end of 2025).

  This person must be you, your spouse, your dependent, or your child (son, daughter, stepchild, adopted child or foster child) who was under age 27 at the end of 2025 even if not your dependent; enter zero for anyone else, such as a parent who is not your dependent or a child 27 or older who is not your dependent.

  Enter only premiums on a qualified long-term care insurance contract, that is, one that meets all of these:

  - it only provides coverage of qualified long-term care services
  - it is guaranteed renewable
  - it provides that refunds (other than on the death of the insured or the complete surrender or cancellation of the contract) and dividends may be used only to reduce future premiums or increase future benefits
  - it generally does not provide for a cash surrender value or other money that can be paid, assigned, pledged or borrowed
  - it generally does not pay or reimburse expenses that would be reimbursed under Medicare (except where Medicare is a secondary payer or the contract makes per diem or other periodic payments without regard to expenses)
- Expr: `{"op":"input","source":"The qualified long-term care insurance premiums paid in 2025 for this person under a policy established under this business (not for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of your dependent or of your child under age 27 at the end of 2025).\n\nThis person must be you, your spouse, your dependent, or your child (son, daughter, stepchild, adopted child or foster child) who was under age 27 at the end of 2025 even if not your dependent; enter zero for anyone else, such as a parent who is not your dependent or a child 27 or older who is not your dependent.\n\nEnter only premiums on a qualified long-term care insurance contract, that is, one that meets all of these:\n\n- it only provides coverage of qualified long-term care services\n- it is guaranteed renewable\n- it provides that refunds (other than on the death of the insured or the complete surrender or cancellation of the contract) and dividends may be used only to reduce future premiums or increase future benefits\n- it generally does not provide for a cash surrender value or other money that can be paid, assigned, pledged or borrowed\n- it generally does not pay or reimburse expenses that would be reimbursed under Medicare (except where Medicare is a secondary payer or the contract makes per diem or other periodic payments without regard to expenses)"}`
- Cite: [f7206] Form 7206 (2025), line 2(a); i7206 p. 1, "You may be able to deduct the amount you paid for health insurance, which includes medical, dental, and vision insurance and qualified long-term care insurance for yourself, your spouse, and your dependents.", "The health insurance can cover your child who was under age 27 at the end of 2025, even if the child wasn’t your dependent.", "A child includes your son, daughter, stepchild, adopted child, or foster child."; i7206 p. 2, Qualified long-term care insurance contract, "A qualified long-term care insurance contract is an insurance contract that only provides coverage of qualified long-term care services. The contract must meet all the following requirements. • It must be guaranteed renewable. • It must provide that refunds, other than refunds on the death of the insured or complete surrender or cancellation of the contract, and dividends under the contract may be used only to reduce future premiums or increase future benefits. • It must generally not provide for a cash surrender value or other money that can be paid, assigned, pledged, or borrowed. • It must generally not pay or reimburse expenses incurred for services or items that would be reimbursed under Medicare, except where Medicare is a secondary payer or the contract makes per diem or other periodic payments without regard to expenses" (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `ltc.age`

- **Authored helper label:** That person's age at the end of 2025
- **Encoded (Enum(ltc_age)):** Input — This person's age at the end of 2025: 40 or younger (to40), 41 to 50 (to50), 51 to 60 (to60), 61 to 70 (to70), or 71 or older (over70)
- Expr: `{"op":"input","source":"This person's age at the end of 2025: 40 or younger (to40), 41 to 50 (to50), 51 to 60 (to60), 61 to 70 (to70), or 71 or older (over70)"}`
- Cite: [f7206] Form 7206 (2025), line 2(b), "Use the person's age at the end of the tax year" (2025; created 2025-10-02; sha256 822203c9)

## 2(b) — `ltc.limit`

- **IRS:** The amount for that person's age
- **Encoded (NonNegDollars):** Find the entry in Qualified long-term care premium limit by age (Form 7206, line 2(b)) for age helper "That person's age at the end of 2025".
- Expr: `{"keys":["ltc.age"],"op":"keyed_lookup","table":"ltc_limit"}`
- Cite: [f7206] Form 7206 (2025), line 2(b), "The amount shown below. Use the person’s age at the end of the tax year" (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `ltc.amount`

- **Authored helper label:** The smaller of (a) or (b)
- **Encoded (NonNegDollars):** Enter the smaller of line 2(a) or line 2(b).
- Expr: `{"of":["ltc.payments","ltc.limit"],"op":"smaller_of"}`
- Cite: [f7206] Form 7206 (2025), line 2, "enter for each person covered the smaller of (a) or (b)"; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)
