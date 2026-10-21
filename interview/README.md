# Stage 2 CLI interview

All amounts are integer cents. The interview computes the excess Social Security
credit, Schedule 3 line 15 and Form 1040 line 31. Other Schedule 3 Part II amounts
are explicit supplied subtotals; this stage does not prepare their underlying
forms or a complete return. No data is transmitted.

With dependencies and Lean already installed, rebuild and check offline:

```sh
npm run check-all
```

Start a local answer log (the file must not already exist):

```sh
node engine/dist/main.js interview start --log /tmp/synthetic-return.jsonl
node engine/dist/main.js interview answer --log /tmp/synthetic-return.jsonl --input f1040.status --value '"single"'
node engine/dist/main.js interview advance --log /tmp/synthetic-return.jsonl
```

Each response is JSON containing `status`, the next `question` (including its
citation), the values with derivations, and a text `sheet`. Answer using the
question's exact `input` key. `--value` is JSON: `false`, `620000`, `null`, or
`["employer_a","employer_b"]`, for example. `null` requests help and remains
unknown. A blank printed money box must be explicitly entered as zero if that
is the intended answer. Unanswered questions never default to zero.

The person roster is fixed by interview data to `taxpayer`. The employer roster
question uses `$w2@person[taxpayer]`. Its keys represent distinct actual
employers, not individual W-2 sheets. Consolidate repeated statements for the
same employer explicitly before entry. Corrected/replacement statements must
not be counted twice. The tool rejects duplicate roster keys; it cannot detect
two different labels that a person inadvertently assigns to the same employer.

An employer amount uses a key such as `person[taxpayer].w2[employer_a].box4`.
The CLI records corrections by appending another event for the same input.
Removing an employer makes its prior answers inactive; re-adding its stable key
reactivates them. The original events remain in the log. Logs are pinned to
2025; they are not silently usable as another tax year.

A refusal is a result, not a command failure. A `refused` response names the
unsupported form, trigger and remedy with a source citation. Its dependent
credit and totals remain refused; independent values remain inspectable.
Malformed input is a command failure and is not appended to the log.

For direct evaluation, supply a JSON object containing the same input keys
(including `"$person": ["taxpayer"]`) and confirmed employer roster:

```sh
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --target f1040.line31
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --target f1040.line31 --json
node engine/dist/main.js eval --inputs /tmp/synthetic-inputs.json --target f1040.line31 --html
```

Outputs can be redirected to local files. Use synthetic data for development;
never commit personal return inputs or logs. Ready-to-review synthetic outputs
are under `reports/2025/`, alongside `stage2-review.md`.

## Collection model

A form's `collection` metadata declares a keyed collection, optionally with a
parent collection. Each `sum_over` specifies `collection`, an entry-local
`field`, and an optional Boolean `where` predicate. Nested collections bind to
the current parent instance. All cross-entry aggregation is explicit.

A missing roster is unknown; a confirmed empty roster sums to zero. Entry keys
are stable metadata. Counts and money are distinct types. Unknown filters make
the aggregate unknown; a count of already-known matching entries is retained
as a lower bound, allowing `count > 0` to trigger an early refusal without
waiting for unrelated entries. Fixed-filter aggregation non-negativity and
monotonicity have Lean lemmas; incomplete-value handling is compared between
the evaluators and exercised through the CLI.

The build enumerates finite enum/Boolean answer domains using synthetic fixture
amounts and roster shapes. It checks termination, final-answer order invariance
and that questions are drawn from unresolved reachable inputs. The CLI tests
separately cover unknown answers, corrections, early refusal and invalid inputs.
This finite enumeration is not a proof for arbitrary numbers of entries.

## Stage 3 sales profile

Start with `node engine/dist/main.js interview start --profile sales --log /tmp/sales.jsonl`.
The log pins its profile; subsequent `advance` and `answer` commands infer it.
The targets are Form 1040 lines 7a and 16, using supplied taxable income,
qualified dividends and distribution components. Stage 4 now computes the special-gain
feeders, Form 4952 and Schedule D Tax Worksheet. This remains a form slice.

`$sales` lists stable transaction keys. For example, `sales[lot1].box` is the
manually determined A–F classification. The interview explains the reporting and
holding-period categories; it does not derive them from dates. Enter each sale
once and select `detail` or `aggregate`. The latter is allowed only for eligible
A/D transactions with no adjustments. Both routes use the same roster, preventing
duplicate routing of an entry. Distinct keys still require the user to avoid
entering the same sale twice.

Code B uses reported basis in column (e) and reported-minus-correct basis in (g)
for covered A/D sales. Noncovered B/E sales use correct basis directly. Code W
uses the supplied correct nondeductible loss. BW combines both adjustments.
Digital assets, other codes, specified special property, carryovers and additional
source forms produce cited refusals. Dates/descriptions, basis determination,
automatic wash-sale detection and statement/PDF preparation remain outside this
calculation interface. Keep the underlying records, including any required
explanation when correcting a reported wash loss downward.

Amounts remain exact cents. See the rounding ambiguity register. Build-time
checks walk every Stage 3 fixture path and reverse its answer events; CLI tests
also exercise corrections and roster removal/restoration. Unlike the Stage 2
finite-domain checks, Stage 3 path coverage is representative, not exhaustive.

## Stage 4 profile

Start with `node engine/dist/main.js interview start LOG --profile stage4`.
This profile covers the additional forms and scope screens described in
`reports/2025/stage4-review.md`. AGI and taxable income are computed through
Form 1040 lines 11b and 15. Interest payer totals and noncash gift groups use
keyed collections. Explicit eligibility answers are required; missing values
never silently default to zero. Corrections append events and recompute the
dependency graph. Fixture paths and reversed event orders are checked at build
time; this is not an exhaustive proof of every possible interview path.

## Full profile

Start with `node engine/dist/main.js interview start LOG --profile full`.
This profile covers the whole single-person return: Form 1040 lines 1a–37 with
the in-scope schedules and refusal screens, computing total tax, payments and
the refund/amount-owed lines. The estimated tax penalty is not computed; the
output states that the IRS will figure it. Withholding totals on lines 25b and
25c, estimated payments on line 26, and the refund split on lines 35a and 36
are supplied amounts read from the filer's records. The three synthetic
whole-return fixtures (`fixtures/2025/stage5.json`) walk this profile at build
time.

## Question data

Every profile asks its questions from one bank, `questions-2025.yaml`: each
entry gives an input's order and help. Its prompt is filled at build from the
form line's question text (`source`), after its collection's frame (for
example "For this business — "), and its citation from the line (a roster
question's from its collection). An entry states a prompt or cite only for
interview wording the line does not carry; the build fails if it repeats the
line's. A profile file lists its targets, initial answers and the inputs it
asks (`full` asks them all).
