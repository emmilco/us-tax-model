# Bug root-cause analysis — BUG-0001 to BUG-0210 (2026-10-29)

Purpose: find the recurring root causes in the bug inventory and, for each, the cheapest structural or
methodological change that would have prevented the bug or caught it earlier. Read-only analysis; no
data, tool or log was changed. Inputs: `BUG_INVENTORY.md` (all 210 entries read in full), `TASKS.md`,
the four plan documents (`docs/2026-10-22_integrity_plan.md`, `2026-10-23_independent_validation.md`,
`2026-10-24_validation_policy.md`, `2026-10-26_plan_revision.md`), `handoffs/HANDOFF-STAGE-21.md`, and
spot reads of `engine/src/check.ts`, `tools/check_all_steps.sh`, `tools/check_refusal_reach.mjs`,
`tools/engines/compare.py`, `tools/citations.py`, `tools/transcription/transcribe.py` and
`engine/src/classm.ts`.

## 1. Method

Each entry was read whole: symptom, root cause, why it survived and fix. The pattern tags were used only
as an index, because they are inconsistent: for example `scope-screen-narrower-than-line`,
`question-incomplete`, `input-wording` and `render-wording` name the same mechanism. Each id was given
one **primary class**, the earliest point in the pipeline where the defect could have been prevented.
Where an entry fits two classes, the other is noted in section 5.

**Severity.** An entry is **V (value)** when, on a return the tool would complete, it changes a tax
amount. That includes a question whose wording leads a filer to enter a wrong amount, or to answer a
screen No and get a completed return that is wrong. Everything else is **N**: display only, labels,
citations, over-refusal, value-neutral, latent outside the current scope, and all tooling. Where the
entry does not state the value effect, the V mark is inferred (listed in section 5). In total 68 entries
are V. The **weighted score** used for ordering is 3 × V + 1 × N.

| Class | Name | Entries | V | Score |
|---|---|---:|---:|---:|
| Q | Input and screen questions that diverge from the source | 30 | 26 | 82 |
| L | A computation or predicate omits or misreads a source rule | 28 | 18 | 64 |
| T1 | Review tooling: context, parsing, comparison | 27 | 0 | 27 |
| I | Incomplete fixes: the fix covered the reported instance, not its siblings | 10 | 6 | 22 |
| F | Flow control (stop, skip, "use only if") not encoded | 19 | 0 | 19 |
| U | One input or definition reused for rules that differ | 7 | 6 | 19 |
| R | Stale invariants when scope grows | 7 | 6 | 19 |
| T2 | Checks that pass without measuring (evidence accounting, gates, test tools) | 18 | 0 | 18 |
| T3 | Infrastructure, robustness, year tooling, usability | 17 | 0 | 17 |
| K | A recorded decision never reached the encoding | 6 | 4 | 14 |
| G | Refusal placement, reach and over-refusal | 10 | 2 | 14 |
| D | Duplicated hand-maintained text drifts | 8 | 0 | 8 |
| C | Citation locators | 8 | 0 | 8 |
| E | Evaluator and renderer semantics | 7 | 0 | 7 |
| X | Closure or disposition records (not new defects) | 8 | — | — |
| | **Total** | **210** | **68** | |

Q and L share an upstream cause: authoring works line by line from the line's own citation. They are
kept separate because different safeguards can see them. Q (question wording) is invisible to every
value-based check, while L can be caught by an engine or a fixture that reaches the condition.

Three entries are aggregates and count as one each: BUG-0032 (25 screens), BUG-0073 (98 citation
problems) and BUG-0076 (five defects).

## 2. Root-cause classes, by weighted score

### Q — Input and screen questions that diverge from the source (30; 26 V)

**Mechanism.** Input questions and scope screens are free prose. They were written from the line's own
instruction, or from the first clause of a step's question, and so left out conditions, alternatives and
exceptions printed beside it (narrow), or generalised a parenthetical (wide). The arithmetic is then
correct for whatever the filer enters, but the filer is asked the wrong question. Fixtures and the
generator supply answers directly, so wording never moves a tested value.

**Representative entries.** 0004–0006, 0008, 0010 (screens missing items of the same instruction
sentence); 0032 (25 screens reworded after the screen review); 0013, 0014, 0023, 0027–0030 (household
exceptions: ITIN applied for, born or died, citizenship of an adopted child, military); 0067 (Form
1099-MISC prizes counted twice); 0070 (own dependent-care contributions); 0119 (payment year used as a
scope limit); 0159 (Form SSA-1099 withholding sent to box 4); 0195 (spouse's main home); 0205 (a use test
the source does not have).

**How caught, and how late.** Claude render comparison caught 0004–0030 and 0058–0086, mostly in the
stage that introduced them (the household cluster before commit, 2026-10-17). The screen review (T-008)
caught 0032. deepseek-flash render caught 0117 and 0119. Execution-triaged source adjudication caught
0159, 0189, 0195, 0197, 0204 and 0205. The long escapes were:

- 0159: a line 25b question from before Stage 16, found 2026-10-26;
- 0195: `eic.us_home`, from Stage 9, found 2026-10-29 in Stage 19.

Q still recurs: 0197, 0203 (class K), 0204 and 0205 all come from Stages 19 to 21.

**Which safeguards should have caught them, and why they didn't.**

- **Fixtures, engines, mutation, Lean and class M** receive answers as givens. Their blind spot is "value-neutral for every fixture and generated return" (0004, 0005, 0010).
- **The transcription comparison** compares expression trees and "sees nothing in a question's wording" (0004).
- **The render review** judged each screen against its own citation, not against the lines the screen stands in for (0032, "Why it survived").
- **The review text** was column-spliced until T-022 and T-025, so the "any other person" and juvenile-detention sentences were never put in front of a reviewer (0017, 0023, 0027, 0029).
- **Review prompts** cut input descriptions at 160 characters until BUG-0131. That this hid wording defects from transcription reviewers is inferred.

### L — A computation or predicate omits or misreads a source rule (28; 18 V)

**Mechanism.** The arithmetic or Boolean logic was written from part of the governing text. Forms include:

- an operand slip (0001);
- a limit that applies across entries, encoded per entry (0063, 0069);
- separate-return rules not read (0062);
- a missing or added floor (0094, 0100, 0180);
- a missing gate or limit (0095, 0097, 0148, 0186, 0201);
- a wrong premise (0078, 0080);
- year-end age used for an at-care age (0111);
- a cross-form amount not carried (0165).

Several stated root causes say the governing sentence sat outside any cited line. Examples: "the cautions sit above each part, not on a numbered line" (0035); "no line cites the SSN-entry sentence" (0095); "the disallowance paragraph ... carries no step number" (0097).

**Representative entries.** 0001, 0063, 0069, 0094, 0095, 0097, 0148, 0165, 0186, 0201.

**How caught, and how late.**

- The engine differential caught 0001 (present since Stage 1/5, found 2026-10-16), 0094 (since Stage 14), 0100 and 0165 (UsTaxes, 2026-10-27).
- The Direct File comparison caught 0095 and 0097, both present since Stages 8/9 and found 2026-10-22.
- Render review caught 0011, 0060, 0063, 0069, 0072 and 0078, mostly in stage.
- The second family caught 0098, 0111 and 0120.
- Source adjudication caught 0148, 0163 and 0186.
- Blind prediction caught 0201.

**Which safeguards should have caught them, and why they didn't.**

- **The same-data blind spot.** Lean "reads the same data", and mutation cannot flag an operand that every recorded expectation contains. The "17 fixtures with qualified dividends had expectations recorded from the engine" (0001).
- **Cited pages only.** Reviewers are given the cited pages, so an uncited paragraph is read by nobody (0095, 0097, 0124).
- **No case reaches the condition:** distant relatives (0011), married filing separately (0035, 0062), negative AGI (0094), an understated entry (0186).
- **Engines take eligibility as given.** "The engines take dependents as given" (0095, 0097).
- **Faithful rendering of a misread line.** The render review accepted "Multiply line 2 by 7.5%" as faithful (0094).

### T1 — Review tooling: context, parsing, comparison (27; 0 V)

**Mechanism.** The review machinery was built and repaired on the main path, between 2026-10-17 and
2026-10-26. Defects fell into four groups:

- **Parsers:** a regex spanning sections (0016); first block taken instead of last (0025); duplicate keys hidden (0112); a blank read as zero (0123).
- **Context given to reviewers:** labels leaked (0107); text truncated (0131); a missing grammar (0130) or table interface (0133); a glossary scope gap (0125); an availability contract missing (0134); authored gates imported (0145); targets missed (0146).
- **Comparators:** units erased (0129); a dependency walker that skipped positions (0132); lines that share a printed number (0054, 0077).
- **Case selection:** 0061, 0122, 0136, 0140, 0142, 0143.

The plan revision's own diagnosis is that "each checker change made recorded reviews stale, which required fresh requests, which exposed the next checker gap".

**How caught.** Request audits, pilots, adversarial audits and adjudication.

**Observation.** No T1 entry is dated after BUG-0146 (2026-10-26). The tooling freeze in plan revision B,
which allows a tool change only for a concrete wrong value or ruling, coincides with the end of this
class. Since then the open tool defects are parked in T-070, T-076, T-079, T-081 and T-083.

### I — Incomplete fixes (10; 6 V)

**Mechanism.** A fix changed the reported line, enum value or question. A sibling that shares the rule
(a mirror predicate, another value of the same bullet, another question citing the same paragraph, a
second line carrying the same gate) was not changed, or the fix introduced a new error.

**Entries.**

- 0015 corrects 0011.
- 0017 corrects 0014: the fix carried the rule without its condition.
- 0021: the Test 2 mirror was not widened with 0015.
- 0024: the conditions went to one of three enum values.
- 0154: one gate on two lines, with the first line's message.
- 0156: gaps left by 0152.
- 0158 and 0161: part-year rule fixes applied to one route only.
- 0192: the 0020/0024 condition sat in the value's description but the predicate never asked it. Pre-existing for 12 days.
- 0066: BUG-0065's one-off check was too narrow.

**How caught.** Usually by the next round of the same review: render reruns for 0015, 0017, 0021 and 0024; round 2 or 3 of source adjudication for 0154, 0156, 0158 and 0161. 0192 was found in Stage 18 from a model's note.

**Which safeguards should have caught them, and why they didn't.**

- **Review reruns attend to the ruled line.** "The BUG-0015 render comparison judged `qr_relationship`, not `hoh_test2`" (0021); "the BUG-0020 render comparison was ruled on the household-member wording" (0024).
- **Subject staling is per form.** The subject-hash staling (T-044 part 2) and binding rulings to the subject (0121) force the changed form's logs to be refreshed, but nothing names the cross-form siblings: `f2441.nondependent` for a fix in `dependent.yaml` (0161).

### F — Flow control (stop, skip, "use only if") not encoded (19; 0 V)

**Mechanism.** The encoding computes and shows every line. Stops were applied only where a result line
chooses its source, as in "applied only where line 27 chooses its source" (0151) and "Only `eic.credit`
and `eic.line6` respected them" (0152). Values were right, but the values sheet, and for Schedule 8812 a
filed form, showed amounts on lines the instructions skip.

**Representative entries.** 0042, 0055 (a stop encoded as a floor), 0057, 0149–0152, 0155, 0183, 0185,
0187, 0191, 0194, 0207–0210.

**How caught, and how late.** Most were caught by execution-triaged source adjudication (2026-10-26
onward). Blind predictions caught 0183 and 0194, and class M caught 0042 and 0191. Two facts matter:

- The owner's decision of 2026-10-26 made "a nonzero amount on a skipped line" a defect. Five entries predate it (0042, 0055, 0057, 0059, 0099), and the rest are a backlog swept after it.
- After that decision, new stages still produced the defect: 0183 and 0185–0187 (Stage 20), 0191 (Stage 18), 0194 (Stage 19), 0207–0210 (Stage 21 and T-067). Authoring has not absorbed the rule, and the catch still depends on adjudicators reading.

**Which safeguards should have caught them, and why they didn't.**

- **Transcription comparison:** "counts a line as AGREE without comparing `shown_when`" (T-076(2), the 0183 case).
- **Class M:** fills of non-collection documents ignore `shown_when` and write hidden lines into expectations (T-079(1), the 0191 case).
- **Fixtures** cannot assert that a line is hidden. Regressions assert the condition line instead (0150–0152).
- **Engines** compare totals only.
- **The round-4 skipped-line sweep** was manual and "covered worksheets after a printed STOP, not worksheets entered only from a Schedule D Yes answer" (0183).

### U — One input or definition reused for rules that differ (7; 6 V)

**Mechanism.** An existing input whose wording fits one rule is read by a second rule with a different
definition:

- whole-year ages for "younger than you" (0019);
- the standard-deduction birth-date boundary reused for the EIC (0034);
- an ITIN-application question reused for the child tax credit (0049);
- filing status standing in for marital status (0092);
- the CTC "valid for employment" SSN reused for the EIC (0096);
- the all-year months answer reused for part-year tests (0153, 0157).

**How caught.** Render review caught 0019, 0034 and 0049, at the stage where the second reader was added. Audit and Direct File caught 0092 and 0096, about 5 to 13 stages after. Source adjudication caught 0153 and 0157 (household since Stage 8, found 2026-10-26).

**Why the safeguards missed them.** The render review reads the consuming line's English, which is faithful to the input's label. "SSN valid for employment" reads as a faithful rendering of "valid SSN" (0096), and "married filing jointly" as a faithful rendering of "married" (0092). No fixture holds the distinguishing fact: the card type, the boundary birth date, a married head of household.

### R — Stale invariants when scope grows (7; 6 V)

**Mechanism.** A line was right for the slice because an operand was zero, refused, or limited to one
filing status. A later stage made it reachable, and nothing recorded that the line depended on the old
state. The entries say so directly:

- "summed only lines 11 and 13" after Stage 14 added lines 15–17 (0051);
- "encoded through line 6 only, when no return in scope had self-employment income" (0053);
- "`ftc.limited` used line 16 alone, which was exact while every Schedule 2 Part I amount was refused" (0190);
- "the earlier ruling rested on married statuses being refused" (0047, 0048).

0084 and 0007 are the same pattern. Cross-listed by tag: 0055, 0057, 0058, 0094.

**How caught.** The engine differential caught 0051. The transcription comparison caught 0053 and 0084. Render review caught 0047 and 0048. Source adjudication caught 0190. All but 0051 were caught in the stage that broke the invariant; 0051 surfaced in Stage 14 via the engines.

**Why the safeguards missed them.** The premise maps and decision batches are prose. Nothing lists the lines whose correctness rested on the old invariant, so a review of a new stage looks at new lines. For 0047 and 0084, "the Stage 13 rulings ... did not address the condition".

### T2 — Checks that pass without measuring (18; 0 V)

**Mechanism.** A safeguard reported green while measuring less than it claimed:

- `runMutation`'s exit status was discarded (0170);
- rates compared as `rate:undefined` (0082);
- keyed-lookup keys were never mutated (0052);
- evidence class M fell into R (0089), and labels were wrong (0090);
- the differential compared about 15% of cases with "0 unexplained" (0093);
- adapter defaults and exclusions hid comparisons (0039, 0040, 0182);
- mutation-equivalence arguments were false (0171) or stale (0116);
- the noise-rate denominator was wrong (0110), and an owner's rule was recorded but not implemented (0106);
- evidence and provenance problems: 0101–0103, 0108, 0127, 0144.

**How caught.** Mostly by human-directed or continuation audits (2026-10-22 and 23), and the mutation second reader (2026-10-27).

**Status.** Mostly fixed with mechanical guards: the `NOT_COMPUTED_FLOOR` in `tools/engines/compare.py`, the mutation exit status, `OPEN_DEFECT_SURVIVORS`, and structural equivalence rules.

### T3 — Infrastructure, robustness, year tooling, usability (17; 0 V)

**Entries.**

- **Limits and build order:** buffer limits (0031), string length (0038), a build-order race (0137).
- **Transport:** 0113, 0114.
- **Extraction:** 0050, 0178.
- **Year adoption tooling:** 0075, 0166–0168, 0177, 0179.
- **Human packet usability:** 0104, 0105, 0128.
- **Performance:** 0118.

**How caught.** All were caught by the run that first exercised the condition. The TY2026 rehearsal alone found six, which is evidence that rehearsals pay. None affected tax values.

### K — A recorded decision never reached the encoding (6; 4 V)

**Entries.**

- 0036: "the decision was taken into the arithmetic ... but not into the question wording".
- 0188: "D6 decided the branch is refused, but `f8962.other` asks only about someone not lawfully present".
- 0202: "D6 had said the question would be reworded".
- 0203: "D4 put the account-value halves in the question's wording, but `retirement.exc_amount` did not mention them".
- Tooling analogues: 0106 (owner's rule "recorded in the plan but not implemented") and 0115 (model pin "recorded in prose only").

**How caught.** In stage: by transcription (0036), by the session checking D6 against the encoding (0188), and by adjudication (0202, 0203). The four V entries are from Stages 12, 18 and 21, so this class recurs in the current workflow.

**Which safeguard should have caught them, and why it didn't.** None checks it. `research/premises/*.decisions.md` is prose, and nothing ties a decision to the line, gate or wording it prescribes.

### G — Refusal placement, reach and over-refusal (10; 2 V)

**Mechanism.** A refusal fires only if its line is evaluated on the interview path.

- **Placed where the interview does not go:** the gate sat on a helper or a path the interview may not reach (0088, 0147), or was never wired (0009).
- **Placed too broadly:** a gate reached too widely made every return ask a question (0046), or refused returns it should not (0037, 0198, 0200).
- **Ordering:** a consistency gate was ordered before the branch that makes it moot (0138), and an availability claim was overstated (0169).

**How caught.** 0147 by source adjudication; it led to the mechanical `tools/check_refusal_reach.mjs` in check-all. 0088 by a regression case; 0200 by the blind scenario builder; 0198 by adjudication.

**Why the safeguards missed them.** "Fixture checks evaluate helper lines the interview never reaches" (0147). This is now partly mechanised. Over-refusal has no systematic check: a refusal fixture shows a gate fires, and nothing shows it does not fire when the claim is zero.

### D — Duplicated hand-maintained text drifts (8; 0 V)

**Entries.**

- Refusal remedies that list "what this tool computes": 0022, 0081, 0193, 0196.
- Interview copies of prompts and citations: 0074.
- Labels copied from a neighbour, or left stale: 0003, 0184.
- Form metadata versus an interview override: 0141.

**How caught.** Render review and adjudication, usually one or more stages after scope changed.

**Status.** 0074 was fixed structurally by the question bank, where the build fails on a repeat. The remedy lists are still hand-maintained, with four recurrences (Stages 8, 14, 18 and 19), and T-050 is still open in TASKS.

### C — Citation locators (8; 0 V)

**Entries.** Missing pages left reviews without source text (0041, 0056, 0124, 0126); wrong pages (0065, 0073); span or unchecked locators (0091); a misquote on an input line (0164).

**Status.** Largely mechanised: `tools/citations.py --strict` in check-all, plus integrity plan 0.2. The open residue is T-072, because quotes on input, parameter and gate citations are still unchecked (0164).

### E — Evaluator and renderer semantics (7; 0 V)

**Entries.**

- **Refusal versus unknown ordering:** 0026, 0079, 0083.
- **Collection entry lines never evaluated or shown:** 0033, 0044.
- **Enum parameter rendered as money:** 0071. This garbled text was in front of the render reviewers.
- **Lean gate key on an enclosing entry:** 0206. This is the only defect the Lean comparison has caught, and it was in Lean itself.

**How caught.** Property tests, building fixtures, the render review and the Lean comparison. All were caught early relative to their effect.

## 3. Cross-cutting findings about the safeguards

**Which safeguards caught the 68 value-affecting defects.** First catcher, from the "Caught by" fields:

| Safeguard | V caught | Notes |
|---|---:|---|
| Claude render comparison (incl. reruns) | 34 | mostly Q, U and early L; household and Schedule C clusters |
| Execution-triaged source adjudication (plan revision A, from 2026-10-26) | 16 | 0147, 0148, 0157, 0159, 0161, 0163, 0186, 0188, 0189, 0190, 0192, 0195, 0197, 0202, 0203, 0205; several pre-existing for many stages |
| Second transcription (Claude) | 4 | 0036, 0053, 0084, 0087 |
| Engine differential | 4 | 0001, 0051, 0094, 0165, all long escapes |
| Direct File comparison | 3 | 0095, 0096, 0097, household predicates no engine reaches |
| deepseek-flash render | 2 | 0119, 0120 |
| Fixture or regression construction | 2 | 0045, 0088 |
| Screen review (T-008) | 1 | 0032 (25 screens) |
| Blind prediction | 1 | 0201 |
| Human-directed audit | 1 | 0092 |
| Lean comparison, mutation, property tests, class M, static checker | 0 | see below |

**Safeguards that catch no value defects.**

- **Lean comparison.** It shares the data, so it can only find evaluator divergences; it has found one, in Lean (0206).
- **Mutation testing.** It found fixture gaps and one display defect (0169, via the second reader of equivalence arguments, 0171). Its value is in keeping fixtures sharp, not in finding source errors.
- **Property tests.** They found evaluator refusal-ordering issues only (0026, 0079, 0083).
- **Class M.** Its findings were display only: 0042, 0080, 0191. The integrity plan's 1.5 records "2 corrections in 484 disagreements", and T-066 is still in progress.
- **Static checker.** It catches structural errors at authoring time, which are not recorded as bugs. Its one inventory appearance is 0002, where its seam rule "made the strict form the path of least resistance".

None of this makes them worthless: they guard regressions. But no new source-reading defect class will be caught by adding more of them.

**Shared blind spots.**

1. **Questions are givens.** Every value-based safeguard supplies input answers directly: fixtures, generator, engines, mutation, Lean, properties. Question wording is checked only by readers (render, screen review, adjudication). This covers Q and U, which are 32 of the 68 V entries.
2. **The citation selects the context.** Authors work from the line's citation, and the review tools give reviewers the pages that citation names. An uncited paragraph is read by nobody (0095, 0097, 0124, 0126, 0041, 0056, 0065, 0032).
3. **The same data.** Lean, mutation and fixtures recorded from the evaluator agree with whatever the data says. This "recorded-expectation laundering" is behind 0001, 0016, 0090, 0123 and 0160.
4. **Visibility is ignored.** The transcription comparison, the class M fill for non-collection documents, fixtures and engines all ignore `shown_when`. This is all of F.
5. **The corpus never reaches the edge.** Distant relatives (0011), same-age persons (0019), boundary birth dates (0034), every filer aged 40 (0039), a married head of household (0092), negative AGI (0094), understated carry-in entries (0186). An oracle still has to judge the edge case, so better generation helps mainly where an engine computes the line.
6. **Attention is anchored on the ruled line.** Reruns and fixes judge the line that was flagged; siblings wait for the next round. This is I.

**Where the work is going.** Of the 17 defect entries from Stage 18 to Stage 21 (0188 to 0205, excluding the closure 0199), 10 are V and nearly all were caught in the stage that introduced them, by source adjudication or blind predictions. In-stage catching is now strong. Pre-existing defects are still being found by each new reader: 0192 and 0195 by adjudication, 0165 by UsTaxes.

## 4. Ranked proposals

The ranking weighs the bugs addressed (V counted triple) and the latency removed against build and
upkeep cost. Bug lists say "stated" where the entry's own root cause supports the claim and "inferred"
where it is this analysis's reading.

### P1. Source-paragraph coverage worklist (stage-close check; tool extension)

**Change.** A new `tools/source_coverage.py`, or `tools/citations.py --coverage`, does the following:

1. For each form, collect every (doc, page) its locators name, across computed lines, inputs, screens, refusal gates and parameters. `citations.py` already parses the segments.
2. Segment those pages of `sources/2025/<doc>.cols.txt` into paragraphs at headings, bullets and blank lines.
3. Mark a paragraph anchored when some locator's heading or quote falls in it.
4. Write `reports/2025/source_coverage.md` listing the unanchored paragraphs per form. Paragraphs starting with "Exception", "Caution", "Note", "TIP", "If married" or "see Pub." go first, as do unnumbered paragraphs.
5. Each unanchored paragraph needs a ruling in `reviews/2025/source_coverage.json`: applies to a named line, refused by a named gate, or not applicable for a stated reason. Check-all fails on unruled paragraphs of forms changed in the commit, so old forms are ruled once and new stages pay only for their own pages.

**Type.** Stage-close check and tool.

**Bugs.**

- Stated: 0035 (caution above the parts), 0095 (SSN sentence uncited), 0097 (unnumbered disallowance paragraph), 0124 (p. 117 uncited).
- Inferred, because the rule was on or next to a cited page and was not encoded: 0014, 0023, 0028, 0030, 0042, 0062, 0063, 0069, 0072, 0084, 0087, 0153 and 0157 (the "see Pub. 501" referral on i1040gi p. 15), 0165 (if line 25c cited only the form), 0201, 0203.
- About 20 in total, 13 of them V, including four of the longest escapes: 0084, 0095, 0097, 0165.
- It would not catch misreadings of a sentence that is anchored: 0159, 0189, 0195.

**Cost.** High. Building it takes about 2 to 3 days. The real cost is the first ruling pass over the cited pages, likely hundreds of paragraphs for i1040gi alone; a model could draft the rulings with adjudication, as plan revision A does. The failure mode to name is rubber-stamped rulings, which would turn the check into theatre. Limit that by requiring each "applies to" ruling to name a line that exists, and each "not applicable" ruling to quote the deciding phrase.

**Already exists?** No. Screen review (T-008) did this once for screens only. Integrity plan 0.2 checks the locators that exist, not coverage. Direct File (1.7) was a one-off outside reader.

### P2. Flow-instruction check (checker rule over the source text)

**Change.** A new `tools/check_flow.py` in check-all does the following:

1. Scan the archived text of each form's cited documents for flow sentences, for example `stop here`, `STOP`, `stop;`, `skip lines? N( through M)?`, `leave lines? N( through M)? blank`, `do not complete`, `use this worksheet (only )?if`, `fill out Part X only if`, `if you checked "Yes" on line N`. A rough count over all sources finds 443 hits; far fewer fall on cited pages.
2. Resolve the line numbers in each sentence to the form's printed and worksheet markers.
3. Require each target line to carry `shown_when` or a ruling in `reviews/2025/flow_rulings.json`, for example "value forced to zero by the arithmetic and line shown as $0, owner's choice" or "helper, T-067".
4. Optionally, once the sentence-to-condition map exists, add a fixture key `shown: false`, so regressions assert hiding directly instead of asserting the condition line.

**Type.** Checker rule and tool.

**Bugs.** 0042, 0055, 0057, 0149–0152, 0155, 0156, 0183, 0185, 0187, 0191, 0194, 0209, 0210 (16; all N). It would not catch 0059, 0099, 0207 or 0208, where applicability is implied rather than stated as a stop.

**Why it ranks second despite no V.** F is the most frequent class in the newest stages: 9 of the 27 non-closure entries from 0183 to 0210 are F, and adjudicators still find them by reading.

**Cost.** Medium. About 1 day, plus an initial ruling pass.

**Already exists?** No mechanical check. The round-4 sweep was manual, and T-067 (hiding helpers) is done. Related open items are T-076(2) and T-079(1) (see P6).

### P3. Fix-sibling set and ruling invalidation (tool plus bug-entry rule)

**Change.** A new `tools/siblings.py <line ids>` lists:

- (a) lines in any form that read the same input, enum value or gate as the changed lines;
- (b) lines and input questions whose locators anchor the same (doc, page, heading);
- (c) predicates that test the same enum values.

`tools/check_bug_inventory.py` then requires a new entry with a **Fix** field to carry a **Siblings
checked:** field listing the generated set. Check-all fails when a sibling's form review logs were not
refreshed in the same commit, extending the subject-hash staling of T-044(2) across forms.

**Type.** Tool, plus a mechanical rule on bug entries.

**Bugs.** 0015, 0017, 0021, 0024, 0154, 0156, 0158, 0161, 0192 (9; 6 V). Most were caught one review round later, so the gain is mostly a round saved. The exceptions are the cross-form or description-versus-predicate cases, 0161 and 0192 (12 days latent).

**Cost.** Low. Half a day to a day: reverse dependencies come from the canonical data, and anchors from `citations.py`.

**Already exists?** Partly. Per-form subject staling (T-044(2)) and binding rulings to the subject (0121) exist, but neither crosses forms nor follows shared anchors.

### P4. Line-profile diff at stage close (stage-close check)

**Change.**

1. A new engine command records, for each line over the generated corpus plus fixtures: ever nonzero, ever negative, ever known, refused-only, filing statuses reached. Output: `reports/2025/line_profile.json`.
2. At stage close, diff against the previous commit's profile. For each line whose profile widened, list:
   - its direct readers;
   - lines that read two or more lines of the same form or printed range but not this one. This sibling-sum heuristic targets the "lines 11 through 20" omissions;
   - refusal remedies and labels whose text names that line's form;
   - register entries whose reason names it.
3. Force the review logs of those lines stale.

**Type.** Stage-close check.

**Bugs.**

- Stated or strongly inferred: 0007 (line 13b), 0051 (Schedule 1 lines 15–17 newly nonzero; `ssb.line6` reads lines 11 and 13), 0055 (Schedule 8812 worksheet line 6 newly nonzero), 0094 (AGI newly negative in Stage 14, read by `sa.line3`), 0100.
- Remedy texts: 0022, 0081, 0193, 0196.
- Weaker: 0053, 0190, through the sibling heuristic.
- About 10, with 4 V of long or mid latency.

Status widening alone (married filing jointly entering in Stage 13: 0047, 0048, 0084) would flag too much to be useful, so the tool should report it but not stale on it.

**Cost.** Medium. 1 to 2 days. Branch and coverage reporting already walk the corpus.

**Already exists?** No. Premise maps are prose, and T-049 was a manual instance of revisiting an assumption.

### P5. Decision-to-encoding trace (checker over decision batches)

**Change.** Each decision in `research/premises/*.decisions.md` that prescribes an encoding change
carries a fenced YAML block, for example `lines: [f8962.line24]`, `refuses_on: {line: f8962.line24, gate: f8962.alien_branch}`, `question_contains: {line: f8889.unsupported, phrases: ["by the due date"]}` and `fixture: stage18.refuse.alien_below_100`.

A new `tools/check_decisions.py` in check-all verifies that the lines exist, that the refusal is
declared on the named line with that gate, that the phrases are present and that the fixture exists.

**Type.** Checker rule plus an authoring convention.

**Bugs.** 0036, 0188, 0202, 0203 (4 V). Tooling analogues: 0106, 0115.

**Cost.** Low. Half a day to build, and minutes per decision.

**Value.** All four V entries were caught in stage, so the gain is earlier catch and fewer adjudication rounds. But this is the only proposal aimed at a defect class that appeared in Stage 21.

**Already exists?** No. Decision files are prose.

### P6. Make visibility part of every comparison (tool fixes)

**Change.**

- The transcription comparison compares `shown_when` (T-076(2)).
- The class M fill of non-collection documents honours `shown_when` (T-079(1)).
- Triage treats a refused or unknown `shown_when` as not shown (T-070(2)).

**Type.** Tool fix.

**Bugs.** 0183 (named in T-076(2)) and 0191 (T-079(1)). It would also surface the rest of F as review disagreements rather than leaving them to adjudicators' reading.

**Cost.** Low.

**Already exists?** All three are open TASKS items, held under plan revision B. 0183 is arguably the concrete case that B requires.

### P7. Boundary-driven generation (test type)

**Change.** `engine/src/generate.ts` draws, for every comparison constant and parameter threshold, values at the boundary and ±1; dates at each birth-date boundary; every enum value; negative values wherever a signed Dollars line can be reached. P4's profile can report whether each boundary was hit.

**Type.** Test-corpus change.

**Bugs survived because no case existed.** 0011, 0019, 0034, 0039, 0092, 0094, 0182, 0186. Conversion to catches needs an oracle, so likely only where engines compute the line: 0034 (EITC age), 0094. Credible early catches are 2 or 3.

**Cost.** Medium.

**Already exists?** Partly: T-052 (screens), BUG-0142 (calendars).

### P8. Quote verification on input, parameter and gate citations (checker extension)

**Change.** T-072 as written.

**Bugs.** 0164.

**Cost.** Low.

**Already exists?** Open in TASKS.

**Not proposed.**

- More prose authoring rules: Q and L are line-local reading failures, which a rule cannot make visible. P1 makes them visible.
- More model-family reviews: render and adjudication already catch most Q in stage, and their misses are context misses (P1), not reader quality.
- A hook for over-refusal (G): no clean mechanical test was found. Over-refusals are rare and owner-accepted where they remain (0198 residue, T-079 note).

## 5. Uncertainties

**Thin or mixed entries.**

- BUG-0076 is five defects with different causes (railroad compensation in SE, the W-2 roster wording, the student loan spouse, a divide by zero, placeholder labels). It was filed under L because the largest value effect (Schedule SE, $4,238.87 against $1,559.85) is a computation scope gap; two of its parts are Q.
- BUG-0032 and BUG-0073 are aggregates that each count once, which understates Q and C.

**Severity inferences.**

- 0045: the V mark is inferred. Part II not applying would zero the tips deduction, but the entry states only that lines 8 to 10 became $0.
- 0203: the V mark is inferred, on the reading that a filer could enter more than the limit.
- 0062 and 0035: marked N because married filing separately is refused for whole returns, so they are latent.
- 0086: marked N because it has "no 2025 tax effect".
- 0162: marked N; a value difference arises only for a filer who would opt out.
- 0012 and 0153: marked N because the effect is a refusal, not a computed wrong amount.

**Boundary calls between classes.**

- 0084 (R or L): the entry tags a stale scope ruling; the rule sits in another form's refusals.
- 0094 (L or R): a missing floor that stayed latent until losses were generated.
- 0055 and 0057 (F or R): a stop instruction that became observable only when a new input arrived.
- 0156, 0158 and 0161 (I or F/U): placed in I because each is explicitly the remainder of an earlier fix.
- 0189 (Q or L): the question carried a per-year reading of a per-month rule.
- 0153 and 0157 (U or Q): the months answer encodes the all-year rule.
- 0169 (G or F): availability overclaimed on a printed step.
- 0141 (D or Q): divergent wording between form metadata and the interview.
- 0136, 0140 and 0142 (T1): benchmark and generator facts, not project tax logic.

**Closures (X).**

- 0160 re-finds 0099 and closes it. Its own distinct fact, that `stage4.sdtw.special_rates` had recorded the defect, is a laundering instance.
- 0172–0176, 0181 and 0199 record fixes or dispositions of earlier entries.

**Catch attribution.** Some entries name more than one catcher (0042, 0080, 0188). The first named was used.

**P1 and P4 hit lists.** These are inferred from where the governing sentence lies relative to the cited pages. They were not verified by running a prototype. A prototype run on the current tree is the cheapest way to test both proposals before committing to them.

## Appendix A. Full id lists per class

- **Q (30):** 0004, 0005, 0006, 0008, 0010, 0013, 0014, 0018, 0020, 0023, 0027, 0028, 0029, 0030, 0032, 0058,
  0064, 0067, 0070, 0085, 0086, 0087, 0117, 0119, 0159, 0189, 0195, 0197, 0204, 0205
- **L (28):** 0001, 0002, 0011, 0012, 0035, 0045, 0060, 0062, 0063, 0069, 0072, 0076, 0078, 0080, 0094, 0095,
  0097, 0098, 0100, 0111, 0120, 0148, 0162, 0163, 0165, 0180, 0186, 0201
- **T1 (27):** 0016, 0025, 0054, 0061, 0068, 0077, 0107, 0109, 0112, 0121, 0122, 0123, 0125, 0129, 0130,
  0131, 0132, 0133, 0134, 0135, 0136, 0139, 0140, 0142, 0143, 0145, 0146
- **I (10):** 0015, 0017, 0021, 0024, 0066, 0154, 0156, 0158, 0161, 0192
- **F (19):** 0042, 0055, 0057, 0059, 0099, 0149, 0150, 0151, 0152, 0155, 0183, 0185, 0187, 0191, 0194, 0207,
  0208, 0209, 0210
- **U (7):** 0019, 0034, 0049, 0092, 0096, 0153, 0157
- **R (7):** 0007, 0047, 0048, 0051, 0053, 0084, 0190
- **T2 (18):** 0039, 0040, 0052, 0082, 0089, 0090, 0093, 0101, 0102, 0103, 0108, 0110, 0116, 0127, 0144,
  0170, 0171, 0182
- **T3 (17):** 0031, 0038, 0050, 0075, 0104, 0105, 0113, 0114, 0118, 0128, 0137, 0166, 0167, 0168, 0177, 0178, 0179
- **K (6):** 0036, 0106, 0115, 0188, 0202, 0203
- **G (10):** 0009, 0037, 0043, 0046, 0088, 0138, 0147, 0169, 0198, 0200
- **D (8):** 0003, 0022, 0074, 0081, 0141, 0184, 0193, 0196
- **C (8):** 0041, 0056, 0065, 0073, 0091, 0124, 0126, 0164
- **E (7):** 0026, 0033, 0044, 0071, 0079, 0083, 0206
- **X (8):** 0160, 0172, 0173, 0174, 0175, 0176, 0181, 0199

BUG-0106 is classed in K, as a recorded owner rule that never reached the tool, not in T2.

## Appendix B. Value-affecting entries (V, 68)

0001, 0004, 0005, 0006, 0008, 0010, 0011, 0013, 0014, 0015, 0017, 0018, 0019, 0020, 0021, 0023, 0024, 0027,
0028, 0029, 0030, 0032, 0034, 0036, 0045, 0047, 0048, 0049, 0051, 0053, 0058, 0060, 0063, 0067, 0069, 0070,
0072, 0076, 0078, 0084, 0085, 0087, 0088, 0092, 0094, 0095, 0096, 0097, 0119, 0120, 0147, 0148, 0157, 0159,
0161, 0163, 0165, 0186, 0188, 0189, 0190, 0192, 0195, 0197, 0201, 0202, 0203, 0205
