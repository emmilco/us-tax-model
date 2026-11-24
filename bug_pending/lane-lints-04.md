## BUG-NEW-lane-lints-04 — rec.medical: the repaid 2024 medical expenses are asked as repaid "to you" only, unlike rec.property_tax

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** p525 p. 26, Recoveries, Example 34, "In 2025, you received a $500 reimbursement from your medical insurance for your 2024 ..."; i1040gi p. 13, "report their combined income and deduct their combined allowable expenses" (a joint return); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** rec.medical, an amount asked once per return, said "How much of your 2024 medical and dental bills was repaid to you in 2025?", while its sibling rec.property_tax asks what was refunded "to you (or, on a joint return, your spouse)". A joint filer can leave out a reimbursement paid to the spouse: the recovery on Schedule 1 line 8z is understated.
- **Where:** interview/2025/questions.yaml rec.medical (prompt).
- **Fix:** Prompt: "How much of your 2024 medical and dental bills was repaid to you (or, on a joint return, your spouse) in 2025?". No fixture: values unchanged.
- **Fix lines:** rec.medical
- **Siblings checked:** rec.medical_if_has
- **Severity:** low
- **Tags:** Schedule 1, recoveries, spouse phrase; fixed
