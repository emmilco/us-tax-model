## BUG-NEW-rename-t353-01 — changes/2026: seven operations no longer apply to the 2025 tree on next

- **Date:** 2026-11-23
- **Caught by:** lane rename-t353 (T-353), running `tools/year_changes.py --check` on `next` (b18efa47) before the rename.
- **Symptom:** `year_changes.py --check` exits 1 with 7 failures on `next`, so the static checks of the applied 2026 tree do not run (they run only when every operation applies). Stale `from` values: qbi.yaml C-SCHED-31 op 3 (`qbi.carryforward` cite.locator); s8812.yaml C-SCHED-17 op 2 (`s8812.line22` cite.locator); sc.wording.yaml C-BUS-08 ops 1, 2, 3 and 5 (`sc.special` label, expr.source, cite.locator and the bank prompt). Dangling: person.s1a.yaml C-SCHED-03 op 1 removes `person.tip_reported`, which `person.tips_over_wages` still reads (the engine's static check of the applied tree reports the unresolved reference). The step `year_changes` is not in the light tier, so commits on `next` did not catch it. The rename of T-353 changes none of the seven (same failures before and after).
- **Where:** changes/2026/qbi.yaml, s8812.yaml, sc.wording.yaml, person.s1a.yaml; forms/2025/qbi.yaml, s8812.yaml, sc.yaml, person.yaml (the lines the operations expect).
- **Proposed fix:** re-base each stale operation's `from` on the current 2025 text after checking its `to` still says what the 2026 source prints; for C-SCHED-03, decide whether `person.tips_over_wages` goes in 2026 with `person.tip_reported` or reads its replacement, and add that operation.
- **Severity:** medium
- **Tags:** changes, year change, TY2026, adoption; open
