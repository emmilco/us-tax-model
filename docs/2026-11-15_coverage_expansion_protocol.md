# Coverage expansion protocol

**Status: normative** (owner decision 2026-11-15; project `CLAUDE.md`) for any work that brings a form, schedule,
worksheet or situation now refused into scope, in the current tax year or a later one. Written 2026-11-15 and adopted
by the owner the same day. Items marked **[R]** were put as recommendations in the text the owner adopted; items
marked **[unverified]** could not be checked against the tree when this was written.

It cites the documents it rests on and does not restate them:

- `docs/consolidation_charter.md`: architecture, the verification table (section 4) and the process rules (section 5).
- `docs/2026-11-13_interview_construction_protocol.md`: every question, topic and form added to the interview.
- `docs/2026-10-24_validation_policy.md`: human readings are optional, and confirmed defects are fixed first.
- `spec/spec.md`: section 2.2 (refusals), 2.4 (the coverage goal and its order), 3, 6.
- `tools/README.md` and `tools/transcription/README.md`: tool behavior, which this document names by section.

Where spec 2.4 still asks for "two model families", the charter governs: reviews are Claude-only.

**Entry gate.** Charter section 1, item 3: coverage growth waits until the project is stable. A round under this
protocol starts only when the owner opens it, and that decision is recorded in the round's plan (step 1.4).

---

## 0. Roles and names

| Role | Model / class | Does |
|---|---|---|
| Coordinator | Opus / judgment | Runs intake, writes the round plan, launches lanes, decides escalations within the owner's delegation, approves review spend up to the owner gate |
| Source lane | Sonnet / mechanical | Archives the documents a round needs (section 2) |
| Build lane | Opus / judgment | Builds one area: forms, interview, fixtures, next-year operations (sections 3 to 5, 7) |
| Integrator | Opus / judgment | Merges one batch of lanes into one tested tree (section 8.5) |
| Adjudication lane | Opus / judgment | Rules one form's review disagreements (section 6) |
| Ruling lane | Sonnet / mechanical | Applies rulings that are already decided, formats bug entries, does bookkeeping |

- **Round:** one set of build lanes cut from one base, integrated in one or more batches, then reviewed once.
- **Round id:** short and lowercase, for example `nx1`. Lane branches are `<round>-<lane>`, for example `nx1-sche`.
  The branch name is also the default prefix of `new_bug.py --pending`.
- **Fable:** `claude-fable-5-2` replaces the default model only when the owner says so for the session (project
  `CLAUDE.md`).

---

## 1. Intake: choosing and scoping an area

The coordinator does this on `main` before any lane exists. The output is the round plan.

1.1 **Rank candidates by measured gain.**
- Read `reports/<year>/filer_coverage.md`, section "Coverage gained by each group", for the greedy order spec 2.4
  prescribes.
- Read `tools/coverage/categories.json` for the refusal gates each category stands for. Each category's `gates` list
  holds those gates.
- If `filer_coverage.json` is older than the forms' last change to a refusal, refresh the estimate first (section 9.3).
  **[unverified]** The committed report is dated 2026-11-01. It lists 188 refusal gates and names `scope.credits`,
  which has since been removed. `docs/COVERAGE.md` lists 234. The report is stale for the gate list. Whether its
  percentages are also stale was not measured here.
- A situation the estimate cannot measure is ranked by `interview/<year>/gate_frequencies.yaml`, or by a recorded
  judgment.
- **Stop rule (owner decision 2026-11-15).** Rerun the estimator first (section 9.3), then take the next area by its
  measured greedy marginal gain in `reports/<year>/filer_coverage.md`, while that gain is at least about 0.5 points of
  filer coverage; stop when the next area's gain falls below. An area the estimate cannot measure is ranked by the
  fallback above (gate frequencies, or a recorded judgment).

1.2 **Scope each chosen area as a row of the plan.** Each row records:

| Field | Content |
|---|---|
| Area | The plain name, and the forms, schedules and worksheets that will exist afterwards (new and changed `forms/<year>/<id>.yaml`) |
| Gates replaced | Every refusal gate (`refuses:` `when` line) the area removes, with its `categories.json` category. Every gate the area narrows, with the residual refusal that stays (section 3.4) |
| Gain | The share from the estimate (alone, and in ladder order), or "unmeasured" with its frequency source |
| Sources | Every document the area cites, for the current year and the next (section 2). Mark each as archived, to archive, or not yet posted |
| Dependencies | Forms it reads or feeds. Other areas it needs first, such as Form 8582 before Schedule E losses. Shared forms it must edit (`f1040`, `s1`, `person`, `dependent`, `household`, ...). A dependency that changes the estimate's order is recorded in spec 2.4, as that section requires |
| Split | The lanes it needs, with no two lanes owning one form file. Each lane must be small enough for one agent: an earlier lane of about 30 questions with model changes ran out of context. Each lane gets a ranked work list, so a lane that runs short has done the valuable part |
| Interview | Its place in the order of a life, its order-number range, and its persona-number range (section 4) |
| Next year | Whether `changes/<next>/` exists, which branch of section 7 applies, and which next-year documents are posted |
| Ripple | New inputs, and the shared files they touch (section 8.4) |

1.3 **Map before splitting.** If an area needs more than one lane, the coordinator (or one architect agent that
changes no code) writes the map that the construction protocol's phase 2 describes, before any build lane starts.
The map gives:
- the topic order;
- every catch-all taken apart, with each item's destination;
- the lanes and their forms;
- the shared decisions: naming, where new inputs are declared, how a refusing child is worded.

1.4 **Write the plan where the lanes will see it.**
- The plan file is `docs/provisional/lanes/<round>-plan.md`, in the form of `ty26-plan.md`.
- It labels evidence [V] verified, [T] testimony and [I] inferred.
- It includes the owner's opening decision.
- Commit it to `main` before cutting lanes. A lane of the TY2026 round worked from its launch message because the
  plan was not in its base (`ty26-o7.md`).
- Add one `TASKS.md` row for the round: `python3 tools/task_row.py add --task ... --source ... --due ...`.

---

## 2. Sources

2.1 **Archive before encoding.**
- One source lane per round writes `tools/sources/<year>.json` and `sources/<year>/`, for the current year and, where
  posted, the next year. Lanes that each append to the catalog collide in that one file.
- Commands, from `tools/README.md` ("Source archiving") and `docs/ty2026/ADOPTION.md` step 1:
  - fetch: `python3 tools/fetch_sources.py --year <Y> --fetch --only <ID...>`, then `--derive`;
  - verify the archive: `python3 tools/fetch_sources.py --year <Y>`;
  - check the extraction: `python3 tools/check_extraction.py --year <Y>`.
- Record in the manifest the printed year and revision that were read off the document. A download is not
  automatically a current-year source.
- Next-year drafts are marked `draft: true`. A draft never backs a release (spec 7).
- Page layouts a new extractor needs go in `tools/layouts/<year>.json` (`tools/README.md`, "Page layouts").

2.2 **Citation discipline.**
- Every line, parameter, guard, refusal and question carries a structured citation to an archived page (spec 3.1, 5).
- A quote must be printed on that page: `python3 tools/citations.py --strict` checks this, and so do the build and the
  source-title check.
- Secondary commentary goes under `research/secondary/` per the validation policy. It informs only a recorded
  ambiguity choice, never a blind review prompt, and it earns no evidence credit.

2.3 **Premises first.** Every premise the area rests on (a threshold, a selection rule, a "can be skipped when") is
checked against the archived text before the line that depends on it is written. Each check is listed in the lane
note (spec 10).

---

## 3. Encoding

The formal model is the only place tax logic lives (charter section 2). Per area:

3.1 **Forms.**
- `forms/<year>/<id>.yaml`, new or changed. Every line has an expression from the closed atom set, a citation, and
  refusals as values.
- Gates are A, B or C (formal gates design). A gated input keeps its id; the gate line `<input>_if_<cond>` reads it,
  and the input carries `gated_by`.
- Ids carry no year (`tools/check_year_ids.py`, spec 4.3).
- A line stated for both a person and a dependent is a twin: claim both forms and declare the pair in
  `reviews/<year>/twins.json` (tools/README.md, "Twin lines").

3.2 **Parameters and tables.**
- New parameters go in `params/<year>.yaml`, prefixed with the form's id and cited at the place they are printed. That
  lets `tools/propose_params.py` find them in the next edition.
- Declare `moves_with_year` or `extends_with_year` where it applies (tools/README.md, "Proposing a year's
  parameters", "Year-valued enums").
- A printed table goes in `tables/<year>/` and is written by an extractor with a `--check` mode that runs in check-all
  (tools/README.md, "Printed tables", "Scripts run by hand"). Otherwise it is listed as hand-written, with the reason.

3.3 **Ambiguities.**
- Every reading where the text is silent, ambiguous or in tension gets an entry in `ambiguities/<year>.yaml`, with an
  id prefixed by the form, linked from the line's `ambiguity` field.
- An entry must be linked, or must say why it is not (`unlinked`).

3.4 **Refusals that remain.**
- Each sub-case the area does not compute stays a refusal: gate, form named, remedy, citation (spec 4.7, 8).
- Each one is placed in `tools/coverage/tree.json` `gates` (topic, part, kind).
- A residual refusal whose estimate category still applies keeps that category's `gates` entry in
  `categories.json`. A retired gate is removed from both files (section 9.3).

3.5 **Fixture defaults.**
- Every new input gets exactly one default in `fixtures/<year>/defaults.json`, with its reason (tools/README.md,
  "Test-data defaults").
- Add `consistency` rules wherever the new answers can contradict others.
- A changed existing default needs `Fixture-default-changed:` lines in the commit (charter section 3).

---

## 4. Interview

`docs/2026-11-13_interview_construction_protocol.md` governs. Read it before the first question changes. Follow its
section 7 checklist and its phases 1, 4 and 6 as they apply to one area. This protocol adds only where things go:

| What | Where | Rule |
|---|---|---|
| Questions | `interview/<year>/questions.yaml` (bank entries; the tick-box `groups`) | Order numbers inside the area's range from the plan. Search the bank before adding a question |
| Profiles | `interview/<year>/full.yaml` and the others | Restated at integration (section 8.4) |
| Coverage rows | `interview/<year>/coverage/<topic>.yaml` | One file per new topic, owned by its lane. One row per refusal situation and per covered situation (`interview/README.md`, "Coverage rows") |
| Personas | `interview/<year>/personas/NN_<name>.yaml` | Numbers inside the lane's range. Two files were once both numbered 13 (T-316). Personas for the typical filer, the filer with nothing in the area and a refused filer; their walks are recorded before any change |
| Walks | `node engine/dist/main.js draft-walk --only <persona> --out <lane dir>` | The before and after walks are compared in the lane note |
| Refusal notes | `interview/<year>/refusal_notes.yaml` | Where a refusal needs a plain note |

What a lane checks: `interview-rules`, `tick-groups` and `interview-coverage` (with `--write` after a row or wording
change). Expected ends and the order-independence baseline are never edited to pass.

---

## 5. Fixtures

5.1 **Predict before you run.**
- Hand-predicted regressions are written in the lane note first, then as cases in `fixtures/<year>/<form>.json`.
  Each case states only the non-default facts and its evidence class (spec 6.1).
- Then they are evaluated. A case whose evaluated value differs from the prediction is investigated. Neither the
  prediction nor the value is ever edited to agree (`land3-fix.md`, `land3-holes.md`).
- Every official example found for the form is a class A case (spec 6.2).

5.2 **Branch coverage.** Together, the cases take both sides of every `smaller_of`, `larger_of`, `subtract_floor0`,
`choose` and gate of the new form (spec 6.2). Check this in `reports/<year>/coverage.md` (step `coverage`): no
**UNOBSERVED** guard of the new form remains without its reason.

5.3 **Mutation.**
- Every surviving mutant of the new form is either killed by a fixture case or explained by a pinned equivalence
  argument (`EQUIVALENT_IF` in `engine/src/mutate.ts`, with premise digest; tools/README.md, after "Wall times").
- `mutate.ts` is a full-tier path.

5.4 **Tool-managed files** (`classm*.json`, `mutation.json`) take no defaults.
- A lane writes only its own forms' cases there.
- Where a new input routes through other forms' class M or mutation cases, the lane states it in those cases, as a
  separate commit, and lists every file and count in its note ("what the merge must know").

5.5 **Adapter and input contracts.**
- If the form has an internal adapter line (plumbing, not an IRS quantity), it registers a host-only contract in
  `tools/transcription/adapter_contracts/<year>/<form>.json`.
- If its transcription needs partial-input facts, it adds an input contract bank in
  `tools/transcription/input_contracts/<year>/` (each directory's `README.md`).
- **[unverified]** This protocol does not establish when a contract is required beyond what those READMEs say.

5.6 **External engines (class C).**
- Where PolicyEngine-US, Tax-Calculator, OpenTaxSolver or UsTaxes compute the new situation:
  - extend the generators (`engine/src/generate.ts` `sampleReturns`, and `tools/engines/generate_cases.py`) so that
    generated returns reach it;
  - map the lines the engine computes (`PE_MAP` and `TC_MAP` in `tools/engines/run_engines.py`, and the adapters);
  - explain every difference in `fixtures/<year>/differential/engine_investigations.json` (`tools/engines/README.md`).
- Where no engine computes it, say so in the lane note. That is the gap the trust statement reports.
- `tools/engines/*` is a full-tier path. **[R]** Run this as a follow-on lane after the area's build lane merges, so
  the build lane stays on the fast tier.

---

## 6. Reviews

Reviews run once per round, on the integrated tree on `main`, after every fix of that form in the round has landed.
Build lanes make no paid calls. Every call is logged with year and jurisdiction.

6.1 **Which reviews run.** "Building" in charter section 4 applies to a new form:

| Subject | Reviews | Scope |
|---|---|---|
| New form | transcription, render, class M | Whole: no log exists, so `rerun_all.py` runs it whole |
| Existing form whose arithmetic changed (a line now reads the new form; a refusal removed) | transcription, class M | `--lines auto` (default); class M has no line scope |
| Existing form whose wording changed | render | `--lines auto` |
| New or changed refusal screens and gates | screen review (`screen_review.py`, kind `gate` for gates) | One sample per subject per milestone |
| New form's completeness; refusals a filer could answer No to wrongly | completeness, false-no | One sample per subject per milestone |
| New or changed questions | question review (`question_review.py`) | Per question subject |

6.2 **Commands.**
- Plan and price first: `python3 tools/transcription/rerun_all.py --forms <ids> --kinds transcription,render,classm
  --dry-run`.
- An estimate above $3.00 needs the owner's `--approve-cost DOLLARS`. Sampled runs (`completeness_review.py`,
  `screen_review.py`, `false_no_review.py`) are guarded the same way.
- A log that already answers its subject is not rerun without `--force-rerun REASON`.
- `carry.py` (and `triage.py`, for transcription) runs after each review. It rules repeats, and equivalences on
  executable triage, mechanically; 1 in 10 of these is held for audit.
- Review data runs in the main checkout, or in a worktree with `worktree_data.py clone` and `carry-back`
  (section 8.2).

6.3 **Adjudication.**
- One adjudication lane per form, or per small group of forms. It rules each open disagreement against the source
  with `rule.py --form F --kind K --rulings <file>`. There are three outcomes: project retained; second construction
  right (a data fix, a pending bug entry and a regression); genuine ambiguity (a register entry).
  - Method: `reviews/<year>/transcription/adjudication/README.md`.
- Class M rulings are applied only after the class M fixtures are merged by case id. The landing round had to wait
  for the merged class M data (`land3-adj12.md`).
- A finding that a help sentence or wording gives a wrong value or wrongly accepts a return is reported before it is
  fixed. A unit already edited once in the round is recorded open, not edited again (`HANDOFF-NEXT-SESSION.md`, entry
  of 2026-11-11/12).

6.4 **Rounds.** Fix, then the form's one rerun on what changed. A round whose reviews find only low findings starts
no further round; the lows wait for the form's next substantive change, recorded in a `TASKS.md` row as T-315 does.

6.5 **The bar for "covered".** **[R]** An area's gates count as covered, and are dropped from the estimate, only when
all of the following hold on `main`:
1. Full-tier check-all is green: fixtures, interview rules, coverage rows, mutation with no unexplained survivor,
   Lean comparison, engine differential with no unexplained difference and under its not-computed floor.
2. The transcription, render and class M logs of every form in 6.1 are current, with every disagreement ruled.
3. The sampled reviews of 6.1 have their sample and their union ruled (`tools/release_reviews.sh` passes for those
   subjects). Question reviews of the new questions are ruled.
4. Every confirmed defect is fixed, with a regression and broadened checks around it (validation policy, item 3).
   No non-low finding is open.
5. Every source backing the area is final.

Whether an area is covered is claimed at a release (section 10.2), not at a merge.

---

## 7. Tax-year rules

Let N be the newest year in `years.json` `adopted`. Coverage is built in N. Which branch applies depends on the next
year, N+1:

7.1 **N+1 in preparation (`changes/<N+1>/` exists; N+1 not adopted).** This is the current state: N = 2025, and
`changes/2026/` exists.
- The new form is built in `forms/<N>/`. At adoption, `year_diff.py --adopt` copies it to N+1 like every other form.
- The lane also writes the form's next-year changes, so they are prepared like the rest and checked on every commit:
  1. Archive the N+1 edition of each document the area cites (section 2), draft or final.
  2. Read it against the N edition. Write every difference as operations in `changes/<N+1>/<form>.yaml`, one file the
     lane owns per new form. Changes to shared forms go in split files `changes/<N+1>/<form>.<round>-<lane>.yaml`.
     - Format and kinds: tools/README.md, "Year changes as operations".
     - `year_changes.py --record EDITED.yaml` writes operations from an edited copy of the form.
     - New inputs carry `default` and `reason`.
     - Ambiguity entries use `add_ambiguity` and `set_ambiguity`.
     - Interview files use `set_interview`, `add_interview_item` and `add_interview_file`.
     - Each entry has evidence quotes on the archived N+1 page and `verified: draft|final`.
  3. Give each entry a change id. **[R]** Use `C-<ROUND>-<FORM>-NN`.
     - Append the entry to the N+1 change map (for 2026, `research/ty2026/changes.md`) in its format.
     - `year_changes.py` reads `change` but does not check it against the map. That is verified by reading
       `load_changes`.
  4. Record the documents with no difference as "no change" rows. A document not yet posted is recorded as awaited.
     The coordinator's bookkeeping commit adds these rows to the `changes/<N+1>/README.md` table.
  5. List the new parameters in the lane note for the next `propose_params.py --from N --to N+1` run. List new tables
     for extraction at adoption.
  6. Run `python3 tools/year_changes.py --check` in the lane. It also runs in check-all. Then run
     `python3 tools/year_shared_refs.py --year <N+1>` and list any reference in shared code to a line the operations
     remove.
- No paid review is spent on next-year operations. They are reviewed once, line-scoped, on the adopted finals
  (ty26-plan D10).
- Reviews carry at adoption with `year_carry.py` where the subject and the cited text are unchanged.

7.2 **N+1 not in preparation (no `changes/<N+1>/`).**
- Nothing more is written for N+1. Adoption carries the form.
- The lane note lists the area's documents for the N+1 archive refresh.

7.3 **N+1 adopted (years.json lists it; it becomes the new N).**
- Coverage added after that is built in `forms/<N+1>/` only.
- The earlier year takes defect fixes only. A fix that applies to both years lands in the newer year, and is ported
  to the earlier year only if it changes an earlier-year return (ty26-plan D12).
- If N+2 is in preparation, 7.1 applies with N+1 as the base.
- **[unverified]** D12 is a decision the TY2026 plan made on the owner's behalf. `TASKS.md` T-300 still lists "the
  owner decision whether the 2025 tree stays under change after 2026 is adopted" as open. **[R]** The owner confirms
  D12 when adopting this protocol.

7.4 **New York.** New York keeps its scope until the owner widens it (charter section 1).
- A federal area changes New York only through the federal lines New York reads.
- The lane runs the New York steps (`test-fixtures --ny`, `ny_compare` in the full tier). It reports any New York
  line whose value moves, and changes no New York form without an owner decision.

---

## 8. Parallel execution

8.1 **Lanes and claims.**
- One area or sub-area per lane. No two lanes own one form file.
- Each lane claims its forms at launch, from its own branch in its own worktree:
  `python3 tools/claims.py claim <form...> --reason "<round> <lane>"`.
- A lane that edits one twin claims both. Shared forms the plan lets several lanes touch (`f1040`, `s1`, `person`,
  `dependent`, `household`) are assigned to one lane per batch. A second lane needing a change there writes it under
  "Requests" in its note, for the owner to route.
- **The `inputs` claim serializes new inputs.** Verified in `tools/claims.py` `check`:
  - a commit on a lane branch that adds an input id claims `inputs` for that branch;
  - another branch's commit that adds an input id is then refused until the holder merges.
- Coverage lanes all add inputs. **[R]** Lanes commit only when the integrator calls them in, in turn. Before each
  lane's commit, the integrator releases the previous holder's `inputs` claim with `claims.py release inputs` and
  gives the reason in the merge message. New input ids are prefixed by their own claimed form, so two lanes' new ids
  cannot collide, and the integrator does the ripple through shared files (8.4).
- A per-form inputs claim in `claims.py` would remove this step. That is a tool task, not part of this protocol.

8.2 **Worktrees and review data.**
- `git worktree add .claude/worktrees/<round>-<lane> -b <round>-<lane> <base>`.
- Then, from the main checkout: `python3 tools/worktree_data.py clone .claude/worktrees/<round>-<lane>`.
- Never copy `.transcription/` or `.classm/` by hand; `bash_guard.py` refuses it. Missing files come with `fill`.
- Results return with `carry-back --dry-run`, then `carry-back`.
- Carry-back leaves tracked files to the branch's commits. A lane that wrote tracked review files (class M fixtures,
  indexes) commits them, or lists them, so the integrator does not lose them (`land3-adj12.md`).
- Use `--prefer-worktree` only after checking which copy the committed logs were written from.
- One worktree per lane, never shared. Lanes sharing `.claude/worktrees/landing` saw stale builds from each other's
  edits (`land3-adj13.md`).
- Use absolute paths. Never `cd` inside a backgrounded command: one lane's checks once ran in the main checkout
  (`land3-mutate.md`).

8.3 **Bases, snapshots, re-basing.**
- Every lane of a round is cut from one base ref, `refs/scratch/<round>-base`, which is a commit of `main` that
  contains the plan.
- The lane note records the base hash.
- A lane re-bases (merges `main` into its branch, or replays its own scripts on `main`'s files) in two cases:
  - when `git diff --name-only <base> main` names a file the lane changed, or a form its forms read;
  - and always before its final check, if a batch merged since its base.
- Generated files are never merged or carried; they are regenerated after a merge or re-base. These are
  `canonical/`, `rendered/`, `reports/`, `docs/COVERAGE.md`, the README coverage block, and walk transcripts. Stale
  renders in snapshots misled several lanes (`land3-mutate`, `land3-consumers`, `ty26-p2`, `ty26-r6`).

8.4 **Shared files.** Each file below has an owner and a merge rule. The integrator merges by structure, never by
text alone:

| File | Lane may | Merge |
|---|---|---|
| `fixtures/<year>/<form>.json` (own forms) | write | — |
| `fixtures/<year>/classm*.json`, `mutation.json` | own forms' cases; restatements listed (5.4) | by case id (`tools/merge_classm.py BASE THEIRS OURS OUT` for `classm.json`) |
| `fixtures/<year>/defaults.json` | add its new inputs' defaults and rules | by input id and rule; `Fixture-default-changed:` lines for changed ones |
| `interview/<year>/questions.yaml` | entries in its order range; its groups | by bank entry id; profiles' input lists restated |
| `interview/<year>/coverage/<topic>.yaml`, personas | own files | — |
| `params/<year>.yaml`, `ambiguities/<year>.yaml` | own-prefix keys and ids | by key and id |
| `tools/coverage/tree.json` | `gates` placements of its own gates; retiring the gates it replaces | by gate id; the `table` changes go to the integrator |
| `tools/coverage/categories.json` | nothing | integrator (9.3) |
| `reviews/<year>/{twins,consumers,operands,limits,signs,instruction_cites,input_quotes}.json` | entries for its own new lines only, listed in the note | by key |
| `engine/src/generate.ts`, `tools/engines/*`, `engine/src/mutate.ts` | one delimited block per form | integrator, by hand; full tier |
| `changes/<N+1>/` | own files and split files (7.1) | `year_changes.py --check` after each merge; a collision is resolved in the later lane |
| `tools/sources/<year>.json`, `sources/` | source lane only | — |
| `BUG_INVENTORY.md`, `TASKS.md`, `changes/<N+1>/README.md` table | nothing: pending entries and note requests | coordinator's bookkeeping |
| `research/costs/agent_runs.jsonl`, `.transcription/costs.jsonl` | through the hooks and `carry-back` only | — |

A lane never edits an expected value, an expected refusal, a coverage row's end, or a check's baseline to pass. If one
would have to change, the lane stops and reports.

8.5 **Merge batches.** Lanes that finish together are integrated as one batch, with one full check-all and one merge
commit. `880445b2` merged six lanes as one commit with seven parents.
1. In an integration worktree on `main`: `git merge --no-ff --no-commit <lane tips...>`. If the octopus refuses
   because of conflicts, resolve the shared files by 8.4 and conclude one merge naming every lane tip.
   **[unverified]** How `880445b2` was assembled was not read. Prefer sequential lane merges in the integration
   branch over hand-built trees if conflicts make the octopus impractical. That costs one green run per merge
   commit, since the pre-commit hook runs on every concluded merge.
2. Regenerate the generated files (8.3). Run `interview-coverage --write`, `tree.py`, and `year_changes.py --check`.
3. Drop duplicate pending bug entries before assigning; parallel lanes find the same defect (`land3-adj9.md`). Then
   run `python3 tools/new_bug.py --assign`, then `git add -A`.
4. Run `tools/check_all.sh --tier full` on that tree. The hook requires only fast for a merge, but the bar of 6.5
   needs mutation, the Lean comparison and the engine differential.
5. `git commit -F <message>`. The message lists each lane, the `BUG-NEW -> BUG-NNNN` lines, any `inputs` release
   reasons, and the `Fixture-default-changed:` lines. Merging releases the lanes' claims.
6. Run the coordinator's bookkeeping commit (section 9).

8.6 **CPU budget.**
- At most `CHECK_ALL_MAX_RUNS` (default 2) check-all runs execute on the machine at once; further runs wait for a
  slot (`tools/check_slot.py --status`).
- Measured times (tools/README.md): full tier 13 to 32 minutes, median 17; fast tier median 7; docs tier 1 to 4.
- While working, a lane runs the quick bar: `npm run compile`, `node engine/dist/main.js build`, `render`,
  `test-fixtures`, `interview-rules`, `tick-groups`, `interview-coverage`, and `python3 tools/coverage/tree.py
  --check`. It never runs two checks at once.
- A lane runs targeted checks only, never check-all (owner, 2026-11-15): the build, its own fixtures and coverage
  rows (`test-fixtures`, `interview-coverage`), `python3 tools/citations.py --strict`, `python3 tools/year_changes.py
  --check`, and the self-tests of the tools it changed. Check-all runs once per integration batch, on the merged tree
  (8.5, step 4).
- Wait on a pid, or poll `tools/check_all_bg.sh --status`, always with a timeout. Never wait with `pgrep -f`.
- **[R]** Run at most six build lanes at once. Sixteen agents made one coverage step take over thirty minutes
  (construction protocol section 5). The TY2026 plan inferred about eight.

8.7 **Lane briefs.** Every brief has the parts of construction protocol section 5, plus what follows. Three of those
parts are written out in the brief itself, for the lane's topic, not left as a pointer to the protocol (owner,
2026-11-15):
- the typical filer of the topic, described, and the filer with nothing in it (construction protocol 5.4; checklist 1);
- the risk particular to this lane, named (5.5);
- the measure the lane is judged by: steps, questions, prompt words and help words for the typical filer and for the
  filer with nothing in the topic, before and after (checklist 8).

The rest of the brief:
- the lines `Model:`, `Class:`, `Year:`, `Jurisdiction:` (the launch hook refuses a brief without them);
- the worktree, branch and base hash, and the forms claimed;
- "no paid reviews, no model calls from code, never the main checkout, never push";
- what to read, in order: this protocol's sections for the lane, the round plan's row, the construction protocol,
  and named worked-example commits;
- what not to touch: 8.4;
- the ranked work list, and the instruction to stop and report a blocking rule rather than design around it;
- a request for a written handoff before the lane's context runs out. Two lane agents outgrew their context
  mid-landing (`HANDOFF-NEXT-SESSION.md`).

8.8 **Lane notes and report.**
- Notes go in `docs/provisional/lanes/<round>-<lane>.md`, written as the lane works.
- Header: model, class, year, jurisdiction, worktree, base, and what was not done ("no paid reviews; check-all tier
  X run / not run").
- Sections, in this order:
  1. What the merge must know: shared-file changes, restated cases, moved questions.
  2. What changed.
  3. Decisions, each with the alternative rejected.
  4. Gates replaced and residual refusals.
  5. Next year (7).
  6. Defects (`BUG-NEW-...`).
  7. For other lanes and requests.
  8. Verification: a command and result table, with "not run" stated.
  9. Review debt: the forms and kinds of 6.1, and the dry-run estimate.
  10. Walks before and after: steps, questions, prompt words and help words for the typical filer and the filer
      with nothing in the topic (construction protocol checklist 8).
  11. Left open, in rank order.
  12. The judgment record (construction protocol section 2; checklist 7): for each new parent question, who could
      answer No wrongly and what guards it; and the cost and share table behind each parent and each split.
- What was run and seen is stated apart from what is inferred.

8.9 **Waves run in parallel by owner decision.** Married filing separately ran in parallel with wave X1 (Schedule E,
Form 1116, digital assets) by owner decision 2026-11-15, overriding the earlier sequencing that put it after the wave.
Merge caution: lanes that run in parallel own disjoint form files, and their changes to shared files (fixtures,
`questions.yaml`, defaults) are merged by id (case id, input id, order and seq), never by taking one lane's copy.


8.10 **Running a parallel round.** Operating facts learned on 2026-11-15:
- **CPU.** Lower lane processes off the critical path with `renice +15`. Do not use macOS `taskpolicy -b`: it stalled
  lanes. While a gating check finishes, pause lane compute with `SIGSTOP` and resume it with `SIGCONT`; never pause
  the agents themselves or the gating check. Pace about one build per two cores.
- **Review calls.** About six concurrent `claude -p` review calls run cleanly; at about eight, calls fail with an
  empty `claude exited 1`.
- **Class M.** Class M runs share the tracked `fixtures/<year>/classm.json`. Run side by side, two runs once corrupted
  it and lost updates. The fix makes `classm.py` write it under the jobs lock with an atomic replace, and building the
  jobs on the merged expansion tree needed a 16 GB Node heap (`JOBS_HEAP_MB`). Both are in `classm.py` from the
  coverage expansion commit on; on an older tree, run class M jobs that write one file in series.
- **Green records are per exact tree, not per parent.** A dependent batch's full check can run in parallel with its
  predecessor's; the commits are then made in order.
- **Rebasing a batch.** A rebased batch takes `main`'s copies of shared generated and tool files (`engine/src/mutate.ts`,
  `fixtures/<year>/mutation.json`) as its base and re-applies its own changes by id (case id, argument key). Taking
  the batch's own stale copy silently reverts repairs made on `main` since.

---

## 9. Bookkeeping

9.1 **Defects.**
- A lane records each defect with `python3 tools/new_bug.py "Title" --pending --field ...` and cites it as
  `BUG-NEW-<round>-<lane>-NN`.
- A committed pending file is never changed on the branch. A correction is a new pending entry that cites it.
  Filling in Fix fields later fails `check_bug_inventory.py` (`land3-fix.md`, `land3-holes.md`).
- Ids are given at the batch merge (8.5, step 3).

9.2 **Tasks.** The coordinator owns `TASKS.md`, through `tools/task_row.py`. There is one row per area. Rows are also
written for review debt and for lows waiting on the form's next change. Lane requests become rows only in the
bookkeeping commit.

9.3 **Coverage documents.** These are written by the integrator, or in the bookkeeping commit, after a batch:
- `tools/coverage/categories.json`:
  - remove the retired gates from each category's `gates`;
  - set `refused: false` on a category the area covers whole;
  - keep the gates of residual refusals;
  - `estimate.py` exits when the file names a gate that is not in the forms.
- Regenerate `docs/COVERAGE.md` and the README coverage table with `python3 tools/coverage/tree.py`.
- `interview/<year>/gate_frequencies.yaml` gets entries for new gates the interview places by frequency
  (`gate_frequencies.py --check`).
- **Estimate refresh.** Run it in the main checkout, which holds `.engines/` and the microdata:
  `.engines/venv/bin/python -I tools/coverage/estimate.py`, then `python3 tools/coverage/roadmap.py`. Commit
  `reports/<year>/filer_coverage.{md,json}`. Run it once per release, and before intake (1.1).
  - **[unverified]** It was not run here; this worktree has no `.engines/`.
- Spec 2.4 "Done so far" and the 2.2 refusal list are updated when the area is covered (6.5), at the release.
- If the round changed a regime, the changes are noted in `docs/TRUST.md`.

9.4 **Next year.** Update the `changes/<N+1>/README.md` table and the change map rows (7.1). Update
`docs/ty2026/ADOPTION.md` (or the next year's equivalent) if the area adds a table, an extractor or a document to
the adoption steps.

9.5 **Ledgers.**
- Each agent run is a row in `research/costs/agent_runs.jsonl`, with `model`, `class`, `year` and `jurisdiction`.
  The hook writes it; `check_agent_runs.py` checks it.
- Each paid call is a row in `.transcription/costs.jsonl`. The round plan's last section records spend by kind.

---

## 10. Definition of done

10.1 **One expansion (an area) is done when:**
1. Every lane of the area is merged to `main` in a batch with a green full-tier run (8.5).
2. Every gate in the plan row is removed or narrowed as planned. The residual refusals are cited, placed in
   `tree.json`, and walked by coverage rows.
3. The construction protocol's checklist is done. The walks for the typical filer, the filer with nothing and the
   refused filer are recorded before and after.
4. Its fixtures meet section 5: predicted, branch-covering, with mutation explained and the engine differential
   mapped or its gap stated.
5. Its reviews meet 6.5, items 2 to 4.
6. Its next-year work meets 7.1 or 7.2: operations checked, documents listed.
7. Its bookkeeping is done (section 9). The coverage documents are regenerated and the task row is updated.
8. Its lanes' worktrees are removed, or archived with `tools/worktree_gc.py archive`, once their work and review
   data are carried back (owner, 2026-11-21); a worktree kept for later work is locked with a reason starting
   "keep". A release fails while a removable or stale worktree remains (`tools/worktree_gc.py check --fail`).

10.2 **A release that claims new coverage** (`tools/release.sh`, on the clean tip of `main`):
1. Full tier is green, and the tag `r<YYYY>.<MM>.<DD>.<n>` is on the tested commit.
2. `tools/release_reviews.sh` passes: no completeness, screen or false-no subject is due, or short of its sample.
   Question reviews join this gate once their first full pass is ruled (owner decision 2026-11-10).
3. No source backing a covered area is a draft (spec 7). An area resting on drafts is held out of the claim.
4. The estimate is refreshed and committed. The README table, `docs/COVERAGE.md`, spec 2.2 and spec 2.4 state the new
   figure and its limits.
5. The handoff entry reports the gain, the spend, the open lows, and what is inferred rather than run.
