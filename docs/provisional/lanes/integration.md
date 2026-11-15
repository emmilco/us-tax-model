# Integration notes: the lanes merged onto `provisional/interview-graph`

Integrator: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call, no model call from
code, nothing pushed, nothing outside `.claude/worktrees/provisional` written.

**This file has two parts.** Part 1 (to the heading "Part 2") is the first integrator's record of the first eleven
lanes, as it stood at `1a4e3023`. Part 2 is the second integrator's: the last five branches, the checks on the whole,
and the current list of what the stitch needs. **A successor reads Part 2's "State after the five merges", "What is
red now" and "What the stitch will need (current list)".**

# Part 1: the first eleven lanes (first integrator)

## State

| Merged | Merge commit | Build | Fixtures on that commit |
|---|---|---|---|
| walk tool, order mechanism, l3, l6a, l2b, l2a, l4a, l7b | up to `016efdd2` (before this integrator) | reported green by the coordinator (not rerun by me) | 1,854 of 1,854, reported (not rerun by me) |
| l1 | `b4c7718e` (before this integrator) | not run by me on that commit | not run on that commit |
| l5a | `370bb945` | OK | 1,854 of 1,854 |
| l4b | `d1e492c6` | OK | 1,854 of 1,854 |
| l8a | `18859943` | OK | 1,854 of 1,854 |
| l5b | `e7bfc20a`, then `46a2bfe7` (its baseline entry taken out, two answers restated) | OK | 1,854 of 1,854 |
| rows, personas, one placement | `a68c060a` | OK | 1,854 of 1,854 (in `tools/draft_check.sh --quick`, green) |

Not merged at `1a4e3023`, by instruction: `lane/l6b`, `lane/l7a`, `lane/l8b`, `lane/l9`, `lane/stitch` (and
`lane/ltick`, which I was not told about and did not look at). **All merged since: Part 2.**

## Conflicts of substance, and how each was resolved

1. **`engine/src/generate.ts`, l5a against l7b** (the list of inputs the return generator does not draw, and the
   answers set at the end of `buildInputs`). Both sides' additions kept: l7b's Schedule 1 and Schedule 2 ids and
   `s1.uc_any`; l5a's `div.other_boxes`, `sb.nominee`, `sb.bonds_any` and the five foreign parents. `sb.foreign_any`
   left the list and lost its assignment (l5a made it a derived line).
2. **`engine/src/generate.ts`, l4b against l5a** (`EARLY_ROOTS`, `EARLY_SET`). l5a's `FOREIGN_PARENTS` kept; `x_other`
   left `EARLY_ROOTS` (l4b made `person.x_other` a derived line).
3. **Bank entries for ids that are no longer inputs (l4b's request).** `person.age65`, `person.under16`,
   `person.died_before_65` (reworded by lane 1) and `person.born_after_1960`, `person.born_before_2001` (renumbered by
   lane 2b to 311) deleted from `interview/2025/questions.yaml`. Lane 1's wording that went with them (a rewording
   for the stitch to carry onto l4b's questions if wanted): `under16` help "A return for a person under 16 is outside
   what this tool prepares; a Yes ends the interview here."; `age65` help "That is, 65 or older at the end of 2025.";
   `died_before_65` prompt "Is this the final return of someone who died in 2025 before reaching age 65?", help "A
   person reaches age 65 on the day before the 65th birthday." `person.edu_born_2007` and `edu_born_2002` (lane 8b's)
   are gone from the bank on this branch; **when l8b is merged its two entries must be deleted the same way.**
4. **`interview/2025/coverage/credits.yaml`, row `credits.elderly_65`.** l4b's side taken (`birth_year: 1955`,
   `work_ssn: true`); the other side's `died_before_65: false` answers a question that no longer exists.
5. **Bank frames, l8a against l2b and l7b.** `dcprov` and `oi8z` as l2b and l7b shortened them, `f1095a` as l8a
   shortened it ("On this Form 1095-A — ").
6. **`interview/2025/coverage/hsa.yaml`, row `hsa.testing_period_no_account`** (the row that ends at `s2.other`): l7b's
   restated answers kept (`$f8889: []`, `s2.hsa_testing: true`); l8a had not changed the row (context only).
7. **`tools/interview_rules_baseline.json`: lane 5b's `scveh.owned` entry taken out** (the file is as it was: all three
   lists empty). What `interview-rules` then reports is under "What is red".

Answers under ids that are no longer inputs, found by `tools/draft/stale_ids.py` and restated (same filer, same end):

| Where | Was | Now | Why |
|---|---|---|---|
| `coverage/care.yaml`, set `low_earner` | `born_after_1960: true`, `born_before_2001: true` | `birth_year: 1980` | l4b: one birth year; the set says "aged 25 to 64" |
| `coverage/marketplace.yaml`, `marketplace.married_in_2025` (l8a) | `household.married: true` | `household.married_dec31: true` | lane 1's rename |
| `personas/03_single_parent_child_care.yaml` | `household.unmarried: true` beside `household.ever_married: false` | the first line removed | lane 1 made it derived; an earlier union had kept the line lane 1 removed |
| `coverage/credits.yaml`, `credits.form2439` (l5b's rewrite) | `sb.unsupported: false` | `sb.nominee: false`, `sb.bonds_any: false` | l5a took `sb.unsupported` apart |
| `personas/04_retired_couple.yaml` | `age65`, `died_before_65` per person; `household.married` | birth years 1954 and 1956 (l4b's); the old lines removed | the crude union had kept lines one side removed; remerged by line |
| `interview/2025/sales.yaml` (profile list) | `person.age65` kept, `qbi.unsupported` re-added by the union | remerged by line | the same |

## Merge tools (`tools/draft/`), as changed tonight

- `merge_lane.sh`: no longer runs the full check after a merge (the integrator builds and checks by hand).
- `merge3.py`: writes a JSON file back in the file's own format (the indent and escaping that reproduce our side byte
  for byte), so a merge's diff shows only the merge.
- `list3.py` (new): a three-way merge by line for the personas and the profiles' question lists, in place of
  `union.py`, which kept lines one side had removed. It exits 1 naming any answer both sides changed.
  `merge_lane.sh` still calls `union.py`; after it, run `python3 tools/draft/list3.py <path>` (merge open) or
  `... <path> HEAD^2 HEAD^1` (merge committed) on each file it reports as unioned.
- `stale_ids.py` (new): lists every answer stated for an id that is not an input of the forms (fixture inputs,
  coverage rows and sets, personas, profile lists, bank entries). Run after every merge; 0 on the current tree.

## Coverage rows restated (answers only; no `expect` changed)

On the first run of the rows on the merged tree `interview-coverage` reported **95 problems in 9 files** (303 rows
walked). None was a wrong end reached on the row's own answers: every one was a question met that the row did not
answer, a refusal that showed only once a background answer was given, or an answer the walk no longer asks for
before its end. Cause, read from the messages and the bank: the rows were written on lane branches without the
order mechanism; on the merged tree a question that states a `seq` opens as soon as the return needs it
(`order.md` 1.4), and other lanes' questions now stand before or after a row's own.

`tools/draft/fix_rows.py` applied what the check named (add the closed answer; add the answer the background gave;
remove the answer never asked), in repeated passes until each file walked clean. Set by hand: `retirement[..].box1`
900000 where an IRA or plan filer is asked the amount; `s1.prizes` 3750000 for the Olympic medallist;
`sales[a].code: none`. The changes, by answer (count of rows):

| Added | Rows | Why the row meets it now |
|---|---|---|
| `retirement.under59: false` | 21 | lane 4a's `seq` puts it after the code; with the order mechanism it is asked there, before the one-line questions |
| `retirement.box1` (an amount), `retirement.not_beneficiary: false` | 6, 4 | the same: an IRA's box 1 follows the account; the code 4 check follows the code |
| `s2.other_tax: false` (7), `s2.amt_owed: false` (4), `s3.credit_bond: false` (4), `s3.farmland: false` (3), `sd.trader_election: false` (2), `s3.prior_other_forms: false`, `s1.digital_income: false` | 22 | the row's refusal now shows only when this later question of the same line is answered (see "What the stitch will need", item 3). The row's filer answers it No |
| `s2.lookback: false` (6), `s2.mortgage_subsidy: false` | 7 | lane 7b's new questions, asked of a filer with a business (lane 6a's rows) or a mortgage credit certificate |
| `sc.line1: 0` (4), `sc.line35: 0` | 5 | lane 6a's `seq` asks the amounts before the business screens the credits rows end at |
| `ftc.taxes: 0` (4), `s3.section965`, `s3.section960c`, `s3.virgin_islands` | 8 | lane 5a's gate: `s3.foreign_any` now opens `ftc.taxes`; the three children are asked in `seq` order before the row's own |
| `sd.route_each`, `sd.f2439`, `sales.proceeds`, `reported_basis`, `code` | 7 | lane 5b's questions met by lane 5a's dividend rows and by its own two refusing sale rows |
| `div.other_boxes`, `div.box3`, `box9`, `box10` | 5 | lane 5a's parent over the rare boxes, in rows of lanes 5a and 5b |
| `dependent.own_money`, `parents_apart`, `disabled`, `gross_income` | 5 | lane 2a's `seq` order, asked before the row's refusing question |
| `person.sav_roth: 0` (2), `sav_student`, `sav_voluntary`, `sav_able`, `s1.uc_repaid`, `s1.alimony_received`, `s1.alimony_paid`, `s1.prizes` | 9 | questions of the same block now asked before the refusing one |

| Removed (never asked before the row's end) | Rows |
|---|---|
| `f1040.tax_exempt_interest` | 5 social security rows (lane 5a moved it to 271; it no longer interrupts social security) |
| seven answers of `retirement.ordinary_ira`; `dependent.citizen_ssn` (3), `multiple_support`, `kidnapped`, `divorced_rule` | rows that end at an expected question (`asks`), which now comes before these |
| `div.box13`, `box10`, `box2e`, `box3`, `box9` of `credits.form2439`; `div.box3` of `dividends.liquidation`; `ftc.carryover` of `credits.form1116`; `work_ssn`, `s3.elderly_credit` of `saving.age_73_minimum_missed` | the refusal comes before them now |

**Two rows are weaker than their authors meant, and their `expect` was not touched:**
`retirement.ordinary_ira` ends at `asks: retirement[r].box1`, which now follows the account at once, so the row no
longer shows an ordinary IRA withdrawal passing every one-line question; `dependents.parents_apart_no_release` ends at
`asks: dependent[kid].own_money`, which is now asked before the release question (`divorced_rule`), so it no longer
shows what follows a No to it. Each wants a later expected end, which is its lane's (or the coordinator's) to choose.
`docs/provisional/lanes/l4a_work/coverage.py` no longer reproduces `coverage/retirement.yaml` (the file's header says
so).

## Personas

| Persona | What was wrong | What was done |
|---|---|---|
| `03_single_parent_child_care` | not readable (a key twice); `household.unmarried`; seven answers never asked (`dependent[child].self_support`, `joint_return`, `months`, `citizen`, `work_ssn`, removed by lane 2a; `dc_incapable`, `dc_under13`, not asked on lane 2b) | the lines removed; all were kept by the crude union of earlier merges |
| `04_retired_couple` | `age65`, `died_before_65`, `household.married` kept by the union | remerged by line: the birth years 1954 and 1956 (lane 4b's) describe the same couple, 71 and 69 |
| `13_ira_saver` | asked `ira.se_capital` ("Is any Schedule C income ... not from personal services?") though the filer has no business | a placement fix in the bank, below; the persona is unchanged |

**One placement changed in the bank: `ira.se_capital` from order 181 `seq` 5 to order 263 `seq` 1.** Its gate
(`ira.se_capital_gate`, `forms/2025/ira.yaml`) is a conjunction of "a traditional IRA contribution", "the return has a
business" (`s1.has_sc`) and the answer. Lane 4b numbered it in the IRA topic (181) when the list of businesses was
at order 11; lane 6a moved that list to 250. With both, the question was asked of every IRA contributor before the
interview knew whether there is a business (seen: persona 13, question 70 of 113; after the move it is not asked,
112 questions). Placed after the list it is asked only of a filer with both, as lane 4b's help text says. No form
changed. `interview-rules` had not reported it (0 problems before and after).

## Checks

All on this clone, 2026-11-13, one check at a time. "Tree" below is the tree of commit `a68c060a` (all eleven lanes
named under "State", the rows and personas restated, the one placement); the commit after it adds only generated
files (`reports/`, `rendered/`, `docs/provisional/walks/after/`, `order_merged.md`) and these notes.

| What was run | On | Result |
|---|---|---|
| `npm run build --silent` | each of `370bb945`, `d1e492c6`, `18859943`, and the tree after l5b | build OK each time |
| `node engine/dist/main.js test-fixtures` | the same four | 1,854 of 1,854 each time |
| `tools/draft_check.sh --quick` | `a68c060a` | **green**: build OK (213 s); fixtures 1,854 of 1,854; interview-rules 0 problems (177 walks, 415 answered in a random order), with `tools/interview_rules_baseline.json` empty; interview-coverage 0 problems (303 rows in 14 files) |
| `node engine/dist/main.js draft-walk` | the same build | 13 personas, 0 problems, each at the end it states; written to `docs/provisional/walks/after/` |
| `node engine/dist/main.js interview-order --write docs/provisional/lanes/order_merged.md` | the same build | written; 559 of 737 questions state a `seq`; 20 gated questions not placed directly after their parent |
| The other steps of `tools/draft_check.sh`, each by hand, once: `spouse-wording --report` then `--report --check`; `spouse-wording --self-test`; `check-self-test`; `test-integration`; `properties`; `test-serve`; `draft-walk --self-test`; `interview-order --self-test`; `tools/check_twins.py`; `render` then `render --check` | the same build | all pass (integration 811 invocations; properties 9 over 400 generated returns, 0 failing; twins 0 problems) **except `test-serve`**, below. `render --check` first failed on `rendered/2025/sd.md` and `index.md` (stale generated files) and passes after `render` |
| `python3 tools/draft/stale_ids.py` | the same tree | 0 answers stated for an id that is not an input |

**interview-rules on the merged tree.** Lanes 2b and 5b each saw problems on their own branch (`person.tin`,
`dependent.edu_tin_issued` on `generated.10`; `scveh.owned` on `generated.6`). On the merged tree, with the baseline
empty, the check reports **0 problems**, run twice (before and after the placement of `ira.se_capital`). So there was
nothing to classify. This does not show the leaks are gone: the generated returns reshuffle whenever inputs are
added (T-290), and the four lanes still to merge will reshuffle them again. Neither lane's reported problem was
reproduced or traced here.

Not run: the whole `tools/draft_check.sh` in one go on the final commit (its steps were run as listed, the four
quick ones by the script and the rest by hand); the New York fixtures by hand; any review, the Lean comparison,
mutation testing, the differential engines, `tools/check_all.sh`.

## What is red

*(As at `1a4e3023`. `test-serve` was mended by the coordinator's decision: Part 2, "Checks on the merged tree".)*

**`test-serve` fails** (outside `--quick`; every lane's own branch passed it):
`a new return has the filing status and spouse-phrased questions pending (both forms of the phrase, and one in a help
text)` (`engine/src/serve-check.ts`, the assertion after `const helped = ...`).

Seen: a return created on a scratch server (`serve --dir <scratch>`, `POST /api/returns`) has 82 questions pending,
`f1040.status` among them, six yes or no prompts with "(or, on a joint return, your spouse)" and six with the
possessive form, and **no pending question whose help text carries the phrase**. The bank entries with the phrase in
their help: 12 at the redraft's base (`f1040.line25b`, `f8959.unsupported`, `ftc.taxes`, `ftc.all_passive`,
`ftc.statements`, `f8960.refund`, `f8960.unsupported`, `s3.virgin_islands`, `sa.line11`, `sa.line5c`, `sa.line8a`,
`sa.unsupported`); lane 1's branch has 11 (no `f1040.line25b`), lane 7b's 11 (no `f8959.unsupported`), lane 5a's 9 (no
`ftc.*`); the merged bank has 7, none of them pending on a new return.

Inferred (not traced in the test's history): the test took its example from whichever of `f1040.line25b`,
`f8959.unsupported` or `ftc.taxes` was pending first, each lane removed one and left the others, and the three
together leave none. It is a premise of the server test about the interview's wording, not a fault in what the server
serves: the same run's rewording assertions were not reached. **Left red.** Not fixed, because either remedy is a
decision: change the test to take its help example from a state where one is pending (an edit to a check), or keep
the phrase in the help of some question a new return asks (wording added for a test).

Nothing else is red on what was run.

## What the stitch will need (seen while merging; not started)

*(As at `1a4e3023`. Replaced by Part 2's current list; kept for its detail, which Part 2 cites.)*

1. **178 of 737 bank entries still carry an old order number (below 100) and no `seq`:** order 0 (`$person`,
   `f1040.status`, and lane 9's three `scope.*`), 2 (`household.ever_married`, `married_dec31`, `spouse_died_2025`;
   `person.birth_year`, `born_jan1`, `under16_at_year_end`), 5 (`$gift`, `sa.gifts`), 10 (34: `sa.*` 11, `refund.*`
   16, `gift.*` 3, `ftc.carryover`, `person.died_at_64`, `f8863.paid`, `sli.interest`), 11 (`$asset`, `$scveh`,
   `sa.gambling_losses`), 12 and 15 (`scveh.*`, `asset.*`, `s179.*`), 21 and 31 (the education questions), 24 to 27
   (`f5695.*`). Most belong to the four lanes not yet merged (6b, 7a, 8b, 9). The ones that belong to merged lanes:
   - lane 1's five: `$person` 100/1, `f1040.status` 100/2, `household.ever_married` 101/1, `married_dec31` 101/2,
     `spouse_died_2025` 101/3 (its notes, "Order numbers and `seq`"; held back because 19 `stage4` fixture walks and
     three `hsa` rows fail while other questions are below 100);
   - lane 4b's four at the head of 110: `person.birth_year`, `born_jan1`, `under16_at_year_end`, `died_at_64`.
     `person.blind` already holds 110 `seq` 4, so the four cannot be 1 to 4 as lane 1's table had its three: `blind`
     moves to 5, or `died_at_64` goes after it;
   - lane 5a's `ftc.carryover`: to 279 directly after `s3.foreign_any` (its request to lane 7b).
2. **When l8b is merged:** delete its bank entries `person.edu_born_2007` and `person.edu_born_2002` (derived lines
   since lane 4b). When l9 is merged: `scope.archer_msa` and `scope.reservist_repaid` overlap lane 4b's
   `person.x_archer_excess` and `ira.reservist_repaid` (one of each pair goes). After every merge:
   `tools/draft/stale_ids.py`, then `list3.py` on each file `merge_lane.sh` reports as unioned.
3. **Refusals told late (N11), seen in the coverage walks.** A refusal shows only when no screen ahead of it on the
   same line is unanswered (`order.md` 1.4). Where a lane took a catch-all apart into items with different order
   numbers, a Yes to an early item is not told until the last item of the line is answered:
   - `s2.other` (derived, lane 7b): `s2.w2_marks` (148), `s2.household_employee` (159), `s2.hsa_testing` (193),
     `s2.credit_recapture` (291) refuse only after `s2.amt_owed` (292);
   - `person.x_other` (derived, lane 4b): its six items (177, 180, 192, 247) refuse only after `s2.other_tax` (293);
   - the electric vehicle children (`s3.ev_dealer`, `s3.ev_credit`, `s3.ev_equipment`, 225) only after
     `s3.credit_bond` (290); `s3.section965`, `s3.section960c`, `s3.virgin_islands` (279) only after `s3.farmland`
     (290); `s3.mcc` (215) only after `s3.prior_other_forms` (290);
   - `s1.cod_unsupported` (160) only after `s1.digital_income` (161);
   - a sale's own refusals (`sales.special`, a digital asset box; 274 `seq` 4 and 5) only after the block's
     once-per-return questions through `sd.trader_election` (`seq` 27), and after the sale's proceeds, basis and code.
   Which line and which entry order holds each back was read from the check's messages ("came on a background
   answer"), not traced in the forms. The remedies are `order.md`'s: number the screens of one line together, or
   reorder the line's `refuses` entries.
4. **Questions that read whether the return has a business, numbered before the list of businesses (250):**
   `ira.se_capital` (moved, above); `carloan.col_ii_input` (221 `seq` 12) waits on `$sc` through
   `carloan.sc_interest` and so is asked after 250, away from its topic (read in the form; not seen in a walk, no
   persona has a car loan).
5. **From `interview-order` (`order_merged.md`):** the late questions and what each waited on (the frequent ones
   are lane 7a's unmerged `sa.*`: `sa.elect_itemize` and `person.blind` wait on `sa.dependent`, `sa.line1` and
   `$gift` on `sa.excluded_income`; `person.eic_ssn` waits on `$oi8z`); children the bank does not place after
   their parent (`sd.f2439` at 274 `seq` 28 under `div.any` at 272; `div.other_boxes` at `seq` 7 and
   `sd.distributions` at `seq` 4 under `div.any`; `sales.route` under `sd.route_each`); 20 gated questions not placed
   directly after their parent.
6. **Requests between lanes that can be met now that both sides are on the branch** (each is in the named lane's
   notes): gate `s1.alimony_any` on `household.ever_married` (7b, request 2); one social security card question in
   place of `person.tin`, `work_ssn`, `eic_ssn` (2b to 4b); `f8889.age55` and `person.simple_age` from
   `person.birth_year` (4b to 8a and 6a); `f1040.tax_exempt_interest` met by a Marketplace filer at 195 (8a to 5a);
   the wording of `sd.distributions` (5a to 5b); `s2.household_employee` against `dcprov.household` (2b to 7b).
7. **Lane 1's wording for the three age questions lane 4b replaced** is in "Conflicts", item 3.
8. **Tick-box groups:** every lane's notes have a section "Candidates for one tick-list"; `lane/stitch` and
   `lane/ltick` were not read.
9. **Two coverage rows want a later expected end** ("Coverage rows restated").
10. **Outside the draft check, named by the lanes and not looked at:** `engine/src/umbrella-what-if.ts` names
    `sb.foreign_any` as an input; `tools/engines/generate_cases.py` names `sd.other_forms`; `tools/year_ids.json`
    lists four birth ids as inputs; `interview/2025/gate_frequencies.yaml` refers to lines that are now derived.

## Next

*(As at `1a4e3023`; all four steps are done. Part 2 ends with the current "Next".)*

1. When the coordinator releases `lane/l6b`, `lane/l7a`, `lane/l8b`, `lane/l9`: for each,
   `tools/draft/merge_lane.sh lane/<x>`; resolve what it leaves open; `python3 tools/draft/list3.py <path>` on each
   file it reports as unioned; `python3 tools/draft/stale_ids.py`; `npm run build --silent`;
   `node engine/dist/main.js test-fixtures`; commit. Then `interview-rules`, and the rows:
   `node engine/dist/main.js interview-coverage --rows interview/2025/coverage/<file>.yaml > out.txt;
   python3 tools/draft/fix_rows.py out.txt` in passes (read what it prints: it gives the closed answer, and an amount
   or a choice the filer has must be set by hand with `--values`). Then `draft-walk`.
2. `lane/stitch` (tick-box groups with the order mechanism) after them; then the list under "What the stitch will
   need".
3. `test-serve` (under "What is red") needs the coordinator's decision.
4. After the last merge regenerate: `npm run build --silent`, `interview-coverage --write`,
   `spouse-wording --report`, `properties`, `render`, `draft-walk`, `interview-order --write
   docs/provisional/lanes/order_merged.md`, and run `tools/draft_check.sh` whole.

# Part 2: the last five merges (second integrator)

Integrator: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call, no model call from
code, nothing pushed, nothing outside `.claude/worktrees/provisional` written, no lane worktree edited. Started from
`1a4e3023`. **A successor reads "State after the five merges", "What is red now" and "What the stitch will need
(current list)"; Part 1 above is the first integrator's record and is unchanged except where it points here.**

## State after the five merges

All fifteen lanes, the walk tool, the order mechanism and the tick-box groups are on the branch.

| Merged | Merge commit | Follow-up commit | Build | Fixtures on the follow-up commit |
|---|---|---|---|---|
| `lane/stitch` (holds `lane/ltick`) | `bc11616c` | in the merge commit | OK | 1,854 of 1,854 |
| `lane/l8b` | `c747ed7b` | `b8e59380` (two bank entries deleted) | OK | 1,854 of 1,854 |
| `lane/l6b` | `a6c21fc0` | none needed for the build | OK | 1,854 of 1,854 |
| `lane/l7a` | `94e8f885` | `6239dbba` (fixture inputs, the sales profile) | OK on `6239dbba`; `94e8f885` alone does not build | 1,854 of 1,854 (1,852 before the two input restatements of `6239dbba`) |
| `lane/l9` | `c0d6c710` | `84cb0657` (five coverage answers) | OK | 1,854 of 1,854 |
| rows, personas, the server test's example | | `d5a35855` | OK | in the whole check, below |

## Conflicts of substance, and how each was resolved

1. **`lane/stitch`: the proof group `rare_events` is not declared.** Lane 7b's order numbers were kept for the six
   Schedule 3 questions: `s3.credit_bond` 290/1, `s3.farmland` 290/2, `s3.farmland_deferral` 290/3,
   `s3.repaid_income` 290/4, and `s3.kerosene` 225/6, `s3.kerosene_credit` 225/7. The map puts kerosene in the topic
   "Electric vehicles and home fuel" (225 to 229), so the four members cannot share an order number without moving a
   question out of its topic, and the build refuses a group on two order numbers. The bank therefore has no `groups`
   entry and no `group` or `tick` field. Kept: the engine, server, page and vetting code, the build's group rules,
   `tick-groups` and `tick-groups --self-test` (constructed cases, 33 planted banks). **Not run any more:** the
   tick-box section of `test-serve` (`engine/src/serve-check.ts`, about 135 lines: the screen served, answered with
   some, none and a refusing box, rejected screens, a member answered earlier, the vetting card). It is written on
   that one group and on a federal fixture that answers its four members; it now runs only when the bank declares a
   group `rare_events` and otherwise prints "serve: tick-box screen not tested here". So the route `/answers` has
   no server test on this tree until a group is declared and that section is pointed at it. `ui/test_browser.mjs`
   (not in the check) still walks to the group and was not edited. `interview/README.md`: the two sentences that
   said the group is in the bank at order 13 were corrected.
   Inferred from the rules, not built: a three-member group at 290 (`s3.credit_bond`, `s3.farmland`,
   `s3.repaid_income`, with `s3.farmland_deferral` moved to follow `s3.repaid_income`) would be accepted. It was not
   made: the instruction was four members or none, and the server test is written on four.
2. **`lane/l8b`: `person.edu_born_2007`, `person.edu_born_2002`.** The structural merge left two stub entries
   (order 243, `seq` 1 and 2, no words); deleted. Order 243 now holds `person.edu_half_support` 3,
   `person.edu_fulltime` 4, `person.edu_parent` 5.
3. **`interview/2025/coverage/credits.yaml`, at the l6b, l7a and l9 merges.** Each lane had restated the business
   rows' answers on its own branch (the Schedule C amounts, the mortgage rows). Our side taken for every conflicting
   hunk, since the first integrator had already restated those rows for the merged order; the lanes' other changes to
   the file came through (`credits.partnership_credit` now answers `scope.k1`; the two mortgage rows answer
   `sa.home_owner` and `sa.mortgage_interest`). The rows were then walked and restated ("Coverage rows", below).
4. **`engine/src/generate.ts`, l7a against l7b, l5a and l8a** (`NOT_DRAWN`, `FIXED`). Both sides kept: our lists
   with lane 7a's twelve `sa.*` ids added to `NOT_DRAWN` and its nine Schedule A parents and guards added to `FIXED`;
   lane 7a's line that still named `sb.foreign_any` and the old `s1.line8*` ids was not taken.
5. **`sa.line8a` renamed by lane 7a; read by lane 7b's `s2.mortgage_subsidy`.** No form change was needed:
   `sa.line8a` is still a line (the printed line 8a, a `choose` on `sa.home_asked`), and `s2.yaml` and `s3.yaml`
   read it as before (read in `forms/2025/s2.yaml` line 150 and `s3.yaml` line 744; the build accepts it). What had
   to change was inputs: seven fixture cases that lane 7b had given `sa.line8a: 0` (`stage12.refuse.form4137_*` (2),
   `stage4.refuse.s2.other`, `stage4.refuse.s2.amt.simultaneous`, `stage18.refuse.s2_other_before_8962`,
   `stage8.refuse.s8812.s2_other`, `classm.s1a.7`) now state `sa.mortgage_interest: 0`; the class M case, which
   takes no defaults, states `sa.home_owner: false`, `sa.home_other: false` instead (no home, so no interest).
6. **Lane 7a's `sa.foreign_tax_deduct` against lane 5a's gate on `ftc.taxes`.** Lane 7a gates the question on
   `ftc.has_tax`; on the merged tree `ftc.taxes` is asked only of a filer with dividends, taxable interest or a Yes
   to `s3.foreign_any`. Three artifacts, all inputs: the `sales` profile did not list `s3.foreign_any` (the build:
   "no question for reachable input s3.foreign_any", for at least 40 cases; only the end of that build's output
   was kept), added; `mutation.t2.no_itemize_f8960_9a` (no
   defaults) states `s3.foreign_any: false` beside its `ftc.taxes: 0`; the row `home.foreign_tax_deduction` answered
   the foreign tax amount without the parent and so completed where it expects a refusal: it now answers
   `s3.foreign_any: true` first (the filer paid tax to another country) and is refused at `sa.unsupported` as it
   states.
7. **Lane 9's rows and one of lane 6a's answered ids that other lanes made derived lines**
   (`tools/draft/stale_ids.py`):

   | Row | Was | Now | Why |
   |---|---|---|---|
   | `scope.business_property_sale` | `sd.other_forms: true` | `sd.sold_other: true`, `sd.business_property: true` | lane 5b took `sd.other_forms` apart; the row still ends at `sd.other_forms` |
   | `scope.care_benefits_other` | `f2441.student_disabled: false` | `f2441.student: false`, `f2441.unable: false` | lane 2b's two questions |
   | `scope.lump_sum` | `retirement[plan].special: true` | `born_1936: true`, `lump_sum: true` (and the plan's other one-line questions, code `normal_7`) | lane 4a took `retirement.special` apart; the row still ends at `retirement[plan].special` |
   | `scope.couple_not_asked_age` | `household.married: true` | `household.married_dec31: true` | lane 1's rename |
   | `business.qbi_other_income` (lane 6a) | `scope.schedule1: true` | `scope.k1: true` | lane 9; the row's situation is a Schedule K-1; it still ends at `scope.schedule1` |

8. **Personas and `stage4.yaml`, at the l9 merge.** `merge_lane.sh` unioned four personas and the profile list;
   each was remerged by line with `tools/draft/list3.py` (no answer changed by both sides).

**No conflict between two lanes' model changes was found**: no fixture's expected value or refusal had to change
(1,854 of 1,854 after input restatements only), and no row's `expect` was changed (each row's `expect` was compared
by script with the same row on `1a4e3023` or on its lane's branch: 447 rows, 0 differ).

**The two overlapping pairs, both kept (instruction):**

| Lane 9 | Lane 4b | As they stand |
|---|---|---|
| `scope.archer_msa` 191/1 "did you put money into an Archer MSA" (everyone; refuses through `scope.schedule1`) | `person.x_archer_excess` 192/2 "Was more put into an Archer MSA of yours than its limit, and is the extra still there?" (per person; refuses through `person.x_other`) | a filer with an Archer MSA is refused at 191; the second is asked of everyone who says No to the first |
| `scope.reservist_repaid` 113/7 (beneath `scope.armed_forces`; refuses through `scope.other_income`) | `ira.reservist_repaid` 181/3 (only with a traditional IRA contribution; refuses) | the same fact asked twice of a reservist with an IRA contribution |

Two more of the same kind, seen in the bank and not asked for: `scope.w2_marks` 146/1 (box 13 statutory employee,
box 12 code H) beside lane 7b's `s2.w2_marks` 148/1 (box 8, box 12 codes A, B, K, M, N, Z): two questions about the
same boxes of the same paper; `scope.excess_deferral` 187/1 beside `person.sav_excess` 315/5: nearly the same
sentence, the second asked only inside the saver's credit.

## Coverage rows restated (answers only; no `expect` changed)

First run on the merged tree: **143 problems in 7 files** (447 rows in 18 files walked, 697 s). One was a wrong end
on the row's own answers (`home.foreign_tax_deduction`, item 6 above); every other was a question met that the row
does not answer, a refusal that showed only on a background answer, or an answer no longer asked before the end.
`tools/draft/fix_rows.py` applied what the check named, file by file, in passes; what it could not do was set by
hand. By cause:

| Change | Rows | Why |
|---|---|---|
| `vehicles_equipment.yaml`: the set `business` rewritten from persona 05 as merged (lane 6b's own recipe: its answers without the vehicle, the equipment list and the estimated payments) | all 40 rows that use it | lane 6a's business questions (`sc.travel_meals`, `sc.employees`, `sc.goods` as parents; the amounts beneath them asked only after a Yes); 63 of the 143 problems |
| the same file: `asset[item].cost: 200000` (10 rows), `scveh[car].cost: 3000000` (2), `asset[item].pct: 100` (1), `scveh[car].miles_business: 4200` (2); `asset.got_other`, `before_2017` No in `equipment.screen_qbu_low` | 15 | the amount is now asked before the refusing screen the row ends at (the order mechanism; lane 6b wrote the rows on a branch without it). The values are those of `l6b_work/coverage.py` |
| `scope.se_plan_other: false`, `scope.income_averaging: false` | 6 rows of `business.yaml` | lane 9's two questions asked of a filer with a business |
| `scope.business_before: false` | 11 rows of `other.yaml`, 4 of `home.yaml` | the row's refusal now shows only when this last Schedule 1 item is answered ("Refusals told late") |
| `s3.foreign_any: false` | `home.gift_carryover_only`, `home.gifts_limited`, `sales.interest_election_too_large` | the same, through `sa.foreign_tax_deduct`'s gate (item 6) |
| `s1.olympic: false` | `other.professional_gambler` | asked before the refusing question now |
| `s2.mortgage_subsidy: false` (2 rows of `home.yaml`); `sa.mortgage_unreported`, `sa.mortgage_over_limit`, `sa.mortgage_other_use`, `sa.line5b: 0`, `sa.property_tax_other_any` (`credits.mcc`) | 3 | lane 7b's and lane 7a's questions beneath mortgage interest, met by each other's rows |
| `f5695.carry: false` | 9 rows of `credits.yaml` that answer `s3.prior_other_forms: true` | lane 8b's carryforward question (239) is asked before `s3.prior_amt` and `s3.prior_forms` (290); lane 8b's notes foresaw it |
| `refund.received: 60000`, `refund.line5d_2024: 500000`, `refund.line5e_2024: 500000` | `home.refund_exception` | asked before the refusal shows; amounts set by hand for a filer who got a refund |
| `home.foreign_tax_deduction`: `s3.foreign_any: true`, its three children and `ftc.carryover` No | 1 | item 6 |
| `scope.yaml`: set `one_business` loses 14 answers never asked (the Schedule C amounts beneath lane 6a's parents); `scope.solo_401k` and `scope.income_averaging` answer `sc.travel_meals`, `employees`, `goods`, `hi_uses` No and `person.plan: none`; `scope.lump_sum` as in item 7 | 3 and the set | lane 6a's and lane 4a's questions |
| Removed, never asked before the row's end: `$asset` and `$scveh` (empty lists) in four business rows of `credits.yaml`; `s3.mcc` in `home.mortgage_over_limit`, `home.mortgage_other_use`; `s8812.combat_pay` in `scope.care_benefits_other`; `f4952.line1`, `f4952.carryover` in `sales.interest_election_asked` | 8 | the refusal or the expected question comes before them now |

**One row is weaker than its author meant, and its `expect` was not touched:** `sales.interest_election_asked`
expects `asks: f4952.line4g` and now reaches it on `f4952.has_interest: true` alone: the election question (277/5)
is asked before the interest amount `f4952.line1` (277/2) and `f4952.carryover` (277/3), against its numbers. Seen
in the row's walk; what the amount waits on was not traced (see `order_merged.md`, the late table). The two weaker
rows of Part 1 stand as they were.

`fix_rows.py` has one fault met here: for a choice (`Enum`) question it wrote `0`, which the interview rejects
(`person.plan`, `retirement.code`); both were set by hand (`none`, `normal_7`). The tool was not changed.

## Personas

| Persona | What was wrong | What was done |
|---|---|---|
| `13_ira_saver` (lane 4b's) | asked lane 9's three W-2 questions, unanswered | `scope.w2_marks`, `scope.artist_official`, `scope.excess_deferral` No, as lane 9 gave the other W-2 personas |
| `13_self_employed_actual_vehicle_computer` (lane 6b's) | 10 questions opened and unanswered, 15 answers never asked: its business answers were persona 05's of lane 6b's branch | its business answers are persona 05's as merged (the same designer: lane 6a's parents, `f1040.estimated_any`, birth year 1987, lane 9's two business questions, `qbi.suspended`, `s2.lookback`); its van and computer answers unchanged |
| `11_refused_rental`, `12_refused_nonresident` | nothing: lane 9 had already restated them | see below |

**Personas 11 and 12.** Each is refused on its own Yes at lane 9's plain question: the rental owner at
`scope.rental` (question 17 of her walk), the nonresident at `scope.nonresident` (question 10, after
`scope.noncitizen`). The gate id the refusal carries is the old screen's: `scope.schedule1` and
`scope.other_income`. Read in `forms/2025/scope.yaml`: those two ids are now derived lines (`any` over the items),
and the refusals stand on `scope.ready_schedule1` (`refuses: when: scope.schedule1`, form "Schedule 1") and
`scope.ready_other_income`. The personas' expected ends were already `{ refused: scope.schedule1 }` and
`{ refused: scope.other_income }` on lane 9's branch, and `draft-walk` reports those ends; nothing was edited.
There are two persona files numbered 13 (lanes 4b and 6b each added one).

## Checks on the merged tree

All on this clone, 2026-11-13, one at a time.

| What was run | On | Result |
|---|---|---|
| `npm run build --silent`, then `node engine/dist/main.js test-fixtures` | after each merge: the trees of `bc11616c`, `b8e59380`, `a6c21fc0`, `6239dbba`, `84cb0657` | build OK and 1,854 of 1,854 each time. On `94e8f885` alone the build fails ("no question for reachable input s3.foreign_any", the `sales` profile); with the profile fixed the fixtures were 1,852 of 1,854 until the two no-default cases stated their inputs (`classm.s1a.7`, `mutation.t2.no_itemize_f8960_9a`) |
| `python3 tools/draft/stale_ids.py` | after each merge and on the final tree | 0 on the final tree (892 inputs read) |
| `node engine/dist/main.js interview-rules` | the tree of `84cb0657` (all lanes merged, rows not yet restated) | 0 problems; 177 walks, 415 answered in a random order; baseline empty |
| `node engine/dist/main.js interview-coverage` | the same tree | 143 problems in 7 files (447 rows), restated as above; then each of the seven files alone with `--rows`, 0 problems each |
| **`tools/draft_check.sh`, whole, first run** | the tree of `d5a35855` with `rendered/2025/index.md` regenerated by `render` | fifteen steps green, **one red**: build OK (266 s); fixtures 1,854 of 1,854; interview-rules 0 problems (177 walks, 415 random orders); interview-coverage 0 problems (447 rows, 747 s); tick-groups passed (0 groups); person wording current; spouse-wording and check self-tests; properties; **test-serve 401 checks passed**; draft-walk, interview-order (692 checks) and tick-groups self-tests; twins 0 problems; render check. **Red: `test-integration`**, "missing s2.mortgage_subsidy" |
| `node engine/dist/main.js test-integration` | after the fix below (`cbdd0fb5`) | 1,027 CLI invocations passed |
| `node engine/dist/main.js draft-walk --out docs/provisional/walks/after` | the build of `cbdd0fb5` | 14 personas, 0 problems (no stale answer, none opened and unanswered), each at the end it states |
| `node engine/dist/main.js interview-order --write docs/provisional/lanes/order_merged.md` | the same | written; 843 of 853 questions state a `seq`; 65 gated questions not placed directly after their parent |
| `node engine/dist/main.js tick-groups` | the same | passed: `full` and `ny`, 0 groups |
| **`tools/draft_check.sh`, whole, second run** | commit `cbdd0fb5` (its last line: "draft-check: green (cbdd0fb5, tree d5ed2db6331d)") | **green, all sixteen steps**: build OK (274 s); fixtures 1,854 of 1,854; interview-rules 0 problems (177 walks, 415 random orders); interview-coverage 0 problems (882 s); tick-groups passed; person wording current; spouse-wording self-test; check self-test (95 cases); test-integration 1,027 CLI invocations; properties; test-serve 401 checks (29 fixture paths replayed, 665 expected values matched); draft-walk, interview-order (692 checks) and tick-groups (33 planted banks) self-tests; twins 0 problems; render check. The commit after it changes only this file |

**Two checks' sources were changed, both because a lane's question is now met by another lane's test:**

1. **`test-serve`, the help-text example** (`engine/src/serve-check.ts`; the coordinator's decision). A new return
   has no pending question whose help carries the spouse phrase (three bank entries still carry it in their help:
   `f8960.unsupported`, `f8960.refund`, `s3.virgin_islands`, each behind a parent). The test now answers
   `s3.foreign_any` Yes on its return when none is pending, which opens `s3.virgin_islands` ("Yes if you (or, on a
   joint return, your spouse) had income from the U.S. Virgin Islands ..."), and takes that as its example. Every
   later assertion is as it was: the help is served as stored with the status unanswered, in the joint reading
   under married filing jointly, and reworded again when the status is corrected. No wording was added to the bank.
2. **`test-integration`, the walk of `stage4.base` with a home owned** (`engine/src/integration.ts`; lane 7a's
   addition). After `sa.home_owner` Yes it answers each question asked from a fixed list; on the merged tree lane
   7b's `s2.mortgage_subsidy` is asked beneath the mortgage interest and was not in the list. Added, answered No;
   the asserted deduction (20,000.00) is unchanged.

Also changed in a check's source: the tick-box section of `test-serve` runs only when the bank declares the group
it is written on ("Conflicts", item 1).

**interview-rules on the merged tree: 0 problems**, with `tools/interview_rules_baseline.json` empty and untouched,
in two runs (by hand on `84cb0657`; in the whole check). So there was nothing to classify, no placement to fix and
nothing to leave red. This does not show the order-dependent leaks are gone (T-290): lanes 2b, 5b, 8b and 9 each saw
one on their own branch at some question count (`person.tin`, `dependent.edu_tin_issued`, `scveh.owned`,
`dependent.disabled`), the generated returns reshuffle whenever inputs are added, and any later change to the
question set will reshuffle them again. None of the four was reproduced or traced here.

Not run: the New York fixtures by hand; `ui/test_browser.mjs`;
any review, the Lean comparison, mutation testing, the differential engines, `tools/check_all.sh`.

## What is red now

**Nothing is red** on what was run: `tools/draft_check.sh` whole is green on `cbdd0fb5`, the personas walk clean,
`tick-groups` passes and the baseline is empty.

What that green does not cover, so that it is not read for more than it is:

- **The tick-box screen has no server test and no group in the bank** ("Conflicts", item 1). `tick-groups` passes
  on zero groups.
- Three coverage rows are weaker than their authors meant (item 7 of the list below).
- The order-dependent leaks of T-290 were not seen and not traced.
- Review debt: every form and question the fifteen lanes changed is unreviewed (NORMS section 5); the files of
  item 6 below are stale.

## What the stitch will need (current list; replaces the list in Part 1)

Seen while merging; none of it started.

### 1. Bank entries still below order 100 or without `seq`: ten, of 853

| Lane | Entry (order now) | Where its lane's notes put it |
|---|---|---|
| 1 | `$person` (0), `f1040.status` (0) | 100/1, 100/2 |
| 1 | `household.ever_married`, `household.married_dec31`, `household.spouse_died_2025` (2) | 101/1 to 101/3. Held back by lane 1 because 19 `stage4` fixture walks and three `hsa` rows failed while other questions were below 100; that condition is now gone but for the entries of this table, and the trial was not repeated |
| 4b | `person.birth_year`, `person.born_jan1`, `person.under16_at_year_end` (2), `person.died_at_64` (10) | the head of 110. `person.blind` holds 110/4 and is the only other entry of 110: the four take 1 to 4 and `blind` 5, or `died_at_64` follows it |
| 5a | `ftc.carryover` (10) | 279, directly after `s3.foreign_any` and its three children (279/1 to 4): 279/5 |

Every other entry states an order of 102 or more and a `seq` (843 of 853). Until these ten move, the opening is
asked as before (they sort first), and `person.died_at_64` and `ftc.carryover`, which state no `seq`, are asked
when the evaluation reaches them.

### 2. Refusals told late (norm N11)

A refusal shows only when no screen ahead of it on the same line is unanswered (`order.md` 1.4). Part 1's list
stands (`s2.other`, `person.x_other`, the vehicle and foreign children of Schedule 3, `s1.cod_unsupported`, a
sale's own refusals). Added by the last five merges, each read from the coverage check's message "the refusal came
on a background answer" and not traced further in the forms:

- **Lane 9's derived screens hold back other topics' refusals.** `scope.schedule1` is unknown until every Schedule 1
  item is answered No; its last item in the order of asking is `scope.business_before` (295/3, with its children
  `scope.nol`, `scope.passive`, `scope.f8978`). Fifteen rows now get their refusal only there: eleven of
  `other.yaml` (the Schedule 1 items of 148, 160 and 161: alimony recapture, canceled debt, digital income, inmate
  wages, a long-term care payout, deferred pay, the Olympic medal, option income, other income, a recovery, fund
  contributions) and four state refund rows of `home.yaml` (165). A Yes to a scope item itself is told at once
  (lane 9 gave each screen a line of its own, `scope.ready_*`; personas 11 and 12 are refused at questions 17 and
  10). The Schedule 1 items run from 113 to 295 and two of them are asked only once the list of businesses (250)
  is known, so renumbering alone cannot bring the screen's answer forward of topic 250. Lane 9's notes, "THE
  FINDING THE COORDINATOR NEEDS FIRST", give three remedies (the engine, direct targets, or the Schedule 1 items
  asked together early); none was tried here.
- **Schedule A's refusals wait for the foreign question.** `sa.unsupported` lists lane 7a's
  `sa.foreign_tax_deduct_if_tax`, which reads `ftc.has_tax`, which is unknown until `s3.foreign_any` (279) for a
  filer with no dividends or interest. Rows `home.gift_carryover_only`, `home.gifts_limited` (202) and
  `sales.interest_election_too_large` (277) are refused only at 279. The rows of the other `sa.unsupported` items
  (200, 204) were not seen late.
- **Lane 6b's screens come after the amounts.** In fifteen rows of `vehicles_equipment.yaml` the cost (or the
  business-use share, or the miles) of an item or vehicle is asked before the refusing question the row ends at:
  lane 6b numbered the amounts first, and with the order mechanism the numbers decide.
- `home.refund_exception`: after `refund.exc_tax` Yes the filer is still asked the refund amount and two 2024
  figures before the refusal shows (at `scope.business_before`).
- `credits.mcc`: after `s3.mcc` Yes (215) the filer is asked the three mortgage screens and the property tax
  questions (200, 201) first.

### 3. Requests between lanes that can be met now (each is in the named lane's notes)

Still open from Part 1: gate `s1.alimony_any` on `household.ever_married` (7b); one social security card question
in place of `person.tin`, `work_ssn`, `eic_ssn` (2b to 4b); `f8889.age55` and `person.simple_age` from
`person.birth_year` (4b to 8a and 6a); `f1040.tax_exempt_interest` met by a Marketplace filer at 195 (8a to 5a);
the wording of `sd.distributions` (5a to 5b); `s2.household_employee` against `dcprov.household` (2b to 7b);
`carloan.col_ii_input` (221/12) waits on the list of businesses (250).

New with the last five lanes:

- **8b to 7b:** `f5695.carry` and `f5695.line12` (239/1, 239/2) belong directly after `s3.prior_amt` and
  `s3.prior_forms` (290/6, 290/7): 290/8 and 290/9 are free. At 239 the carryforward question is asked before the
  two questions about the same 2024 return, and nine `credits.yaml` rows answer it for that reason alone.
- **7a to 7b:** `sa.gambling_losses` (204/7) directly after the gambling winnings questions
  (`s1.gambling_winnings` 160/14); it is asked only with winnings.
- **7a to 5b:** `sd.casualty` (216/1) must catch what `sa.unsupported` used to name: a personal casualty or theft
  loss, a loss of income-producing property (a financial scam included) and a disaster loss claimed with the
  standard deduction. Its help today speaks of things owned for personal use and a declared disaster; whether it
  covers the other two was not judged here.
- **7a to 9:** a gift to charity or a generation-skipping tax deduction that comes through a trust or a Schedule
  K-1 has no Schedule A question now; `scope.k1` (130/2) is its refusal.
- **9 to 2b:** `scope.care_benefits_other` (158/1) is beneath `f2441.benefits`; a self-employed person with a plan
  of their own reaches it only if that parent's wording does not speak of box 10 alone.
- **9 to 2a:** "Count costs your employer paid." in the help of `s3.adoption_any`, the guard of
  `scope.adoption_benefits` (127/2).
- **9 to 3:** `scope.w2_marks` asks box 13 and box 12 code H once per return; if the box 12 codes are asked per
  W-2, code H belongs there. See also the overlap with `s2.w2_marks`.
- **6b to 6a:** `scveh.fleet` and the two `short_year` questions are facts about the business or the person.
- **8b to 1 or 4b:** done by lane 4b (the two education birth questions are derived from `person.birth_year`).
- **The overlapping pairs** ("Conflicts", above): `scope.archer_msa` and `person.x_archer_excess`;
  `scope.reservist_repaid` and `ira.reservist_repaid`; `scope.w2_marks` and `s2.w2_marks`; `scope.excess_deferral`
  and `person.sav_excess`. One of each pair goes, or the two are made parent and child.

### 4. Tick-box groups

No group is declared in the merged bank. To declare one: `docs/provisional/lanes/stitch.md`, part 2 (the eight
rules), and `tick.md`. Three things first:

1. `test-serve`'s tick-box section runs only on a group `rare_events` with the four Schedule 3 members. When the
   first real group is declared, point that section at it (its constants `TICKS`, `OPENED`, the group id, and a
   fixture return that answers every member No).
2. Rule 8 (what a member's Yes opens follows the group at once) refuses lane 8b's three energy groups as numbered,
   and any group whose members are parents with their children between (lane 6a's first, lane 7b's second).
   Lane 8b's notes give the two ways out.
3. The rule wants consecutive `seq` numbers; the column below says which candidates have them today.

Every candidate the lanes proposed, with each member's order and `seq` as they stand in the merged bank
(generated from the bank by script; the headings and member lists are the lanes'):

| Lane | Heading | Members: order/seq in the merged bank | One order, consecutive `seq`? | Notes |
|---|---|---|---|---|
| 1 | About you (per person and per return; not proposed as built) | `person.blind` 110/4; `sa.dependent` 111/1 | no: 110, 111 (orders) | lane says none as built; old members person.under16, person.age65 are derived lines since lane 4b |
| 2a | About this child (or person): does any of these apply? | `dependent.other_claimant` 120/13; `dependent.parents_apart` 120/14; `dependent.ever_married` 120/15; `dependent.own_money` 120/16 | yes | per dependent |
| 2b | About that care. Do any of these apply? | `f2441.care_other` 155/3; `f2441.prior_year` 155/5; `f2441.student` 155/6; `f2441.unable` 155/7; `f2441.spouse_died` 155/8 | one order, `seq` not consecutive | after Yes to care; spouse_died joint returns only |
| 3 | About the tips from this employer, did any of these happen? | `tipjob.other_work` 151/3; `tipjob.charged` 151/4; `tipjob.unlawful` 151/5 | yes | per employer with tips |
| 4a | Is any of these true of this pension or plan payment? | `retirement.box6` 170/5; `retirement.disaster` 170/23; `retirement.loan_offset` 170/24; `retirement.disability` 170/25; `retirement.pso_exclusion` 170/29; `retirement.born_1936` 170/30 | one order, `seq` not consecutive | per Form 1099-R of a plan; disability and born_1936 open children |
| 4a | Is any of these true of this IRA withdrawal? | `retirement.charity_hsa` 170/20; `retirement.ira_returned` 170/21; `retirement.ira_basis` 170/22; `retirement.disaster` 170/23 | yes | per Form 1099-R of an IRA; retirement.disaster is in both of lane 4a's lists |
| 4a | Is any of these true of your social security benefits? | `ssb.repaid_more` 178/3; `ssb.ira_covered` 178/4; `ssb.prior_year_pay` 178/5; `ssb.terror_disability` 178/7 | one order, `seq` not consecutive |  |
| 4b | Did any of these happen with your IRA or your pay in 2025? | `ira.deferred_comp` 181/1; `ira.fellowship` 181/2; `ira.reservist_repaid` 181/3; `ira.care_payments` 181/4 | yes | only with a traditional IRA contribution; each refuses |
| 4b | Accounts with their own penalties | `person.x_edu_account` 247/1; `person.inherited_account` 177/1; `person.x_archer_excess` 192/2 | no: 177, 192, 247 (orders) | per person; three topics; the lane would leave them apart |
| 5a | Money, property and ties outside the United States | `sb.account_any` 285/1; `sb.asset_any` 285/2; `sb.trust_any` 285/3; `sb.company_any` 285/4; `sb.territory_any` 285/5; `scope.foreign_shares` 287/1 | no: 285, 287 (orders) | lane 5a proposes scope.foreign_shares (lane 9) as the sixth; it is a parent |
| 5b | Less common sales and trades in 2025 | `sd.sold_other` 274/20; `sd.sec1256` 274/24; `sd.condemned` 274/25; `sd.small_business_stock` 274/26; `sd.trader_election` 274/27; `sd.f2439` 274/28 | one order, `seq` not consecutive | sd.sold_other has three children; sd.f2439 asked only with dividends |
| 6a | Which of these did this business have in 2025? | `sc.employees` 252/20; `sc.goods` 253/1; `sc.travel_meals` 252/15; `sc.ho_uses` 254/1; `sc.hi_uses` 259/1 | no: 252, 253, 254, 259 (orders) | per business; each a parent with children between |
| 6a | Is any of these true of this business? | `sc.spouse_owned` 251/1; `sc.statutory` 251/2; `sc.business_credit` 251/6; `sc.fuel_credit` 251/7 | one order, `seq` not consecutive | per business; each refuses |
| 6b | What this item is | `asset.kind_excluded` 257/4; `asset.software` 257/5; `asset.industry` 257/7; `asset.long_production` 257/9 | one order, `seq` not consecutive | per item of equipment; software and industry open a child |
| 6b | How you got it | `asset.got_other` 257/14; `asset.before_2017` 257/15; `asset.used_before` 257/28 | one order, `seq` not consecutive | used_before is known to be needed only after the special allowance choice |
| 6b | What has happened to it | `asset.ended_2025` 257/16; `asset.basis_changed` 257/17; `asset.use_changed` 257/18; `asset.short_year` 257/19 | yes |  |
| 6b | How it is depreciated and where it is used | `asset.method_other` 257/20; `asset.ads_required` 257/21; `asset.outside_use` 257/22 | yes |  |
| 6b | How you got this vehicle and what has happened to it | `scveh.got_other` 255/17; `scveh.before_2017` 255/18; `scveh.converted` 255/19; `scveh.disposed` 255/20; `scveh.basis_changed` 255/21; `scveh.short_year` 255/22 | yes | per owned vehicle on actual expenses |
| 6b | How this vehicle is used | `scveh.for_hire` 255/23; `scveh.investment` 255/24; `scveh.others_use` 255/25; `scveh.method_other` 255/29 | one order, `seq` not consecutive | others_use opens three children |
| 6b | In earlier years | `scveh.prior_bonus` 255/30; `scveh.prior_smr` 255/31; `scveh.prior_low_use` 255/32 | yes |  |
| 7a | Uncommon deductions | `sa.estate_tax_income` 204/2; `sa.bond_premium` 204/3; `sa.debt_instrument_loss` 204/4; `sa.pension_unrecovered` 204/5; `sa.impairment_work` 204/6 | yes | each refuses |
| 7b | Look at your W-2s | `s2.w2_marks` 148/1; `s1.nqdc_pension` 148/2; `f8959.territory_w2` 148/3 | yes | lane 9's scope.w2_marks (146) is the same paper |
| 7b | In 2025, did you get any of these? | `s1.uc_any` 160/1; `s1.alimony_any` 160/5; `s1.cod_any` 160/10; `s1.winnings_any` 160/13; `s1.scholarship_any` 160/18; `s1.jury_any` 160/20 | one order, `seq` not consecutive | each a parent; children between |
| 7b | And any of these? | `s1.alaska_any` 161/1; `s1.hobby_any` 161/3; `s1.ltc_payout` 161/5; `s1.inmate_wages` 161/6; `s1.digital_income` 161/7 | one order, `seq` not consecutive |  |
| 8a | About the people your Marketplace plan covered | `f8962.shared_policy` 196/1; `f8962.divorced_enrolled` 196/2; `f8962.married_in_2025` 196/3; `f8962.no_family` 196/4; `f8962.not_lawful` 196/5; `f8962.incarcerated` 196/6 | yes | with a Form 1095-A; married_in_2025 joint returns only |
| 8a | About the premiums | `f8962.unpaid` 196/20; `f8962.a_zero_paid` 196/21; `f8962.premium_refunded` 196/22; `f8962.midmonth_start` 196/23 | yes |  |
| 8b | Did the work include any of these for making or storing energy? (energy_power) | `f5695.solar` 230/2; `f5695.solar_water` 230/3; `f5695.wind` 230/4; `f5695.geothermal` 230/5; `f5695.line5a` 230/6; `f5695.line7a` 230/7 | yes | after Yes to f5695.any; line7a refuses; opened costs do not follow the group directly (rule 8) |
| 8b | Did the work include any of these? (energy_shell) | `f5695.insulation` 230/8; `f5695.doors` 230/9; `f5695.windows` 230/10; `f5695.panel` 230/11; `f5695.audit` 230/12 | yes | the same |
| 8b | Did the work include any of this heating, cooling or hot-water equipment? (energy_heating) | `f5695.heat_pump` 230/13; `f5695.hp_water_heater` 230/14; `f5695.central_ac` 230/15; `f5695.water_heater` 230/16; `f5695.furnace` 230/17; `f5695.biomass` 230/18 | yes | the same |
| 9 | Income from things you own | `scope.rental` 130/1; `scope.k1` 130/2; `scope.farm` 130/3 | yes | each refuses |
| 9 | Pay for work that is not ordinary wages | `scope.pay_no_w2` 145/1; `scope.medicaid_waiver` 145/2 | yes | each refuses |
| 9 | Rare things | `scope.reforestation` 295/1; `scope.attorney_fees` 295/2; `scope.recovery` 168/1; `scope.disaster_distribution` 175/1; `scope.archer_msa` 191/1; `scope.education_recapture` 248/1 | no: 168, 175, 191, 248, 295 (orders) | placed by topic (N5); gathering them is the owner's choice |
| 9 | Did any of these apply to you in 2025? (about you) | `scope.noncitizen` 113/1; `scope.chapter11` 113/3; `scope.armed_forces` 113/4; `scope.under24` 113/8 | one order, `seq` not consecutive | three are parents; lane 9 lists it as possible only if the page allows parents |
| tick/stitch | In 2025, did you do any of these? (rare_events, the proof group; not declared) | `s3.farmland` 290/2; `s3.kerosene` 225/6; `s3.repaid_income` 290/4; `s3.credit_bond` 290/1 | no: 225, 290 (orders) | children s3.farmland_deferral, s3.kerosene_credit; kerosene is in topic 225 |

Of the 34 candidates, 17 are on one order number with consecutive `seq` today, 11 on one order number with gaps or other questions between, and 6 on several order numbers. Those marked "not consecutive" need renumbering (and, where a member is a parent, rule 8 or a
change of it); those on several orders need a decision about topics.

### 5. From `interview-order` on the merged tree (`order_merged.md`)

Measured on the build of `cbdd0fb5` (11 whole-return fixtures, 12 generated returns, 56 minimal returns). No order
number is re-entered for sorting; every re-entry is a question that became reachable part-way (per walk: 4.5, 3.1
and 5.1 order numbers re-entered). The frequent ones, with the answer each waited on and the number of walks:

| Question (place) | Waited on | Walks | Read |
|---|---|---|---|
| `person.blind` (110/4) | `sa.dependent` (111/1) | 75 | as before the merge (order notes 4.1); the two are numbered the wrong way round for it |
| `s1.inmate_wages` (161/6); `s1.nqdc_pension` (148/2) | `s1.nqdc_pension`; `s1.ltc_payout` (161/5) | 69; 67 | order 148 is re-entered after 161: lane 7b's items of one Schedule 1 line sit in 148, 149, 160 and 161. Why the reach pass does not open them was not traced |
| `sa.state_tax_any` (201/1) | `sa.elect_itemize` (204/1) | 69 | lane 7a's notes foresaw it: the state tax, property tax and (6 walks) `sa.line5b` questions wait for the choice to itemize, numbered after them |
| `household.ever_married` (2) | `f1040.status` (0) | 64 | the opening, still unnumbered (item 1) |
| `s2.hsa_testing` (193/1) | `sa.home_other` (200/2) | 63 | not traced |
| `person.eic_ssn` (311/4) | `scope.business_before` (295/3) | 57 | lane 9's finding: what stands behind a derived screen waits for its last item |
| `qbi.prior_form`, `person.plan`, `scope.se_plan_other`, `w2.box3`, `sc.at_risk` | `scope.business_before`, `$sc`, `s179.prior_form` | 1 to 3 each | the business list (250) and the scope screen |

Children the bank does not place directly after their parent: 65 gated questions (20 before the last five merges).
Many are as their lane numbered them: the home energy costs and conditions beneath their kinds (lane 8b numbers
every kind before any detail), lane 9's children whose parent is another lane's question
(`scope.adoption_benefits` 127/2 beneath `s3.adoption_any` 126/1). The list was not gone through one by one. Seen as delays in the walks: `sd.f2439`
(274/28), `div.other_boxes` (272/7) and `sd.distributions` (272/4) beneath `div.any` (272/1); `sales.route` (274/11)
beneath `sd.route_each` (274/2); `scope.f8978` (295/6) beneath `scope.business_before` (295/3). The full tables are
in `order_merged.md` ("What the late questions waited on", "Delayed children for the sorting cause", "What the bank
states").

### 6. Still stale outside the draft check (named by the lanes; not looked at)

`ui/test_browser.mjs` (walks to `scope.other_line16` as "the long question" and to the tick-box group);
`tools/engines/generate_cases.py` and `tools/engines/compare.py` (state `sd.other_forms`, `f5695.part1_any`,
`f5695.part2_any`, one `sli.interest`); `engine/src/umbrella-what-if.ts` (names `sb.foreign_any`,
`scope.other_line16`); `engine/src/mutate.ts` (a pinned explanation names `scope.schedule1`);
`tools/year_ids.json`; `tools/coverage/*.json`; `interview/2025/gate_frequencies.yaml` (refers to lines that are
now derived, and has no entry for the new parents); `research/audits/credits-misc/specs/f5695_no_part2.json`;
`docs/provisional/lanes/l4a_work/coverage.py` and `l6b_work/coverage.py` no longer reproduce their row files; every
review log of a changed form (NORMS section 5).

### 7. Rows that want a later expected end

`retirement.ordinary_ira`, `dependents.parents_apart_no_release` (Part 1) and `sales.interest_election_asked`
(above).

## Next

1. The stitch, from the list above; item 1 (ten entries) and item 3's first request (two entries) are bank fields only.
2. After any bank change: `npm run build --silent`; `node engine/dist/main.js test-fixtures`;
   `python3 tools/draft/stale_ids.py`; the rows of the files touched
   (`interview-coverage --rows FILE > out.txt; python3 tools/draft/fix_rows.py out.txt`, reading what it prints and
   setting amounts and choices by hand); `draft-walk`; then `tools/draft_check.sh` whole (about 40 minutes
   here; the coverage rows are the long step).
