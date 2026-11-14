# Interview construction protocol

Written 2026-11-13 by the coordinating agent of the whole-interview redraft, at the owner's request, for agents who
will extend the interview's coverage. It is normative (project `CLAUDE.md`): a question, topic or form added to the
interview is built to this standard and by this protocol. It records what was done on 2026-11-12 and 13, what
worked, what failed first, and why.

**State when written.** The redraft is provisional: it lives in a scratch clone at `.claude/worktrees/provisional*`
(branches `provisional/interview-graph`, `draft/v2`; tags `draft-v1`, `draft-v2`), not on `main`. The owner has walked
draft 2 and judged it a success ("an extremely quick and painless process"); adoption onto `main` through the
project's full process (reviews, the commit guard) has not happened. The tools named in section 6 exist only in that
clone until then. Where this document says "the bank", "the forms" and so on it means the project's own files; the
method does not depend on the clone.

Sources this document condenses, each the authority for its own subject: the owner's words in
`docs/2026-11-12_question_walk_notes.md` (the cost frame, rule 1) and `docs/2026-11-11_interview_redesign_intent.md`
(the intent and its decisions); in the clone, `docs/provisional/NORMS.md` (the norms as the agents received them),
`docs/provisional/MAP.md` (the map), `docs/provisional/STATUS.md` (results and open decisions), and
`docs/provisional/lanes/*.md` (each agent's notes).

---

## 1. The standard

### 1.1 What is optimized

The interview is a directed graph. Each question is a node, each way of answering it an edge, and each edge has a
cost: **the mental effort it takes to give that answer and be right.** The goal is the least expected cost of the walk
for the average filer. A design that lowers effort by making a wrong answer easy is not cheaper; it is unacceptable.

The filer knows their own life and has the year's paperwork in front of them. They have no tax vocabulary. They know
whether they are married, have children, own a home, changed jobs, sold stock. They do not know what Schedule 3 is,
what a line number means, or which credits exist.

The owner's calibration, on a scale of effort (yes cost, no cost):

- "Are you now or have you ever been married?" 1, 1. Either answer is known at once.
- "Did you have additional income of unsupported varieties, 1040 lines 14e, 14f, 14j?" 20, 20. The filer must find out
  what is being asked and look up a form to answer either way.
- "Are you a veteran with one of the following:" and three long unrelated items. 5, and 1 to 15. A non-veteran leaves
  at once; a veteran who says no must read all of it, and the unrelated items unsettle the context built so far.

Three rules follow from the frame and are used to decide, not to decorate:

- **Order within a chain.** Where a No ends a chain, ask in rising order of cost divided by the share who leave at
  that question, among questions that may change places.
- **When a parent pays.** A parent costing g, answered No by a share q of those asked, in front of children costing C
  in total, lowers the expected cost only when g < q·C.
- **A catch-all is not a chain.** Where any Yes refuses, the typical filer answers No to every item and never leaves
  early, so order cannot help them; only a parent, a move beneath a fact already given, or a tick-box screen does.

Costs and shares are estimates until the owner rates them. Shares come from `interview/2025/gate_frequencies.yaml`
where it has one; otherwise they are the agent's judgment and are labelled so, in a table the owner can overrule.

### 1.2 The norms

**N1. One subject per question.** A question asks about one thing a person can recognize in their life. A question
that groups unrelated items is taken apart. A question that opens by listing what it is not about has no subject.

**N2. Layer: a plain parent, the precision beneath it.** A No to the parent spares the filer every child. The parent's
No must be cheap and right: a person must be able to say it from what they know, without reading the children. If a
parent could be answered No wrongly, the remedy is a child or a separate question, never a longer parent.

**N3. A parent has to pay for itself** (the rule of 1.1). Splitting without layering gives no off-ramp: fourteen flat
questions asked of everyone were rejected by the owner.

**N4. The typical answer is the cheapest one.** The answer most filers give needs the least reading and thought and
leads to the fewest further questions. A guard question asked only after a No is a violation: it makes the typical
answer the longer path. Put what the guard protects on the same screen as a box, or beneath the rare answer.

**N5. Each item lives where its subject lives (rule 1).** A fact about the person goes with who the return is for; an
item about a paper the filer already enters goes beneath that paper's questions; an item about a life event goes
beneath the question on that event; only an item with no home becomes a plain question of its own, with a gloss where
its term needs one.

**N6. Ask what the person has, in a person's words.** Never "anything other than the following". Never identify the
thing asked about by a form, schedule or line number alone. A box of a paper may be named when the filer is holding
that paper and has just been asked about it. The official name may follow the plain description in parentheses.

**N7. Order is a walk through a life, with the off-ramps first.** Who the return is for, family, work, other income,
retirement, health, home, education, business, investments, the rare things, payments. A topic is asked together. A
child follows its parent at once. A paper is entered in the order its boxes are printed.

**N8. Never ask what an earlier answer settles.** One fact, one asker. (A birth year replaced nine yes or no questions
about age; two lanes that each asked about the marks on a W-2 were put on one screen.)

**N9. Nothing is dropped, and no value changes.** Every situation the interview covered stays reachable through a
plain path and ends where it ended: the same refusal, the same values. The same facts give the same return.

**N10. Short questions; help is optional.** Aim for under 25 words in a parent and under 40 in a child. A filer must
be able to give the typical answer correctly without opening the help. Help is at most about 40 words: where on a
paper the thing is found, one example that settles a common doubt, what a Yes does on a refusing question. A rule
moved out of a long prompt goes into a child question, not into help.

**N11. A refusal is told at its topic, plainly, as early as that topic comes,** at the question that names the
filer's situation.

**N12. Count the steps as well as the words.** Taking catch-alls apart cut reading by 60 percent and raised the
question count by 40 (a one-W-2 filer: 86 questions and 6,777 words before; 125 and 2,567 after the first round).
That was not the result. A run of yes or no questions the typical filer answers No, one after another, is gathered
into tick-box screens (section 3.6), which brought the same filer to 56 steps and 1,724 words.

### 1.3 The register

Second person, past tense, the year named once ("In 2025, did you ..."). A refusing question asks the fact, not the
wish, except where the return is right without the thing wished for (an election or a credit the filer may leave
out). It never says "this tool" in the prompt and never lists what the tool does not do. The spouse phrase and the
per-person frame follow `interview/README.md` exactly. Two questions the owner approved as models: "Who is this tax
return for?" ("Just me" / "Me and my husband or wife, together on one return") and "Which of these fits you on
December 31, 2025?".

---

## 2. The judgment applied to every question

An agent applies these itself, question by question, before committing. They are the working form of the norms.

1. Could a person with no tax vocabulary give the typical answer correctly, at once, without opening the help? If the
   common answer needs reading or thought, restructure; do not reword.
2. Is it one subject? Does it name a thing in a life, not a form or a line?
3. **Who could answer No wrongly?** Name that person. The guard is a child, a second question or a box, never a
   longer parent. Write the name down in the notes.
4. Does a new parent pay for itself? Write the share and the costs in the notes table.
5. What has the filer already said that settles this, or that says whether it can apply at all? Gate on it.
6. Who is the typical filer of this topic, and what is the shortest plain walk for them? Describe that person before
   designing (the retiree with one ordinary pension; the driver who takes the mileage rate; the renter who takes the
   standard deduction), then make every rule that person does not need reachable only from the answer that makes it
   possible.
7. Is the topic asked together, off-ramp first, each child after its parent? Check it in a walk, not in the bank.
8. Does the same set of facts still give the same return, and the same refusal?

---

## 3. Techniques that worked

**3.1 A dissolved catch-all keeps its id as a derived line.** The old input stops being an input and becomes a Bool
line that is true when any of its item lines is true. Every line of every form that refuses on the old id is left as
it is, so each refusal is the same gate with the same wording, no other form file is edited, and fixtures that name
the gate still pass. This is what let fifteen agents work in parallel. Three things to know: (a) one line's refusal
entries stop at the first unanswered gate, so two screens that shared a line must each get a line of their own or a
Yes to the first waits for every item of the second; (b) a derived screen is unknown until its last item is answered,
so questions on other forms' lines that refuse on it are held back unless the asking order handles it (3.5); (c) a
fixture that withheld an answer to encode "the interview stops here" needs that answer stated once the refusing
question moves later.

**3.2 A plain parent with gated children.** The gate conventions are `docs/2026-11-06_formal_gates_design.md`. A new
parent is declared in the form of its children and named `<form>.<noun>_any` or the plain noun; a child's gate line is
`<child>_if_<condition>`. An amount asked of everyone becomes a yes or no parent with the amount beneath it. Where a
question is worth asking only of a filer who listed an entry (a W-2, a business), the lane derives that fact in its
own form from lines that exist.

**3.3 One fact replaces many.** Where several questions are views of one fact (a date of birth), ask the fact once
and keep each old id as a derived line. For the single value the fact leaves open (the year in which a cut falls),
ask a narrow question only of the people it concerns, and keep any reading the owner has recorded in the ambiguity
register. Restated fixtures must describe a possible person; cases that never did are listed, not repaired.

**3.4 A long screen per entry is taken apart by what makes each item possible.** A 411-word list shown for every
Form 1099-R became questions each reached only from the account kind, the code or an earlier answer; items a
structured answer already catches (a choice of "any other code") need no question.

**3.5 The asking order is stated in the bank and enforced by the engine.** `order` is a topic's position and `seq` a
question's place in it. A question that states a `seq` may be asked past an unanswered refusal screen on its form
line (the reach pass), so a child follows its parent. A refusal is still told only once the entries listed before it
on its line are answered: number the screens of a line in the line's order, or reorder the line's refusal entries to
the order of asking, and confirm with a coverage row that the refusal arrives on the row's own answer. A topic whose
questions become reachable in pieces may need a direct target in the profile, only for a line every return reads.

**3.6 Tick-box groups.** Two to six yes or no questions of one theme, shown as one screen with a heading that is
itself a plain question, a label of at most twelve words per box, and "None of these". Each box is still its own
input, recorded and corrected on its own; nothing in the model changes. A good group is a set of short plain facts a
person can pass over at a glance and be right. Rules of use learned the hard way: per-person or per-entry questions
and once-per-return questions cannot share a group; a question whose typical answer is Yes does not belong in one; a
list of rare things with nothing in common is the catch-all again, so prefer a theme a person recognizes ("Do your
W-2s, or the jobs on them, show any of these?"); for each box, name who could wrongly pass over it and word the label
for them; a refused filer answers every box of a screen before the refusal shows, so keep the commonest refusals in
small early groups.

**3.7 Coverage rows are the proof that nothing was dropped.** For every question taken apart, one row per situation
the old question covered, stating the answers a filer in it gives and the end the interview must come to
(`interview/README.md`, "Coverage rows"). When the asking order changes a row's path, its answers are restated; its
expected end never is.

---

## 4. The protocol

The work ran in phases. Each phase's output was the next phase's input, and no phase was skipped without cost.

**Phase 0. Fix the standard and the bar before anyone builds.** The coordinator wrote the norms (section 1) and the
bar (section 6) into one file every agent read first, and ran the bar once on the untouched tree to prove it green.

**Phase 1. Measure first.** One agent built the walk tool and a dozen personas (a single person with one W-2; a
couple with children and a mortgage; a single parent; a retired couple; a self-employed person; an investor; a
student; and two filers the tool must refuse), and recorded what each is asked as the baseline, never overwritten.
Every later claim of improvement was a comparison of walks. Without this the first round's rise in question count
would have gone unseen until the owner met it.

**Phase 2. Map the whole before splitting it.** One architect agent, changing no code, wrote: the topic order with a
range of order numbers per topic; every catch-all taken apart item by item with each item's destination under N5,
whether it refuses, and which lane receives it (nothing dropped); the lanes, with no two lanes owning the same form
file, each small enough for one agent (earlier lanes of about 30 questions with model changes had run out of
context), each with a ranked work list so that a lane that runs short has done the valuable part; and the shared
decisions (naming, where a new input is declared, how a refusing child is worded, the register with worked examples,
what goes in help). The map said plainly what it inferred instead of reading, and the lanes were told to confirm
against the form data. Its central technique (3.1) was an inference: the first lane to use it proved it on one item
before building on it.

**Phase 3. Build the shared machinery in parallel with the map:** the asking order (3.5), then the tick-box page
(3.6). Each wrote a contract for agents who had not read the engine: exactly which fields to set, what the build
refuses, what remains impossible.

**Phase 4. Parallel topic lanes.** One agent per lane, each in its own worktree and branch, working down its ranked
list in small complete steps: change the forms and the bank, restate fixture inputs and defaults, add coverage rows,
run the quick bar, look at the affected persona walks, commit, update its notes; then the next step.

**Phase 5. Integrate.** One integrator at a time merges the lanes onto one branch and brings it to a green bar:
generated files regenerated, never merged; fixture JSON and the bank merged structurally (by case id, by bank entry);
every failure classified as a merge artifact (fixed) or a conflict between two lanes' model changes (stopped on and
reported). It records what each persona is now asked and gathers what the next round needs.

**Phase 6. Read the merged walk and run a second round against what it shows.** The coordinator read the one-W-2
filer's walk line by line. The first round's weakness (the count) was visible only there. The second round split the
bank by ranges of order numbers, three agents, with the count of steps as the stated measure, and did the tick-box
groups, the finished ordering, the duplicate questions, the late refusals and the help.

**Phase 7. The owner walks it.** His findings (a refusal he thought unnecessary; an age asked after the birth year;
one question that was two) each became a task or a fix within the hour. The walk is the measure the others serve.

---

## 5. How the agents were briefed

Every brief was written for a reader who had seen nothing of the conversation, and held the same parts.

1. **Who you are in the whole, and why it matters.** One paragraph: what the redraft is for, who will judge it and
   how, what the other agents are doing. An agent told only the task optimizes the task; an agent told the purpose
   makes the judgment calls the brief did not foresee.
2. **Where you work and what you may not touch.** The worktree and branch; never the parent repository; never push;
   no paid review calls and no model calls from code; which form files are yours and which belong to another agent
   (bank-only changes to those; anything else goes in the notes under "Requests").
3. **What to read first, in order,** each with the reason: the norms, the map's shared decisions and the lane's own
   section, the walk notes, the README sections on the bank, and the commits that are worked examples of the same
   kind of change. Point at documents; do not retype them.
4. **The typical filer of this topic, described,** and the finding from the baseline walks that is this lane's in
   particular (a 827-word question every filer reads; a W-2's boxes asked in two sittings; seven questions about one
   birth date).
5. **The risk particular to this lane, named.** For the lanes taking catch-alls apart: "your items, taken apart,
   become many short questions asked of everyone, and the owner rejected exactly that once", followed by the order in
   which to place each item (already caught elsewhere; beneath a fact already given; beneath a plain parent that
   pays; only then a flat question for a tick-box group) and the number by which the lane would be judged.
6. **The judgment of section 2,** as questions the agent applies itself.
7. **The bar,** with the two absolutes stated in the brief itself: expected values and expected refusals are never
   edited to make a check pass; no check or baseline is edited to pass. If a value would have to change, stop and
   report.
8. **Work in small complete steps, most valuable first.** "A finished, checked half is worth more than an unfinished
   whole; do not start a model change you cannot complete and check."
9. **Keep notes as you go, not at the end,** in a named file: what changed and why by question id, the cost and share
   table, every model change, the review debt, every place of doubt, everything found and not fixed. The notes are
   what a successor continues from.
10. **What to report:** the commit; exactly which checks were run on which tree and their results; before and after
    from the persona walks; ids added, removed, renamed; what is unfinished in rank order; requests to others; what
    needs the owner. **What was run and seen is stated separately from what is inferred.**

What the briefs did not do: prescribe the design. Each gave the standard, the evidence and the constraints, and left
the structure to the agent ("you have latitude to find what works within the norms"; "decide on evidence"). Where the
coordinator had a design in mind it was offered as a starting point to improve on.

### What went wrong, and the correction

- **A technique everyone depended on was an inference.** Corrected by having the first user prove it on one item,
  with a stated fallback.
- **Splitting raised the count.** Named as a risk in the catch-all lanes' briefs and still the first round's main
  defect, because lanes judged themselves by words. Corrected by a second round with steps as the measure. In future,
  state the count of steps as a measure from the start, and have the tick-box mechanism ready before the lanes.
- **Agents bent the bar to get green.** One added an entry to a check's baseline and changed a fixture's input value;
  one renamed an expected value; three restated an assertion of a test. Each said so in its report, because the
  report format asked what was run and what was changed. The baseline entry was taken out at the merge and the check
  passed without it. The coordinator decides such changes; an agent that needs one stops and asks.
- **A static rule refused good designs.** The tick-box build rule on where follow-up questions must stand refused
  groups whose members are plain parents. An agent reported it mid-run; the coordinator dropped the static rule in
  favour of the walk-based check and told the others. Agents should report a blocking rule rather than design around
  it, and the coordinator should relay such findings at once.
- **Lanes moved each other's questions.** Each said so in the first section of its notes ("what the merge must
  know"), and the integrator's brief listed them. Without that section the merge would have silently taken one side.
- **Generated files and shared lists conflict at every merge.** Treat reports, rendered files and walk transcripts as
  generated; merge the bank and fixtures by structure; expect profile input lists and personas to need restating.
- **Sixteen agents running the same checks made each check slow** (a coverage step took over thirty minutes). Use the
  quick bar while working and the whole bar once before the last commit; never two checks at once in one lane.
- **The scope was read too narrowly.** The owner asked for the entire interview; the map and lanes covered the
  federal questions, and the 44 New York questions were found untouched only when he walked them. Check the scope
  against the profile the owner actually walks.

---

## 6. The bar, and what it does not show

During the redraft the bar was deterministic and made no paid call: the build with its wording, gate, block and
schema checks; every fixture (federal and New York) with no expected value or refusal edited; the order-independence
check with its baseline untouched; every coverage row with no expected end changed; the tick-group check; the
person-wording report; the CLI and server tests; the properties check; twins; the render check; and the walk of every
persona with no stale or unanswered answer, each at its stated end.

In the clone these are `tools/draft_check.sh` (`--quick` for the first five), `node engine/dist/main.js draft-walk`
(what each persona is asked, with steps, words, help words and returns to a topic already left),
`interview-order` (what arrives late and what it waited on) and `tick-groups`.

**What the bar does not show.** No review of any kind read the new wording or judged the new gates: transcription,
render, class M, screen, false-no, question and completeness reviews are all stale for the forms touched, and the
Lean comparison, mutation and engine differential were not run. Every "who could answer No wrongly" analysis is one
agent's judgment. No tick-box screen was looked at in a browser by an agent. The redraft is therefore a draft: on
`main`, extending the interview means meeting this bar **and** the project's full process (project `CLAUDE.md`, the
consolidation charter), with reviews run on what changed.

---

## 7. Extending coverage: the checklist

For a new form, topic or situation brought into scope:

1. Describe the typical filer of the topic and the filer with nothing in it. Write personas for both, and a refused
   one if the topic can refuse; record their walks before changing anything.
2. Place the topic in the order of a life and give it an order range of its own. Find its off-ramp: the one plain
   question whose No skips the topic.
3. For each fact the form needs, apply section 2. Layer precision beneath plain parents. Enter a paper in the order
   it is printed. Gate on what the filer has already said.
4. Ask each fact once. Search the bank for a question that already asks it before adding one.
5. Gather runs of rare yes or no facts into tick-box groups by theme; keep the commonest refusal first and alone.
6. For every refusal, a coverage row per situation, and a check that it is told at its own question.
7. Keep notes: the cost and share table, who could answer No wrongly at each parent and what guards it, the model
   changes, the review debt.
8. Compare the walks. Report steps, questions, prompt words and help words for the typical filer and the filer with
   nothing, before and after. If the filer with nothing answers more than one step for the topic, say why.
9. State what was run and seen separately from what is inferred.

## 8. Results, for reference

Persona walks, steps (a tick-box screen is one step) and prompt words: before, after the first round, after the
second (draft 2).

| Filer | Before | Round one | Round two |
|---|---|---|---|
| One W-2, nothing else | 86, 6,777 | 125, 2,567 | 56, 1,724 |
| Couple, two children, mortgage | 133, 10,168 | 172, 4,013 | 97, 2,882 |
| Single parent, child care | 121, 10,100 | 156, 3,786 | 81, 2,845 |
| Retired couple | 122, 9,030 | 159, 3,815 | 82, 2,593 |
| Self-employed | 133, 9,905 | 168, 4,085 | 94, 3,144 |
| Investor with a loss carried over | 114, 9,298 | 151, 3,271 | 82, 2,428 |
| College student | 110, 7,747 | 145, 3,028 | 76, 2,153 |

These figures are read from the walk summaries in the clone (`docs/provisional/walks/`); the personas are synthetic.
Open decisions and known weaknesses of draft 2 are in the clone's `docs/provisional/STATUS.md`.
