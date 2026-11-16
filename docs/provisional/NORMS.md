# Provisional redraft of the whole interview: norms and working rules

**Historical.** The working rules given to the agents of the whole-interview redraft (2026-11-12 and 13), in a scratch clone. The redraft has landed on `main` (`a2f24909`). The current standard for interview questions is `docs/2026-11-13_interview_construction_protocol.md`, which restates these norms as N1 to N12; follow it, not this file.

Written by the coordinator on the night of 2026-11-12 for every agent of the redraft. The owner asked for the entire
interview to be reconstructed on the norms below, as provisional work he will walk in the morning and adopt or reject.
This clone (`.claude/worktrees/provisional`, branch `provisional/interview-graph` and lane branches cut from it) is a
scratch copy: nothing here reaches `main` unless the owner adopts it, and adoption will then go through the project's
full process (reviews, the commit guard). Read this file whole before doing anything.

Sources, in the owner's words where it matters: `docs/2026-11-12_question_walk_notes.md` (the frame and rule 1),
`docs/2026-11-11_interview_redesign_intent.md` (the intent and its decisions), `docs/2026-11-11_owner_walkthrough_notes.md`
(his first walk). Where this file and those disagree, those win; tell the coordinator.

## 1. What we are optimizing

The interview is a directed graph. Each question is a node, each way of answering it an edge, and each edge has a
cost: **the mental effort it takes to give that answer and be right.** The goal is the least expected cost of the walk
for the average filer. A design that lowers effort by making a wrong answer easy is not cheaper; it is unacceptable.

The filer knows their own life and has the year's paperwork in front of them. They have no tax vocabulary. They know
whether they are married, have children, own a home, changed jobs, sold stock. They do not know what Schedule 3 is,
what a line number means, or which credits exist.

The owner's three calibration examples (yes cost, no cost):

- "Are you now or have you ever been married?" 1, 1. Either answer is known at once.
- "Did you have additional income of unsupported varieties, 1040 lines 14e, 14f, 14j?" 20, 20. The filer must find out
  what is being asked and look up a form to answer either way.
- "Are you a veteran with one of the following:" followed by three long unrelated items. 5, and 1 to 15. A non-veteran
  leaves at once; a veteran who says no must read all of it, and the unrelated items unsettle the context.

Two questions the owner has already approved as they stand (thumbs up on the vetting page); treat them as the model of
the register wanted: `$person` ("Who is this tax return for?" with the choices "Just me" and "Me and my husband or
wife, together on one return") and `f1040.status` ("Which of these fits you on December 31, 2025?").

## 2. The norms

**N1. One subject per question.** A question asks about one thing a person can recognize in their life. A question
that groups unrelated items is taken apart. A question that opens by listing what it is not about has no subject of
its own.

**N2. Layer: a plain parent, the precision beneath it.** "Do you have any pets?" / "Do you own a cat?" / "Was your cat
trampled by lions, or is it orange?". A no to the parent spares the filer every child. The parent's no must be cheap
and right: a person must be able to say it from what they know, without reading the children. If a parent could be
answered no wrongly, the remedy is a child or a separate question, never a longer parent (`sb.foreign_any` grew to
about 840 words by the other remedy).

**N3. A parent has to pay for itself.** A parent costing g, answered no by a share q of those asked, in front of
children costing C in total, lowers the expected cost only when g < q·C. Do not add a parent over one cheap child, or
over children most people answer yes to. Fourteen flat questions asked of everyone were rejected by the owner:
splitting without layering gives no off-ramp.

**N4. The typical answer is the cheapest one.** For each question, the answer most filers give must be the one that
needs the least reading and thought. The detail that only the rare answer needs sits behind the rare answer (in a
child), not in front of everyone.

**N5. Each item lives where its subject lives (rule 1).** Taking a catch-all apart moves its items into other topics:
a fact about the person goes with who the return is for; an item about a paper the filer already enters goes beneath
that paper's questions; an item about a life event goes beneath the question on that event; only an item with no home
becomes a plain question of its own, with a gloss where its term needs one.

**N6. Ask what the person has, in a person's words.** Never "anything other than the following". Never identify the
thing asked about by a form number, schedule or line number alone. A box of a paper may be named when the filer is
holding that paper and has just been asked about it ("box 12 of this W-2"). The official name may follow the plain
description in parentheses when it helps a filer find it on their paper.

**N7. Order is a walk through a life, with the off-ramps first.** Topics come in the order a person would tell their
year: who the return is for, family and household, work, other income, retirement, health, home, education, business,
investments, then the rare things. A topic is asked together and is not interleaved with another. Within a topic, a
child follows its parent at once. Among questions that may change places, ask first the one with the lowest cost per
unit chance of leaving (cost divided by the share who exit on it).

**N8. Never ask what an earlier answer settles.**

**N9. Nothing is dropped, and no value changes.** Every situation today's interview covers stays reachable through
some plain path, and still ends where it ends today (the same refusal, the same values). A situation no plain parent
leads to keeps a question of its own, however rare. The same facts must give the same return.

**N10. Short questions; help is optional.** The prompt is the question. Aim for under 25 words in a parent and under
40 in a child; where a question needs more, that is a sign it is two questions. A filer must be able to give the
typical answer correctly without opening the help. Do not move a long prompt into the help (the health savings account
lane's help doubled that way); move it into children.

**N11. A refusal is told at its topic, plainly, as early as that topic comes.** A common reason the tool cannot do a
return should not wait behind a long stretch of questions.

## 3. Estimating cost and share (how to decide, not a deliverable in itself)

For each parent or reordering you propose, write down in your lane notes: the share of filers reaching it who answer
yes (from `interview/2025/gate_frequencies.yaml` where it has one; otherwise your judgment, labelled as judgment), and
your estimate of the cost of each answer on the owner's scale (1 = known at once; 5 = a moment's thought or a glance
at a paper; 20 = must find out what is being asked). These are your estimates, not measurements: the owner will rate
costs himself. Use them to apply N3, N4 and N7, and keep them in a table so he can overrule them.

## 4. What may be changed

Everything the interview is made of: `interview/2025/questions.yaml` (prompts, help, order, `seq`, choices, labels),
the form definitions in `forms/2025/` where a new parent, a split catch-all or a moved item needs the model to change,
the profiles, `interview/2025/coverage/`, fixtures' inputs, and the engine or page where the structure needs it.
`interview/README.md` describes the bank, blocks, the spouse phrase, the per-person frame and the build's wording
rules; `docs/2026-11-06_formal_gates_design.md` the gate conventions; commits `abf7d60a` (credits), `e70f95bb` (health
savings accounts) and `8acf6830` (the opening) are worked examples of exactly this kind of change, on main.

There is no tick-all-that-apply question type (T-285); do not build one unless the coordinator assigns it.

## 5. The bar every lane meets (deterministic; no paid calls)

- **No paid review calls and no model calls from code.** Do not run `transcribe.py`, `render_compare.py`, `classm.py`,
  `screen_review.py`, `false_no_review.py`, `question_review.py`, `completeness_review.py` or `rerun_all.py`. Do not
  touch `.transcription/` or `.classm/`. Review logs will go stale; that is expected here and is recorded as debt.
- **`tools/draft_check.sh` passes** in your worktree before every commit: the build (with its wording, gate and
  schema checks), the fixtures, interview-rules, the coverage rows, the person-wording report, the CLI integration
  tests, the properties check and the server test.
- **Expected values are never edited to make a check pass.** A fixture's *inputs* change when a question is renamed,
  split or added (the new answers that describe the same facts). If an expected value or an expected refusal would
  have to change, stop: either your change altered the tax result (undo it) or you found an existing defect (record it
  in your lane notes with the case, do not fix the model's arithmetic in this redraft).
- **Do not regenerate** `fixtures/**/classm*.json` or `mutation.json` by model or mutation run; edit their inputs only
  where the build requires it. New inputs need a default in `fixtures/2025/defaults.json` (the build checks this).
- **Coverage rows.** For every catch-all or long question you take apart, write rows in
  `interview/2025/coverage/<part>.yaml` showing that each situation it covered still reaches its end, and keep the
  existing rows passing (rewrite their answers where your change moved a question).
- **Commit in your own worktree and branch only.** Plain `git commit` works here (this clone has no commit guard).
  Never commit, push or change anything in `/Users/elliotmilco/Documents/GitHub/tax-formalization` outside
  `.claude/worktrees/provisional*`. Never push anywhere.
- **Lane notes.** Keep `docs/provisional/lanes/<lane>.md` up to date as you work, not at the end: what you changed
  and why (by question id), the cost and share table of section 3, every model change (inputs added, removed,
  renamed; gates added), the review debt it creates, every place you were unsure, and everything you found and did
  not fix. If you run low on context, the notes are what a successor continues from; write them so that works.
- **Stay in your lane's files.** The map (`docs/provisional/MAP.md`) says which forms and which bank entries are
  yours and which items another lane hands you or you hand on. If you need a change outside them, write it in your
  notes under "Requests to other lanes" and report it; do not make it.

## 6. What a lane reports when it ends

Its branch and last commit; the result of `tools/draft_check.sh`; before and after for its topic (questions asked and
prompt words for a filer with nothing in the topic, and for an ordinary filer with the topic's common case); what it
did not finish; anything that needs the owner. State what you ran and saw separately from what you infer.
