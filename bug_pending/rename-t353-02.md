## BUG-NEW-rename-t353-02 — Mutation: 46 pinned equivalence arguments no longer hold on next

- **Date:** 2026-11-23
- **Caught by:** lane rename-t353 (T-353), evaluating every `EQUIVALENT_IF` argument's `holds` on the canonical build of `next` (b18efa47) before the rename, to tell the rename's digest moves from earlier ones (`npm run mutate` itself not run).
- **Symptom:** 46 keyed arguments of `engine/src/mutate.ts` `EQUIVALENT_IF` fail `holds` on the build of `next` (a premise digest moved, or a structural condition no longer met), among them arguments on f8889, f8962 (`marriage.no.then1` to `then4`), household, dependent, eic, sa, sc, sdtw, f5695, sche (`filter.sche.*`), ira, person and New York (`ny_it201.gate.spouse_nonresident`). The mutation step (`staleEquivalences`) would fail on each; it is in the full tier only. The T-353 rename moved none of them (the same 46 fail with the renamed names put back).
- **Where:** engine/src/mutate.ts EQUIVALENT_IF; the full list is printed by evaluating each argument's holds on canonical/2025 (or by `npm run mutate`).
- **Proposed fix:** run `npm run mutate` on `next`; for each argument it lists, re-read it against the current premises and re-record the digest, rewrite it, or remove it if its mutant is now killed.
- **Severity:** low
- **Tags:** mutation, tools; open
