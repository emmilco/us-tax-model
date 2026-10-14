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
