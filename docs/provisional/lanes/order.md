# Lane notes: the order of asking (norm N7; T-284)

Branch `lane/order`, worktree `.claude/worktrees/provisional-order`. Model `claude-fable-5-2`, class judgment, year
2025, jurisdiction us. No paid call was made and no model was called from code.

Section 1 is the contract for the rebuild lanes: read it if you only set bank fields. Sections 2 to 6 are the record:
what was measured, what was decided and why, what conflicts with a guarantee, and the working log a successor would
continue from.

## 1. The contract for the rebuild lanes

You place a question by two fields of its entry in `interview/2025/questions.yaml`. Nothing else decides the order.

### 1.1 The two fields

- **`order`: the topic's position.** A whole number. The interview asks the open question with the lowest `order`
  first, so a topic with a lower number is asked before a topic with a higher one. Give every question of your topic
  the same `order`, whatever form it belongs to. Use the number the coordinator's map gives your topic; two topics
  must not share a number (their questions would be one topic, sorted together by `seq`).
- **`seq`: the question's place within its topic.** A whole number from 1. Within one `order`, lower `seq` is asked
  first. Leave gaps (10, 20, 30) so a question can be added later. No two questions of one `order` may state the same
  `seq`. Give every question of your topic a `seq`.

Example:

```yaml
  - input: s3.foreign_any        # the plain parent
    order: 10
    seq: 10
  - input: s3.section960c        # its children, directly after it
    order: 10
    seq: 20
  - input: s3.section965
    order: 10
    seq: 30
```

A question that states no `seq` is asked after every question of its `order` that states one, in id order. That is
how today's bank still works while lanes are part-way; do not leave it so in a topic you have rebuilt.

### 1.2 Questions asked per person, per W-2, per entry

Number the questions of a topic as you would write an outline, in one run of numbers, whoever they are asked of:

```yaml
  - input: $w2          # "Which employers gave you a W-2?"   (asked of each person)
    order: 3
    seq: 10
  - input: w2.box1      # asked of each W-2
    order: 3
    seq: 20
  - input: w2.box2
    order: 3
    seq: 30
  - input: person.rrta  # asked of each person, after that person's W-2s
    order: 3
    seq: 40
```

The interview asks this as: for the first person, the roster, then the first W-2's questions through (20, 30), then
the second W-2's (20, 30), then `person.rrta`; then the same for the second person. The rule: a stretch of
consecutive `seq` numbers that all belong to one collection (here 20 to 30, the W-2 questions) is asked one entry at
a time, each entry through. A question of the enclosing level (the person) that you number in the middle of the
stretch cuts it in two: each half is asked entry by entry on its own. So keep an entry's questions consecutive unless
you mean that.

On a joint return, a topic's per-person questions are asked for one person through, then for the other. A question
of the whole return in the same topic is asked once, at its `seq`; numbered in the middle of the per-person stretch
it cuts that stretch in two in the same way (each person's first half, the question, each person's second half).
The ids above are real, the numbers an illustration.

### 1.3 Making a child follow its parent

1. Give the child the parent's `order` and the next `seq`. Several children of one parent: consecutive numbers after
   the parent. A grandchild: directly after its own parent, before the parent's next sibling.
2. The child must be reachable as soon as the parent is answered. It is when the child is asked only because of the
   parent's answer: the child is `gated_by` a gate line whose guard reads the parent (`interview/README.md`,
   "Question data"; `docs/2026-11-06_formal_gates_design.md`), or the child is an entry question of the roster the
   parent is. A refusal screen that stands ahead of the child in the form (an earlier entry of a line's `refuses`
   list, or a screen in front of an amount) does not hold back a child that states a `seq`: you need not reorder
   refusal entries. (A question without a `seq` still waits behind such a screen, as it always did.)
3. If the child still comes late, it is waiting on some other answer (section 1.6). Run the measurement
   (section 1.7): it names the answer.

### 1.4 Stating a `seq` makes the order yours: screens and coverage rows

Until a question states a `seq`, the form decides part of its order: a refusal screen is asked before whatever stands
behind it on the same line, because the question behind is not open until the screen is answered. Once the questions
of your topic state a `seq`, they are all open as soon as the return needs them, and only your numbers order them.
Two consequences:

- **Number each refusing screen where you want it told** (norm N11: at its topic, early). A screen you number after
  the amounts it guards is asked after them.
- **A coverage row may meet a question it used not to.** A row that ends in a refusal answers only the questions on
  the way to it. If your numbering puts another question of the topic before the refusing one, the row's walk now
  asks it and `interview-coverage` fails with "the walk asks ..., which the row does not answer". Add the answer that
  situation's filer gives (an input, never the expected end). If the refusal now shows on an answer the row does not
  give ("came on a background answer"), add that answer to the row too.

A refusal is still told only when the form's line can no longer come out otherwise: if the refusing question is
answered yes while a screen ahead of it on the same line is unanswered, the refusal shows when that screen is
answered. Number the screens of one line in the form's order if the refusal must show at once.

### 1.5 What the build and the checks refuse

The build (`npm run build --silent`) fails when:

- an `order` is not a whole number, or a `seq` is not a whole number of 1 or more;
- two questions of one `order` state the same `seq` (the message names both).

It no longer fails when only some questions of an `order` state a `seq`.

`tools/draft_check.sh` (interview-rules) fails when your placement makes the interview ask a question the finished
return does not read ("... is asked in bank order and unread by the complete return"), or leaves a question that can
be reached in one order of answering and not in the interview's own ("... is reachable before the answer that hides
it, and the walk in bank order never asks it"). The messages name the question and, the second, the answer that makes
it unneeded. The remedy is to place the question after that
answer (a higher `seq`, or a later topic), never to edit the check or its baseline
(`tools/interview_rules_baseline.json` stays empty).

### 1.6 What remains impossible

- **A question cannot be asked before the return is certain to need it.** Its `order` and `seq` say where it is asked
  among the questions that are open; they cannot open it. A question opens only after: the roster that lists its
  entry; the answer its gate reads (its parent); and any answer that decides whether the form it belongs to is used
  at all. If you place it before one of those, it is not asked early: it is asked the moment it opens, in the middle
  of whatever topic the interview has reached by then (the lowest open number always goes first). So place every
  question after everything it waits on.
- **A question that waits on a computed amount cannot sit in an early topic.** Some questions are needed only when
  an amount worked out from many answers falls one way: the qualified business income questions (`qbi.*`) are read
  only once taxable income before that deduction is known, which is after every income, adjustment and deduction
  question. Three remedies, in this order of preference: place the question (or its small group) in a later topic,
  after what it waits on; or change the form so that the question hangs on a plain parent instead (a model change:
  record it in your lane notes); or, only where the return reads the form's results whatever the answers are, ask for
  those results directly in `interview/2025/full.yaml` (`targets`), as the health savings account block does. A
  direct target that the return does not read in every case makes the interview ask, and possibly refuse on, questions
  the return would not have read: that changes results and is not allowed (norm N9); `tools/draft_check.sh` shows it
  as a changed refusal or an unread question.
- **Beneath a condition with several parts, a refusal screen still holds its questions back.** Where a form tests
  "A and B" or "A or B" and A is not yet answered, the questions that stand behind a refusal gate inside B wait for
  that gate's own question, as before. (Asking them earlier is what made questions go unread; section 4.) If the
  measurement shows a question of yours waiting on such a screen, place it after the screen's question.
- **Entries are asked in the order of their keys, not the order the filer listed them.** On a joint return the
  spouse's questions come before the taxpayer's (`spouse` sorts before `taxpayer`), as today. The bank cannot change
  that.
- **Within a stretch of entry questions you cannot go across entries** (box 1 of every W-2, then box 2 of every
  W-2). Each entry is asked through.

### 1.7 Checking your topic

After a build:

```
node engine/dist/main.js interview-order --write /tmp/order.md
```

walks the whole-return fixtures, generated returns and minimal returns in the interview's own order (about a
minute of processor time; no model) and writes a report. Read three things in it:

1. "What the bank states": your `order` number should show every question stating a `seq`, and none of your gated
   questions should be in the list "not placed directly after their parent".
2. "What the late questions waited on": none of your questions should be in the first column. If one is, the second
   column is the answer it waited on: place your question after it, or see section 1.6.
3. Under each walk, "order N re-entered" and "child of ..." lines that name your questions.

`--strict` makes the command exit 1 when any walk re-enters an order number or delays a child; `--returns FILE` walks
the cases of a fixture file of your own (the fixtures' form: `{cases: [{id, inputs}]}`).

## 2. What was measured on today's interview

The command: `node engine/dist/main.js interview-order` (`engine/src/interview-order.ts`; in `PROJECT_INDEX.md`). It
walks returns in the interview's own order, to completion or refusal, and records for every question asked its order
number, its form and the step at which it became reachable. The reports here were made with `--generated 40`: 11
whole-return fixtures (`fixtures/2025/returns.json`; 9 complete, 2 refused within 5 questions), 40 generated
returns (6 complete, 34 refused; 22 of the 40 ask 40 questions or more before they end) and 13 minimal returns (every
gate closed, then 12 walks each with one existence gate opened alone).

`order_before.md` is today's interview: today's bank, walked with `--no-reach`, which leaves out the reach pass of
section 3. Its 52 walks' sequences of (order number, form) are the same, line for line, as those of a report made on
the lane's base engine (`2e3878e3` with only the command added) before any change to the engine.

Per walk, means (totals in brackets):

| | whole-return fixtures (11) | generated returns (40) | minimal returns (13) |
|---|---|---|---|
| order numbers re-entered | 8.7 (96) | 5.0 (198) | 7.2 (93) |
| forms re-entered, sorting | 3.5 (39) | 2.2 (87) | 4.2 (54) |
| forms re-entered, late | 8.2 (90) | 4.7 (187) | 8.5 (110) |
| gated children not directly after their parent, sorting | 0.5 (6) | 0.3 (13) | 0.2 (3) |
| gated children not directly after their parent, late | 1.3 (14) | 0.7 (28) | 0.5 (7) |

Readings:

- **Every order-number re-entry is cause 2 (late reachability).** It could not be otherwise: the order number is the
  first thing the interview sorts by, so an order number is left and re-entered only when a question of a lower number
  becomes reachable part-way.
- **Cause 2 is the larger cause for forms too**: about two thirds of the form re-entries (387 of 567).
- **A late question almost never waited on its parent.** The report's table "What the late questions waited on" has 89
  distinct (question, answer waited on) pairs; in 83 the answer is not one the question's gate reads and not its
  roster. The question was held back in evaluation by a question of another matter (`$sales` waited on
  `sd.other_forms` in 31 walks, `sa.gifts` on `sa.unsupported` in 34, `w2.box4` on `person.rrta` in 23).
- **Cause 1 (sorting by id within an order number)** shows as the form re-entries for sorting (180) and as the gated
  children the bank does not place after their parent: 20 of the bank's gated questions (the report's "What the bank
  states" lists them; e.g. the three children of `s3.foreign_any`, with 8 questions between that the parent does not
  open).
- Not established: the fixtures answer no to most questions, and only 12 existence gates are plain yes/no inputs, so
  a filer with many yes answers is under-represented. The generated returns give the widest spread available without
  writing new returns.

## 3. The mechanism

Two changes, both needed, neither enough alone. `order_after.md` is today's bank under both. Its totals are those
of `order_before.md`, and 51 of the 52 walks whose runs the report lists (the fixtures, the generated returns and the every-gate-closed
return) have the same runs: the second change
applies only to a question that states a `seq`, and today only the health savings account block does. The one walk
that differs is in that block: `generated.18`, a refused return, is asked 32 health savings account questions before
its refusal, where it was asked 30 (the block's `seq` order now decides, where the form's order of refusal gates
did). `order_reach_all.md` (`--reach-all`) is today's bank with the second change applied
to every question, as if each stated a `seq` and nothing were renumbered: it shows what the change does, and is not
how the interview asks today's bank.

### 3.1 The bank states the whole order (cause 1)

`askOrder` (`engine/src/interview.ts`) now reads `order`, then `seq` for any question that states one, as an outline
(section 1.2; `interview/README.md`, "Blocks"). Before, `seq` was read only when every question of an order number
stated one, and it sorted by the outermost entry and then `seq`, which interleaves two W-2s of one person. The build
computes, for each question of a collection, the lowest `seq` of the run of entry questions it is in (`at`, in the
built question; `blockPlaces`), and refuses two questions of one order number with the same `seq`. It no longer
requires an order number to be all `seq` or none.

Today's bank is asked exactly as before under this change alone: its one block (order 9, health savings accounts)
sorts the same (a second account of one person would now be asked account by account rather than line by line), and
a question without `seq` sorts by id as before. Checked: the 52 walk sequences were identical before and after the
comparator changed, with the reach pass held fixed.

### 3.2 The reach pass (cause 2)

A question is asked only once it is reachable. The evaluation reads a line's refusal gates in order and stops at the
first unanswered one, so everything behind the gate (the later gates, and the line's own amount or roster) waited for
the gate's question, wherever the bank put it. That is not a true dependency: once the gate is answered no,
everything behind it is read; if it is answered yes, the return is refused.

While a return is incomplete, the interview now also runs a second evaluation, the reach pass (`inputsAhead` in
`engine/src/eval.ts`; `neededInputs` in `interview.ts`), which reads past an unanswered refusal gate. A question it
finds that states a `seq` is open at once, and the bank's order decides among the open questions. A question that
states no `seq` is left as it was, open only when the evaluation itself reaches it (section 4.3 says why). It differs from the evaluation in two places
only: past an unanswered gate it goes on to the later gates and the line's own expression (unless a later gate
already refuses); and in an `all`/`any` test it stops at the first unanswered operand (section 4 says why). Its
values are thrown away: every value, the status and the refusal come from the evaluation proper, which is unchanged
(`evaluate` without the option runs the same code as before). A complete or refused return's open questions are the
evaluation's own, so the completion check sees exactly what it saw.

Measured with today's bank and the pass applied to every question (`order_reach_all.md`), per walk:

| | whole-return fixtures (11) | generated returns (40) | minimal returns (13) |
|---|---|---|---|
| order numbers re-entered | 3.8 (42), was 8.7 | 3.1 (124), was 5.0 | 4.0 (52), was 7.2 |
| forms re-entered, sorting | 5.2 (57) | 3.7 (149) | 5.2 (68) |
| forms re-entered, late | 3.0 (33), was 8.2 | 2.4 (95), was 4.7 | 3.2 (42), was 8.5 |
| gated children not directly after their parent, sorting | 1.2 (13) | 0.9 (36) | 0.6 (8) |
| gated children not directly after their parent, late | 0.8 (9), was 1.3 | 0.4 (15), was 0.7 | 0.2 (3), was 0.5 |

The late causes fall by a little more than half; the sorting counts rise because a question that is open earlier is
then placed by the bank's (unchanged, id-sorted) order. That part is the lanes' to fix with `seq`. In this trial one
pair is worse: `sa.charity_limited` no longer follows its parent `sa.gifts` at once in 12 of the 64 walks (the parent,
order 5, is asked earlier; the child is order 10). Total delayed children: 71 before, 84 in the trial.

### 3.3 That the two together do what the contract says (a trial, not committed)

On a scratch copy of the bank (reverted; nothing of it is in the commit) the 22 W-2 questions and their roster were
given order 3 and consecutive `seq`, and `s3.foreign_any`, its three children and `ftc.carryover` consecutive `seq`
in order 10. Bank fields only. Seen:

- `s3.foreign_any = true alone`: the parent and its children asked together, no delayed child (before: three, with
  3 questions between, two of them late behind each other's refusal entries).
- `stage5.return.owed` (two W-2s): one run of 15 W-2 questions, the roster, then employer A's questions through,
  then employer B's (before: three separate runs in three order numbers). One walk with two W-2s; the self-test
  covers two people with two W-2s each.
- `interview-rules` on that bank: 0 problems.

That trial was built and run while the pass still applied to every question. Under the final rule (the pass for
questions that state a `seq`) it was repeated without a build, by giving the same numbers to the built questions in
memory and walking the same two returns: `stage5.return.owed` asked the roster, then employer A's seven questions,
then employer B's seven (steps 14 to 28); `s3.foreign_any = true alone` asked the parent, its three children and
`ftc.carryover` at steps 17 to 21, with no delayed child. `interview-rules` was not rerun on the scratch bank under
the final rule.

### 3.4 The options, and why

- **(a) Make every order number a block, every question a `seq`.** Taken, in a form that lets lanes do it one topic
  at a time (a `seq` is no longer all-or-none per order number) and that is right for nested entries (outline order).
  Alone it is not enough: at the base, every order-number re-entry and two thirds of the form re-entries are late
  reachability, which no sorting changes. A late question is asked the moment it opens, wherever it is numbered.
- **(b) An opened child inherits its parent's place.** Not taken. The bank can already state a child's place, and a
  second, implied source of order could contradict the stated one. It also does not address what was measured: of the
  71 delayed children at the base, 49 were late, not missorted; an inherited place does not make a question
  reachable.
- **(c) Ask a topic's questions together before they are reachable.** Not taken as a general rule: it asks questions
  whose answers a return may never read, and an answer to an unreachable question is refused by the interview
  (`applyAnswer`). The reach pass is the part of (c) that is safe: it opens a question early only when the return is
  certain to need it short of a refusal. Direct targets (the health savings account device) remain available per form,
  on the condition in section 1.6.
- **(d) Reorder the refusal entries in the forms.** Not taken as the mechanism. It cannot put a line's own amount or
  roster ahead of the screen on that line (13 input lines and many sums stand behind a screen); the forms hold 310
  lines with refusal gates, 84 with more than one entry, 503 entries in all, so the bank's order and the forms' would
  have to be kept in step by hand, each form change carrying review debt; and with the reach pass the order of
  refusal entries no longer affects the order of asking, outside the case of section 4.

## 4. Conflicts with the guarantees

**4.1 Reading ahead everywhere asks questions a return does not read.** The first form of the reach pass read past
every unanswered refusal gate. It lowered order re-entries further (to 2.8, 2.7 and 2.0 per walk) and left no late
child. `interview-rules` then reported 10 problems: nine templates reachable before an answer that hides them and
never asked in bank order (`household.home_cost`, `household.unmarried`, `household.qss_eligible`, `household.rdp`,
`household.community_property`, `dependent.parent_home_paid`, `person.ira_basis_adjusted`, `sales.wash_loss`,
`ny_it201.ask.use_tax_st141`), and `household.home_cost` asked and unread on five New York fixtures. Read in
`forms/2025/household.yaml`: `household.hoh_fails` is `all: [f1040.status = hoh, household.hoh_eligible = false]`. An
`all`/`any` test evaluates the operands after an unanswered one, and the refusal gates of `household.hoh_eligible` had
been keeping that line's own questions back until the filing status was answered. Reading ahead beneath such an
operand asks them of every filer. The check was not edited and nothing was added to its baseline; the pass was
narrowed to stop at the first unanswered operand of an `all`/`any` test. With that, `interview-rules` reports 0
problems (177 walks, 415 random traversals). The cause was read for the household lines only; for the other
templates it is inferred from the same check passing after the narrowing.

The cost of the narrowing, from comparing the two trials' tables: 15 (question, waited on) pairs are late only
because of it, the most frequent `sa.gifts` waiting on `sa.elect_itemize` (34 walks), `person.blind` on `sa.dependent`
(31) and the dividend boxes `div.box3`, `div.box9`, `div.box10` on `div.box2c` or `div.box13` (6 and fewer). For
these the wanted order and the guarantee conflict as the forms stand: a lane places the question after the answer it
waits on, or rewrites the test in the form as nested `choose` lines so the dependency is explicit (a model change).

**4.2 Questions whose need depends on an answer of another topic.** 36 pairs stay late under either trial: the
question is behind a `choose` whose guard is not yet known, so the return does not know whether it will read it.
Asking it in its own topic would ask what may go unread. The frequent ones: `qbi.unsupported` and `qbi.carryforward`
(26 walks; read in `forms/2025/qbi.yaml`: `qbi.deduction` chooses on `qbi.use_8995a`, the test that taxable income
before the deduction exceeds the Form 8995 threshold, so the questions open only after the last question that amount
depends on); `$gift` after `sa.gifts` (12); `s3.mcc` after `sa.line8a` (11); `f1040.line3a` after
`sb.ordinary_dividends` (8); `dependent.gross_income` after `dependent.qr_all_year` (6). The full list is the table
in `order_reach_all.md` with "no" in its third column. Each is a decision for the lane that owns the question (section
1.6). Which of the 36 are a plain parent that is simply not written as a `gated_by` gate (and so only need placing
after it) and which wait on a computed amount was not gone through one by one.

**4.3 Without a stated order, the forms' order of refusal gates is the order, and the checks rely on it.** With the
pass applied to every question, `tools/draft_check.sh` failed in two steps (first run, 50 minutes on a loaded machine):

- `interview-coverage`, 4 of 79 rows. Three rows ending in a refusal met a question they do not answer, asked before
  the refusing one because it sorts first by id: `credits.employment_credit` (`sc.business_credit`),
  `credits.used_vehicle_dealer` (`s3.ev_bought`), `hsa.ira_transfer_at_the_1099r` (`retirement.box1`: the boxes of a
  Form 1099-R were asked before its screen `retirement.special`). One, `hsa.prior_year_excess`, got its refusal at
  `person.x_other` only when the background answered `s2.other`, a screen ahead of it on the same line. Also seen in
  the measurement: `stage5.refuse.screens` refused after 5 questions, was 4.
- `test-serve` crashed: its constructed form (`engine/src/serve-check.ts`, line 407) has a line whose expression is
  `{op: "copy", ref: ...}` (the field is `from`), behind a refusal gate. The evaluation never reads that expression
  while the gate is unanswered; the pass did. The check was not edited; the malformed line is still there.

So a refusal screen ahead of an amount is, today, how the interview asks the screen first, and rows and fixtures are
written to that. Rather than rewrite rows that belong to other lanes or let today's order get worse, the pass now
applies only to questions that state a `seq`: a lane that numbers a topic takes over its order, screens included
(section 1.4), and a topic nobody has numbered is asked exactly as before. With that, both steps pass and today's
walks are unchanged.

**4.4 Seven pairs wait on their parent or roster and are placed before it by today's bank** (`w2.box1`, `w2.box3`,
`w2.box5` in order 3 with their roster `$w2` in order 5; `gift.deduction`; `sa.charity_limited`; `ftc.carryover`).
No conflict: the bank places them after, and the trial in 3.3 shows it for the W-2s.

## 5. What changed, by file

- `engine/src/eval.ts`: `EvalOptions.ahead`, `inputsAhead`, `Derivation.awaits`; the two differences of the reach
  pass, in `evalLine` (refusal gates) and `evalTest` (`all`/`any`). `evaluate` without the option is unchanged.
- `engine/src/interview.ts`: `askOrder` (outline order), `entriesOf`, `placeOf`, `blockPlaces`; `neededInputs` (the
  evaluation's unknown inputs and, while incomplete and a line is held behind a gate, those of the reach pass whose
  question states a `seq`); `interviewStatus` takes `{ reach: "none" | "all" }` for the measurement only.
  `outerEntry` removed (unused).
- `engine/src/build.ts`: a duplicate `seq` in an order number is refused; all-or-none per order number is not; `at`
  is computed into the built questions. `schema/data.schema.json`: `at`.
- `engine/src/interview-rules.ts`: one line, `bankOrder` takes a question's place from `placeOf`, so the check walks
  in the interview's order as it did. No check, bound or baseline changed.
- `engine/src/interview-order.ts` (new), `engine/src/main.ts`: the measurement and its `--self-test` (692 checks:
  the outline order as a strict total order over a couple with two W-2s each, the places of entry runs, the reach
  pass on a small form). `tools/draft_check.sh`: runs that self-test.
- `interview/README.md` ("Blocks"), `PROJECT_INDEX.md`: brought up to date.
- `interview/2025/questions.yaml`, `forms/`, fixtures: not touched.

Review debt: none from this lane (no question, form line or expected value changed). The Lean evaluator and the
other engines evaluate without the reach pass, as `evaluate` does by default; they were not run here.

## 6. Found and not fixed; open points

- Cost. The reach pass is a second evaluation of each incomplete state that has a line held behind a gate. Run back
  to back, the measurement's default 36 walks took 30 seconds of processor time with `--no-reach` and 59 with the
  pass. The build and `interview-rules` walk many states and will be slower by some part of that factor; their times
  were not measured cleanly, because the other lanes' builds were loading the machine (load average above 40) for
  every run after the first. Not optimised; the pass could share the first evaluation's work.
- The health savings account block (order 9) already states `seq`, so the pass applies to it today. Of the 64
  returns measured one changed (`generated.18`, refused two questions later; section 3), and the block's 23 coverage
  rows pass. Which two questions, and whether the block's numbering should put the refusing one earlier, was not
  looked into: it is the health lane's numbering.
- `engine/src/serve-check.ts` line 407: the constructed line's expression is malformed (section 4.3). Not edited.
- Entries are asked in key order, so the spouse before the taxpayer (section 1.6). Asking in the roster's listed order
  would need the answers in `askOrder`.
- The measurement's parents are the yes/no inputs a `gated_by` gate reads. A child that hangs on a parent through a
  plain `choose` (not a `gated_by` gate), an enum or an amount is not counted as a child; it shows in the late table
  instead.
- A refusal that is certain is still told only when the evaluation reaches it: with one gate unanswered and a later
  gate already yes, the line stays unknown until the first is answered. Telling it at once (norm N11) would change
  what an incomplete return reports, so it was left.
- `order_before.md` and `order_after.md` are reports of this lane's base bank; the coordinator reruns the command on
  the merged interview.

## Working log

1. Read the norms, `interview/README.md`, T-284, `askOrder`, the interview-rules checks, `e70f95bb`. Wrote the
   measurement and ran it on the base engine.
2. Read `engine/src/eval.ts` for where evaluation stops on an unknown: refusal gates in order (`evalLine`), a
   `choose` at its first unanswered guard (`chooseUnresolved`, which forgets what it looked at beyond), a collection
   sum at its roster. The arithmetic operators read all operands.
3. Tried reading past every unanswered refusal gate. Order re-entries 2.8 / 2.7 / 2.0 per walk; `interview-rules`
   10 problems (section 4.1).
4. Narrowed: the reach pass as a second evaluation that stops at the first unanswered operand of an `all`/`any`
   test, used only while the return is incomplete. `interview-rules` 0 problems.
5. Generalised `askOrder` to the outline order; confirmed today's walks unchanged by it.
6. Scratch trial of the contract on the W-2 questions and the `s3.foreign_any` family (section 3.3); bank reverted.
7. Added `--no-reach` so the before report is made on any build; confirmed it reproduces the base engine's walks.
8. First full `tools/draft_check.sh`: red in `interview-coverage` (4 rows) and `test-serve` (section 4.3). Limited the
   pass to questions that state a `seq`; added `--reach-all` to keep the measurement of the pass on the whole bank.
9. Repeated the contract trial under the final rule (section 3.3). Second full `tools/draft_check.sh` on the final
   tree: green, every step (57 minutes on the loaded machine).
