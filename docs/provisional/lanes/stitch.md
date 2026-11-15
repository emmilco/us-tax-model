# Lane notes: stitch (the order of asking and the tick-box groups on one base)

Branch `lane/stitch`, worktree `.claude/worktrees/provisional-stitch`, cut from `provisional/interview-graph` at
`3bd68051` (which holds `lane/order`). Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No
paid call was made and no model was called from code.

The task: merge `lane/ltick` (tick-box groups, built against the old rule that an order number is all block or none)
onto the base that has the order mechanism (`docs/provisional/lanes/order.md`), restate the group rules in terms of
the order contract, and find out whether the reach pass removes the wait the tick lane found behind `s3.credit_bond`
(`docs/provisional/lanes/tick.md`, part 9).

## 1. The merge, conflict by conflict

`git merge lane/ltick` conflicted in five files.

| File | Resolution |
|---|---|
| `engine/src/interview.ts` | Both. The built question and `Question` keep `at` (order lane) and gain `group`, `tick` (tick lane); `InterviewData` gains `groups`. One change of substance beyond the text: see 1.1 |
| `engine/src/build.ts` | Both. The imports of both lanes; the order lane's `at` computation (`blockPlaces`) and the tick lane's group rules and built groups stand one after the other. The all-or-none rule the order lane removed stays removed (the tick lane had not touched it) |
| `engine/src/main.ts` | Both imports (`interviewOrder`, `tickGroups`) |
| `tools/draft_check.sh` | Both self-tests (`interview-order --self-test`, `tick-groups --self-test`) |
| `reports/2025/interview_coverage.md` | Generated: regenerated with `interview-coverage --write` on the merged build |

### 1.1 The screen's members are worked out with the reach pass

`tickScreen` (`engine/src/interview.ts`) puts on the screen the members that are open and those that would be open
once the open ones are answered No. The tick lane worked the second part out with a plain evaluation. On the merged
base the interview's open questions are those of `neededInputs`, which adds what the reach pass finds for a question
that states a `seq`; and every member states one. A member that stands behind another member's No *and* behind an
unanswered refusal screen outside the group would be asked directly after the screen's answers (the reach pass opens
it), yet the plain evaluation would have left it off the screen. `tickScreen` now asks `neededInputs` in both places,
so the screen shows exactly the members the interview would otherwise ask next. `tick-groups --self-test` has a
constructed case for it (a member behind another member's No and behind a refusal screen whose question is outside
the group); with the plain evaluation put back, that case fails ("the member behind the screen is on the tick-box
screen"), and with `neededInputs` it passes. The proof group does not depend on it: its four members are all open
when the screen comes up.

### 1.2 The rule that a member has `seq`

`tickGroupProblems` (`engine/src/tick-groups.ts`) said "a member has no seq; a group lies in a block (every question
of its order number has seq)". The second half was the old block rule. The message now says what the rule is for;
the rule itself (each member states a `seq`) stays, and has a second reason on this base: a stated `seq` is what
opens a member past a refusal screen (order contract, 1.3 and 1.4).

### 1.3 One server test stated what the reach pass changes (a check's expectation was restated; in a commit of its own)

`engine/src/serve-check.ts` (the tick lane's tests of the screen) held, as the reason for the one-request route:
after `s3.farmland` Yes and `s3.kerosene` No sent one at a time, the ordinary route rejects `s3.repaid_income` No
("neither reachable nor a correction"), because farmland's Yes opened `s3.farmland_deferral` and the engine did not
reach `s3.repaid_income` until that was answered. On the merged base the first full `tools/draft_check.sh` failed
there and nowhere else: "one at a time, a later box of the same screen: expected 400, got 200".

Cause, checked: `s3.repaid_income` stands behind the gate `s3.farmland_deferral_if_sold` in the refusal list of
`s3.line14`; it states a `seq`; the reach pass reads past an unanswered gate. So it stays open, which is the order
contract (1.3: a refusal screen ahead of a question does not hold back a question that states a `seq`). The failure
is the same with this lane's change to `tickScreen` taken out (one run; `experiment_log.md`).

The two contracts cannot both hold in that assertion, and no engine behaviour satisfies both: either the reach pass
opens the question or the route rejects it. The assertion was therefore restated to what the merged engine does, and
this is the one place where this lane changed what a check expects. It is in a commit of its own so that it can be
read, or reverted, apart from the merge. Now: the four answers sent one at a time in the order shown are each
accepted, the log ends with the same four events the screen writes, no screen is offered and
`s3.farmland_deferral` is next. That a later box is rejected one at a time where members are read by one `choose`
chain is still tested, on the constructed form of `tick-groups --self-test` (unchanged). No expected value, expected
refusal, fixture, coverage row or baseline was edited.

## 2. The tick-box group rules as they now stand

This is what a lane must write; `docs/provisional/lanes/tick.md`, parts 2 to 4, and `interview/README.md`,
"Tick-box groups", say the same at more length.

**Changed since (lane `tickrule`): items 4 and 8 below are as the stitch lane left them, not as the build now reads
them.** Members' `seq` numbers may leave gaps; the build no longer says where a question a member opens must stand
(only that it is not a member of the same group), and the walk of `tick-groups` checks when it is asked; the bank
declares the group `rare_credits`. The rules a lane follows are in `docs/provisional/lanes/tick.md`, parts 2 and 3.

In `interview/2025/questions.yaml`:

1. Declare the group once in `bank.groups`: `{id, heading}`. The `id` is lower-case letters, digits and `_`,
   starting with a letter, and unique. The `heading` is one line of at most 25 words, with no entry syntax and the
   spouse phrase in its exact form if it names the spouse.
2. On each member: `group: <id>` and `tick: <label>`. The label is required, one line, at most 12 words, does not
   end in `?`, has no entry syntax, and differs from the other members' labels. The member keeps its `prompt` and
   `help` unchanged.
3. Two to six members, each a yes or no input (no amount, number, choice or list question).
4. **Place.** All members have the same `order` (their topic's). Each member states a `seq`. The members' `seq`
   numbers follow one another with no gap (40, 41, 42), in the order of the boxes. No other question of that order
   number has a `seq` among them (with consecutive numbers that would be a duplicate, which the build refuses in any
   case).
5. **Not required any more:** an order number of the group's own, or a `seq` on the other questions of the order
   number. A question of the same order number that states no `seq` is asked after those that do.
6. The members are inputs of one form, or all of forms asked once per return (a screen is asked of one entry).
7. On a group asked of each person, the heading and labels must be covered by the person-wording rule.
8. **Children.** A question that a member's Yes opens (its `gated_by` gate reads the member, directly or through
   yes/no lines) must have the group's `order` and a `seq` after the last member's, with no other question's `seq`
   between the group and it. A member is never a question another member's Yes opens.

The build refuses each breach of 1 to 8 by name. After the build, `node engine/dist/main.js tick-groups` checks each
group on the background return: shown whole; with each member in turn ticked, what it opens is asked before anything
already waiting; the same answers one at a time end the same way.

What decides whether the screen is whole, on the merged base:

- A member behind a refusal screen in its form is on the screen (every member states a `seq`, so the reach pass
  opens it).
- A member reached only after another member's No is on the screen (`tickScreen`'s probe).
- A member that truly waits on an answer outside the group is not: its gate's parent, its roster, an undecided
  `choose` guard, an unanswered operand of an `all` or `any` test, or a computed amount (order contract, 1.6). Take
  it out of the group or place the group after that answer.

What a group cannot settle, and a lane must check with the coverage rows: a member that refuses is told at the
screen only if the questions its form line lists before it are answered by then (part 3).

Decided and open to the coordinator: the members' `seq` numbers must be consecutive whole numbers, as the tick lane
had it. The alternative, "no other question's `seq` between the lowest and the highest member", would let a lane
keep gaps of ten inside a group. It was not taken: it would change a rule and its planted test for no gain in what
the page shows, and "40, 41, 42" is checkable by eye.

## 3. The wait behind `s3.credit_bond`, revisited with the reach pass

### 3.1 What was run

The commands walk the bank as built, and the question was about numbers the bank does not have yet. So the walks
were made by `docs/provisional/lanes/stitch_trial/trial.mjs`, which loads the built `full` interview, gives the
questions named in a placements file another `order` and `seq` **in memory**, and then calls the engine's own
functions: `backgroundOf` (the background return, walked in the interview's order), `tickGroupWalkProblems` (what
`tick-groups` runs) and `checkFiles` on `interview/2025/coverage/credits.yaml` (what `interview-coverage` runs). It
writes nothing. Run after a build:

```
node docs/provisional/lanes/stitch_trial/trial.mjs "$PWD" docs/provisional/lanes/stitch_trial/map.json --rows --ends
```

`--reorder` and `--split` change the Schedule 3 form in memory (3.4). The placements:

| File | What it places |
|---|---|
| `asis.json` | Nothing: the bank as committed (group at order 13; the other Schedule 3 questions at order 10, no `seq`) |
| `seq10.json` | The fifteen other Schedule 3 questions of order 10 given `seq` 1 to 15 where they are; the group still at 13 |
| `map.json` | The map's numbers: `s3.disability_retired` 118, `s3.adoption*` 126, `s3.mcc` 215, `s3.ev*` 225, `s3.foreign_any`, its children and `ftc.*` 279, the group (members 1 to 4, the two opened questions 5 and 6) and `s3.prior_*` 290, `s3.line10` 305, `s3.elderly_credit` 318. Every other question of the bank keeps today's number (0 to 316), so the Schedule 3 questions come late in the walk |
| `reverse.json` | The chain's order reversed, among the early topics: the group at order 1, `s3.prior_*` 3, `s3.foreign_any` and children 4, `s3.ev*` 5, `s3.disability_retired` 8, `s3.mcc` 11, `s3.adoption*` 14 |

### 3.2 What was seen

The background return is 82 questions in every trial. "Rows" are the 46 rows of `credits.yaml`.

| Trial | Where the background return is asked the Schedule 3 questions | Group | Rows failing |
|---|---|---|---|
| `asis` | group 64 to 67; then `s3.disability_retired` 68 and `s3.ev` 69, order 10 re-entered after 13 | whole | 0 |
| `seq10` | `s3.ev` 16, `s3.foreign_any` 17, `s3.prior_other_forms` 18, `s3.disability_retired` 29; group 66 to 69; no Schedule 3 question after a later order number | whole | 21 |
| `map` | 118 at 64, 126 at 65, 225 at 74, 279 at 75 and 76, the group 77 to 80, `s3.prior_other_forms` 81, 305 at 82: each in its place, none late | whole | 9 |
| `reverse` | group 6 to 9, `s3.prior_other_forms` 17, `s3.foreign_any` 18, `s3.ev` 19, `s3.adoption_any` 69: each in its place; `s3.disability_retired` (order 8) asked at 32, after order 10 had begun | whole | 22 |

The failing rows, by kind:

- **The refusal came on a background answer** (the row's filer answers Yes, the interview goes on, and the refusal
  shows when a later question is answered No): 19 of the 21 in `seq10` (16 on `s3.credit_bond`, 3 on `s3.farmland`);
  8 of the 9 in `map` (`credits.new_vehicle`, `credits.charger`, `credits.used_vehicle_dealer` and
  `credits.gap.vehicle_ordered_earlier` on `s3.credit_bond`; `credits.mcc` on `s3.prior_other_forms`;
  `credits.section960c`, `credits.section965` and `credits.virgin_islands` on `s3.farmland`); 17 of the 22 in
  `reverse` (16 on `s3.adoption_any`, `credits.repaid_income` on `s3.foreign_any`).
- **The row meets a question it does not answer, or gives an answer never asked**: the rest (2, 1 and 5). These are
  the ordinary consequence of numbering a topic (order contract, 1.4) and of where the trial put `ftc.carryover` and
  `ftc.taxes`; they are the numbering lane's to settle by row inputs.

In `map`, every row but one ends where it ends on the bank as committed (the same refusal gate, or complete): the
late rows are refused at the same gate, later. The one, `credits.gap.foreign_tax_carryover`, stops at a question the
row does not answer (`s3.section960c`): its refusal is listed on `ftc.credit` after `ftc.needs1116`, which waits for
`ftc.taxes`, numbered later in the trial.

On the tree as built (no trial), the project's commands:

- `node engine/dist/main.js interview-order --write /tmp/…` (37 walks: 11 whole-return fixtures, 12 generated
  returns, 14 minimal returns, by its default): `s3.disability_retired` waited on `s3.credit_bond` in 26 walks (order
  10 re-entered after 13); in the one walk with `s3.foreign_any` Yes its children were asked 21 questions after it,
  having waited on `s3.farmland`; in the one with `s3.prior_other_forms` Yes its children were asked 25 questions
  after it, having waited on `s3.ev`. None of these questions states a `seq`.
- `node engine/dist/main.js draft-walk --out /tmp/… --summary`: 12 personas, 0 problems; `01_single_w2` is 86
  questions on 83 screens, as the tick lane had it.
- `tick-groups` and `tick-groups --self-test`: in `tools/draft_check.sh` (part 5).

One more walk at the map's numbers (`stitch_trial/senior.mjs`): a filer of 65 or over whose dealer took the vehicle
credit answers `s3.ev_dealer` Yes at 225 and is refused, at `s3.ev_dealer_if_ev`, only when `s3.elderly_credit` is
answered at 318 (nine questions later on this bank); the same filer under 65 is refused when `s3.credit_bond` is
answered at 290.

### 3.3 What it shows, and what it does not

Seen (one background return, one bank, 46 rows; the trials are in memory, not built):

- **Asking.** With the reach pass, a Schedule 3 question that states a `seq` was asked at the order number it was
  given, before or after `s3.credit_bond`, in every trial. Questions that state none (`asis`) still wait behind it.
- **The group.** The four members were on one screen at order 13, at 290 and at order 1 (ahead of every other
  Schedule 3 question, where the tick lane had found `s3.repaid_income` left out without the reach pass).
- **The exception is a true wait.** `s3.disability_retired` is asked only when someone on the return is under 65
  (`s3.any_under65`, read in `forms/2025/s3.yaml`), so it waits for the age answers (`person.age65`, order 10
  today). The map puts it at 118, after the ages at 110: no conflict.
- **Telling.** A refusal is told only when the entries listed before it on its line are answered. Read in
  `forms/2025/s3.yaml`: `s3.line7` lists, in order, `s3.adoption_if_any`, `s3.adoption_us_if_earlier`,
  `s3.credit_bond`, `s3.elderly_credit_if_asked`, `s3.ev_dealer_if_ev`, `s3.ev_credit_if_bought`,
  `s3.ev_equipment_if_ev`, `s3.prior_amt_if_forms`, `s3.prior_forms_if_forms`, `s3.mcc_if_interest`; `s3.line14`
  lists `s3.farmland_deferral_if_sold`, `s3.section960c_if_foreign`, `s3.section965_if_foreign`,
  `s3.virgin_islands_if_foreign`, `s3.repaid_income`; `s3.line12` lists `s3.kerosene_credit_if_kerosene` alone. The
  late rows of 3.2 are exactly the pairs these lists predict.

Inferred, not walked:

- That the same holds for a filer who is not the background return (a couple, a filer with other topics open). The
  reach pass stops at an `all` or `any` test and at a `choose`; none stands between the targets and these three
  lists for the background return, and I did not look for a return where one does.
- That every refusal listed after `s3.elderly_credit_if_asked` (the fourth entry of `s3.line7`: vehicles, the
  earlier year's forms, the mortgage certificate) waits for `s3.elderly_credit` at 318 on a return with a person of
  65 or over. One such walk was made, for `s3.ev_dealer` (3.2); the others follow from the list.
- That `scope.ready`'s list and the chain `s3.other_credit` do not delay a Schedule 3 refusal: in 3.4 every one was
  told at once with those two untouched, on these 46 rows. The chain still decides when `f5695`, `f8863` and `s8812`
  tell their refusal on `s3.other_credit`; no row of `credits.yaml` ends there.

### 3.4 What still holds something back, and the least change

Nothing holds back the **asking** of a Schedule 3 question that states a `seq`, short of a true wait. What is held
back is the **telling** of a refusal, by the order of the entries of `s3.line7` and `s3.line14`. At the map's
numbers:

| Refusal | Asked at | Told at | Behind |
|---|---|---|---|
| `s3.ev_dealer_if_ev`, `s3.ev_credit_if_bought`, `s3.ev_equipment_if_ev` | 225 | 290 | `s3.credit_bond` (third entry of `s3.line7`) |
| `s3.mcc_if_interest` | 215 | 290 | every other entry of `s3.line7` (it is the last) |
| the same six, on a return with a person of 65 or over | 215 to 290 | 318 | `s3.elderly_credit` (fourth entry of `s3.line7`; one walk, 3.2) |
| `s3.section960c_if_foreign`, `s3.section965_if_foreign`, `s3.virgin_islands_if_foreign` | 279 | 290 | `s3.farmland` (first entry of `s3.line14`) |

Three ways to remove it, smallest first. Two were tried in memory (`trial.mjs --reorder`, `--split`); neither is in
the commit.

1. **The bank only.** Number the screens of one line in the line's order (order contract, 1.4). Not possible at the
   map's numbers: `s3.credit_bond` (290) is listed before the vehicle questions (225) and `s3.mcc` (215). Otherwise
   accept the late telling and give each late row the background answer it waits on (an input; the contract allows
   it). The cost is norm N11 for those filers.
2. **The form, for one known order: list the entries in the order of asking.** For the map's numbers, `s3.line7`
   becomes adoption, adoption (earlier year), mortgage certificate, the three vehicle entries, bond, the two
   earlier-year entries, elderly; `s3.line14` becomes the three foreign entries, farmland, repaid income. Four
   entries move and no line is added. Tried with `map.json --reorder`: 45 of 46 rows pass, every Schedule 3 refusal
   told on the row's own answer, every row's end unchanged but the one of 3.2 (which is `ftc.credit`'s list, not
   Schedule 3's). Not checked: the fixtures (a return on which two situations of one line hold would be refused
   on that line at another gate; the return's own refusal comes from `scope.ready`, whose list was not touched),
   `render --check`, and the walks of the bank as committed, where the unnumbered questions follow the lists.
3. **The form, for any order: each situation on a line of its own.** `s3.line7` and `s3.line14` become the sum of
   one helper line per entry, each zero behind its one refusal. A sum reads all its operands and a refusal among
   them is the sum's value (`engine/src/eval.ts`), so each situation is told as soon as its own question is
   answered, and the line is still zero. Tried with `map.json --split` (45 of 46, as above) and `reverse.json
   --split` (no refusal late; 14 rows then need an answer removed or added, because a refusal told earlier ends the
   walk before a question the row answers). Fifteen lines added to a form no lane owns, each needing a label and a
   citation, with the review debt of new lines.

Why neither form change was made here. The second depends on the final numbers, which lane 7b is setting tonight,
and on this branch's bank (Schedule 3 questions unnumbered) it would change the order of asking instead of mending
it. The third is not small. The brief allowed a change only if small, with every check passing and the rows shown to
end where they did; on this branch that can be shown for neither.

An engine change was considered and not tried: telling a refusal as soon as a later entry is Yes while an earlier
one is unanswered (order notes, part 6). It changes what an incomplete return reports and which gate is named when
two situations hold, and the other evaluators would have to follow.

### 3.5 The proof group's place

Left at the placeholder, order 13, `seq` 1 to 6, as the tick lane had it. On this bank the other Schedule 3
questions state no `seq`, so wherever the group goes, `s3.credit_bond` is asked there and the unnumbered questions
that `s3.line7` and `s3.line14` list after its members are asked after the group. At order 13 that is
`s3.disability_retired` and `s3.ev` for the background return, and the children of `s3.prior_other_forms` and of
`s3.foreign_any` for a filer who has them (3.2, `interview-order`), and all 46 rows pass. A place inside order 10 was not tried: it would need those questions numbered, which
is lane 7b's work tonight. Once they are numbered the group is whole wherever it was tried (order 1, 13, 290) and
holds nothing back.

For the coordinator, merging lane 7b: keep the six questions (`s3.farmland`, `s3.kerosene`, `s3.repaid_income`,
`s3.credit_bond`, then `s3.farmland_deferral`, `s3.kerosene_credit`) on one `order` with consecutive `seq`, the two
opened questions directly after the four members; then run `tick-groups` and the coverage rows. If lane 7b sends
`s3.kerosene*` to 225 and the others to 290, the group is split by topic and the build will say so ("different order
numbers"): either kerosene leaves the group or the map's placement of it changes.

## 4. What changed, by file (beyond the merge itself)

| Path | Change |
|---|---|
| `engine/src/interview.ts` | `tickScreen` asks `neededInputs` for what would be open (1.1); two comments no longer say "block" |
| `engine/src/tick-groups.ts` | The message for a member without `seq`, and the comment above the place rules (1.2). No rule added or removed |
| `engine/src/tick-groups-check.ts` | One constructed case added to `--self-test` (1.1). No existing case changed |
| `engine/src/serve-check.ts` | The `ticks-one-by-one` assertion restated (1.3), in its own commit |
| `interview/README.md` | "Blocks": the Schedule 3 paragraph rewritten to part 3's finding. "Tick-box groups": the place rules restated; what "open" means for the screen |
| `docs/provisional/lanes/tick.md` | Parts 2 to 4 restated on the order contract; part 9 gains "Revisited"; the requests restated |
| `docs/provisional/lanes/stitch.md`, `docs/provisional/lanes/stitch_trial/` | These notes; the trial script, its placements and the one extra walk |
| `experiment_log.md` | The entry for part 3 |
| `PROJECT_INDEX.md` | The tick-groups row no longer says "block" |
| `reports/2025/interview_coverage.md` | Regenerated |

Not touched: `forms/`, fixtures, `interview/2025/questions.yaml` beyond what `lane/ltick` brought, the coverage rows,
any check's expectations, `tools/interview_rules_baseline.json`. Review debt: none added by this lane (the tick
lane's is in its notes).

## 5. The check

`tools/draft_check.sh`, in full, three runs:

1. On the merge as resolved (with 1.1 and 1.2): stopped by hand after the build and the fixtures, to add the
   self-test case of 1.1.
2. With that case: red at one step, `test_serve`, the assertion of 1.3; every other step passed.
3. On the final tree (the tree of the second commit): green, all sixteen steps. Build OK; fixtures 1854 of 1854;
   interview-rules 0 problems (177 walks, 415 random traversals); coverage rows 0 problems; `tick-groups` passed (one
   group, shown whole, for `full` and `ny`); the person-wording report current; the spouse-wording and check
   self-tests; 694 command-line invocations; properties; `test-serve` 452 checks; the `draft-walk`,
   `interview-order` (692 checks) and `tick-groups` self-tests; twins; render.

The first commit (the merge) is therefore red at `test_serve` on its own, by the one assertion; the second commit
restates it. Not run: the page's browser test (`ui/test_browser.mjs`), which is not in the check; nothing under
`ui/` was changed by this lane.

Working log, for a successor:

1. Read the norms, the order contract and the tick notes; merged; resolved the five conflicts (part 1).
2. Built; wrote `stitch_trial/trial.mjs`; ran `asis`, `seq10`, `map`, `reverse` (3.2).
3. Read `forms/2025/s3.yaml` for the lists; added `--reorder` and `--split`; ran them with `map` and `reverse`.
4. `interview-order` and `draft-walk` on the built tree; the walk of `senior.mjs`.
5. The self-test case of 1.1, shown to fail without the change.
6. Full check: red at `test_serve`; cause checked (1.3); the assertion restated; full check green.

## 6. Found and not fixed; requests

- **Coordinator, with lane 7b's numbers in hand:** which of the three remedies of 3.4 the Schedule 3 refusals get.
  Rerun `stitch_trial/trial.mjs` with a placements file of lane 7b's numbers: `--rows` lists the late rows and the
  answer each waits on.
- **Lane 7b:** give every Schedule 3 question a `seq`. One left without is asked after the questions its line lists
  before it.
- **Lane 5a (`ftc`):** `ftc.credit` lists `ftc.needs1116` before `ftc.carryover_if_asked`, and `ftc.needs1116` reads
  `ftc.taxes`. If `ftc.carryover` is numbered before `ftc.taxes`, its refusal is told only when `ftc.taxes` is
  answered (seen in the `map` trial, where the trial's own numbers put it so).
- `tick-groups` checks the background return only, and does not look at when a member's refusal is told; the
  coverage rows do.
- The trials were made in memory on the built interview. They use the engine's own walking functions, but no bank
  with those numbers was built, so the build's own rules (duplicate `seq`, the group rules) were not exercised on
  them.
- On the tree as committed, `interview-order` lists 22 gated questions not placed directly after their parent and
  the late questions of the other topics; they are the rebuild lanes' and were not looked at.
