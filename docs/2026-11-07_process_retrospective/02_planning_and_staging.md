# Process retrospective, slice 2: planning, staging and decisions as recorded in documents

Investigator: claude-opus-5-5 (judgment class), read-only. Written 2026-11-07.
Repository: `/Users/elliotmilco/Documents/GitHub/tax-formalization`, HEAD `d05db7e6`.

**Method.** I read the original spec, design and HANDOFF at their first commits (`git show d3f06cb3`, `f6504260`), the 10-16 amendment (`7b60e465`), every plan document in `docs/`, the heads and owner-decision sections of all 21 handoffs, `HANDOFF-NEXT-SESSION.md` and its archive, `TASKS.md`'s header, and the history of `CLAUDE.md` and `spec/`. Documents count as testimony. Where a check was cheap I compared them against git (creation commits, dates, renames, commit gaps, commit sizes). Observations and interpretations are kept apart, and each interpretation is marked with a credence: *weak*, *moderate* or *strong*.

---

## 0. Summary of findings

1. **The original plan (2026-10-13) was coherent and well suited to its task.** It was a single-return proof of concept, built in 7 stages (0–6), each with a "done when" a third party could check. It stopped for the owner after every stage, enforced strict evidence classes and checked premises before encoding anything. Stages 0–5 were finished by 2026-10-15 (`8417477f`), about 48 hours after the plan was committed. *Strong.*
2. **The defining event was the 2026-10-16 pivot (`7b60e465`, written by Claude Fable 5.1).** It changed the goal from a proof of concept to coverage of most filers (later all filers, 80% then 95%). It also replaced human line-by-line reading with agreement among model-built "independent constructions". The verification apparatus was rescoped in that commit. The process around it was not: how stages relate to verification, what the owner can vouch for, cost, and the interview layer. After that, stages were appended one at a time ("Stage 9 onward. Coverage") and never redesigned. *Moderate to strong.*
3. **From 10-16 onward the process alternated in phases:** coverage sprints (Stages 8–16, 10-17 to 10-22; Stages 20, 18, 19, 21, 10-27 to 10-29), then correction programs (integrity, 10-22 to 10-27; hardening and backlog, 10-29 to 11-04), then late product work (NY 11-04/05, web UI and gates 11-06/07). Each correction began with a dated plan document that diagnosed the previous phase. **Most of these diagnoses were sound and based on evidence.** Several described consequences that the 10-16 design either stated itself or could have predicted: the shared-reader blind spot, the year deadline, errors concentrated in question wording, review-tool churn, cost and suite time. *Moderate.*
4. **Few fixes survived intact.** The root-cause analysis, pressure test and source-coverage checks (T-084–T-090) did, which is the clearest case of a feedback loop working. The central integrity-plan fixes were softened within days or weeks: human reading became optional after 2 days, and the second model family became optional after 11 days. The 2026-10-21 cost rule was reversed on 11-03. The question-structure design was superseded about 8 hours after approval (11-06). *Strong as observation; the reasons are discussed below.*
5. **Owner decisions rarely held work up for long, and most were rubber stamps.** Every per-stage decision batch with a recorded outcome (Stages 15, 16, 18, 19, 20, 21, and NY Parts B/C) was answered "all recommended accepted". The decisions that actually changed direction were frame-level: goal, verification regime, cost, human labour, target year, personal-data rule. Each was made reactively, after an agent-written evaluation, rather than up front. *Strong as observation; moderate as interpretation.*
6. **The documentation became a real burden** (about 148k words of planning-layer prose, 32 "supersede" markers, a 640 KB bug inventory, and stacked amendment headers). Its authority now conflicts. `TASKS.md` and the backlog plan both say the backlog plan controls sequencing and that coverage expansion comes last. That plan has been stale since 11-04, while the project went on to NY (11-04/05) and the web UI (11-06), which it ranks last or does not mention. `CLAUDE.md` does not mention the backlog plan at all. *Strong.*

Bottom line (interpretation, moderate credence): there was a coherent vision at two points, 10-13 and, in a different form, 10-16. Between 10-16 and 11-07 the strategy was revised reactively by appending plan documents rather than holding one roadmap. The work was not chaotic in the sense of random. It was well recorded and self-correcting. It was inefficient in a specific, nameable way: it scaled scope before designing the verification, cost and owner-attention model that the larger scope needed, and then paid for that design in instalments.

---

## 1. The original plan (2026-10-13) and what survived

### 1.1 What it was (observation)

- `d3f06cb3` (10-13 22:54) added `research/` (six web-only reports and a synthesis), `spec/spec.md` (281 lines) and `spec/design.md` (217 lines). `f6504260` added `HANDOFF.md` ("begin the build").
- **Scope (spec 2):** "One return: a US resident individual with wage income from two employers, interest, dividends and stock sales." A list of about 17 forms and worksheets, an explicit refusal list (2.2) and non-goals (2.3), which included state returns.
- **Product framing:** "The durable asset is the formalization … The interview tool is the first client."
- **Verification (spec 3, 6):** ten evidentiary requirements. Evidence classes A (official), B (human hand-work), C (independent calculator) and D (property). Lean proofs of atom properties, a mutation score and whole-return differentials against two calculators. **Spec 6.4 already required interview checks:** "same answers always give the same return, regardless of order"; "no question is asked whose answer cannot affect a reachable line."
- **Stage structure (design 5):** Stage 0, ground the premises. Stage 1, a format spike, with a stop condition: if more than one line in eight needs `opaque`, reconsider the atom language. Stage 2, an architecture test (W-2 collections, a refusal gate). Stages 3–4, forms. Stage 5, whole return. Stage 6, TY2026 as a reviewed diff. Every stage had a "Done when" that a third party could run.
- **Working method (HANDOFF.md, "How to work with me"):** stop at the end of each stage and at any decision with more than one defensible answer. "Keep the work at a size I can check. I have to be able to vouch for what is produced." An intent readback before Stage 0. Hard constraints included "Never read the owner's personal tax documents."
- **A warning that proved prescient:** "Nearly every tax fact in `research/` is unverified testimony … Do not encode any line from memory."

### 1.2 Execution against it (observation, from git)

| Stage | Commit | Date |
|---|---|---|
| 0 premises | `198610c0` | 10-13 |
| 1 format spike | `919322a2`, `bd35a5ce` | 10-14 |
| 2 architecture test | `b8cd3e6e` | 10-14 |
| 3 sales | `30b5ed14` | 10-14 |
| 4 remaining forms | `4e62fc71` | 10-14 |
| 5 whole return | `8417477f` (56 files, +18.8k lines) | 10-15 |
| 6 TY2026 | not done as a stage; became T-045 year tooling (done 10-21, `b2b79b16`), `docs/ty2026/` (11-04, `d6017626`) | — |

Stages 2–4 were committed on the same day. It is hard to square "stop for my review at the end of each stage" with three stage commits in one day. Either the owner reviewed quickly or the stop boundaries were thin. I could not determine which from documents. `HANDOFF-STAGE-2.md` was written retroactively on 10-16 (`9d36338f`, "Add the Stage 2 handoff document referenced by the project index").

### 1.3 What survived (observation)

**Survived, and still the backbone:**
- forms as data with citations;
- the closed atom vocabulary (still "frozen"; an owner decision on 11-04 kept `bracket_schedule`);
- integer cents and no floating point;
- the CLI as the backend (the web UI is a client of `main.js serve`);
- the Lean reference evaluator agreeing with the TypeScript one;
- mutation scoring;
- evidence classes, extended with M, R and H;
- refusals with citations;
- premise maps before each stage (`research/premises/stage*.md` plus verification files).

**Rewritten on day 3 (10-16):**
- the product goal;
- human reading, replaced by model independent construction (spec requirement 11, spec 6.5);
- class M added;
- the Lean checker soundness proof dropped.

**Abandoned or relaxed later:**
- **The stage model itself.** After Stage 21 (10-29) there are no more numbered stages. Work is organised by dated plan documents, "packages" (P0–P6), "lanes", "rounds" and T-numbers. `design.md` section 5 still ends at "Stage 9 onward. Coverage" (checked against the current file). It describes none of the integrity, hardening, backlog, release or gates phases.
- **The personal-data constraint.** The original rule was "Never read the owner's personal tax documents." The web UI design (`docs/2026-11-06_web_ui_design.md`) says the owner's answer logs "hold real amounts … and agents may read them during the pilot (2026-11-06; supersedes the 2026-11-04 'agents never read the owner's data')". This was an owner decision, so it is legitimate, but it reverses a hard constraint from day 1.
- **"State returns" as a non-goal.** NY was restored as intended on 10-19 (`2587c1b4`) and built on 11-04/05 (`bdac4121`), recorded as an owner exception in spec 2.3.

**Rediscovered:** the 11-06 formal-gates design rules ("the same answers in any order give the same values"; "only the formal model can make a question disappear", `docs/2026-11-06_formal_gates_design.md`) restate spec 6.4 from 10-13 almost exactly. This is interpretation (moderate): the original design was sound on the interview layer, and the project departed from it in practice for about three weeks. The project evaluation (10-22) found 83 steps for a simple return, and the question-structure design (11-06) found 165 questions, 142 of them answered no, zero or none. Then, on 11-06, the project re-derived the original rule at higher cost, after building an interview-layer topic system that an independent review found had 43 problems, 16 of them high.

---

## 2. The arc of replans

Each row gives the trigger, the diagnosis, whether it was foreseeable from the design in force at the time, and whether the fix held. Dates are first commits.

### 2.1 Spec amendment: product goal and independent construction (10-16, `7b60e465`)
- **Trigger:** the proof of concept was done (10-15). The commit was co-authored by Claude Fable 5.1, which suggests an owner session with the stronger model.
- **Diagnosis:** the product should serve most filers. The tool "is built largely by language-model agents, so it cannot be trusted because of who wrote it." No human reading is claimed; trust comes from independent constructions.
- **What it added:** design Stages 7 (integrity stack), 8 (household architecture test) and "9 onward" (coverage, in prevalence order). Spec 6.5 states the shared-English blind spot itself: "The shared blind spot of every model-driven check is that it reads the same English. The engine differential is the only check against a shared misreading."
- **Foreseeability of what followed:** the amendment changed the goal by roughly an order of magnitude (from about 17 forms to dozens of forms over seven coverage groups). It did not revise:
  - stage size or review boundaries;
  - owner capacity ("a size I can check");
  - the cost of running every review on every form;
  - the fact that every construction was one model family;
  - the interview layer's verification.

  Each of these later became its own replan. *Interpretation, moderate:* the 10-16 commit is the point where a real redesign was due and only a partial one was done. The verification rescoping was serious; the process rescoping was absent.
- **Held?** Mostly. The goal held and grew (10-18 "all returns", `d99988aa`; 10-21 "80% the first coverage goal, 95% the target", `b9be1462`). Independent construction held but was amended twice (2.3, 2.4).

### 2.2 Coverage measurement and goal escalation (10-18, Stage 12 handoff, "The roadmap changed this session")
- **Trigger:** an owner decision during Stage 12.
- **Change:** coverage of all individual returns, measured against IRS Statistics of Income tables plus PolicyEngine microdata (`tools/coverage/estimate.py`). Estimated coverage after Stage 12 was 33.9% (range 20.9–41.9%). Stages were ordered by greedy coverage gain.
- **Assessment:** this gave the project a measurable objective, which counts against the "chaotic" thesis. It also set coverage percentage as the visible scoreboard while the evidence base was still one model family. The 10-22 evaluation measured the consequence: 68.6% coverage estimated against 13.1% of computed lines with any outside-family assertion (198/1515 on 10-24). *Interpretation, moderate:* choosing coverage as the metric pulled effort toward breadth just before the integrity audit.

### 2.3 Project evaluation and integrity plan (10-22, `a946fae5`)
- **Trigger:** an "outside-eye" evaluation in an owner session with Claude Fable 5.1 (`docs/2026-10-22_project_evaluation.md`). Two audit sessions then drafted the plan adversarially (`docs/2026-10-22_integrity_plan.md`, v7).
- **Diagnosis (evaluation, "Flaws worth treating as serious"):**
  1. The fixtures mostly pin the evaluator to itself (about 854 of 1,034 cases are synthetic regression).
  2. Mutation equivalence is an unproved escape hatch (129 of 149 survivors argued in prose).
  3. TY2025 can no longer be filed on time.
  4. The legal position is unreviewed.
  5. Vouchability: "the owner vouches for the checking regime, not the encoding … defensible only if the regime's independence is real."
  6. Evidence accounting drifted from the spec (class M missing, Lean agreement labelled C).
- **Foreseeability (my reading, moderate-strong):**
  - Items 1, 5 and 6 were visible from spec 6.1/6.5 and the 10-16 amendment's own blind-spot paragraph.
  - Item 3, the deadline, was knowable on 10-13: the extended TY2025 deadline was 10-15. The original plan already said "Stage 6. Tax year 2026", yet coverage growth went ahead on TY2025.
  - Item 4 was named in spec 11 (open items) from the start.

  None of these was new information on 10-22. What was new was that someone measured them.
- **Fix:** Phase 0 (honest reporting, the scoreboard "share of computed lines with at least one outside-family assertion"). Phase 1 (human reading packets, the DeepSeek transport, four engines, blind whole returns). A stop rule: coverage paused on value errors. The stop rule fired the same day with BUG-0094, 0096 and 0097, and "the reading list was doubled" (`HANDOFF-INTEGRITY.md`, "Stop rule").
- **Held? Partly.**
  - Phase 0 held.
  - The human-reading component was dropped within 2 days (2.4).
  - The second family was downgraded to optional on 11-02 (`804cb65c`, CLAUDE.md: "The required review family is Claude … `deepseek-flash` and `gpt-6-astra` are optional peer families").
  - The cost data later recorded DeepSeek transcription as 77% model error and "1 bug in 1,488 rulings all-time" (`docs/2026-11-04_process_optimization.md` item 7). DeepSeek class M, by contrast, "supplies all 32 class-M-only mutation kills".

  *Interpretation, moderate:* the integrity plan's diagnosis was right. Its main remedy, second-family transcription review, had a low yield per call for transcription and was quietly scaled back. Nothing in the document trail re-examines the shared-reader problem the plan was built to solve. As far as I can tell from documents, the trust claim's reliance on the second family weakened without the plan being amended. I did not check README or TRUST.md wording for this.

### 2.4 Validation policy (10-24, `735e6442`)
- **Trigger:** the owner's labour. Owner feedback that "one verdict was overwhelming" turned item 2 into 14 one-at-a-time questions. The owner completed them (10 MATCH, 3 MISMATCH, 1 UNCLEAR) and then "approved removing the remaining mandatory packets and the ten-ruling sample". Git shows a 47-hour commit gap before `735e6442` (10-22 → 10-24 21:17), the longest in the project. It coincides with the human-packet period, which is consistent with, but does not prove, work waiting on the owner.
- **Diagnosis:** a recurring human labour commitment is not sustainable. Engineering should not wait on it.
- **Foreseeability:** high. HANDOFF.md (10-13) already said "Keep the work at a size I can check", and the 10-16 amendment had already removed human reading as a requirement. The integrity plan reintroduced it as a gate, including automatic doubling of the reading list, and it was removed again two days later.
- **Note against my thesis:** the 14 human answers produced 4 non-MATCH verdicts. All were judged to be presentation and legibility problems, not value errors (`reviews/2025/human_findings.md`; BUG-0128). That is a high hit rate for legibility, which matters for vouchability (QMS 5.8), and it was the cheapest evidence the project ever got. Dropping it was a capacity decision, not an evidence decision.
- **Held?** Yes. Human evidence stays optional to date (CLAUDE.md). The policy also gained the model-authority ranking (owner, 11-01).

### 2.5 Plan revision (10-26, `4d8e51dd`)
- **Trigger:** measured. "Between 2026-10-24 and 2026-10-26 nearly all work went to item 1.3 … Of BUG-0129 to BUG-0146, one entry (BUG-0138) changes a tax value; the rest are defects in review tooling. The scoreboard stayed at 209 of 1,515 … Each checker change made recorded reviews stale, which required fresh requests, which exposed the next checker gap." 622 source disagreements were awaiting rulings.
- **Diagnosis:** a review-tooling treadmill. This is the single clearest self-diagnosis of inefficiency in the corpus.
- **Fix:**
  - A: adjudicate disagreements by execution;
  - B: freeze the review tooling, and change it only on a concrete wrong value;
  - C: parallel engines, blind returns, the TY2026 rehearsal;
  - D: a gate for resuming coverage;
  - E (10-27): a greedy route to 80% (Stages 20, 18, 19, 21).
- **Foreseeability:** moderate. The design put review logs under subject hashes, with "logs go stale with what they judged" (T-044, 10-21, `8c8ede84`). Combined with a changing checker, staleness cascades are predictable.
- **Held? Partly.**
  - Gate D was met on 10-27 and the coverage route ran to 82.2% by 10-29, so the revision worked on its own terms.
  - The tooling freeze eroded. Many review-tool and prompt-policy changes followed:
    - `source-only-computation-v3` (11-03);
    - line-scoped reviews (T-219, 11-04);
    - wording-blind subjects (11-05);
    - a scoped catalog.
  - T1 "review tooling" is the third-largest bug class in the root-cause analysis (27 entries, 0 value-changing).
  - Some of these changes were justified on cost grounds and introduced migrations ("no-call migration") to avoid global re-review. The owner's 11-03 rule ("applies prospectively") is in effect a refined, cost-aware freeze, so the 10-26 diagnosis was eventually built into standing rules.
  - The revision was superseded for execution order on 11-01.

### 2.6 Root-cause analysis (10-29/30, `2ca33119`) and mitigation pressure test (10-30, `0fd59d31`)
- **Trigger:** Stage 21 reached the first coverage goal (82.2%, `a428e8b`). The owner then directed hardening (`HANDOFF-HARDENING-1.md`).
- **Diagnosis:** of 210 bugs, 68 change values. The largest value class is **Q, question and screen wording that diverges from the source** (30 entries, 26 V), then L (misread rules, 28 entries, 18 V). "Fixtures and the generator supply answers directly, so wording never moves a tested value." The pressure test reframed the classes by cause:
  - R1, scope-filtered omission (clauses inert in the current slice that went live when scope grew);
  - R3, governing text outside the cited locus;
  - and others.

  26 of 68 V entries were caught a stage or more late.
- **Foreseeability (moderate-strong):** the verification stack was designed around arithmetic (Lean, mutation, engine differential, class M) because research found no official worked values. The error mass turned out to be in reading and asking. Spec 6.4 had named interview properties but none checked wording against source. R1 is a direct consequence of growing scope one slice at a time: the staged-coverage strategy itself manufactures this bug class. Both points could have been anticipated at the 10-16 pivot. Recognising them after 210 bugs is good, and late.
- **Fix:** T-084–T-090, ranks 1–6 and 9 of the pressure test, were implemented by 10-31. Examples are the instruction-section citation check, the operand check, the sign rule, the standing screen review and the standing completeness review (`84fa3309`, 10-31: "BUG-0211 to BUG-0260; standing completeness review (T-090)").
- **Held? Yes.** This is the best example of a replan that stuck. The 11-04 process document independently reports that "screen and completeness reviews have the best yield", and CLAUDE.md records that as owner policy. *Strong.*

### 2.7 Tech-debt audit and temporary backlog plan (11-01, `55cb9f1c`)
- **Trigger:** accumulated lows and baselines. HARDENING-1 lists 736 baseline entries and "56 forms never completeness-reviewed". An external audit (`docs/2026-11-01_tech_debt_audit.md`) appeared untracked mid-session; the archive says "Not mine, untracked, leave it alone … ask the owner". Its findings: 37 claims, 7 bugs, 4 evaluators or AST expanders, 13 AST walkers, and a new input touching 5 subsystems.
- **Diagnosis:** a finite hardening backlog should be cleared in packages P0–P6, with coverage expansion last (P6).
- **Assessment of the audit:** three Luna agents checked it and found several claims materially inaccurate. Examples: "Audit's operand examples are materially inaccurate"; "Blanket zero-self-tests claim false." The memo-alias bug (BUG-0287) and others were real. *Moderate:* this was a sensible "verify before acting" treatment. Note that Luna is ranked "mechanical or advisory only" in the owner's 11-01 model ranking, yet it was used for this judgement-heavy verification on the same day.
- **Held? No, as a coordinating document.**
  - The package tracker was last updated around 11-02/11-04 (`0c43e49e`). F1 still reads "Pending" although the 11-03 handoff says the F1 batch was integrated.
  - The retirement checklist is entirely unchecked.
  - The document says it "supersedes earlier execution orders" and `TASKS.md` line 3 still names it "Current execution order … Coverage expansion is last."
  - Since then: NY, which is state coverage expansion, landed 11-05 as an owner exception; the web UI pilot was prioritised "before coverage expansion resumes" (handoff 11-05); formal gates followed on 11-06/07.

  The plan was effectively abandoned without being retired, which its own rules forbid ("Do not preserve this entire tracker as another historical handoff"). *Strong as observation.*

### 2.8 Cost decisions (11-03) and process optimisation (11-04 → committed 11-05, `bdac4121`)
- **Trigger:** cost visibility. CLAUDE.md on 10-21 (`8c8ede84`) said: "Paid model calls … are part of the work. Do not weigh their cost, ask before running them, or hold work back to save it." On 11-03 (`465bcfc7`) this was replaced by: "Use inference only where it adds evidence."
- **Diagnosis (process optimisation):**
  - 44% of Claude review spend went to an unused prompt cache;
  - transcription reviews cost $122 for 0 findings in one 13-hour window;
  - `sales` was reviewed 8 times in one day;
  - 59 of 61 agent runs were Opus despite the 11-03 "Sonnet for mechanical" decision;
  - check-all ran 20+ minutes per bookkeeping commit.
- **Foreseeability:** high. Every review-per-change on every form under 2–3 families is a cost multiplier set by the design, and the 10-21 rule turned off the feedback signal. Logging costs (`costs.jsonl`) started only around 11-03/04, the third week. A cost model built in at 10-16, when the review regime was designed, would have had three weeks of data.
- **Held?** Yes, so far. Items 1–3 and 9 landed (`ce1e69a`, A/B cost $2.75, prompts 33–40% cheaper with identical verdicts). Package B was redesigned into release gating. The process document shows the same pattern as the rest of the arc: a sharp measured diagnosis, written by a separate analysis session for "the coordinating session", with three open owner decisions.

### 2.9 Release-gated check-all (11-05, `e2adfe68`)
- **Trigger:** a 38-minute full check-all. "`main` went 6.5 hours without a push." The suite took about 15 minutes on 10-31 (HARDENING-1) and 38 minutes on 11-05.
- **Fix:** fast, docs and full tiers, with a release at session end. It was approved, and the first release `r2026.11.06.1` was made.
- **Foreseeability:** high. The commit guard requiring a green full suite on the exact tree came early (Stage 8 handoff, "next, the commit guard"), and suite time grew with every check added in each correction phase. This is a predictable side effect of choosing "every check on every commit" as the integrity mechanism.

### 2.10 Web UI, question structure and formal gates (11-06)
- **Trigger:** the product layer was the "least advanced" part of the project, flagged on 10-22. The web UI design came at 08:08 (`5d0d66e8`), the question-structure design (T-251) was approved at 13:02 (`a68b8dfa`), and the formal-gates design at 20:57 (`3c1e5d17`).
- **Observation:** T-251's owner decision "Implications live in the interview layer, as reviewed data" was reversed about 8 hours later by formal-gates rule 1, "All tax logic lives in the formal model. The interview gathers facts …". The reason given was that an independent review found 43 problems (16 high) in the T-251 layer. The T-251 branch "is superseded and stays unmerged" (HANDOFF-NEXT-SESSION top entry).
- **Assessment:** the independent review caught a design error before merge. That is the process working, which counts against the chaos thesis. But the error was a departure from spec 6.4 and from the project's own principle that tax logic is cited data. A design readback against the spec should have caught it before the build.
- **Decisions revisited:**
  - Stage 15 owner question 1 (10-22): keep the Form 8880 contributions-first stop order, or test AGI first. Recommended and accepted: keep. Reversed on 11-07 (`2f3460eb`, "Form 8880 eligibility AGI-first").
  - Form 8889 got a coverage question first (`d563b283`).
  - Current open decision 1 says the owner's AGI-first order fails 7 recorded fixtures.

  *Interpretation:* stage-time decisions were made under a "printed-order" frame. Once interview ergonomics became a goal, they reopened.

### 2.11 The arc in one table

| Date | Document | Trigger | Foreseeable from the plan in force? | Held? |
|---|---|---|---|---|
| 10-16 | spec amendment | proof of concept done | n/a (owner strategy) | goal yes; verification amended twice |
| 10-18/21 | coverage goal 80/95% | owner | n/a | yes (82.2% reached 10-29) |
| 10-22 | evaluation + integrity plan | outside-eye audit | mostly yes (blind spot named in spec 6.5; deadline knowable) | Phase 0 yes; human reading no (2 days); second family weakened (11-02) |
| 10-24 | validation policy | owner labour | yes ("size I can check") | yes |
| 10-26 | plan revision | tooling treadmill measured | moderately | route yes; freeze eroded, later re-encoded as cost rules |
| 10-29/30 | root-cause analysis + pressure test | goal reached, hardening | partly (wording class, slice-filtered omission) | yes (T-084–090) |
| 11-01 | backlog plan | accumulated debt, audit | yes | no; stale since about 11-04, unretired |
| 11-03/04 | cost rules, process optimisation | cost visibility | yes | yes so far |
| 11-05 | release gating | 38-minute suite | yes | yes so far |
| 11-06 | question structure → formal gates | product layer | yes (spec 6.4) | first design reversed same day; second in progress |

---

## 3. How work was staged and delegated

### 3.1 Stage size and acceptance (observation)

- **Stages 0–5:** each had a "Done when" in design 5 that could be checked. They were finished in about 2 days. Commits were large: Stage 5 was 56 files and +18.8k lines.
- **Stages 7–21 (10-16 → 10-29):** each handoff has a fixed shape:
  - Scope, usually "owner-confirmed";
  - Sources archived;
  - How it was built;
  - Findings, with BUG ranges;
  - Evidence (fixtures, mutation score, reviews);
  - Open for the owner;
  - Facts a fresh session needs.

  Acceptance became "passes the Stage 7 checks", meaning the standing regime, not a stage-specific criterion. From Stage 18 on, each stage starts with a premise map, an independent verification of that map, and a decisions file (`research/premises/stage{16,18,19,20,21}*.{md,verification.md,decisions.md}`). This is a disciplined template. *Strong.*
- **Pace:** 15 coverage stages in about 13 days, some of them two per day (Stages 15 and 16 both on 10-22, alongside the integrity Phase 0 and Phase 1 commits). Stage 10 handoff: "the owner's overnight queue: small fixes, Lean proofs, T-019, then the next coverage stage". So, from Stage 10, unattended overnight runs of multiple items replaced the "stop at the end of each stage" boundary.
- **After Stage 21:** there are no stages. The work units become:
  - plan packages (P0–P6) and form "passes" or batches (F1–F5);
  - "rounds" of review (round 2: $41.12, 90 calls; round 3: $36.85, 70 calls);
  - parallel cloud or worktree "packages" ("eight parallel packages", `0a43f158`, 536 files, +976k/−416k lines, mostly generated);
  - "lanes" (gates lanes A–D, 11-07).

  Acceptance becomes "exact tested tree green in its tier, all medium or high findings resolved, the round finds only lows".
- **Review boundary:** the original rule "stop for my review at the end of each stage" turned, by 11-04, into "Decisions taken under the standing instruction (Elliot can reverse)" (HANDOFF-NEXT-SESSION, round 2 entry) and "My own choices, not explicitly ruled by the owner; tell them" (HANDOFF-T091). The validation policy (10-24) formalised this: "owner decisions are reserved for substantive scope choices or ambiguities requiring owner judgment, not routine work."

*Interpretation (moderate):* the move from human-reviewable stages to agent-reviewed rounds was a deliberate adaptation, owner-approved, to a scope that no longer fit human review. The cost is that QMS 5.8 / HANDOFF "size I can check" vouchability went from reviewing the work to reviewing summaries of the regime. The 10-22 evaluation said so ("the owner vouches for the checking regime, not the encoding"), and it has not been revisited in the documents since.

### 3.2 Owner decisions: how they were requested, and how they were answered

**Per-stage decision batches (observation):**

| Batch | Size | Outcome recorded |
|---|---|---|
| Stage 14 owner rulings | several, including a 3-option Form 4562 depth choice | individual rulings; T-041 "accepted six … the seventh became T-043" |
| Stage 15 "Open for the owner" | about 14 numbered questions | "all recommended answers below accepted" (10-22) |
| Stage 16 | 25 questions (D1–D14 in the decisions file) | "all recommended answers accepted" (10-22) |
| Stage 18 | 9 decisions | "all recommended, 2026-10-28" |
| Stage 19 | 9 | "all recommended, 2026-10-29" |
| Stage 20 | 6 | "all recommended, 2026-10-27" |
| Stage 21 | 10 | "all recommended, 2026-10-29" |
| NY batch 1 | Parts A–C | Part A answered (answers not recorded); B and C "accept all suggestions" (11-04) |

I could not determine the outcome for Stages 8–13. Those handoffs record "owner-confirmed" scope but not batch outcomes in the same form.

**Blocking duration.** Batches for Stages 15/16 and 18–21 were answered on the day written or the next day. Mid-session scope choices, such as the household completeness choice on 11-01, were answered within the same day. The longest visible stall is the 47-hour gap during the human packet (10-22 → 10-24). I could not determine wall-clock owner latency more precisely; handoffs do not timestamp questions.

**Decisions currently waiting** (top of `HANDOFF-NEXT-SESSION.md`): 6 items.
- Item 1 (partial fixtures against nested gates) explicitly "blocks the G2 leak rewrite and every gate round".
- Item 2 asks whether to adopt, partly adopt or drop a held branch of three commits.
- Items 3–6 are small.

Earlier entries show 3 open process-plan decisions (11-04) and the "last question … unanswered at close" in HARDENING-1. Dated owner-decision mentions cluster on 10-22 (7), 10-30 (8), 11-03 (7) and 11-04 (11) (crude grep count of "owner … 2026-xx-xx" strings across the planning docs). The clusters line up with the replans.

**Characterisation** (interpretation; credence moderate-strong on the first two points):
- **Micro-decisions** (tax readings, stop orders, refuse versus compute) were asked often and accepted as recommended almost 100% of the time. This shows either good recommendations or decisions the owner could not cheaply second-guess. The 10-22 evaluation's phrase "25-question decision batches per stage" suggests the latter is at least partly true. Either way, the batches cost owner attention without changing outcomes. *Counter-evidence:* they did create an owner-approved record, and some were revisited later (Form 8880), which suggests the owner did engage.
- **Frame decisions** were never put up front as a batch. They were made reactively, each after an agent-written evaluation or measurement:
  - the product goal (10-16);
  - the coverage metric (10-18);
  - whether human reading is required (10-22 and 10-24);
  - which model families count (10-22, 11-01, 11-02);
  - cost (10-21, reversed 11-03);
  - the target year (TY2026 per the 10-26 plan revision, while the 11-06 pilot runs on TY2025);
  - personal data (11-06).

  These are the decisions that changed direction, and each reversal came with re-work.
- **Operational decisions** (tooling adoption, test policy) accumulate as "decisions waiting" lists at handoff boundaries. They are increasingly technical (cache soundness, partial-fixture authority) and hard for a non-programmer owner to judge. Agents increasingly take them "under the standing instruction" with reversal rights.

---

## 4. Recurring themes across handoffs

Observation, with counts where cheap. Counts are crude greps over `handoffs/*.md` plus `HANDOFF-NEXT-SESSION.md`.

1. **Staleness and invalidation cascades.** "stale" appears 39 times. Examples:
   - T-044 (10-21) made logs go stale with their subjects;
   - the plan revision (10-26) diagnosed the cascade;
   - P0 (11-01) found that adding two f1040 refusals pulled 55 untouched forms out of baseline;
   - wording-blind subjects (11-05) fixed another source of it;
   - open decision 4 (11-07) is about stale optional-family logs.

   This is a structural cost of the "review logs bound to subject hashes" design. It was fixed piecemeal at least four times.
2. **New-input ripple.** "A new input ripples to five places … (missed three times)" (HARDENING-1, Facts). The tech-debt audit flagged the same thing. It was handled by tooling (T-150 `siblings.py`, `--input` ripple), not by redesign.
3. **Parallel agents and integration hazards.**
   - "Parallel agents worked well with disjoint file ownership; only one agent may own new inputs" (HARDENING-1).
   - Cloud session Claude logs had no local raw replies, so all were rerun (asset/sc pass, 11-02).
   - "agents in worktrees write paid-review outputs … into their own clone … a plain sync overwrote newer files once" (11-07).
   - The background-wait rule added to CLAUDE.md on 11-07 (`11883002`).
   - About 20+ leftover `worktree-agent-*` branches (from `git branch`).
4. **Suite time.** 15 minutes (10-31) → 22 minutes for mutation tier 3 alone (11-04) → 38 minutes full (11-05) → tiers → fast tier "about 11 min to about 5 min" (11-07, T-254).
5. **Usage and credit interruptions:** "session wound down for credits" (11-01), "Owner stopped work for usage" (11-01), GPT-6 Astra "57 of 61 calls failed on the usage limit" (11-04), "T-217 after 2026-11-06 15:49". These left uncommitted multi-step states that needed long restart handoffs (the household closure handoff is 167 lines).
6. **Rules added after incidents** (CLAUDE.md, dated):
   - 10-21, the inference-cost rule (later reversed);
   - 10-25, the current-execution pointer and T-062 hold;
   - 10-31, the handoff pointer and family definition;
   - 11-02, model-authority ranking and optional families;
   - 11-03, the inference-cost reversal and review-what-changed;
   - 11-05, model and class in every agent brief (T-241, after 59/61 runs were Opus despite the 11-03 decision);
   - 11-07, worktree data clone and carry-back (after the overwrite incident);
   - 11-07, background waits (pgrep self-match).

   Every behavioural CLAUDE.md rule after 10-21 is reactive. That fits QMS 5.6's own warning against the "anti-treadmill" pattern. Here some were turned into tools (`worktree_data.py`, `new_bug.py`, hooks), which follows the QMS priority order.
7. **Carried-over tasks.** TASKS.md has 28 open rows, and T-ids reach about T-254 with 226 rows in TASKS-DONE. The bug inventory reaches BUG-0456. Long-lived carryovers include:
   - T-094, the baseline burn-down (736 entries, from 10-30);
   - T-057, legacy render reviews;
   - T-012, product and legal;
   - T-034, prevalence;
   - T-011, final TY2026 adoption (on an external trigger);
   - Schedule E (Stage 17 premise map exists; deferred from 10-18 to "after the first goal", then to "P6", now still open as T-151).
8. **Scope that kept expanding:**
   - the goal (one return → most filers → all returns, 80/95%);
   - families (Claude → plus DeepSeek → plus GPT-6 → optional);
   - engines (2 → 4 targeted);
   - states (none → NY);
   - product (values sheet → web UI → filled PDFs, T-252);
   - review kinds (transcription, render, class M → plus screen, completeness, consumers, false-no gate review).

   Each correction phase added checks; few were removed. T-231 and T-196 were "closed by cost decision" (11-04), so some pruning did occur.

---

## 5. Did the documentation become a burden?

**Observation:**
- **Planning-layer volume:** about 148,000 words across `handoffs/*.md`, `docs/*.md` (top level), `HANDOFF-NEXT-SESSION.md`, `TASKS.md`, `CLAUDE.md`, `spec/*.md`, `PROJECT_INDEX.md` and `README.md` (`wc -w`). Plus `BUG_INVENTORY.md` 640 KB (456 entries), `TASKS-DONE.md` 133 KB and `PROJECT_INDEX.md` 47 KB. The process document itself says: "A tool that assigns the next id and appends would keep agents from loading them. Not verified that agents read them whole today."
- **Supersession layering:** 32 "supersed*" occurrences. Examples:
  - The integrity plan carries two stacked owner-amendment headers (10-24, 10-26) above its v7 text.
  - `2026-10-23_independent_validation.md` opens with "Superseding owner amendment" and then "Historical run record — superseded".
  - `HANDOFF-INTEGRITY.md` (574 lines) is a stack of "Current … after `<hash>`" sections, newest first, followed by "Historical execution record — superseded where noted".
  - The plan revision says it controls execution order over two handoffs, then itself says the backlog plan controls sequencing.
  - The archive (802 lines) holds 22 entries, several marked "(historical; superseded by the entry above)".
- **Authority chain** a fresh session must resolve today:
  1. CLAUDE.md;
  2. the top entry of HANDOFF-NEXT-SESSION;
  3. HARDENING-1 (standing decisions);
  4. the validation policy (controlling for validation);
  5. the plan revision (keeps evidence requirements);
  6. the integrity plan (amended twice);
  7. the backlog plan (claims sequencing control; stale);
  8. TASKS.md (status authority; header points to the backlog plan);
  9. spec and design (the design's build order is out of date).

  At least one live conflict exists: backlog plan and TASKS.md ("coverage expansion is last") against the actual sequence (NY, then web UI, then gates). Another is less direct: CLAUDE.md lists HARDENING-1 as holding the owner's standing decisions, but many later standing decisions (inference cost, formal-gates rules, model authority) live elsewhere.
- **Cost evidence:**
  - Handoffs repeatedly correct inherited claims: "Correction of an inherited ruling" (11-02); the "Triage sample check" correcting the household handoff's "~95 completed returns" to 309; "Older reported test results are historical evidence."
  - The documents themselves warn against trusting earlier documents. This is good epistemic practice (QMS AP-10) and a sign of a heavy carrying cost.
  - The P0 checkpoint appears in both the backlog plan and the archive, worded differently.

**Interpretation (strong):** yes. Documentation was both the coordination mechanism and a significant overhead. The style was to append a dated amendment that "supersedes" part of an earlier document, rather than edit one living roadmap. That preserves history, which git already does, at the cost of the current state being reconstructable only by reading the whole chain. Each new session (and each subagent) pays that cost. The "Temporary backlog plan" tried to break the pattern with its own retirement checklist, and it fell into it anyway.

**Counter-evidence:** handoffs were consistently specific. They gave commit hashes, measured counts, explicit "Verified vs inferred" sections and precise next steps. Sessions resumed reliably across many usage interruptions and different agents (Claude Opus, Fable, Codex, cloud sessions, Luna). Without the documents the project could not have coordinated so many short-lived sessions. The burden is in the layering, not in writing things down.

---

## 6. Evidence against my own thesis

**Against "inefficient or reactive":**
- The 82.2% coverage goal was reached in 16 days from the pivot. The stage template (premise map → independent verification → owner decisions → build → standing review) was consistent from Stage 15 to Stage 21 and NY.
- Every replan was evidence-led, with measured triggers (scoreboard flat, bug classes, cost ledger, suite timings), and most were owner-approved in session. That is not chaos.
- The bug root-cause analysis → pressure test → implemented checks loop is exemplary. It tested its own proposals against history (`git archive <fix>^`), rejected several ("What not to do"), and the resulting reviews became the highest-yield checks.
- Some "reversals" are correct learning: human reading optional, cost discipline, formal gates over the interview layer. Changing course on new evidence is conformance, not failure.
- Owner micro-decisions did not block much. Batches were answered within about a day.

**Against "the original plan would have sufficed":**
- The original plan was a proof of concept. It said nothing about how to scale to dozens of forms, and its human-reading requirement (step 4 "Record who did so") was not viable at the later scale, as the 10-24 retreat showed. A clearer upfront design would have had to be a different design, not the 10-13 one carried forward.
- The wording or question bug class may only have become visible once household rules (Stage 8+) were built. It is not certain it was foreseeable from a wage-plus-investments slice.

**For "inefficient", beyond what I have argued:**
- Two coverage stages were committed on the same day as the integrity plan that paused coverage (10-22: Stages 15 and 16, then `a946fae5`).
- TY2025 coverage kept growing for two weeks after the evaluation noted that TY2025 could no longer be filed and that each stage "will all need re-deriving".
- I could not find documentation of how much of the TY2025 work the TY2026 rehearsal carries over automatically; `docs/ty2026/ADOPTION.md` was not read in depth.

---

## 7. What would plausibly have been better (interpretation)

Ordered by how much re-work each would likely have avoided (my judgement, moderate credence).

1. **Treat the 10-16 pivot as a redesign point, not an amendment.** When the goal grew by an order of magnitude, write (and get owner confirmation of) a new design covering:
   - the verification regime across all layers, including interview wording, which is where 26 of 68 value bugs were;
   - the model-family policy and what the second family is for, since transcription review proved low-yield and class M high-yield;
   - a cost model and logging from day 1;
   - suite-time and commit-guard scaling (tiers);
   - what the owner can actually vouch for, and the human-reading budget, stated as a fixed small sample rather than a gate that doubles;
   - target year (TY2026) against development year.

   Most of the later replans are instalments of this document.
2. **One living roadmap, edited in place,** with history left to git. Dated analysis documents (evaluation, root-cause analysis, pressure test, process optimisation) are fine as inputs, but sequencing authority should live in exactly one file. Retire superseded plans by deleting them. The backlog plan's own retirement rule was right and was not followed.
3. **Interleave hardening with coverage instead of alternating phases.** For example, every stage closes with the screen and completeness reviews (now standing) and a slice-scoped R1 sweep ("clauses inert in this slice"). The pressure test shows 26 of 68 value bugs escaped their stage. Phase alternation (sprint → audit → pause) produced the 10-22 to 10-27 and 10-29 to 11-04 correction programs.
4. **Spend owner attention on frame decisions, not reading micro-decisions.** The 100% "all recommended accepted" record suggests the stage batches could have been agent-decided with a reversible log (the later "decisions taken under the standing instruction" model) from Stage 15 on. A short frame batch at each phase boundary (goal, metric, families, cost, year, data rules) would have surfaced the reversals of 10-21/11-03 and 10-22/11-02 sooner.
5. **Keep the original interview invariants (spec 6.4) as enforced checks from Stage 5.** The 11-06 formal-gates rules are those invariants. Enforcing them early would likely have prevented the T-251 detour and part of the Q bug class.
6. **Freeze review-subject and prompt policies early.** Design subjects as line-scoped and wording-blind from the start. The staleness cascade was fixed four times.

---

## 8. What I could not determine

- Owner wall-clock latency on decisions. Handoffs do not timestamp when a question was posed; I inferred from commit gaps only.
- Outcomes of the Stage 8–13 decision batches. Owner-confirmed scope is recorded, but there are no batch tallies.
- Whether owner review actually happened at each early stage boundary (Stages 2–4 on one day).
- Whether README or TRUST.md currently state the shared-reader limitation and the optional status of second families consistently with CLAUDE.md. Not read.
- The effectiveness of the TY2026 adoption path (`docs/ty2026/` not read in depth).
- Whether agents actually load the large bookkeeping files whole (the process document also could not tell).
- Content of the untracked `docs/2026-11-01_contributor_safe_gating_sketch.md` (no git history; not read).
- Cost and agent-token totals across the whole project. Logging starts around 11-03; this is in another investigator's slice.

## Files cited (all under `/Users/elliotmilco/Documents/GitHub/tax-formalization/`)
- `spec/spec.md`, `spec/design.md`, and `git show d3f06cb3:spec/*`, `git show 7b60e465`
- `handoffs/HANDOFF.md` (`git show f6504260:HANDOFF.md`), `handoffs/HANDOFF-STAGE-{2,7..16,18..21}.md`, `handoffs/HANDOFF-T091.md`, `handoffs/HANDOFF-HARDENING-1.md`, `handoffs/HANDOFF-INTEGRITY.md`, `handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md`, `handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md`
- `HANDOFF-NEXT-SESSION.md`, `TASKS.md`, `CLAUDE.md` (history via `git log -- CLAUDE.md`)
- `docs/2026-10-22_project_evaluation.md`, `docs/2026-10-22_integrity_plan.md`, `docs/2026-10-23_independent_validation.md`, `docs/2026-10-24_validation_policy.md`, `docs/2026-10-26_plan_revision.md`, `docs/2026-10-29_bug_root_cause_analysis.md`, `docs/2026-10-30_mitigation_strategy_pressure_test.md`, `docs/2026-11-01_backlog_plan.md`, `docs/2026-11-01_tech_debt_audit.md`, `docs/2026-11-04_process_optimization.md`, `docs/2026-11-05_release_gating_design.md`, `docs/2026-11-06_{formal_gates,question_structure,web_ui}_design.md`, `docs/ny/DECISIONS.md`
- `research/premises/stage*.decisions.md`, `reviews/2025/human_findings.md`
