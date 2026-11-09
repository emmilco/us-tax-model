> **Historical (2026-11-09):** superseded by `docs/2026-11-09_consolidation_charter.md`. Kept as a record; it no longer governs.

# T-251 question structure: design

Status: approved by the owner 2026-11-06 (intent readback confirmed the same day). Built on the T-236 branch, merged with T-236.

## Goal

The interview asks what a person can answer from their own life, and asks first the questions that rule out the most.
A typical return finishes in a few dozen questions, and no question asks the user to check their situation against a
long list of exceptions. The tax logic, refusal rules and reviewed form data are unchanged. What changes is which
questions are shown, in what order and in what words.

Baseline (one return, not an average): the single-filer fixture `ny.table.single.0` asks 165 questions to completion,
142 of them (86%) answered no, zero or none. The four scope screens (`scope.*`) have a median prompt length of about
880 characters, and each asks for the complement of a long list.

## Owner decisions

- A topic layer up front that rules out whole subtrees, not only a reordering of the existing questions (2026-11-06).
- Implications live in the interview layer, as reviewed data; the engine and form data are unchanged (2026-11-06).
- Topic questions are about situations, with documents as examples ("Did you receive dividends? Usually reported on
  Form 1099-DIV"), because documents do not map exactly onto income (2026-11-06).

## The topic layer

A **topic** is a situation question in the question bank: its prompt and help, the input templates it **covers**,
and for each covered template the value it **implies** when the answer is no (an empty roster, a zero amount, false).

```yaml
topics:
- id: dividends
  prompt: Did you receive any dividends in 2025?
  help: Usually reported on Form 1099-DIV. Include dividends of any size, even without a form.
  covers:
    div.box1a: 0
    div.box2a: 0
    # ...every input template that only matters when there are dividends
```

A **checklist topic** replaces a scope screen. Its items are short situations, each one clause of the screen's
reviewed text, plus "None of these". The screen input's value is implied as true when any item is ticked and false
when only "None of these" is. The screen's reviewed text stays in the form data as the definition the items are
checked against.

Initial topics, refined by the build and fixed by the review: wages (W-2, including tips and overtime); interest;
dividends; securities sales; retirement distributions (1099-R) and IRAs; Social Security benefits; unemployment and
state or local refunds; self-employment or a business (Schedule C, vehicles, depreciable property); children and other
dependents (credits, care expenses); Marketplace health insurance (1095-A); HSA; education expenses; home energy
improvements; car loan interest; charitable gifts and other itemized deductions; long-term care insurance; other
income. The four scope screens become checklist topics. New York residency questions stay as they are.

### Semantics

- **Log.** A topic answer is an event `{topic, value}` in the answer log, beside the existing `{input, value}` events.
  The engine never sees topics: replay turns them into inputs.
- **Replay.** Each covered input not explicitly answered takes the value the topic implies when the topic's answer is
  no. When a topic is no, explicit answers to its covered inputs are inactive but kept in the log, as removed roster
  entries are now. Changing the topic back to yes reactivates them.
- **Asking.** Unanswered topics come first, in a fixed order (most common situations first). A covered input is not
  asked while its topic is unanswered or no. After the topics, the pending questions are asked as now.
- **Provenance.** An implied value says where it came from. The page shows "from your answer: no dividends" and links
  to the topic. The derivation view shows the same. The CLI state lists implied inputs with their topic.
- **CLI.** `interview answer --topic <id> --value <JSON>` answers a topic, through the same `applyAnswer` path.

### What stays always asked

Inputs no topic covers are asked as now: filing status, the person roster and ages, New York residency, and anything
the build cannot place under a topic soundly. The build lists them and says why each is uncovered.

## Checks

Mechanical, in `check-all`:

1. **Fixture equivalence.** For every federal and New York fixture: set each topic to no exactly when all its covered
   inputs equal their implied values, walk the interview answering only what it asks, and require the final values to
   equal `test-fixtures`' expected values. The same holds on generated returns (`generate.ts`). This catches rules that
   hide an input a return needs. It cannot show that a rule is true of the world. That is the review's job.
2. **Coverage.** Every covered template exists and is an input. An implied value has the input's type. No template
   is covered by two topics with different implied values. Every clause of each scope screen maps to a checklist item,
   recorded as data that the review checks.
3. **Question count.** For every fixture walk, the number of questions with topics against without. The build reports
   the distribution, and `check-all` fails if a fixture's count increases.

Judgment, before the owner uses it with real data: an **independent review** (Opus, an agent other than the builder)
of every topic against its sources. Is "no" to the topic's situation enough to make each implied value true? Do the
checklist items cover each screen's reviewed text exactly? Findings go into the bug inventory, as other reviews' do.

## Ordering beyond topics

Once topics are in, ordering the remaining questions by expected pruning is measured, not assumed. The build reports
which questions are still asked most across fixture walks. A further step (weighting by how common each situation is,
from the coverage estimate's microdata) is designed only if that report shows it would cut the count materially.

## Out of scope

Changing tax logic, refusal rules or form data; bounded-count selectors and the type review (T-253); filled PDFs
(T-252); and `person.role` and "skip for now", which the owner decides separately.

## Build

One Opus agent (judgment class) in the T-236 worktree, on the T-236 branch, because the page and server it extends are
there. Fast tier. The independent review follows as a separate Opus agent.
