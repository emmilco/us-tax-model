# 2026-11-23: the 2026-11-22/23 wave integrated on `next`; `main` unchanged and unreleased

**State (2026-11-23).** `main` = `870cc146` (round F); last release `r2026.11.16.1`; nothing of this wave is released.
`next` holds every lane of the wave, oldest first: `9a2b3e9c` (release gating: next/main split, light commit tier,
preflight), `f4d8ea31` (batches 1 and 2: rollover tools T-339 to T-346, 2026 parameters and finals refresh, closures,
wording and round F fixes; BUG-0998 to BUG-1118), `ed6c46ea` (five lanes: speed, rb, left, wk1, wk2; BUG-1119 to
BUG-1128), `25e48ec0` (six lanes: ty26-ops, hh, adlow, fx-seqbi, fx-eduhsa, fx-capital; BUG-1129 to BUG-1172),
`8175c23d` (three lanes: advfix-land with the retirement findings, fx-ny with nyfix, fx-itemized; BUG-1173 to
BUG-1224), then the commit holding this entry (the `worktree_data.py carry-back --keep-main` option, ledger-fix
`3bb2046c`, and this entry). Each integration commit's message lists its lanes, merge resolutions and review debt.
The wave's worktrees are archived (`tools/worktree_gc.py archive`); their review data is carried back to the main
checkout.

**Owner decisions (2026-11-23).** EIC self-only age (`amb.2025.eic_self_only_age`): the Pub. 596 reading. EIC head of
household with a nonresident spouse (`amb.2025.eic_hoh_nonresident_spouse`): the Pub. 596 reading, unchanged. HSA split
(`amb.2025.hsa_split_spouse_eligible`): only the shared family months are split, as built in fx-eduhsa. Charity band
(BUG-1204): kept as built; refuse past the 60% and 30% legal limits, below them `sa.charity_limited` decides.

**Open work from `.claude/wave-2026-11-22/after-int-queue.md`**, each checked against this tree on 2026-11-23:
- W2 guard (offer `scope.nol` only after a business or disaster route): not built; `scope.nol` has no `gated_by`.
- W4 guard (re-ask when a non-land rental has an empty building list): no such check found in `forms/2025/rental.yaml`
  (searched, not walked).
- BUG-0993 (rental building basis prompt) and its `rprop.credit` help draft (`leftovers-check.md`): open.
- `samples.confirmed_bugs()` counting an id inside a "no defect" class (queue item 6), and `core.hooksPath` pointing at
  the main checkout's hooks (item 19; commits use `git -c core.hooksPath=tools/hooks commit`): neither is in
  `BUG_INVENTORY.md`; not filed.
- Agent-run rows of the wave (item 11): not in `research/costs/agent_runs.jsonl` on `next`. 53 rows of 2026-11-22/23
  sit uncommitted in the main checkout's working copy of that file; they reach `next` by a fold or a copy there.
- BUG-0764 (AMT line 7 over-refusal at $0 taxable income): open. The kill fixture drafted at
  `/tmp/scout-mutants/fixtures/amt_l7_zero_taxable_income.json` is not in the repository (unverified whether /tmp
  still holds it).
- Mutation survivors `s8812.line18a` and `person.f8919_line10` (item 14): both still argued in
  `reports/2025/mutation.md`; whether they were re-looked at after advfix is unverified.
- BUG-1124 (f2441 fixture), BUG-1127 (W7, one `sales.special` question per return), BUG-1136 (fx-eduhsa-05, an AOC ban
  also blocks the LLC): open. BUG-1125 (W5) is recorded fixed by a help change; whether the follow-up question for
  filers 16 to 23 is still wanted is unverified.
- adlow mediums BUG-1151 (NY S-201), BUG-1152 (NY railroad S-122), BUG-1154 (Roth-only excess contributions): open.
- BUG-1212 (New York itemize choice; the fx-ny-04 subject, owner's call; lane recommendation: leave filed as low): open.
- fx-capital and fx-seqbi leftovers, per their messages (not rechecked): code H not in the `sales.code` list;
  `qbi.prior_form` asked of filers without QBI; the generate.ts premiums-over-Form-7206 differential at release.
- T-353 is done on branch `rename-t353` (TASKS-DONE.md): the 67 ids and the two s2 add-back helpers are renamed in the 2025
  tree. `year_changes.py --check` still fails on 7 operations of `changes/2026/` (BUG-NEW-rename-t353-01), and 46
  pinned mutation arguments no longer hold (BUG-NEW-rename-t353-02); both were already true on `next` before the rename.

**Review debt the integrations recorded** (run before the release): class M person (BUG-1207's
`person.tip_employers` and the other person changes since fx-ny's run), sc and sa against the combined form changes,
and f1040 (no candidate matched the merged computation at `25e48ec0`; rerun on Claude at `8175c23d`, agree 589:
recheck whether that settles it, unverified); index lines current on neither side (transcription sa 1, sc 3; render sa
1, 4, 17; render s1 8a); `ny_it201` render 40 and 48 (ruled a finding of BUG-0762) and 1; household transcription
`hoh_fails`; the sampled screen, false-no and completeness reviews due at release (advland's, adlow's `f4952` gate and
screens, fx-capital's `sd.sold_other`).

**Tool bugs and other open entries:** BUG-1170 (`siblings.py --check` re-tests entries already committed on `next`),
BUG-1171 (`rule.py --amend` cannot set the drop flag on a ruled class M section), BUG-1214 (unscoped interview-rules
finds nine problems on `next` itself), BUG-1215 (wording of the three new New York screening questions). Because of
BUG-1171, integration 5 set the drop flag by hand on fx-ny's 33 New York whole-dollar class M rulings
(`amb.ny.2025.whole_dollars`; the count is that commit's) and removed those lines from their fixture cases, as every
earlier ruling of that ambiguity is set. Counted on this tree: every ruling naming the ambiguity has drop set, 76 in
`reviews/ny/2025/classm/ny_it201.rulings.json` and 172 across the New York class M rulings files.

**Open owner-facing points:** T-312, T-326, T-332 and T-333 (listed in the entry below); the IRS 2026 finals are still
expected December 2026 to January 2027 (T-011, T-322).

## State

<!-- figures:handoff-state -->
<!-- Generated by tools/doc_figures.py (check-all runs it with --check); do not edit between these markers. -->

- **Last release:** `r2026.11.16.1` (2026-11-16), the newest release tag before this commit; `git describe --tags
  --match 'r*'` gives the commits after it (a file cannot name the commit that holds it).
- **Figures**, read from this tree: `BUG_INVENTORY.md` 1,224 entries (highest BUG-1224), 116 open, 4 of them covered
  by a `TASKS.md` row (`reports/bug_status.md`); `TASKS.md` 72 rows not done; scoreboard 692 of 3,911 computed lines
  (17.7%, `reports/2025/evidence.md`); estimated filer coverage 85.9% of returns (`reports/2025/filer_coverage.md`);
  156 ambiguity entries, 152 linked to a line (`ambiguities/2025.yaml`).
<!-- /figures:handoff-state -->

- **Tax years:** 2025 is the only adopted year (`years.json`). 2026 is prepared, not adopted: the definition changes as
  operations in `changes/2026/`, parameters and tables staged in `research/ty2026/`, plan in `docs/ty2026/ADOPTION.md`.
- **Reviews:** a form is satisfied by any qualified family's current log (`tools/transcription/families.json`); new
  review calls run on Claude (`claude-opus-5-5`).

## What governs the work

Normative documents, by the kind of work. Read the one that applies before the first change.

| Work | Read |
| --- | --- |
| Any work | `CLAUDE.md` (the owner's standing rules: models, inference cost, worktrees, background waits, parallel lanes); `docs/consolidation_charter.md` (architecture, the verification system, the order of work, the documentation conventions in section 6) |
| Validation, rulings, human review | `docs/2026-10-24_validation_policy.md` |
| Adding or changing an interview question, topic or form | `docs/2026-11-13_interview_construction_protocol.md` |
| Bringing a refused form or situation into scope | `docs/2026-11-15_coverage_expansion_protocol.md` (owner decision 2026-11-15) |
| Releases and the check tiers | `docs/2026-11-05_release_gating_design.md` (approved 2026-11-05); `tools/README.md` ("Review rerun guards"; "Sampled completeness, screen and false-no reviews") |
| Tax year 2026 | `docs/ty2026/ADOPTION.md`; `docs/2026-11-14_year_change_operations.md`; `changes/2026/README.md` |
| New York | `docs/ny/INTEGRATION.md`; `docs/ny/2026-11-14_ny_year_handling.md` |

**Standing decisions** are in `CLAUDE.md`, `handoffs/HANDOFF-HARDENING-1.md` (the owner's decisions of the hardening
phase), `docs/provisional/DECISIONS.md` (questions of the interview redraft settled by the coordinator under the
owner's delegation of 2026-11-14; each says how to reverse it) and the `TASKS.md` rows that name an owner decision
(T-326 lists the 2026 preparation decisions taken on the owner's behalf, for the owner to confirm).

## What is a record, not guidance

These are records of past work. Cite them as evidence of what an agent did or found on a date; never follow them as
instructions, and check any claim in them against the tree before relying on it:

- `docs/provisional/lanes/` (one note per agent lane, with the lanes' `*_work/` scratch), `docs/provisional/walks/`,
  `docs/provisional/map_work/`, and `docs/provisional/STATUS.md`, `MAP.md`, `NORMS.md` (the redraft's working
  documents, superseded by the landing and the interview construction protocol). See `docs/provisional/README.md`.
- `docs/records/` (dated folders of a round's lane briefs, design scouts and coordinator notes, kept verbatim as worked
  examples for the coverage expansion protocol's section 8.7; placeholder ids in them are not rewritten).
- `handoffs/`, except `HANDOFF-HARDENING-1.md`; the archive of this file.
- Dated documents in `docs/` other than the normative ones above: each is a point-in-time document.

## Next

The order of work is at the top of `TASKS.md`. Open owner-facing points and open work are listed in the entry above.

# 2026-11-22 evening: release gating landed on `next`; integration wave in flight (superseded by the entry above where they differ)

**State (2026-11-22).** `main` = `870cc146` (round F, pushed); last release `r2026.11.16.1`. `next` = `9a2b3e9c`: round F
plus the release-gating change (next/main split, light commit tier, preflight, release-only full checks;
`docs/2026-11-05_release_gating_design.md`, amendment of 2026-11-22; `CLAUDE.md`, "Commit guard and releases"). Work is
committed on `next` or a lane branch, never on `main`; `main` moves only by `tools/release.sh`. A commit needs a green
light-tier run (`tools/check_all.sh`); the full tier runs only at a release.

**Owner decision (2026-11-22).** Back on Ultra: heavy parallel work in worktrees, with agent autonomy. The usage-scarcity
rule of 2026-11-16 has ended (`CLAUDE.md`). Reviews run on Claude (`claude-opus-5-5`; owner, 2026-11-21); DeepSeek is
qualified and not callable (`tools/transcription/families.json`).

**In flight, not on `next`** (check `git worktree list` and each branch before relying on this; none of it is released):
- `integrate-1` (worktree int1): about 500 staged files: year rollover T-339 to T-346, the 2026 finals, fixes for
  BUG-0998 to BUG-1113; BUG_INVENTORY.md highest entry there BUG-1118. [flight]
- `integrate-2` (worktree int2): batch 1+2, staged on `next`; the queue of
  `.claude/wave-2026-11-22/after-int-queue.md` waits for it. [flight]
- `adversarial-fixes` (advfix): fixes of the adversarial scouts' medium findings and T-333 mediums (Form 8919 reason code G,
  s2, s8812, retirement, person.yaml, scope.yaml); uncommitted. [flight]
- `ny-schedule-e` (nyfix): NY IT-201 line 11 and depreciation decoupling; staged. [flight]
- Lane branches off `next` (worktrees adlow, hh, left, rb, speed, wk1, wk2 ...): scout and fix lanes of the wave; each lane
  claims its forms with `tools/claims.py`. Their reports are in `.claude/scouts-2026-11-22/` and are testimony: confirm each
  finding against the archived source and the current YAML before fixing. [flight]

**Queued once integrate-2 is on `next`** (`.claude/wave-2026-11-22/after-int-queue.md`): the BUG-1094 closure (not a defect,
p970 p. 11); guards for W2 and W4; nyfix and advfix onto `next`; the 2026 operations of
`.claude/wave-2026-11-22/ty2026-ops-ready.md` (BUG-1031 AMT phase-out rate, BUG-1032 IRA rate labels, T-353 renaming of 67
ids; blocked until other branches release their form claims); BUG-0993 fix; the tool bug in `samples.confirmed_bugs()`;
the two pending nyfix defects (05 and 06).

**Open owner-facing points:** T-312 (redraft choices), T-326 (2026 preparation choices), T-332 (owner walk) and T-333
(judgment records) of the 2026-11-15 expansion areas. The IRS 2026 finals are still expected December 2026 to January 2027
(T-011, T-322).

Read first: `CLAUDE.md`, then `docs/2026-11-05_release_gating_design.md` (last section), `tools/README.md`, and the
"What governs the work" table of the entry above.
