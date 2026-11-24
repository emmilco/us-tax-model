## BUG-NEW-lane-lints-11 — f8853c.rate: its label prints the 2025 amount of f8853c.per_diem_limit, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** rp-25-32 (2026) p. 34, "chronically ill individual, is $430"; research/ty2026/params-2026.proposed.yaml f8853c.per_diem_limit (source: final)
- **Symptom:** The label of f8853c.rate prints "Year parameter f8853c.per_diem_limit ($420)". The line reads f8853c.per_diem_limit, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/f8853c.yaml f8853c.rate (label), as adopted for 2026.
- **Fix:** changes/2026/f8853c.labels.yaml, entry BUG-NEW-lane-lints-11: a set of the label to "Year parameter f8853c.per_diem_limit ($430)" (verified: final). No 2025 text or value changes.
- **Fix lines:** f8853c.rate
- **Siblings checked:** f8853c.line21_figured
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
