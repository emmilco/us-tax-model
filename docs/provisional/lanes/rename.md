# Lane notes: year-free ids, delegated decisions, single-reader gates (the last change before the review round)

Branch `draft/land` (worktree `.claude/worktrees/provisional-land`, from `d6e7c1e6`). Agent: `claude-opus-5-5`, class
judgment, tax year 2025, jurisdiction `us`. No paid call and no model call. Three commits, one per part.
Scripts: `rename_work/` (`rename.py` applies and verifies the map; `cutoffs.py` turned the birth-year literals into
parameters; `single_gate.py` lists the inputs read only by one gate-shaped `choose`).

## Part 1. Year-free ids

### The map

`tools/year_free_names.json` holds the whole map (old id, new id, kind, class, reason), 54 line ids plus the document
`clcw26` (its 84 line ids `clcw26.<x>` become `clcw_next_year.<x>`, and `forms/2025/clcw26.yaml` is now
`forms/2025/clcw_next_year.yaml`). Read it there; the classes:

| Class | Rule | Ids |
|---|---|---|
| this_year | the year is the tax year: `this_year`, or a name for what the line is | 28 |
| prior_year | `prior_year` | 4 |
| next_year | `next_year` | 3 (with the document) |
| offset | a birth-year or recovery-year cut: named for the age or rule tested | 12 |
| fixed_date | a date in the law that does not move: named for the rule | 7 |
| misnomer | named for what the line is | 1 |

Before the rename `check_year_ids.py` read every id of the canonical build; every id it takes for year-bearing is in
the map (`rename_work/` check against the baseline build: no carrier outside the map, no new name already in use).

The five names I am least sure of:

1. `asset.acquired_before_bonus_date` / `scveh.acquired_before_bonus_date` (was `before_2017`): "bonus date" is
   September 28, 2017, the first acquisition date of the special allowance in i4562 line 14; but the same page has a
   second date (January 19, 2025, `asset.after_jan19`), so "the bonus date" can be misread. The alternative was
   `acquired_before_sep28`, named for the date like its neighbour `after_jan19`.
2. `retirement.started_before_simplified_method_date` and its gate `..._if_cost`: long (44 and 52 characters). The
   rule is that the Simplified Method is required for an annuity starting after November 18, 1996.
3. `retirement.born_before_averaging_date` (and `lump_sum_if_born_before_averaging_date`, 47 characters): Form 4972
   is open to a participant born before January 2, 1936; "averaging" names the ten-year tax option, not all of 4972.
4. `asset.mqbase_q4` and `asset.cost179_over_half` (were `mq_q4_2025` and `cost179_2025`): named for what the line
   computes, because neither tests the year (the year test is in `asset.mq_q4` and `asset.cost179`, which read them);
   a reader who expects the `_this_year` pair of the other asset lines will not find it.
5. `person.edu_a_this_year` / `person.edu_a_next_year` (and `dependent.`): the names the brief gave; `edu_a` keeps the
   old cryptic stem ("a" for assistance) rather than `edu_assist_...`.

### Cut-off years are parameters

The form language cannot compute "tax year minus N": `subtract` is typed for money (`engine/src/check.ts`,
`case "subtract"` requires a money type), there is no Count arithmetic, and the tax year itself (`params.tax_year`) is
not a parameter value a line can read. So each cut is its own parameter, named for the age rule, in
`params/2025.yaml`, with the page that states the rule:

| Parameter | 2025 | Meaning | Cited |
|---|---|---|---|
| `age.cut_65` | 1961 | born before January 2 of it: 65 or older at year end | i1040gi p. 33, line 12d |
| `age.turning_65` | 1960 | the 65th birthday falls in the tax year | i1040gi p. 110, Schedule 1-A Part V |
| `age.cut_25` | 2001 | the earned income credit's 25 | i1040gi p. 41 |
| `age.cut_24` | 2002 | under 24 (education credits, Form 8615) | i8863 p. 7 |
| `age.cut_19` | 2007 | over 18 | i8863 p. 7 |
| `age.cut_18` | 2008 | the saver's credit's 18 | f8880 p. 2 |
| `age.cut_16` | 2010 | under 16 (Self-Select PIN) | i1040gi p. 66 |
| `age.cut_50` | 1976 | IRA and catch-up 50 | i1040gi p. 97 |
| `age.cut_55` | 1971 | HSA 55 | i8889 p. 4 |
| `age.cut_60` | 1966 | SIMPLE band 60 to 63, lower end | p560 p. 16 |
| `age.cut_64` | 1962 | SIMPLE band 60 to 63, upper end | p560 p. 16 |
| `age.cut_73` | 1953 | 73 or older (required distributions) | i5329 p. 8 |

`age.cut_N` is one rule throughout: the year of birth in which only a January 1 birthday makes a person N or older at
the end of the tax year. Where a line compared with the year before a cut (`le 1975`, `gt 1965`, `ge 2011`, `le 1952`)
the comparison is restated against the cut (`lt age.cut_50`, `ge age.cut_60`, `gt age.cut_16`, `lt age.cut_73`); the
values are the same for every whole year.

`person.simple_age` could not keep its shape. Its seven-piece interval tiling had one-year pieces written as
`(1961, 1962]`; with only cut parameters such a piece is `[age.cut_64, age.cut_64]`, which the build's guard analyser
refuses as empty (it reads the bounds as real numbers), and writing it as `(age.cut_65, age.cut_64]` would need a
parameter for every year before a cut. It is now a four-piece tiling (`[0, cut_64)` 50 to 59 or 64 and over;
`[cut_64, cut_60)`; `[cut_60, cut_50)`; `[cut_50, ...)`) whose last three pieces are three new helper lines, each a
Bool choice on the open-year line the old tiling's one-year piece stood for: `person.simple_age_60_63_years`
(`person.simple_open_year`: the stated band, else 60 to 63), `person.simple_age_50_59_years` (`simple_open_year`: the
stated band, else 50) and `person.simple_age_under50_years` (`person.age50_open_year`: from the age-50 answer, else under
50). The value for every year of birth is the old one (the same alternative is taken for each year; checked by the
fixtures, among them the eight `stage14.simple.*` cases, and the coverage rows `business.simple_age_*`). New York: `ny_it201.pension_59_people` compared with
1965; it now reads `ny.pension.latest_birth_year` (1965) in `params/ny/2025.yaml`, cited to ny_it201i p. 9.

The placed-in-service tests did not get a parameter: `asset.placed_this_year` and `scveh.placed_this_year` (were
`placed == y2025`) now test the year of recovery `asset.year` / `scveh.year` = 1, and
`scveh.first_year_after_recovery` (was `placed == y2019`) tests `scveh.year` = 7. The year of recovery is the
per-year table `recovery_year`, which already moves with the tax year; the table maps y2005..y2025 one to one onto
21..1, so the tests are true for the same enum values. `engine/src/mutate.ts` (the 2019-vehicle argument) checks the
new expression and that y2019 alone has recovery year 7.

Fixed dates in the law (September 28, 2017; November 19, 1996; January 2, 1936) were never literals in a line: they
are the wording of Bool inputs, and only the ids carried them.

### Where the map was applied, and how only ids changed

`rename_work/rename.py apply` replaces every whole old id, and every path form `<doc>[key].<local>` of a mapped line
id (`person[taxpayer].edu_a2025`, `person[taxpayer].sc[desk].asset[pc].before_2017`), by its new name; `local` also
replaces bare local names, for code that builds paths from them. Files:

| Class | Files | How applied |
|---|---|---|
| Forms | 15 federal form files, the renamed `clcw_next_year.yaml`; `forms/ny/2025/ny_it201.yaml` (the parameter only) | `apply`; then the cut-off and placed-in-service edits above |
| Parameters | `params/2025.yaml` (12 new `age.*`), `params/ny/2025.yaml` (1 new) | by hand |
| Interview | `questions.yaml`, `full.yaml`, `sales.yaml`, `stage4.yaml`, `social-security.yaml`, `gate_frequencies.yaml`, 11 coverage files, 3 personas | `apply`; two coverage row ids that carried a year renamed by hand (`marketplace.married_this_year`, `saving.turned_65_this_year`) |
| Fixtures | 22 federal files, 4 New York files | `apply`, leaving every line whose key is `id`, `description` or `evidence_note` (case labels and the record of past class M reviews) |
| Engine | `generate.ts` (also the suffix lists `_a_this_year`, `_a_next_year`, `_over18`, `_age24`, which build ids by concatenation), `serve-check.ts`, `mutate.ts` (by hand) | `local` |
| Tools | `engines/generate_cases.py` (and its suffix list), `coverage/tree.json`, `human_review/reading_list.json`, `year_ids.json` (emptied), `check_year_ids.py` (the summary of an empty list) | `local` / `apply` / by hand |
| Reviews | `reviews/2025/twins.json` only (two keys, four `pair` names) | `local` |
| Register | `ambiguities/2025.yaml` (five mentions in `chosen` text and one option; no entry id changes) | `apply` |
| Prose | `PROJECT_INDEX.md` (the form file name) | `apply` |

Not touched, on purpose: review logs, indexes, rulings and baselines under `reviews/` other than `twins.json`;
`.transcription/`; dated documents, lane notes, handoffs, `BUG_INVENTORY.md`, `TASKS*.md`, `research/`,
`docs/provisional/MAP.md` (the plan as written), `sources/2025/PREMISES.md`; `tools/year_diff.py` and the examples in
`tools/README.md` and `check_year_ids.py`, which are about the year-literal rules and must keep their years; the
fixture file name `fixtures/2025/clcw26.json` and fixture case ids such as `bug0477.clcw26.final_return_long`
(labels, and keys of review records). `docs/COVERAGE.md` is generated by `tools/coverage/tree.py`, a check-all step
outside `draft_check.sh`; it was not regenerated (see "Found, not fixed").

**Fixture verification.** `rename.py compare OLD NEW` loads a fixture file from before the rename, applies the map to
every key and string value except the `id`, `description` and `evidence_note` fields, and reports every remaining
difference from the file after it. Run over every fixture file (federal and New York, 59 files, 26 of them changed): 0 differences in each. No
expected value and no expected refusal changed except by the renaming of a key. A scan of the renamed `interview/` and
`fixtures/` trees for any old id or local name outside those three fields found only the two coverage row ids above.

### Pins and review subjects the rename changes

Mutation pins (`engine/src/mutate.ts`, `pinned(...)`, a digest of the premise lines' expressions, types and readers):
of 70 pins, 29 held on the build before this change (the rest were already stale from the redraft). Computed with
`premiseDigest` on the build before and after (the premise ids mapped): three that held no longer hold, because a
premise line's expression or readers name a renamed id: `operand.sd.sd.to1040.line21.then0` (the `clcw_next_year`
lines), `operand.dependent.dependent.edu_adj.zero.then1` and `operand.dependent.dependent.edu_over_refused.edu_no.then1`
(`edu_a_this_year`, `edu_a_next_year`). Mutation testing is not run here; the pins need re-pinning when it is. The
vehicle argument `vehicle2019` was rewritten to the new `scveh.first_year_after_recovery` expression (above).

Review subjects: every review keyed by an old id (transcription, render, class M, screen, false-no) is stale by
construction; the carry tool takes each verdict across by `tools/year_free_names.json`. Lines whose content changed
beyond the id, which a carried verdict does not cover: the 17 person lines and one Form 8889 line whose literals
became parameters, `person.simple_age` and its three new helpers, `asset.placed_this_year`,
`scveh.placed_this_year`, `scveh.first_year_after_recovery`, `ny_it201.pension_59_people`, and the 13 new parameters.
The generated returns of `generate.ts` move (sorted input ids changed), as any rename moves them.

### Checks (Part 1)

RAN on the tree of the Part 1 commit (tree `76a446f6375c` before the notes and the summary fix): `tools/draft_check.sh
--quick` green (build; fixtures 1854/1854; interview-rules 0 problems over 177 walks, baseline untouched; coverage
rows 0 problems, 484 rows; tick-groups passed); `node engine/dist/main.js test-fixtures --ny` 338/338;
`python3 tools/check_year_ids.py`: 5095 ids read, no id carries a year, 0 listed; its self-test OK.

## Part 2. Decisions delegated by the owner

Written in `docs/provisional/DECISIONS.md` (what, by whom, the lane note, how to reverse). Two change the model:

**1. Four scope questions.** `scope.reservist_expenses`, `scope.military_move`, `scope.performer_expenses` ask the wish
("Do you want to deduct ...?"), and their help ends "To go on without the deduction, answer No." (MAP 4.3).
`scope.recovery` is not a deduction: a taxable recovery left out makes the return wrong, so MAP 4.3 does not allow the
wish. It is put back to the old screen's scope ("a recovery ... requiring Schedule 1": one that has to be reported),
in plain words: "... paid back an amount whose deduction on an earlier year's return lowered your tax ...", with help
that says a recovery of a deduction that did not lower the tax is answered No; tick label "Paid back a deduction that
lowered your tax (not a state refund)" (the build allows twelve words). The coordinator's brief named all four for the
wish; this is the one place I departed from it, for the reason above. Model unchanged otherwise (same inputs, gates
and refusals). Coverage rows (`coverage/scope.yaml`): the four refusing rows are unchanged and pass; four new rows,
each the filer the fact question refused and the old screen did not, complete: `scope.reservist_expenses_not_deducted`,
`scope.military_move_not_deducted`, `scope.performing_artist_not_deducted`, `scope.recovery_no_tax_benefit`.

**2. A birth year is range-checked.** New line `person.birth_year_bad` in the person form (birth year above
`age.birth_year_latest`, 2025, or below `age.birth_year_earliest`, 1900: two new parameters, cited to the age
question's page with the bound marked as a consistency bound). The refusal sits on the household roster line
(`household.birth_year_bad`, a count over the people of `person.birth_year_bad`), as the first refusal entry of that
line, ahead of `household.filer_under16`: put on a person line first, a year after 2025 was told as "a filer under
age 16" (a person born in 2026 is under 16), because that refusal came first. The explanation is in
`interview/2025/conflict_checks.yaml` under `household.birth_year_bad`, so the page shows it as conflicting answers
naming the question. Coverage rows (`coverage/opening.yaml`): `opening.birth_year_after_tax_year` (2026) and
`opening.birth_year_too_early` (1899), refused at `household.birth_year_bad`; `opening.birth_year_earliest_accepted`
(1900) completes; `opening.birth_year_latest_accepted` (2025) is not refused for the year and ends at
`household.filer_under16`, where any filer born in 2025 ends.

Review debt: `scope.yaml` and the bank entries of the four questions (render, screen, false-no for the three gated
ones); `person.birth_year_bad`, `household.birth_year_bad_count`, `household.birth_year_bad` and its refusal, the
two parameters.

### Checks (Part 2)

RAN on the tree of the Part 2 commit (tree `adc601240a5a`, before these notes): `tools/draft_check.sh --quick` green
(build; fixtures 1854/1854; interview-rules 0 problems over 177 walks, baseline untouched; coverage rows 0 problems;
tick-groups passed); `test-fixtures --ny` 338/338; `check_year_ids.py` 5100 ids, none carries a year.

## Part 3. Inputs with a single gating reader marked `gated_by` (T-281)

`rename_work/single_gate.py` lists, from the canonical build, every input read by exactly one line, where that line is
a `choose` of the same document taking the input as an alternative's `then`, whose guards do not read it, and is not
marked. On the tree after Part 2: 56 inputs. 44 have a gate of the conventions' shape (every other alternative a
parameter line of zero or false); 12 do not.

**Marked (30).** `carloan.col_ii_input`; `dependent.ptc_magi`, `edu_over`, `edu_ein`; `f4952.prior_7`;
`f5695.battery_cost`, `line17c`, `line17e`, `line21b`, `b_new_home`, `condo`; `f8863.ban`; `f8962.estimate_100`,
`alien_below` (two of the four the T-281 row names); `ira.deduct_less`; `ny_it201.ask.state_resident`,
`pension_exclusion`, `real_property_credit`, `abode_part_year`, `est_late`, `gov_pension_other`; `person.ira_trad`,
`ira_basis`, `ira_dist`, `edu_over`, `edu_ein`; `s1.gambling_pro`; `sa.spouse_extra`, `sa.spouse_itemizes`;
`scope.care_benefits_other`. Each is marked with its
existing gate line; no line, gate or wording changed. `scope.care_benefits_other`, which lane 9 could not mark
(`l9.md`, "Found and not fixed" item 2: the minimal return opened `f2441.benefits` alone and met
`f2441.nondependent`), passes now: lane 2b's redesign of Form 2441 gave `f2441.nondependent` its own gate.

**Not marked: the gate is asked of the all-closed return (9).** interview-rules' minimal returns answer every question
with its closed answer and fail when the walk asks an input whose gate counts as closed, a gate counting as open only
when the existence gate (an input its guard reads) is the one opened. These nine are asked exactly on that return,
because their gate opens on the closed answer of what it reads or on a fact every return has:

| Input | Gate | Why it is asked on the all-closed return |
|---|---|---|
| `sa.home_other`, `sa.gift_carryover`, `sa.medical_premiums` | `..._if_not_owner`, `..._if_no_gifts`, `..._if_not_large` | asked after a No (lane 7a, `l7a.md`, "For the owner") |
| `s3.disability_retired` | `s3.disability_if_under65` | asked of everyone under 65; the background person (born 1980) is |
| `person.inherited_account` | `person.inherited_account_if_under_73` | asked of everyone under 73 |
| `ny_it201.ask.item_c`, `ny_it201.ask.other_withholding`, `ny_it201.ask.late_penalty` | `..._if_not_federal`, `gate.other_withholding`, `gate.late` | open on the New York background return |
| `ny_it201.ask.use_tax_exact` | `..._if_small` | asked when `ny_it201.ask.owes_use_tax` is opened alone, which the check does not count as its opener |

Found by marking all 44, building, and running interview-rules (it stops at the first: `s3.disability_retired`), then
`rename_work/minimal_asks.mjs`, which walks the same minimal returns giving the closed answer where the check stops and
lists every marked input asked while its gate counts as closed; those nine were unmarked and the check rerun (below).

What would let them be marked. The check's idea of a closed gate fits an existence gate (kind B: "does this exist?",
whose closed answer is No); these are applicability gates of kind A or C, opened by a No or by an age, whose closed
answer opens them. The change I would make is to the check, not the guards: in the minimal returns, count a gated
input as closed only when its gate line, evaluated on the answers so far, takes its else alternative; an input whose
gate takes it on the closed answers is then answered with its closed answer like any other question. That keeps the
check's purpose (no question beneath a closed gate is asked) and admits gates opened by a No. Reshaping the guards
instead (asking `sa.home_owner` as "Do you rent, or own nothing?" so the child opens on a Yes) would change wording
and the cost of the typical answer; for the age gates no guard shape helps. Not done: the brief says not to weaken the
check, and this is a change to it for the owner or the coordinator to decide.

**Not marked: the mark makes a new existence gate the minimal returns cannot open alone (4).** Marking an input makes
every input its gate's guards read an existence gate, which interview-rules then opens alone on the minimal return.

| Input | Gate reads | What the check then reported |
|---|---|---|
| `f8962.married_this_year` (named in the T-281 row) | `f1040.status` | `f1040.status = "mfj"`, `"mfs"`, `"hoh"` alone: each ends refused (full and New York; a joint status with no spouse, a separate or head of household return with none of its facts) |
| `f5695.separate_homes` | `f1040.status` | the same |
| `ny_it201.ask.spouse_itemizes` | `f1040.status` | the same |
| `ny_it201.ask.college_tuition` | `f8863.paid` | `f8863.paid = true` alone: `person[taxpayer].tin` is reachable before `person[taxpayer].edu`, the answer that hides it, and the bank-order walk never asks it (an order leak of Form 8863's own lines) |

The filing status is not an existence gate (an enum every return answers; its other values each need answers of their
own), so opening it alone refuses by construction. What would let these three be marked: the check should not treat
an enum input every return answers as an existence gate (count only Bool inputs, or inputs whose closed answer hides
something), or the gates should read a derived Bool (`..._status_mfj`) whose opening the check can follow. For
`college_tuition`, the leak in Form 8863 (`person.tin` before `person.edu`) is to be fixed first; it is the same kind as
T-290's order-dependent leaks. Neither change is made here.

**Not marked: its twin is not marked (1).** `dependent.edu_1098t` (gate `dependent.edu_student_tin`) conforms and
passed interview-rules, but `tools/check_twins.py` (in the whole `draft_check.sh`) requires the twin pair
`person.edu_1098t` / `dependent.edu_1098t` to agree in `gated_by` unless the difference is declared, and
`person.edu_1098t` cannot be marked (two lines read it). Unmarked rather than declared: a declared difference would
need a reason from the sources, and there is none; the person side's two readers would have to become one gate line
first.

**Not marked: not a gate of the conventions (12).** Their single reader is a `choose` between the input and a computed
value, not zero or false: `dependent.supported` (the fourth the T-281 row names; `dependent.supported_by_view` takes
`dependent.no`, the computed `dependent.supported_view_over` or the input), `dependent.self_support`,
`dependent.citizen`, `dependent.canada_mexico`, `dependent.work_ssn`, `dependent.placed`, `dependent.eic_ssn`,
`dependent.qr_all_year`, `household.ever_married` (`household.marriage_possible` takes it or what the filing status
states), `f1095a.c_total`, `f8889.allocated`, `retirement.last_line4`. The convention allows a gate's other
alternatives to be only a parameter of the input's type, so these cannot be marked as they stand. Each could be, by
splitting its reader in two: a gate line `<input>_if_<condition>` taking the input or false/zero, read by the existing
line in place of the input (for `dependent.supported`: `dependent.supported_if_close`, taking the input when the view
is "close or not sure" and `dependent.no` otherwise). That adds a line per input and changes the readers' expressions;
it is a model change, not a mark, and I did not make it.

Review debt: each marked input comes under the screen and false-no reviews (a review each of its gate condition).

### Checks (Part 3)

RAN: with all 44 marked, the build passed and interview-rules failed at the minimal returns (`s3.disability_retired`
asked with its gate closed); `minimal_asks.mjs` then named the nine above; with those nine unmarked, interview-rules
failed on `f1040.status` opened alone (six) and the Form 8863 leak (one); with the four above unmarked, on the tree of
the Part 3 commit (tree `8cd09a15da7d`, before these notes): `tools/draft_check.sh --quick` green (build; fixtures
1854/1854; interview-rules 0 problems over 177 walks, baseline untouched; coverage rows 0 problems; tick-groups
passed); `test-fixtures --ny` 338/338; `check_year_ids.py` 5100 ids, none carries a year.

## Found, not fixed

1. `tools/coverage/tree.py --check` (check-all, not in `draft_check.sh`) reports five refusal gates of the redraft that
   `tools/coverage/tree.json` does not place: `dependent.divorced_rule_if_parents_apart`,
   `dependent.married_if_ever_married_eic`, `..._qc`, `..._qr`, `sa.gift_carryover_if_no_gifts`. The gate added here,
   `household.birth_year_bad`, is placed. `docs/COVERAGE.md`, which the same tool keeps current, was not regenerated.
2. Labels of the lines whose year literals became parameters still name the 2025 years in words ("Born before January
   2, 1961", "Born in 1962 or 1966 ..."); the year-literals-in-text half of charter 7 item 4 is not part of this work.
   The labels of the renamed and new lines were left as they were, so that a render verdict carried by the map still
   reads the same words, except the four new or rewritten SIMPLE lines.
3. 41 of the 70 mutation pins already did not hold on the tree before this work (the redraft's changes); with the three
   above, 44 need re-pinning before mutation testing is run.
4. The fixture file `fixtures/2025/clcw26.json` and case ids carrying a year are labels and were left.

## Final checks and walks

RAN on the final tree (tree `2e42d77bd0b8`, the last commit but for these notes, the regenerated pages, reports and
walks): `tools/draft_check.sh` (whole) green: build; fixtures 1854/1854; interview-rules 0 problems over 177 walks
(baseline untouched); coverage rows 0 problems; tick-groups; person wording current; spouse-wording, check, draft-walk,
order and tick-groups self-tests; integration 1021 invocations; properties; test-serve 505 checks; twins 0 problems;
render check current (after `node engine/dist/main.js render`, which rewrote `rendered/2025/` and replaced
`clcw26.md` by `clcw_next_year.md`). `node engine/dist/main.js properties --ny`: 2 properties over 400 generated
returns, 0 failing. `test-fixtures --ny` 338/338. `check_year_ids.py`: 5100 ids, none carries a year, 0 listed.
`draft-walk --out docs/provisional/walks/after`: 19 personas, 0 problems, each at the `end` its persona file states
(fourteen complete; `11_refused_rental` at `scope.schedule1`, `12_refused_nonresident` at `scope.other_income`,
`ny02` at `ny_it201.gate.child_credit`, `ny03` at `ny_it201.gate.line26`, `ny04` at `ny_it201.gate.part_year_state`).
The first whole run failed only at twins (`dependent.edu_1098t` marked, its twin not): unmarked, above.
