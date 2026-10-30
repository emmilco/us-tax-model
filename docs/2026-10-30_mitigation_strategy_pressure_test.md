# Mitigation strategy pressure test — value-changing bugs (2026-10-30)

Purpose: decide the most effective and efficient way to reduce the bugs that put wrong tax amounts on returns, by
testing the proposals of `docs/2026-10-29_bug_root_cause_analysis.md` (section 4, "P1" to "P8") and the session's
candidates (A) to (D) against the inventory entries and against cheap read-only prototypes. Read-only work: no form,
fixture, review, tool, inventory or task file was changed; no model was called. Scratch scripts and their outputs are
in `/tmp/pressure-test/` (section 4).

Method, in the order required: all 68 entries of the prior report's Appendix B and about 40 near relatives were read
in full (list in `/tmp/pressure-test/phase1_notes.md`), the problem framing and my own strategies were written down
before section 4 of the prior report was read, and then every "would have caught" claim that could be checked
cheaply was checked: on the current tree, and on the tree just before the fix (`git archive <fix>^`) where the
buggy state was ever committed. Bias note: the candidate list (A) to (D) was in my brief, so I saw it before Phase 1.

Marking: **measured** = a prototype or a direct read of the source or the historical tree showed it; **inferred** =
my reading of the entry, not executed. The per-bug strategy table (`/tmp/pressure-test/matrix.py`) is my judgement
except where a cell is marked measured below.

## 1. How the problems are best expressed

### 1.1 What is wrong with the prior cut

The prior classes split mainly by **artifact**: question prose (Q), expression (L), shared input (U), stale
invariant (R). The artifact matters for *detection*, because it decides which oracle can see the defect. But it
does not say *why the author produced the defect*, and two pairs of the prior classes turn out to be the same
failure:

- **0195 (Q) and 0190 (R) are one failure.** In both, the cited sentence held the clause, and the author dropped
  it because that clause was inert in the slice at the time.
  - 0195: before the fix, `eic.us_home` cited "p. 42, Step 4, question 3", the very sentence that reads "and
    your spouse's if filing a joint return" (measured, `git show 34b2346^`). Married filing jointly was refused
    when the line was written in Stage 9.
  - 0190: `ftc.limited` cited "p. 25, Line 20". Schedule 2 line 1z was refused when the line was written.
  - 0047 and 0048 follow the same pattern. The source prints "younger than you (or your spouse if filing
    jointly)" (i1040gi p. 17) and "your spouse's Archer MSAs" (f8889 line 4) (both measured).
- **0153 and 0157 (U) belong with the months cluster 0014, 0017 and 0027 (Q).** The months question encoded one
  residency rule as a conclusion that the filer computes, and every later rule that read the answer inherited
  that rule.

The cut below is by **the relation between source and encoding that broke, and when it broke**. It is chosen
because each cause has its own cheapest prevention point.

### 1.2 The framing used here

| Code | Cause (what the author did) | V entries | Caught late (next stage or later) |
|---|---|---|---|
| R1 | **Scope-filtered omission.** The author read the sentence and left out a clause or operand that was inert in the current slice. Nothing recorded the omission, so it went live when scope grew. | 0001 (in part), 0047, 0048, 0051, 0053, 0058, 0072, 0084, 0190, 0195 (10). Latent precursors: 0007, 0035, 0062 | 0001, 0051, 0072, 0195 |
| R2 | **Lossy paraphrase of an anchored sentence.** The sentence was on the cited page and in front of the author, and the restatement dropped, widened or invented a condition. | 0013, 0018, 0020, 0029, 0045, 0067, 0070, 0085, 0119, 0189, 0197, 0205 (12) | 0067, 0070, 0119 |
| R3 | **Governing text outside the cited locus.** The rule sat in an exception paragraph, a definitions section, another line's instruction, an uncited page or another document. | 0014, 0023, 0027, 0028, 0030, 0087, 0095, 0097, 0159, 0165 (10) | 0095, 0097, 0159, 0165 |
| SCR | **Screens narrower than the lines they stand in for.** A set-coverage failure over the instructions of the gated lines. | 0004, 0005, 0006, 0008, 0010, 0032 (6); recurrences after T-008 under R1/R6: 0048, 0087, 0188, 0202 | 0032 |
| R4 | **One encoded element answers for several source definitions.** A conclusion is baked into an input or enum value, then read by a rule whose definition differs. | 0011, 0019, 0034, 0049, 0092, 0096, 0157 (7); also 0153 (N) | 0034, 0092, 0096, 0157 |
| R5 | **A limit across entries or years, or an entry-validity bound, not encoded.** | 0060, 0063, 0069, 0078, 0120, 0148, 0186, 0201 (8) | 0069, 0078, 0120, 0148 |
| R6 | **A change not carried to its siblings or targets.** Fixes: 0015, 0017, 0021, 0024, 0161, 0192. Decisions: 0036, 0188, 0202, 0203. | 10 | 0161, 0192 |
| R7 | **Arithmetic sign domain.** | 0094 (V); 0100, 0180 (N) | 0094 |
| G | **Refusal reach.** | 0088, 0147 | 0147 |
| other | Interpretation of proposed regulations (0163); mixed (0076) | 2 | both |

Totals: 68 V entries. 38 were caught in the stage that introduced them and 4 before commit. 26 were caught a stage
or more later (`matrix.py`).

### 1.3 Where the escapes are

The 26 late catches spread across all causes:

| Cause | Late catches |
|---|---:|
| R1 | 4 |
| R2 | 3 |
| R3 | 4 |
| R4 | 4 |
| R5 | 4 |
| R6 | 2 |
| R7 | 1 |
| SCR | 1 |
| G | 1 |
| other | 2 |

R2 is the largest class, but render review mostly catches it in stage, so most of what remains is late R1, R3, R4
and R5. Three facts shape the strategy:

1. **Several of the longest escapes need no reader at all.** BUG-0001's own label lists the addends. BUG-0165's
   instruction says "Include the amount shown on Form 8959, line 24". BUG-0094 multiplies a signed amount by a
   rate. Each is mechanically detectable from data already in the repository (section 4, measured).
2. **The prior report's "the citation selects the context" is half right.** For R3 it holds. For R1 and R2 the
   sentence was cited and still lost, so widening the context does nothing for them.
3. **R4 defects are created at one observable moment.** That moment is when a new rule in a different source
   section starts reading an existing input:
   - 0034: the EIC read `sa.age65`;
   - 0049: the CTC read the ODC question;
   - 0096: the EIC read `person.work_ssn`;
   - 0157: Form 2441 read `lived_half`;
   - 0092: Form 8889 read `f1040.status`.

   That trigger can be detected in a diff of the consumer graph.

## 2. Verdict per problem

### 2.1 R1 — scope-filtered omission. Verdict: **reframe, then a better approach** (it is not "stale invariants")

**Recommended strategy (three parts).**

1. **An operand check in `engine/src/check.ts`.** For a computed line whose label is the printed instruction
   ("Add lines …", "Enter the total of … lines …", "Subtract line X from line Y", "smaller of"), the line numbers
   in the label must equal the expression's operands, after helpers are resolved and printed markers normalised.
2. **A convention the check enforces: a refused operand stays in the expression.** It is carried as a reference
   to the refused line, or to a refused stub; it is not dropped with a note in the locator. Exceptions go in a
   rulings file with reasons.
3. **For prose:** every input carries a quote of its governing sentence, and T-072 makes those quotes verified.
   When a stage widens scope (a filing status, final returns, a newly computed line), a sweep lists every input
   whose quote mentions the widened concept but whose question text does not.

**Evidence.**

- The prototype (`operands3.py`, measured) flags **BUG-0001** on `cbabd7b^`: label "Add lines 1z, 2b, 3b, 4b, 5b,
  6b, 7a, and 8", extra operand 3a, missing 4b, 5b and 6b.
- It flags **BUG-0051** on `f16237f^`: `ssb.line6` and `sli.line3`, label "lines 11 through 20, and 23 and 25",
  operands 11 and 13. The miss sat there from Stage 11. Under the convention, lines 15 to 17 would have been
  present as refused operands, so Stage 14 could not have left them out.
- On the current tree it checks 204 lines and flags 31. About 10 of the flags are true dropped-refused operands,
  latent today and each guarded by a refusal, the BUG-0007 pattern:
  - `s3.line8`, where line 7 is replaced by `s3.zero`;
  - Schedule SE line 3 (1a and 1b) and line 8d (8b and 8c);
  - Form 7206 line 13;
  - `ssb.line6` and `sli.line3` (lines 12, 14 and 23);
  - `s8812.line22` (Schedule 2 lines 5, 6 and 13);
  - Form 8863 and 8880 Credit Limit Worksheets (Schedule 3 lines 6d and 6l).

  The rest are resolver artefacts of the prototype: cross-form helpers, worksheet markers and collection
  entries. TASKS T-002 ("line 1z: become the sum of lines 1a–1h when they come into scope") shows the project
  already keeps such omissions as prose memory.
- The prose half is not mechanically covered today. The 0195, 0047 and 0048 sentences contain the clause
  (measured). A spouse/joint sweep over current input quotes gives 6 hits in 541 inputs, all benign
  (per-person entries) (measured). The load is therefore small, but recall depends on quotes existing: 339 of
  541 inputs have a quote now (measured), and 0195's locator had none.

**Expected effect.**

- Prevented at authoring:
  - 0001: was latent from Stage 1, caught by engines on 2026-10-16;
  - 0051: caught by engines a stage late;
  - the 10 current latent sites.
- Caught when scope widens rather than later (inferred): 0195, saving about six stages (Stage 13 against
  Stage 19); 0047, 0048 and 0190, which were already caught in stage.
- Not covered: 0053 (`s8812.line21`'s label is a paraphrase, so no printed operand list existed, measured), 0058,
  0072 and 0084, which are partly covered at best.

**Cost.**

- Checker rule: about 1 day, using the canonical JSON and the existing printed markers.
- One-time ruling pass: about 30 lines.
- Quote requirement on inputs: about 200 inputs to quote, best done with T-072.
- Per stage: near zero for the check; the sweep is minutes per widened concept.

**Failure modes.**

- Labels that paraphrase instead of printing the instruction escape the check. Mitigation: the rule applies when
  `printed` is a line number, and the label must then be the printed text (helper lines exempt).
- Exception rulings rubber-stamped as "refused, fine". Mitigation: an exception must name the refusal that guards
  it, and the checker verifies that the refusal is declared on the line.

**Why this beats the alternatives.** The strongest alternative is the prior **P4, the line-profile diff at stage
close**. It catches what a static rule cannot, such as a line that first goes negative (0094) and remedy texts
naming a stale form. But it reaches 0051 only through a sibling-sum heuristic, and only after the omission is
already live. The prior report itself declines to stale on status widening (0047, 0048, 0084), which is exactly
where R1 bites. S1 prevents the defect at authoring at a fraction of the cost, and 0094 is covered more cheaply by
the sign rule (2.8). Keep P4's remedy-text part only if D-class drift matters; it is not value-changing.

### 2.2 R3 — governing text outside the cited locus. Verdict: **combine; the prior P1 is modified, and its 0095 claim does not hold**

**Recommended strategy, in cost order.**

1. **(a) Instruction-section citation check (mechanical).** A printed line whose citation names only the form
   face, where the archived instructions have a "Line N" section, must cite that section, or carry a ruling.
2. **(b) Supplied-input cross-reference check (mechanical).** For an input that stands for a printed line, scan
   its Line N section for "Form/Schedule X, line Y" references to lines the project computes.
3. **(c) Operative-sentence completeness review per implemented section.** An isolated model is given the whole
   instruction section a form implements, by heading range rather than by cited page, plus the documents it
   points to ("see Pub. 501"), and the list of encoded lines, screens and refusals. It lists only the operative
   rules ("can't", "must", "unless", "exception", "limited to", "treated as") that nothing encodes. Each claimed
   gap is adjudicated as in plan revision A.

**Evidence.**

- **0159 and 0165** both cited only "Form 1040 (2025), line 25b/25c" before their fixes (measured). Prototype (b)
  run on `f7d89e3^` flags `f1040.line25c` → "Form 8959, line 24" (measured), with 5 other hits in 56 inputs. All
  5 are benign: section mismatches or exclusion pointers, each ruled once.
- On the current tree, **164 printed lines** cite only the form face while the archived instructions have a Line
  N section (measured, `formface_all.py`; an upper bound for Schedules 1 to 3, whose headings share i1040gi).
  Examples are Form 8959 lines 1 to 24, Form 8960, and Form 1040 lines 10 to 37. TASKS T-069 is an
  adjudicator-found instance of the same gap (Schedule 8812 lines 4 and 6).
- A 4-section sample turned up one probable new gap (inferred, not verified against scope): Form 1040 line 26.
  The instructions divide joint estimated payments between spouses now filing separately, and the question says
  only "2025 estimated tax payments". The `f8889.line2` question already carried its instruction, uncited.
- **The prior P1 does not catch 0095.** The governing sentence ("You must enter each dependent's social security
  number", i1040gi p. 22) is on a page no form cited before the fix. The cited i1040gi pages were 14, 16 to 21
  and 23 to 35 (measured, `pages.py` on `0186a66^`). P1 scans only cited pages.
- **P1 does catch 0097.** The disallowance paragraph (pp. 40 and 46) is listed unanchored by the prototype
  (measured, `paracov.py`).
- Ruling load:

  | Scope | Paragraphs or sentences | Unanchored |
  |---|---:|---:|
  | EIC pages 40 to 48, all paragraphs | 129 | 82, with crude anchoring |
  | EIC pages 40 to 48, operative paragraphs only | — | 12, including both 0097 hits |
  | All 361 cited pages, all sentences | 13,050 | — |
  | All 361 cited pages, operative sentences | 1,670 | 1,446 not quote-anchored |

  An uncited page inside the dependents section (p. 22) is reached only if the unit is the section by heading
  range, which is why (c) uses heading ranges.
- **Byproduct (inferred, for the owner).**
  - The candidate live gap is on the EIC pages: "Adopted child … includes a child lawfully placed with you for
    legal adoption" (i1040gi p. 43; the same rule is in the dependents section).
  - The `dependent.relationship` value `child` lists "son, daughter, stepchild, foster child" and does not name
    an adopted child or a pre-adoption placement.
  - A filer with such a child might choose `other`.
  - Not checked against the interview help text.

**Expected effect.**

- (a) and (b): 0159 and 0165 caught at authoring, where they were long escapes (0165: present from the stage that
  added Form 8959 until UsTaxes found it on 2026-10-27).
- (c): 0097 and 0095 (inferred), and probably 0035 and 0148. These are the "no line cites it" defects, the class
  that only Direct File and adjudication have found.
- The exception-paragraph group (0014, 0023, 0027, 0028, 0030, 0087) was caught in stage by render once the
  reading-order text existed, so (c) would only move those catches earlier by a review round.

**Cost.**

- (a) and (b): about half a day for the checks. Citing the 164 lines and the roughly 70 form-face inputs takes
  about a day; the reruns are model calls, which CLAUDE.md says not to weigh.
- (c): a new review tool in the pattern of `screen_review.py`, about 1 to 2 days. Adjudication runs to tens of
  claims per form once, then only for the new sections of each stage.

**Failure modes.**

- (a) can be satisfied by citing a page without reading it. That is acceptable, because the point is to put the
  paragraph in front of render.
- (c) depends on model recall, which was not measured (section 5). Its claims can be rubber-stamped like any
  ruling. Mitigation: a "covered" ruling must name an existing line, gate or screen, which is mechanically
  checked.

**Why this beats the alternatives.**

- The strongest rejected alternative is the **prior P1 as specified**: a ruling for every unanchored paragraph
  on cited pages. It is deterministic and cannot be fooled by a model's recall. Against it:
  - it requires on the order of a thousand rulings even when restricted to operative sentences, and several
    thousand otherwise;
  - its measured unique value is 0097;
  - it structurally misses 0095;
  - a ruling pass of that size is exactly where rubber-stamping becomes theatre. Render's existing 800 rulings
    are overwhelmingly "project retained" (`render/*.rulings.json`, measured).
- **Candidate (C)**, citation coverage for questions, is subsumed. Requiring a question's citation to cover the
  exceptions of its sentence is (c) restricted to one heading, and the bugs it targets (0014, 0023, 0027, 0028)
  were caught in stage by render after T-022/T-025. It does nothing for 0195 (sentence cited, clause dropped) or
  0159 (instruction not cited at all).

### 2.3 SCR — screens narrower than the lines they stand in for. Verdict: **confirm the T-008 method; make it standing**

**Recommended strategy.** Run `tools/transcription/screen_review.py`, which today is a one-time tool, whenever a
screen's text, the set of lines it gates, or the citations of a gated line change. Mechanically, this means
subject-hash staling of screen-review records on the screen plus its gated lines.

**Evidence.** The one-time screen review found 25 screens in one pass (BUG-0032). Since then the same defect has
recurred in screens that the one-time pass never saw in their later form:

| Entry | Screen | Stage |
|---|---|---|
| 0048 | `f8889.unsupported`, spouse's Archer MSA | 13 |
| 0087 | `f8889.unsupported`, estate beneficiary | 16 |
| 0188 | `f8962.other`, lawfully present alien | 18 |
| 0202 | `f8889.unsupported`, withdrawal by the due date | 21 |

**Expected effect.** Those four would have been caught at the change rather than by adjudication (inferred; all
four were in fact caught in stage, so the gain is fewer adjudication rounds, not latency).

**Cost.** Low: a staling rule plus reruns.

**Failure modes.** Accepted WIDE findings accumulate. Keep the accept-with-reason ruling.

**Why this beats the alternatives.** Candidate (A) does not apply to screens: a screen is an enumeration of refused
situations, not a conclusion that could be factored. (c) in 2.2 would also find screen gaps, but the screen review
already has the right unit, the gated lines.

### 2.4 R4 — one input answering for several definitions. Verdict: **combine (A) targeted with (D) re-triggered; reject both as stated**

**Recommended strategy.**

1. **(D′) New-consumer check at stage close.** For every Bool, Enum or Count input that gains a direct consumer
   citing a different (document, page) section than its existing consumers, an isolated model is given the input
   question and each consumer's governing sentence. It answers whether that rule needs exactly what the question
   asks. Only "differs" verdicts are adjudicated.
2. **(A′) Facts, not conclusions, for a targeted set:** conclusion-style inputs that are read by two or more
   sections, or that carry enumerated exceptions, in the household and credit-eligibility domain:
   - relationship;
   - months and residency, with dates;
   - SSN card facts;
   - marital status as a fact;
   - TIN issued versus applied for.

   The facts must be precise enough. BUG-0019 is the warning: a predicate derived from whole-year ages was wrong,
   and the fix moved the other way, back to a conclusion question.

**Evidence.**

- **Candidate (D) as stated** (inputs whose consumers cite different documents) flags 127 of 548 inputs on the
  current tree, including `f1040.status` with 60 consumers. It **does not flag `person.work_ssn` on `0186a66^`**,
  the tree just before BUG-0096, because every consumer cites i1040gi (measured, `inputdef.py`).
- At the (document, page) level, restricted to Bool, Enum and Count inputs, it flags 68 inputs on that tree. These
  include `person.work_ssn` (0096), `person.age65` (0034), `dependent.months` (0153/0157) and `f1040.status`
  (0092) (measured).
- On the current tree, 29 inputs are both conclusion-style and read across two or more sections (measured,
  heuristic), for example `sa.dependent` (5 sections), `household.married` (4), `person.work_ssn` (7) and
  `eic.us_home` (2). A spot read of `sa.dependent`'s consumers found no defect: the EIC and dependents paths
  match the source structure.
- **Candidate (A)'s premise** ("many question-wording bugs are conclusion questions"):
  - Of the about 45 question-related V entries, about 24 are factorisable conclusions. Of the rest, 10 are
    screens, where A does not apply; about 9 are amount-content questions; and 2 are fact questions
    (inferred, `phase1_notes.md`).
  - Over all inputs, a keyword heuristic puts 112 Bool or other inputs and 56 amount inputs as conclusion-style,
    out of 541 (measured, heuristic, overcounts "qualified …" items).
  - The claim holds for household and eligibility, and not for screens or amounts.
  - The project's own fixes converged on A: 0049 split issued from applied; 0153, 0157 and 0158 added
    `born_died`, `placed` and `part_year_home`; 0034, 0096 and 0192 added their own inputs.
  - Fact-level encoding is also what let Direct File, a fact-dictionary oracle, find 0095, 0096 and 0097. Prose
    cannot be compared by any value oracle.

**Expected effect.**

- D′ at the Stage 9 boundary would have queued 0034 and 0096, and at Stage 11 or 15 0092 and 0157 (inferred).
  Those are four long escapes, 1 to 13 stages earlier.
- A′ removes the shared-conclusion mechanism for 0011, 0019, 0020, 0021, 0024, 0049, 0153, 0157 and 0192. It also
  moves the months-cluster rules (0014, 0017, 0027, 0029) into expressions, where the transcription comparison,
  Direct File, blind predictions and generated cases can see them (inferred).
- A′ does not by itself prevent an omitted exception. That becomes an expression bug instead of a prose bug,
  visible to more oracles.

**Cost.**

- D′: about 1 day of tooling, using the consumer graph, which the prototype builds from the YAML in seconds. A
  one-time pass over about 70 inputs and about 200 (input, section) pairs is model-drafted. After that, a handful
  of pairs per stage.
- A′: about 2 to 3 days to rework about 10 to 15 remaining household inputs (for example `dependent.us_half`,
  `dependent.citizen`, `dependent.tin`, `eic.us_home` and `f2441.nondependent`), with their fixtures and
  regenerated reviews. It adds interview questions.

**Failure modes.**

- D′: model verdicts of "same definition" accepted without reading the second sentence. Mitigation: the verdict
  must quote both sentences' defining phrases.
- A′: interview burden; reviews staled for the reworked forms (the BUG-0184/0192 deferral pattern shows the
  project avoids this); open-textured tests (support, material participation, main home) cannot be factored and
  stay as conclusions.

**Why this beats the alternatives.**

- The strongest rejected alternative is **(A) wholesale**: rewrite every conclusion question into facts. It would
  remove the most prose from reader-only checking. But about a third of the inputs are conclusion-style, many are
  irreducible legal standards, and its measured bug yield is concentrated in about 15 household inputs. It also
  does not apply to screens or amounts.
- **(D) as stated** is rejected on measurement: it is blind to 0096 and noisy elsewhere.

### 2.5 R2 — lossy paraphrase of an anchored sentence. Verdict: **confirm the existing readers; reframe (B)**

**Recommended strategy.**

- Keep both render families and execution-triaged adjudication. They caught most of R2 in stage, and the second
  family caught 0119 and 0120 that Claude accepted.
- Turn the session's blind answerer (B) into an **outcome-level, isolated-translation blind prediction**:
  1. scenario facts are written from the stage's exception and condition sentences (as Stage 21's E5 was) and
     expressed at document level (boxes, events);
  2. an isolated answerer with only the interview questions translates them into answers;
  3. the project's values are compared with the predictors' source-derived values.

  The only change to today's blind predictions is that the translator is no longer the author.

**Evidence.** I acted as the blind answerer on seven known-bug questions, using the old wording read literally
(measured as an exercise; biased, because I knew every bug; `blind_answerer.md`).

- **Answer-level comparison** (the answerer's answer against the generator's intended answer) flags 3 of 7:
  - 0067: double entry of a prize;
  - 0204: missing code options;
  - 0159: only if the fact sheet gives box numbers, which a generator working in the project's own concepts
    ("withholding on your Forms 1099: $2,000") does not.
- It **cannot** flag 0195, 0205, 0014 or 0119. Those are mis-specifications: the question faithfully conveys the
  author's wrong rule, so the "intended answer" carries the same error. For 0195 the generator cannot even express
  the deciding fact, because the spouse's home was not a project input.
- The claimed catch of 0205 therefore fails as (B) is specified. It holds only with a source-reading oracle
  deciding the correct exception amount, which is a blind predictor.
- Outcome-level comparison flags all 7, but only when the scenario contains the deciding fact.
- History supports both halves. Blind predictions found 0201 because E5 was built around the one-per-year
  sentence. They missed 0205 because E4 never stated how a birth distribution was spent, and the author did the
  translation. Stage 18's predictors "worked from the same screens" (0188).
- 0204's class is caught more cheaply by a trivial check: a question that names enum value ids must name all of
  them. On the current tree, the 11 enum questions that omit ids omit all of them (years, quarters, asset
  classes), so that check has no false positives today (measured).

**Expected effect.** It raises the yield of blind predictions on wording defects (0067, 0159-type, 0013/0018-type)
and keeps their existing yield on mis-specifications (0201) (inferred). R2 is not a latency problem today: 9 of
its 12 V entries were caught in stage.

**Cost.** One more isolated model per scenario. Scenario design from exception sentences is the real cost, about
an hour per stage.

**Failure modes.**

- Scenarios chosen from the author's own model of the rule reproduce the author's blind spots, and the scenario
  must contain the deciding fact.
- I am a model: my literal reading is not evidence of how another model or a filer reads.

**Why this beats the alternatives.** The strongest rejected alternative is **(B) as stated**, run over plain-language
fact sheets of generated returns. It scales to thousands of cases at no design cost. But generated returns live
in the project's input space, so the fact sheets cannot contain the facts the project failed to model, and the
intended answers inherit the author's reading. Its measured reach is the ambiguity minority of R2, not the
mis-specification majority.

### 2.6 R5 — limits across entries and entry validity. Verdict: **better approach** (not covered by any prior proposal)

**Recommended strategy.** A one-time and per-stage **limit-sentence worklist** over cited pages, with correct
multi-document locator parsing as `citations.py` already does. The phrases are "can't be more than", "limited to",
"not more than", "per calendar year", "for all of the businesses" and "the total … can't". Each sentence is ruled
to the cap, gate or aggregation that enforces it, which must exist.

**Evidence.**

- 65 such sentences on the 361 cited pages (measured, `limits.py`). Hits:
  - 0069, "300 square feet … for all of the businesses", i1040sc p. 10;
  - 0201, "one emergency personal expense distribution per calendar year", p590b p. 28;
  - 0148, "limited to the maximum dollar amount on line 1", i4562 p. 4.
- 0063's sentence ("the total of the amounts … on line 2 of all Form(s) 7206 can't be more than", i7206 p. 2) was
  missed only because the prototype attributed "i7206 pp. 1–2" inside another document's locator to the wrong
  document (measured; inferred hit with proper parsing).
- 0078 ("only the earned income from that business is considered for that plan") is not a limit phrase and is
  missed.

**Expected effect.** 0063, 0069, 0148 and 0201 at authoring (0069 and 0148 were late); 0120 and 0186 partly.

**Cost.** About half a day, plus about 100 one-time rulings, most of them a pointer to an existing gate; per stage,
about 5 to 15.

**Failure modes.** Phrase lists miss paraphrased limits (0078). Rulings that point at a gate which does not
actually enforce the sentence.

**Why this beats the alternatives.** The strongest alternative is **P7, boundary-driven generation**. But it needs
an oracle, and the engines do not model these cross-entry limits. Note that this worklist is the limit slice of
2.2(c); if (c) is built, it can carry this list as its first, deterministic pass.

### 2.7 R6 — change propagation. Verdict: **confirm P3 and P5, at their stated low priority**

**Recommended strategy.** As the prior report proposes:

- **P3:** a sibling set computed for every fix, from shared inputs, shared enum values and shared anchors.
- **P5:** decision blocks that name lines, gates and phrases, checked in check-all.

**Evidence.**

- Every R6-fix entry shares an input, an enum value or an anchor with the fixed line: 0015/0011, 0017/0014,
  0021/0015, 0024/0020, 0157/0153, 0161/0157, 0192/0020/0024 (inferred from the entries).
- All four decision entries (0036, 0188, 0202, 0203) name a decision whose words are absent from the encoded
  question.
- Most were caught one review round later. The exceptions are 0161, and 0192 (latent for 12 days).

**Expected effect.** One adjudication round saved per fix. 0161 and 0192 are caught at the fix.

**Cost.** About half a day each.

**Failure modes.** The "Siblings checked" field becomes boilerplate. P5 phrase checks pass on a phrase placed in the
wrong question.

**Why it ranks below 2.1 to 2.4.** These bugs are mostly caught in stage, so they are not where the escapes are.

### 2.8 R7 — arithmetic sign domain. Verdict: **better approach than P4 or P7 for this class**

**Recommended strategy.** A checker rule: a `multiply_rate` (or similar) whose amount operand is typed signed
`Dollars` needs a ruling that the operand cannot be negative on a reachable return, or a floor.

**Evidence.** On `ac69196^`, `sa.line2` was `Dollars` and `sa.line3` multiplied it by the medical rate (measured):
this is BUG-0094, found by Tax-Calculator after the Stage 14 losses. On the current tree the rule finds 5 sites:
`f8889.chart_limit`, `sdtw.raw34`, `sdtw.raw43`, `qdcg.line18` and `qdcg.line21` (measured). Each takes minutes to
rule.

**Expected effect.** 0094 at authoring rather than about 8 stages later.

**Cost.** About 2 hours.

**Failure modes.** A sign error that is not a rate product (0100 and 0180 are display floors, N).

**Why this beats the alternatives.** P4 and P7 find 0094 only once a negative case is generated and an engine
disagrees.

### 2.9 G — refusal reach. Verdict: **confirm what exists**

`tools/check_refusal_reach.mjs` (from 0147) mechanises the class. 0088 needed a fixture that answered the screen.
Nothing new is proposed.

## 3. Overall strategy, ranked by expected reduction of value-changing bugs per unit of effort

Ranked by (late V entries prevented or caught earlier, plus latent sites found) against effort. All effort figures
are inferred.

| Rank | Action | Effort | V entries it would have changed (late ones in bold) |
|---|---|---|---|
| 1 | **Instruction-section citation check, plus the supplied-input cross-reference check** (2.2 a, b). Cite the 164 lines and about 70 inputs | ½ day + ~1 day citing | **0159, 0165**; T-069; one probable new gap (line 26) |
| 2 | **Operand check, plus the refused-operand convention** (2.1) | ~1 day + ~30 rulings | **0001, 0051**; 10 latent sites now |
| 3 | **Sign rule** (2.8) | ~2 hours | **0094** |
| 4 | **New-consumer definition check (D′)** (2.4) | ~1 day + ~200 model-drafted pairs once | **0034, 0092, 0096, 0157**; 0049 |
| 5 | **Standing screen review** (2.3) | ~½ day | 0048, 0087, 0188, 0202 (rounds saved) |
| 6 | **Limit-sentence worklist** (2.6) | ~½ day + ~100 rulings | **0069, 0148**; 0063, 0201 |
| 7 | **Quotes on inputs (with T-072), plus the scope-widening sweep** (2.1, prose half) | ~1 day | **0195**; 0047, 0048, 0190 |
| 8 | **Targeted facts-not-conclusions (A′)**, about 10 to 15 household inputs | 2–3 days | **0192**; removes the 0011–0030/0153–0158 mechanism |
| 9 | **Section completeness review** (2.2 c) | 1–2 days + adjudication | **0095, 0097**; 0035, 0148 |
| 10 | P3 siblings, P5 decision trace | ½ day each | **0161, 0192**; 0036, 0188, 0202, 0203 (rounds) |
| 11 | Outcome-level blind predictions with isolated translation (2.5) | ~1 hour per stage | 0201-type; 0067/0159-type wording |

Ranks 1 to 6 are mechanical or near-mechanical. Together they reach 24 of the 68 V entries, and 12 of the 26 late
ones (`matrix.py`; my per-bug judgement, with measured cells as noted in section 2). Rank 9 is the only remedy for
"no line cites it" defects, but its recall is the least known (section 5).

**What not to do.**

- **The prior P1 as a per-paragraph ruling gate.** It means thousands of paragraphs, or about 1,400 unanchored
  operative sentences, to rule. Its unique measured catch is 0097, it misses 0095 by construction, and the pass
  invites theatre. Use rank 9 instead.
- **Candidate (D) at document granularity.** It misses 0096 and flags 127 inputs (2.4).
- **Candidate (B) as answer-level comparison on generated returns.** It is structurally blind to
  mis-specification (2.5).
- **Candidate (C) as a separate gate.** It is subsumed by render plus rank 9 (2.2).
- **Wholesale facts-not-conclusions.** Target it instead (2.4).
- **Broad boundary generation (P7) without an oracle, and indiscriminate render reruns.** About 800 existing
  render rulings, mostly "project retained", show the adjudication cost of unfocused re-review.
- **New prose authoring rules on their own.** Each recommendation above is a check or a triggered review. The
  refused-operand convention is enforced by rank 2, not left as advice.
- **Treating P2 or P6 (flow and visibility) as value work.** All 19 F entries are N. They are worth doing for the
  values sheet and filed-form display, but they do not reduce wrong tax amounts.

## 4. Prototype results

All scripts are in `/tmp/pressure-test/`. They read the tree or a `git archive` of the tree before a fix. The
historical trees are `tree_cbabd7b` (0001), `tree_f16237f` (0051), `tree_2d971ad` (0190), `tree_f7d89e3` (0165)
and `tree_0186a66` (0095–0097).

| Script | What it does | Result |
|---|---|---|
| `extract.py` | Prints inventory entries by id | — |
| `inputs.py` | Extracts all inputs | 541 inputs in the form files (9 more in four definition files, not covered) |
| `operands.py`, `operands2.py`, `operands3.py` | Label line references against expression operands, with helpers resolved, printed markers normalised and cross-form "Schedule 1, lines …" handled | Current tree: 204 checked, 31 flagged, about 10 true dropped-refused operands (listed in 2.1), no live mismatch. Historical: 0001 and 0051 flagged |
| `formface.py`, `formface_all.py` | Lines and inputs citing only a form face where the instructions have a Line N section | 113 inputs cite only a form face (70 with archived instructions); 164 printed lines in all |
| `xref.py`, `xref_hist.py` | Supplied inputs whose Line N section names a project-computed line | Current tree: 5 benign hits in 62. `f7d89e3^`: `f1040.line25c` → Form 8959 line 24 (0165) |
| `classify.py` | Keyword classification of inputs | 34 screens by regex (an undercount); 112 conclusion-style (Bool or other); 56 conclusion-style amounts; 106 fact; 196 plain amounts; 37 other |
| `inputdef.py` | Candidate D at document and (document, page) granularity, and the conclusion intersection | Document level: 127/548 flagged, `person.work_ssn` not flagged on `0186a66^`. Page level, Bool/Enum/Count: 68 on `0186a66^` including work_ssn, age65, months, status; 87 now; 29 that are also conclusion-style |
| `pages.py` | Cited pages per document | i1040gi p. 22 uncited before the 0095 fix |
| `paracov.py` | P1 paragraph coverage | EIC pp. 40–48: 129 paragraphs, 82 unanchored (crude anchoring), about 12 operative, including the 0097 paragraph on pp. 40 and 46 |
| `operative.py` | Operative sentences on all cited pages | 13,050 sentences; 1,670 operative; 224 quote-anchored |
| `limits.py` | Limit and aggregation sentences | 65 on 361 cited pages; recall 3/5 direct, 4/5 with locator parsing |
| `blind_answerer.md` | The blind-answerer exercise | Answer-level 3/7; outcome-level 7/7 given the deciding fact |
| Enum-option check (inline) | Enum questions that name some value ids but not all | 0 of 31 enum inputs |
| Sign-rule scan (inline) | Rate products of signed `Dollars` | 5 current sites; `sa.line3` on `ac69196^` |
| `matrix.py` | The per-bug strategy table | Counts in sections 1 and 3 |

## 5. What remains uncertain, and the cheapest experiment for each

1. **The recall of a model completeness review (2.2 c)**, which is the basis of rank 9.
   - Experiment: give an isolated model the dependents and EIC sections of the `0186a66^` tree, by heading range
     including p. 22, and the encoded line list, without mentioning the bugs.
   - Count whether 0095 and 0097 appear, and how many claims it makes. This takes two model calls.
2. **The yield of re-citing the 164 form-face lines (rank 1).** One probable gap in 4 sampled sections is n = 4.
   Experiment: read 20 sampled Line N sections against their lines, which takes about an hour, with no model.
3. **Whether A′ actually speeds detection rather than just moving the bug.** Experiment:
   - in a scratch copy, factor `dependent.months` into facts;
   - delete the born-or-died branch from the new predicate;
   - run the transcription comparison and one outcome-level blind scenario.

   Then see whether either flags the deletion.
4. **The precision of D′.** Experiment: replay the consumer-graph diff across the Stage 9 commit, and count the
   new cross-section consumer pairs and how many are real (0034 and 0096 should appear).
5. **The prose half of the scope-widening sweep (2.1).** Its recall rests on inputs carrying quotes. 0195 had none.
   Experiment: on `20b9c3e` (Stage 13), list existing inputs whose cited section text, not just quote, mentions
   "spouse" or "joint", and count the list. This tests whether the sweep is small enough to adjudicate.
6. **My V classification and strategy table are one reader's judgement.** The prior report's V/N calls were
   adopted (for example 0012, 0035 and 0062 as N). The R1–R7 assignment and the Y/p cells have not had a second
   reader. Cheapest check: a second reader re-codes 15 random rows of `matrix.py`.
7. **The blind-answerer exercise was run by a model that knew every bug**, so it shows the mechanism (answer-level
   comparison cannot see mis-specification), not rates. Experiment: an isolated model answers the seven old
   questions from the W fact sheets in `blind_answerer.md`.
8. **Two byproduct findings are unverified:**
   - the adopted-child / pre-adoption placement wording of `dependent.relationship`;
   - joint estimated payments on separate returns (Form 1040 line 26).

   Each needs a source read against scope and the interview help, about 15 minutes, before it is entered in the
   inventory.
