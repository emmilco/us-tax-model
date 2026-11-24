## BUG-NEW-lane-lints-16 — person.excess: its label prints the 2025 amount of ss.limit, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** iw2w3 (2026) p. 19, "For 2026, the amount should not exceed $11,439 ($184,500 × 6.2%)."; research/ty2026/params-2026.proposed.yaml ss.limit (source: final)
- **Symptom:** The label of person.excess prints "Withholding above $10,918.20, if any". The line reads ss.limit, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.excess (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-16: a set of the label to "Withholding above $11,439, if any" (verified: final). No 2025 text or value changes.
- **Fix lines:** person.excess
- **Siblings checked:** person.credit
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
