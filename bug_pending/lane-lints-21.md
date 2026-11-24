## BUG-NEW-lane-lints-21 — qdcg.line6: its label prints the 2025 amount of qdcg.zero_rate_ceiling, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** rp-25-32 (2026) p. 13, "Married Individuals Filing Joint Returns and Surviving Spouse $98,900 $613,700"; rp-25-32 (2026) p. 13, "Married Individuals Filing Separate Returns $49,450 $306,850"; rp-25-32 (2026) p. 13, "Heads of Household $66,200 $579,600"; rp-25-32 (2026) p. 13, "All Other Individuals $49,450 $545,500"; research/ty2026/params-2026.proposed.yaml qdcg.zero_rate_ceiling (source: final)
- **Symptom:** The label of qdcg.line6 prints "Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household". The line reads qdcg.zero_rate_ceiling, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/qdcg.yaml qdcg.line6 (label), as adopted for 2026.
- **Fix:** changes/2026/qdcg.labels.yaml, entry BUG-NEW-lane-lints-21: a set of the label to "Enter: $49,450 if single or married filing separately, $98,900 if married filing jointly or qualifying surviving spouse, $66,200 if head of household" (verified: final). No 2025 text or value changes.
- **Fix lines:** qdcg.line6
- **Siblings checked:** qdcg.line7
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
