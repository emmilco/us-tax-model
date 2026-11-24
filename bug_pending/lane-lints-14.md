## BUG-NEW-lane-lints-14 — person.educator_max: its label prints the 2025 amount of s1.educator_max, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** rp-25-32 (2026) p. 17, "supplementary materials used by the eligible educator in the classroom is $350."; research/ty2026/params-2026.proposed.yaml s1.educator_max (source: final)
- **Symptom:** The label of person.educator_max prints "Year parameter s1.educator_max ($300)". The line reads s1.educator_max, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.educator_max (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-14: a set of the label to "Year parameter s1.educator_max ($350)" (verified: final). No 2025 text or value changes.
- **Fix lines:** person.educator_max
- **Siblings checked:** person.educator_limited
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
