# The interview

The interview is a client of the evaluator (`engine/src/interview.ts`): the inputs the
evaluator finds unknown and reachable on the way to a profile's targets are the questions;
authored data (`2025/questions.yaml`) supplies their wording and order; an append-only log
supplies the answers. All amounts are integer cents. No data is transmitted.

With dependencies and Lean installed, rebuild and check offline with `npm run check-all`.

## Profiles

A profile file lists its targets, its initial answers and the inputs it asks; the build
(`engine/src/build.ts`) reads the profiles below and writes each to `canonical/`.

| Profile | File | Targets | Scope reported by the CLI |
|---|---|---|---|
| `full` | `2025/full.yaml` | `scope.ready`, Form 1040 lines 24, 33, 34 and 37, `f2441.line1_box`, `f2441.line1_paid`, `f2441.statement_notice`, `f2441.household_notice`, `f5695.line32b`, `ira.basis_total`, `clcw_next_year.line8`, `clcw_next_year.line13`, `clcw_next_year.decedent_notice`, `clcw.figures_notice`, `s179.line13`, Form 8889's three results (`s1.line13`, `s1.line8f`, `s2.line17c`), and `s1.line10`, `s1a.line7`, `s1a.line15`, `sa.line17` and `s2.other`, asked for directly so that their questions are open in their own topics | the whole return: Form 1040 lines 1a–37 end to end for single, head of household, qualifying surviving spouse and married filing jointly returns, with cited refusals for unsupported items (married filing separately among them); no filing or transmission |

The `full` profile starts from no answers and asks `$person` first
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

Without `--profile`, `start` uses the `full` profile. The log's first line pins the
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
questions never default to zero. Questions are asked in the order the bank states: by `order`, then by
`seq`, entry by entry, then by key ("Blocks", under Question data).

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
summary stays in the footer. A second page, `/vet`, is for vetting the questions
themselves ("Vetting the questions" below):

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

A few yes or no questions the bank puts in a tick-box group ("Tick-box groups" below) are shown
on one screen when the first of them is the next question: the group's heading as the question,
one box per member with its short label and its id, and two ways to answer. "None of these"
records No for every box; ticking boxes and choosing "Continue" records Yes for the ticked and
No for the others. One way is live at a time: "Continue" is disabled until a box is ticked, and
"None of these" while one is. Beside each box, "What this asks" opens the member's own question
in full, its explanation and its source, with "Answer this one on its own", which shows it as an
ordinary question (with "I don't know / need help"). The screen's answers are sent together and
saved together or not at all (`POST …/answers`). Afterwards nothing remembers the screen: the
answered list has each member as its own answer under its own question, choosing one reopens
that question alone, and a refusal a ticked member brings about is shown as that question's
refusal always is. A member answered earlier is not on the screen; when one member is left it is
asked as an ordinary question; a group asked of each person has a screen per person under the
per-person frame.

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
| `GET /api/returns/:name` | the state: the CLI's fields, `pending` with each input's `type` (and enum `values`) and `forms` (the catalogued forms its question names: `designation`, `id`, `title`, `purpose`), `group` (the tick-box screen the first pending question is shown in, or null: `id`, `heading` as shown, `frame`, and `members`, the questions shown as its boxes, each as a pending question is served, with its label `tick`), `refusalFinal`, the structured `sheets` (federal and New York), the `answered` questions, the `entryLabels` (entry path to label) and the lines the last answer `changed` |
| `POST /api/returns/:name/answer` `{input, value[, labels]}` | appends the answer and returns the new state, or 400 with the reason |
| `POST /api/returns/:name/answers` `{answers: [{input, value}, …]}` | the answers of the tick-box screen the state offers (`group`): exactly one for each box, each `true` or `false`. Appends one event per box, in the order given, in one write, and returns the new state; 400 with the reason, and nothing appended, when any is rejected |
| `GET /api/vetting` | the vetting page's cards, each with its record and whether it is stale, the records of questions no longer asked, the counts and the verdict file's path ("Vetting the questions") |
| `POST /api/vetting` `{id, digest[, verdict][, note]}` | saves a verdict (`up`, `down` or `none`) or a note on the question as shown and returns the record and the counts; 409 when `digest` is not the card's (the wording changed), 500 with the reason when the file could not be written |

`test-serve` (in `check-all`) tests the server on synthetic returns in temporary
directories; `ui/test_browser.mjs` is a smoke test of both pages in a separately launched
headless Chrome, run by hand.

### Vetting the questions

The same server has a second page, `/vet` (a link at the top of the interview page leads to
it, and one leads back): every question the `ny` profile can ask, one at a time, for the
owner to mark thumbs up or thumbs down, with a note. Start the server as above and open
`http://127.0.0.1:8791/vet`. The questions come in the interview's asking order (`askOrder`:
order number, `seq` within a block, then id) and are the questions
`reports/2025/interview_words.md` counts.

A card shows, apart from one another:

- **The question** as the interview page words it. The main text is what a one-person return
  is shown (`shownAt` in `engine/src/interview-words.ts`, which applies `shownFor`: the spouse
  phrase reworded, no per-person frame). Beneath it, smaller, are the wording on a joint return
  and, for a question asked of a person or beneath one, the wording for the spouse's entry,
  each only where it differs. The stored text, before it is reworded, is under "As stored in
  the question bank".
- **The help**, in full, with its other wordings where they differ.
- **The answer** it takes, in plain words: Yes or No; a dollar amount (zero or more, or one
  that may be negative); a whole number; one choice from a list, with the choices as labelled
  (a filing status a one-person return is not offered is marked); or a list the filer builds,
  with what an entry is (the title of the list's form).
- **Context**: the id, with a control that copies it; the form the input belongs to and its
  printed line; whether it is asked once per return, once per person or once per entry of a
  list (named by its list question); when it is asked, as far as the engine can say; and the
  words of the question and the help as shown (the words tool's `words`), with the longest
  sentence of the stored question (`longestSentence`; over 40 words is long, as the words
  report counts). A member of a tick-box group also has "Shown as": the group, the screen's
  heading and the label beside this question's box. A verdict's digest does not cover them.

"When" is one of a few fixed statements, each read off the engine and none of them a guess. A
question whose input has a gate (`gated_by`) says "asked only after an earlier answer" and
names the questions its gate is figured from, when they can be read off the gate's
expressions and are at most four; otherwise it says "asked only in some cases" and names
the gate line. A question with no gate says it is open from the start (it is pending on a
return with nothing answered), open once who the return is for is answered (pending on the
one-person return, the joint return or both), asked of an entry as soon as it is listed
(pending on a one-person return whose lists each have one entry and nothing else answered),
or, failing all of these, only "asked only in some cases". Being open at the start does not
mean every filer is asked it: a later answer can still make a question unnecessary.

The controls stay at the foot of the window: thumbs up, thumbs down, clear, the notes box,
previous and next. A progress line gives the place and the counts ("37 of 663; 30 up, 5
down, 2 skipped": skipped are the questions without a verdict that come before the last
question that has one). The page can go to the first question without a verdict or to a
question by id, and can show only the questions without a verdict, with thumbs down, with a
note, that are long, or that are stale; next and previous then move among those. Keys, when
the cursor is not in a text box: `u` thumbs up, `d` thumbs down, `x` clear, `j` or the right
arrow next, `k` or the left arrow previous, `n` the notes box (Esc leaves it), `f` the first
question without a verdict, `g` the box for an id.

Every change is saved at once (a note a moment after typing stops, and when the cursor
leaves the box), and a line at the top says so, or says in red that it was NOT SAVED, with
the reason and a control to try again. The page shows a verdict as given only after the
server has confirmed it.

Verdicts are kept in `reviews/2025/owner_vetting/verdicts.json`, a tracked file of the
repository (`reviews/2025/owner_vetting/README.md` gives its format). It does not depend
on the returns directory, and holds nothing from a return. `serve --vetting <file>` names
another file, which the tests use. Each record holds what was judged, as the question bank
stored it then (prompt, help, answer type and the answers offered), and the digest of that.
When a question's stored wording, type or offered answers differ from what its record
judged, the record is **stale**: the page shows the earlier verdict and note marked as given
on earlier wording, with that wording, and counts it as no verdict on today's question,
until a verdict is given again. A note changed on a stale record leaves it stale. A record
whose id the interview no longer asks is kept and listed under "Questions no longer in the
interview". Nothing is ever dropped because the wording moved.

`node engine/dist/main.js vetting-report [--write] [--file <verdicts.json>]` lists the
verdicts for whoever acts on them: the counts, the thumbs-down questions with their notes,
the notes on thumbs-up questions and on questions with no verdict, the stale records and
the records of questions no longer asked, each with its id and the wording judged. With
`--write` it writes `reports/2025/owner_vetting.md`. The report is written on demand; no
check requires it to exist or to be current, so saving verdicts never leaves a check
failing. Its `--self-test` (in `check-all`) tests the digest, the file and the record rules
on planted cases and the cards of the built bank.

## The answer log

The log is append-only JSON lines: a header, then one `{input, value}` event per answer.
Replaying it starts from the profile's initial answers and applies the events in order;
an event on an initial key is invalid. A correction is another event for the same input;
`answer` accepts an input only if it is currently reachable or already answered. Before
an event is appended the candidate inputs are validated and the state is computed, so a
malformed or unreachable answer is a command failure and is not written.

The answers of a tick-box screen are ordinary events, one `{input, value}` per box, appended
together (`applyAnswers` in `interview.ts`). They are checked against the state before any of
them, because the filer gave them together: each must be a box of the screen the interview
offers at that moment, every box must be answered, and each answer is yes or no. So the log may
hold a No for a question the engine would not have reached one question at a time (a member
after one whose Yes refuses the return); replay reads it as any answer, and it stands if the
question is reached later. The log does not record that the answers shared a screen.

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

At build (`engine/src/interview-check.ts`): each fixture case marked `walk: full` (the whole
returns of `returns.json`) is walked once with the fixture's answers, checking termination,
that each question is a reachable input with a fixture representative and is never repeated,
and order invariance (the reversed answer order gives the same values and status);
that is representative coverage, not an exhaustive proof. The build also fails when a
reachable input has no question in the bank, when a profile asks the roster of an
implicit collection, and when a line nothing reads is neither a target nor marked
`display`.

The CLI tests (`engine/src/integration.ts`, `test-integration` in `check-all`) cover
help requests, corrections, early refusals, invalid inputs, the refusal to overwrite a
log and the profile-mismatch error.

## Coverage rows

`2025/coverage/` lists the situations the interview is known to handle, one file per part of
the interview (`opening.yaml`, `jobs.yaml`, `credits.yaml`, `hsa.yaml` and the others; `ny.yaml` holds the
New York part's rows, profile `ny`). A row names a situation as the
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
  - id: opening.married_picks_single
    design: C.1 row 9 (married, picks "None of these")
    situation: A married person takes the line that says they were not married, then says they were married at the end of 2025.
    uses: [one_person]
    answers:
      household.ever_married: true
      household.married_dec31: true
    expect:
      refused: household.filing_status_conflict
```

A row has an `id` (lower case, no tax year, unique across the files), the `design` row it
comes from, the `situation` in one plain sentence, its `answers` and one expected end.
Answers are keyed by the question's exact id, as the answer log has it and the page shows
it (`person[taxpayer].birth_year`, `$f8889@person[taxpayer]`), with the log's values. A row
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
an input's `order` and `help`, and where it has them its `seq` ("Blocks") and its tick-box `group` and `tick`
("Tick-box groups"). Its prompt is filled at build from the form line's
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

### Blocks

The bank states the order of asking (`askOrder` in `engine/src/interview.ts`, which the interview-rules check also
uses). A question's `order` number is its topic's position: the open question with the lowest `order` is asked first.
Its `seq` (a whole number from 1; gaps are allowed) is its place within the topic. No two questions of one order
number state the same `seq` (the build fails otherwise). A question that states no `seq` is asked after those of
its order number that do, by key.

Within one order number the questions that state a `seq` are asked as an outline reads. At each level (the return;
an entry of a collection, such as a person; an entry of a collection inside it, such as one of that person's W-2s)
the lower number comes first, where a question of that level counts by its own `seq` and a run of entry questions by
the lowest `seq` in it. A run is a stretch of questions, consecutive in `seq`, that belong to one collection; all of
one entry's questions in the run are asked before the next entry's (entries by key). So a couple is asked one
person's questions through, then the other's; a person with two W-2s is asked one W-2 through, then the other; and a
question of the person placed (by its `seq`) after the W-2 questions is asked after the last W-2. The build computes
each run's place into the built question (`at`).

A child follows its parent at once when the bank gives it the same `order` and the next `seq`, and when the child is
reachable as soon as the parent is answered. A question is asked only once the return is certain to need it. The
evaluation proper reads a line's refusal gates in order and stops at the first one not yet answered, so a question
behind such a gate used to wait for the gate's own question, whatever the bank said. While a return is incomplete the
interview therefore also runs a reach pass (`inputsAhead` in `engine/src/eval.ts`), which reads past an unanswered
refusal gate to the gates after it and to the line's own expression, as the evaluation will once the gate is answered
no. A question it finds that states a `seq` is open at once, and the bank's order decides among the open
questions; one that states no `seq` stays closed until the evaluation itself reaches it, so where the bank states no
order the forms' order of refusal gates still decides (a screen before what stands behind it). The pass changes no
value, and a complete or refused return's open questions are the evaluation's own. It does not read ahead in two places, where
the need for a question truly depends on an answer: beyond the first unanswered guard of a `choose`, and beneath the
operands of an `all` or `any` test that follow an unanswered one. A question that waits on such an answer (or on its
roster) is placed after the question it waits on; `node engine/dist/main.js interview-order` walks returns and lists
every question that became reachable late, with the answer it waited on.

Order alone does not keep a topic together where a form's results enter the return in several places, each read
only once the return has got that far. The
health savings account block (order 190: the roster `$f8889`, the Form 8889 questions, `person.age55_at_year_end` and
`person.x_hsa_value`) is
kept together by the `full` profile's asking for Form 8889's three results directly (`s1.line13`, `s1.line8f` and
`s2.line17c`, which the return's own targets read in any case): each of the form's questions is then reachable as
soon as the account is listed, and a refusal on the form is told at once. `person.x_hsa_value` is the exception: it
is reached through Form 5329 and is asked when that form is.

Schedule 3's unprepared credits are refused from lists read in order: the refusal entries of `s3.line7` (adoption,
the bond credit, the credit for the elderly, vehicles, the earlier year's forms, the mortgage certificate) and of
`s3.line14` (the farmland choice, the three foreign items, repaid income), with the chain `s3.other_credit` and the
list of `scope.ready` in nearly the same order. Two things follow, and they are different
(`docs/provisional/lanes/stitch.md`, part 3, measured):

- **When a question is asked.** A Schedule 3 question that states a `seq` is open as soon as the return needs it,
  whatever stands ahead of it in those lists (the reach pass), so each can be asked at an order number of its own. One
  that states no `seq` still waits for the questions ahead of it.
- **When a refusal is told.** A refusal is told only once the situations listed before it on its line are answered.
  A question numbered before one that its line lists earlier is asked in its place, but its Yes is told as a refusal
  only when that earlier question is answered (`s3.ev_dealer` before `s3.credit_bond`; a child of `s3.foreign_any`
  before `s3.farmland`). The coverage rows show it as "the refusal … came on a background answer". The bank's remedy
  is to number the screens of one line in the line's order; the form's is to list the entries in the order of
  asking, or to give each situation a line of its own.

The Form 8863 Part III questions exist twice, as `person.edu*` and `dependent.edu*` lines with a bank entry
each, because a student is a person on the return or a dependent. The two statements are kept the same:
a change to the wording, help, order or citation of one is made to its twin in the same commit, by a lane
that has claimed both `person` and `dependent`, and `tools/check_twins.py` (check-all) fails on any
difference not declared with its reason in `reviews/2025/twins.json`. `check_twins.py --sync-from person`
shows the copy and `--write` makes it (tools/README.md, "Twin lines").

### Tick-box groups

A tick-box group is a few yes or no questions, side by side in one topic, that the page shows on
one screen ("Web UI"). It is presentation only: each member stays its own input with its own
prompt, help and citation, is recorded as its own answer and is corrected on its own; the CLI
asks the members one at a time, and the forms know nothing of groups. The bank declares a group
once and a question joins it by naming it (the bank's group `rare_credits`, three Schedule 3
questions of order 290, on which `test-serve` tests the screen):

```yaml
bank:
  groups:
  - id: rare_credits
    heading: In 2025, did you (or, on a joint return, your spouse) do any of these?
  questions:
  - input: s3.farmland
    order: 290
    seq: 2
    group: rare_credits
    tick: Sold farmland
```

`heading` is the question the filer reads above the boxes; `tick` is the few plain words beside
a member's box. Both are reworded as a prompt is when shown (the spouse phrase; for a group
asked of each person the build puts the collection's frame before the heading, and the
per-person frame and the person named follow the entry).

A group is placed as its members are ("Blocks"): the members have one `order`, the topic's, and
each states a `seq`, the order of the boxes. The numbers may leave gaps (10, 20, 30), but no other
question of the order number has a `seq` from the lowest member's to the highest's. The group
needs no order number of its own, and the other questions of the topic need
not state a `seq` (one that states none is asked after those that do). Stating a `seq` also
opens a member as soon as the return needs it, whatever refusal screen stands ahead of it in
its form, so the screen is whole unless a member truly waits on an answer outside the group (its
parent's, its roster's, or an answer that decides whether its form is read).

The build (`tickGroupProblems` in `engine/src/tick-groups.ts`) refuses: a group with fewer than
two or more than six members; a member that is not a yes or no input; a member without `tick`,
or `tick` without `group`; a label of more than twelve words, on more than one line, ending in a
question mark, or shared by two members; a heading of more than 25 words or more than one line;
entry syntax or a near-miss of the spouse phrase in either; a group no question names, or a name
no group declares; members of more than one order number; a member without `seq`; another
question's `seq` lying from the lowest member's to the highest's; members of
several forms when one of them is a list's form (a screen is asked of one entry); and a member
that another member's Yes opens (its gate reads that member, directly or through what yes/no
lines compute; a gate that only stands behind a derived refusal screen does not count). The
build does not say where the other questions a member opens stand; `tick-groups` checks when
they are asked. Asked one at a time (the CLI, or a member answered on its own), an opened
question follows the remaining members rather than its own parent.

When the first pending question is a member, `interviewView` returns the screen as `group`: the
members of that group, for the same entry, that are open, and those that would be open once the
open ones are answered No (a member the engine reaches only after another member, because the
two are read by one chain of tests, belongs on the screen: with none ticked it is asked next in
any case). Open means what it means for the next question: the evaluation's own inputs and those
the reach pass finds. A member already answered, or waiting on an answer outside the group, is not on it,
and a screen of one box is no screen (`group` is null and the question is asked as usual).

`node engine/dist/main.js tick-groups` (check-all step `tick_groups`; its `--self-test` in `tools/self_tests.py`) checks every group of the
built `full` and `ny` interviews on the background return: that the screen shows the whole
group; that with each member in turn ticked each question the answers open is asked before
any question that was already waiting and has an earlier order number than the opened one (so
an opened question is given the group's order number; within it, other questions may come
first); and that the same answers given one at a time end the return the same
way. `tick-groups --self-test` plants each refused declaration, and a group asked of each
person on the built interview. `docs/provisional/lanes/tick.md` says what makes a good group.

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

## What a given filer is asked

`node engine/dist/main.js draft-walk` (`engine/src/draft-walk.ts`; free and deterministic, no model call) walks each
persona of `2025/personas/` through the built `full` interview and writes a transcript per persona, and `SUMMARY.md`,
to `docs/provisional/walks/after/` (`--out DIR` for another place; `--only NAME` for one persona; `--summary` for the
table alone). A persona is a filer in one sentence with the answers that filer gives, keyed by the question's exact id
as the answer log has it:

```yaml
name: 01_single_w2                # the file's name
who: A single person, 31, with one job (one Form W-2, $52,000 of wages) and nothing else to report.
end: complete                     # or { refused: <gate> }; optional
answers:
  $person: [taxpayer]
  f1040.status: single
  $w2@person[taxpayer]: [acme]
  person[taxpayer].w2[acme].box1: 5200000
```

The walk is the coverage rows' walk (`interviewView`, `applyAnswer`, first refusal or completion), and every question
the persona does not answer is answered by the same background return. It differs in one way: a question the
background return never met is given the closed answer (no, zero, none, the first option) so that the walk goes on, and
is reported as opened and unanswered, with the answer that opened it. The command fails, naming the persona, on an
opened and unanswered question, on a stale answer (an id that names no question, or a question the walk never asks),
on an answer the interview rejects, and on an end other than the persona's `end`; the transcript is written all the
same, with the problems at its head.

A transcript lists each question asked, in order: its id, its topic (the form its input belongs to), the prompt as the
page shows it to this filer (`shownAt`), the answers offered, the answer and where it came from, the words of the
prompt and of the help, and the help's first sentence. A question whose topic differs from the one before it is marked
as a topic switch, and as a return when the walk had already left that topic. It ends with the end reached (a
refusal's wording as shown), the totals, the ten longest prompts and the whole walk at one line per question.
A tick-box screen is one step: the walk answers its boxes together, as the page does, prints the
heading and the labels with the boxes ticked, and counts the heading's and the labels' words
once in place of the members' own prompts (which the page keeps behind "What this asks"). The
totals and `SUMMARY.md` give the steps (screens) beside the questions.
`docs/provisional/walks/before/` holds the walks of the interview before the provisional redraft; a file there is
never overwritten. `draft-walk --self-test` (check-all, `tools/self_tests.py`) plants each failure on the built interview.
