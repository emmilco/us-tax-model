# Proposed bug entries (C-backlog: T-164, T-165, T-166)

Ids are placeholders; the integrator assigns BUG numbers. Each entry closes an open entry, because
the inventory is append-only.

## PENDING-1 — T-164 is fixed: f8962.premium_adjust asks only about Marketplace coverage and 2025 months

- **Caught by:** the f8962 screen review's WIDE and UNCLEAR findings on `f8962.premium_adjust`, ruled accepted over-refusal and recorded as T-164; this entry closes T-164.
- **Source:** i8962 p. 4, "Generally, if coverage in a qualified health plan began after the first day of the month, you are not allowed a monthly credit amount for the coverage for that month."; p. 4, "The enrollment premiums are the total amount of the premiums for the month, reduced by any premium amounts for that month that were refunded in 2025"; p. 5, "Catastrophic health plans and stand-alone dental plans purchased through the Marketplace, and all plans purchased through the Small Business Health Options Program (SHOP), are not qualified health plans for purposes of the PTC."
- **Symptom:** the question asked whether "coverage for anyone in your tax family began after the first day of a month" and whether "any Marketplace premiums for a month [were] refunded in 2025". A dependent's employer or Medicaid coverage starting mid-month, or a 2025 refund of a 2024 month's premium, read as yes and refused a return whose column A is right as reported. Over-refusal only; no amount was wrong.
- **Fix:** the question and its interview help ask about Marketplace coverage reported on a Form 1095-A (a qualified health plan) that began after the first day of a 2025 month, and about premiums for a 2025 month of that coverage refunded in 2025; they say a start date of other coverage (employer, Medicaid, a catastrophic, stand-alone dental or SHOP plan) does not count. The cite adds the p. 5 sentence. No expression changed; the refusal remedy is unchanged.
- **Fix lines:** `f8962.premium_adjust`
- **Siblings checked:** `f8962.line24`, `f8962.line25` (`siblings.py f8962.premium_adjust`: no same-anchor siblings)
- **Regression predictions:** `stage18.refuse.premium_adjust` already answers the gate yes and refuses at `f8962.line24`, `f8962.line25` and `s3.line9`; evaluated on the changed tree it still refuses there, and the same inputs with the gate answered no complete (line 24 $3,560, line 25 $3,500). No fixture changed because no expression changed. Fixtures 1,437/1,437.
- **Validation:** source inspection; f8962 screen review to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## PENDING-2 — BUG-0298 is fixed: the column B questions no longer say "zero if blank" for a covered month

- **Caught by:** BUG-0298, recorded open (T-165); this entry closes it.
- **Source:** i8962 p. 5, "Form 1095-A, Part III, column B, may be wrong or blank or may report your applicable SLCSP premium as -0-. ... In either case, you must determine your correct applicable SLCSP premium."; p. 17, "If columns (a) and (b) of any of lines 12 through 23 are blank, leave column (c) of the corresponding line blank."
- **Symptom:** as recorded in BUG-0298. Reproduced on the unchanged expressions: one Form 1095-A, January to June covered (column A $500, column B $450, column C $300 a month), not uniform; entering column B as zero for March, as "zero if blank" invites, completes the return with Form 8962 line 24 $1,485 against $1,782 with the correct $450, the $297 credit for March lost. No refusal stops it.
- **Fix:** the twelve `f1095a.in_b_<month>` questions end "zero only if no one was enrolled in this policy that month (column A blank)". The row's proposed "no one was enrolled that month" was narrowed to "in this policy", because with two policies that follow one another (both counted) a filer reading "no one" across policies could enter an SLCSP premium on both forms for the same month and double column B. `f1095a.mo_b` never carried the clause (it is asked only when the form shows all twelve months), so it is unchanged; BUG-0298's "13 questions" is 12. No expression changed.
- **Fix lines:** `f1095a.in_b_jan` through `f1095a.in_b_dec`
- **Siblings checked:** `f1095a.b_jan`–`f1095a.b_dec`, `f1095a.yr_b_monthly`, `f1095a.mo_b` (`siblings.py f1095a.in_b_jan`); the column A and C questions keep "zero if blank", which is right for them.
- **Regression predictions:** no expression changed, so no fixture can tell the wording apart; the reproduction above is recorded in the C-backlog report, not as a fixture. Fixtures pass unchanged.
- **Validation:** source inspection and evaluation of the reproduction; f1095a and f8962 reviews to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## PENDING-3 — BUG-0299 is fixed: f8962.other defines "affordable" for the employee and for family members

- **Caught by:** BUG-0299, recorded open (T-166); this entry closes it.
- **Source:** i8962 p. 5, "The coverage offered by your employer is generally considered affordable for you if your share of the annual cost for self-only coverage, which is sometimes referred to as the “employee required contribution,” is not more than 9.02% of your household income."; p. 5, "coverage if your share of the annual cost for coverage for yourself and the other members of your tax family allowed to enroll in the coverage is not more than 9.02% of your household income."; p. 5, "If your employer coverage is affordable for you but not affordable for your other family members, you may be able to take the PTC for your other family members if they enroll in a Marketplace qualified health plan."
- **Symptom:** as recorded in BUG-0299 (an employee whose self-only cost is affordable but whose family cost is not could answer no and keep the PTC for the employee's own months).
- **Fix:** the employer limb of the `f8962.other` question states the test: for the employee, the employee's share of the annual cost of self-only coverage is not more than 9.02% of household income (Form 8962, line 3), whatever family coverage costs; for another member of the tax family allowed to enroll, the employee's share of the annual cost of coverage for the employee and the family members allowed to enroll is not more than 9.02%. The cite adds the three p. 5 sentences. No expression changed; the Marketplace-determination exception stays omitted (accepted over-refusal in the f8962.other screen ruling).
- **Fix lines:** `f8962.other`
- **Siblings checked:** `f8962.line24`, `f8962.line25` (`siblings.py f8962.other`: no same-anchor siblings)
- **Regression predictions:** no expression changed; existing fixtures that answer `f8962.other` yes still refuse (see the report). Fixtures pass unchanged.
- **Validation:** source inspection; f8962 reviews and completeness to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed
