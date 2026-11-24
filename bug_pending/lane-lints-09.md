## BUG-NEW-lane-lints-09 — dependent.qr_income: its label prints the 2025 amount of qr.gross_income_limit, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** rp-25-32 (2026) p. 20, "the exemption amount referred to in § 152(d)(1)(B) is $5,300."; research/ty2026/params-2026.proposed.yaml qr.gross_income_limit (source: final)
- **Symptom:** The label of dependent.qr_income prints "Gross income under $5,200". The line reads qr.gross_income_limit, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/dependent.yaml dependent.qr_income (label), as adopted for 2026.
- **Fix:** changes/2026/dependent.labels.yaml, entry BUG-NEW-lane-lints-09: a set of the label to "Gross income under $5,300" (verified: final). No 2025 text or value changes.
- **Fix lines:** dependent.qr_income
- **Siblings checked:** none generated
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
