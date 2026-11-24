## BUG-NEW-lane-lints-20 — qdcg.line13: its label prints the 2025 amount of qdcg.fifteen_rate_ceiling, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** rp-25-32 (2026) p. 13, "Married Individuals Filing Joint Returns and Surviving Spouse $98,900 $613,700"; rp-25-32 (2026) p. 13, "Married Individuals Filing Separate Returns $49,450 $306,850"; rp-25-32 (2026) p. 13, "Heads of Household $66,200 $579,600"; rp-25-32 (2026) p. 13, "All Other Individuals $49,450 $545,500"; research/ty2026/params-2026.proposed.yaml qdcg.fifteen_rate_ceiling (source: final)
- **Symptom:** The label of qdcg.line13 prints "Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household". The line reads qdcg.fifteen_rate_ceiling, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/qdcg.yaml qdcg.line13 (label), as adopted for 2026.
- **Fix:** changes/2026/qdcg.labels.yaml, entry BUG-NEW-lane-lints-20: a set of the label to "Enter: $545,500 if single, $306,850 if married filing separately, $613,700 if married filing jointly or qualifying surviving spouse, $579,600 if head of household" (verified: final). No 2025 text or value changes.
- **Fix lines:** qdcg.line13
- **Siblings checked:** qdcg.line14
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
