## BUG-NEW-lane-lints-36 — s2.household_employee: the help leaves out pay to a student under 18 from every test, but it counts toward the $1,000 quarterly (FUTA) test

- **Date:** 2026-11-24
- **Caught by:** the question review of 2026-11-24 (claude-opus-5-5), sample #1 on the reworded question, ruled in lane lints (claude-opus-5-5, judgment)
- **Source:** i1040sh Line A (the under-18 exclusion is for the $2,800 test); Line 9, "Did you pay total cash wages of $1,000 or more in any calendar quarter of 2024 or 2025 to all household employees?", and Line 15 list only a spouse, a child under 21 and a parent as excluded
- **Symptom:** A filer who paid a 17-year-old student babysitter $1,200 in cash in one quarter answers No, following the help, and the Schedule H refusal is missed (FUTA tax left off Schedule 2 line 9).
- **Where:** interview/2025/questions.yaml s2.household_employee (help).
- **Proposed fix:** Limit the help's exclusion to the $2,800 test.
- **Proposed fix lines:** s2.household_employee
- **Severity:** low
- **Tags:** Schedule 2, Schedule H, wording, question review; open
