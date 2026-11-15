# Lane O3b: Schedule 3 and Schedule 8812 year-change operations (TY2026)

Lane O3b of the TY2026 wave-1 preparation (claude-opus-5-5, judgment class; year 2026, jurisdiction us).
Worktree `.claude/worktrees/ty26-o3b`. Not committed; the coordinator merges the diff.

## What was written

- `changes/2026/s3.yaml`: 2 entries, 8 operations.
  - **C-SCHED-12.** `s3.line5a`'s label and citation now say Form 5695 line 3. `s3.line5b` becomes a zero line labeled
    "Reserved for future use" (its expression is a copy of `s3.zero`). `s3.line8`'s label and sum drop line 5b.
  - **C-SCHED-39.** In `s3.line14`'s refusals, the Form 1062 election (`s3.farmland_deferral_if_sold`) now cites
    Schedule 3 line 13e on the 2026 Schedule 3 draft. Line 13e is not encoded as a line of its own.
- `changes/2026/s8812.yaml`: 7 entries, 24 operations.
  - **C-SCHED-16.** `s8812.line1` reads `f1040.line11b`, with the new label.
  - **C-SCHED-17.** `s8812.line22` gets a new label, citation and refusal text (Schedule 2 lines 16c and 17c, still
    refused through `s2.other`). `s8812.clwb_8` gets a new label.
  - **C-SCHED-18.** `s8812.amt_ws7`'s label and citation now say "one-half of Form 8959, line 18". It still reads
    `f8959.line13`.
  - **C-SCHED-19.** The i1040s8812 parts of the `s8812.line4` and `s8812.line6` citations are requoted from the 2026
    draft (p. 2).
  - **C-SCHED-20.** The `s8812.clwb_10` to `clwb_15` citations become "p. 7, Credit Limit Worksheet B (continued)".
  - **C-SCHED-23 with C-CRED-05** (one entry, `change: [C-SCHED-23, C-CRED-05]`). `s8812.clw_a2` drops `s3.line5b`
    from its label and sum. `s8812.clwb_complete`'s label says "Form 5695" instead of "Form 5695 Part I".
  - **C-SCHED-26.** A note on `s8812.line27`: the refund limit is applied through Schedule 3-A, which reads this credit
    within Form 1040 line 32a.

Every `from` value was read from `forms/2025` by a script, not typed by hand. All 15 evidence quotes are printed on
their pages. When the four page-7 quotes were moved to page 8, the check failed on them.

## Decisions

1. **`s3.line5b` is kept as a zero "Reserved" line, not removed.** `f5695.rce_ws2` (owned by lane O3a) still reads
   it. Removing it here would leave a dangling reference until O3a rewrites that worksheet. The 2026 form still prints
   5b as reserved. Its old expression read `f5695.part2_any` and `f5695.line32`, which O3a removes (C-CRED-06 to -08),
   so the zero copy also separates the two lanes. O3a or adoption may remove the line once nothing reads it.
2. **Line 13e stays inside the zero `s3.line14`, like 13a to 13d and 13z.** The change map left this choice open.
   An encoded 13e would be always zero and refused, and only a single-item sum could carry it into line 14 (no form
   uses one). So the only change is to point the refusal at line 13e.
3. **No expression changes where only a printed number moves.** Ids survive renumbering, so `s3.line5a` keeps
   reading `f5695.line15` (printed 3 after C-CRED-03), `s8812.amt_ws7` keeps `f8959.line13` (printed 18 after
   C-SCHED-13), and `s8812.clwb_complete` keeps `f5695.claiming_part1` (redefined by O3a).
4. **C-SCHED-26 is one note, not an added line or refusal.** The change map classed it as add_line plus set refuses.
   But the Schedule 3-A operations (C-PRI-05) already take Form 1040 line 32a, which includes line 28 (the ACTC),
   into the federal-public-benefit figure and refuse where the qualified-alien question must be answered.
5. **Page moves are left to `citations.py --relocate`.** These are citations whose words are unchanged, for example
   Credit Limit Worksheet A on p. 4 moving to p. 5.
6. **No reads of new Schedule 2 lines, so no `awaits`.** `s8812.line22` keeps refusing through `s2.other` and does
   not read `s2.line16c` or `s2.line17c`.

## Waiting on unpublished documents

- **2026 Instructions for Form 1040 (i1040gi).** These citations still hold 2025 i1040gi quotes:
  - the i1040gi parts of the `s8812.line4` and `s8812.line6` citations (pp. 17–19, "Step 3" quotes that name 2025);
  - `s3.line9`, `s3.line10`, `s3.line11` and `s3.mfs`;
  - the four i1040gi-cited refusals of `s3.line14` (lines 13b, 13d, 13z);
  - the `s3.farmland`, `s3.farmland_deferral` and `s3.farmland_deferral_if_sold` citations. These quote the 2025
    line 13z sentence on farmland, which the 2026 instructions should move to line 13e.
- **Finals of f1040s3, f1040s8812, i1040s8812, f5695 and f1062.** Every entry is `verified: draft`. Mark each one
  `final` as its documents post (D9).

## Defects recorded

- `BUG-0651` (`bug_pending/ty26-o3b-01.md`): the 2026 operations ask about the Form 1062 farmland
  installment election twice. `f1040.form1062` is added by C-PRI-04 in `changes/2026/f1040.yaml`, and the 2025
  `s3.farmland` / `s3.farmland_deferral` pair asks about the same election. Not fixed: `f1040.yaml` is outside this
  lane, and either fix changes the interview, so the interview construction protocol applies.

## For other lanes

- **O3a (Form 5695).** `s3.line5b` is now zero and is no longer read by `s3.line8` or `s8812.clw_a2`. Only
  `f5695.rce_ws2` still reads it. Keep the ids `f5695.line15` and `f5695.claiming_part1`, or mend `s3.line5a`,
  `s8812.clwb_15` and `s8812.clwb_complete` here if they change.
- **O1 (Schedule 2, Form 8959).** `s8812.line22`'s refusal assumes `s2.other` still covers 2026 Schedule 2 lines 16c
  and 17c. `s8812.amt_ws7` assumes `f8959.line13` keeps its id (printed 18).
- **No files touched outside the scope** other than this report and the pending bug entry.

## Verification

- `python3 tools/year_changes.py --check`: 26 entries and 118 operations all apply. The notes are the baseline's
  (five parameters, the new inputs, and the awaited `s2.line20` of `s3a.yaml`) and add nothing from this lane.
- `tools/check_all.sh` was not run, on the coordinator's instruction: it runs one check-all per batch of merged
  lanes. No tool was changed, so no tool self-test applies. The build does not read `changes/`.

## Extension: BUG-0651 fixed (coordinator request)

**The election is now asked once.** The two Schedule 3 questions ask it: `s3.farmland` is the "Sold farmland" box of
the rare_credits tick-box screen, and `s3.farmland_deferral` sits beneath it. Under the interview construction
protocol (N2, N4, N8, N12), that pair is the cheaper walk. The filer with no sale leaves one box unticked. The flat
`f1040.form1062` had no parent, so, as I read the operations, every filer would have been asked it.

- **`changes/2026/f1040.yaml` (C-PRI-04).**
  - The `add_line` and `add_question` of `f1040.form1062` are removed.
  - `f1040.line24b` is now added after `f1040.line24` and refuses on `s3.farmland_deferral_if_sold`.
  - The 2026 sources put the election on two lines: Form 1040 line 24b (Form 1062 line 15) and Schedule 3 line 13e
    (Form 1062 line 14). The one gate now refuses on both.
- **`changes/2026/s3.yaml` (C-SCHED-39), 4 more operations.**
  - `s3.farmland_deferral` gets the 2026 election wording in its label and source. Its question prompt is unchanged.
  - It and `s3.farmland_deferral_if_sold` now cite i1062 p. 2 (2026 draft) instead of the 2025 i1040gi line 13z
    sentence.
  - i1062 p. 2 is added to the evidence.
- **New split file `changes/2026/scope.credits.yaml` (`form: scope`, C-SCHED-39, 1 operation).**
  - `scope.ready_credits`' refusal on the same gate gets the line 13e wording and citation that `s3.line14`'s has.
  - Under D3 this lane owns the file. It touches only that one refuses list, which holds the Schedule 3 situations
    only.
- **Not edited:** the prose in `changes/2026/README.md` that still lists `f1040.form1062` among the questions written
  (the README is the coordinator's).
- **Check.** `year_changes.py --check` applies 27 entries and 121 operations. `f1040.form1062` has left the
  new-input note.
- **Scratch build** of the applied operations in `/tmp/o3b-scratch`, set up as the design doc describes:
  - setup: the documents f1040s3a, f1062, i1062, n-26-10 and irb26-29 added to the 2025 manifest, the five
    parameters, a stub `amb.2026.gift_floor_base`, `s3a.line4` pointed at `s2.line21`, and `s3a`'s tax_year set to
    2025;
  - first result: the build fails only on the test-data defaults of the remaining new inputs (and the old
    `scveh.miles_business`), with none for `f1040.form1062`;
  - with scratch defaults added: `build OK`.
- **Coverage walk** (`interview-coverage`) on that scratch build: 46 problems, none in row `credits.farmland` (still
  refused at `s3.farmland_deferral_if_sold`) and none naming Form 1062 or `f1040.line24b`. The problems by file:
  - 23 in `vehicles_equipment` and 3 in `home` plus 1 in `credits` come from other entries' new or split inputs
    (`scveh.miles_business_h1`/`_h2`, `sa.mortgage_insurance`). Those rows need 2026 answers at adoption.
  - 17 in `education_energy` (rows `l8b.energy_*`): Form 5695 Part II questions are no longer reached. This follows
    from C-SCHED-12, since `s3.line5b` no longer reads `f5695.line32`. It is right for 2026, where Part II is gone,
    and those rows are for O3a to retire with C-CRED-06 to -08.
  - 1 says the coverage report differs from what the rows produce.
- **Pending entry `bug_pending/ty26-o3b-01.md`.** Its Fix, Fix lines, Siblings checked and Regression predictions are
  filled in. `tools/check_bug_inventory.py` reports nothing for it; its only problems are the base's `landing-*`
  ones.
- **`tools/siblings.py --check` still fails on this entry**, with "no review log changed since HEAD for sibling
  form(s): s3, scope". Every generated sibling is now named. The fix lies wholly in `changes/2026/` and changes no
  2025 form, but the check requires refreshed review logs for the sibling forms, and D10 forbids paid reviews during
  preparation. The coordinator must decide how to treat it: rerun reviews, or exempt fixes made only in operations.
  It is the only problem `--check` reports in this tree.
