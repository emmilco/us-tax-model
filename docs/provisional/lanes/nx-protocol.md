# Lane nx-protocol: the coverage expansion protocol (draft)

Model claude-opus-5-5, judgment class, year 2025, jurisdiction us. Worktree `.claude/worktrees/nx-protocol`; base
`63a20efc` (snapshot of the landing plus TY2026 batches A and B). Not committed. No build, no check-all, no paid
reviews, no model calls from code. One read-only Opus subagent summarized the `land3-*` and `ty26-*` lane notes.

## What was written

- `docs/2026-11-15_coverage_expansion_protocol.md`: the procedure, sections 0 to 10. Items marked [R] are for the
  owner to confirm; items marked [unverified] could not be checked.

## Decisions made in the draft (for the owner)

1. **Entry gate.** A round starts only on the owner's opening decision (charter 1, item 3). The charter has no
   section on coverage growth after consolidation; only 1.3 ("waits until the project is stable").
2. **Where coverage is built.** In the newest adopted year. A new form needs next-year operations only when
   `changes/<N+1>/` exists (section 7.1); otherwise adoption carries it (section 7.2).
3. **D12** carried as the rule after adoption. It is flagged because T-300 still lists that owner decision as open.
4. **Next-year change ids** `C-<ROUND>-<FORM>-NN`, appended to the change map. A convention: `year_changes.py`
   does not check ids against the map.
5. **The `inputs` claim serializes new inputs** (verified in `claims.py` `check`). Recommended: lanes commit in turn
   when called in, with the integrator releasing `inputs` between them. A per-form inputs claim is a tool task.
6. **A full tier per batch merge,** although the hook requires only fast. The bar for "covered" needs mutation, the
   Lean comparison and the engine differential.
7. **At most six build lanes at once.**
8. **Engine differential work as a follow-on lane** (full-tier paths).
9. **"Covered" is claimed at a release, not at a merge.** The bar is in section 6.5.

## Not verified

- How `880445b2` (seven parents) was assembled when lanes conflict.
- When adapter and input contracts are required for a new form, beyond their READMEs.
- Whether the committed estimate's percentages are stale. `reports/2025/filer_coverage.*` is dated 2026-11-01 and
  lists 188 gates, including the removed `scope.credits`; `docs/COVERAGE.md` lists 234. `estimate.py` was not run
  (this worktree has no `.engines/`).
- Coverage figures disagree: spec 2.4 says 82.2% after Stage 21; the charter, COVERAGE.md and the report say 78.4%.
  Not reconciled.
- `fetch_sources.py --derive`: taken from ADOPTION.md, not run.

## For the coordinator

- The protocol cites `docs/provisional/lanes/ty26-plan.md` (D10, D12) and the `land3-*` notes. If those notes are
  archived, the citations need restating.
- No `TASKS.md` row was written.
