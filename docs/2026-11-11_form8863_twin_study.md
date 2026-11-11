# Form 8863 Part III written twice: measurement and options

Study date 2026-11-11, main checkout at `355d7302` (working tree: only `research/costs/agent_runs.jsonl` modified,
not by this study). Read-only: nothing in the repository was edited, no paid review, no check-all, no sub-agents.
Scripts and raw output are in `/tmp/dedup8863/` (`ids.py`, `pairs.py`, `pairs.out`, `refs.py`, `dup.py`, `dup2.py`,
`census.py`, `history.py`).

Every statement below is marked **[M]** (measured: I ran or read it today) or **[I]** (inferred: not checked against
an artifact). The inventory's numbers are not used.

---

## 1. The duplication as it is now

### 1.1 Ids and lines [M]

| | `person.edu*` | `dependent.edu*` |
|---|---|---|
| ids | 51 | 40 |
| lines of YAML | 1,066 (`person.yaml:3635-4700`, contiguous) | 853 (`dependent.yaml:2297-3149`, contiguous) |
| file total | 5,293 lines, 310 ids | 3,202 lines, 154 ids |
| by expression | 18 input, 25 choose, 6 test, 1 sum, 1 param | 14 input, 18 choose, 6 test, 1 sum, 1 param |
| by marker | 9 printed (23 to 31), 36 helper, 6 gate | 9 printed, 25 helper, 6 gate |

(The inventory's 48 / 997 and 38 / 821 are stale; both blocks grew, and the person block is now contiguous.)

**38 ids pair up by local name**, in the same relative order on both sides: 813 lines on the person side, 815 on the
dependent side. By kind, per side: 13 inputs (197 lines), 20 computed helpers and gates (407 lines), 5 printed lines
27 to 31 that call the `aqee` definition (209 lines, mostly the repeated refusal text).

**One-sided ids:**

- Person only, 13 ids, 253 lines: `edu_student_itin`, and the twelve lines of the Form 8863 line 7 test
  (`edu_born_2007`, `edu_born_2002`, `edu_fulltime`, `edu_half_support`, `edu_parent`, `edu_kid_age`, `edu_kid_18`,
  `edu_kid_18_support`, `edu_kid_student_age`, `edu_kid_support`, `edu_kid_fulltime`, `edu_kid`). The line 7 test is
  about the filer (i8863 p. 7, read by `f8863.yaml:360`), not about a student. It is not Part III and has no twin by
  design. `edu_student_itin` exists because the person's TIN is asked as two inputs (`person.tin`, issued;
  `person.itin_applied`).
- Dependent only, 2 ids, 38 lines: `edu_student_claimed` (the student must be claimed, `dependent.claimed`) and
  `edu_tin_issued` (an input; the dependent's `dependent.tin` already merges "issued or applied for", so "issued" is
  asked separately for the lifetime learning credit refusal, BUG-0331).

**Similarity.** After replacing the document prefix with `X.`: paired lines 0.974 (`difflib.SequenceMatcher` over
lines, `autojunk=False`); whole blocks including one-sided ids 0.828. I checked that the prefix replacement hides no
prose difference (no sentence in either block ends in "person." or "dependent." outside the lines already flagged).

**Readers outside the blocks.** Only `f8863.yaml`: `sum_over` of `edu_line30` and `edu_line31` over each collection
(4 helper lines plus 2 sums), and `person.edu_kid`. No other form, federal or New York, names a `.edu*` id.

### 1.2 Pair by pair [M]

Compared as parsed YAML with the prefix normalized:

- **28 pairs identical** in every field including the citation.
- **5 pairs differ only in the citation** (`edu_line23`, `edu_line24`, `edu_line25`, `edu_line26`, `edu_line27`): drift,
  finding D1 below.
- **5 pairs differ in wording or expression:**

| Pair | Difference | Intended? |
|---|---|---|
| `edu` | "for this person" / "for this dependent" in label and question | Intended (wording follows the collection) |
| `edu_student` | Dependent label adds "and claimed as your dependent"; the true branch goes to `edu_student_claimed` instead of `edu_student_edu`; the citation differs (person: i8863 p. 3 item 5, the TIN rule; dependent: i8863 p. 2 "Who can claim a dependent's expenses") | Intended (i8863 p. 2: only the person who claims the student can claim the credit). The two citations support different conditions of the same chain, not the test on the line (`f8863.paid`); harmless |
| `edu_student_edu` | Label only ("With education expenses paid: this person was a student..." / "Your dependent: a student...") | Intended |
| `edu_student_tin` | Person false branch goes to `edu_student_itin` (ITIN applied for); dependent goes to `edu_no`. Labels differ | Intended in logic: `dependent.tin` already includes "applied for". Label: see D3 |
| `edu_llc_tin_refused` | Person tests `person.tin` false; dependent tests the input `edu_tin_issued` false. Label "ITIN" / "ITIN or ATIN" | Intended (BUG-0331; an ATIN exists only for a dependent) |

Two more raw-text differences (`edu_1098t`, and the question of `edu`) are line wrapping only; the parsed values are
equal.

**Hidden difference behind identical text.** Identical text can still mean different things when it names a line
that differs between the hosts. The blocks name these outside lines: `X.zero` (7 times each; both are the amount 0,
from different parameters, `ss.zero` and `sales.zero`), `household.all_tin`, `f8863.paid`, `edu.no`, and the host
TIN lines covered in the table. I found no pair whose identical text reads a host line with a different meaning.

### 1.3 Drift findings

**D1. Lines 23 to 27 cite the instruction section on the dependent side only.** [M]

- `dependent.yaml:2632, 2667, 2697, 2728, 2969`: locators end `; i8863 p. 8, Line 23` (24, 25, 26) and
  `; i8863 p. 9, Line 27`.
- `person.yaml:3967, 4002, 4032, 4063, 4290`: the same locators without that suffix, for example
  `p. 2, Part III, line 23, "Has the American opportunity credit been claimed for this student for any 4 prior tax years?"`.
- Source: `sources/2025/i8863.txt` has the sections "Line 23" to "Line 26" on p. 8 and "Line 27" on p. 9. The
  question texts on both sides use them (line 25's "as determined by the institution" is from that section).
- Origin: commit `84fa3309` (2026-10-31) added the suffix to six dependent lines. Line 31 was brought into step on
  2026-11-03 (`0d9718cc`); 23 to 27 have been out of step for 11 days.
- The project already knows the person side as an accepted gap: `reviews/2025/instruction_cites.json` baseline holds
  `section:person.edu_line23` to `section:person.edu_line27`, and no dependent entry. The check
  (`tools/check_instruction_cites.py`) exists "so that the paragraph governing the line is among the pages its reviews
  are given".
- Effect [I]: reviews of the person's lines 23 to 27 are not handed i8863 pp. 8-9 through these citations. No value
  differs. Severity low; it is the textbook case of "one copy fixed, the other baselined".

**D2. The same operand finding is ruled on one side and baselined on the other.** [M]
`reviews/2025/operands.json`: `operands:dependent.edu_line28` is a ruling with a reason ("Bound per student to the
aqee definition's line 28..."); `operands:person.edu_line28` is a baseline entry. Same line, same finding, two
dispositions. Evidence-layer drift, no effect on values.

**D3. `edu_student_tin` label on the dependent side says less than the test does.** [M]
Person: "A student with qualified expenses: an SSN or ITIN (or an ITIN applied for by the due date), and a Form
1098-T (or an exception)". Dependent: "A student with qualified expenses: a TIN by the due date and a Form 1098-T (or
an exception)", while `dependent.tin` is true also when an ITIN or ATIN was only applied for. The person label was
made precise and the dependent one was not. Wording only (helper label), low.

**D4. A refusal names "ATIN" for a filer.** [M] `person.edu_line31` refuses with `form: Lifetime learning credit for
a student whose ITIN or ATIN was only applied for`, identical to the dependent's text, although the gate's own label
on the person side says "ITIN" only. Shared text that is slightly too wide on one side; cosmetic. Listed because a
merge has to decide which wording the shared text carries.

**Asymmetries that are not drift** [M]: `engine/src/mutate.ts` pins `operand.dependent.dependent.edu_over_refused.edu_no.then1`
with no person twin (the other two edu pins are twinned); the render index shows 4 of 9 dependent lines 23 to 31 as
MISMATCH (ruled) against 9 MATCH for the person. Both follow from different fixture and review histories, not from
the form data.

**History** [M] (`history.py`, 45 first-parent commits touching either file): the number of differing pairs went
2 (10-29) → 8 (10-31, D1 opens) → 8 → 9 → 8 (11-07: `edu_inst` reworded in `dependent.yaml` at 02:35 and in
`person.yaml` at 03:42, two commits of a form-by-form wording pass) → 10 (11-08, the two intended TIN lines). So in
two weeks: one drift that stuck (D1), one that closed in three days (line 31), and one planned one-hour window.

### 1.4 Interview questions and help [M]

`interview/2025/questions.yaml` has 13 paired entries. Each has only `order` and `help`; the prompt is the form
line's question. All 26 carry the same help sentence ("Married filing separately and unsupported items are refused
with citations.") and equal orders (21; `edu_over` 31). **No drift.** In the built data
(`canonical/2025/interview-full.json`, built 02:24 today, after the forms' last change) the paired prompts differ only
by the person frame ("For this person (you, or your spouse on a joint return) — "; the bank has no `dependent`
frame), the intended wording of `edu`, and the D1 citations. `fixtures/2025/defaults.json` gives the 13 paired inputs
equal defaults.

Not drift, but visible: that help sentence says nothing about the question it is attached to, on all 26.

---

## 2. Other duplication of the same shape

**Method A, exact repeated blocks** [M] (`dup.py`): each of the 68 form files (62 federal, 6 New York; 59,161
non-blank lines), own document prefix replaced by `X.`, indentation kept; maximal runs of at least 10 equal
consecutive lines between two files or two places in one file.

- Largest pair by far: `dependent.yaml` and `person.yaml`, 755 lines covered; single runs of 211, 180 and 179 lines.
- The next longest single run anywhere is 38 lines (`sb.yaml`, a repeated citation block). Across files the next
  pairs are `asset`/`scveh` (113 lines in runs of at most 27) and `clcw`/`clcw26` (89).

**Method B, same-named lines across documents** [M]: for every pair of documents, lines with the same local name and
an identical body after prefix normalization, ignoring bare parameter wrappers. `dependent`/`person`: 27 (of 44
shared names). Next: `clcw`/`clcw26`: 4. Nothing else reaches 3.

**Method C, shape repetition** [M] (`dup2.py`): every dotted id → `ID`, digits → `N`, month names → `MON`; runs of
at least 12 lines. 22,690 of 59,161 lines (38%) sit in a run repeated elsewhere in the same file: `s1a` 74%,
`f8962` 64%, `sd` 73%, `f1095a` 83%, `ny_rs` 92%. This is not copied logic but two other things: the 14-line form of
every two-way `choose`, and unrolled months (`f8962`: 12 months × 8 ids = 96 of 161 ids, 1,503 lines; `f1095a`: 60 of
77 ids, 843 lines; inventory row 5.2a).

**Conclusion.** The Part III block is the only case of logic copied between documents at any size. A mechanism built
for "the same lines under two parents" would have one customer today. The larger mass of repetition is within one
file (months, verbose `choose`), a different problem with a different remedy.

---

## 3. What the data model offers

Read: `spec/spec.md` section 4, `engine/src/types.ts`, `build.ts`, `check.ts` (reference rules), `eval.ts`
(collections and instances), the forms.

1. **Collections** [M]. A document is a collection through `collection: {parent?, implicit?}`. One parent only
   (`types.ts` `collection?: { parent?: string; implicit?: string }`). A line of an entry may read a line of an
   enclosing entry by its full id (`person.tin`); any other reference into a collection must be a `sum_over`
   (`check.ts` `requireRef`). `sum_over` returns money or a count, never a Bool.
2. **Implicit collections** [M]: one entry per parent entry under a fixed key, never asked (`f8606`, `f5329` under
   `person`; `f4562` under `sc`). This is how "one Form X per person" is already modelled.
3. **Definitions** [M] (`kind: def`, 4 federal: `aqee`, `se`, `tcw`, `tax_on_amount`): a document with `parameters`,
   instanced from a line by `{def, bind, line}`. **This is the existing reuse mechanism, and Part III already uses
   it**: `aqee.yaml` (210 lines) holds lines 27 to 30 and the worksheet once, called 5 times from each host. What a
   definition cannot hold today: a real input (its `input` lines are the bound parameters), a refusal that surfaces
   on a host line, a `shown_when` target, or anything read lazily. `eval.ts:383` and `:623` evaluate every binding
   operand in the caller when the instance is called ("for the record"). The eligibility chain was rebuilt as nested
   `choose` lines precisely so that answers are read in order (BUG-0446, BUG-0460); a definition called with lines 23
   to 26 bound would read all four at once.
4. **YAML anchors** [M] are used inside a file in 6 forms (13 anchors; `refuses: *claimed_no_tin` in
   `dependent.yaml`, `*mfs` in `f2441.yaml`). They cannot cross files.
5. **Authored YAML equals canonical JSON apart from citations** [M]: for all 62 federal documents,
   `yaml.safe_load(forms/2025/X.yaml)` with `cite` removed equals `canonical/2025/X.json` with `cite` removed. The
   build adds nothing but the filled citation. About 15 Python tools (some 35 call sites: `transcribe.py`,
   `subjects.py`, `carry.py`, `year_carry.py`, `check_logs.py`, `citations.py`, `year_diff.py`, `siblings.py`,
   `screen_review.py`, `question_review.py`, `render_compare.py`, `coverage/estimate.py`, `human_review/*`) rely on
   this by reading `forms/<year>/<doc>.yaml` directly; `carry.py` and `year_carry.py` also read it from other
   commits and trees, where no canonical build exists.

**Is there already a way for a line to range over "every student, whether person or dependent"?** No [M]. A
collection has one parent; a child line reads its parent by the parent's own document id; nothing reads a Bool out of
a collection. The form data handles it by stating Part III in each host and adding the two sums in `f8863`.

**What a real "student" collection would need** [I, from the code read above]: a parent list in the schema
(`schema/data.schema.json`, `collection.parent`), and a way for the child to read "my parent's TIN line" without
naming the parent document (a parent interface). That touches the parent walk in `check.ts` (15 mentions of
parent/enclosing), `eval.ts` (22), `Eval.lean` (15) and `Main.lean` (6), and the instance-key handling in
`mutate.ts` (20), `output.ts`, `fixture-inputs.ts`, `generate.ts`, `classm.ts`, `interview-rules-worker.ts`,
`ui/app.ts`; the renderer and the review tools' reach (`subjects.reach`) follow.

---

## 4. What the ids key [M]

Counts of `person.edu*` / `dependent.edu*` (bracketed entry keys included, `educator` excluded), `census.py`:

| Layer | Keyed on | Numbers |
|---|---|---|
| Fixtures | Line ids with entry keys (`person[taxpayer].edu_line23`) | 184 of 2,106 cases in files with a `cases` list mention them: `f8863.json` 32 of 35, `classm.json` 61 of 254, `classm.deepseek.json` 42, `mutation.json` 25, `dependent.json` 4, `person.json` 4, New York 9. 150 cases set them as inputs (3,895 occurrences). Expected values: printed lines in 36 cases, inputs 16, helpers 14, gates 9. `defaults.json`: 31 entries |
| Review subjects | Both. `subjects.py` hashes content per document: the whole form (`of_form`, authored YAML, citations out) and, per compared line, the line with its in-document reach, **including the ids it names** | A log entry is keyed by form, family and line key (printed marker or id) |
| Review logs | Form + line key + subject hash | Transcription index: person 104 compared lines (5 are 27 to 31), dependent 22 (5). Render index: person 32 (9 are 23 to 31), dependent 11 (9). Rulings naming the ids: transcription 51 (person) + 64 (dependent), render 35 + 57, questions 18, completeness 5. Content-addressed store: 10 transcription and 4 class M records |
| Rename carry | **None.** `carry.py` carries a ruling only for "the same kind, form and model family, and the same printed line or id" with unchanged content. `year_carry.py` carries across years on a content key that includes the ids in the reach. Neither maps an old id to a new one | A renamed line is a new line to both |
| Mutation pins | Keys and argument lists hold ids (`engine/src/mutate.ts`) | 3 of 70 pins |
| Baselines and rulings by id | `reviews/2025/instruction_cites.json` 5, `operands.json` 2, `consumers.json` 7 | |
| Ambiguities | The register's own ids; lines link to them | 6 `amb.2025.edu_*`; 2 linked from each paired side, 4 more from person-only lines. 6 id mentions in the register text |
| Coverage tree | `tools/coverage/tree.json` | 4 ids (the two refusal gates on each side) |
| Bug inventory | Prose | 19 of 595 entries name the ids (170 occurrences); history, not rewritten |
| Interview | Input ids | 27 questions in the bank (13 + 13 + `dependent.edu_tin_issued`), plus 5 person-only |
| Generator | `engine/src/generate.ts:769-802` builds ids as `${E}.edu${k}` for either kind of entity: it already relies on the shared local names | |
| `tools/siblings.py` | `EDU_TWIN` regex: a bug entry's "Siblings checked" must list the twin | The only existing guard; it checks the bug entry, not the form text |
| Rendered, reports, canonical | Derived | `rendered/` 4 files, `reports/` 18 files, regenerated |
| Lean, UI | | No mention |

Recorded review prices for these forms [M] (`.transcription/costs.jsonl`, Claude rows): a whole-form call costs
$0.4 to $3.9 (person transcription median $1.37, render $1.64; dependent $1.57 and $0.42). Review money is small
under every option; the cost that matters is engineering, adjudication and risk.

---

## 5. The options

### Option A. Keep both copies; a check keeps them in step

A standing check pairs `person.edu*` with `dependent.edu*` by local name, normalizes the prefix and compares the
parsed lines, citations included. Every difference and every one-sided id must be declared, with a reason and a
source, in a data file, each tied to a hash of the two lines so that a change to either side reopens it (the
`baseline_check.py` convention the project already uses). An optional `--write` copies the person line over the
dependent line for every undeclared pair, so a fix is made once and synced.

Form data: unchanged, apart from fixing D1.

```yaml
# reviews/2025/twins.json (new), sketch
{"pattern": "^(person|dependent)\\.(edu(_\\w+)?)$",
 "one_sided": {"person.edu_kid": "Form 8863 line 7 test of the filer (i8863 p. 7), not Part III", "...": "..."},
 "differences": {
   "edu_student_tin": {"reason": "dependent.tin already includes 'applied for'; the person asks it as itin_applied",
                       "subject": "<hash of both lines>"},
   "edu_llc_tin_refused": {"reason": "BUG-0331: 'issued' is person.tin for a filer, the input edu_tin_issued for a dependent",
                           "subject": "..."}}}
```

- Machinery: one Python tool or a mode of `siblings.py` (which owns `EDU_TWIN`), about 150 to 250 lines with a
  self-test; one check-all step. Evaluators, schema, renderer, review tools untouched.
- Ids changed: 0. Fixtures 0, logs 0, pins 0. Reviews: none stale (D1 changes citations only, which subjects leave
  out) [I for the last clause: from `subjects.py`'s docstring and `_without_cites`, not from a run].
- Charter tests. One change: still two edits, but the second is forced, and with `--write` it is one edit and one
  command. Rollover: two diffs and two line-scoped reviews, as today; a year change applied to one side fails the
  check.
- Risk while landing: none to values. One process effect: a change to a twin needs claims on both forms
  (`tools/claims.py`), which rules out the form-by-form split that produced the one-hour window on 11-07.
- Size: half a session. [I]
- What it does not do: `person.yaml` stays 5,293 lines; the text is still there twice.

### Option B. One authored template, expanded at build; canonical data unchanged

The 33 lines that are (after D1) equal, plus `edu` with one wording slot, move to a template file outside the
`forms/<year>/*.yaml` glob. The hosts keep their 4 differing lines and their one-sided lines and include the template
at the points where the lines sit today (three points, because host lines are interleaved). The build expands it, so
`canonical/2025/person.json` and `dependent.json` come out byte-identical to today's.

```yaml
# forms/2025/shared/f8863p3.yaml (new)
template:
  id: f8863p3
  hosts: {person: {who: this person}, dependent: {who: this dependent}}
  parts:
    lines23to26:
    - id: $.edu_line23
      printed: '23'
      label: Has the American opportunity credit been claimed for this student for any 4 prior tax years?
      shown_when: $.edu_student
      type: Bool
      expr: {op: input, source: "Has the American opportunity credit been claimed (by you or anyone else) ..."}
      cite: {doc: f8863, locator: 'p. 2, Part III, line 23, "..."; i8863 p. 8, Line 23'}

# forms/2025/dependent.yaml, after: the 853-line block becomes about 130 lines
    - include: f8863p3.gate            # edu, edu_1098t
    - id: dependent.edu_student        # host-specific, as today
    - id: dependent.edu_student_claimed
    - id: dependent.edu_student_edu
    - id: dependent.edu_student_tin
    - include: f8863p3.lines23to26     # edu_inst ... edu_llc
    - id: dependent.edu_tin_issued
    - id: dependent.edu_llc_tin_refused
    - include: f8863p3.lines27to31
```

- Machinery: schema (a template kind and `include`), `build.ts` (expansion), and **every reader of authored YAML**
  (section 3 item 5: about 15 Python tools, 35 sites), because authored YAML would no longer equal canonical data.
  That means a second expander in Python, used also on other commits by `carry.py` and `year_carry.py`. The hard
  spots: `citations.py` rewrites citation scalars in the authored file by offset (`_scalar_offsets`, `_rewrite`) and
  must learn that a host line's citation lives in the template; `year_diff.py`; `claims.py` (the template is a third
  unit to claim); the whole-form subject (`subjects.of_form` reads the authored file). The evaluators, Lean, the
  renderer and the UI read canonical data and need nothing.
- Ids changed: 0. Fixtures 0, pins 0. Logs: none stale if every subject is computed from the expanded document [I].
- Charter tests. One change: yes, one place, for 34 of 38 pairs. Rollover: one diff for those lines; reviews still
  run per host (the two expanded documents are two subjects), so review count is as today.
- Risk: two expanders (TypeScript and Python) that must agree. It can be guarded by making the invariant measured in
  section 3 item 5 a standing check (expanded YAML equals canonical apart from citations). A window in which a
  review tool still reads the unexpanded file would compute wrong subjects; landing needs all readers switched in one
  commit.
- Size: 2 to 3 sessions [I]. The template is about 725 lines (the 34 shared lines); each host loses that many and
  the template adds them once, so about 725 lines fewer in total (`dependent.yaml` 3,202 → about 2,480;
  `person.yaml` 5,293 → about 4,570).  [M for the line counts, I for the template's exact size]
- It introduces a macro layer the spec does not have ("There are no user-defined functions, loops, local
  variables..."), for one customer. If it were designed with an instance list it could also serve the unrolled
  months (2,346 lines in `f8962` and `f1095a`), which is where a template pays.

### Option C. Move the computed lines into a definition (the existing mechanism)

Extend what `aqee` does: a definition `f8863p3` whose parameters are the student's answers and host facts and whose
lines are the eligibility chain, the adjustments and lines 27 to 31. Each host keeps its inputs and thin calling
lines.

```yaml
# before (each host, 23 lines)
    - id: person.edu_aoc24
      expr:
        op: choose
        alternatives:
        - guard: {op: test, eq: [person.edu_line24, {const: true}]}
          then: person.edu_aoc25
        - guard: {op: test, eq: [person.edu_line24, {const: false}]}
          then: person.edu_no
# after: the line exists once in the def; the host has
    - id: person.edu_aoc
      expr: {op: copy, from: {def: f8863p3, bind: &edu {paid: f8863.paid, claimed: person.yes, has: person.edu,
             tin: person.tin_or_itin_applied, f1098t: person.edu_1098t, l23: person.edu_line23, ...}, line: aoc}}
```

- Machinery: bindings must become lazy in `eval.ts` and `Eval.lean` (today every bound operand is evaluated at the
  call), or the ordered-reading property behind BUG-0446 and BUG-0460 is lost and questions are asked that the chain
  would not reach. Laziness changes the recorded operands of every existing instance (`aqee`, `se`, `tcw`,
  `tax_on_amount`) [I]. Refusal gates and `shown_when` targets must stay host lines.
- Ids changed: the 20 computed helpers either remain as thin copies (little saved) or disappear into the definition.
  If they disappear: expected values in 14 fixture cases (helpers) and 9 (gates), `covers` and notes in about 42
  cases, the 3 pins, 4 coverage-tree ids, 2 baseline entries.
- Reviews: the new definition is a form in its building phase (whole-form transcription, render, class M,
  completeness: a few dollars), plus the changed host lines; nothing carries (no rename carry).
- Charter tests. One change: yes for computed logic. **No for the 13 questions**, which stay in both hosts (197
  lines each) and are the part the wording pass (phase 3) will edit. D1, D3 and the 11-07 window were all in inputs
  or wording; C would have prevented none of them.
- Risk: an evaluator semantics change in both evaluators at once, in the area (reachability) with the most recent
  bugs. Size: 2 to 4 sessions [I].

### Option D. One per-student document under both collections (the true merge)

A document `f8863s`, an implicit collection whose parent is `person` or `dependent`, holds Part III once. Hosts
expose a small interface (`student_claimed`, `student_tin`, `student_tin_issued`); `f8863` sums one collection.

```yaml
# forms/2025/f8863s.yaml (new)
form:
  id: f8863s
  collection: {parent: [person, dependent], implicit: student, cite: {doc: f8863, locator: 'p. 2, Part III, "Complete Part III for each student"'}}
  lines:
  - id: f8863s.line23
    printed: '23'
    ...
  - id: f8863s.student_tin
    expr: {op: choose, alternatives: [{guard: {op: test, eq: [parent.student_tin, {const: true}]}, then: f8863s.f1098t}, ...]}
# f8863.yaml: aoc_person, aoc_dep and aoc_sum become one sum_over of f8863s.line30
```

- Machinery: schema, `check.ts`, `eval.ts`, `Eval.lean`, `Main.lean`, `mutate.ts`, `output.ts`,
  `fixture-inputs.ts`, `generate.ts`, `classm.ts`, the interview (frames, entry syntax), the renderer, `ui/app.ts`,
  the review tools' reach, the spec (a new concept: a collection with two parents and a parent interface).
- Ids changed: all 78 paired ids (38 × 2) become 38 plus about 6 interface lines; every entry key changes shape
  (`person[taxpayer].edu_line23` → `person[taxpayer].f8863s[student].line23`). Fixtures: 184 cases rewritten (150
  with inputs), 31 defaults, 27 interview questions, 3 pins, 4 coverage ids, 14 baseline and ruling keys. Logs for
  the moved lines are void and are not carried; the new document needs building-phase reviews; `f8863` and both
  hosts need line-scoped reviews.
- Charter tests. Both fully met: one place, one diff, one review.
- Risk: the largest. Both evaluators change in their collection core in one landing; fixtures are rewritten by
  script in the same change, so the usual protection (fixtures unchanged across a refactor) is absent exactly here.
  A differential run of old tree against new on every fixture and on generated returns would be the safeguard.
- Size: 5 or more sessions [I]. One customer today (section 2).

### Comparison

| | A check | B template | C definition | D per-student collection |
|---|---|---|---|---|
| Authored lines removed (net) | 0 | about 725 | about 300 [I] | about 800 [I] |
| Wording stated once | no (synced) | yes | **no** | yes |
| Logic stated once | no (synced) | yes | yes | yes |
| Evaluators change | no | no | yes, both | yes, both |
| Tools that must change | 1 new | about 15 | few | about 15 plus engine |
| Ids changed | 0 | 0 | 0 to 40 | 78 and all entry keys |
| Fixture cases touched | 0 | 0 | 0 to about 60 | 184 |
| Review logs voided | 0 | 0 [I] | changed lines + new def | all Part III lines |
| Drift possible afterwards | caught at commit | no (4 host lines aside) | in the 13 questions | no |
| Size [I] | 0.5 session | 2 to 3 | 2 to 4 | 5+ |

---

## 6. Recommendation

**Option A, landed now, with D1 to D3 fixed first; decide B later and only together with the unrolled months.**

Reasons:

1. The harm the owner names is a fix applied to one copy and missed in the other. A removes that harm completely
   and mechanically at about a tenth of the cost of any merge, with no id, fixture, log or evaluator touched.
2. The measured drift is small and benign: in two weeks of heavy editing, one citation drift that stuck and two
   label slips; no value ever differed. The duplication is a real cost, but it has not yet produced a wrong return.
3. The block is the only cross-document copy in the form data (section 2). B, C and D each add a mechanism to the
   model or the build for one customer. C does not even cover the questions, where all the observed drift was.
4. A is not wasted if a merge follows: its declared-differences file is exactly the parameter list of B's template
   or D's parent interface, and its check is the acceptance test for the migration.
5. What A leaves unpaid is intelligibility: `person.yaml` stays over 5,000 lines. That is row 5.1a, and moving 725
   lines out of it does not solve it either (about 4,570 would remain).

**Separately green steps:**

1. Fix D1: add the five instruction-section suffixes to `person.edu_line23` to `edu_line27` and drop the five
   baseline entries in `reviews/2025/instruction_cites.json`. Fix D2 (one disposition for `edu_line28`) and D3 (the
   dependent label). D3 changes a label, so the dependent render review of that helper may be due [I].
2. Add the twin check with the declared differences (5 pairs, 15 one-sided ids) and the check-all step.
3. Add `--write` (sync from the person side) and say in `tools/README.md` that a twin change claims both forms.
4. Decision point, not a step: B, designed with an instance list so that it also serves `f8962` and `f1095a`.

**What would change my mind:**

- Toward B: the owner wants the unrolled months (row 5.2a, 2,346 lines) addressed anyway; or the wording pass turns
  out to edit these 13 questions often enough that sync commits become noise; or TY2026 brings a second block that
  must exist under both `person` and `dependent`.
- Toward D: a second and third customer for a per-student or per-individual document (for example New York
  per-student lines, or another credit figured per person-or-dependent), or a decision that review and rollover
  cost per duplicated line matters more than I measured ($0.4 to $3.9 per whole-form review).
- Toward doing nothing more than step 1: if the owner judges that `siblings.py`'s existing rule (a bug entry must
  list the twin) is enough. I do not: it checks the bug entry's text, not the forms, and it did not catch D1.
- Against A: if the owner reads "paid down" as "the text exists once" and accepts a macro layer in the build; then
  B is the smallest design that achieves it without changing an id.

**Limits of this study.** Staleness claims for options A and B come from reading `subjects.py`, `check_logs.py` and
`carry.py`, not from running `check_logs` on a changed tree. Sizes are estimates. Options B, C and D were not
prototyped; A's comparison was (`pairs.py` is the check in miniature and produced section 1.2). The canonical build
I compared against is today's 02:24 build, newer than both form files (00:21); I did not rebuild.

---

## 7. One-page summary

**State.** Form 8863 Part III is written in `person.yaml` (51 ids, 1,066 lines) and `dependent.yaml` (40 ids, 853
lines). 38 ids pair up (about 814 lines a side, 0.974 similar). Of the 38: 28 are identical, 5 differ only in a
citation (drift), 5 differ on purpose (wording of "this person / this dependent", the claimed-dependent step, and
the two TIN lines, which follow from how each host asks for the TIN; BUG-0331). 13 person-only ids are mostly the
line 7 test of the filer and are not Part III. Lines 27 to 30 are already shared through the `aqee` definition.

**Drift found.** D1: `person.edu_line23` to `edu_line27` lack the i8863 pp. 8-9 instruction-section citations their
dependent twins got on 10-31; the gap sits in a baseline. D2: one operand finding ruled on one side, baselined on the
other. D3: a dependent helper label less precise than its twin. D4: "ITIN or ATIN" in a filer's refusal text. No
value differs between the copies, and the interview questions, help and fixture defaults are in step.

**Elsewhere.** This is the only logic copied across documents (next largest exact run: 38 lines). The big
repetition is inside single files: unrolled months (2,346 lines) and verbose two-way choices.

**The model.** No line can range over "every student". A collection has one parent; a definition can share
arithmetic (and does) but not questions, refusals or answers read in order.

**Options.**

- A. Check that the copies stay in step, differences declared with reasons; optional sync. Half a session. No id,
  fixture, log or evaluator touched. Two copies remain on disk.
- B. One template expanded at build; canonical data byte-identical. 2 to 3 sessions; about 15 tools must read the
  expanded form; about 725 lines removed; no id changes.
- C. Push the computed lines into a definition. Both evaluators change (lazy bindings); the 13 questions stay
  duplicated, and all observed drift was in questions and citations.
- D. One per-student document under both collections. Meets both charter tests fully; changes both evaluators'
  collection core, 78 ids, 184 fixture cases, and voids the Part III review logs. 5+ sessions, one customer.

**Recommendation.** A now: fix D1 to D3, add the check, add the sync. Revisit B only together with the unrolled
months, where a template has enough customers to earn its place. D is not justified by one block.

**Decide.** (1) Is "cannot drift" enough, or must the text exist once? (2) If once: is a build-time template
acceptable in a model whose spec has no macros? (3) Should the months (row 5.2a) be planned with it?
