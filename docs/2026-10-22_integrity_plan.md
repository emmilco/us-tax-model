# Integrity plan — 2026-10-22 (v7, amended 2026-10-24 and 2026-10-26)

**Owner amendment, 2026-10-26:** the remaining work is re-sequenced and the gate for resuming
coverage (item 2.6) is fixed in `2026-10-26_plan_revision.md`, which controls the execution order.
TY2026 is the target year.

**Owner amendment, 2026-10-24:** remaining human packets, future stage source readings and the
ten-ruling sample are optional. The owner completed item2; all original findings are preserved.
Independent source/calculation checks carry the completion requirements. Confirmed defects require
correction, regression cases and broader independent checks instead of automatically assigning more
human packets. Online interpretation may supply separately recorded, non-authoritative soft evidence;
it earns no worked-value, human or scoreboard credit. See `2026-10-24_validation_policy.md` for the
controlling policy, provenance requirements and execution order. Earlier decisions below remain history
where superseded by this amendment.

A plan to bring the project to high integrity, meaningful validation and completeness, under the three pillars:
completeness, correctness, and a sound evidentiary basis. Drafted jointly by two audit sessions (tax-audit1 and
tax-audit2, both Claude Fable 5.1) from the evaluation in `docs/2026-10-22_project_evaluation.md` and two rounds of
investigation; each session read the other's draft adversarially. The owner's decisions of 2026-10-22 (recorded
below) were given in the tax-audit2 session and relayed to tax-audit1. The audit sessions did not commit this file.

Items are ordered by integrity bought per unit of work. Each gives what changes, who does it, the effort, and a
done-when that cannot be met without the integrity actually improving. "Elliot" marks work only a human can do.

## Continuation: human-reading integration (2026-10-22)

The first complete review path is being verified on item 2. Human source reading is **H** in the
report, separate from **B**, which remains human-calculated expected values under spec 6.1. A
reading earns H on its printed line and the helpers actually expanded in the packet, with the
reader named. It requires MATCH, the reader's reason, a current per-line receipt across form
boundaries, and the exact log committed with that reader as author. This corrects the original
plan's use of B for source readings. After owner feedback that one verdict was overwhelming, item 2 is now fourteen separate questions
shown one at a time, with credit restricted to the computation actually reviewed. The owner has not
yet completed the packet; partial verdicts are saved. BUG-0104 records this change. BUG-0101 to BUG-0103
record the integration, freshness and check-order gaps found while tracing this path.

## The position at plan adoption, stated plainly

Every construction to date (authoring, second transcription, render comparison, class M hand-work, the blind
fixture predictions, and both audit sessions) is one model family. Evidence from outside it comes from three
places only: a human reading (class B, none yet), a second model family (none yet), and the two engines (18
summary lines). Under this plan, human evidence will exist for the twelve read lines only; whole returns are
checked by two model families (Claude, DeepSeek) and four engines, two of them line-level (OpenTaxSolver,
UsTaxes). That is outside the Claude family, which is what the trust statement needs; it is not human, and the
spec says so.

## Scoreboard

One number the whole plan moves, printed at the top of `reports/2025/evidence.md`, with its three sub-counts
beside it (class B, second-family reading, engine) so a move in one cannot hide a fall in another:

> the share of computed lines with at least one outside-family assertion.

Definitions, so the number cannot be inflated:
- A computed line is one whose atom is not `input`, `param` or `copy`.
- An engine assertion counts only when (a) the engine computes the value rather than receiving it as input;
  (b) the comparison ran on generated returns where the line is nonzero on at least 50 cases; (c) fewer than
  half of those returns were excluded for engine limitations.
- An H assertion counts only from a human source-reading log meeting item 1.1's rules. Class B remains a human-worked expected value.
- A second-family assertion counts only from a run meeting item 1.3's agreement floor, or a class M log under
  item 1.2 whose model is not a Claude model.
- An assertion on a `copy` line credits the line it copies from, following the chain to the first non-copy line
  (a copy's value equals its source's exactly, so agreement on the copy is agreement on the source); the report
  marks such credits "via <copy line>". Owner's decision 2026-10-22.

Today: the engines' 18 summary lines, against a denominator still to be computed under the definition above.

## Sequencing rule

The build session owns the tree; `tools/green.sh` hashes untracked files too, so nothing lands without a green
check-all on the full tree. Phase 0 edits are made by one session, after the current run, one commit each.
Item 0.3 goes first: it touches nothing the suite reads.

## Phase 0 — hours each; honest reporting before anything else

0.3 Repository hygiene (first, see the sequencing rule). LICENSE (Apache-2.0 code, CC0 data); README with the
    trust statement, the standing notices, the coverage list and the one command; `handoffs/` for the eleven
    superseded handoffs, their PROJECT_INDEX rows moved; `interview/README.md` rewritten; spec and design
    reconciled (Lean Check soundness dropped from design 2.6; rounding default versus deferred).
    Done when: the files exist, PROJECT_INDEX is updated, check-all is green.

0.1 Evidence report corrected and extended (`engine/src/fixtures.ts`, `evidenceReport`).
    - Class M gets its own column (today "M" falls to R at the class mapping, fixtures.ts:165).
    - Stage 1's 57 "C" cases relabelled R with a note (Lean agreement is not an independent engine; spec 6.1).
    - The ~40 blind-predicted Stage 15/16 returns and `qdcg.handworked.single` are rerun through `classm.py`
      so they earn M with the model, prompt hash and snapshot record spec 6.1 requires (owner's decision,
      2026-10-22); until then they stay R.
    - An engine-differential column fed from `tools/engines` output under the scoreboard's definition, and the
      scoreboard line with its sub-counts.
    Done when: evidence.md shows A B C M R plus the engine column and the scoreboard; zero B rows without a
    named human; the three sub-counts are printed.

0.2 Citation integrity (`tools/citations.py`, `engine/src/check.ts`).
    - Forbid whole-form span locators on computed lines (the audit counted 187 over all lines; measured under this
      item's definition on 2026-10-22: 54 computed lines carry one, 164 span segments over every citation in the
      form files; 610 of the 1,756 segments on computed lines name no page).
    - The 1,252 quote checks stay. New: on a computed line every segment carries either a quote or a printed
      line number with label words; a form-line locator is verified by finding that line number beside those
      words anywhere in the form document; an anchor that is only the document title is rejected.
    Done when: citations.md reports 0 span locators on computed lines, 0 unchecked segments, 0 title-only
    anchors.

0.4 Regime honesty in the spec. 6.5 names the shared-reader blind spot and that the engine differential is
    required for every tax year (item 2.1 inherits it); the trust statement says all constructions are one
    model family until Phase 1 changes it, and after Phase 1 that whole returns are checked by model families
    and engines, not by a human; 6.1 says what the engine differential is and is not.
    Done when: the spec diff is reviewed by the owner.

0.5 Bug inventory entries for the audit findings (spec 6.6 requires every defect caught by any reading to be
    recorded before or with its fix): the class-M-to-R mapping; the B mislabel; the 187 span locators and 733
    unchecked locators; the Form 8889 marital proxy. Catch method: "human-directed audit".
    Done when: the entries exist and `check_bug_inventory.py` passes.

## Phase 1 — days; evidence from outside the model family

Order within the phase: the implemented packet and transport tools (1.0/1.0b) support the remaining
work. Engine comparisons, source adjudication and independent calculations proceed alongside each
other. An engine disagreement gets priority investigation. Optional human reading (1.1) does not
delay engineering or completion of the independent-evidence requirements.

1.0 Human-reading packet tool (agent, hours; prerequisite to 1.1). The project already has
    `tools/extraction/page_review.py`, which renders each archived page to PNG and shows it beside the
    project's text in a two-pane local HTML (writing the git-ignored `.extraction-review/`). This item extends
    that shape: one HTML per reading-list item with the cited page images on the left and, on the right, each
    line's printed number, IRS label, rendered English and YAML expression, with an empty verdict box per line.
    Verdicts save to `reviews/2025/human/<form>.md` in the 1.1 format with the subject hash. Optionally served
    through lab-server (QMS 9.2) so the owner can read on a tablet.
    Done when: the twelve packets open; every line of the reading list appears in one; a verdict typed in the
    page lands in the log with the subject hash.

1.0b Second transport in `call_model` (`tools/transcription/transcribe.py`), built once and used by 1.2, 1.3
    and the `classm.py` rerun of item 0.1. One hosted API (DeepSeek; GPT-6 dropped by the owner's decision
    2026-10-22 to simplify), so gpu-broker does not apply; Annex A
    (AISP, `~/.claude/AISP.md`) governs and is read before the first build step; credentials, isolation and the
    aiuser sandbox follow it. The job is fixed-prompt: output is parsed as YAML, verdicts or worked values and
    compared, nothing executes from it. The data sent is synthetic figures and public IRS text only. The model
    name is recorded in every log as the review tools already do. QMS 11.1 is untouched: no Anthropic API.
    Done when: `transcribe.py --model <non-Claude>` runs end to end on one form and its log records the model.

1.4 Engine differential extended per form, and two line-level engines added. (a) Per-form mapping for the
    engines in use. Verified against the installed package: PolicyEngine-US has
    variables for the dependent care credit, the saver's credit, the residential energy credits, the HSA and
    IRA deductions, taxable social security, self-employment tax, the EITC, the CTC and ACTC, the senior
    deduction, QBI and alimony; none for the taxable state refund. Today 18 summary lines; the Stage 8–16
    forms are seen only through AGI and taxable income. Map the per-form result lines (f2441, f8880, f5695,
    s8812, eic, f8889 line 13, ira, se) in `tools/engines/run_engines.py`.
    (b) OpenTaxSolver (TY2025 v23.06+, C, GPL-2.0: Form 1040, Schedules 1–3 and A–D, Forms 8949, 8889, 8995,
    beta 2441; local, no account, text input and output) and UsTaxes (TypeScript, AGPL-3.0, TY2020–2025) added
    as third and fourth engines through the adapter pattern of `tools/engines/`, installed into the git-ignored
    `.engines/`. The project's own research (`research/02_prior_art_tax_software.md`, comparison table and
    "Oracles for differential testing") named both as line-level oracles covering the slice and PolicyEngine-US
    and Tax-Calculator as "totals only"; the build used only the latter two. Line-level oracles compare the
    worksheet lines themselves (Schedule D, the QDCG worksheet, Form 8889), not just AGI and tax. Each
    difference needs a cited cause, as now; each engine's limitations are recorded once in the adapter.
    Before writing the adapters: download each package, read its input format and confirm which forms it
    reaches; an engine's line counts toward the scoreboard only for forms it is confirmed to compute, under
    the same three-part definition as (a). Known limits from the research: OpenTaxSolver's published list has
    no Schedule C or SE and AMT was pending in January; UsTaxes' maintenance and its QDCG worksheet were not
    confirmed (research/02 line 110); both are TY2025 only, so item 2.1's TY2026 rehearsal cannot use them
    until their 2026 releases, expected early 2027 (research/02 line 97); tenforty is not independent of
    OpenTaxSolver and is not added.
    Done when: engine_differential.md lists all four engines with per-form lines and 0 unexplained; the
    scoreboard's engine sub-count rises under its definition (computed, nonzero on 50+ cases, under half
    excluded), with OpenTaxSolver and UsTaxes columns counted separately.

1.1 Optional human source reading against the IRS pages through the packets
    of item 1.0. Owner's answer 2026-10-22: yes, provided the packet UI lets him match an image of the form to
    the lines asked. [Elliot, one sitting of 10 to 30 minutes per item]
    Rules: the agent prepares the packet with every verdict empty; the owner fills every verdict in his own
    words; the log is `reviews/2025/human/<form>.md` with page, quote, reading, verdict, date, reader, and the
    subject hash from `tools/transcription/subjects.py`, so `check_logs.py` flags it stale when the line
    changes (the T-044 lesson); the commit's git author is the named reader; `check_logs.py` rejects a human
    log whose reader field names a model or whose last commit author (from `git log`) is not the named reader.
    evidence.md's H column reads only such logs; B is reserved for worked values. If offered, the owner may also sample ten rulings from
    items 1.2 and 1.3 that overruled a non-Claude model.
    Credit when offered: the log meets those rules and evidence.md shows H with the owner named.
    Neither the reading list nor the ruling sample is a required completion gate.
    Reading list (stakes × churn; pages are form-feed pages of the `.cols.txt` files; items 10 and 11 are new
    2025 law that no prior-year diff could catch):
     1. Tax on taxable income: f1040.gate.qdcg_applies, f1040.gate.sdtw, f1040.non_sdtw_tax, tax_on_amount
        (the $100,000 switch), one Tax Table cell. i1040gi p. 33, p. 80, pp. 68–79. Every return.
     2. Standard deduction: sa.standardbase, sa.boxes_age65, sa.boxes_blind, sa.standard, sa.itemizes;
        person.age65. i1040gi pp. 33–35. Every return.
     3. QDCG worksheet lines 5–25 (qdcg.yaml). i1040gi p. 38.
     4. EIC Step 5 earned income, Worksheet A lines 1–6, Step 1 limits (eic.line1..line6, eic.top_limit).
        i1040gi pp. 40, 42, 43, 46. Largest refundable dollars.
     5. CTC qualifying child and the Schedule 8812 chain: dependent.ctc_child, dependent.ctc_amount,
        dependent.odc_person; s8812 lines 4–7, 10–12, 14 and Credit Limit Worksheet A. f1040s8812 p. 1;
        i1040s8812 pp. 3–6.
     6. Self-employment chain: sc line 31 to se.line2 (person.se_line2 binding), se.line12 and line13 to
        Schedule 1 line 15; person.se_rrta. f1040sc p. 1; f1040sse p. 1; i1040sse p. 2.
     7. Form 8889 line 3 chart and line 13. i8889 pp. 4–6.
     8. IRA Deduction Worksheet lines 7–12 with the round-up to $10 (person.ira_*, ira.yaml). i1040gi
        pp. 97–98.
     9. State and Local Income Tax Refund Worksheet lines 1–9 (refund.yaml). i1040gi pp. 88–90.
    10. Schedule 1-A phase-outs: s1a.line9_calc, line17_calc, line26_calc, line32_calc and their steps.
        i1040gi pp. 101–109.
    11. SALT limit chain: sa.line5d..line5e (saltbase, saltthreshold, saltreduction, saltlimit). i1040sca p. 7.
    12. Social Security Benefits Worksheet lines 1–18 (ssb.yaml). i1040gi pp. 31–32.
    Optional 13. Simplified Method Worksheet (retirement.yaml). i1040gi pp. 29–30.

1.2 Whole-return hand-work by a second model family (replaces the consumer-calculator step; owner's answers
    2026-10-22: no calculators; DeepSeek; GPT-6 dropped to simplify). DeepSeek, in an isolated context given
    only the archived text and the inputs, works 3–5 returns drawn from existing fixtures and chosen to
    exercise Stage 14–16 features, plus the ~40 blind-predicted returns that item 0.1 sends back through
    `classm.py`. Records are class M logs with model, prompt hash and snapshot per spec 6.1;
    the scoreboard's second-family sub-count reads them. A cause for a difference is a cited IRS sentence that
    decides which side is right (a BUG entry when it is the project); the record reports how many differences
    resolved against the project. [agent, a day, after 1.0b]
    Done when: each return has a DeepSeek working logged; every difference has a cited cause; the
    second-family sub-count rises. Whole-return evidence from outside any model family comes from item 1.4's
    four engines, not from this item.

1.3 Second-family reader for transcription and render on all 55 forms, through 1.0b. Transport: DeepSeek
    over its hosted API (owner's decision 2026-10-22: ample DeepSeek credit). Rule the disagreements, every ruling that overrules the second family citing the
    source sentence (the existing regime).
    Agreement floor, as a noise rate (owner's decision 2026-10-22, replacing the raw 90% agreement, which one
    correct systematic objection would fail): the second family's disputes that are ruled "model error", over the
    lines it judged, must be at most 10% per form; above it, choose a stronger model and do not count the run.
    A dispute ruled a finding or a representation difference is not noise.
    Done when: every log records a non-Claude run above the floor with no open ruling; the log states the
    independence yield (disagreements the second family raised that the Claude reading did not), zero being a
    visible result; defects found are BUG entries. The owner's ten-ruling sample is optional (item 1.1).

    Execution update 2026-10-23: the noise gate and response provenance checks are implemented and
    tested. All 55 DeepSeek render reviews have returned; the full transcription batch has returned
    with final failed-job retries underway. Source adjudication, family promotion and the owner's
    sample remain incomplete. See `docs/2026-10-23_independent_validation.md`; no milestone completion
    or worked-value evidence is inferred from completed API calls.

1.5 Class M made to bite: restrict jobs to printed lines, or present helper lines in the model's own terms.
    Today 2 corrections in 484 disagreements; 222 ruled "representation".
    Done when: the "representation" share of class M rulings is below 10% and the branches reached by class M
    cases (`reports/2025/coverage.md`) do not fall.

1.6 Mutation equivalences: write the evaluation-order semantics the 89 arguments rely on into spec 4 /
    design 2.5 (refusals checked at line entry; all/any order; refusal outranks unknown); a second reader over
    the 89; recurring shapes made mechanical like copy-chain. A survivor whose argument cannot be made
    mechanical is killed by a fixture, not kept by a better argument.
    Done when: at most 20 of the 89 remain prose-only, each named with its reviewer; no new prose-only entry
    is added.

1.7 Direct File's fact dictionary read against the household predicates (owner's decision 2026-10-22). The IRS's
    own TY2024 encoding (IRS-Public/direct-file, CC0, archived; developed with Chief Counsel) of the dependent
    tests, head of household, the earned income credit, the child tax credit and the standard deduction is
    compared, predicate by predicate, against dependent.yaml, household.yaml, eic.yaml, s8812.yaml and sa.yaml.
    It is a reader from outside the model family on the household logic no engine reaches; year-shifted, so
    each difference is first checked against the 2024 and 2025 texts (sources/2024/, sources/2025/) before it
    counts as a finding. Its arithmetic is not used (TY2024, tax-table midpoint rounding, no Schedule D).
    Done when: a log in reviews/2025/direct-file/ lists every predicate compared, the reading on each side, and
    the ruling with its source sentence; findings are BUG entries or register entries.

Stop rule for Phase 1, revised 2026-10-24: an error is any case where the IRS text supports one value
and the evaluator gives another on a reachable return, whether or not a register entry follows.
Confirmed errors require correction, source-backed regressions and expanded independent checks of
the affected regime. A cluster of errors pauses coverage until that investigation closes. No automatic
increase in mandatory human reading remains. Unexplained differences and unmet independent-evidence
requirements cannot be cleared by making human review optional.

1.8 Secondary interpretation as soft evidence. Search professional explanations, software notes and
    practitioner discussions for support, counterexamples and competing readings, especially at source
    ambiguities. Record year, facts, author, URL, dates, a short captured passage/hash, primary references,
    source lineage, opposing material and uncertainty under `research/secondary/`. This supplements
    source adjudication, earns no assertion/scoreboard or noise-floor exception, and is kept out of the
    existing blind source-only prompts. The first example covers standard-deduction dollar increments.

## Phase 2 — a week or more; completeness and a fileable year

2.1 TY2026 rehearsal now on the posted drafts (Form 1040 of 2026-09-17; Schedules 1, 1-A, A, C, SE, 8812;
    instructions for C, SE, 8812). Archive under `sources/2026` marked draft (spec 7: drafts cannot back a
    release); 2026 is never added to `years.json`, so `check-all --year 2026` is checked but never green by
    design. Run `year_diff.py`, `--adopt` into the year, `fixtures_year.py`; log every tool defect.
    Done when: `reports/2026/year_diff_from_2025.md` and `fixtures_from_2025.md` exist (the latter listing
    what would be re-recorded) and the defect list is worked.

2.2 "Complete" defined in spec 2.4 (text below). Done when: the spec diff is in; the roadmap page shows status
    per condition.

2.3 Unmeasured-gate prevalence buckets (method below). Done when: filer_coverage.md states a bound.

2.4 Form 8889 reads a marital answer instead of f1040.status in `f8889.married_family` and
    `f8889.age55_unmarried` (the only two such proxies of 38 grep hits; eic.yaml already carries
    `eic.married`), with a fixture. Done when: the fixture passes; the f8889 render review is rerun.

2.5 Product surface: values sheet in printed order with helpers folded; scope screens rewritten as lay
    questions, drawing on Direct File's user-tested screen wording and knockout screens (its flow XML and
    screen components, CC0) wherever a situation matches, and the screen review rerun. A rewritten screen keeps its citation and its refusal set unchanged;
    the rerun checks wording only. Notices and the coverage list in every output.
    Done when: the interview-exercise walk is re-recorded; screen_review.md is closed; a diff shows no refusal
    set changed.

2.6 Coverage stages resume (Schedule E, the rest of Schedule 1, the premium tax credit) only after item 2.1
    shows adoption works and the defect investigations required by the revised stop rule close;
    each stage closes under the standing regime, with human readings optional.

## Lawyer review

Trigger: any distribution beyond the owner. Questions: `research/04_legal_liability.md`, "Needs a real
lawyer". A gate on distribution, not on building.

## Standing regime after this plan (what "high integrity" means per stage close)

- transcription and render reviews under two model families; class M on printed lines only
- evidence report with M and engine columns and the scoreboard; citations check with 0 unchecked
- one second-family whole-return working per stage; human source readings and ruling samples optional
- engine differential mapping extended wherever an engine models the new feature
- every tax year adopted under the full check-all including the engine differential
- a stage handoff reports the scoreboard and the per-form outside-family coverage first, fixture counts last

## Text for 2.2, "complete"

A release of this project is complete for a tax year when four conditions hold, and the roadmap page reports
each: (1) Coverage: the estimate in filer_coverage.md is at or above the goal for the measured situations, and
every refusal gate the estimate cannot measure carries a prevalence bucket with a source, so the report states a
bound on what the headline leaves out. (2) Refusals: every situation outside scope is reached by a cited gate
with a fixture, and the interview arrives at the refusal before asking for data it cannot use. (3) Product
surface: the values sheet, derivations, path explanations, ambiguity notices, refusal explanations and standing
notices of spec section 8 reach the filer in the output, and every question asked has interview wording a lay
filer can answer. (4) A fileable year: the definitions are built from the final instructions of a tax year whose
return can still be filed on time, under the full check-all. Coverage growth counts toward (1) only; a stage is
not complete for the year until (2) to (4) hold for its lines.

## Text for 2.3, prevalence buckets

Each refusal gate with no IRS count or microdata variable is assigned one of three buckets with a source:
common (plausibly above 1% of returns), uncommon (0.1% to 1%), rare (below 0.1%). Sources, in order of
preference: an IRS Statistics of Income cell that counts a superset of the situation (an upper bound); a count
from a published IRS or GAO study; a prevalence from the PolicyEngine microdata for a related variable; else the
author's reasoning stated in a sentence. filer_coverage.md then reports, beside the headline, the sum of the
common buckets' upper bounds as the most the headline could overstate coverage, and lists the gates by bucket.
A gate's bucket is reviewed when its stage is reopened or its category is retired.

## Checked and set aside

- IRS MeF ATS scenarios (TY2025, scenarios 1 and 5 pulled): inputs only, computed lines blank; not class A.
- Filing status standing in for marital status: 38 grep hits, 36 legitimately about filing status; see 2.4.
- Fixture expectation keys that resolve to no line fail the case ("not evaluated"); the odd keys listed at
  the end of evidence.md are instance keys, not dead assertions.
- Consumer-calculator records (the Stage 5 design's FreeTaxUSA/OLT step): dropped by the owner's decision;
  replaced by item 1.2 (model hand-work) and item 1.4(b) (line-level engines).
- A browser-driven consumer calculator with the owner present: possible, but unnecessary once 1.4(b) exists,
  and it carries the hosted-terms question; not adopted.

## Owner's decisions, 2026-10-22 (given in the tax-audit2 session)

1. Item 1.1, the reading: yes, provided the packet UI lets him match an image of the form to the lines asked
   (item 1.0 is the response).
2. Item 1.2, calculator cases: no; run them through DeepSeek and GPT-6 instead (item 1.2 as rewritten).
3. Item 0.1, the blind-prediction label: rerun through `classm.py` so they earn M.

4. Item 1.3, the second-family reader: DeepSeek (ample credit).
5. OpenTaxSolver and UsTaxes added as third and fourth engines (item 1.4(b)), in place of any consumer
   calculator.
6. GPT-6 dropped everywhere to simplify; DeepSeek is the single second family.
7. An assertion on a copy line credits its source line (Scoreboard); one commit for Phase 0; the spec wording of
   item 0.4 approved.
8. Direct File's fact dictionary compared against the household predicates (item 1.7); its screen wording drawn
   on for item 2.5.
9. Direct File findings F1 to F4 accepted with the recommended handling (BUG-0095 to BUG-0097; the foster-parent
   gloss as a register entry).
10. New refusals from Direct File's knockouts: a married filer in a community property state filing as head of
    household; a filer or spouse under 16.
11. The Tax Computation Worksheet row results re-keyed from column (d) to the Tax column (the first DeepSeek render
    yield); value-neutral.
12. The agreement floor measured as a noise rate (item 1.3).
13. The reading list doubled now (items 14 onward chosen by the same rule); the owner reads the first twelve first.
14. Log-check policy for an optional family: a stale log fails, an open ruling does not.
15. Amendment 2026-10-24: remaining human packets, future stage source readings and the ten-ruling
    sample are optional. Preserve findings; incomplete/stale/negative readings earn no H and do not
    block unrelated validation. Confirmed defects require correction, regression and broader independent
    checks; automatic doubling of human reading is retired. Four-engine and blind-calculation work remain.
16. Amendment 2026-10-24: online tax interpretation/commentary may support or challenge a recorded
    reading as soft evidence, with year/facts, attribution, dates, captured passage/hash, lineage and
    contrary material. No official-source substitution, blind-prompt contamination or scoreboard credit.

Stop rule status: fired on 2026-10-22 with three value errors (BUG-0094, BUG-0096, BUG-0097), subsequently
fixed. Coverage stays paused for the unfinished independent-validation/year-rehearsal gates. Decision15
retires the mandatory-reading consequence of decision13; the expanded list remains optional research UI.

## Open question for the owner

None.

## Provenance

Inspected by the audit sessions, between them: `engine/src/fixtures.ts` (evidenceReport, loadCases,
testFixtures), `engine/src/differential.ts`, `engine/src/mutate.ts` (the equivalence rules and three arguments
read against the YAML), `engine/src/eval.ts` (refusal order), `tools/transcription/transcribe.py` (call_model),
`tools/engines/run_engines.py` and `compare.py`, the installed PolicyEngine-US variable tree, `tools/year_diff.py`
and `fixtures_year.py` headers, `tools/extraction/page_review.py` (by description in PROJECT_INDEX), every
fixture file's evidence labels, the three review log sets' ruling tallies, the bug inventory's catch tags,
`reports/2025/{evidence,coverage,mutation,engine_differential,filer_coverage,interview-exercise}`, se.yaml,
f8889.yaml (line 3 chart), sa.yaml (standard deduction), s8812.yaml Part I, eic.yaml Worksheet A, f1040 lines
11a–15, each against its archived pages; two whole-return fixtures recomputed by hand; the IRS draft-forms
listing and two TY2025 ATS scenario PDFs.
Inferred (unverified): the 90% floor and 50-case threshold (judgment numbers); page numbers for reading-list
items 4–6 and 10 (from title searches, not read); that TY2026 final instructions will arrive on the 2025
pattern; that DeepSeek is reachable from this machine under the AISP (not tested); that OpenTaxSolver's and
UsTaxes' input formats are scriptable as the research describes (not downloaded or run).
