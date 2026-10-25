# Transcription agreement

The data-layer counterpart of the engine differential (spec 6.5): every
worksheet is transcribed a second time by a model that sees only the archived
IRS pages the project's own citations name, plus the data model, and the two
transcriptions are compared line by line. Agreement is evidence that the
operand structure follows the text; a disagreement is adjudicated by the
agent reading the source page, with the quote and page recorded in the
ruling. These model reviews supply no human-reading credit (spec 3, requirement 11). Nothing here writes to
`forms/`; a transcription defect becomes an ordinary fix with a bug inventory
entry.

The owner's 2026-10-24 amendment is in `docs/2026-10-24_validation_policy.md`. Human packets and
ruling samples are optional. Engineering adjudicates routine source disagreements; only substantive
scope choices or ambiguities requiring owner judgment need escalation. Online interpretation can
corroborate a recorded reading under `research/secondary/`, with provenance and contrary material;
it does not enter blind source-only prompts, qualify a noisy run or add scoreboard assertions.

## Isolation

Fixed-prompt, curated input, unattended, non-secret: the model's text is parsed
as YAML, verdicts or worked values and compared; it drives no write path,
command or execution (AISP Part I §2 classification by the apply code). What is
sent is the archived public IRS text, the data model, and synthetic figures
from generated returns; no personal data.

## Transports

`call_model` in `transcribe.py` chooses the transport by the model name, and
every tool here (`transcribe.py`, `render_compare.py`, `classm.py`,
`transcribe_tables.py`, `screen_review.py`, `rerun_all.py`) takes `--model`:

- `claude*` — `claude -p --setting-sources "" --tools "" --no-session-persistence
  --permission-prompts none --model <pinned>`, system prompt task-only. The tool
  list in the init event is empty and a request to read a file is refused;
  verified before the first run. No credential beyond the CLI's own.
- `deepseek*` — DeepSeek's hosted OpenAI-compatible endpoint
  (`https://api.deepseek.com/chat/completions`), standard library only: the
  system and user prompts become the two messages, temperature 0, one
  non-streaming request with a timeout, retried with backoff on 429 and 5xx
  (at most three retries). The model ids the account sees are listed by
  `GET https://api.deepseek.com/models` (`deepseek-flash`, `deepseek-v4-pro` at
  the time of writing; check the pricing page before choosing). The API key is
  read at call time from the macOS keychain, service `deepseek-api`, account
  `elliotmilco` (`security find-generic-password -s deepseek-api -a elliotmilco
  -w`), held in memory for the request only, and never written to a file,
  printed, logged or exported to the environment (AISP Part II §5). A missing
  entry fails with a message naming it. `cost_usd` in the meta is `None` for
  this transport: DeepSeek prices depend on the hour (peak and off-peak) and
  are not reproduced here; the token usage is recorded instead.

Any other model name is refused; nothing routes to a transport by default.
Every log records both the model requested and the model the service
reported, whichever transport ran. `--dry-run` builds the prompt and excerpt
and reaches neither transport nor the keychain.

```
python3 tools/transcription/transport_check.py [--model deepseek-flash]   # one tiny call; prints model and usage
```

## Model families

The owner's selected second-family model is `deepseek-flash` (correction 2026-10-23).
Use that id explicitly for new runs; earlier Pro artifacts retain their actual model labels.
The `models` pin in `families.json` is enforced before network calls and when qualifying review
logs, so another member of the same family cannot silently substitute for Flash.

A family is the first token of the model name (`families.py`: `claude-opus-5-5`
is `claude`, `deepseek-v4-pro` is `deepseek`). Each family's review of a form
is its own log beside the others, never a replacement: the Claude logs keep
their plain names, and a run with another family writes

```
reviews/<year>/transcription/<form>.<family>.md   with <form>.<family>.rulings.json
reviews/<year>/render/<form>.<family>.md          with <form>.<family>.rulings.json
reviews/<year>/classm/<form>.<family>.md          with <form>.<family>.rulings.json
fixtures/<year>/classm.<family>.json              that family's class M fixtures
```

`rulings.py`, `rule.py` (`--family deepseek`) and `check_logs.py` address a log
by (kind, form, family); the Claude family is implied when none is named. The
raw prompt and response under `.transcription/` and `.classm/` take the same
stem, so `--from-response --model deepseek-flash` re-reads that family's
saved response. A second family's class M fixture cases carry the family as a
suffix on the case id (`classm.qdcg.1.deepseek`) so no two families' cases
share an id; their `evidence_note` records the model, which is how the
evidence report counts second-family M assertions.

`families.json` lists the families `check_logs.py` expects:

```json
{"required": ["claude"], "optional": ["deepseek"], "models": {"deepseek": "deepseek-flash"}}
```

Every required family must have a current log with no open ruling for every
form (`check-all` fails otherwise). An optional family's logs may be missing;
those present are held to the same snapshot and subject checks, and their
open rulings are counted and printed without failing the run, so a second
family's disagreements can stand open while they undergo source adjudication. A log whose
family is in neither list fails. Counts are printed per kind and family. The
family can move to `required` only once every form has a qualifying log; an owner reading sample
is no longer a prerequisite under the amended plan.
Optional `by_kind` entries override the two lists for one review kind. This lets
transcription/render become required while class M is still being qualified.

### Agreement floor and independence yield

```
python3 tools/transcription/compare_families.py      # offline; writes reports/<year>/second_family.md
```

For every form with a Claude log and a second family's log of the same kind,
the lines judged by both are compared and three things reported, per form and
overall, in `reports/<year>/second_family.md`:

- the **noise rate** (owner's decision 12): second-family disputes explicitly
  ruled `model error`, divided by that family's judged lines, at most 10% per
  form-kind run. Findings, representation, scope and ambiguity rulings are not
  noise. Integer arithmetic makes 1/10 pass and 1/9 fail. Above the limit,
  choose a stronger model and do not count the run. Raw agreement remains a
  diagnostic; a correct objection does not disqualify a reader.
- **eligibility**: subjects and archived source hashes must be current, the
  requested/reported models must belong to the named family, all expected
  lines must be judged, verdicts must be valid and unique, and every dispute
  must have a classified ruling. Transcription also requires the current
  independence policy. Open/unclassified, missing, stale or empty reviews
  earn no assertion. Optional pending reviews remain visible.
- the **independence yield**: lines the second family disputed where the
  Claude log agreed or matched, each with the second family's reason. Zero is
  a visible result.
- the lines **both** families disputed, and the lines only the Claude run
  disputed.

MISSING lines are excluded from the noise denominator and block eligibility;
they cannot improve a run's qualification. A log whose subject hash is no longer
current is marked stale. `check_logs.py` prints the report's summary line when
the report exists. `rerun_all.py --model <non-Claude>` runs every form that has
a log of any family through that family, leaving the Claude logs as they are.

## Running

```
python3 tools/transcription/transcribe.py --form qdcg            # one model call
python3 tools/transcription/transcribe.py --form qdcg --dry-run  # excerpt and prompt only
python3 tools/transcription/transcribe.py --form qdcg --from-response   # re-compare the saved response
python3 tools/transcription/rerun_all.py --kinds transcription,render --model deepseek-flash --resume
```

This is a deliberate network step like the source fetcher; it is not run by
`check-all`. `check_logs.py` runs in `check-all` and fails on an open ruling,
a missing log, a log made against a different source snapshot, or a log whose
subject has changed. Every form has a log; a new form fails `check-all` until
it has one.

Each log records the hash of its subject, what that kind of review judges
(`subjects.py`): for a transcription the form's definition, for a render
comparison the rendered English, for class M each line's id, type and
expression, all without citations (`tools/citations.py` checks those). A change
to the subject fails `check-all` until the review is run again; a change to a
tool's prompt or to the pages a citation names does not, and is rerun
deliberately. `classm.py` builds the data and rebuilds its document's jobs
before every run, so it never works from jobs of older data.

Raw prompts and responses are kept under the git-ignored `.transcription/`;
the committed artifact is the log. For transcription/render/class M, cached responses
are bound to the exact prompt, system prompt, model, policy and explicit
reasoning effort. A changed request requires a fresh call; it cannot relabel
an old response. `--dry-run` writes a separate `.preview.prompt.txt`.
`rerun_all.py --resume` reuses only matching receipts and saves progress after
each completed job. `--reasoning-effort low|high|max` is supported for DeepSeek
reviews; it is recorded and checked on reuse. Class M rebuilds current jobs
even when reusing a response, so changed supplied amounts require fresh work.
`--max-output-tokens N` raises the DeepSeek allowance for reasoning plus the
final answer (default 65536; use 131072 for the largest documents); the request
timeout grows proportionally. The effective allowance is bound in receipts and
recorded in logs. A response ending because of length cannot be accepted, even
if its partial content happens to parse. Original bound receipts predating this
option retain their fixed 65536 allowance and cannot be relabeled as larger calls.

## Excerpt selection

The pages a form's citations name (`p. N`, `pp. N–M`), cut at the archived
text's page breaks; a whole document when it has six pages or fewer; and for
a locator that names a worksheet or an instruction line without a page, the
page whose heading starts a line. The log records which pages were used.

## Rulings

```
python3 tools/transcription/rule.py --form sd --rulings rulings.json   # {"<printed or id>": "Ruling: ...", "*": "..."}
python3 tools/transcription/rule.py --form sd --family deepseek --rulings rulings.json   # a second family's log
```

A ruling is written into the log under the disagreement it answers, with the
source quote and page it rests on, and one of three outcomes: project
retained (representation or scope difference), second transcription right
(a data fix follows, with a bug inventory entry), or genuine ambiguity (an
ambiguity register entry). Re-comparing a saved response keeps a ruling only
when both the disagreement and its recorded review context are unchanged.
The context binds the reviewed subject, prompt, system, source excerpts and
request settings. A question-wording change can therefore reopen a ruling even
when its expression trees are identical (BUG-0121). Class M includes every case's
prompt hash. Historical sidecars without a context remain readable but are
never automatically reused; migration does not certify an old rationale in a new context.

## What is compared

Printed computed lines, matched by printed number. In addition, helper lines
that other forms read (for example `qbi.deduction`, `ftc.credit`, the
per-person W-2 totals) and the result lines of the shared definitions
(`tax_on_amount.tax`, `tcw.tax`) are listed in the prompt by id and compared
by id after full expansion, since no printed line exposes their logic. The
prompt also lists the collections with their entry fields, enumerations,
year parameters and every other form's ids, printed markers and types.
Computed labels and expressions are omitted from every catalog, including
exported helpers and collection fields (`source-only-computation-v2`). Input
questions and refusal-screen interfaces remain explicit shared assumptions.
The input interface is closed: a reviewer must encode the supported slice
using those inputs and document excluded cases. Shared IR conventions explain
parameter selection and result propagation after an IRS STOP without supplying
the project's chosen operands or formula.

## Comparison

Each printed line of both transcriptions is expanded into a tree over inputs,
parameters, constants and references outside the form, so helper naming on
either side does not matter. Shared parameterised definitions are inlined with
their bindings; another form's helper lines are expanded in place; guards are
normalised (`X == true` is `X`, negation pushed through `all`/`any`,
comparisons oriented one way, a zero test on a non-negative line read as a
bound, a guard written as a Boolean line reference expanded); literal-valued
parameters compare as constants; zero terms are dropped from sums; `choose`
alternatives that select the same target are merged under one `any` guard.
Lines agree when the canonical trees are equal.

**BUG-0129 follow-up (2026-10-25):** constant normalization preserves Count annotations and
parameter units, and distinguishes Boolean constants from numeric zero/one. Before comparison,
`check_model_types.mjs` validates expressions with the project JSON schema and the build's
reference/type rules. It keeps published input types, rejects added inputs/changed result types,
and uses only the model's own computed helpers in the reviewed document. No candidate expression
is executed. Citation and guard-exhaustiveness checks are outside this adapter's scope.

New logs record `checked-expression-types-v2`, `project-expression-types-v1` and a passing/failing
validation result. A type error reaches every line that reads that helper; even an unused invalid
helper fails the form's type check and gives tool exit 3. BUG-0132 extends dependency traversal to
count, proration, keyed-table and collection-field operands. Invalid expressions cannot agree by
canonicalization alone. Passing types does not establish source correctness or numeric evidence.

BUG-0130 supplies Count-literal syntax; BUG-0131 preserves complete input/refusal questions instead
of cutting off late meanings and exceptions. New logs separately check the actual prompt against
all current filer-input questions (`complete-input-context-v1`; shared-definition caller bindings
are excluded). This is a host-side completeness finding, not a change to the original request's
prompt-policy metadata. Both families need current comparison, passing types and complete input
context before the pair can qualify. These properties are bound into ruling contexts.
This version verifies question wording only: it does not certify which answers the guided
interview may leave unasked (BUG-0134/T-063). Availability-sensitive disagreements remain gaps.

BUG-0133 supplies declared table ids, ordered key types and result types without cells or authored
formulas. Requests also include the generic expression JSON Schema, restricted to the engine's
implemented atoms; reserved operations and unavailable table interfaces are omitted. Run
`npm run compile` before building a prompt so the implemented-atom catalog and validator exist.
Explicit syntax reminders address nested Boolean tests, collection binding, Count and money types.
Exact saved request hashes remain the provenance: earlier replies are not relabeled as seeing a
later schema or interface catalog. The first asset probe demonstrates valid table references but
still has other invalid IR and unresolved source issues; a schema catalog is not tax certification.

All transcription qualification remains held until verified record migration/fresh requests and
source adjudication close (T-062). Removing the global hold cannot promote unchecked legacy logs.
Render, worked-value and engine evidence have separate rules.

`python3 tools/transcription/audit_transcription.py` verifies saved subjects, prompt hashes,
metadata consistency and embedded replies before checking types and comparing. It writes only
`.transcription/expression-type-audit-current.json`; it never modifies requests, replies, logs or
rulings. Legacy incomplete receipts remain legacy-limited. `--forms`, `--family` and `--report`
restrict/output the diagnostic audit. Exit 1 means some records could not be verified/recompared.
The initial literal audit is preserved at `.transcription/typed-literal-audit.json`; its nine lost
agreements were an earlier, narrower result. Current totals and migration limits are in
`reports/2025/transcription_audit.md`. An audit report alone never qualifies a reading.

Representational differences the comparison cannot see through remain as
disagreements and get a ruling: typically a value the project derives from
another form where the second transcriber asked a question, or a line the
project pins to zero because the spec refuses that part of the return.

## Render comparison

The second construction in this directory (spec 6.5): `render_compare.py`
gives an isolated model the rendered English of every printed line of one
form (`rendered/2025/<form>.md`: the encoded restatement, its refusal rules,
and a glossary of the helper values it names, followed transitively) together
with the same cited pages, and asks for a verdict per printed line: MATCH,
MISMATCH (quoting the IRS words that differ) or UNCLEAR (what is missing).
The model never sees the YAML or an expression tree; it judges whether the
English says what the page says. Same isolation and the same `call_model`
transports as the transcription, with its own task-only system prompt; about
$0.10 per form on Claude.

```
python3 tools/transcription/render_compare.py --form qdcg            # one model call
python3 tools/transcription/render_compare.py --form qdcg --dry-run  # prompt only
python3 tools/transcription/render_compare.py --form qdcg --from-response
python3 tools/transcription/rule.py --kind render --form qdcg --rulings rulings.json
```

The glossary names each helper by its label (the renderer writes helper
references that way), lists the gate lines that refusals name by id, and ends
with the IRS wording of every line of another form the restatements mention.
The excerpt is the transcription excerpt plus the pages a locator names for
another document ("i8995 pp. 3–4"), the pages refusal citations name, and the
pages cited by the year parameters the form uses (structural zeros and ones
excepted). Printed lines are keyed by printed number, a marker several rows
share (the Tax Computation Worksheet's columns) is qualified by the line id,
and a form whose lines are all helpers is judged line by line keyed by name.

Logs go to `reviews/2025/render/<form>.md`, one per form, with the pages
given, the model and prompt hash, every line's verdict and the model's
reason, and a ruling under each MISMATCH or UNCLEAR. `check_logs.py` holds
render logs to the same rules as transcription logs. Rulings are keyed by the
restatement and the model's reason, so a changed rendering or a new response
reopens them. A renderer change that alters a restatement therefore reopens
the rulings on that line; a value-neutral wording change is still a change
to what was judged.

The two constructions see different things. Transcription agreement compares
operand structure and is blind to a rendering that misdescribes a correct
expression; the render comparison reads the description and is blind to an
expression the description flatters. A line both pass has an expression that
a second transcriber built the same way and an English restatement a second
reader accepts against the page.

## Class M hand-work

The third construction here (spec 6.1 class M, 6.5): `classm.py` has an
isolated model fill one document by hand from its archived pages and the
amounts that flow into it, for the generated returns that together take every
reachable branch of the document. `node engine/dist/main.js classm-jobs`
chooses those returns (whole-dollar inputs, a greedy cover of the document's
choose guards, Bool sides and floor/min/max sides over a 2,000-return
corpus) and writes `.classm/jobs.json` with, per case, the whole-return
inputs, the values the document reads from other documents (printed lines by
title and number, helpers by label, collection entries field by field), the
filer's own inputs, and the project's values for comparison, which the model
never sees. Results of the shared tax computation (Tax Table or Tax
Computation Worksheet) are given, not worked; that computation is covered by
the Tax Table conjecture and the transcription and render logs of `tcw` and
`tax_on_amount`.

```
node engine/dist/main.js classm-jobs [--docs qdcg,sd]
python3 tools/transcription/classm.py --doc qdcg            # one call per case
python3 tools/transcription/classm.py --doc qdcg --dry-run
python3 tools/transcription/rule.py --kind classm --form qdcg --rulings r.json
```

One log per document in `reviews/2025/classm/<doc>.md`: pages, model,
prompt hash per case, the branches each case takes, every line's agreement
or disagreement with the model's own arithmetic shown, and a ruling under
each disagreement. The agreements are fixture cases `classm.<doc>.<n>` in
`fixtures/2025/classm.json`, evidence class M, run by `test-fixtures` like
any other. A model of another family writes `<doc>.<family>.md` and its
cases, suffixed with the family, to `fixtures/2025/classm.<family>.json`
(see Model families). A disagreement is written into the fixture as the model's value,
so the build fails until it is ruled: a project defect gets a data fix and an
inventory entry; a model arithmetic error is dropped from the fixture with
`{"ruling": "...", "drop": true}` and stays in the log. Documents that are
collections (`person`, `w2`, `sales`, `gift`, `interest`) or definitions
(`tcw`, `tax_on_amount`) have no class M cases yet.

Worked-value runs seed the generated corpus with non-M regression facts for the
requested document (`classm-jobs --include-fixtures`). The reviewer receives
the facts and incoming amounts, never the fixture's expected values. A declared
filing flag must be true, and positive examples of supplied money amounts are
included when available. This prevents an unlucky random sample from silently
losing an active regime after a validation fix. The coverage summary describes
the sampled, buildable cases; it does not prove other branches unreachable.

Blank/skip replies are recorded as SKIPPED and earn no numeric fixture assertion,
including when the evaluator happens to produce zero. Explicit printed zero
remains an assertion. `audit_skipped.py` checks old logs against their embedded
raw replies; `--apply` removes only skipped expectations and archives originals
with hashes. The audit is an offline check-all step (BUG-0123).

