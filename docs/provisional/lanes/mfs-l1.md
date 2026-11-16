# Lane mfs-l1: married filing separately, opening and household

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree: `.claude/worktrees/mfs-l1`, base `refs/scratch/x1-base` (825024d8, detached, broken mid-merge as the brief
says). No paid reviews, no model calls, no commit, no claims; `check_all.sh` not run (brief); mutate not run (brief:
it runs at integration). Design: `docs/provisional/lanes/scout-mfs.md`; decisions: `docs/provisional/DECISIONS.md`,
section "MFS L1".

## 1. What the merge must know

- **Defaults** (`fixtures/2025/defaults.json`): the tree carries nx-b1's copy (brief) plus this lane's patch,
  `/tmp/mfs-l1/defaults_patch.py` (idempotent; run it on the merged file): drops the `ssb.lived_apart` default
  (now a derived line), adds `household.mfs_living` = `together_late` after `household.married_dec31`.
- **Shared files touched, by entry:** `interview/2025/questions.yaml` (new `household.mfs_living` at order 102 seq 4;
  `household.community_property` help reworded; `ssb.lived_apart` entry removed); `interview/2025/full.yaml` (target
  `household.mfs_spouse_notice`); `ambiguities/2025.yaml` (three new entries; `amb.2025.hoh_community_property` reason
  updated); `params/2025.yaml` (enum `mfs_living`, `household.mfs_living_else`, `ira.line2_apart`,
  `dc.exclusion_max_mfs`; cite parentheticals of `ira.line2` and `edu.magi_limit` no longer say a separate return is
  refused); `forms/2025/scope.yaml`, `f1040.yaml` (shared); `tools/coverage/categories.json`, `tree.json`;
  `interview/2025/refusal_notes.yaml` (the `s3.mfs` note is replaced by the `household.mfs_community_property` note).
- **`s1a.yaml` note** (no lane owns s1a): the form note said "married filing separately is refused through s3.mfs";
  rewritten, and `changes/2026/s1a.yaml` C-SCHED-01's `set_form note` op mended (from and to).
- **`s3.mfs` is kept** as a line (it still refuses at `f2441.line11` and `f2441.line26` in this tree; L3 removes
  those). Once L3 lands it has no reader and no `when:`: delete it then, or keep it as a helper (check the build's
  unread-line rule). `tools/coverage/tree.json` no longer places it and `categories.json` no longer names it, so
  `tree.py --check`/`estimate.py` may flag it until L3's change is merged.
- **2026 mends that need L3's tree** (written in `/tmp/mfs-declared-ids.md` for L3): `changes/2026/f2441.yaml` (the
  two `set refuses` ops of `f2441.line11` and `f2441.line26` quote the `s3.mfs` entries) and the `set_form note` op of
  `changes/2026/f8962.yaml`. This lane mended `changes/2026/scope.credits.yaml` (both lists) and `s1a.yaml`.
- **Fixture restatements (inputs only, the scenario's own facts):** f1040.json `stage9.eic.mfs.lived_apart`
  (+`household.mfs_living: apart_last6`, the case's "no shared principal residence for the last 6 months"),
  `stage10.ss.mfs_apart` (`ssb.lived_apart: true` -> `household.mfs_living: apart_all_year`); eic.json
  `stage9.mut.eic_mfs_child_same_home` (`eic.same_home: true` -> `household.mfs_living: together_late`); qdcg.json
  `tcw.mfs.b1`..`b5`, `tcw.mfs.bound1..4.plus99c`, `qdcg.mfs.ceilings` (+`household.married_dec31: true`); New York
  it201.json `ny.status.mfs.{40000,70000,120000,300000}`, `ny.refuse.hh_mfs` (+`household.married_dec31: true`, the null
  `w2[a].box2` dropped: it stopped the walk at the old refusal). Scripts: `/tmp/mfs-l1/restate_fixtures.py`,
  `/tmp/mfs-l1/restate_ny.py`, `/tmp/mfs-l1/add_fixtures.py` (all idempotent).
- **Approved end changes (scout D2), restated from the source:** coverage row `opening.separate` (now
  `proceeds: {f1040.status: mfs}`, with `household.married_dec31: true` and `household.community_property: false`
  answered); `stage4.refuse.married` (scope.json: `scope.ready` true; its nulls dropped, 3.1(c)); `ss.mfs` (s3.json:
  lines 11, 15 and Form 1040 line 31 $0, no W-2; nulls dropped).
- **For L5 (not restated here):** `/tmp/mfs-l1/l5_list.txt` (246 rows): every case that states `ssb.lived_apart` (now
  derived; the evaluator rejects it: `classm.ssb.2` fails on it), MFS cases stating `household.married_dec31: false`
  (now refused at `household.filing_status_conflict`), MFS cases stating `eic.same_home: false` (no longer read on a
  separate return; the same fact is `household.mfs_living: apart_last6`), and MFS cases without `married_dec31`
  (lines below Form 1040 line 12e are unknown for them; all such hand-authored cases pass on the lines they assert).
  Mostly `classm*.json` and `mutation.json`, whose failures are hidden on this base by `s2.amt_owed`/`sd.qof`.
- **Personas:** `14_mfs_separate_finances`, `16_refused_mfs_texas` (numbers from the scout; 15, the separated parent,
  is left to L4/L5, who own the dependent answers). Check for collisions with X1 lanes' personas.
- **Collision notes with lane F9** (`nx-f9` diff of household.yaml and s3.yaml, not applied): F9 edits household.yaml
  at the head-of-household considered-unmarried cite (l.488-496) and inserts `household.hoh_missed` and its helpers
  after l.1168 (a `refuses:` on the line before `household.hoh_fails`); this lane edits `household.joint_unmarried`'s
  label, the `household.filing_status_conflict` mfs alternative and cite (l.1573-1650) and appends seven lines at the
  end of the file: no overlapping hunk. In s3.yaml F9 adds refusal entries (Form 3800, Form 4136, Form 2439) to
  lines around Schedule 3 lines 6a-8, 12 and 13-14, and new helper lines; its hunk line numbers are against its own
  base, which differs from x1-base. This lane removes only the `refuses:` block of `s3.line11`, which sits directly
  before `s3.line12`: no shared line, but the two hunks may be textually adjacent at merge. F9's `hoh_missed`
  applies to single only; a married filing separately filer who is considered unmarried is not told to choose head of
  household (see 11).

## 2. What changed

Computed now: a married filing separately return of a filer married at the end of 2025 (or whose spouse died in
2025) who did not live in a community property state in 2025, through every line that was latent for MFS (status
parameters, tax table column, SSB, EIC, s1a, sa, sd, f8959, f8960, s3 line 11), except the sub-cases still refused
below and the forms the other lanes change (sa/s1/sli/ira/person: L2; f2441/f8863/f8962/f8889: L3; dependent: L4).

| File | Lines |
|---|---|
| household.yaml | new `household.mfs`, `household.mfs_spouse_notice`, `household.mfs_living` (Enum input, gated), `household.mfs_living_else`, `household.mfs_living_if_mfs` (gate line), `household.mfs_apart_all_year`, `household.mfs_apart_last6`, `household.mfs_community_property` (gate); `household.filing_status_conflict` mfs alternative `household.no` -> `household.joint_unmarried` (+cite); `household.joint_unmarried` label |
| f1040.yaml | `f1040.line1a` refuses `household.mfs_community_property` (first entry, before `roster_bad`, so the refusal comes at the community property question); `f1040.line6d` reads `ssb.has_benefits` too (+cite, ambiguity); new `f1040.line12b` (copy of `sa.mfs_spouse_itemizes`) |
| scope.yaml | `scope.ready_credits`: `s3.mfs` refusal removed |
| s3.yaml | `s3.line11`: `s3.mfs` refusal removed |
| ssb.yaml | `ssb.lived_apart`: input -> copy of `household.mfs_apart_all_year` (id kept; readers unchanged) |
| eic.yaml | new `eic.mfs_same_home`, `eic.same_principal_home`; `eic.step3_married` reads `eic.same_principal_home` |
| s1a.yaml | form note |
| params/2025.yaml | see 1 |

Questions (bank):
- `household.mfs_living` (new): "In 2025, when did your husband or wife live with you?" - "At some time from July
  through December (or all year)" / "Only before July" / "Not at any time in 2025". Help: "Time away for work, school,
  medical care or military service, when you expected to come back, counts as living together." Asked only on MFS, and
  only when a line reads it (benefits, EIC with a child; later IRA and Form 2441 line A from L2/L3).
- `household.community_property` help (reworded): "In these nine states a married couple's income belongs to both of
  them by law (community property). If you are married and file apart from your husband or wife, a Yes ends the
  interview here."
- Not asked any more: `ssb.lived_apart` (derived); `eic.same_home` on MFS (derived; still asked of a married head of
  household).

## 3. Decisions (DECISIONS.md, "MFS L1")

D1 refuse community property (rejected: compute Pub. 555); D2 approved end changes; D7 notices only (rejected: status
comparison advice); D8 no New York change. As built: `eic.same_home` kept (rejected: the scout's rename to
`eic.same_home_input`, which would have rippled through every fixture answering it); line 6d only with benefits
(rejected: every MFS apart-all-year return, which asks the living question of every separate filer); CP question kept
at order 103 (rejected: moving it to 100/3, which changes every filer's walk); temporary absences count as living
together for every test (rejected: physical separation for the all-year test).

## 4. Gates replaced and residual refusals

- Removed: `s3.mfs` at `scope.ready_credits` and `s3.line11` (L3 removes it at `f2441.line11`, `f2441.line26`).
- New: `household.mfs_community_property` (f1040.line1a; tree.json topic household; categories.json `mfs` category now
  names it; `refused` left at its default true: the category is claimed covered only at a release, protocol 6.5).
- Narrowed (made reachable): `household.filing_status_conflict` now refuses an MFS filer not married at the end of 2025
  with no spouse who died in 2025.
- Residual, other lanes: `f8889.mfs` (L3), `s179.mfs`, `sa.mfs_spouse_extra` (L2), `clcw.spouse_screen`,
  `f8962.alloc`, `dependent.qc_tiebreak` (L4).

## 5. Next year (protocol 7.1)

- Mended: `changes/2026/scope.credits.yaml` (C-SCHED-39: the `s3.mfs` entry dropped from `from` and `to`),
  `changes/2026/s1a.yaml` (C-SCHED-01 note op). `year_changes.py --check`: all 1254 operations apply.
- No operations for the new lines: the 2026 i1040gi (pp. 14-15, 31-33, 41, 44, 97, the text every new line cites) is
  not posted; awaited. f1040 2026 draft: lines 6d and 12b unchanged (scout [V], not re-read here).
- New parameters for `propose_params.py --from 2025 --to 2026`: `ira.line2_apart` ($91,000 per change map C-PEOP-08
  note, scout testimony), `dc.exclusion_max_mfs` ($3,750, C-CRED-11), `household.mfs_living_else` (unchanged), enum
  `mfs_living` (unchanged).

## 6. Defects

- `BUG-0765`: the `household.widowed_this_year` remedy still says a separate return is not supported (left
  because the remedy is an expected value of a household.json fixture).

## 7. For other lanes and requests

- L2: `reviews/2025/consumers.json` ruling `consumer:sa.mortgage_over_limit@i1040sca:p8` reason says the MFS halves
  "cannot apply because that status is refused at scope.ready_credits (s3.mfs)": now false. Params L2 needs are added
  (`ira.line2_apart`). Schedule 1 line 20 box may link `amb.2025.mfs_lived_apart_boxes`.
- L3: `dc.exclusion_max_mfs` added; the two 2026 mends above.
- Coordinator: Schedule 1-A tips and overtime parents are still asked on MFS before the status zeroes the lines (no
  lane owns s1a); `household.hoh_missed` (F9) covers single only, so an MFS filer who is considered unmarried is not
  pointed to head of household (a choice, not an error: MFS is allowed). NY lane (D8): `tools/ny_fixtures.py` assumes
  the federal refusal (scout l.435).

## 8. Verification (run and seen; base x1-base is broken, see the brief)

| Command | Result |
|---|---|
| `build`, `render`, `render --ny` | OK (after restating the five NY MFS cases; first builds failed on them) |
| `test-fixtures` (federal; before the last refusal-order change) | all lane cases pass: `mfs.m1.basic`, `mfs.m2.spouse_itemizes`, `mfs.m5.ssb_together`, `mfs.m6.ssb_apart`, `mfs.m7.separated_parent`, `mfs.m8.no_child`, six `mfs.household.*`, `ss.mfs`, `ss.mfs.two_jobs`, `stage4.refuse.married`, and every restated case; each matched its hand prediction on the first evaluation on a current build. 1406/2024 overall: 616 failures from the base (`s2.amt_owed`, `sd.qof`, `s2.mortgage_subsidy`), `stage4.sb.foreign_no_filing` (base, single), `classm.ssb.2` (states `ssb.lived_apart`: L5) |
| `test-fixtures --ny` | the five MFS cases pass with unchanged values; other failures are base (`s2.amt_owed`, `sd.qof`) |
| `interview-coverage --rows mfs.yaml opening.yaml` (final build) | every lane row passes; 1 problem: `opening.widowed_this_year_alone` (refusal on the background `$dependent` answer), not in this lane's rows and not touched by it [I: base, F9's dependent-reading helpers] |
| `tick-groups` | passed (on the build before the last refusal-order change) |
| `citations.py --strict` (final) | 0 findings |
| `year_changes.py --check` (final) | all 1254 operations apply |
| `check_consumers.py` | no finding on this lane's lines after 6 rulings (`household.community_property@i1040gi:p14`, five `eic.us_home` pairs that came due because eic.yaml changed; baseline entries moved to rulings); 33 new and 6 stale remain, all base |
| `check_false_no.py` | 0 new |
| `siblings.py --check` | fails on other lanes' pending entries (g1-f9, g1-t2, g1-t3) only |
| `tree.py --check` | flags `s3.mfs` (unplaced until L3 removes its last refusals) and six base gates |
| `check_bug_inventory.py` | fails on other lanes' citations only |
| not run / not finished | `interview-rules` (killed by the pauses, then dropped on the coordinator's instruction), `check_questions.py`, `check_screens.py` (timed out while paused), `mutate` (brief), `check_all.sh` (brief) |

## 9. Review debt (round 2, after the merge)

transcription + class M (arithmetic changed): household, f1040, scope, s3, ssb, eic; render (wording changed):
household, f1040, ssb, eic, s1a (note), plus the new questions' question review (`household.mfs_living`, the reworded
`household.community_property`); screen review kind gate for `household.mfs_community_property` and the reached
`household.filing_status_conflict` mfs branch; false-no review for `household.community_property` on MFS. Dry-run
estimate not run (no paid tooling in the lane).

## 10. Walks (final build; transcripts in `docs/provisional/walks/after/`)

| Persona | Before | After |
|---|---|---|
| 14_mfs_separate_finances (typical) | refused at `s3.mfs` right after the status [I: from the base row `opening.separate`, not walked] | completes: 128 questions on 59 screens, 1,804 prompt words, 3,489 help words (01_single_w2 on the same build: 126 / 57 / 1,767 / 3,404). The extra steps are the marriage and community property questions; `sa.spouse_itemizes` and `sa.spouse_extra` are asked too (L2's) |
| 16_refused_mfs_texas (refused) | refused at `s3.mfs` [I] | refused at `household.mfs_community_property` on its own answer, question 4 of 4 (after moving the refusal first on line 1a; before that it waited for the birth year) |
| filer with nothing in the area | 01_single_w2 unchanged in shape (126 / 57), not affected | |

## 11. Left open (rank order)

1. L5 restatements (`/tmp/mfs-l1/l5_list.txt`), then mutation at integration (pins on `household.filing_status_conflict`
   mfs alternative, `household.mfs_living_if_mfs`, `eic.same_principal_home`, `f1040.line6d`'s new term; the pinned
   arguments in `engine/src/mutate.ts` that name `ssb.lived_apart` as an input, l.1788/1956, may go stale).
2. Widowed remedy (BUG-0765).
3. Pub. 915 to archive (amb.2025.mfs_lived_apart); Pub. 555 if D1 is ever reversed.
4. Persona 15 (separated parent) after L4.
5. s1a tips/overtime parents on MFS (N8).

## 12. Coverage gain (estimate, not measured)

MFS is 2.6% of returns (SOI 2023 Table 1.2, scout). Removing `s3.mfs` makes MFS outside community property states
computable for every line the other MFS lanes also open; the scout's inference of +1.3 to +1.5 points (2.1 x ~0.69
for the non-community-property share, less residuals) is not re-measured here (`estimate.py` needs `.engines/`). The
community property share is unmeasured (no IRS count by state).
