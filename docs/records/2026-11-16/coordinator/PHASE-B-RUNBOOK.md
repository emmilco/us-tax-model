# Phase B runbook: night of 2026-11-15/16 (coordinator)

The durable plan for the fix round after release r2026.11.15.1. A later session resumes from here: read
coordinator/morning-report-notes.md first, for state, then this file.

## Principles (owner goal, ~01:20)
- Atomic units: each lane's output is a commit on its own branch in its own worktree, plus a note in
  docs/provisional/lanes/<lane>.md. Nothing reaches `main` until the combined round passes. An interrupted lane leaves
  only its worktree, which is discarded or resumed.
- Combine the expensive checks. Lanes run targeted checks only (build, test-fixtures, interview-coverage, tick-groups,
  draft-walk on their personas, and the fast tier once at the end). Then: one merge, one paid review round on the
  changed lines and forms, one release-review sample round, and ONE release-mode full check, which is also the
  release's run (the skip path).
- Before the full check, run the fast-failing steps directly: check_extraction (us and ny), check_limits,
  year_changes --check, check_logs (us and ny), release_reviews.sh, citations --strict, check_consumers,
  bug_status --check, doc_figures --check, check_bug_inventory, check_agent_runs, interview-coverage, tick-groups.
- Bottleneck: about 75 min for a release-mode full check, and 2 check slots per machine. Keep CPU work off the
  critical path (renice +15). Builds: about one per two cores.

## Order
0. B0 (coordinator, after the release): the records commit on `main`: docs/records/2026-11-16/ (the nightplan md
   files, patches v1/v2/v3, small edit scripts; no scratch file copies), the protocol 8.10 additions
   (coordinator/protocol-8.10-additions.md plus the fast-failing-steps lesson), task row T-337, and the re-appended
   agent_runs rows. Docs tier.
1. S0 (Sonnet, mechanical): archive p936, p926 (2025, from the irs-prior URL) and i1040sh per
   nightplan/sources/README.md. Its own small commit (full tier if check_extraction runs on sources: run it first).
2. Wave 1 lanes, in parallel worktrees cut from the post-release `main` (lane-briefs.md L1-L6), each applying the v2
   patch, then the v3 lows add-on, in the order its .md gives:
   - L1 pay: inc-m12.base + inc-m12.cod (owner: option B) + inc-m12-lows (v3) + the jr.patch parts for scope.recovery
     and f1040.digital_assets (check the order in round4/jr.md)
   - L2 amtpay: int-amt, then inc-m34, then inc-m34-lows (v3)
   - L3 rental: sche-a (v2) + sche-a-lows (v3) + int-rprop (owner: land) + the NY bond lows (0857, with int-amt:
     coordinate with L2)
   - L4 credits (Sonnet): older-credits (v2) + its lows
   - L5 ny: older-ny (v2) + its lows
   - L6 scha: older-scha (v2) + 0817a (owner: ask every giver) + its lows
   - jr community property (MEDIUM): household is touched only by jr.patch, so it is its own lane L8
3. Integration: merge L4, L5, L6, L3, L8, L1, L2 (the `inputs` claim moves between L1 and L2), resolve, number the
   pending entries, write closures (0911 field, 0629, 0092 and the lows.md list), regenerate reports. Then the paid
   review round: line-scoped transcription and render, class M only where arithmetic changed, rerun_all with
   --approve-cost; adjudicate with Opus forks by family; then release_reviews.sh, its samples and rulings.
4. Wave 2 (in parallel with step 3's reviews, in its own worktree on the wave-1 merge): L7 interview (int-p18,
   int-personas, int-n10, int-n10-ticks (owner: applies)) + int-lows. Merge before the full check if it is ready,
   else the next round.
5. Fast-failing steps, then the release-mode full check through check_all_bg, then commit, ff, push, and release.sh
   (a skip run), tag r2026.11.16.1.
6. Tooling lands, as its own units, after step 5: tooling-1 (blob guard), tooling-2 (fixture-gate; resolve its
   flags), tooling-5 (skip test), tooling-4 (age limit), tooling-3 (owner decision on 2026 engines: defer). mutate A/B
   only in a window with no check running.
7. Coverage expansion next (when the backlog is clear): the K-1 integration (round4/k1int.md), then k1e
   (round4/k1e.md), then Form 8615 (round4/scout-8615.md), under the coverage expansion protocol.

## REVISION ~01:45: one apply-chain lane, not six parallel lanes
Nearly every patch edits interview/2025/questions.yaml, and the v3 add-ons apply only at the END of the v2 chain
(round4/lows-sche.md). int-rprop's bank hunks must be redone with its script after sche-a
(scratch/round4-lows-sche/apply_bank_chain.py). Parallel lanes would each pay a merge of the same file, so wave 1 is
ONE lane in ONE worktree:
  F1 (Opus, judgment) applies the chain in sequence with `patch -p1 -F0`, committing after each patch (an atomic unit:
  each commit is one patch, and an interrupted run resumes at the next patch):
    sche-a, int-amt, int-p18, int-personas, int-n10, int-n10-ticks, int-rprop (bank by script), inc-m12.base,
    inc-m12.cod, inc-m34, then the v3 add-ons: sche-a-lows, int-lows, inc-m12-lows, inc-m34-lows, older-* (v2) and
    their lows, jr.patch (order per round4/*.md).
  After each commit: build; after the chain: test-fixtures (us, ny), interview-coverage, tick-groups, draft-walk of
  the affected personas, render. Failures are fixed in their own commits, citing the patch.
Parallel work that doesn't touch questions.yaml runs beside F1: S0 sources; tooling-5 (the skip test, tests only);
the mutate A/B (no check may be running).
- Review tooling unit (its own commit, before the paid review round in step 3): screens.patch + screens-joint.patch
  (round4/screens.md). All 149 federal and 12 NY screens become due, and their re-review rides in the same round
  (~$21). Skip the migration: the joint fix moves every subject anyway.
- Tooling unit T-store (fast tier, its own commit, can run beside F1 because it touches only tools/transcription):
  store-dedup.patch; run its 4 unit tests and roundtrip_store.py; then tooling-1 without large_blobs.txt. The clone
  proof plus `share --write` on old records is a later unit.
- 2026 units (beside F1: they don't touch questions.yaml), each its own commit, fast tier unless the corpus hash
  changes:
  Y1 land R7+R8 from ty26-r8 with the realty_year fix (round4/r78-2026.md section 4) and assign the 11 entries;
  Y2 operations for the 3 recovery-year constants + the realty_recovery_year table (Opus);
  Y3 stage the 37 parameters (Sonnet for kept constants, Opus for indexed values);
  Y4 the 8 catalog rows (Sonnet); T-321 row closure.
  The T-317 rehearsal (~5.5 h of CPU) runs only when no check is pending; probably the next day.
- N10 trim pass (after F1's chain, before the review round): one Opus lane lists every prompt, label and help over
  the N10 limits in the changed entries, and trims each without losing its guard (red-team every cut). Overruns
  that must stay go to the owner with the named wrong answer each one prevents.
- F1 step after fix-round.patch: apply round4/trimA.json and trimB.json with a YAML-aware script (the "old" values are
  parsed YAML values), applying the coordinator's overrides listed in morning-report-notes (k1p.t6 standard wording;
  skip the edu_over books-rule cut). Then build, tick-groups, interview-coverage, draft-walk.
