## BUG-NEW-lane-lints-30 — sli.base_joint: its label prints the 2025 amount of sli.base_joint, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** rp-25-32 (2026) p. 23, "modified adjusted gross income in excess of $85,000 ($175,000 for joint returns)"; research/ty2026/params-2026.proposed.yaml sli.base_joint (source: final)
- **Symptom:** The label of sli.base_joint prints "Year parameter sli.base_joint ($170,000)". The line reads sli.base_joint, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/sli.yaml sli.base_joint (label), as adopted for 2026.
- **Fix:** changes/2026/sli.labels.yaml, entry BUG-NEW-lane-lints-30: a set of the label to "Year parameter sli.base_joint ($175,000)" (verified: final). No 2025 text or value changes.
- **Fix lines:** sli.base_joint
- **Siblings checked:** sli.line5
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
