# Year-free ids: inventory, rename cost and options (2025-us)

Study date 2026-11-11. Model `claude-fable-5-2`, class judgment, year 2025, jurisdiction us.
Measured on the main checkout at `355d7302` (main moved to `131747ca` during the study; counts taken by
`git grep` on the main checkout after that are marked "at 131747ca"). Nothing in the repository was edited.
Experiments ran in scratch clones under `/tmp/yearfree/` (`repo`: renames applied; `repo0`: subject sweeps;
`repo1`: pristine baseline, built). No paid call was made; every review tool was run with `--dry-run` or as an
offline check.

Marking used throughout: **[M]** measured by running or by reading the artifact named; **[I]** inferred, not
checked directly.

One departure from the project's rules, disclosed: to give the first scratch clone the review data the dry runs
need, `.transcription/` and `.classm/` were copied into `/tmp/yearfree/repo` with `cp -Rc` (the project rule is
`tools/worktree_data.py clone`; the Bash guard refused the second such copy and it was not repeated). The copy
is outside the repository and nothing is carried back from it.

---

## 0. Summary of findings (details below; one-page decision summary at the end)

1. **The debt is smaller in ids and larger in text than the charter's figures say.** Now: 35 line ids carry a
   year (16 inputs, 19 computed), plus one document id by two digits (`clcw26`, 26 lines), 21 enum values
   (`y2005`..`y2025`), 100 ambiguity ids (93 federal, 7 New York) and 28 fixture case ids. No parameter, table,
   def, enum, conflict or gate-unit id carries one. Year literals in *wording* are the bulk: 2,099 lines of the
   model name a year outside citations by the project's own rule, 1,378 of them in labels, questions, help and
   notes. [M]
2. **The project already has the conventions; 35 ids are the exceptions to them.** 3,681 of 3,716 line ids are
   year-free. The tax year is unmarked (`f2441.spouse_died`), last year is `prior_` (37 line ids, 4 parameters:
   `clcw.prior_sd7`, `f4952.prior_7`), a birth cutoff is named by its purpose (`person.sav_born`,
   `refund.you_born`). Only "next year" has no precedent. [M]
3. **A rename is not free and nothing carries it today.** Every review subject hashes ids. Renaming the three
   T-261 ids in a scratch copy made `check_logs` fail for 3 transcription logs (19 compared lines, all 19 of
   them ruled disagreements), 2 render logs (6 lines, one of them a log key that is the renamed id itself) and
   2 class M logs (whole), made `check_questions` and `check_consumers` fail outright, and left 1 screen,
   2 completeness reviews and 3 questions due. No tool carries a ruling, a log or a sampled review across a
   rename: `carry.py` requires the same line id and an unchanged closure, `year_carry.py` does not normalize a
   year inside an id. [M]
4. **A rename also changes the seeded generated returns.** With only `eic.died_2025` renamed, `interview-rules`
   went from 0 problems to 27 at the same commit: the 12 generated returns are different returns (1,645 walked
   states became 1,571), and the new sample exposes reach problems in `f1095a`. [M] So a "pure" rename is not
   neutral for seeded evidence, and it cannot land without a judgment call on what the new sample finds.
5. **The append-only records cannot be rewritten** (`check_bug_inventory.py`: byte-prefix check;
   `review_store.py`: records named by their hash, "never rewritten"). History keeps the old names; what is
   needed is a rename ledger the reader and the tools can consult. [M]
6. **`amb.2025.*` needs no rename, only a rule.** The TY2026 preparation already names a new entry
   `amb.2026.gift_floor_base` while citing carried entries as `amb.2025.*`; the year is the edition that first
   recorded the entry, a fact that does not roll. [M]
7. **The T-261 pilot is not safe to run mechanically tonight** (section 7).

---

## 1. The inventory, now

Source: the canonical build of `355d7302` (`canonical/2025/*.json`: 60 forms, 8 defs, both parameter files,
both registers, the conflict checks), the tables directories, the fixtures, and the committed review indexes.
Script: `/tmp/yearfree/inventory.py`. A "year" is a four-digit 19xx/20xx literal not adjacent to another
digit; two-digit suffixes were listed and read by hand. [M]

### 1.1 Counts by kind

| Kind | Total | With a year | Data id or path | Defined in | Notes |
|---|---|---|---|---|---|
| Input line ids | 630 | **16** | data id | `forms/2025/*.yaml` | the charter's "about 30 input ids" counted ids in forms, interview and params by `grep`, computed lines included |
| Computed line ids | 3,086 | **19** | data id | `forms/2025/*.yaml` | 8 in `asset`, 9 in `scveh`, `f8880.dist_2025`, `household.widowed_2025` |
| Document (form) ids | 60 forms + 8 defs | **1** by two digits: `clcw26` | data id **and** path | `forms/2025/clcw26.yaml` | 26 line ids `clcw26.*`; also `fixtures/2025/clcw26.json`, `rendered/2025/clcw26.md`, three review indexes |
| Parameter ids | 503 (286 federal, 217 New York) | 0 | | `params/2025.yaml`, `params/ny/2025.yaml` | |
| Enum ids | 28 | 0 | | `params/2025.yaml` | |
| Enum values | 301 | **21**: `y2005`..`y2025` of `placed_year` | data value | `params/2025.yaml:213` | key of `tables/2025/auto_limit*.yaml`, `recovery_year.yaml`; 345 occurrences in 15 fixture files |
| Table ids | 39 | 0 | | `tables/2025/`, `tables/ny/2025/` | |
| Def ids | 8 | 0 | | | |
| Conflict-check ids | 27 | 0 | | `interview/2025/conflict_checks.yaml` | |
| Ambiguity ids | 100 | **100** (`amb.2025.*` 93, `amb.ny.2025.*` 7) | data id | `ambiguities/2025.yaml`, `ambiguities/ny/2025.yaml` | 3 slugs carry a second year: `savers_2026_joint`, `refund_boxes_2024`, `clcw_to_2026` |
| Fixture case ids | 2,106 | **28** (29 by regex; `ny.household.single.2000` is an amount) | data id (a label) | `fixtures/2025/*.json` | 14 in `scveh.json` |
| Fixture default keys | | **16** (the 16 inputs above) | data id | `fixtures/2025/defaults.json` | the measurement doc counted 13 |
| Review index keys (Claude family) | 14,877 over 339 indexes (all families) | **10** | data id | `reviews/2025/<kind>/<form>.index.json` | render `household`: `spouse_died_2025`, `widowed_2025`; transcription `asset`: 3, `household`: 1; class M `asset`: 4 |
| Sampled-review unit keys | 505 questions, 16 false-no gates | **14 questions**, 2 screens (`eic.died_2025`, `refund.not_2024`) | data id | `reviews/2025/questions/<form>.json`, `screens/screen_review.json` | |
| Ruling and baseline keys | | 3 in `reviews/2025/consumers.json`, 8 in `questions/rulings.json`, 1 in `screens/rulings.json` | data id | | 0 in `citations`, `input_quotes`, `instruction_cites`, `limits`, `operands`, `signs`, `completeness`, `false_no` |
| Engine source | | 2 full ids in `generate.ts` lines 139-140, 614, 617, 891, and **fragments** built by concatenation (`"_a2025"`, `"_a2026"`, `"_born_2007"`, `"_born_2002"` at 142-143, 759, 783); `scveh.is2019` 7 times in `mutate.ts` with a structural test on `y2019` | code | `engine/src/generate.ts`, `mutate.ts` | Lean and the UI name no line id. The charter's "the engine is already clean" does not hold for the generator |
| Paths with a year | every per-year directory and file | n/a | **path**, not a data id | `forms/2025/`, `params/2025.yaml`, `reviews/2025/`, ... | handled by `engine/src/year.ts` and `tools/taxyear.py`; out of scope here. Stragglers are charter section 6 |

### 1.2 The 35 line ids, classed by what the year means

The right year-free name differs by class. Names in the last column are candidates, not decisions; each needs
the owner's or a judgment agent's eye (see 6.3).

**Class T: the year is the tax year ("this year"). 22 ids.** Convention already in the tree: the tax year is
unmarked; add a word only where two periods must be told apart.

| Id | Kind | Reads as | Candidate |
|---|---|---|---|
| `eic.died_2025` | input, Bool | spouse died in the year, or return of someone who died in the year | `eic.died` |
| `household.spouse_died_2025` | input, Bool | spouse died in the year | `household.spouse_died` (cf. `f2441.spouse_died`, `household.no_spouse_died`) |
| `household.widowed_2025` | computed | single or head of household though the spouse died in the year | `household.widowed` |
| `f8962.married_in_2025` | input, Bool | married during the year with coverage before the first full month | `f8962.married_in_year` |
| `dependent.edu_a2025`, `person.edu_a2025` | input | tax-free assistance received in the year | `*.edu_assist` |
| `f8880.dist_2025` | computed | distributions received in the year | `f8880.dist_year` |
| `asset.is2025`, `scveh.is2025` | computed | placed in service in the year (`placed == y2025`) | `*.first_year` |
| `asset.on_26_2025`, `asset.macrs2025`, `asset.dep_2025`, `asset.bonus_2025`, `asset.s179_2025` | computed | the same figure "for property placed in service this year"; the tree pairs them with `asset.macrs_prior`, `asset.dep_prior` | `*_new` or `*_first` |
| `asset.cost179_2025`, `asset.mq_q4_2025` | computed | labels say nothing of 2025 ("the business cost when used more than 50%") | drop the suffix |
| `scveh.lim_2025`, `scveh.s179_2025_ok`, `scveh.line10_2025`, `scveh.bonus_2025`, `scveh.line19_2025`, `scveh.s179_2025`, `scveh.s179_2025_o` | computed | "for a vehicle placed in service this year" | `*_first` |

**Class N: the year after ("next year"). 2 ids + 1 document.** No precedent in the tree.

| Id | Reads as | Candidate |
|---|---|---|
| `dependent.edu_a2026`, `person.edu_a2026` | assistance received next year, before filing, for this year's expenses | `*.edu_assist_after` |
| document `clcw26` (26 line ids, a file name in four trees) | carryover to next year | `clcw_next` |

**Class P: the year before ("prior year"). 4 ids.** Precedent: `prior_`.

| Id | Candidate |
|---|---|
| `refund.not_2024` | `refund.not_prior_year` |
| `refund.line5d_2024`, `refund.line5e_2024`, `refund.line17_2024` | `refund.prior_5d`, `refund.prior_5e`, `refund.prior_17` (cf. `clcw.prior_sd7`) |

**Class O: a year at a fixed offset from the tax year. 5 ids.** The literal rolls every year, but not as
"this year"; `year_carry.py` deliberately does not normalize these ("Birth-year cutoffs (1961 -> 1962) lie
outside the window: they change, so their lines are reviewed").

| Id | Offset | Candidate (named by purpose, cf. `person.sav_born`) |
|---|---|---|
| `person.born_before_2001` | TY-24: age 25 at year end | `person.eic_age_min` |
| `person.born_after_1960` | TY-65: under 65 at year end | `person.eic_age_max` |
| `person.edu_born_2007` | TY-18 | `person.edu_age_18` |
| `person.edu_born_2002` | TY-23: under 24 at year end | `person.edu_under_24` |
| `scveh.is2019` | TY-6: first year after the recovery period | `scveh.past_recovery` |

**Class M: a misnomer. 1 id, and it is one of the three in T-261.** `f2441.paid_2026` is not a "next year"
quantity. Its line is "Qualified care expenses incurred in 2025 not already counted in the per-person care
amounts", and the YAML above it says "The legacy input id is retained; line 16 is not limited to a payment
year" (`forms/2025/f2441.yaml:990`). It is also `NonNegDollars`, not `Bool` as the T-261 row says. Candidate:
`f2441.other_expenses`. The name is a judgment, not a substitution of the year.

**Class F: a fact that does not roll.**
- Enum values `y2005`..`y2025`: the calendar year a property was placed in service. A 2019 vehicle is a 2019
  vehicle in every later return. What rolls is the set (it gains `y2026`) and the two tests that read it
  (`asset.is2025`, `scveh.is2025`: class T; `scveh.is2019`: class O). `tools/fixtures_year.py` already moves
  `placed: y2025` with the year (`YEAR_KEYS`). **No rename.**
- Ambiguity ids `amb.2025.*`: see 1.3. **No rename.**
- Fixture case ids naming a statutory date (`stage14.asset.qip_2018`, `refuse_pre_2017`): labels of scenarios.
  The rest of the 28 (`stage14.veh.2025_bonus`, `stage9.eic.no_child.born_jan1_1961`) name the scenario's year
  and go stale as labels when `fixtures_year.py` re-records them; they are referenced from 76 review files,
  55 reports and 10 BUG entries. [M] Low value to rename; leave them and let the "no new year in an id" check
  cover line ids only.

### 1.3 Ambiguity ids

100 ids, all prefixed with the year. References (at `355d7302`, `git grep -o`): 4,795 in 389 tracked files:
forms 298 (45 files), rendered 404 (47), ambiguities 109, fixtures 23, tools 10, engine 2 (comments), lean 1
(a comment), reviews 2,115 (191 files), reports 1,571, research 169, handoffs 30, TASKS 24, BUG_INVENTORY 21,
docs 10, spec 5. [M] The charter's "93 ids with 258 references" counted the form links only (278 `ambiguity:`
links in 45 forms now).

What the year means here is a choice, and the tree has already made it in practice:
- `ambiguities/<year>.yaml` is "one file per tax year" (spec section 5); the path already carries the edition.
- The TY2026 preparation names its new entry `amb.2026.gift_floor_base` and cites the carried entries as
  `amb.2025.*` (`docs/ty2026/ADOPTION.md:92`, `research/ty2026/changes.md`). [M]
- The build constrains only the New York prefix (`build.ts:221`). [M]

So `amb.<year>.<slug>` reads as "first recorded for the <year> edition", which does not roll.
Dropping the year instead (`amb.<slug>`) would change the rendered English of every line that links an entry;
measured in the sweep (section 3.5).

### 1.4 Year literals in wording (not ids, but the larger part of charter 7 item 4)

With the project's own rule (`year_diff.year_literal`: a line outside `locator:`/`quote:` that names 2025 or an
id or constant bearing a year), over forms, tables, params, registers and interview of both jurisdictions:
**2,099 lines** (forms 1,488, New York forms 118, tables 149, params 9, registers 179, interview 156). Split:
year in text 1,378; an `amb` id only 381; an id or constant only 222; `tax_year:` headers 118. [M] The
federal-only figure comparable to the measurement doc's 1,731 is 1,913 (+10% in two days).

Wording gets the year as literal text. There is no placeholder: no `{year}` token anywhere in `engine/src`,
`tools`, `forms`, `interview` or `spec`, and `build.ts` substitutes `YEAR` only into paths and citations. [M]

---

## 2. What the project already has for the year

- **`engine/src/year.ts`** [M]: `YEAR` is `--year N` or the newest year in `years.json` (`{"adopted": [2025]}`).
  `yearPath(top)` is `<top>/<YEAR>`, `nyPath(top)` is `<top>/ny/<YEAR>`, `reportPath` likewise. `build.ts` checks
  that every file's `tax_year:` equals `YEAR`. Nothing in it touches ids or wording.
- **`params/2025.yaml`** [M]: values and enums keyed by year-free names; the year lives in the path and in
  `tax_year:`. This is the model for a year-relative fact: a year-free name whose value is the year's. A test
  such as `asset.is2025` (`placed == y2025`) could read a year parameter instead of a constant.
- **`tools/year_diff.py --adopt`** [M]: copies forms, tables, params, register and interview to the new year,
  rewrites only `tax_year:` and "(2025)" form citations, and lists every other line naming the year or an id
  that bears a year (`YEAR_ID = [A-Za-z_](19|20)\d\d(?!\d)`) on a worklist for a person. It renames no id.
- **`tools/fixtures_year.py`** [M]: carries fixtures; moves `placed`/`placed_date` values with the year;
  parameter-relative inputs follow their parameter. It renames no input key.
- **`tools/transcription/year_carry.py`** [M]: carries a review verdict to the next year when the line's key is
  equal in both years after "lockstep" normalization: a year token is replaced by `{Y}`, `{Y-1}` only where the
  cited source moved the same year by +1. Tokens are `\w+`, so `died_2025` is one token and is **not**
  normalized. Tested in scratch: a line whose id moves `eic.died_2025` -> `eic.died_2026` with its wording does
  not carry; the same line under a year-free id with the wording year moved does carry. [M] The index is also
  matched by log key ("the line is not compared under the same key in both years"). So **a year-bound id
  defeats the cross-year carry for its own line and for every compared line whose reach names it**, whether it
  is renamed each year or kept: renamed, the id token differs; kept, the wording moved and the name is false.
- **`tools/transcription/migrate_line_subjects.py`** [M]: a precedent for a no-model rewrite of the logs' subject
  tables when the definition of a subject changed, guarded by "a log is written only when its state after equals
  its state before".
- **Rules for ids** [M]: spec 4.3: "`id`: Stable identifier that survives renumbering between years". Charter
  section 2: "A gated input keeps its id". Charter section 7 item 4: "No year literals in ids or text". There is
  no written rule for naming a relative year; the convention exists only as practice (finding 2 above).
- **No check forbids a new year-bearing id.** [M] The measurement doc proposed one ("a build check that
  forbids new year literals in ids"); it is not built.

---

## 3. What a rename costs

### 3.1 Where the three T-261 ids are mentioned

Tracked files at `355d7302`, plus ignored review data; a file is counted once per id. [M] (`/tmp/yearfree/refs.py`)

| Layer | `eic.died_2025` files / lines | `f2441.paid_2026` | `household.spouse_died_2025` | Treatment on a rename |
|---|---|---|---|---|
| Form (definition and readers) | 1 / 2 | 1 / 2 | 1 / 4 | rename (mechanical) |
| Interview bank and profiles | 1 / 1 | 1 / 1 | 5 / 5 (`questions`, `sales`, `social-security`, `stage4`, `gate_frequencies`) | rename (mechanical) |
| Fixtures (inputs; `defaults.json`, per-form, `classm*.json`, `mutation.json`, New York) | 14 / 264 | 6 / 151 | 10 / 536 | rename (mechanical); `classm*.json` and `mutation.json` are tool-managed |
| Engine source (`generate.ts`) | 1 / 2 | 1 / 1 | 1 / 2 | rename (mechanical; fragments for other ids are not found by a whole-id search) |
| Lean, UI | 0 | 0 | 0 | none |
| Tools (`engines/generate_cases.py`, `coverage/tree.json`, `human_review/reading_list.json`, `year_diff.py` self-test) | 2 / 2 | 3 / 4 | 1 / 1 | rename, except the `year_diff.py` self-test, which uses the id as its example of a year-bearing id |
| Reviews: indexes, ruling sidecars, sampled logs, adjudication notes, `consumers.json` | 8 / 19 | 6 / 16 | 8 / 22 | keys must be rewritten or the checks fail; prose stays |
| Review store records (immutable) | 5 / 22 | 20 / 30 | 75 / 98 | **cannot** be rewritten |
| Rendered and reports (generated) | 14 / 19 | 11 / 12 | 23 / 35 | regenerated by the build and check-all |
| `BUG_INVENTORY.md` (append-only) | 1 / 2 | 1 / 5 | 1 / 3 | **cannot** be rewritten |
| TASKS, docs, handoffs, research | 9 / 13 | 9 / 17 | 9 / 10 | history; leave, except living docs |
| Tracked total | **56 / 346** | **59 / 239** | **134 / 716** | |
| Ignored `.transcription/`, `.classm/` | 534 / 1,629 | 625 / 3,432 | 526 / 1,695 | raw prompts and replies; history |

Mutation pins: none of the three ids, and none of the 35 except `scveh.is2019`, is named in `mutate.ts`. But a
pin's premise digest (`premiseDigest`) hashes each premise line's `id`, `expr`, refusal gates and the list of
its readers, so a pin whose premises read or are read by a renamed line moves without naming it. [M] for `eic.died_2025`: `mutations()` and
`equivalenceReason()` over the pristine build and over the renamed one give 6,497 mutants and 386 holding
pinned arguments in both, no mutant id changed. Not measured for the other 34; `scveh.is2019` is named in a
pin's own code (`mutate.ts:2372`), and a renamed *computed* line changes the `readers` list of what it reads,
so some pins would need their digest constant made again. [I]

### 3.2 Do reviews go stale on a pure rename? Yes, by construction

Read in the tools [M]:

| Review | Subject is | Keyed by | Id in the subject? |
|---|---|---|---|
| Transcription (whole) | `subjects.of_form`: the form YAML without citations | form | yes |
| Transcription (per line) | the line and its in-document reach (helpers and inputs followed), wording fields left out, an input's question kept; plus a "foreign interfaces" hash of other documents' lines it names (id, document, marker, type, question) | log key: the printed marker, or **the id** for an exported helper | yes: every member line's `id`, every reference |
| Render (per line) | the line's rendered section and the glossary sections it names | printed marker, or **the local id** for a form of helpers only (`household`) | yes: ids are printed in the rendered English |
| Class M | `subjects.of_computation`: each line's id, type, expression | form (whole only; no per-line path) | yes |
| Question | the question's line, its interview wording, each direct reader's line and English | **the input id** | yes |
| Screen | the review prompt without gate and help | **the screen's input id**, or `gate:<condition id>` | yes |
| False-no | `gates.subject`: condition, gate lines, gated inputs, English | `gate:<condition id>` | yes |
| Completeness | the form's lines, citations, cited pages | form | yes |
| Consumers baseline (`check_consumers.py`, no model) | | `consumer:<id>@<doc>:<page>` | yes, in the key |

So every subject is keyed by text that contains the id, and several are keyed by the id itself.

Can any tool carry across a rename? No. [M by reading; the first by dry run]
- `rerun_all.py --dry-run` plans a paid rerun for every stale log (3.3).
- `carry.py` carries a *ruling* to a repeat disagreement after a rerun, and only for "the same printed line or
  id", "the same disagreement content: both expression trees" and "the same project line: the line and
  everything it reads ... unchanged between the source log's commit and the working tree". A renamed operand
  changes both the trees and the closure. [I: not run, since it needs a new reply.]
- `year_carry.py` normalizes years in text, not ids (section 2). [M]
- `samples.carried` carries a sampled ruling only "on the same subject".
- `migrate_line_subjects.py` rewrites subject tables only to the hash of "the version of the document the log
  reviewed".

### 3.3 What the tools call stale after renaming the three (scratch, real build, no paid call)

Procedure: in `/tmp/yearfree/repo` at `355d7302`, each id was replaced as a whole token in `forms`,
`interview`, `fixtures`, `engine/src`, `tools` (not `tools/year_diff.py`); then `npm run compile`,
`main.js build`, `main.js render`; then the offline checks. Baseline at the same commit: `check_logs` OK for
62/62/55 Claude logs; 143 questions, 1 screen and 1 false-no gate already due; `interview-rules` 0 problems. [M]

| Check | `eic.died_2025` | `f2441.paid_2026` | `household.spouse_died_2025` |
|---|---|---|---|
| `check_logs` transcription | **fails**: `eic` stale for 16 of 20 compared lines | **fails**: `f2441` stale for 1 of 37 (line 16) | **fails**: `household` stale for 2 of 19 |
| ... ruled disagreements on those lines (rulings that would be made again) | 16 of 16 | 1 of 1 | 2 of 2 |
| `check_logs` render | current | **fails**: `f2441` 2 of 36 (lines 16, 17) | **fails**: `household` 4 of 64, and "lines no longer compared: `spouse_died_2025`" (the id is the log key) |
| `check_logs` class M | **fails**: `eic` whole (131 sections) | **fails**: `f2441` whole (245 sections) | none (`household` has no class M log) |
| `check_questions` | no change (never reviewed; already due) | **fails**: orphan record `f2441.paid_2026`; new id due | **fails**: orphan record; new id due; its ruling `unruled:household.spouse_died_2025#1` orphaned; reader `f1040.status` due |
| `check_screens` | screen `eic.died_in_year` "never reviewed", due at the next release; its ruling orphaned | none | none |
| `check_false_no` | none | none | none |
| `check_completeness` | `eic` due; 3 ruled findings leave the count | none | `household` due; 3 ruled findings leave the count |
| `check_consumers` | **fails**: 1 new, 1 stale key | none | **fails**: 1 new, 1 stale key |
| `coverage/tree.py --check` | fails until `docs/COVERAGE.md` is regenerated | | |
| `test-fixtures` (federal 1,768, New York 338) | pass | (run for the first id only) | |
| `review_store.py check`, `check_bug_inventory.py`, limits, operands, signs, instruction cites, citations, siblings, gate frequencies, adapter contracts | pass (run for the first id only) | | |
| `interview-rules` | **27 problems** (baseline 0); see 3.4 | (not run again) | |

Paid reruns the tools would plan for the three together (`rerun_all.py --forms eic,f2441,household --dry-run`,
its own estimator) [M]:

| Job | Scope | Prompt chars | Tool estimate |
|---|---|---|---|
| class M `eic` | whole | 2,291,151 | $3.09 |
| class M `f2441` | whole | 719,105 | $1.01 |
| transcription `eic` | `--lines auto` | 456,143 | $1.21 |
| transcription `f2441` | `--lines auto` | 243,994 | $0.64 |
| transcription `household` | `--lines auto` | 283,103 | $0.75 |
| render `f2441` | `--lines auto` | 82,257 | $0.21 |
| render `household` | `--lines auto` | 40,664 | $0.11 |
| **Total, 7 jobs** | | | **$7.02** (above the $3.00 gate: needs `--approve-cost`) |

Per id: `eic.died_2025` $4.30 (2 jobs), `f2441.paid_2026` $1.86 (3 jobs), `household.spouse_died_2025` $0.86
(2 jobs). Sampled reviews due beyond the baseline: 3 questions, 1 screen, 2 completeness reviews; at the
ledger's mean cost per call (question $0.06, screen $0.10, completeness $0.31) about $0.90. [M counts, I price]
**Total about $8 by the tool, about $16 at the current model's rate** (the ledger's `claude-fable-5-2` rows
run 1.4x to 3x the older model's cost per prompt character; the brief's factor of two is used).

The dollars are not the main cost. The 19 stale transcription lines are all ruled disagreements, the two class
M logs hold 3 more, and the orphaned question, screen and completeness rulings (1 + 1 + 6) would have to be
made again where the finding recurs. `carry.py` cannot repeat them (3.2). That is judgment-agent work.

### 3.4 A rename changes the seeded generated returns

Observation [M]: `interview-rules` at `355d7302`, pristine build: "0 problem(s)"; generated returns "12 walked
(1645 states)" federal, "(2044 states)" New York. Same commit with only `eic.died_2025` renamed everywhere it is
live: "27 problem(s)"; "12 walked (1571 states)" and "(2029 states)". The problems are 11 `f1095a.in_b_<month>`
templates "reachable before the answer that hides it", 13 `f1095a.in_a_<month>`/`in_b_dec` "asked in bank order
and unread by the complete return" (all on `generated.0`), and 3 entries of
`tools/interview_rules_baseline.json` "no longer asked and unread" (`f1095a.c_total`, `f8962.alien_below`,
`f8962.estimate_100`).

Interpretation [I]: `engine/src/generate.ts:937` (`derivedStream`) seeds a stream from
`JSON.stringify(Object.entries(inputs).sort(...))`, that is from the input ids as well as the values, so a
renamed input gives every generated return a different derived stream. I did not isolate that function as the
cause. Whatever the path, the observation stands: the generated sample depends on id names.

Two consequences:
- A rename cannot be proven neutral by "the same checks pass", because the checks no longer run on the same
  sample. Each landing of a rename batch needs someone to judge what the new sample finds.
- The `f1095a` findings look like a latent defect the current seed happens not to draw (a month's column B
  question reachable before its column A answer), independent of this study. One run, one sample: weak
  evidence, worth a look by whoever owns `f1095a`. I have not opened a BUG entry (read-only brief).

Every ruling that cites "500 generated returns seed 20261026" as triage evidence was made on the old sample. [I]

### 3.5 Extrapolation to the 35 line ids and the ambiguity ids

Method: for each id, the id was replaced as a whole token in `forms/` and `rendered/` of a pristine scratch
tree and every review subject recomputed with the project's own `subjects.py`
(`/tmp/yearfree/dump_subjects.py`, `sweep.sh`, `agg.py`). The method was checked against the real rebuild for
the three T-261 ids: identical line lists for transcription, render and class M. [M] It does not cover the
sampled reviews, which need the build; those are counted from the committed logs (1.1).

Per id (each alone) [M]:

| Id | Transcription: form, stale lines / compared | Ruled disagreements on them | Render | Class M logs (whole) |
|---|---|---|---|---|
| `eic.died_2025` | eic 16/20 | 16 | none | eic |
| `f2441.paid_2026` | f2441 1/37 | 1 | f2441 2/36 | f2441 |
| `household.spouse_died_2025` | household 2/19 | 2 | household 4/64, key renamed | none |
| `household.widowed_2025` | f1040 1/53; household 1/19, key renamed | 1 | f1040 2/58; household 1/64, key renamed | none |
| `f8962.married_in_2025` | f8962 3/97 | 3 | f8962 3/95 | f8962 |
| `f8880.dist_2025` | f8880 2/22 | 2 | f8880 3/21 | f8880 |
| `dependent.edu_a2025`, `dependent.edu_a2026` (each) | dependent 5/22 | 5 | dependent 5/11 | dependent |
| `person.edu_a2025`, `person.edu_a2026` (each) | person 5/104 | 5 | person 5/32 | person |
| `person.edu_born_2007`, `person.edu_born_2002` (each) | person 1/104 | 1 | none | person |
| `person.born_before_2001`, `person.born_after_1960` (each) | eic 16/20 | 16 | none | eic, person |
| `refund.not_2024` | refund 1/11 | 1 | none | refund |
| `refund.line5d_2024` / `line5e_2024` / `line17_2024` | refund 2/11, 1/11, 1/11 | 0 | refund 4/9, 3/9, 2/9 | refund |
| `asset.is2025` | asset 14/16 | 13 | asset 2/15 | asset |
| `asset.dep_2025` | asset 2/16; sc 10/55 | 12 | asset 1/15; sc 3/75 | asset, sc |
| `asset.bonus_2025` | asset 1/16; sc 6/55 | 7 | sc 3/75 | asset, sc |
| `asset.s179_2025` | asset 1/16; sc 4/55 | 2 | sc 2/75 | asset, sc |
| `asset.on_26_2025`, `macrs2025`, `mq_q4_2025`, `cost179_2025` | asset 2, 3, 1, 1 of 16 | 2, 3, 1, 1 | asset 2, 2, 1, 0 of 15 | asset |
| `scveh.is2025` | scveh 8/21 | 8 | scveh 13/27 | scveh |
| `scveh.s179_2025` | sc 3/55; scveh 1/21 | 3 | sc 2/75; scveh 1/27 | sc, scveh |
| the other 7 `scveh.*` (each) | scveh 1/21 or 2/21 | 1 or 2 | scveh 1 to 4 of 27 | scveh |

Ids overlap heavily (three ids each stale the same 16 `eic` lines), so the batch is far cheaper than the sum.

**All 35 at once**, by a real rebuild of the scratch copy and by the union of the sweep (the two agree) [M]:

| Review | Falls due | Detail |
|---|---|---|
| Transcription | 12 logs, **80 compared lines** | asset, dependent, eic, f1040, f2441, f8880, f8962, household, person, refund, sc, scveh. 73 of the 80 are ruled disagreements. `dependent` reruns whole (a form with partial-input cases) |
| Render | 11 logs, **50 lines** | 3 of them ruled mismatches; 2 `household` keys are the renamed ids |
| Class M | **10 logs, whole** | asset, dependent, eic, f2441, f8880, f8962, person, refund, sc, scveh: 1,211 sections, 37 ruled disagreements |
| Questions | 170 due against 143 before: **+27**; `check_questions` fails on **14 orphan records** | |
| Screens | **+2** (`eic.died_2025`, `refund.not_2024` under their new names) | |
| Completeness | **+4** forms (eic, f8880, household, scveh); 11 ruled findings leave the count; one ruling error: `unruled:f4562#5.2` names a renamed line in its `covered` field | |
| False-no | 0 | |
| Consumers baseline | 3 new, 4 stale keys; fails | |

Cost [M for the first line, I for the rest]: `rerun_all.py --dry-run` prices the 23 transcription and render
jobs at **$17.62**. It could not build the 10 class M requests in my scratch copy, because my whole-token
replacement did not reach collection-instance keys in fixtures (`person[taxpayer].edu_a2025`,
`asset[item_1].is2025`): 279 of 1,768 fixtures failed there. That is a defect of my scratch procedure, and a
warning for any real one: **16 fixture keys of that form are missed by a search for the dotted id.** From the
two class M jobs that did price ($3.09 for 131 sections, $1.01 for 245) the ten are roughly $15 to $25. Sampled
reviews about $3. **Batch total roughly $35 to $45 by the tool, $70 to $90 at the current model's rate**, and
113 ruled disagreements (73 + 3 + 37) to adjudicate again where they recur.

**Document `clcw26`.** A document id is part of each record's identity (`review_store.check`: the record must
name its form), so a renamed document's three logs cannot be re-pointed: a whole re-review. Dry run: $1.30 for
the three (transcription $1.07, render $0.07, class M $0.16), about $2.60 at the current rate. [M]

**Ambiguity ids.** Dropping the year from all 100 (`amb.2025.x` -> `amb.x`) would leave transcription and class
M current (the `ambiguity` link is a wording field outside those subjects; 1 transcription line moves) and
stale **317 render lines in 41 forms**, 61 of them ruled, plus the question and completeness subjects of the
45 forms that link an entry. [M for render and transcription; I for the sampled reviews, not built] That is
most of a render round (a round is priced at about $85 in the ledger) for no gain over the origin-year rule.

---

## 4. May the append-only records be rewritten?

By the project's own checks [M]:

| Record | Rule | Enforced by | On a rename |
|---|---|---|---|
| `BUG_INVENTORY.md` | "append-only": HEAD's content must be a byte-for-byte prefix of the working file | `tools/check_bug_inventory.py` (check-all, pre-commit for merges) | **may not** be rewritten. 20 mentions of the 35 ids, 21 of `amb` ids stay as written |
| Review store records `reviews/store/<kind>/<sha>.md` | "stored once and never rewritten"; the file name is the hash of the pass's identity (kind, form, family, scope, **each scoped line's subject key**, prompt and response hashes) | `review_store.py check`: "record ... is not the pass its name hashes"; `write_record` refuses other content under a stored sha | **may not** be rewritten. 118 distinct records mention one of the 35 ids |
| Review indexes `reviews/<year>/<kind>/<form>.index.json` | mutable by design: "the form's index says which lines it still judges"; `year_carry.py --write` writes carried entries into them | `review_store.py check`: records exist, the view parses back, **the view's sections are the index's lines**, every key with a subject has a verdict section | may be rewritten in their subject hashes. A **key** cannot simply be renamed: the section heading in the immutable record carries the old key, so "the view's sections are not the index's lines" would fail. A class M index takes its subject from the immutable base record's header |
| Ruling sidecars `*.rulings.json` | bound to a review context hash; "Legacy rulings without a context remain historical records, but are never automatically reused" | `rulings.check()`: each ruling in a log equals its sidecar's | keys are log keys (unchanged unless the id is the key); the ids appear in ruling **prose** (6 in `eic.rulings.json`), which is history |
| Sampled logs and rulings (`questions/<form>.json`, `screens/screen_review.json`, `*/rulings.json`) | a record holds one `subject_sha`; a ruling is accepted only with its unit's current `subject_sha` | `check_questions.py` (an orphan record **fails**), `check_screens.py`, `check_completeness.py`, `check_false_no.py` | the old record must be removed or re-keyed, or the check fails; the sample's stored response names the old id |
| `reviews/2025/consumers.json` | rulings and a shrink-only baseline keyed `consumer:<id>@<doc>:<page>` | `check_consumers.py` (stale key **fails**) | key must be rewritten (mechanical; the ruling's text does not name the id) |
| Committed rulings' prose, adjudication notes, handoffs, dated docs | point-in-time documents | `check_docs_conventions.py` (dated names) | leave as written |

The honest treatment follows from the table:
1. **Leave history as written.** BUG entries, store records, ruling prose, dated docs, handoffs and the ignored
   raw prompts keep the old names. Rewriting them is forbidden for the first two and dishonest for the rest:
   the reviewer was shown `eic.died_2025`.
2. **Keep one rename ledger in the tree**, read by people and by tools: `old id, new id, date, commit, class
   (T/N/P/O/M)`. A reader who meets `f2441.paid_2026` in BUG-0111 finds the current name in one place.
   `siblings.py` and any tool that resolves an id from a BUG entry or an old record consult it.
3. **Carry by proof, not by rewriting what was reviewed.** Where a tool is to treat an old verdict as current
   under the new name, it must first prove the two documents equal up to the ledger's substitution, and it may
   then write only mutable files (indexes, sampled-log keys and subject hashes, baseline keys), each entry
   marked with the ledger row it was carried under. Records, and the verdict text inside them, are untouched.
4. **Do not alias at hash time.** The alternative, mapping new ids back to old ones inside `subjects.py` so
   that no hash ever moves, needs no rewrite at all but puts a permanent indirection in the integrity path of
   every review check, in both Python and TypeScript (`premiseDigest`). It trades a one-time, checkable step for
   a standing one that every later reader of a subject hash must know about. I recommend against it.

---

## 5. The options

Common to every option that renames: the names are a judgment (1.2), `f2441.paid_2026` is a correction and
not a year rename, history keeps the old names (4), and the seeded sample moves (3.4).

### (a) Rename the ids in place now, in the 2025 tree

- **Changes:** 35 line ids (and, if included, document `clcw26` with 26 more). 314 distinct tracked files
  mention one of the 35 (118 immutable records, 72 other review files, 48 generated, 34 docs, 18 fixtures,
  12 forms, 5 interview, 4 tools, 2 engine, BUG_INVENTORY). About 40 are edited by hand or script; the generated
  ones follow from the build; the rest stay. [M]
- **(a1) and pay for the reviews.** 12 + 11 + 10 logs, 27 questions, 2 screens, 4 completeness reviews: roughly
  $70 to $90 at the current rate, plus up to 113 rulings made again by a judgment agent, plus re-keying the
  orphaned sampled records and `consumers.json` by hand. The 2026 adoption then reviews most of the same lines
  again (the rehearsal carried 5 of 1,211 transcription lines; "cited text changed" on 956), so much of this
  money buys evidence with a short life. [M rehearsal figures from `research/ty2026/review_carry_rehearsal.md`,
  which ran before most 2026 documents existed; I that the final documents still change most cited sections]
- **(a2) with a rename-carry tool.** Does not exist. It would have to: prove the tree equals the pre-rename
  commit under the ledger's substitution; rewrite the per-line subject and foreign-interface hashes in 23
  transcription and render indexes; handle 10 index keys that are themselves renamed ids (the view check
  compares them with headings inside immutable records, so `review_store` needs a key alias); give class M an
  index-level "carried subject", since its subject sits in an immutable record header (a change to
  `subjects.index_state`); re-key 14 question records, 2 screen records, their rulings, 3 `consumers.json`
  keys and one completeness `covered` field, and recompute their `subject_sha`. It changes what "current"
  means in the integrity path of every review check, so it is a design the owner approves, and judgment-class
  work to build (one session, with tests). All 113 rulings then stand. The seeded-sample shift remains.
- **Charter tests:** one change: no effect afterwards. One rollover: removes the id part of the worklist (222
  of 2,099 literal lines) and lets `year_carry` carry the lines that read these ids.
- **Risk while it lands:** (a1) low to integrity, high in churn; (a2) the highest of all options, because a
  tool marks 2025 evidence current without a model having seen the new names.
- **Size:** (a1) one mechanical lane plus one adjudication lane, a full check-all tier; (a2) the tool first.

### (b) Keep the ids, make the year in them a derived suffix

- **Changes:** forms would write `eic.died_{Y}` and the build would expand it, so adoption copies files and the
  id becomes `eic.died_2026` by itself.
- **Why it fails:** the id still differs between years. That breaks spec 4.3 ("stable identifier that survives
  ... between years"); `year_carry` rejects the line and every line that reads it unless it too learns to
  normalize ids [M, section 2]; every keyed store (question records, screens, consumers, index keys, fixtures,
  `generate.ts`, pins) is re-keyed every year instead of once; and the seeded sample moves every year. It also
  cannot express class O (five different offsets) or fix class M.
- **Charter tests:** one rollover becomes mechanical for the forms and stays manual for the evidence, every
  year. Worse than (a) and (c) on the test it is meant to serve.
- **Not recommended.** The useful half of the idea is for *wording*, where a year token expanded at build is
  what the measurement doc proposed; that is a separate piece of work (6.4).

### (c) Leave the 2025 ids; rename once, at adoption, in the new year's tree

- **Changes now:** none to any id or review. Decide the names and write the ledger; add a check that refuses a
  *new* year-bearing id. **At adoption:** `year_diff.py --adopt` applies the ledger while it copies 2025 to
  2026 (forms, interview, register links), `fixtures_year.py` applies it to input keys, including the
  collection-instance form, and `generate.ts`, `generate_cases.py`, `coverage/tree.json` are edited in the same
  change. The 2026 reviews are written under the new names from the start; no 2025 record, index or ruling is
  touched.
- **Reviews:** zero fall due in 2025. In 2026 the affected lines (80 transcription, 50 render, 10 class M
  documents at today's count) are reviewed as part of the adoption round, which reviews most lines anyway.
  If the owner wants them carried rather than reviewed, the ledger becomes one more normalization in
  `year_carry.py`, beside `{Y}`: the same proof as (a2), but writing only the new year's indexes, which
  `year_carry --write` already does.
- **Charter tests:** one change: untouched. One rollover: the first one carries the rename as one mechanical
  step of adoption; every later one has no year in an id.
- **Risk while it lands:** the lowest for 2025 evidence (none is rewritten). The rename lands inside the
  adoption, which already has the most moving parts; and the 2025 and 2026 trees differ in 35 ids for good,
  bridged by the ledger in every cross-year tool.
- **Does the debt grow while it waits?** Under (a), yes: each review that lands on a line reading these ids is
  one more to redo. Under (c), no, provided no new year-bearing id is added: the rename is applied by the
  ledger whatever has been built on the names. That is what the check is for.
- **Size:** now, one small judgment task (names, rule, ledger) and one small tool change (the check, shrink-only
  baseline of the 35 ids and `clcw26`). At adoption, ledger support in two tools.

### (d) Do only the three T-261 ids now, as a pilot

- **Changes:** 3 ids; 7 paid reruns (about $16 at the current rate with the sampled reviews), 22 or more rulings
  made again, 2 question records and 2 consumer keys re-keyed, 1 screen and 2 completeness reviews due.
- **What it would teach:** that a rename stales what section 3.3 already shows; nothing about a carry tool,
  because none exists to pilot.
- **It is a poor sample:** one of the three is a misnomer needing a new name by judgment, one is a render log
  key, none is a collection field (the case my own scratch procedure got wrong), and it moves the seeded sample
  once now and again for the other 32.
- **Not recommended** as a landing. As a *rehearsal in a scratch copy* it is done: this study is it.

---

## 6. Recommendation

**Option (c), with its preparation done now.** I am recommending against paying this debt in the 2025 tree
before more work lands, which is what the brief says the owner wants, so the reason first: the measurements
say the debt does not grow with work on the existing names if the rename is applied by a ledger at adoption,
while renaming in 2025 costs $70 to $90 and up to 113 rulings (or a tool that rewrites what "current" means for
2025 evidence) to buy names that the 2026 adoption round will review again anyway.

### 6.1 Do now

1. **Write the rule** (spec 4.3 and charter section 7 item 4): an id carries no year. The tax year is unmarked;
   the year before is `prior_`; the year after gets one agreed word; an age or recovery cutoff is named for its
   purpose; a calendar year that is a fact (`placed_year` values) is a value, never part of an id.
   `amb.<year>.<slug>` is the edition that first recorded the entry and does not change when the entry is
   carried.
2. **Write the rename ledger** with the 35 line ids and `clcw26`, each with its class and agreed new name.
3. **Add a check that refuses a new year-bearing id** (line, parameter, enum, table, document), with a
   shrink-only baseline of today's 35 and `clcw26`. The project's `YEAR_ID` pattern in `year_diff.py` is the
   test. This is what stops the debt growing.
4. **Exempt `amb.<year>.` ids from the adoption worklist** (381 of the 2,099 literal lines) and correct the
   T-261 row: `f2441.paid_2026` is `NonNegDollars` and a misnomer, and the scope is 35 ids, not 3.
5. **Look at the `f1095a` reach findings** from 3.4 as a possible defect in its own right.

### 6.2 Do at adoption

6. `year_diff.py --adopt` and `fixtures_year.py` apply the ledger; the engine and tool files that name ids are
   edited in the same change; `clcw26` is renamed there too (a whole review of a 26-line form, about $2.60).
7. Decide then, from the real 2026 carry report, whether the ledger is worth adding to `year_carry.py` as a
   normalization. If few lines carry anyway, do not build it.

### 6.3 Mechanical and judgment

| Part | Class |
|---|---|
| Choosing the 36 names; deciding the "next year" word; the name for `f2441.paid_2026` | judgment (owner confirms) |
| Writing the rule into spec and charter | judgment, small |
| The no-new-year-id check and its baseline | mechanical to write once the rule is fixed; its self-test is the proof |
| Applying a ledger row to forms, interview, fixtures, generator and tool files | mechanical. Proof that nothing else changed: apply the inverse substitution to the result and require `git diff --quiet` against the starting commit, with the new name absent from that commit (`git grep -F`); then `build`, `render`, `test-fixtures` (both jurisdictions) unchanged in count and values |
| Collection-instance keys (`person[taxpayer].edu_a2025`) and concatenated fragments in `generate.ts` | mechanical only if the script knows both forms; a search for the dotted id misses them [M] |
| Regenerating `rendered/`, reports, `docs/COVERAGE.md` | mechanical |
| Re-keying `consumers.json`, question and screen records, their rulings | mechanical in form, but it edits committed rulings: needs the owner's rule on carry by proof |
| Rerunning reviews; ruling the disagreements that recur | paid, and judgment |
| Judging what the changed generated sample finds (`interview-rules`, properties, triage witnesses) | judgment |
| Re-making a mutation pin whose premise digest moved | judgment (the argument must be re-read), small |

### 6.4 What this does not cover

Year literals in wording are 1,378 of the 2,099 lines and are untouched by any id rename. A year token expanded
at build would change every review subject that hashes source text unless the subjects are computed after
expansion. That is the larger half of charter section 7 item 4 and deserves its own study before anyone starts.

### 6.5 What would change my mind

- **The 2025 tree stays under active change long after 2026 is adopted** (amended-return support, backported
  fixes), so two trees with different ids are a standing cost: then (a2), once, now.
- **The owner rules out carry by proof altogether:** then (c) without the `year_carry` normalization, or (a1)
  if clean 2025 names are worth $70 to $90 and the adjudication.
- **The real 2026 carry report shows most lines carrying:** then the renamed lines are the exception that is
  re-reviewed, and the `year_carry` normalization becomes worth building.
- **Adoption is far off and a wording pass (phase 3) will rewrite and re-review these same forms first:** then
  rename each id in 2025 inside that pass, when its lines are being re-reviewed for another reason. The
  per-id table in 3.5 says which forms.

---

## 7. The T-261 pilot: not safe to run mechanically

My measurements do **not** show that the three ids can be renamed with every review carried and no judgment
call. They show the opposite:

1. No tool carries a review across a rename; after the rename `check_logs`, `check_questions` and
   `check_consumers` fail, and 7 paid reruns are planned ($7.02 by the tool, above its $3.00 gate). [M]
2. 19 ruled transcription disagreements, 3 class M ones and 8 sampled rulings would need a judgment agent. [M]
3. `f2441.paid_2026` needs a new name chosen, not a year removed. [M]
4. `household.spouse_died_2025` is a key of the `household` render log. [M]
5. `interview-rules` goes from 0 to 27 problems on a changed generated sample. [M]

So the coordinator should not run it tonight. If the owner nevertheless chooses to pay for it, this is the
procedure, with the steps that are not mechanical marked:

1. Claim `eic`, `f2441`, `household` and `inputs` (`tools/claims.py`); work in a worktree with
   `tools/worktree_data.py clone`.
2. **Judgment:** fix the three new names; confirm each is absent: `git grep -n -F '<new>'` prints nothing.
3. Replace each id as a whole token (not preceded by `[A-Za-z0-9_.]`, not followed by `[A-Za-z0-9_]`) in
   `forms/`, `interview/`, `fixtures/`, `engine/src/`, `tools/` except `tools/year_diff.py`. Expect 19, 11 and
   18 files.
4. Proof of purity: apply the inverse replacement to a copy of the tree; `git diff --quiet HEAD` on those
   directories must pass.
5. `npm run compile`, `build`, `render`; `test-fixtures` and `test-fixtures --ny` must report 1,768 and 338.
6. Re-key `reviews/2025/consumers.json` (2 keys), `reviews/2025/questions/f2441.json` and `household.json`
   (2 records), `questions/rulings.json` (1), `screens/screen_review.json` and `screens/rulings.json`
   (`eic.died_2025`). **Needs the owner's rule**, since these are committed rulings.
7. `python3 tools/coverage/tree.py`; `python3 tools/transcription/check_logs.py` must list exactly: transcription
   `eic` (16 lines), `f2441` (16), `household` (2); render `f2441` (16, 17), `household` (4, one no longer
   compared); class M `eic`, `f2441`. Anything else means something else changed.
8. **Paid:** `rerun_all.py --forms eic,f2441,household --approve-cost 7.02`; then the due question, screen and
   completeness samples.
9. **Judgment:** rule the disagreements; judge the `interview-rules` findings on the new sample; re-make any
   pin the full tier reports.
10. Append the three rows to the rename ledger; BUG entry for the change; `tools/check_all.sh` in the worktree.

---

## 8. One-page summary

**Question.** Ids that carry a tax year must be renamed or duplicated at every rollover. Pay now, later, or
never?

**What exists (measured at `355d7302`).**
- 35 line ids with a year (16 inputs, 19 computed), one document id (`clcw26`), 100 ambiguity ids, 21
  placed-year enum values, 28 fixture case ids. 3,681 of 3,716 line ids are already year-free and follow a
  consistent practice (tax year unmarked, `prior_` for last year, cutoffs named by purpose).
- The 35 split into: this year 22, next year 2, prior year 4, fixed offset 5, misnomer 1 (`f2441.paid_2026`, a
  dollar amount that has nothing to do with 2026). `amb.2025.*` and `y2019` name facts that do not roll.
- Year literals in wording are six times the id problem: 1,378 lines.

**What a rename costs.**
- Every review subject contains ids; several stores are keyed by them. No tool carries anything across a
  rename.
- The three T-261 ids: 3 transcription, 2 render, 2 class M logs stale; two checks fail outright; about $16 and
  22 or more rulings to redo.
- All 35: 12 + 11 + 10 logs (80 and 50 lines, 1,211 class M sections), 27 questions, 2 screens, 4 completeness
  reviews; roughly $70 to $90 and up to 113 rulings.
- A rename changes the seeded generated returns: `interview-rules` went from 0 to 27 problems with one id
  renamed.
- BUG_INVENTORY and the review records may not be rewritten; history keeps the old names and needs a ledger.

**Options.**

| | Reviews due | Cost now | Rollover after | Risk |
|---|---|---|---|---|
| (a1) rename now, rerun | all above | $70-90 + adjudication | clean | churn; evidence re-reviewed again at adoption |
| (a2) rename now, carry by a new tool | none | build the tool; owner approves carry by proof | clean | highest: a tool marks 2025 evidence current |
| (b) year as a derived suffix | every year | tool work | never clean; breaks the spec's id rule and the cross-year carry | high |
| **(c) ledger now, rename at adoption** | **none in 2025** | **names, rule, one check** | **clean after the first** | **lowest; two trees differ in 35 ids** |
| (d) pilot the three | 7 jobs | $16 + adjudication | no change | teaches nothing new |

**Recommendation: (c).** Now: write the naming rule, the ledger of 36 names, and a check that refuses any new
year-bearing id; declare `amb.<year>.` an origin year; leave the 2025 ids and all 2025 evidence alone. At
adoption: the ledger is applied while the definitions and fixtures are copied to 2026. This goes against
paying the debt in 2025 first; the measurements say that buys little, because the debt stops growing once new
year-bearing ids are refused, and the adoption round reviews these lines anyway.

**The T-261 pilot is not safe to run mechanically tonight.** It fails three checks, needs paid reruns above the
cost gate, a naming judgment for `f2441.paid_2026`, and a judgment on a changed generated sample.

**Open for the owner.** (1) Is a verdict carried under a proven rename acceptable evidence, in principle?
(2) Will the 2025 tree stay under active change after 2026 is adopted? (3) The 36 names.

**Not checked.** Mutation pins beyond `eic.died_2025`; sampled-review effects of the ambiguity option; the
class M cost of eight of the ten documents (estimated from two); whether `derivedStream` is the cause of the
sample change; `carry.py` on a real rerun.

