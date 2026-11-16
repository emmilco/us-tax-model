# Morning report, night of 2026-11-15 to 11-16 (corrected, state at about 07:25 EST on 11-16)

**Superseded in part.** This report describes the state at about 07:25. After it, the release was restructured: the
expansion, the mutation-survivor work (372 unexplained survivors to 0, 5 listed under an open defect), the tooling
(T-337, T-338), the sources and these records went into one release commit through one release-mode check. Where this
report gives a different order or status, `coordinator/morning-report-notes.md` in this directory is authoritative,
and the open owner decisions are restated in `post-release/OWNER-DECISIONS.md` in this directory.

Rewrites the 00:40 draft (`nightplan/MORNING-REPORT.md`) using the coordinator's notes, whose end is authoritative.
Marks: **[measured]** I read it from a file or command in this pass. **[notes]** relayed from the coordinator's
notes without re-checking. **[unverified]** I could not check it.

## 1. In one paragraph

Only the B1 fix round (`acde74b5`) is on `main` [measured: `git log`, and `origin/main` is the same commit]. The
coverage expansion (rental, Form 8582, royalties, Form 1116, digital assets, MFS, dependent filers) is not committed
to `main`. **The release is deferred.** At about 06:30 you decided it waits until the 372 mutation survivors are
killed or explained; you first chose a waiver, then reversed it [notes]. The fast tier on the expansion tree failed at
about 06:50 (5 steps, all repaired or being repaired), so the expansion commit is still pending [notes]. A witness
search and four fixture lanes to kill the survivors were launched at about 07:20; none has reported [notes]. The
coverage estimate is 85.9% (was 78.4%) [notes; the 00:40 draft read it from `docs/COVERAGE.md`].

## 2. What landed

- On `main`: `acde74b5` (22:31, pushed 22:33), the Goal-1 consolidation round, eighteen fix lanes, BUG-0656 to
  BUG-0764, full check green on tree 815a7955 [notes]. Earlier on 11-15: `c556c598`, `a2f24909`, `8a5a25d8`,
  `66a808c8` [measured: `git log`].
- `git status` of the main checkout shows only a modified `research/costs/agent_runs.jsonl` (hook rows) [measured].
- The expansion tree (aebecaa7 on `acde74b5`) is committed on the scratch ref `refs/scratch/xint-fast` at 6649c637,
  for the mutation lanes to start from. It is a scratch commit, not the release commit [notes; I did not check the ref].
- Corrections to the 00:40 draft:
  - The 65 agent-run rows saved in `/tmp/main-agent_runs.2230.jsonl` WERE re-appended, by XINT at step 0 (310 to 375
    rows; `check_agent_runs` OK) [notes]. They are in xint, not yet in `main`. The rows for lanes D1 to D6 and the D6
    fork were written by the agent hook, no manual rows needed [notes].
  - The stale form claims (41, from the landing and interview-redraft lanes) DID refuse B1's first commit attempt
    [notes: observed]. They were released at the landing.

## 3. Ready, not landed

All inputs are in `docs/records/2026-11-16/` once committed. Nothing below is on `main`.

| Unit | State [notes] |
|---|---|
| Expansion (xint) | 9 of 11 steps passed by 04:20; fixtures 2386/2386, NY 358/358. X-MUT re-pinned 65 stale mutation arguments, ny_mutate exit 0. X-K1 added `scope.k1: true` to 19 refuse fixtures; refusal_reach exit 0. Federal mutate exit 1: 372 survivors that were there before (by form: f1116sb 65, k1s 56, k1p 49, rental 38, person 34, f1116col 24, rec 17, f8582 16, f1116 14, sche 8, royalty 8, f7203 5, eic 4, about 35 smaller). Fast tier then failed in 5 steps (xleak sibling lists, 3 stale consumers, bug_status, dependent review logs); XINT repaired them, ran the paid reruns ($2.40) and was to run the fast tier and `commit_tested.sh` |
| F1 fix round (branch `fix-round-1`) | 79-file patch plus the trims, build green after F1b fixed 11 errors. Fixtures 2404/2406 (the known pre1996 pair), NY 361/361, coverage 0, tick-groups 0, walks 2 problems (the same two on base; was 19). 29 files staged with personas 23 to 31 (those 9 personas walk clean, figures equal the hand-derived values for the 7 that complete; not checked against IRS tables). Needs a rebase onto the expansion commit, then group D (interview-rules, about 10 findings) |
| Tooling (T-337, T-338 and the 26-name rename migration) | patches apply clean in order; their self-tests pass. 18 code self-test rows failed only for environment (no build or node deps in scratch); rerun in the landing tree |
| S0 sources | 20 source files (p936, p926 2025, i1040sh, usc 402 and 457), 5.2 MB patch (not in the records tree). Apply only the 20 files and re-add the JSON rows in `round6/s0.md`; do not apply the catalog hunks wholesale |
| K-1 stack, Form 8615 | patches in `patches/v4/`; V1 and V2 (build validation of F2, F3 and the K-1 stack) had not reported at 07:25 [unverified]. 8615 is held until the K-1 integration and the owner answers in section 7 |
| Mutation survivor lanes (M-1116, M-K1, M-rental, M-exist; MW witness search) | launched about 07:20, waiting for the witness lists |

## 4. What the night found

- **Community property (medium):** `household.community_property` asks where the filer lived, not domicile (Pub. 555).
  Patched in F1 (`household.spouse_cp_domicile` plus helpers) [notes].
- **Four owner questions answered from the sources (round 6, lane R1)** [notes; the drafts are in `bug_pending/`]:
  1. Rental-only costs divided by days: moderate reading that they should not be (Pub. 527 pp. 23-24, Worksheet 5-1 line 2d). Medium.
  2. Thrift-store clothing refused under "belongings the charity will not use": strong that the text does not require it (Pub. 526 p. 19). Low.
  3. Form 8853 line 22 counts the gross cost "whoever paid"; line 24 counts only what was "paid back to you". Inconsistent on either reading. Medium.
  4. S corporation K-1 box 17 A and B: neither refused nor carried to Form 4952 (strong that the instructions treat them like partnership 20A/B). Low, latent.
  Also: the AMT cap reaches every child under section 1(g) (moderate), but f8615.kid's questions are reached only above $2,700, so the patch may behave as the narrow reading; check when Form 8615 is validated.
- **Tool findings:** `check_extraction` pdfkit exceptions fixed (BUG-0927); the fixture runner ignores an input behind a
  gate answered No with no warning (`engine/src/eval.ts:843`); `transcribe.py` `catalog_selection` drops computed
  helper lines (fixed in xint); a missing-engine run still records as release (`run_engines.py:628`); `rename_carry`
  missed collection-indexed keys (5 steps failed on it).
- **Test-drive:** a server on port 8791 serves the release candidate tree 9ddb71b6 (profile ny) with logs in
  `~/Documents/Tax-Interview/rc-2026-11-16`; your logs there are walk evidence for T-332 [notes].
- **Incidents:** a recursive shell function `wc` spawned about 6,700 processes for about 2 minutes (about 00:05); the
  what-if report delayed the first release check by about 35 minutes; the pre-release gate failed twice (13 minutes,
  then 52). Their lessons are in the section 8.10 additions.

## 5. Spend

- **Paid review calls** [measured: xint `.transcription/costs.jsonl`, rows dated 2026-11-15 or 11-16 UTC, last row
  06:54 EST]: **$388.90 over 1,574 calls**, all `claude-opus-5-5`. By kind: class M $163.83, transcription $80.08,
  render $55.13, screen $39.01, false-no $30.96, completeness $19.90. The 00:40 draft read $384.71 for the same window
  shape.
- Of that, $5.66 (11 calls) is dated after 23:57 EST on 11-15 [measured].
- Not in that file at its last row [notes]: the dependent transcription and render reruns, $2.40 (1.91 and 0.48),
  and a dependent class M log of about $1.77 that you approved. The $85.82 reported at 23:55 as spent on release-sample
  reviews is a coordinator figure [notes]; I could not tell whether it sits inside the $388.90.
- Agent runs: `research/costs/agent_runs.jsonl` holds no dollar costs (subscription usage) [measured: 378 lines in the
  main checkout, including the hook rows]. Rows now carry model, class, year and jurisdiction.

## 6. What I could not verify

- Whether the 5 failed fast-tier steps are all fixed, and whether the expansion commit exists: the notes end at the
  repair.
- Whether the mutation lanes found witnesses for the 372 survivors.
- The V1 and V2 validation results; the `round6/v1.md` and `round6/v2.md` files did not exist when I copied.
- Whether the $85.82 is inside the $388.90.
- The `refs/scratch/xint-fast` commit and the worktrees named in the notes were not inspected.

## 7. Decisions for you

Each is self-contained. A "default" is what the coordinator has done meanwhile under delegation.

1. **Rental-only costs (draft bug rec-01).** Pub. 527's worksheet for a used-as-home dwelling deducts advertising and
   agency fees whole; the model divides every rental expense by rental days over total days when the dwelling had
   personal use but was not used as a home. Do rental-only costs stay whole? Recommend yes (moderate reading). Default:
   the release would ship as is, like the 42 open mediums; file the bug after.
2. **Thrift-store donors (rec-03).** The gift question "art or other belongings the charity will not use" refuses used
   clothing donors, though the unrelated-use rule reduces only appreciation. Narrow it to property worth more than
   the donor paid and held over a year, or keep the over-refusal? Recommend narrowing (low severity, a design call).
3. **Care payments made straight to the provider (rec-02; owner decision 8).** Form 8853 line 22 counts the cost
   "whoever paid", line 24 only what was "paid back to you". Count Medicaid and VA payments to the provider on both
   lines, or on neither? Either way the lines must agree. The fix-chain patch chooses both (line 24 counts them).
   Related open medium BUG-0873 has the same line 24 wording.
4. **S corporation K-1 box 17 A and B (rec-04).** Add a per-K-1 tick when box 17 has an amount, refuse Form 4952
   whenever an S corporation K-1 shows box 17, or accept the gap? Default: refuse, until you pick.
5. **Form 8615 sources.** `f8615` and `i8615` are printed 2025 revisions ("Created 9/9/25"; "Oct 22 2025") but marked
   "not cleared for encoding" in the manifest. Clear them, or the area cannot count as covered. Also: does the child AMT
   cap reach all children under section 1(g) (moderate) or only the narrow reading the patch may implement?
6. **Release after the mutation survivors.** You chose to fix the 372 survivors first. Confirm that the combined plan
   stands (expansion commit on a green fast tier, then F1, tooling and sources, then the survivor lanes, then ONE
   release-mode check and the tag), or say if you want the release earlier.
7. **ftc.taxes order.** To stop the foreign-tax question coming after later topics, a filer who is refused later
   answers one extra amount first. Default: accepted at order 272. Revisit?
8. **Dependent read order.** Reading `household_all_year` before `spouse_relative` changes the case
   `stage8.mut.mfj_spouse_relative_all_year_unanswered`. Default: keep the order; confirm.
9. **Holds and tool gates.** 0570b (up to 35 fixture cases may newly refuse) and 0719 (needs usc-26-402 and 457,
   Pub. 525 p. 9 reads against it) are held. Tool patch tooling-3 (a run missing an engine fails the release) would
   block 2026 releases until the engines support 2026; tooling-4 (24-hour age limit on release entries) lands after
   the release. Approve, hold or reject each.
10. **Items still open from the 00:40 draft** that your 01:15 answers did not settle (the plan default applies):
    BUG-0790 boats (v2 refuses every boat); the NY item C spouse case; `amb.2025.ira_age50` reason against the
    i1040gi child-age rule; the A-F1 refusal timing and A-F2 sign-off (`sa.line1` from Form 1095-A).

## 8. Cleanup after the landings

Worktrees s0, t1, v1, v2, mw, m1116, mk1, mrental, mexist, p1; `refs/scratch/xint-fast`; `/tmp/t1-xint.diff` (271 MB);
`refs/scratch/f1-base`. A 71.5 MB review-store file is over GitHub's 50 MB warning; the dedup and the 50 MiB guard are
in the tooling patches [notes].

---

Provenance. Inspected: the coordinator's notes (whole file), the 00:40 draft, `git log` and `git status` of the main
checkout, xint `.transcription/costs.jsonl` totals, the line count of `agent_runs.jsonl`, the lane files named above.
Inferred (unverified): everything in section 3 beyond the notes, and the outcomes in section 6.
