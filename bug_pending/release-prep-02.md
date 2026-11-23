## BUG-NEW-release-prep-02 — Return generator still names two ids T-353 renamed (sc.line16b, f5695.line12)

- **Date:** 2026-11-23
- **Caught by:** release preparation of next (7466debd): rerun_all.py --kinds classm --dry-run could not build the class M requests of person, sa and sc (classm-jobs: person[taxpayer].sc[biz_a].line16b: input is not declared).
- **Symptom:** engine/src/generate.ts lists Schedule C expense inputs by bare name (SC_EXPENSES) and Form 5695 inputs that are often nonzero (EXTRA_NONZERO_PERCENT). The T-353 rename (sc.line16b to sc.interest_other, f5695.line12 to f5695.carry_in) did not reach these lists: every generated return with a Schedule C carried an undeclared input, so classm-jobs, and every step that evaluates generated returns (properties, the engine differential, mutation, compare), failed or would fail; the Form 5695 carryforward lost its nonzero weighting silently. The light tier does not evaluate generated returns, so commits on next passed.
- **Where:** engine/src/generate.ts (SC_EXPENSES, EXTRA_NONZERO_PERCENT); tools/rename_ids.py and the rename's own search, which matched dotted ids only.
- **Tool change:** generate.ts names interest_other and carry_in. The other 67 renamed ids were searched for in engine/src, ui, lean and tools as dotted ids and as bare quoted names beside their form: no other use.
- **Evidence:** classm-jobs --docs person (and sa, sc) builds its jobs; rerun_all.py --dry-run prices person, sa and sc.
- **Severity:** medium
- **Tags:** tool, generator, rename, T-353, fixed
