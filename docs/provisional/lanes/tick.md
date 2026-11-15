# Lane notes: tick (a few yes or no questions on one screen of tick-boxes)

Branch `lane/ltick`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Task T-285. This lane changes no form, no fixture and no expected value. It adds a presentation
feature (bank, build, engine, server, page, `draft-walk`, the vetting page), and declares one group to prove it.

Parts 1 to 4 are written for an agent who has not read the engine and has groups to declare. Parts 5 to 9 are the
lane's own notes.

The lane was built before the order mechanism (`docs/provisional/lanes/order.md`). The stitch lane merged the two
(`docs/provisional/lanes/stitch.md`) and restated parts 2 to 4 in terms of the order contract: they say what holds on
the merged base. Parts 6 to 8 are the tick lane's record as it wrote it. Part 9 keeps its finding and says, under
"Revisited", what the reach pass changed.

Lane `tickrule` (branch `lane/tickrule`) then changed two rules, by the coordinator's decision, and parts 1 to 5 state
them as the build now reads them: the members' `seq` numbers may leave gaps (rule 7), and the build no longer says
where a question a member opens must stand (rule 10 keeps only that a member is never a question another member of
its group opens); when the opened questions are asked is left to the walk of `tick-groups` (part 3, "Children next").
The limits of two to six members, 12 words in a label and 25 in a heading are unchanged. The bank now declares one
group, `rare_credits` (`s3.credit_bond`, `s3.farmland`, `s3.repaid_income`, order 290), on which `test-serve` tests
the screen; so that no other question's `seq` lies among the members', `s3.repaid_income` and
`s3.farmland_deferral` exchanged `seq` 3 and 4. Parts 6 to 9 still speak
of the earlier proof group `rare_events`, which is not declared.

## 1. What a tick-box group is

A group is two to six yes or no questions, each a plain fact about the filer, that the page shows on one screen:

```
In 2025, did you do any of these?

[ ] Got a federal tax credit from a bond or a fund
[ ] Sold farmland
[ ] Paid back more than $3,000 of income from an earlier year

[ None of these ]   [ Continue ]
```

It is presentation only. Each member stays its own question in the bank, with its own input, prompt, help and
citation. Each is recorded in the answer log as its own answer (Yes if its box was ticked, No if not), is listed on
its own in the answered list, and is corrected on its own, as an ordinary yes or no question with its full prompt.
Nothing in `forms/` knows about groups, a fixture's answers do not change, and the command-line interview still asks
the members one at a time. A group needs no new input, no gate and no coverage row of its own.

## 2. How to declare a group

Everything is in `interview/2025/questions.yaml`. Two things: the group, once, in the list `groups` (it sits between
`frames` and `questions`); and four lines on each member's own entry.

```yaml
bank:
  tax_year: 2025
  frames:
    ...
  groups:
  - id: rare_credits
    heading: In 2025, did you (or, on a joint return, your spouse) do any of these?
  questions:
  ...
  - input: s3.credit_bond
    order: 290
    seq: 1
    group: rare_credits
    tick: Got a federal tax credit from a bond or a fund
    help: ...
    prompt: In 2025, did a bond you (or, on a joint return, your spouse) own, or a fund, give you a federal tax credit?
  - input: s3.farmland
    order: 290
    seq: 2
    group: rare_credits
    tick: Sold farmland
    help: Yes also if you traded it for other property.
    prompt: In 2025, did you (or, on a joint return, your spouse) sell farmland?
  ...
  - input: s3.repaid_income
    order: 290
    seq: 3
    group: rare_credits
    tick: Paid back more than $3,000 of income from an earlier year
    ...
  - input: s3.farmland_deferral        # the question a Yes to s3.farmland opens: not a member; same order number
    order: 290
    seq: 4
    help: ...
```

This is the one group the merged bank declares (`rare_credits`; the server test `test-serve` runs on it).

The fields:

| Field | Where | What it is |
|---|---|---|
| `groups[].id` | the group | A name of lower-case letters, digits and `_`, starting with a letter. Unique. Only the bank and the tools read it |
| `groups[].heading` | the group | The question the filer reads above the boxes. One line, at most 25 words. Written as a prompt is (see "Wording" below) |
| `group` | each member | The group's `id` |
| `tick` | each member | The words beside the member's box. Required. One line, at most 12 words, not ending in `?`, different from every other member's |
| `order` | each member | One order number for all the members: their topic's (the order contract, 1.1). The group needs no order number of its own |
| `seq` | each member | Required. The boxes are shown in `seq` order. The numbers may leave gaps (10, 20, 30); no other question of the order number may have a `seq` from the lowest member's to the highest's |

A member keeps its `prompt` and `help` exactly as they are. They are what the filer sees when the member is asked
alone, when it is corrected, in the answered list, on the command line, and behind "What this asks" beside its box.
Do not shorten a prompt because the label is short: the label is read with the heading, the prompt stands alone.

**Placing a group, under the order contract.** A group is placed exactly as its members are, by `order` and `seq`
(`docs/provisional/lanes/order.md`, part 1). What a lane must write:

1. Every member has the same `order`: the number of the topic the group belongs to. Other questions of that topic
   may share the number, before the group or after it, with a `seq` or without one (a question that states no `seq`
   is asked after every one that does).
2. Every member states a `seq`. The members' numbers need not follow one another (40, 41, 42 and 10, 20, 30 are both
   right), but no other question of that order number may state a `seq` that lies from the lowest member's to the
   highest's: nothing is asked among the members.
3. A question that a member's Yes opens is never a member of the same group (rule 10 of part 3). Where the other
   questions a member opens stand, the build does not say. Give them the group's `order` (or an earlier one): the
   walk of `tick-groups` fails when, with one box ticked, a question the answer opens is asked only after a question
   of an earlier order number that was already waiting (part 3, "Children next"). Within the order number they may
   stand anywhere after the members: directly after the group, after two or three groups shown one after another,
   or with other questions of the topic between.
4. Nothing else is needed. In particular no question of the topic has to gain a `seq` because the group has one,
   and the members need not come first in their form.

Stating a `seq` does a second thing for a member: it is then open as soon as the return is certain to need it,
whatever refusal screen stands ahead of it in its form (the reach pass; the order contract, 1.3 and 1.4). That is
what lets the four members of the proof group, which the form reads at different points of three refusal lists, be
on one screen wherever the group is placed (without it, placed ahead of the other Schedule 3 questions, the screen
lacked `s3.repaid_income`: part 9). It also means the order is yours: a member that refuses is told at the screen only if the questions its form
line lists before it are already answered (part 4, "A refusal").

**Wording.**

- The heading and the labels are reworded when shown exactly as a prompt is. Write the spouse phrase in its one exact
  form, "you (or, on a joint return, your spouse)" or "your (or, on a joint return, your spouse's)": a joint filer then
  reads "you or your spouse" and everyone else "you". Put it in the heading, so that the labels need not carry it.
- For a group asked of each person (its members are `person.*` inputs, or inputs of another list's form), write the
  heading without the frame, in the second person ("Were any of these true of you in 2025?"); the build puts the
  form's frame before it and the page shows "About you — …" or "About your spouse — Were any of these true of your
  spouse in 2025?". The labels are reworded for the person the same way ("You were blind" becomes "Your spouse was
  blind"), under the same rule as framed prompts (`interview/README.md`, "The person a question is about, as shown"),
  and the build names any word the rule does not cover.
- No entry syntax (the build refuses "true or false", "whole number", "cents" and the like in a heading or label, as
  it does in a prompt); no form number or line number alone (N6).

## 3. What the build refuses

`npm run build --silent` fails, naming the group or the question, on each of these (`tickGroupProblems` in
`engine/src/tick-groups.ts`; `node engine/dist/main.js tick-groups --self-test` plants every one):

1. `groups` that is not a list of `{id, heading}`; an `id` not of the form above; an `id` declared twice; any other key.
2. A heading that is empty, has a line break or leading or trailing space, has more than 25 words, states entry
   syntax, or holds a near-miss of the spouse phrase.
3. A group no question names. A question whose `group` names no declared group. A question with `tick` and no `group`.
4. A member that is not a yes or no input (an amount, a number, a choice from a list, or a list question `$…`).
5. A member without `tick`; a `tick` that is empty, has a line break, has more than 12 words, ends in `?`, states
   entry syntax, or holds a near-miss of the spouse phrase; two members of a group with the same `tick`.
6. Fewer than two members or more than six.
7. Members with different order numbers; a member without `seq`; another question of that order number whose `seq`
   lies from the lowest member's `seq` to the highest's. The members' own numbers may leave gaps. (Two questions of
   one order number with the same `seq` fail the build in any case. A question of the order number that states no
   `seq` is not a problem.)
8. Members of more than one form when any of those forms is a list's (a form asked per person, per employer, per
   account). A screen is asked of one entry, so its members are inputs of one form, or all of forms asked once per
   return.
9. On a group asked of each person, a heading or label whose "you", "your spouse" or "this person" the person rule
   does not cover.
10. **The children rule.** A member may never be a question that another member of its group opens (a group does
    not hold a parent and its child). The build reads this from the form data: a question is *opened by* a member
    when its input is gated (`gated_by`) and its gate's tests read the member's input, directly or through what
    other yes/no lines compute. A gate that only stands behind a derived refusal screen (a computed line some
    line refuses on) does not count: a Yes that refuses there opens nothing. That is the whole rule. The build does
    not refuse an opened question for where it stands (its order number, its `seq`, or what lies between the group
    and it); the walk below checks when it is asked. For clients that ask one question at a time (the command
    line, and the page when a member is answered on its own), a child comes after the remaining members, not
    directly after its parent.

After the build, `node engine/dist/main.js tick-groups` (it is in `tools/draft_check.sh`) checks each group of the
built interview on the background return, the filer with nothing to report:

- **Shown together.** When the group's first member is the next question, the screen has every member. If it does
  not, the command fails and names the members left out. See part 4, "Members the screen leaves out".
- **Children next, as it happens.** With each member in turn ticked and the others not: every question the answers
  open (one that was not waiting before and is now) is asked before any question that was already waiting and has
  an earlier order number than the opened question's own. So what a ticked box opens is asked while the interview
  is still in the topic it belongs to, not behind a topic the filer was already due to reach. Questions of the
  opened question's own order number that were already waiting (other groups, other questions of the topic) may be
  asked before it, in `seq` order, and anything of a later order number or later `seq` follows freely. What this
  does not look at: a ticked member that refuses the return (nothing is asked next); two or more boxes ticked
  together; a question that opens only after a further answer (a grandchild, an amount's follow-up, a list's
  entries); and any return but the background one.
- **Same end one at a time.** The same answers given one question at a time, as the command line asks them, end the
  return the same way (the same status and, if refused, the same gate).

A group the background return never meets (all its members lie behind an answer that filer does not give) is
reported as not checked. Check such a group with a persona that reaches it (`draft-walk`, below).

## 4. What the page does, and what follows for you

When the next question is a member of a group, the page shows the group's heading, a box for each member with its
label and its id, and two buttons. **None of these** records No for every box. Ticking one or more boxes and choosing
**Continue** records Yes for the ticked and No for the rest. Only one of the two is live at a time (Continue is
disabled until a box is ticked; None of these is disabled while one is), so a filer cannot tick a box and then
discard it by mistake. Beside each box, "What this asks" opens the member's full prompt, its help and its source, and
"Answer this one on its own" shows it as an ordinary question, which is also where "I don't know / need help" is.

The answers are saved together or not at all. The page then asks whatever is next: the questions the ticked members
opened (part 3, "Children next"), other questions of the topic, or the next topic.

What is on the screen:

- **Members answered earlier are not shown.** If only one member is still open, there is no screen: it is asked as an
  ordinary question with its full prompt. So every member's prompt must still read well alone.
- **Members asked of each person** get one screen per person, under "About you" and "About your spouse".
- **A refusal.** If a ticked member's Yes refuses the return, the refusal is shown exactly as it is for that question
  today (the status line, the details, the refusal's note). All the screen's answers are saved with it. As for any
  question, the refusal is told at once only if the questions that the member's form line lists before it are
  answered by then (the order contract, 1.4): a member numbered before such a question is ticked, the interview goes
  on, and the refusal shows when that question is answered. `tick-groups` does not look for this; the coverage rows
  do ("the refusal … came on a background answer").
- **Members the screen leaves out.** The engine only asks for an input when the return's figures need it. Three
  cases:
  - A member that stands behind a refusal screen in its form (an earlier entry of a line's refusal list, or a screen
    in front of an amount) **is shown**: every member states a `seq`, and the reach pass opens such a question as soon
    as the return needs it. You need do nothing.
  - A member the engine reaches only after *another member* is answered No (the two are read by one `choose` chain
    of tests in the form) **is shown**: the page works out which members would be asked once the open ones are
    answered No, and puts them on the screen. You need do nothing.
  - A member that truly waits on an answer *outside the group* is not shown with the others and is asked later,
    alone: it is gated (its parent is not yet answered Yes), its roster is not yet answered, it lies behind a
    `choose` whose guard is not yet decided or behind an unanswered operand of an `all` or `any` test, or its form is
    read only once a computed amount is known (the order contract, 1.6). `tick-groups` fails on this for the
    background return. The remedies, in order: take the member out of the group; or move the group to after the
    answer it waits on (`node engine/dist/main.js interview-order` names that answer); or, only where the return
    reads the form's results whatever the answers are, a target in `interview/2025/full.yaml`, on the condition of
    the order contract, 1.6 (lanes do not edit that file; ask the coordinator).
- **A group does not hold back a question that states a `seq`.** Where a form reads several questions from one
  refusal list, a question that states no `seq` waits for every question listed before it, so a member asked later
  than before delays the unnumbered questions listed after it (the proof group does this today: part 9). A question
  that states a `seq` is not delayed. So number the questions that the members' form lists after them, or check with
  `draft-walk` where they are now asked.

**To see a group as a filer does:** `node engine/dist/main.js draft-walk --out /tmp/walks` and read a transcript. A
screen is one numbered step, printed with its heading, its labels and the boxes ticked; the summary's "Steps" column
counts screens beside "Questions". To see it in the page, run `serve` (`interview/README.md`, "Web UI").

**Fixtures and personas do not change** when questions are put in a group: answers are keyed by question id, and the
ids do not change. A coverage row can change in one way, and only if the members moved: stating a `seq` makes the
order of the topic yours (the order contract, 1.4), so a row that ends in a refusal may now meet a question it did not
answer, or get its refusal on a background answer. Add the answer that situation's filer gives; never the expected
end.

## 5. A good group and a bad one

The standard is the least mental effort to answer correctly. A group earns its place when a person can run an eye
down it and say "none of these" in one step, and be right.

A good group:

- **Each member is a plain fact** a person knows about their own year without looking anything up (cost 1 on the
  owner's scale). "Sold farmland." "Got divorced." If a member needs its help to be answered, it is not a tick-box.
- **"None of these" is the typical answer, by a wide margin.** The screen is an off-ramp: one glance, one click. A
  member most people tick belongs in a question of its own, asked plainly.
- **Few members: three to five.** Six is the limit the build allows, not the target. Every added label is read by
  everyone.
- **One kind of thing**, so the heading can be one honest question: things that happened to you this year, kinds of
  paper you received, things true of your home. The filer should be able to guess what a fifth item would look like.
- **Labels are parallel and short**: the same grammatical form, each completing the heading, the distinguishing word
  early ("Sold farmland", not "In 2025 there was a sale by you of land used for farming").
- **Flat.** Members open nothing, or a short block of questions asked in the same topic after the screen (part 3,
  "Children next").

A bad group, each of which is the catch-all again in another form:

- **A mixed list.** Unrelated items under "Did you have any of the following?": the filer must read and judge each
  item separately, and the unrelated ones unsettle the context (the owner's veteran example, cost 1 to 15).
- **Tax vocabulary in a label** ("Section 965 installment", "Form 8912 credit"). A filer who does not know the term
  cannot say "none of these" and be right. Such an item keeps a question of its own with a gloss, or goes beneath a
  plain parent.
- **A parent and its child together**, or a member only some filers should be asked. A group is not a substitute for
  layering (N2): if a plain parent's No spares the filer the list, use the parent.
- **A member whose Yes opens a long branch.** Two such members ticked together send the filer down two branches in
  succession with the screen far behind. Ask such a question on its own, with its children beneath it.
- **A long label standing in for a long prompt.** If the fact cannot be said in a dozen plain words, it is two
  questions or it needs a parent (N10: do not move the length somewhere else).
- **A group to hide a count.** Six boxes are cheaper than six screens only if each box is as cheap as a glance.
  Ten rare facts are two or three groups by kind, or better, facts moved to where their subjects live (N5).

When in doubt, the test is the owner's: would a person with none of these pass the screen in one step, and would a
person with one of them find it at once?

## 6. What was built (by file)

| Path | Change |
|---|---|
| `interview/2025/questions.yaml` | `groups` with one group, `rare_events`; its four members and the two questions they open moved from order 10 to a block of their own, order 13 |
| `engine/src/tick-groups.ts` | new: the declaration rules (`tickGroupProblems`), and which inputs a member's Yes opens (`opensMap`) |
| `engine/src/tick-groups-check.ts` | new: the command `tick-groups` (the three checks on the background return) and its `--self-test` |
| `engine/src/build.ts` | reads `groups`, `group`, `tick`; runs the rules; writes `groups` and each member's `group` and `tick` into the built interviews |
| `schema/data.schema.json` | `groups` on an interview; `group` and `tick` on a question |
| `engine/src/interview.ts` | `interviewView` returns `group`, the screen for the first pending question (`tickScreen`); `applyAnswers`, the screen's answers checked together; `entryPath` |
| `engine/src/spouse-wording.ts` | `shownLabel`: a label reworded as its question is |
| `engine/src/serve.ts` | the state's `group`; `POST /api/returns/:name/answers` |
| `ui/app.ts`, `ui/style.css` | the tick-box screen (`renderGroup`) |
| `engine/src/draft-walk.ts` | a screen is one step; the transcript, totals and summary; self-test |
| `engine/src/vetting.ts`, `ui/vet.ts`, `ui/vet.css` | a member's card shows "Shown as": its group, the heading and its label |
| `engine/src/serve-check.ts` | the server's tests of the screen (part 8) |
| `ui/test_browser.mjs` | the smoke test answers a tick-box screen it meets and checks it; `CHROME_PORT` |
| `engine/src/main.ts`, `tools/draft_check.sh` | the command; `tick-groups --self-test` and `tick-groups` in the check |
| `interview/README.md` | "Web UI", the API table, "The answer log", "Tick-box groups" (new), the vetting card, "What a given filer is asked" |

## 7. Decisions, and what was decided against

1. **One route that records the screen's answers together** (`POST …/answers`, `applyAnswers`), not the page calling
   the existing route once per member. Measured on the proof group, on a whole return (fixture `stage5.return.owed`):
   with farmland ticked, the answers sent one at a time in the order shown are farmland Yes (written), kerosene No
   (written), then `s3.repaid_income` No, which the existing route rejects ("neither reachable nor a correction"),
   because farmland's Yes opened `s3.farmland_deferral` and the engine does not reach `s3.repaid_income` until that
   is answered. The screen would be left half written. The screen's answers are therefore checked against the state
   before any of them and appended in one write. The server test holds both halves (returns `ticks-one-by-one` and
   `ticks-some`).
   *On the merged base (stitch lane):* the measurement above no longer holds for this group. Its members state a
   `seq`, so the reach pass keeps `s3.repaid_income` open after farmland's Yes, and the four answers sent one at a
   time are all written. The reason for one route stands where members are read by one `choose` chain of tests
   (`tick-groups --self-test`, the constructed chain: a later box is rejected one at a time), and one write still
   leaves no half-answered screen. The server test `ticks-one-by-one` was restated accordingly
   (`docs/provisional/lanes/stitch.md`, 1.3).
2. **The request must answer exactly the boxes of the screen offered now**, each yes or no. Not "any open members":
   an exact rule leaves no partly answered screen, and a stale page (the state changed elsewhere) gets a 400 and
   writes nothing.
3. **The screen includes a member reached only after another member's No** (a departure from the brief's "members not
   yet reachable are not shown", on evidence). On this branch, when the group comes up, `s3.repaid_income` is not
   reachable until `s3.farmland` and `s3.kerosene` are answered, because the form tests them in order. Showing
   three boxes and then the fourth as a lone question would defeat the group. Instead the engine asks which members
   would be open once the open ones are answered No, and shows those too. With none ticked this records exactly
   what one question at a time records (tested). With one ticked it can record a No for a member the engine has not
   reached yet (`s3.repaid_income` when farmland is ticked, until the question farmland opens is answered); that
   answer is read by nothing until the member is reached, and then it is the answer the filer gave. Cost: one or two extra evaluations, only when a group is next and a member is not open.
   Members waiting on an answer outside the group are still not shown.
4. **`tick` is required**, where the brief had it optional. A prompt is a full question and a label is read under a
   heading; a fallback to the prompt would put questions under a question, and two of the four prompts here are over
   a dozen words. One rule (every member has a label, at most 12 words) is easier to follow exactly.
5. **A label does not end in `?`** and the heading carries the spouse phrase, so labels stay short and a joint filer
   is still asked about both people.
6. **The children rule is static and narrow, with a dynamic check behind it.** "Opened by" follows a gate's tests
   through yes/no lines only. Following every line was tried on the built data and rejected: some gates are figured
   from amounts that depend on hundreds of answers (`household.credit_disallowed` reads 297 questions that way), which
   would have named unrelated questions as children. What the static rule cannot see, `tick-groups` checks on the
   background return.
7. **No batch of help requests.** A screen's answers are yes or no. A filer who cannot answer one box opens it on its
   own, where "I don't know / need help" is. A member with help requested stays open, so it stays on the screen.
8. **The answer log is unchanged in form.** It does not record that answers shared a screen. One consequence: the
   state returned by the answering request lists the lines changed by the whole screen, while a reload of the page
   lists those changed by the last event only (the last box). Not fixed: fixing it would mean marking events in the
   log.
9. **The vetting digest does not cover the group.** A verdict stays tied to the question's own prompt, help and
   answers, so declaring a group makes no record stale. The card shows the heading and label for information.
10. **Order 13 for the proof group** is a number no question used and no lane owns. It is a placeholder: the map
    sends `s3.kerosene*` to 225 to 229 and the other three to 290 to 294 (lane 7b), which would split this group by
    topic. Where it goes, and whether kerosene stays in it, is the coordinator's call. The group no longer needs a
    number of its own (part 2); the placeholder was kept by the stitch lane because lane 7b is setting the final
    numbers. Moving `s3.credit_bond` later has a cost, which is the state of this branch: see part 9.
11. **Heading of the proof group.** "In 2025, did you (or, on a joint return, your spouse) do any of these?" with
    labels in the past tense. "Did any of these happen in 2025?" was the brief's example; it was not used because the
    labels would then each need a subject, and on a joint return the spouse's sale or repayment counts, so the couple
    has to be named once, in the heading.

## 8. What was run and seen, and what is inferred

Ran and saw (this worktree, built data):

- `npm run build --silent` with the group declared: build OK. The built `full`, `ny` and social security interviews
  each carry the group and the four members' `group` and `tick`.
- `tick-groups`: for `full` and `ny`, 1 group, shown whole on the background return, 0 problems (so: all four boxes
  on one screen; with each member in turn ticked, what it opens is asked before anything already waiting; the same
  answers one at a time end the same way). `tick-groups --self-test`: passed (33 planted declarations; a constructed
  chain of tests, where a screen shows the members reached through the others' No and not one waiting on an answer
  outside the group, and takes together answers that one at a time are cut short; and a group
  planted on `person.rrta` and `person.age65` of the built interview for a couple: the spouse's screen under "About
  your spouse" with the heading and labels reworded, a box of the other person refused, then the filer's screen,
  then one member left open asked as an ordinary question).
- What each member's Yes does, on the built data: `s3.farmland` opens `s3.farmland_deferral`; `s3.kerosene` opens
  `s3.kerosene_credit`; `s3.credit_bond` refuses (gate `s3.credit_bond`, Form 8912); `s3.repaid_income` refuses
  (gate `s3.repaid_income`). So two members test the children rule and two the refusal.
- Reachability, on the whole return `stage5.return.owed`: when the group comes up, `s3.farmland`, `s3.kerosene` and
  `s3.credit_bond` are pending and `s3.repaid_income` is not; with farmland and kerosene answered No it is. The
  screen shows all four (decision 3), there and on the background return.
- `test-serve`: 452 checks passed, with the fixture walks. The screen's tests, each on a whole federal return written
  as a log without the group's answers: the screen served (heading reworded for the filing status, four boxes with
  labels, each box's own question, help, source and type; the command line's state names the same screen); nine
  rejected requests, each a 400 that leaves the log byte for byte as it was (a box left out, a question outside the
  group, an undeclared input, a box twice, a help request, an answer as text, a body that is no list, items that are
  not `{input, value}`, a screen when none is offered) and a 404; some ticked (four events appended in order, the
  opened question asked next, each member its own row of the answered list, then one member corrected on its own and
  another corrected to Yes); none ticked (four No, nothing opened, the fixture's expected values); a refusing member
  (the same refusal, note, conflicts and finality as the same answers one at a time; then corrected, which clears
  it); a member answered earlier (three boxes; a request naming the answered member refused); a member with help
  requested (still a box); one member open (no screen, the full prompt); the heading on a joint return; a member's
  vetting card; and the half-written screen of decision 1.
- `draft-walk --self-test`: passed; the plain walk is 82 questions on 79 screens, one of them a tick-box screen.
  `draft-walk --out /tmp/…` over the twelve personas: 0 problems, no persona changed. Against the baseline
  (`docs/provisional/walks/before/SUMMARY.md`), `01_single_w2`: questions 86 and 86, screens 86 and 83, prompt words
  6,777 and 6,764 (the four members' prompts are 54 words in all for this filer; the heading and labels are 41),
  topic switches 43 and 44 (the group and its two children left the run of `s3` questions at order 10 for order 13).
  Every completing persona: three screens fewer, 13 prompt words fewer (19 for the two couples), the same questions. I did not write
  `docs/provisional/walks/after/`: those files are for the merged redraft.
- The page, in headless Chrome 157 (`CHROME_PORT=9341 node ui/test_browser.mjs`, which passed to its end): the smoke
  walk met the screen after 84 answers. Checked there: the heading word for word; one box per member with label and
  id; nothing ticked, so only "None of these" live; a box ticked, so only "Continue with 1 ticked" live; "What this
  asks" showing the member's own prompt word for word, its help and source; "Answer this one on its own" giving an
  ordinary Yes/No question with help and source, and "Back to the next question" returning; nothing written until
  the screen is answered; then four events written in order; the "Saved: None of these for …" line; each member its
  own row of the answered list under its own prompt; a member reopened alone for correction. Two screenshots were
  read: `/private/tmp/tax-ui-design-ticks.png` and `…-ticks-open.png`.
- `tools/draft_check.sh`, in full, on the tree of the first commit (`a53eadc1`): green, all sixteen steps (build; fixtures 1854/1854;
  interview-rules 0 problems; coverage rows 0 problems; tick-groups; the person-wording report current; the
  spouse-wording and check self-tests; 696 command-line invocations; properties; test-serve 453 checks; the
  draft-walk and tick-groups self-tests; twins; render). No fixture, coverage row or persona changed; the coverage
  report was regenerated (its paths show the new order). Run in full again on
  the tree of the second commit (the constructed self-test and these notes added): green, the same sixteen steps.
  Between the two, one full run with the target `s3.other_credit_4` added failed at the coverage rows (part 9).

Inferred, not checked:

- That a ticked screen behaves in the page as it does through the server for the cases the browser walk did not
  drive: the walk answered the screen with "None of these" (its fixture answers every member No). "Continue" with a
  box ticked was driven only as far as the button becoming live; the request it sends is the one the server tests
  cover. A refusal after a ticked box, the per-person frame above a screen, and a screen with a help-requested member
  were not looked at in a browser.
- The narrow-window layout of the screen (no screenshot was taken at a narrow width), keyboard use and a screen
  reader. The boxes are native checkboxes, each with a `label`, in a group named by the heading.
- The vetting page's "Shown as" row in a browser: the server test covers the card's data (`tick` on four cards, the
  digest unchanged); the row itself was not looked at.
- That the static children rule's reading of gates ("through yes/no lines only") names the right questions for other
  lanes' groups. It was checked on these four members only; `tick-groups` is the backstop.
- That groups survive the other lanes' changes to order numbers. Lane 7b moves these six questions; the merge will
  conflict on their `order` lines, and whoever resolves it must keep the six in one block (part 2).

## 9. Not done, and found

### Revisited on the merged base (stitch lane; the evidence is in `docs/provisional/lanes/stitch.md`, part 3)

The finding below was made without the reach pass. With it, on the merged base:

- **Consequence 1 holds only for questions that state no `seq`.** On the branch as committed, the background return
  is still asked `s3.disability_retired` and `s3.ev` after the group (68 and 69, the group at 64 to 67): they state
  no `seq`. With the Schedule 3 questions given a `seq` (in memory), the background return was asked each at the
  order number it was given, at the map's numbers and with the chain's order reversed, and the group was shown whole
  in both. The one exception is a true wait: `s3.disability_retired`, numbered before the age questions in the
  reversed trial, was asked when they were answered.
- **Consequence 3 no longer holds.** With the six questions at order 1, before every other Schedule 3 question, the
  screen had all four members.
- **Consequence 2's cause is narrower than was written.** The refusals wait on the refusal lists of `s3.line7` and
  `s3.line14`, not on the list of `scope.ready` or the chain `s3.other_credit`: with only those two lists changed (in
  memory), every Schedule 3 refusal of the credits rows was told on the row's own answer.
- **What remains** is when a refusal is told, not when a question is asked: a question numbered before one that its
  line lists earlier has its refusal told late. At the map's numbers that is the vehicle questions and `s3.mcc`
  (behind `s3.credit_bond` and `s3.prior_other_forms`) and the children of `s3.foreign_any` (behind `s3.farmland`).

So the three choices at the end of this part are superseded: all four members can share a screen at any place after
what they truly wait on, and what the coordinator has to settle is the order of the refusal lists (stitch notes,
part 3).

### The chain behind `s3.credit_bond` (found without the reach pass; kept as the tick lane wrote it)

Schedule 3's unprepared credits are tested in order, in more than one place: the chain `s3.other_credit`,
`s3.other_credit_2` to `_16` (adoption, adoption in an earlier year, `s3.credit_bond` third, then thirteen more
situations: retired on disability and the credit for the elderly, vehicles, the farmland choice, foreign items, the
kerosene claim, the earlier year's forms; `s3.repaid_income` sixteenth; then the mortgage certificate), and the
refusal list of `scope.ready`, in nearly the same order. The engine goes through such a chain or list in order and
stops at the first test it cannot yet decide (`engine/src/eval.ts`, the loop over a line's `refuses`; a `choose`
likewise). So a question is reached only when the tests before it are decided, and a refusal is told only when the
ones before it in its list are. What follows was measured, not derived:

1. **A question of this chain asked later than today holds back every s3 question behind it**, whatever their order
   numbers. With the group (and so `s3.credit_bond`) at order 13 and nothing else changed, the background return is
   asked `s3.disability_retired` and `s3.ev` as questions 73 and 74, after the group (69 to 72), where they had been 46 and 47;
   and the children of `s3.prior_other_forms` (`s3.prior_amt`, `s3.prior_forms`) come 27 questions after their
   parent, where they had followed it at once (`reports/2025/interview_coverage.md`, the paths of
   `credits.business_credit_carried` and its neighbours, regenerated in this lane's first commit). **This is the
   state of this branch.** Every check passes with it; the cost is this order.
2. **A target does not mend it.** I added `s3.other_credit_4` (the chain from its fourth link on) to the targets of
   `interview/2025/full.yaml`, as the health savings account block does for its form. In memory and built, the
   questions went back before the group (45 and 46, the group whole at 71 to 74). But `tools/draft_check.sh` then
   failed: 16 coverage rows of `interview/2025/coverage/credits.yaml` (`credits.new_vehicle`, `credits.mcc`,
   `credits.elderly_65` and others), each because the refusal now "came on a background answer (… `s3.credit_bond` =
   false)": the vehicle question was asked in place, but its refusal was not told until the bond question was
   answered, thirty questions later (N11). The target was taken out again; it is in no commit.

3. **Asked early, the group is not whole.** Tried in memory with the six questions at order 7, before the other s3
   questions: the screen has `s3.farmland`, `s3.kerosene` and `s3.credit_bond` (questions 15 to 17 of the
   background return), and `s3.repaid_income` is asked alone at 51, after `s3.disability_retired`, `s3.ev` and
   `s3.foreign_any`; `tick-groups` fails on it ("not on it … waiting on an answer outside the group").

So these four cannot share a screen for free: `s3.credit_bond` has to be answered before the situations behind it,
and `s3.repaid_income` is reached only after some of them. The choices, for whoever places the group:

- **As here:** all four, asked after the rest of the chain's questions would have been, which holds those back
  until the screen is answered. Acceptable only if the group sits directly after the last question before
  `s3.credit_bond` in the chain and before the thirteen behind it are due, which no order number gives while those
  are spread over other topics.
- **Three members early:** `s3.farmland`, `s3.kerosene` and `s3.credit_bond` in a block before the other s3
  questions, `s3.repaid_income` left as a question of its own after them. Nothing is held back and no refusal is
  late. Not built here (the brief named the four); it is a three-line change to the bank.
- **Change the form** so that each situation is tested and refused on its own, not in a chain. Then any grouping
  and any order works. `forms/2025/s3.yaml` has no owner under the map and was outside this lane's limits; this is a
  request to the coordinator.

The same chain bears on the map as it stands, apart from any tick-box: it sends `s3.credit_bond` to 290 to 294 and
`s3.ev*` to 225 to 229, `s3.disability_retired` to 118, `s3.mcc` to 215. By consequence 1 those would all wait for
the bond question at 290. I have not built that order; it follows from what was measured here.

### The rest

- `interview-words` and `interview-length` (the reports under `reports/2025/`) still count a group's members one
  question at a time, each with its full prompt. Only `draft-walk` counts a screen as the page shows it.
- The command-line interview prints `group` in its state but still asks one question at a time.
- No group asked of each person exists in the bank. The per-person screen is tested on a group planted on the built
  interview (`tick-groups --self-test`), not through the server or the page.
- A group whose members are of a list nested in another list (a form per employer per person) is shown per entry by
  the same code, but nothing tests it.
- Review debt: the four members' labels and the group's heading are new wording no review has read. The members'
  prompts and help are unchanged.
- Found, not changed: `s3.kerosene`'s label says "Used kerosene at home" under a heading that names "you or your
  spouse"; the prompt asks whether kerosene "was used in your home" by anyone. For a household the two read the same;
  the owner may prefer "Kerosene was used at home for heat, light or cooking" under another heading.

## Requests to other lanes

- **Coordinator:** where the proof group goes (decision 10). Any place after lane 7b's numbering works for the
  screen; see part 9, "Revisited".
- **Coordinator (form `s3`, which no lane owns), restated by the stitch lane:** the order of the refusal entries of
  `s3.line7` and `s3.line14`, if a Schedule 3 refusal is to be told at its own question at lane 7b's numbers
  (`docs/provisional/lanes/stitch.md`, part 3).
- **Lane 7b:** give every Schedule 3 question a `seq`; one left without is asked after the questions its line lists
  before it.

Each lane's proposed groups can be declared from parts 2 and 3 alone, then checked with `npm run build --silent`,
`node engine/dist/main.js tick-groups` and `tools/draft_check.sh --quick`.
