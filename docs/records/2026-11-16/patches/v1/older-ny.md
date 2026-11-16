# Patch older-ny: BUG-0850 and BUG-0851 (New York), plus closure records for BUG-0629 and BUG-0092

Lane patch-older, claude-opus-5-5, judgment, 2026-11-16. Year 2025, jurisdiction ny (closures: us).
Base: the xint worktree as frozen (copies in `/tmp/nightplan/scratch/older-ny/a/`). Patch:
`/tmp/nightplan/patches/older-ny.patch` (3 files; `git apply --check` passes on the base copies, and it applies
in sequence with older-credits, older-scha and older-scha-0817a). Nothing in the repository was written.
Labels: **[V]** checked against the file named; **[I]** inferred, not run. No engine run was made (none
allowed tonight): every expected value is hand-predicted.

## Summary

- **BUG-0850 (structural, medium).** A new helper `ny_it201.dis_pension_wages` (sum of `person.dis_wages`) and a
  new gate `ny_it201.gov_pension_candidate` (lines 9/10 pension income **or** a disability pension in wages). The
  government pension question and its No-branch (`gov_pension_if_income`, `gov_said_no`) read the new gate. The
  line 29 chain stays on `has_pension_income` (lines 9 and 10 only), as the plan says. The stale note is
  rewritten. Two NY fixtures added.
- **BUG-0851 (wording, medium).** `ask.ny_529` is asked "At any time in 2025" (form source and label);
  its help counts a closed or moved account; `ask.529_nonqualified` names student loans, the July 4 start and
  the eligible-school condition, and moves pre-college tuition to help. The Advisor-Guided Plan is **not**
  named (plan owner decision 7: no archived source names it).
- **Closure records** for BUG-0629 and BUG-0092 drafted below (text only; not in the patch).

## Hunks

### forms/ny/2025/ny_it201.yaml
1. `ny_it201.has_pension_income` note: rewritten. It now says that a disability pension paid wholly before the
   minimum retirement age is wages on federal line 1h (`person.dis_wages`) and is read by
   `gov_pension_candidate`, and that the split case is refused federally (`retirement.dis_split` through
   `retirement.special`) [V: forms/2025/retirement.yaml:663, :1232, :1277; refusals at :1649, :2304].
   The expression is unchanged.
2. New `ny_it201.dis_pension_wages` (helper, NonNegDollars): `sum_over person, field person.dis_wages`
   [V: person.dis_wages at forms/2025/person.yaml:1941; NY already sums over `person` at ny_it201.yaml:686, :887].
3. New `ny_it201.gov_pension_candidate` (gate, Bool): `has_pension_income = true` or `dis_pension_wages > 0`.
4. `ny_it201.gov_pension_if_income` and `ny_it201.gov_said_no`: read `gov_pension_candidate` in place of
   `has_pension_income`; labels widened. Ids kept, so `gate.line26`, `gov_pension_other_if_no` and
   `gov_pension_any` are untouched.
5. `ny_it201.ask.ny_529`: label and source become "At any time in 2025, did you (or, on a joint return, your
   spouse) own an account in New York's 529 college savings program?" (24 words). Source: IT-201-I p. 10, Line 30,
   "During 2025, did you, as an account owner, make contributions to or a withdrawal..."; p. 8, Line 22,
   "the transfer to another state's program" [V: per the plan, sources/ny/2025/ny_it201i.txt:472-505].

Not changed, on purpose: `ny_it201.gate.line29` and `pension_exclusion_after_gov` stay on lines 9 and 10.
Whether a pre-retirement disability pension is "pension and annuity income" for the line 29 exclusion is a
separate source question. **Note it on the BUG-0850 closure** as open, not decided here.

### interview/ny/2025/questions.yaml
6. `ask.ny_529` help: "Count an account you closed, or moved to another state's plan, during 2025. A 529 plan of
   another state, or an account someone else owns for you, counts as No." (30 words; the sentence naming "the New
   York 529 College Savings Program" is dropped).
7. `ask.529_nonqualified` prompt: "In 2025, did you take money out of that New York 529 account for anything but
   college, student loans, or career training at a college or other eligible school from July 4 on? A move to
   another state's plan counts." (40 words, child; the current one has 33). Help: "School tuition before college
   counts as Yes. A rollover to a Roth IRA or an ABLE account, or money taken out because the student died or
   became disabled, is No, as is a move between family members' New York accounts." (40 words). The form label
   (`ny_it201.yaml:175-182`) already lists the July 4 and eligible-institution rules [V], so the form source is
   unchanged.
8. `ask.gov_pension` is **not** changed. Its prompt ("pension or retirement money from the federal government,
   the military, or a New York State or local government job") reads correctly for a disability pension
   [judgment, I]. The entry's optional naming of a U.S. territory and the District of Columbia is left out: the
   prompt is already over the N10 parent aim.

### fixtures/ny/2025/it201.json (two cases after `ny.gate.pension_line28_zero`)
The file is canonical `json.dumps(indent=2, ensure_ascii=False)` [V: round-trip equal], so the cases were
inserted by load and dump; no other byte changed. Inputs are the entry's witness
(`/tmp/xrel/ny/dis_cases.json`: a full-year City resident with two W-2s of $38,000 and $40,000 and a
`disability_3` Form 1099-R of $18,000 wholly before the minimum retirement age), plus:

| Case | Added answers | Expected | Derivation |
|---|---|---|---|
| `ny.gate.pension_disability_wages` | `ask.gov_pension: true` | `line26`: refusal at `ny_it201.gate.line26` (the same refusal object as `ny.gate.pension_line28_zero`) | Witness evaluation [V: /tmp/xrel/ny/dis_out.json]: `f1040.line1h` $18,000, lines 9 and 10 $0. So `dis_pension_wages` = $18,000, the candidate gate is true, the question is asked, and Yes gives `gov_pension_any` true, so line 26 refuses [I: hand trace of the patched expressions] |
| `ny.gate.pension_disability_wages_not_gov` | `ask.gov_pension: false`, `ask.gov_pension_other: false` | `line26` $0; `line29` $0; `line33` $96,000 | Line 26 is `ny.zero` with no refusal. Line 29: `gate.line29` reads `has_pension_income`, false (lines 9/10 $0), so $0. Line 33: the witness value is $96,000 on the unpatched tree [V: dis_out.json], and the patch changes no addition or subtraction on this path [I] |

## Siblings checked
- The other readers of `has_pension_income`: `gate.line29` (`ny_it201.yaml:917`), deliberately unchanged
  [V: grep]. Nothing else reads `gov_pension_if_income`/`gov_said_no` outside the chain [V: grep].
- The federal side: `f1040.line1h` = `person.line1h` = strike pay + `person.dis_wages` [V: person.yaml:1959-1967].
  Strike pay is not a pension, so the helper sums `dis_wages`, not line 1h.
- The 529 gates: `gate.line22` and `gate.line30` both hang on `ny_529_if_account` [V: :705-711, per the plan :930].
  The past-tense ownership is right for both. Line 30 asks about contributions or withdrawals "during 2025".
- The New York coverage rows (`interview/2025/coverage/ny.yaml`): no row has a disability pension [I: no grep hit
  for `dis_` in the NY rows]. The report quotes wording, so it needs `--write`.

## What to run
1. `node engine/dist/main.js test-fixtures --ny`. Both new cases should pass, and no existing case should change.
   Watch `ny.gate.pension_line28_zero` and every case with a pension.
2. `node engine/dist/main.js interview-coverage --write`, then check that it passes (the 529 wording is quoted).
3. `node engine/dist/main.js draft-walk` for a New York persona with a 529 account and one with a pension.
   Check that the government pension question now follows a disability Form 1099-R.
4. The mutation run for `ny_it201` (new operands on `gov_pension_candidate`; an equivalent mutant may need an argument).
5. `node engine/dist/main.js tick-groups` (no group changes; a sanity check).

## Reviews made due (one per form per round, line-scoped)
- Transcription, line-scoped: `ny_it201.has_pension_income` (note), `dis_pension_wages`, `gov_pension_candidate`,
  `gov_pension_if_income`, `gov_said_no`, `ask.ny_529`.
- Screen and false-no samples: gates `gov_pension_if_income` and `gov_said_no` (their subject changed);
  `ny_529_if_account` and `has_edu_account` (the entry asks for both).
- Question reviews of `ask.ny_529` and `ask.529_nonqualified`.

## Closure entries to record when this lands (pending entries, `tools/new_bug.py ... --pending PREFIX`)
Add these after the check is green, with that run's evidence. They are sketches:
- `Closure: BUG-0850 is fixed: the New York pension gate also reads disability pensions in wages`, with
  `Closes=BUG-0850`, `Closure=fixed`, and `Evidence=` naming the two fixture ids and the line-29 question left open.
- `Closure: BUG-0851 is fixed: the New York 529 ownership question asks about any time in 2025`, with
  `Closes=BUG-0851`, `Closure=fixed`, and `Evidence=` naming the source, the help, the 529_nonqualified prompt, and
  that the Advisor-Guided Plan is not named (no archived source).

---

## Closure record drafts (bug-inventory conventions, tools/README.md "Bug status" [V: tools/README.md:780-791])

Each is recorded with `python3 tools/new_bug.py "<title>" --pending <PREFIX> --field ...`. That writes
`bug_pending/<PREFIX>-<NN>.md`, and the merge numbers it. The field shape copies BUG-0670 to BUG-0672
[V: BUG_INVENTORY.md:8416-8441].

### BUG-0629

```
python3 tools/new_bug.py "Closure: BUG-0629 is fixed: the year rollover defects found by the New York rehearsal (T-295)" \
  --pending <PREFIX> \
  --field "Caught by=lane patch-older (claude-opus-5-5, judgment), 2026-11-16, verifying the open high entries against the coverage-expansion tree (plan-med-older)." \
  --field "Closes=BUG-0629" \
  --field "Closure=fixed" \
  --field "Evidence=T-295 is done 2026-11-14 (TASKS-DONE.md row T-295) and each of the eight parts has its change in the tree: (1) years.json lists ny_adopted [2025]; tools/jurisdiction.py reads it; engine/src/build.ts dropNyConflicts drops New York gates from the conflict checks when forms/ny is absent (line 63, called at line 407), so interview/2025/conflict_checks.yaml may keep ny_it201.gate.line79_over (line 95). (2) tools/year_diff.py extend_year_enums and extend_recovery_year (lines 615, 642). (3) tools/transcription/year_carry.py write_sidecar (line 611). (4) --adopt carries the operand, consumer, limit, instruction_cites and sign baselines and the contract banks (TASKS-DONE T-295). (5) tools/build_fresh.py takes --year. (6) tools/ny_fixtures.py refuses a tracked or existing file and writes --out. (7) tools/fetch_sources.py requires an edition_marker on a New York year-free address. (8) tools/check_year_ids.py refuses a year with no build. The self-tests of year_changes.py and year_diff.py passed 2026-11-15 (TASKS-DONE); they were not rerun here. No adoption has been run end to end: that is T-317 (open), the rehearsal that proves parts (1) and (2) together." \
  --field "Tags=closure; record-drift"
```

Checked here [V]: `years.json:3`, `tools/jurisdiction.py:27,90-96`, `engine/src/build.ts:63,407`,
`tools/year_diff.py:615,642`, `tools/transcription/year_carry.py:611`, `tools/fetch_sources.py:155-158`,
`tools/check_year_ids.py:95`, `tools/ny_fixtures.py:15-19,291`, `interview/2025/conflict_checks.yaml:95`. Part (4)
and `build_fresh.py --year` are relayed from the TASKS-DONE row [T]. Only a usage line was seen for the latter
(`tools/build_fresh.py:9`).
Alternative, if the owner wants the end-to-end proof first: record `Closure=fixed` with "BUG-0629 in part" in
`Closes` (this leaves it open, per tools/README.md:786), and close it fully when T-317 passes.

### BUG-0092

```
python3 tools/new_bug.py "Closure: BUG-0092 is fixed: Form 8889 reads the marital answer household.married" \
  --pending <PREFIX> \
  --field "Caught by=lane patch-older (claude-opus-5-5, judgment), 2026-11-16, verifying stale open entries against the coverage-expansion tree (plan-med-older)." \
  --field "Closes=BUG-0092" \
  --field "Closure=fixed" \
  --field "Evidence=Fixed in a65e6afb (integrity plan Phase 1, second batch, 2026-10-22: 'eic.married becomes household.married; Form 8889's married tests read it (i8889 p. 4 rule 6)'). In the tree, f8889.married_family (forms/2025/f8889.yaml lines 1024-1041) chooses on household.married, and the age-55 unmarried test reads household.married = false (line 1120), as do the other marital tests of the form (lines 658, 664, 756, 762). No line of the form tests f1040.status for marriage. household.married (forms/2025/household.yaml line 647) is household.married_dec31 when marriage is possible, so a married head of household is married here. The entry's missing fixture exists: audit.f8889.married_hoh_family_age55 (fixtures/2025/f8889.json). Its expected values were not re-evaluated here. The entry stayed open only because its Fix field reads 'open; integrity plan item 2.4' and no closure was recorded. It matters more now that married filing separately is being widened." \
  --field "Tags=closure; record-drift"
```

Checked here [V]: `git show a65e6afb` message; `forms/2025/f8889.yaml:658,664,756,762,1034,1040,1120`;
`forms/2025/household.yaml:647-664`; `fixtures/2025/f8889.json` holds `audit.f8889.married_hoh_family_age55`
(a head-of-household case with `household.married_dec31: true`); `tools/bug_status.py BUG-0092` reports "open
[Fix: open; integrity plan item 2.4 ...]". Inferred [I]: that the fixture passes on the xint tree. It was not
run, since engine runs are not allowed tonight.
