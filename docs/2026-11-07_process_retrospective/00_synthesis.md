# Process retrospective: tax-formalization, 2026-10-13 to 2026-11-07

Synthesis of four read-only investigations, each by a claude-opus-5-5 agent:
- 01_git_history.md: phases, churn and composition across 211 commits
- 02_planning_and_staging.md: handoffs, plans, replans and owner decisions
- 03_delegation_review_cost.md: agent runs, paid reviews and the bug inventory
- 04_architecture.md: layers, file construction and tooling

The detail and citations are in those files. This document gives my combined reading of them.
Credence is marked where it matters.

---

## 1. Verdict in one paragraph

The project was not chaotic. It had a coherent vision of the artifact, and that vision held. The
day-1 spec and design (`d3f06cb3`, 10-13) are still the architecture: a small DSL, an evaluator of
827 lines, refusals treated as values, citations, and a Lean reference evaluator. Churn in the
authored source was low (deleted lines were 0.08 to 0.24 of added lines), and the history is
linear.

What was not designed was everything the artifact needed once the goal became much larger. On
10-16 (`7b60e465`) the target changed from a one-return proof of concept to a product meant to
cover 80% of filers, then 95%. That change was written as an amendment to the spec, not as a
redesign. Three systems were never designed for the new scale:
1. the verification system: how reviews are run, stored, kept current, scoped and paid for;
2. the interview's applicability layer: whether a form or amount applies to this person at all;
3. the infrastructure for scale: fixtures, jurisdiction, test tiers and parallel lanes.

Each was built later, in instalments, usually after an incident. Most of the inefficiency you can
see traces back to that one missed redesign point, not to disorder in day-to-day work.
(Credence: moderate to high. All four investigations reached this independently, each from a
different source.)

---

## 2. The shape of the work over time

| Phase | Dates | Commits | What happened |
|---|---|---|---|
| P0–P1 Design and proof of concept | 10-13 → 10-15 | 15 | Spec, source archive, stages 0–5 with "done when" checks. Clean. |
| P2 Verification retrofit | 10-16/17 | 12 | The pivot. Model "independent construction" was added after the content it checks. BUG-0001, a value error, turned up 7 minutes in. |
| P3 Coverage stages 8–16 | 10-17 → 10-22 | 62 | Fast coverage growth, ordered by a measured estimator. |
| P4 Integrity overhaul | 10-22 → 10-27 | 21 | An outside evaluation credited only 1.3% of computed lines with a check by a different model family. Integrity plan, validation policy, plan revision. |
| P5 Route to 80% | 10-27 → 10-29 | 8 | Peak coverage 82.2% (`a428e8bb`). |
| P6 Sweeps and hardening | 10-30 → 11-02 | 33 | Root-cause analysis. The completeness review, first run on day 18, found 50 defects. Coverage corrected to 78.4% (`e6a8053a`). |
| P7 Parallel backlog and cost control | 11-02 → 11-04 | 16 | Cost ledger from 11-04; the owner reversed the earlier "don't weigh cost" rule. |
| P8 TY2026, New York, release tiers | 11-04 → 11-06 | 8 | New York retrofitted through a `--jurisdiction` flag across 36 tools. |
| P9 Web UI and formal gates | 11-06 → 11-07 | 36 | The UI exposed interview length (165 questions, 142 answered no or zero). Topic layer built and dropped; formal gates designed. |

The pattern repeats: **build sprint → incident or audit → dated plan document → new tooling →
new rule in CLAUDE.md → next sprint.** It happened at least four times (P2, P4, P6, P7/P9).
The project corrects itself and records everything, which is a real strength. The cost is that
the corrections arrive after the content they apply to, so every form gets reviewed again each
time.

---

## 3. Six findings, each supported by more than one investigation

### 3.1 The pivot on 10-16 is the root decision
The goal grew roughly tenfold. Only the verification checks were rescoped. Staging, cost, what
the owner could vouch for, the role of the second model family, suite time, the target tax year
and the interview layer were left as they were. Each later received its own plan:

| Plan | Date |
|---|---|
| Integrity plan | 10-22 |
| Validation policy | 10-24 |
| Plan revision | 10-26 |
| Root-cause analysis | 10-29 |
| Backlog plan | 11-01 |
| Cost rules | 11-03 |
| Release gating | 11-05 |
| Formal gates | 11-06 |

Several of these diagnose problems the 10-16 spec already named or that were knowable then. One
example: the TY2025 filing deadline (10-15) had already passed when the pivot was made.
(Investigations 02 and 01.)

### 3.2 The architecture fits the arithmetic of tax law but not the interview
Computation was a good fit:
- 0 of 3,549 lines are opaque.
- The evaluator gained only 5 atoms after day 1.

Applicability was not modelled at all. The day-1 spec says the tool "decides which forms apply",
but there were no existence facts, the yes/no facts such as "did you receive dividends?". As a
result every input stayed reachable. This surfaced only on day 24, through the UI.

Question wording is the project's top bug class: 30 bugs, 26 of which changed tax amounts. The
day-1 interview invariants in spec 6.4 are essentially the formal-gates rules approved on 11-06.
Had they been enforced from Stage 5, they would likely have prevented the topic-layer detour and
part of that bug class. (Investigations 04 and 02. Credence that this was foreseeable: moderate
to high, since the Direct File Fact Graph cited in the README models exactly these facts.)

### 3.3 Evidence is tightly coupled to content
- **Derived files dominate changes:** in the commits that touch form definitions, derived files
  (fixtures, reviews, reports, renders) changed about 8 times as often as authored files.
- **One gate touched 153 files:** the dividends gate (`1075bb5c`; I confirmed the 153 files).
- **Fixtures are organized by stage, not by form:** whole-return fixtures list every input, so
  `stage1.json` carries 105 inputs per case.
- **Most churn is generated evidence:** 88% of the 9.5M lines churned were committed review
  output that was later regenerated.
- **Old review data is still on disk:** 91 git-ignored snapshots of invalidated review data.

This coupling is the mechanism that turns every convention change into a migration across the
whole project. (Investigations 04 and 01.)

### 3.4 Rules enforced by tools held; rules written as prose did not
Rules built into code had measurable effects:
- Turning off prompt caching cut cost per input token by about 42%.
- The DeepSeek restriction held.
- `siblings.py`: 8 missed-sibling bugs before it, 1 after.

Rules written only in CLAUDE.md showed little effect:
- "One review per form per round" (11-05) was routinely broken. f8889 was reviewed several times
  on 11-07 by three lanes and after rebases. The guard the process-optimization doc proposed was
  never built.
- "Mechanical work on Sonnet" moved Sonnet's share of tokens only from about 1% to 5–11%.

(Investigation 03. My own recount from the ledger: on 11-07, 127 of 214
subject/review-type/tool combinations ran two or more times, and f8889 had 5 completeness calls
in the UTC day. The agent reported 81 of 208 and 7, using a different grouping and time zone.
The exact numbers depend on method, but the conclusion that repeats were common holds either way.)

This is the same principle as QMS §5.6: hooks beat rituals, and rituals beat prose. Here it shows
up at project level.

### 3.5 Owner attention went to the wrong decisions
Every stage batch of reading decisions with a recorded outcome was "all recommended accepted",
usually the same or the next day. Frame decisions were never put to you up front:
- the goal metric
- what the second model family is for
- whether to weigh cost
- the target year
- the human-reading requirement

Those are exactly the decisions that were later reversed:
- human reading was made optional within 2 days;
- the second family was made optional on 11-02, after finding 1 bug in 1,488 rulings;
- the rule "don't weigh cost" (10-21) was reversed on 11-03.

(Investigation 02. Credence: moderate.)

### 3.6 The goal widened while federal coverage stopped
Federal coverage has stayed at 78.4% since 11-01. Stage 17 (Schedule E) was deferred repeatedly.
About 90 commits since then went to hardening, New York, TY2026 and the web UI.

The backlog plan says coverage expansion comes last. That plan has been stale since about 11-04
and was never retired, so the written authority and what actually happened disagree. **Nothing in
the record says whether this was your deliberate priority or drift.** Only you can say.
(Investigations 01 and 02.)

---

## 4. Review economics in brief (investigation 03)

- **Coverage of the data:** the ledger covers only 11-04 onward, about $328, an estimated 17% of
  all-time review spend (low confidence). The agent log covers only 11-03 onward. 21 of 26 days
  cannot be priced.
- **Yield by review type:**
  - Completeness, screen and false-no reviews cost about $2–3 per bug.
  - Transcription cost more than $150 per bug and render about $70.
  - Class M found nothing in the ledger window.
  - Claude transcription is still the largest single line item: $157.63, 48% of the ledger, for
    almost no findings.
- **Mismatch with phase:** render and transcription were the right tools while forms were being
  written. Spend never shifted after the stages closed on 10-29.
- **Completeness review works like a random sample.** Each run finds a different subset of
  long-standing gaps, so "review what changed" pulls a fresh batch of old low findings on every
  small edit. Half of the 146 completeness rulings are scope noise.
- **The worst single waste:** $58 (18% of the ledger) on replies for 45 unchanged forms that were
  archived without adjudication.
- **Rework was modest:** 5–13% of agent tokens, depending on definition. Most agent cost went to
  gate and engine work, not to rework.

---

## 5. Evidence against the "inefficient" reading

- The core design bet paid off decisively. Up-front design effort was not wasted, and the formal
  gates show the architecture can take the interview fix without a rewrite (the evaluator change
  was `a061e282`, 10 files).
- A design sized for a 5-stage proof of concept reasonably would not include month arrays or
  existence facts. The failure was not re-designing at the pivot, more than not designing on day 1.
- Some guarantees that look like overhead were chosen deliberately. Fixtures that list every input
  catch reachability leaks.
- Every correction is dated, reasoned and kept in the record. Plenty of projects drift without
  ever noticing. This one noticed each time, within days.
- Some of the widening (New York, TY2026, the UI) may have been exactly what you wanted.

---

## 6. Recommendations, ranked by expected rework avoided (my judgment)

1. **Treat now as the redesign point you skipped on 10-16.** Write one short design document,
   confirmed by you, that covers:
   - the goal and its order (federal coverage vs NY vs TY2026 vs UI);
   - the verification system: which review types run in which phase, what the second family is
     for, and the cost budget;
   - the applicability/gates model;
   - the fixture and evidence layout.

   Retire the stale plans by deleting them. Keep one living roadmap, with history left to git.
2. **Move process rules into tools.** The current prose rules most in need of a tool guard:
   - a once-per-round guard and a dry-run cost estimate in `rerun_all.py`, with an owner gate above
     a dollar threshold;
   - Sonnet as the default model for mechanical agent launches.

   Each prose rule in CLAUDE.md should either get a guard or be treated as advisory.
3. **Separate evidence from content.** Organize fixtures and evidence by form, not by stage. Allow
   partial per-form fixtures with defaults set by rule, and keep a small whole-return set. Take
   generated review output out of git, or make it content-addressed.
4. **Match review spend to phase.** Cut Claude transcription on forms that are not changing. Run
   completeness as a fixed number of independent samples per form per milestone, adjudicate their
   union once, and stop letting pre-existing low findings trigger another rerun.
5. **Settle conventions before fanning out parallel lanes, and serialize lanes that touch the same
   form.** 11-07 paid for keep-the-id conversions, rebases and triple reviews of f8889.
6. **Spend your attention on frame decisions.** At each phase boundary, ask a short batch of frame
   questions. Let agents decide the micro-decisions under a reversible log.
7. **Prune the tooling.** `check-all` grew from 24 steps to 90, about 38 of them self-tests and 19
   New York duplicates. `tools/` has 120 scripts, including Python reimplementations of the
   evaluator and the renderer.

---

## 7. Limits of this retrospective

- Cost data covers only the last 4–5 days. Earlier spend is an estimate, at low confidence.
- 50 commits have no co-author trailer, so who made them is unknown.
- The owner's intent behind New York, TY2026 and the UI cannot be read from artifacts.
- Agent claims I re-checked myself:
  - the commit subjects and dates of `7b60e465`, `a946fae5`, `a428e8bb`, `e6a8053a` and
    `0186a66f`;
  - the 153 files in `1075bb5c`;
  - total ledger spend ($328.30);
  - the repeat-review pattern on 11-07 (which reproduced, with different counts).
- Everything else rests on the agents' reports. They cite commits and files, and I have not
  audited those citations.
