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
initial answers. The `full` profile starts from no answers and asks `$person` first
("Who is this tax return for?"): `["taxpayer"]`, or `["taxpayer","spouse"]` for a couple
filing together. That answer also records each entry's role and, for the couple, the
filing status ("Answers a choice records"), so a couple is asked nothing more to open the
return and one person is asked the filing status next. It asks every question in the bank
(`questions: all`).

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
hint for typing the answer as `--value` JSON from the input's type, `choices` for a
roster with a fixed set of answers, such as `$person`, and, where they apply, `frame`,
the per-person frame its prompt begins with, and `withheld`, the values not offered), the
`pending` questions (every question still reachable, in asking order, in the same form),
the `refusal` if any with its `refusalNote` ("Refusal as a result"), `reachableInputs`, the
`recorded` answers (each answer a roster choice recorded: its `input`, `value`, the
question it was recorded `by` and the sentence `shown` for it), the profile's `scope`
sentence, the standing
`notices`, the `values` with derivations, and a text `sheet`. A question's `prompt` and
`help` are as shown to the filer: the spouse phrase is reworded for the filing status
answered, and the per-person frame for the entry's role ("The spouse phrase as shown" and
"The per-person frame as shown", under Question data). `question` is null once the
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
current question. A refusal that has a note (`2025/refusal_notes.yaml`) shows it above the
current question and in the refusal's details. A question asked of a person on the return
begins "About you" or "About your spouse" when the return has two people, and has no frame
when it has one; the line above the question then names only the entries beneath the person
(an employer, an account). Everything else is one tab away: the answered questions (choosing one
reopens it for correction; under the answer to "Who is this tax return for?" the list shows
what that answer recorded, each with its id, to be changed by changing that answer); "Your return so far", the federal and New York values sheets (the
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
blank amount as zero. Yes/no questions, enums and rosters with `choices` are selectors: a
labelled enum (`value_labels`) is a list of its labels, one to a line in the bank's order
without the withheld values, and choosing one answers. An
open roster is entered as a list of labels the user types ("Acme Corp"); the page derives
each new entry's key from its label (lowercase, other characters to `_`, a numeric suffix
when the key is taken), an edited label keeps its entry's key, and the page shows labels,
not keys, except in a question's id. The labels are saved on the roster answer's event as
`labels`, a map from entry key to label, which replay ignores.

Every question shows its id, the input key the engine and the answer log know it by: under
the current question's text (with a control that copies it), and under each question of the
answered list, of a conflict's answers and of a derivation's "Answers it depends on". A
question asked per entry shows its key with the entry keys (`person[taxpayer].role`,
`person[taxpayer].w2[acme_corp].box1`). The id is small, in the monospace face, and one
click selects the whole of it. It is a separate element after the question's words, outside
the question's heading and outside any button, so a screen reader reads the question first
and then "Question id: …".

Its API:

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

### Answers a choice records

The interview sets no input, with one declared exception: the choice a filer makes on a
roster question with fixed `choices` may record answers that its label already states. The
bank declares them beside the choice, as `records` (each an `input`, a `value` and the
sentence `shown` to the filer for it). The person roster's choices record each entry's
role (`person[taxpayer].role`, `person[spouse].role`), and "Me and my husband or wife,
together on one return" also records `f1040.status` as married filing jointly. The limits,
checked at build and by `interview-rules`:

- a choice records only inputs of the entries it creates, or an input on the allow-list
  `RECORD_ALLOWED` (`interview.ts`), which holds one input: `f1040.status`, with the value
  `mfj`, for the couple's choice of `$person`. Nothing else is set by the interview;
- each recorded value is one the input can take, each input is recorded once, and a gated
  input is never recorded;
- an entry input one choice records is recorded by every choice for every entry it
  creates, so that input (`person.role`) is never asked and has no question in the bank.
  It stays an input of the model: `eval` and the fixtures state it directly.

One function, `answerEvent` (`interview.ts`), turns an answer into its event, and every
client answers through it: the CLI and the server (`applyAnswer`) and the walks of the
fixtures, the generated returns and the tests (`interview-rules.ts`,
`interview-check.ts`). It accepts only a declared choice as the answer to a roster
question with choices (in any key order), attaches that choice's records, and refuses a
direct answer to an input a choice recorded: that answer is changed by changing the choice.

The records are saved on the roster answer's event (`{input, value, labels, records}`), and
replay applies them from the event, so a log gives the same state whatever the bank says
later. An answer to a roster question first withdraws what that question's earlier answer
recorded and then applies its own records. So when the choice is changed:

- from the couple to one person, the recorded filing status is withdrawn and the status is
  asked; the spouse's entry and its answers become inactive, as for any removed entry;
- from one person to the couple, married filing jointly is recorded over the status that
  was answered alone; going back to one person withdraws it again, and the status is asked
  again (the earlier answer is not brought back);
- a help request on the roster question withdraws its records with its answer.

A filer who chose the couple therefore cannot end with another filing status: the status
is not asked, cannot be answered directly, and is replaced only with the choice. A log
answered when the roster, the status and each role were separate questions carries them
as ordinary answers and replays to the same state; if such a log stops before a role was
answered, the interview asks the roster question again, whose answer records it.

A fixture or generated return walked through the interview must state what its roster
answer records (the same roles, and married filing jointly for two people): one that
states otherwise is a return only typed-in inputs can make, and its walk fails saying so.

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

The interview may add to a refusal what the filer can do next, in plain words:
`2025/refusal_notes.yaml` maps a refusal gate to a note, which the response carries as
`refusalNote` and the page shows above the question and in the refusal's details. Married
filing separately, and a head of household or qualifying surviving spouse choice whose
tests are not met, have one (go back and choose "together", or another line). A note is
presentation only: the refusal, its remedy and its citation are the form data's. The
build checks each key is a refusal gate that is not a consistency check.

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

## Coverage rows

`2025/coverage/` lists the situations the interview is known to handle, one file per part of
the interview (`opening.yaml`, `credits.yaml`, `hsa.yaml`). A row names a situation as the
answers a filer in it gives and the end the interview must come to, and `interview-coverage`
(`engine/src/interview-coverage.ts`, in `check-all`) walks the built interview with those
answers, in the interview's own order, and fails naming the row when the tree does not end
there. No model is called. `reports/2025/interview_coverage.md` lists every row with its
situation, its end in the interview's own words and its path, and the background return;
`interview-coverage --write` writes it and the check fails when it is not current (it
quotes question and refusal wording, so it is rewritten after a wording change).

```yaml
tax_year: 2025
part: The opening                 # the report's heading
profile: full                     # full or ny; a row may give its own
sets:                             # optional: named answers several rows share
  one_person:
    says: One person on the return, who takes the filing status single.
    answers:
      f1040.status: single
rows:
  - id: opening.single_but_married
    design: C.1 row 9 (married, picks "None of these")
    situation: A married person files alone and takes the status of an unmarried person.
    uses: [one_person]
    answers:
      household.married: true
    expect:
      refused: household.filing_status_conflict
```

A row has an `id` (lower case, no tax year, unique across the files), the `design` row it
comes from, the `situation` in one plain sentence, its `answers` and one expected end.
Answers are keyed by the question's exact id, as the answer log has it and the page shows
it (`person[taxpayer].age65`, `$f8889@person[taxpayer]`), with the log's values. A row
written against the interview as it stands before a redesigned part lands says so in
`replace_when`, and the report marks it. The schema is `coverageFile` in
`schema/data.schema.json`.

| `expect` | The row passes when | The walk stops |
|---|---|---|
| `asks: <question>` | that question is the interview's next question | there |
| `refused: <gate>` | the return is refused at that gate (the refusal's `gate`), on an answer the row gave | at the first refusal |
| `records: {<input>: <value>}` | once the row's own answers are given, each input holds the value without having been asked (an answer a choice records) | when the row's own answers are given |
| `proceeds: {<input>: <value>}` | the return is completed and each input holds the value, given by the row or recorded | at completion |
| `not_asked: [<question>]`, beside one of the above | none of them was asked before the walk stopped | |

The walk reads each next question from `interviewView` and answers through `applyAnswer`,
as the page and the CLI do, so an answer the interview would reject is rejected and what
an answer records is recorded. It ends where a filer's does: at the first refusal (the
interview then asks nothing more; a refusal met while questions are pending is the one the
filer is shown first) or at completion.

A question the row does not answer is answered by the background return: the minimal
return of `interview-rules` (every question answered no, zero, none or the first option;
the other option where that one refuses), walked once per profile. The rules are strict:

- The background answers only the kinds of question it is itself asked (the same input
  template, for any person or entry). A question the row's answers opened, which a filer
  with nothing to report never meets, must be answered by the row; otherwise the row fails,
  and the failure names the answer that opened the question. A question added beneath an
  existing one therefore fails the rows whose path passes it until each says what its
  filer answers.
- The background never brings about a row's end. A refusal met on a background answer
  fails the row, as does an expected value the background supplied. Where a refusal waits
  on an answer the row would otherwise leave to the background, the row states that answer.
- An answer of a set counts as the row's own, and a row's own answer replaces a set's.
- Every answer of a row must be asked before its walk stops, and every answer of a set in
  the walk of at least one row that uses it: an answer never asked is a stale row. An id
  that names no question, input, gate or set fails without a walk.

The check tests the structure, given the answers: that a filer who answers so is led where
the row says. Whether a filer in the situation would give those answers is a matter of the
questions' wording, which it does not judge. A row cannot name a refusal's wording, a
computed line's value, "either of two gates" (one row per path), or a state only typed-in
inputs produce.

`interview-coverage --rows FILE` checks other row files in place of the year's (the report
is then neither checked nor written). `interview-coverage --self-test` (in `check-all`)
plants each kind of failure on the built interview: a wrong end, an unanswered question, a
stale answer, an id that does not exist, an end the background brings about, a rejected
answer, recorded answers, and a file's repeated id, unused set and stale set answer.

## Question data

Every profile asks its questions from one bank, `2025/questions.yaml`: each entry gives
an input's `order` and `help`. Its prompt is filled at build from the form line's
question text, after its collection's frame (for example "For this business — "), and
its citation from the line (a roster question's from its collection). An entry states a
`prompt` or `cite` only for interview wording the line does not carry; the build fails
if it repeats the line's. `help` is optional. A roster with a fixed set of answers lists
them as `choices` (a label, the entry keys, a label for each key and, optionally, the
answers the choice `records`; "Answers a choice records"), which the page shows
as a selector. An enum input may give `value_labels`, a label for each value of its enum
(presentation only: the answer is still the value). The build requires exactly one
distinct label per value; the page's selector, its answered list and the CLI's entry hint
show the labels, in the order the bank lists them (`value_order` in the built question).

A value is not offered (`withheld` on the question as shown; `withheldValues`) when a choice
of an answered roster question records it and the filer answered that question with another
choice: married filing jointly is what the couple's choice records, so a filer who answered
"Just me" is offered the four other filing statuses. This too is presentation only: the
value given now is always offered, and an answer is accepted whether or not it was offered
(one person answering married filing jointly meets the consistency check
`household.roster_bad`, as a typed-in return does).

The Form 8863 Part III questions exist twice, as `person.edu*` and `dependent.edu*` lines with a bank entry
each, because a student is a person on the return or a dependent. The two statements are kept the same:
a change to the wording, help, order or citation of one is made to its twin in the same commit, by a lane
that has claimed both `person` and `dependent`, and `tools/check_twins.py` (check-all) fails on any
difference not declared with its reason in `reviews/2025/twins.json`. `check_twins.py --sync-from person`
shows the copy and `--write` makes it (tools/README.md, "Twin lines").

A long question is written as structured text (`engine/src/text.ts`): a line's `label`, an input's
`source`, a `note`, and a bank `prompt` or `help` may hold line breaks, and then only a small Markdown
subset, which the build checks. The first line is the question; then one-line paragraphs separated by
blank lines, a heading (a short line ending in ":") directly above a list, `- ` bullets and `  - ` nested
bullets (one level). Text without a line break is plain text, shown unchanged everywhere. The authored text
is canonical and already reads as plain text: the CLI's JSON carries it as it is (but for the spouse
phrase, reworded as shown; see "The spouse phrase as shown"), the values sheet,
`rendered/` and the review prompts indent its continuation lines, a reference to a structured label names
its first line, and the page renders the blocks as HTML.

Wording says what to answer, not how to type it: the build fails when a filled prompt or
help states entry syntax (`entrySyntax` in `interview.ts`: cents, integer, whole number,
true or false, JSON, null, a list literal such as `[]`, entry keys). Each client states
entry syntax itself, the CLI in the question's `entry` hint and the page in its widgets.

A joint return combines both spouses' items, and a filer reading a bare "you" answers for
themselves only. So an amount or yes/no question asked once per return (its form has no
`collection` block), whose "you" would lead a joint filer to leave out the spouse's item
when that item counts on a joint return, names the spouse. Spouse wording that is added or
changed uses exactly one phrase, "(or, on a joint return, your spouse)", or its possessive
form, "your (or, on a joint return, your spouse's)", in lower case and not split by other
words. The stored wording does not vary with filing status, and the conditional form stays
true for a filer who is not filing jointly; the phrase is reworded for the filer's own return
only when a question is shown (next section). Spouse wording in another form that is
already correct stays as it is until the question is next changed.
The rule does not apply to a question asked per person, per dependent or per roster entry; a
question reached only by filers who are not filing jointly; a question about the return or
the household itself; or a question where naming the spouse would change what the form line
means (a line the form asks about the taxpayer only). Each use is grounded in the source the
question cites: the spouse's item counts on the joint return.

### The spouse phrase as shown

A filer reads the phrase in the form that fits their return. When a question is handed to a
client its prompt and help are reworded from the return's filing-status answer
(`f1040.status`) at that moment (`engine/src/spouse-wording.ts`, one function,
`spouseWording`):

| Filing status answered | "you (or, on a joint return, your spouse)" | "your (or, on a joint return, your spouse's)" |
|---|---|---|
| married filing jointly | "you or your spouse" | "your or your spouse's" |
| single, head of household, qualifying surviving spouse, married filing separately | "you" | "your" |
| not yet answered (or help requested on it) | as stored | as stored |

Married filing separately is read as no spouse on the return: the spouse's items are not on a
separate return (and the tool refuses that status). The replacement is exact, on the built
text: the phrase with the space before it, and the possessive form with its "your". Every
occurrence in a text is reworded. No other spouse wording is touched: "(and, on a joint return,
your spouse)", "(or your spouse, if filing jointly)" and "you or your spouse" are shown as
stored. The per-person frame has its own rule ("The per-person frame as shown").

Where it applies: `interviewView` (`interview.ts`) rewords the next `question` and every
`pending` question, so the CLI's JSON and the server's state carry the text as shown, and the
server (`serve.ts`) rewords the `answered` questions (and through them a conflict's
`answers`) the same way. The page has no rewording of its own. Each response is reworded
from the answers it is computed from and nothing reworded is saved (the log holds inputs and
values only), so a corrected filing status changes every list on the next response.

Where it does not apply: the stored text. `canonical/`, `rendered/`, the review prompts, the
fixtures and the question bank carry the conditional phrase, so the reviews, which are keyed
to the built text, are unaffected by how a question is shown. The forms a question names are
found in its stored wording.

A form line's `label` that carries the phrase is reworded the same way where the interview
shows it: on the values sheet of `interviewView` (the page's "Your return so far" and a
line's derivation, and the CLI interview's text `sheet`) and in a conflict's `figures`
(`shownSheet`; `serve.ts`). `valuesSheet` itself (`output.ts`) is not reworded, so `eval`
and the values sheets under `reports/` print the stored labels. A label with a near-miss of
the phrase fails the build, naming the line.

Because only the two exact forms are reworded, a prompt or help that holds a near-miss of the
phrase fails the build, naming the question (`spousePhraseNearMisses`): the words "or, on a
joint return, your spouse" in that order with other capitalisation, punctuation or spacing, a
curly apostrophe, another or no preposition or article before "joint return", no space before
the parenthesis, or a possessive without its "your". Spouse wording in another word order
("or your spouse, on a joint return") is not a near-miss; it is shown as stored.
`spouse-wording --self-test` (in `check-all`) tests the rewording, the status reading (every
value of the `filing_status` enum is read as joint or not) and the near-miss rule on
constructed texts, and that every built question parses as structured text in both readings;
`test-serve` tests one return read three ways as the filing status goes from unanswered to
married filing jointly to single.

### The per-person frame as shown

Every question asked of a person on the return is stored with one frame, "For this person
(you, or your spouse on a joint return) — " (the bank's `person` and `f8889` frames, and the
rosters listed under a person; the build fails if the `person` frame is any other text). A
filer reads it in the form that fits the entry (`shownFor` in `spouse-wording.ts`), from the
entry's role (`person[…].role`, which the first question's choice records) and the number of
people on the return, not from the entry's key or the filing status alone:

| The entry's role | Two people on the return | One person on the return |
|---|---|---|
| taxpayer | "About you — " | no frame; the question's first letter is a capital |
| spouse | "About your spouse — " | "About your spouse — " |
| not answered | as stored | as stored |

The question as shown carries the frame it begins with as `frame` ("About you", "About your
spouse"), so a client that prints its own heading for the entry does not say it twice. The
rule applies wherever the spouse phrase's does (the next `question`, the `pending` and the
`answered` questions) and nowhere in the stored text. `spouse-wording --self-test` tests the
frames on constructed returns and that every built framed question parses as structured
text in each shown form; `test-integration` and `test-serve` test them on a couple's return
and on one person's.

### The person a question is about, as shown

A framed question is stored in the second person: "you" and "your" are the person whose entry
it is, "your spouse" is that person's husband or wife, and "this person" is that person again.
Shown for the spouse's entry, the person is named ("About your spouse — Was your spouse born
before January 2, 1961?"); shown for the taxpayer's entry, only "this person" changes, to "you"
(`personWording` in `spouse-wording.ts`, applied by `shownFor` to the prompt and the help after
the spouse phrase):

| Stored | For the taxpayer's entry | For the spouse's entry |
|---|---|---|
| "you" as a subject | as stored | "your spouse", the verb after it agreeing ("you have" to "your spouse has") |
| "Were you", "Do you", "Have you", "Are you" | as stored | "Was your spouse", "Does your spouse", "Has your spouse", "Is your spouse" |
| "you" as an object ("paid to you") | as stored | "your spouse" |
| "your", "yours" | as stored | "your spouse's" |
| "yourself" | as stored | "himself or herself" |
| "this person", "this person's", "you (this person)" | "you" (the verb agreeing), "your", "you" | "your spouse", "your spouse's", "your spouse" |
| "your spouse", "your spouse's" | as stored | "you" (the verb agreeing); "your" before a noun, "yours" otherwise |
| a phrase that means both people ("you and your spouse", "you or your spouse", "you both", "either of you", "both of you") | as stored | as stored |

So in a framed question "you" never means the couple: the couple is written with one of the
phrases of `COUPLE_PHRASES`. The rule works from closed lists in `spouse-wording.ts`: the verbs
that change with their subject (`SECOND_TO_THIRD`, `THIRD_TO_SECOND`) and the words that may
follow a subject or an object unchanged (`UNCHANGED_AFTER`). The build fails, naming the
question and the words, on a framed prompt or help the rule does not cover: a subject before a
word in neither list ("you swim"), a contraction ("you're"), or a verb the lists change standing
after a preposition's object ("of this person reports"), where the rule cannot tell whose verb
it is. Such a question is reworded, or its word is added to a list.

The reviews read the stored text, so the shown text has a record of its own:
`reports/2025/person_wording.md` lists every framed question as stored and in each shown form
(a one-person return, the taxpayer's entry of a couple's return, the spouse's entry), prompt
and help. `node engine/dist/main.js spouse-wording --report` writes it, and check-all fails
when it is not current (`--report --check`), so a change to the rule or to a stored question
is a difference a person reads. The rule cannot check meaning: a new or changed framed
question's shown forms are read in that report before it is committed.

## The words a filer reads

`node engine/dist/main.js interview-words [--write]` (`engine/src/interview-words.ts`; free and deterministic, no
model call) measures the reading the interview asks of a filer. Each return is walked as the page walks it, to
completion or refusal, and every question asked is counted as shown: the prompt reworded for the filing status
answered, once per time it is asked (a question asked per person or per entry counts per entry). The report,
`reports/2025/interview_words.md`, gives per group of returns the questions asked, the prompt words, the words of the
answers offered, the help words (help is shown and optional to read, so it is counted apart), the prompt words read
before the first question the filer answers with something of their own (an amount, a number or a list), the longest
prompts met, and the longest sentences of the question bank. A word is a run of characters holding a letter or a
digit, so list markers and dashes are not counted. The returns are those `interview-length` walks. It is a sibling of
that tool, not part of it: `interview-length` compares question counts under three orders and never builds a question
as shown; this one counts reading under the one order the interview has. Its `--self-test` runs in `check-all`.
