# The interview

The interview is a client of the evaluator (`engine/src/interview.ts`): the inputs the
evaluator finds unknown and reachable on the way to a profile's targets are the questions;
authored data (`questions-2025.yaml`) supplies their wording and order; an append-only log
supplies the answers. All amounts are integer cents. No data is transmitted.

With dependencies and Lean installed, rebuild and check offline with `npm run check-all`.

## Profiles

A profile file lists its targets, its initial answers and the inputs it asks; the build
(`engine/src/build.ts`) reads the four below and writes each to `canonical/`.

| Profile | File | Targets | Scope reported by the CLI |
|---|---|---|---|
| default (`social-security`) | `2025.yaml` | Form 1040 line 31 | Social Security credit and supplied Schedule 3 Part II subtotals; not a complete return |
| `sales` | `sales-2025.yaml` | Form 1040 lines 7a and 16 | securities sales, Schedule D and tax-method selection; AGI and taxable income computed; not a complete return |
| `stage4` | `stage4-2025.yaml` | `scope.ready`, lines 7a and 16, the Schedule A deduction, Form 4952 line 8, the QBI deduction, Schedule 2 line 21, Form 8959 line 24, Schedule 3 line 1 | form slices with eligibility and valuation screens; not a complete return |
| `full` | `full-2025.yaml` | `scope.ready`, Form 1040 lines 24, 33, 34 and 37, `f2441.line1_box`, `f2441.line1_paid`, `f2441.statement_notice`, `f2441.household_notice`, `f5695.line32b`, `ira.basis_total` | the whole return: Form 1040 lines 1a–37 end to end for single, head of household, qualifying surviving spouse and married filing jointly returns, with cited refusals for unsupported items (married filing separately among them); no filing or transmission |

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
`question` (its `input`, `prompt`, `help`, `order` and `cite`, and `helpRequested`), the
`refusal` if any, `reachableInputs`, the profile's `scope` sentence, the standing
`notices`, the `values` with derivations, and a text `sheet`.

Answer using the question's exact `input` key. `--value` is JSON: `false`, `620000`,
`"single"`, `null` or `["employer_a","employer_b"]`. `null` requests help: the value
stays unknown and the same question is asked again with `helpRequested` set. A blank
printed money box must be entered as zero if that is the intended answer; unanswered
questions never default to zero. Questions are asked in bank order, then by key.

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

Every profile asks its questions from one bank, `questions-2025.yaml`: each entry gives
an input's `order` and `help`. Its prompt is filled at build from the form line's
question text, after its collection's frame (for example "For this business — "), and
its citation from the line (a roster question's from its collection). An entry states a
`prompt` or `cite` only for interview wording the line does not carry; the build fails
if it repeats the line's.
