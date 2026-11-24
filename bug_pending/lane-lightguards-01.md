## BUG-NEW-lane-lightguards-01 — Closure: BUG-1122 is fixed; the unread-parameter check runs in the light tier, and hsa.no_months is removed

- **Date:** 2026-11-24
- **Caught by:** lane lightguards (claude-opus-5-5, judgment): tools/check_unread_params.py on next d60f83a9 reported four parameters that no form, interview, change file, engine source or tool names: ny.est.min_due, ny.est.share and ny.est.high_agi (params/ny/2025.yaml; BUG-1122) and hsa.no_months (params/2025.yaml).
- **Closes:** BUG-1122
- **Closure:** fixed
- **Tool change:** params/ny/2025.yaml drops ny.est.min_due, ny.est.share and ny.est.high_agi; params/2025.yaml drops hsa.no_months, with its staged 2026 value (research/ty2026/params-2026.proposed.yaml, params_auto.json). No form line reads any of them (a whole-name search of forms, interview, changes/2026 and the code; the committed reports/ny/2025/mutation.md explains the three ny.est mutants by the rule 'Unread parameter'), so no value, refusal or question changes. New light-tier step unread_params (tools/check_unread_params.py) fails on any parameter of either jurisdiction no reader names; the eight EIC Table parameters eic.earned_amount0-3 and eic.maximum0-3, read by built names in engine/src/conjecture.ts and tools/engines/compare.py, are listed in tools/unread_params_allow.json, so the reason of the mutation rule 'Unread parameter' (it serves a cross-check outside the computation) is true of every parameter it now applies to. ny_it201.gate.estimated_penalty still refuses without the $300 and 10% test of ny_it201i Line 81, as before (the conservative over-refusal BUG-1122 describes).
- **Evidence:** python3 tools/check_unread_params.py: 4 problems on d60f83a9, 0 after (566 parameters, 8 by a built name); grep of the tree outside reports/, rendered/, research/ and the review store finds no other mention of the four keys.
- **Severity:** low
- **Tags:** ny, params, mutation, tools, fixed
