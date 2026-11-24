## BUG-NEW-lane-lints-10 — eic.step2_income: its label prints the 2025 amount of eic.investment_limit, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** rp-25-32 (2026) p. 15, "investment income exceeds $12,200."; research/ty2026/params-2026.proposed.yaml eic.investment_limit (source: final)
- **Symptom:** The label of eic.step2_income prints "Step 2, question 2. Investment income not more than $11,950 (more than $11,950 stops at question 3 without Form 4797)". The line reads eic.investment_limit, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/eic.yaml eic.step2_income (label), as adopted for 2026.
- **Fix:** changes/2026/eic.labels.yaml, entry BUG-NEW-lane-lints-10: a set of the label to "Step 2, question 2. Investment income not more than $12,200 (more than $12,200 stops at question 3 without Form 4797)" (verified: final). No 2025 text or value changes.
- **Fix lines:** eic.step2_income
- **Siblings checked:** eic.from_step2_income, eic.wsb_line5_stop
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
