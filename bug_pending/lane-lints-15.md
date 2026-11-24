## BUG-NEW-lane-lints-15 — person.eligible: its label prints the 2025 amount of ss.base, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** p15 (2026) p. 2, "The social security wage base limit is $184,500."; research/ty2026/params-2026.proposed.yaml ss.base (source: final)
- **Symptom:** The label of person.eligible prints "More than one employer and total social security wages over $176,100". The line reads ss.base, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.eligible (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-15: a set of the label to "More than one employer and total social security wages over $184,500" (verified: final). No 2025 text or value changes.
- **Fix lines:** person.eligible
- **Siblings checked:** person.credit
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
