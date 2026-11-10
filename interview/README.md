# The interview

The interview is a client of the evaluator (`engine/src/interview.ts`): the inputs the
evaluator finds unknown and reachable on the way to a profile's targets are the questions;
authored data (`2025/questions.yaml`) supplies their wording and order; an append-only log
supplies the answers. All amounts are integer cents. No data is transmitted.

With dependencies and Lean installed, rebuild and check offline with `npm run check-all`.

## Profiles

A profile file lists its targets, its initial answers and the inputs it asks; the build
(`engine/src/build.ts`) reads the four below and writes each to `canonical/`.

| Profile | File | Targets | Scope reported by the CLI |
|---|---|---|---|
| default (`social-security`) | `2025/social-security.yaml` | Form 1040 line 31 | Social Security credit and supplied Schedule 3 Part II subtotals; not a complete return |
| `sales` | `2025/sales.yaml` | Form 1040 lines 7a and 16 | securities sales, Schedule D and tax-method selection; AGI and taxable income computed; not a complete return |
| `stage4` | `2025/stage4.yaml` | `scope.ready`, lines 7a and 16, the Schedule A deduction, Form 4952 line 8, the QBI deduction, Schedule 2 line 21, Form 8959 line 24, Schedule 3 line 1 | form slices with eligibility and valuation screens; not a complete return |
| `full` | `2025/full.yaml` | `scope.ready`, Form 1040 lines 24, 33, 34 and 37, `f2441.line1_box`, `f2441.line1_paid`, `f2441.statement_notice`, `f2441.household_notice`, `f5695.line32b`, `ira.basis_total` | the whole return: Form 1040 lines 1a–37 end to end for single, head of household, qualifying surviving spouse and married filing jointly returns, with cited refusals for unsupported items (married filing separately among them); no filing or transmission |

The default, `sales` and `stage4` profiles fix the person roster to `taxpayer` in their
initial answers. The `full` profile starts from no answers and asks `$person` first:
`["taxpayer"]`, or `["taxpayer","spouse"]` on a joint return. It asks every question in
the bank (`questions: all`).

## CLI

Start a local answer log (the file must not already exist; it is created mode 0600):

```sh
node engine/dist/main.js interview start --log /tmp/synthetic-return.jsonl --profile full
node engine/dist/main.js interview answer --log /tmp/synthetic-return.jsonl --input '$person' --value '["taxpayer"]'
node engine/dist/main.js interview advance --log /tmp/synthetic-return.jsonl
```

Without `--profile`, `start` uses the default profile. The log's first line pins the
profile and tax year; `advance` and `answer` read them from it, and a `--profile` that
differs from the log's is an error. A log is pinned to 2025 and is not usable as another
tax year. Every command takes `--year N` (default: the newest year in `years.json`).

Each response is JSON with `status` (`incomplete`, `complete` or `refused`), the next
`question` (its `input`, `prompt`, `help`, `order` and `cite`, `helpRequested`, `entry`, a
hint for typing the answer as `--value` JSON from the input's type, and `choices` for a
roster with a fixed set of answers, such as `$person`), the
`pending` questions (every question still reachable, in asking order, in the same form),
the `refusal` if any, `reachableInputs`, the profile's `scope` sentence, the standing
`notices`, the `values` with derivations, and a text `sheet`. `question` is null once the
return is complete or refused; `pending` continues after a refusal, because on an
incomplete return a later answer may clear it. A refusal is final only when nothing is
pending.

Answer using the question's exact `input` key. `--value` is JSON: `false`, `620000`,
`"single"`, `null` or `["employer_a","employer_b"]`. `null` requests help: the value
stays unknown and the same question is asked again with `helpRequested` set. A blank
printed money box must be entered as zero if that is the intended answer; unanswered
questions never default to zero. Questions are asked in bank order, then by key.

## Web UI

`serve` runs a local, single-user page (`ui/`) over the `ny` profile (the federal questions,
then the New York ones). The current question is the centre of the page: its full text (long
text is broken into paragraphs at sentence ends, never shortened), the answer widget, then the
explanation (a very long explanation shows its opening and a control for the rest), then the
forms the question's prompt and help name ("Forms mentioned"): each one's designation and printed
title, and, where its catalog entry has a `form_purpose`, the official statement of what the form is
for, quoted with its document and page (`check_source_titles.py` checks it on that page); more than
two forms are folded to one line each. The server finds them in the question's wording by the
catalogs' designations ("Form 8814", "Forms 1099-INT and 1099-OID", "Schedule J", "Schedules C and E
(Form 1040)"; a schedule named without its parent form resolves when the catalogs hold exactly one
schedule of that number) and sends only the forms the catalogs hold (`engine/src/form-refs.ts`). Beside it,
or below the explanation on a narrow window, is its source: the cited document's designation
and printed title, as "Form 1040 — U.S. Individual Income Tax Return" (the `designation`, the form,
schedule or publication number as the document prints it, and the `title` of its entry in
`tools/sources/<year>.json` or `tools/sources/ny/<year>.json`, which `tools/check_source_titles.py`
checks against the archived document; a document with no printed designation, such as a statute or
a statistics table, shows its title alone, and one whose title already contains its designation
shows the title once), every reference of
the citation's locator with the quoted words set apart, and the document's id and revision. A
status line under the tabs shows the return's progress, or its refusal, labelled provisional
while questions are pending and final once none are, with the refusal's form, remedy, trigger
and source in a dialog. A refusal whose gate is a consistency check (`2025/conflict_checks.yaml`:
answers that contradict each other or are impossible, such as more family months than eligible
months) is shown instead as conflicting answers, neither unsupported nor provisional: the
check's explanation and the answers it reads, each a link that reopens its question, above the
current question. Everything else is one tab away: the answered questions (choosing one
reopens it for correction); "Your return so far", the federal and New York values sheets (the
return first, then its schedules, the other forms, and worksheets and helper sections last;
the order is the page's, the text sheet keeps the engine's), where the lines the last answer
changed are highlighted and a line opens its derivation beside the sheet (operation,
citation, the lines it uses, the answers it depends on, which reopen their questions,
conditions not taken and notes); and the scope and standing notices, whose one-sentence
summary stays in the footer:

```sh
node engine/dist/main.js serve --dir /path/to/returns [--port 8791]
```

`--dir` is required and names the directory of answer logs, one `<name>.jsonl` per return,
in the format above (the CLI reads and answers the same logs). The server refuses a
directory that is missing, inside the repository (resolved through symlinks) or readable by
group or others; it creates logs mode 0600 and never overwrites one. It listens on
127.0.0.1 only and refuses requests whose `Host` is not `127.0.0.1:<port>` or
`localhost:<port>`, and POSTs whose `Origin` is not that same origin. Answers go through the
same validation as `interview answer` (`applyAnswer` in `interview.ts`); a rejected answer
is a 400 and nothing is written. The page sends money as integer cents and never sends a
blank amount as zero. Yes/no questions, enums and rosters with `choices` are selectors. An
open roster is entered as a list of labels the user types ("Acme Corp"); the page derives
each new entry's key from its label (lowercase, other characters to `_`, a numeric suffix
when the key is taken), an edited label keeps its entry's key, and the page shows labels,
not keys. The labels are saved on the roster answer's event as `labels`, a map from entry
key to label, which replay ignores. Its API:

| Route | Does |
|---|---|
| `GET /api/returns` | the return logs in the directory, the scope sentence, the notices, `docTitles` (document id to printed title) and `docDesignations` (document id to printed designation, for the documents that have one), both from the year's source catalogs |
| `POST /api/returns` `{name}` | starts a log (profile `ny`); an existing name is refused |
| `GET /api/returns/:name` | the state: the CLI's fields, `pending` with each input's `type` (and enum `values`) and `forms` (the catalogued forms its question names: `designation`, `id`, `title`, `purpose`), `refusalFinal`, the structured `sheets` (federal and New York), the `answered` questions, the `entryLabels` (entry path to label) and the lines the last answer `changed` |
| `POST /api/returns/:name/answer` `{input, value[, labels]}` | appends the answer and returns the new state, or 400 with the reason |

`test-serve` (in `check-all`) tests the server on synthetic returns in temporary
directories; `ui/test_browser.mjs` is a smoke test of the page in a separately launched
headless Chrome, run by hand.

## The answer log

The log is append-only JSON lines: a header, then one `{input, value}` event per answer.
Replaying it starts from the profile's initial answers and applies the events in order;
an event on an initial key is invalid. A correction is another event for the same input;
`answer` accepts an input only if it is currently reachable or already answered. Before
an event is appended the candidate inputs are validated and the state is computed, so a
malformed or unreachable answer is a command failure and is not written.

Keyed collections are entered through roster questions: `$w2@person[taxpayer]` lists an
employer roster, `$sales` the transactions, `$interest` the payers, `$gift` the noncash
gift groups. An entry's amounts use keys such as `person[taxpayer].w2[employer_a].box4`.
Removing an entry from its roster makes that entry's answers inactive while they stay in
the log; re-adding the same key reactivates them. A roster's keys stand for distinct
things (for `$w2`, distinct employers, not W-2 sheets: the excess Social Security credit
turns on the number of employers); the tool rejects duplicate keys but cannot tell two
labels a person gives the same employer. A collection declared `implicit` has one entry
and no roster question.

## Refusal as a result

A refusal is a result, not a command failure: a `refused` response names the gate, the
form the tool cannot prepare and the remedy, with a source citation. The targets that
depend on it are refused; independent values remain inspectable in `values`.

## Direct evaluation

Supply a JSON object of the same input keys (including the rosters) to `eval`:

```sh
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --target f1040.line37
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --json
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --html
node engine/dist/main.js eval --batch /tmp/cases.json
```

Without `--target` every line of every top-level form (not a collection entry) is a
target; `--batch` takes `[{id, inputs}]` and emits one result per case. Use synthetic data for development; never commit personal return
inputs or logs. Synthetic values sheets are under `reports/2025/`.

## Collection model

A form's `collection` metadata declares a keyed collection, optionally with a `parent`
collection or an `implicit` single entry, and carries its citation. A `sum_over` names
the `collection`, an entry-local `field` and an optional `where` test. A nested
collection's roster is keyed under the current parent instance. All cross-entry
aggregation is explicit.

A roster not yet given is unknown; a confirmed empty roster sums to zero. A refusal in
any entry refuses the sum. An unknown entry value, or an unknown `where` test, makes
the sum unknown; when the field is a count, the sum of the entries already known is
kept as a lower bound, so a `count > 0` gate can refuse early. Non-negativity and
monotonicity of the aggregation have Lean lemmas (`sumOver_nonneg`, `sumOver_mono` in
`lean/TaxFormalization/Lemmas.lean`); the handling of unknown values is compared between
the two evaluators and exercised through the CLI.

## Checks

At build (`engine/src/interview-check.ts`): for the default profile, every finite
(Boolean or enumerated) answer of every question asked is enumerated over the
`fixtures/2025/stage2.json` cases, checking termination, that each question is a
reachable input with a fixture representative and is never repeated, and that the
reversed answer order gives the same values and status. For `sales`, `stage4` and
`full`, each case of `stage3.json`, `stage4.json` and `stage5.json` respectively is
walked once with the fixture's answers, checking termination and order invariance;
that is representative coverage, not an exhaustive proof. The build also fails when a
reachable input has no question in the bank, when a profile asks the roster of an
implicit collection, and when a line nothing reads is neither a target nor marked
`display`.

The CLI tests (`engine/src/integration.ts`, `test-integration` in `check-all`) cover
help requests, corrections, early refusals, invalid inputs, the refusal to overwrite a
log and the profile-mismatch error.

## Question data

Every profile asks its questions from one bank, `2025/questions.yaml`: each entry gives
an input's `order` and `help`. Its prompt is filled at build from the form line's
question text, after its collection's frame (for example "For this business — "), and
its citation from the line (a roster question's from its collection). An entry states a
`prompt` or `cite` only for interview wording the line does not carry; the build fails
if it repeats the line's. `help` is optional. A roster with a fixed set of answers lists
them as `choices` (a label, the entry keys and a label for each key), which the page shows
as a selector. An enum input may give `value_labels`, a label for each value of its enum
(presentation only: the answer is still the value). The build requires exactly one
distinct label per value; the page's selector, its answered list and the CLI's entry hint
show the labels.

A long question is written as structured text (`engine/src/text.ts`): a line's `label`, an input's
`source`, a `note`, and a bank `prompt` or `help` may hold line breaks, and then only a small Markdown
subset, which the build checks. The first line is the question; then one-line paragraphs separated by
blank lines, a heading (a short line ending in ":") directly above a list, `- ` bullets and `  - ` nested
bullets (one level). Text without a line break is plain text, shown unchanged everywhere. The authored text
is canonical and already reads as plain text: the CLI's JSON carries it as it is, the values sheet,
`rendered/` and the review prompts indent its continuation lines, a reference to a structured label names
its first line, and the page renders the blocks as HTML.

Wording says what to answer, not how to type it: the build fails when a filled prompt or
help states entry syntax (`entrySyntax` in `interview.ts`: cents, integer, whole number,
true or false, JSON, null, a list literal such as `[]`, entry keys). Each client states
entry syntax itself, the CLI in the question's `entry` hint and the page in its widgets.
