## BUG-NEW-lane-lints-02 — s2.household_employee: the Schedule H wage test is asked of "you" only on a joint return

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** i1040sh p. 4, Name of employer, "Only two Schedules H can be attached to Form 1040, 1040-SR, and 1040-SS, one Schedule H for each of the primary taxpayer and the secondary taxpayer"; i1040sh, Line A, "Did you pay any one household employee cash wages of $2,800 or more in 2025?"; i1040gi p. 13, "report their combined income and deduct their combined allowable expenses" (a joint return); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** s2.household_employee, a refusal screen asked once per return, said "Did you pay any one of them $2,800 or more ..." while its parent s2.household_help asks whether "you (or, on a joint return, your spouse)" paid anyone to work in the home. A joint filer whose spouse employs the household worker can answer No: the Schedule H refusal is missed and the household employment taxes are left off Schedule 2.
- **Where:** interview/2025/questions.yaml s2.household_employee (prompt).
- **Fix:** Prompt: "Did you (or, on a joint return, your spouse) pay any one of them $2,800 or more in 2025, ..." (the rest unchanged). No fixture: values unchanged.
- **Fix lines:** s2.household_employee
- **Siblings checked:** s2.household_employee_if_help
- **Severity:** low
- **Tags:** Schedule 2, Schedule H, spouse phrase; fixed
