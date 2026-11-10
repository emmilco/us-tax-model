# Question review: design for the owner's approval (phase 3, lane C)

Status: proposal. Nothing here has run a model. The prototype `tools/transcription/question_review.py` builds and
prices the prompts offline (`--dry-run`) and measures what the existing reviews cover (`--coverage`); it has no
code path that calls a model.

## 1. The problem, measured

Question wording that diverges from the source is the project's largest class of value-changing bugs (class Q: 30
bugs, 26 value-changing; `docs/2026-10-29_bug_root_cause_analysis.md`). Every mechanical check supplies answers
directly, so a wrong question never moves a tested value. Only reviews that put the wording beside the source can
catch it.

**What the interview asks.** 563 federal and 43 New York input lines are questions. That excludes 9 federal and 14
New York inputs of definition documents (`tax_on_amount`, `tcw`, `se`, `aqee`, `ny_rs`, `ny_city_rs`, `ny_tcw`,
`ny_tcw_first`). Those are parameters their callers bind, not questions: the brief's figure of 572 counted them.
The federal questions by type: 262 Bool, 249 NonNegDollars, 32 Enum, 16 Count, 4 Dollars. 440 of the 563 carry help text in the interview (`interview/2025/questions.yaml`),
and 4 carry an authored prompt that replaces the line's own question text. Every question is in the `full` or the New York
profile.

**Which existing reviews judge a question's wording** (measured by `question_review.py --coverage` on this tree).
Judged means a review asks a model whether this question's wording is right. Context means a prompt shows the
wording while it judges something else.

| Review | How it sees a question | Federal inputs | New York inputs |
|---|---|---|---|
| Render (`render_compare.py`) | judged: a printed input line ("Input — question") against its own cited text. It is blind to help text and to the lines that read the answer | 246 (236 render only, 10 also screens) | 4 |
| Screen (`screen_review.py`) | judged: a refusal-gate screen against the lines it refuses. It is shown `expr.source` only, never the help | 59 (49 only, 10 also render) | 6 |
| Gate condition (screen gate review and false-no) | judged: the condition with its help, against the gated lines | 4 (3 only, 1 also render) | 0 |
| Gated question (inside a gate's prompt) | context only | 31 (11 of them judged by nothing else) | 1 |
| Completeness | context: every input is listed as `QUESTION` in its form's prompt, and the reviewer looks for uncovered rules | all | all |
| Transcription | context: inputs are given as the form's interface | all | all |
| **Judged by none** | | **264 of 563 (47%)** | **33 of 43** |

The 264 unjudged federal questions by type: 137 Bool, 89 NonNegDollars, 24 Enum, 10 Count, 4 Dollars. By form:
person 51, dependent 43, retirement 21, f5695 13, scveh 13, refund 12, carloan 11, f8889 11, s1 10, asset 9, sales
8, f2441 7, and 22 forms with 5 or fewer.

Two more gaps sit inside the "judged" rows:
- **Help is reviewed almost nowhere.** Of the 246 render-judged federal questions, 175 have help text the render
  review never sees. The screen review shows only `expr.source`. Only the gate reviews show help (`gates.wording`).
- **Judged against the wrong text.** The render review judges a printed input against its own line's citation.
  It does not judge against the lines that read the answer, which is the failure the root-cause analysis names
  for BUG-0032. 362 of the 563 questions are read only by helper lines. For those, the printed line that
  finally uses the answer is two or more steps away.

Side finding: `reviews/2025/screens/screen_review.json` holds 7 screen records for inputs that no longer gate a
refusal (`dependent.kidnapped`, `dependent.other_claimant`, `f4952.carryover`, `household.credit_disallowed`,
`sa.spouse_extra`, `scope.schedule1a`, `sd.carryover`). `check_screens.py` flags orphaned gate records but not
orphaned screen records.

## 2. Decisions the design settles

Each item gives a recommendation and the alternatives. Section 5 lists the decisions the owner must make.

### 2.1 Scope and unit

**Recommendation: one unit per question (input line), for all 563 federal and 43 New York questions.** A gated
question's prompt states its gate condition, but the condition is not part of the question's subject, because
the gate has its own review (as `screen_review.screen_gate` does).

- *Per question.* This gives focused attention. A changed question makes only that unit due, and a ruling attaches
  to one question. Estimated first pass: $41.33 federal plus $2.24 New York (section 2.5).
- *Per form, or per collection (here the same thing: `person`, `dependent`, `sc` are forms).* Estimated at $11.40
  federal (47 prompts). It is cheaper because the pages are shared. But every wording change on the form makes the
  whole form due again. Long prompts also behave like a random sample of the gaps: completeness had to adopt
  sampling for exactly this reason. A form prompt holding 62 questions (person) would get the attention that
  completeness gives one rule in a section.
- *Per cited page cluster.* This groups questions that share a source paragraph, which is the sibling pattern in
  the root-cause analysis. It is the cheapest per finding if the clusters hold. But the units would have no stable
  identity across years, and rulings would not attach to a question.

Size guard: 6 questions have more than 20 readers (`f1040.status` 68, `sales.box` 35, `person.role` 33,
`sales.route` 33, `f1095a.uniform` 28, `sa.excluded_income` 24), and 9 prompts exceed 100,000 characters
(`f1040.status` is 453,462 characters with 53 pages, about $0.64). Recommendation: above 20 readers, list the
readers by document with their labels only, and give pages for the question's own citation alone. Filing status
and roster role are better judged by the household and screen reviews that already cover them.

In or out, for owner decision: the 63 federal and 6 New York questions that a screen or gate review already
judges ($4.60). Recommendation: include them in the question review, because it checks a different property: what
the answer feeds and the help text. Then also add help text to the screen review's prompt, which is a one-line
change (`screen_review.build_prompt` uses `sline['expr']['source']`; `gates.wording` already has prompt and help).

### 2.2 One review or two (wording and T-253 type and range)

**Recommendation: one model review with TYPE as one of its verdicts, plus a mechanical part of T-253 kept out of
the model.**

- The two checks read the same inputs: the question, its type, the readers and the cited pages. A second review
  would pay for the same pages twice, about $41 more. In the prototype, the TYPE instruction adds about 300
  characters to a prompt of 28,000.
- T-253's other half is not a review. The model of the forms has no `range` on inputs (spec 4.1: `Count` is "Non-negative
  integer", with no bound). Recording bounds (months 0 to 12, whole percent 0 to 100, a year) needs a schema field
  and engine validation, so the page can present selectors. That is a form-language change for the owner's design
  approval. The review's TYPE findings (each with a `bound`) supply its worklist.
- A mechanical pre-pass flags 13 federal type suspects (`question_review.py --coverage`). It is a lead list, not
  findings: Count questions that ask for a percent, rate or age (`asset.pct`, `person.sep_rate`, `retirement.age`,
  `retirement.combined_age`); month counts with no bound (`dependent.months`, `f8889.months_eligible`,
  `f8889.months_family`, `retirement.months`, `scveh.placed_date`); and the 4 signed `Dollars` inputs
  (`clcw.prior_11`, `clcw.prior_sd7`, `clcw.prior_sd15`, `dependent.ptc_magi`). `scveh.placed_date` asks for a year
  ("for example 2023") but is typed Count. No line reads it, so it only affects presentation (Schedule C line 43).
  `person.sep_rate` is a whole percent typed Count, so a rate such as 12.5% cannot be entered.
- *Alternative: two reviews.* This would keep each prompt's task smaller. It is worth doing only if the pilot shows
  TYPE findings crowding out wording findings or the reverse.

### 2.3 What the reviewer sees and returns

Modelled on `screen_review.build_prompt` and `completeness_review`. The prototype's prompt (`build_prompt`) gives:
1. The question as the filer reads it: the interview prompt (collection frame included) and the help, from
   `canonical/<year>/interview-full.json` and `interview-ny.json`.
2. The accepted answer: type, sign, bound and enum values (Enum values are shown as codes; the prompt should show
   the choice labels the page shows once those exist). It also gives the label, the note, every linked ambiguity
   entry (text at issue and the chosen reading), the question's citation, and the interview's citation where it
   differs.
3. The gate condition, when the question is gated (`gates.describe`).
4. Every line that reads the answer, with its label, rendered English (`rendered/`) and citation. Each refusal the
   answer gates is given with its form and remedy. Lines that read the answer only in `shown_when` are marked as
   display only.
5. The printed form lines the answer reaches through helper lines (at most 8, label and citation; `printed_reached`).
   These matter for the 362 questions whose direct readers are all helpers.
6. The archived pages that the question, its readers, their refusals and the interview cite (`transcribe.excerpt_for`):
   a median of 3 pages and a 90th percentile of 7.

It returns YAML: `verdict` is one of MATCH, NARROW, WIDE, WRONG_FIGURE, TYPE or UNCLEAR. The verdict is the most
serious finding, in that order. `findings` holds entries of the form `{kind, situation, source_text, why, bound}`.
NARROW and WIDE are the screen review's kinds, applied to an amount as well as a yes. WRONG_FIGURE covers another
box or line, before or after an adjustment, gross for net, or per person for combined. TYPE covers a sign, a bound,
a date or rate taken as a count, or a missing choice. UNCLEAR covers two reasonable readings that give different
values. The reviewer is told not to report style, or situations that a listed refusal or the gate already handles.
The system prompt follows the screen review's: no tools, YAML only.

Subject (what makes a unit due): **recommended** is a structured hash of the question's wording, help, type,
label, note, linked ambiguity ids, citation, and each direct reader's line and English. This follows
`gates.subject`, so a change to the review prompt applies prospectively, as the cost rules require. Leaving out
of the subject: the page text (it changes yearly, and year adoption makes everything due anyway), the gate
condition (it has its own review), and the reached printed lines. The alternative, the prompt hash without the
system prompt (as completeness does), is simpler, but an edit to any of the reached lines would make the
question due.

### 2.4 Fit with the sampled-review machinery and check-all

The review is the same pattern as completeness, screen and false-no (`tools/README.md`, "Sampled completeness,
screen and false-no reviews"):
- `question_review.py` takes `--inputs`, `--samples K`, `--force-rerun REASON`, `--approve-cost DOLLARS`,
  `--dry-run` and `--jobs`. Records go in `reviews/<year>/questions/<form>.json` (one file per form, as false-no
  logs per form, so lanes on different forms do not conflict). Each record holds one subject and its samples
  (`samples.py`; `SAMPLES_PER_MILESTONE` = 1). Raw prompts and replies go in `.transcription/questions/`, and the
  ledger kind is `question`. Pricing uses `spend.estimate` with the screen review's fit until the tool has its own
  ledger rows, and runs above the $3.00 gate are refused without `--approve-cost`.
- Rulings are per sample, `unruled:<input>#<k>` in `reviews/<year>/questions/rulings.json` with `subject_sha`, and
  `samples.carried` handles mechanical carry. `rule.py` records severity.
- `check_questions.py` is a check-all step (`jstep question_currency "--jurisdiction ny"`, beside
  `screen_currency`). A unit whose subject changed is due: listed, not failed. An unruled sample fails. A record
  whose input no longer exists is an orphan and fails. `--release` is added to `tools/release_reviews.sh`.
- Introducing it: when the check lands, all 606 units are due. Either the first release after it is gated on the
  full pass, or the step lists only until the first full pass has run (owner decision 4).
- `review_yield.py` gains the `question` kind (KINDS, rulings path, the "Caught by" word "question review").

### 2.5 Cost of the first full pass

Measured with `question_review.py --dry-run --by-form`. Every federal and New York prompt was built from this
tree and priced with `spend.prices()` and `spend.estimate()`. The tool has no ledger price yet, so the fit of
`screen_review.py` on Claude stands in: $0.0355 per call plus $1.34 per million prompt characters. Its sister fits
are false-no at $0.0724 plus $1.39 and completeness at $0.0924 plus $1.54. Under either of those, the federal pass
would cost about $63 or $77.

| Pass | Units | Estimate | Per unit: median / p90 / max |
|---|---|---|---|
| Federal, per question | 563 | $41.33 | $0.067 / $0.097 / $0.64 |
| New York, per question | 43 | $2.24 | $0.050 / $0.059 / $0.093 |
| **First full pass** | **606** | **$43.57** | |
| Federal, per form (alternative; the page union is computed, the prompts are not built) | 47 | $11.40 | $0.14 / $0.57 / $1.11 |

Federal per-question distribution: 86 units under $0.05, 295 from $0.05 to $0.075, 134 from $0.075 to $0.10, 44
from $0.10 to $0.20, and 4 at $0.20 or more. Prompt size: median 23,771 characters, 90th percentile 45,767. The
largest forms by total are person (62 questions, $4.18), f5695 (56, $4.09), sc (46, $4.00), dependent (50, $3.40)
and f1095a (42, $3.27). By coverage class: the 264 unjudged questions cost $17.86, the render-judged $19.87, and the
screen- or gate-judged $4.60.

The model calls are not the main cost. Adjudication is. In the screen review (the closest kind: one question
against the lines it stands for), 63 of 81 federal samples were not COVERS, with 216 findings in total (2.7 per
sample). If question samples behaved the same, a full pass would yield about 470 non-MATCH samples and about 1,600
findings to rule. Simple box-copy amounts should do better than screens, which summarize many lines, but that is a
guess, not a measurement.

**Expected yield, compared with the ledger** (`review_yield.py`, run on this tree; window since 2026-11-04):

| Kind | Calls | $ | Bugs caught (window) | $ per bug | Bugs, all time |
|---|---|---|---|---|---|
| screen | 137 | 13.62 | 5 | 2.72 | 52 |
| false-no | 59 | 6.45 | 3 | 2.15 | 3 |
| completeness | 237 | 72.37 | 33 | 2.19 | 90 |
| render (Claude) | 159 | 80.71 | 1 | 80.71 | 55 |

The screen review is the closest analogue, and its first pass on never-reviewed screens produced BUG-0032 (25
screens reworded). At the screen review's window rate, $43.57 would buy about 16 bugs. That is an extrapolation
from one kind's rate on a different population, and the true figure could be several times higher or lower. The
264 never-judged questions are a population no review has read, so no rate measured elsewhere transfers to them.
This is the case for a pilot.

**Recommended pilot (under the $3.00 gate, no approval needed): 40 units for about $2.90.** Stratify them: 15
unjudged Bool, 10 unjudged amounts or counts, 10 render-judged with help, and 5 screen-judged as a control. A
control that only re-finds known screen findings measures redundancy. The pilot measures the non-MATCH rate,
findings per sample, noise (model-error share), and value-changing defects per unit. Those figures decide whether
the full pass runs, whether the screen-judged questions stay in, and whether TYPE stays in the same prompt.

### 2.6 From finding to fix

- **Who rules.** An Opus adjudicator (judgment) reads each non-MATCH sample against the cited page. It rules each
  finding as one of: model error; covered (a refusal, gate or other question already handles it); a defect with a
  severity, where value-changing is high or medium and display-only is low; or an ambiguity (a register entry,
  which the owner decides if the readings change values). Rulings go through `rule.py` with `subject_sha`. A
  defect gets a `BUG_INVENTORY.md` entry (`new_bug.py`) with "Caught by: the question review of `<input>`".
- **What a fix touches.**
  - Wording, the usual case: `forms/<year>/<form>.yaml` `expr.source` (and `label` if needed), or the help or
    prompt in `interview/<year>/questions.yaml` or `interview/ny/<year>/questions.yaml`. Fixtures do not change,
    because they supply values. The ripple: the line's rendering changes, so a line-scoped render review is due.
    The form's completeness subject changes (its prompt lists every `QUESTION`), so one completeness sample is due.
    If the input is a screen or gated question, its screen or gate subject changes too. Each question fix
    therefore costs about one completeness sample per form ($0.3 to $1) plus line-scoped renders, so fixes should
    be batched per form per round (the once-per-round rule).
  - A question that must split (one answer cannot serve two readers: class U in the root-cause analysis): a new
    input id, which needs an `inputs` claim (`tools/claims.py`), plus fixture defaults (`fixtures/<year>/defaults.json`,
    with a `Fixture-default-changed` line if an existing default moves) and the interview-rules baseline.
  - TYPE: a type change (Count to Enum or Rate) moves fixtures and engine validation. A bound waits for the
    `range` field (2.2).
- **Lanes.** Fix work splits by form under `tools/claims.py`. The adjudicator writes the replacement wording into
  the ruling, so applying it is mechanical (Sonnet). Suggested clusters, by questions and by the help files they
  touch:
  - person, retirement and f8889 (95 questions);
  - dependent, household, eic and s8812;
  - sc, scveh, asset, s179 and f4562;
  - f5695;
  - f1095a and f8962;
  - sales, sd and div;
  - the rest of the federal forms;
  - New York.

  `interview/<year>/questions.yaml` is one file shared by every lane. Its entries are per input, so concurrent
  lanes conflict only textually. Merging the lanes in sequence is enough; claims are not needed for it.

## 3. The prototype

`tools/transcription/question_review.py` (self-test registered as `question_review_self_test` in
`tools/self_tests.py`, listed under "Scripts run by hand" in `tools/README.md`):
- `--coverage [--json PATH]`: the coverage table in section 1 and the mechanical type suspects.
- `--dry-run [--inputs a,b] [--by-form] [--write-prompts DIR] [--json PATH]`: builds every prompt and prices it.
  `--jurisdiction ny` does the same for New York.
- Without either flag it refuses: the review is not approved to run.

Not built yet (after approval): the call path, records, `check_questions.py`, the release step, the yield kind, the
structured subject, the size guard, and help in the screen review's prompt.

## 4. Limits of these measurements

- "Judged" is a property of the review tools' code paths (render's `_judged_lines`, `screen_review.screens`,
  `gates.units`), not a check that every such unit has a current log. The screen log does hold a record for every
  computed screen and gate: 59 screens and 15 gates federal (plus the 7 orphaned screen records, 81 in all), and 12
  New York records. Each is one grandfathered sample.
- Prices are fitted to another tool's calls. Replies to a question prompt may be longer or shorter than screen
  replies.
- The per-form alternative is estimated from its page union plus 4,000 characters per question. Its prompts were
  not built.

## 5. Decisions for the owner

1. **Unit:** review each question on its own (606 prompts, about $43.57 for the first pass), or one prompt per
   form (about $11.40 federal), at the cost of whole-form re-review on every wording change and diluted attention?
   Recommended: per question.
2. **Pilot:** run a 40-question stratified pilot first (about $2.90, under the $3.00 gate), and decide on the full
   pass ($43.57, which needs `--approve-cost`) from its measured findings and noise? Recommended: yes.
3. **Overlap:** include the 69 questions already judged by a screen or gate review (about $4.60), and also give the
   screen review the help text? Recommended: include them and add the help.
4. **Release gating:** should the new check gate the very next release, which means the full pass and its
   adjudication (perhaps 1,000 or more findings) must finish first? Or should it only list due questions until the
   first full pass is done, and gate releases after that? Recommended: list only until the first full pass.
5. **T-253 split:** fold T-253's type and range check into this review as a TYPE verdict (no extra calls), and
   treat the input `range` field (bounds such as months 0 to 12 that let the page show selectors) as a separate
   form-language change for your approval? Recommended: yes to both.
6. **Large questions:** for the 6 questions read by more than 20 lines (filing status, roster role, sales box and
   route, f1095a uniform, Schedule A excluded income), list the readers by label only and give only the question's
   own cited pages, rather than every reader's pages (`f1040.status` alone would be a 450,000-character prompt)?
   Recommended: yes.
