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
as YAML, verdicts or worked values and compared; model-generated code, commands,
tools and paths are never executed. The separate partial-input checker can interpret
validated declarative IR using the fixed evaluator in a bounded process. What is
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
- `gpt*` (inactive family; runs only under `--inactive-family gpt`, see Model families) — `codex exec --skip-git-repo-check --ignore-user-config -s read-only
  --json --model <pinned> -` with the working directory set to an empty scratch
  directory, so no project file is in its workspace. Codex has no separate
  system-prompt flag, so the system prompt and the review prompt are joined on
  stdin; both hashes are bound in the receipt. Codex is an agent harness, so the
  call **fails closed** if the event stream reports any tool activity (command
  execution, file change, MCP or web search); only agent messages are accepted.
  The model actually used is read from codex's session rollout, which is deleted
  after the model is recorded. The owner's authority ranking is in
  `docs/2026-10-24_validation_policy.md`: `gpt-6-astra` is a peer of
  `claude-opus-5-5` and `deepseek-v4.1-flash`.
- `deepseek*` (inactive family; runs only under `--inactive-family deepseek`) — DeepSeek's hosted OpenAI-compatible endpoint
  (`https://api.deepseek.com/chat/completions`), standard library only: the
  system and user prompts become the two messages, temperature 0, one
  non-streaming request with a timeout, retried with backoff on 429 and 5xx
  (at most three retries). The model ids the account sees are listed by
  `GET https://api.deepseek.com/models` (`deepseek-flash`, `deepseek-v4-pro` at
  the time of writing; check the pricing page before choosing). The API key is
  read at call time from the macOS keychain, service `deepseek-api`, account
  `elliotmilco` unless the environment variable `DEEPSEEK_KEYCHAIN_ACCOUNT`
  names another (`security find-generic-password -s deepseek-api -a elliotmilco
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
python3 tools/transcription/transport_check.py [--model deepseek-flash] --inactive-family deepseek --inactive-family-reason TEXT   # one tiny call; prints model and usage
```

### Cost ledger

Every call that reaches a transport (`call_model`, used by transcription,
render, class M, completeness, screen, false-no, table and transport checks) appends one
JSON line to `.transcription/costs.jsonl`, success or failure: timestamp,
tool, kind, subject (form, job, screen or gate), `year` (integer) and `jurisdiction`
(`us` or `ny`) of the run (`--year`, `--jurisdiction`; a caller may pass `year` and
`jurisdiction_id` to `call_model`), model requested and reported,
transport, prompt and system characters, the prompt's sha256 and the reply's
(`response_sha256`, the identity a ruling's `run` stamp names), the usage fields as reported,
`cost_usd` as reported, `estimated_cost_usd` with its `price_basis`, duration
and outcome. Each line is one `write()` on an `O_APPEND` descriptor, so
concurrent reviews do not interleave lines. Receipts are overwritten at each
rerun; the ledger is not. It enters no prompt, receipt or meta.

The estimate uses `prices.json`: Claude's reported cost; DeepSeek's peak or
off-peak rate by the call's UTC hour (Chinese public holidays are not
modelled); GPT-6 Astra at the API list price, which is an equivalent rather
than a bill when codex runs under a ChatGPT plan. Each price names the page it
was read from; a model without a cited price is left unpriced.

```
python3 tools/transcription/costs.py [--by year,jurisdiction,day,family,kind,form,model] [--since 2026-11-01] [--json]
```

The default grouping is year, jurisdiction, family and kind. A row written before the ledger
carried `year` and `jurisdiction` is read as year 2025 and, for the jurisdiction, as New York when a
dot- or colon-separated part of its subject begins `ny_`, else federal. This is an inference
(the ledger history is not rewritten), made by `costs.py` only when a reader asks.

## Model families

Reviews run under the Claude family only. The second families, DeepSeek (`deepseek-flash`) and GPT
(`gpt-6-astra`), are **inactive** in `families.json` (`"active": {"claude": true, "deepseek": false,
"gpt": false}`). While a family is inactive:

- no review tool calls its model: `transcribe.call_model` raises `families.InactiveFamily` before any
  transport, keychain read or ledger row, and the writers (`transcribe.py`, `render_compare.py`,
  `classm.py`), `transport_check.py` and `rerun_all.py` refuse a `--model` of that family at their
  arguments;
- a single deliberate run needs the override naming the family, `--inactive-family deepseek
  --inactive-family-reason TEXT` (on those tools; `rerun_all.py` passes it to each tool). Each paid call
  made under it records `"inactive_family_override": {"family", "reason"}` in its cost-ledger row;
- `check_logs.py` counts the family's logs as history and never requires or fails them; their integrity
  is still checked for every family by `rulings.check()` (run by `check_logs.py`) and
  `review_store.py check`;
- `compare_families.py` (the check-all step `compare_families`) does not regenerate
  `reports/<year>/second_family.md`; the last report written stays as the record and the step says so;
- the family's class M fixtures (`fixtures/<year>/classm.<family>.json`) still run as evidence cases,
  and the evidence report still counts them as second-family M.

The transport (DeepSeek's hosted endpoint, `codex exec` for GPT), the DeepSeek token-budget and
reasoning-effort options, the eligibility checks and the comparison are kept and tested offline
(`test_review_tools.py` runs them under the override). **To reactivate a family**, set its `active`
flag to true in `families.json`: `check_logs.py` then checks its logs as an optional family again
(stale logs that would earn credit fail), `compare_families.py` rewrites the report, and its models
run without the override. The `models` pin in `families.json` is enforced before network calls and
when qualifying review logs, so another member of the same family cannot silently substitute.

A family is the first token of the model name (`families.py`: `claude-opus-5-5`
is `claude`, `deepseek-v4-pro` is `deepseek`, `gpt-6-astra` is `gpt`). Each family's review of a form
is its own log beside the others, never a replacement: the Claude logs keep
their plain names, and a run with another family writes

```
reviews/<year>/transcription/<form>.<family>.index.json   with <form>.<family>.rulings.json
reviews/<year>/render/<form>.<family>.index.json          with <form>.<family>.rulings.json
reviews/<year>/classm/<form>.<family>.index.json          with <form>.<family>.rulings.json
fixtures/<year>/classm.<family>.json                      that family's class M fixtures
```

A review is committed as records and an index (`review_store.py`; design
`docs/2026-11-09_review_store_design.md`, 2.2). Each pass (a whole-form review, or a line-scoped
pass) is one record, `reviews/store/<kind>/<record-sha>.md`, written once and never rewritten:
the pass's header or block, the sections of the lines it judged (each with its ruling as
`Ruling: open`), their gate rows and the raw reply; `record-sha` hashes kind, form, family,
scope, each scoped line's subject, the prompt and response hashes and the policies. The index
maps each compared line to `{key, record, status, ruling, subject_key}` (the subject key folds
the line subject and, for transcription, its foreign interfaces), with the line subjects, the
rest of the document (`__rest__`), the foreign interfaces, the whole-form record its header
comes from (`base`) and the header rows a later pass rewrote (`head_rows`). A rerun writes one
record and changes only the index; a ruling changes only the index. The per-form log is a view,
not committed: tools read it with `rulings.read_log` and write it with `rulings.write_log`
(which stores what is new and checks the view reproduces the log byte for byte), and
`python3 tools/transcription/review_store.py render [--kind K] [--form F]` writes the readable
views to `.transcription/logs/<year>/<kind>/<stem>.md` (git-ignored; a writer refreshes its
own). `review_store.py check` verifies every index's records.

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
{"required": ["claude"], "optional": ["deepseek", "gpt"],
 "active": {"claude": true, "deepseek": false, "gpt": false},
 "models": {"deepseek": "deepseek-flash", "gpt": "gpt-6-astra"}}
```

Only active families are checked as below; an inactive family's logs are history (above). Every required family must have a current log with no open ruling for every
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
current is marked stale. The report's summary line is printed when it is written.
`rerun_all.py --model <non-Claude>` (an active family, or an inactive one under the override)
runs every form that has a log of any family through that family, leaving the Claude logs as they are.

## Running

```
python3 tools/transcription/transcribe.py --form qdcg            # one model call
python3 tools/transcription/transcribe.py --form qdcg --dry-run  # excerpt and prompt only
python3 tools/transcription/transcribe.py --form qdcg --from-response   # re-compare the saved response
python3 tools/transcription/rerun_all.py --kinds transcription,render --resume   # the Claude family
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
each completed job. A model family's first usage-limit failure (an exhausted allowance or balance, not a
rate limit or timeout) stops `rerun_all.py` calling that family: calls in flight finish, later jobs of the
family are not run (a `--resume` reuse still runs; it makes no call), and the end of the run lists every
job the limit stopped with the command that reruns it. `--reasoning-effort low|high|max` is supported for DeepSeek
reviews (an inactive family: under the override only); it is recorded and checked on reuse. Class M rebuilds current jobs
even when reusing a response, so changed supplied amounts require fresh work.
`--max-output-tokens N` raises the DeepSeek allowance for reasoning plus the
final answer (default 65536; use 131072 for the largest documents); the request
timeout grows proportionally. The effective allowance is bound in receipts and
recorded in logs. A response ending because of length cannot be accepted, even
if its partial content happens to parse. Original bound receipts predating this
option retain their fixed 65536 allowance and cannot be relabeled as larger calls.

## New York (`--jurisdiction ny`)

Every review tool and check takes `--jurisdiction ny` (read by `tools/jurisdiction.py`; default
federal, whose paths, prompts and outputs it leaves as they are). In New York mode the tools review
the New York documents (`forms/ny/<year>/`: `ny_it201`, `ny_it2`, `ny_rs`, `ny_city_rs`, `ny_tcw`,
`ny_tcw_first`) against `sources/ny/<year>/`, write their logs under `reviews/ny/<year>/` and their
reports under `reports/ny/<year>/`, and read the rendering in `rendered/ny/<year>/`
(`node engine/dist/main.js render --ny`). Because a New York line copies federal lines, the tools
read across both trees: the manifest, the documents, tables and parameters of the catalog and
type checker are the federal ones and the New York ones. A New York request:

- opens with a short jurisdiction note (`jurisdiction.NY_NOTE`; the system prompt gains one
  sentence), the fixed wording after it unchanged;
- cites only New York pages for the document's own lines; a render or class M glossary entry of a
  federal line brings that line's own federal pages, as across federal forms;
- lists the New York year parameters (`ny.`) only;
- keeps the catalog source-selected. Of the federal return it lists the federal lines the New York
  text names (catalog reason `named lines: ...`): by form and line ("federal Form 1040, line 1z"), or
  by printed label (`federal_labelled`), since the New York form copies most federal amounts by their
  federal labels without naming the line. A label match is the whole label phrase, normalized (case,
  parentheses and punctuation dropped), from the line's printed label as printed on the federal form's
  own archived pages (its sentences, less "This is your" and instruction sentences such as "Add lines
  ..."; "Earned income credit (EIC)" also without "(EIC)"; "IRA distributions, taxable amount" also as
  "taxable amount of IRA distributions"); it counts only where the 50 words before it name the line's
  federal form or say "federal" (implying Form 1040 and its numbered schedules), not where the text
  qualifies it as New York's ("New York adjusted gross income", "city taxable income"), and not inside
  a longer phrase matched at the same place. A federal document is listed whole only where a line of
  the document cites its pages or the document instantiates a federal definition; a federal form the
  text names without naming a line, and the federal definitions, are not listed (a note after the
  catalog says so). A federal line the encoding reads that the text does not name stays out, and the
  input-context check (`input_context.py`) reports it. The IT-201 instructions are, like `i1040gi`, left
  out of the whole-text catalog selection;
- gives of the IT-201-I web edition (`ny_it201i-html`, archived as one page) only the sections its
  locators name by heading (`html_sections.py`): the heading's section, widened to the enclosing
  section where the locator quotes a phrase outside it, with the headings above it and their lead
  text; a locator naming no heading gives the whole page. Its citations are its tables and
  worksheets, the IT-201-I pages whose PDF text is out of reading order
  (`sources/ny/<year>/README.md`), and name no PDF page, so the web text is kept for them.

Class M runs `classm-jobs --ny`, which seeds its corpus from the New York fixtures; agreements go to
`fixtures/ny/<year>/classm.json`. The screen review covers input screens only, and every New York
refusal is gated by a computed gate over interview answers, so New York mode has no screens (the
gates are judged in the render review's glossary).

```
python3 tools/transcription/transcribe.py --jurisdiction ny --form ny_it201 --dry-run
python3 tools/transcription/rerun_all.py --jurisdiction ny --kinds transcription,render,classm
python3 tools/transcription/completeness_review.py --jurisdiction ny
python3 tools/transcription/check_logs.py --jurisdiction ny
```

Until a New York document's first review of a kind is run, it is listed in
`reviews/ny/<year>/pending.json` (`pending.py`): `check_logs.py`, `check_completeness.py` and
`check_screens.py` in New York mode report it as pending instead of failing. A listed document that
has a review fails the check until it is removed from the list, so the list only shrinks; deleting the
file makes the checks strict. `rerun_all.py --jurisdiction ny` runs the logged documents and the
pending ones.

## Gate reviews

A formal gate (`docs/2026-11-06_formal_gates_design.md`) is an input marked `gated_by: <gate line>` in the form
data, whose gate line is a `choose` of the same document taking the input when its guard holds and a parameter of the
input's type otherwise (zero, false or an enum value, which the review prompt states); the build checks the convention (`engine/src/gates.ts`). `gates.py` groups gate lines by the one line their
guards read, the gate's condition: an applicability or existence `Bool` the filer answers, or a condition computed
from earlier answers. Each group is one review unit, keyed `gate:<condition>`. Two standing reviews judge each unit
against the pages its lines cite, and both are logged by the unit's subject (`gates.subject`): the condition's line
and its wording as the filer reads it (the interview's prompt and help), each gate line and gated input with their
English and wording, citations included. The review prompt's own text and the archived page text are not part of the
subject, so a prompt change applies at each gate's next real change (`CLAUDE.md`, review what changed).

- **Screen review of gates** (`screen_review.py`, the same tool as the refusal screens, recorded in
  `reviews/<year>/screens/screen_review.json` with `kind: gate`): `NARROW`, a situation the cited text gives a gated
  line an amount in which the condition is false; `SOURCE`, a condition the cited text states that the gate does not
  match; `UNCLEAR`; and `WIDE`, reported but not changing the verdict, since gate wording leans to yes. The verdict
  is `COVERS` without a NARROW, SOURCE or UNCLEAR finding. `check_screens.py` reports a gate `stale` when its subject
  differs from the recorded `subject_sha`, `unruled` until a non-COVERS review is ruled in
  `reviews/<year>/screens/rulings.json` under `unruled:gate:<condition>` with the review's `prompt_sha`, and
  `orphan` when a recorded gate is gone.
- **False-no review** (`false_no_review.py`, kind `false_no` in the cost ledger): adversarial, "who would honestly
  answer no while a gated line is non-zero?". The prompt carries the patterns of the 43 findings of the T-251 review
  (`research/audits/2026-11-06_t251_ladder_review.md`): narrow time frames, narrow verbs ("sell", "paid"), a missing
  spouse, a document or one issuer for a fact, hierarchy leaks, lists read as complete, legal classifications asked
  before checkable facts, and amounts not perceived as the thing asked, each with its finding numbers. Findings carry
  `who`, `why_no`, the line, the IRS text, a severity (the T-251 scale) and a fix; the verdict is `SOUND` without a
  medium or high finding. Logged per form in `reviews/<year>/false_no/<form>.json` (the form of the condition), ruled
  in `reviews/<year>/false_no/rulings.json` under `unruled:<gate>` with the review's `prompt_sha`, and checked in
  `check-all` by `check_false_no.py` (`stale`, `unruled`, `rerun`, `orphan`; report
  `reports/<year>/false_no_currency.md`). Raw prompts and replies are under `.transcription/false_no/`.

```
python3 tools/transcription/screen_review.py --gates-only --dry-run      # prompts and estimated cost, no call
python3 tools/transcription/screen_review.py --screens gate:div.any      # one gate's screen review
python3 tools/transcription/false_no_review.py --dry-run                 # every gate, no call
python3 tools/transcription/false_no_review.py --gates gate:div.any [--from-response]
```

Both dry runs print each prompt's size and an estimated cost from a fit to the ledger's 17 Claude screen calls
(`screen_review.estimate_usd`: $0.048 a call plus $0.00295 per thousand prompt characters, each call within $0.03 of
it). Claude's price basis is the reported cost, so the estimate is for planning; the ledger records what was paid.
Both tools are tested offline in `test_review_tools.py` (`GateUnits`, `GateReviewRuns`): a stubbed model call, a
placeholder for the archived pages, and files in a temporary directory.

## Excerpt selection

The pages a form's citations name (`p. N`, `pp. N–M`), cut at the archived
text's page breaks; a whole document when it has six pages or fewer; and for
a locator that names a worksheet or an instruction line without a page, the
page whose heading starts a line. The log records which pages were used.

## Carrying reviews across a tax year

`year_carry.py`, run from the TY+1 tree with `--year <TY+1>` and `--from <TY tree>`, lists for each
transcription, render and class M review which compared lines carry to TY+1 and which need a review, and
with `--write` writes the carried entries into TY+1's indexes (same record, status and ruling, each marked
`carried: {from, year_key}`; a form's `__rest__` is set to TY+1's only when the document's own fields
carry). A line carries only when its year-carry key is equal in both years: its subject with foreign
interfaces, the values of the parameters, enums and tables its reach reads, the cited source text at
anchor-section granularity over its reach and the foreign lines it names (never only the quoted words; a
citation naming no page stands for its whole document), and the review tools' policy versions. Year
literals are normalized in lockstep: only where the year moved by exactly +1 between the two years'
texts, within ten years before the tax year; the project's own year is normalized only where its cited
source moved that year and kept it nowhere unchanged in the same context. So a fixed statutory date the
project wrongly incremented, a rolling year the project failed to move, and a birth-year cutoff all need
a review. The report lists every carried line for spot review and separates the lines that wait only on
a TY+1 source not yet archived or a TY+1 parameter not yet set. `--self-test` (in check-all) runs
near-miss pairs: a paragraph added under the same heading, a changed parameter value, an incremented
fixed date, a rolling year not moved, a moved birth year.

## Rulings

Before ruling, `triage.py` executes both sides of every open disagreement on the same
inputs (every fixture, generated returns and partial records withholding one answer of
the reviewed document) and writes `.transcription/triage/<year>/<stem>.json` (git-ignored, regenerated on
demand; New York under `.transcription/triage/ny/<year>/`) with comparison counts, difference kinds and
witnesses. A ruling written while a record of the reply it rules exists keeps a compact stamp of that line
(`triage`: verdict, kind names, witness ids, policy) in the rulings file. `--explain` rebuilds one witness and
prints both derivation trees. Every reply is read from the committed review log, so triage runs without the
git-ignored review data. Each section is evaluated against the reply that judged it: a section marked
`Reviewed in: pass <id>` against that pass's recorded reply (its receipt, when this checkout holds it, must
answer the block's prompt hash and equal the recorded reply; one it lacks is recorded as `receipt_verified:
false`), with the project's other computed lines spliced beside it as
`compare()` splices them for type validation (a scoped line the reply omits stays missing); every other
section against the whole-form reply. Each reply is evaluated in its own run; the record lists each pass
under `passes` and marks its lines with `pass`. Triage exits non-zero, naming the form, the handles, the
pass ids and the reason, when a pass reply cannot be found, parsed, or reconciled with its receipt.
A transcription rulings entry stores both expressions as `project_expr_sha256` and `second_expr_sha256` (the
sha256 of each expression's text as the log section embeds it; the text is in the log), and every entry
records the line's cross-document subject when it was ruled (`subject_key`, `carry.line_subject`). The method and ruling classes are in
`reviews/2025/transcription/adjudication/README.md`.

```
python3 tools/transcription/triage.py --form sd [--family deepseek]
python3 tools/transcription/triage.py --form sd --explain '<handle>' --witness 0
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
prompt also lists enumerations, year parameters, every refusal-gate input of
every form (the screening list, with each gate's form, printed marker, type
and question) and a catalog of other forms' and collections' ids, printed
markers and types. Computed labels and expressions are omitted from every
catalog, including exported helpers and collection fields. Input questions and
refusal-screen interfaces remain explicit shared assumptions.

The catalog is a subset chosen from the IRS source alone
(`catalog_selection` in transcribe.py; `source-only-computation-v3`). Another
form or collection is listed, whole, when:

- it is a shared definition (`tax_on_amount`, `tcw`, `se`, `aqee`): always;
- its own source pages (the pages its own review is given) share a page with
  the reviewed form's excerpt;
- the excerpt, or the whole archived document it is cut from, names an IRS
  form or schedule the other form belongs to ("Form 8962", "Schedule B"); a
  form belongs to the IRS forms whose documents it cites (fNNNN, or the form
  of its iNNNN instructions if it cites no form document);
- that text names the IRS worksheet the other form's title names ("Qualified
  Dividends and Capital Gain Tax Worksheet");
- that text names a form line ("Form 1040 or 1040-SR, line 2b", "line 17 of
  Schedule 1") the other form feeds: by its IRS title ("...Worksheet A—Line
  27a") or by an "enter ... on" sentence in its source pages or its own form
  documents.

The general Form 1040 instructions (`i1040gi`) count only by their excerpt
pages, since their whole text names every form. Nothing in the selection reads
the reviewed form's expressions, refusal lists or visibility conditions, so the
catalog does not show which foreign lines the project reads. The log's "Other
documents in the catalog" table records what was listed and why. Where the
project reads a line the rule does not reach, the required-interface check
(`input_context.assess`) reports it missing and the review cannot qualify;
the remedy is a source citation that reaches the naming page, not a
hand-picked catalog entry.
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

New logs record `checked-expression-types-v2`, `project-expression-types-v3` and a passing/failing
validation result. A type error reaches every line that reads that helper; even an unused invalid
helper fails the form's type check and gives tool exit 3. BUG-0132 extends dependency traversal to
count, proration, keyed-table and collection-field operands. Invalid expressions cannot agree by
canonicalization alone. Passing types does not establish source correctness or numeric evidence.

BUG-0130 supplies Count-literal syntax; BUG-0131 preserves complete input/refusal questions instead
of cutting off late meanings and exceptions. `required-review-interfaces-v2` checks the actual
request against every own input and direct foreign boundaries referenced by either the authored
form or the returned candidate (including helpers, collection fields, bindings and gates). The
fingerprint binds ids, printed markers, types and complete input wording. Unrelated foreign
questions do not invalidate it; omitting a dependency cannot shrink the required context. This
host-only assessment imports no foreign authored arithmetic and confers no numeric evidence.
The older global question diagnostic remains separately reported, with its original policy.
Neither check certifies which questions the interview may leave unasked; source-based availability
cases remain necessary for those regimes (BUG-0134/T-063).

Qualification rechecks the actual bound request/reply and live interface hash, including current
types. A recorded passing header alone cannot qualify a changed foreign interface. Original
policies remain visible in audits; no audit silently upgrades old request provenance. The global
BUG-0129 hold remains while migration and adjudication continue.

BUG-0144 versions the refusal checks. BUG-0145 removes authored input refusal gates from published
input stubs: only identity, type and question metadata are retained. Gates explicitly returned on
an input by the model are validated/interpreted as that model's declarations. Hidden authored
computed helpers cannot become prerequisites of an independent candidate. v1/v2 results remain
historical; current checking is v3.

`--from-response` now verifies the original log/request/reply/meta identity in addition to the
transport's exact current prompt/model/system match, and rejects unbound receipts. It archives
the parent log, sidecar and raw artifacts under `.transcription/archive/verified-replays/` with
hashes, then labels the derived log as a verified host replay with its parent hash and original
policies. No new model call or repaired response is claimed. A request with changed wording or a
mismatched receipt requires an actual fresh request. `rerun_all.py --resume` can fall back to a
fresh request; direct `transcribe.py --from-response` never does.

T-063 adds source-based partial-input cases under `input_contracts/<year>/`. The request
receives synthetic input facts and target ids only; host reference answers and rationale are
withheld. After expression checks pass, a separate fixed interpreter checks at most 32 cases
under a 30-second timeout and 256-MiB V8 old-space setting. It maps model-declared refusal ids to the evaluator's
object representation, validates that those gates are Bool, and imports no authored refusal
placement for computed model lines. Invalid IR is not evaluated. No candidate is installed in
the project forms or return runtime; no H/B/M/engine assertion or numeric fixture is created.

Logs bind the case-bank hash, policy, actual request inclusion and observed results into ruling
contexts. Both families must pass current applicable cases before qualification. An older reply
can be checked diagnostically without pretending its request contained the cases. The current
dependent bank covers ten source-derived age/timing records, including one genuinely unknown
answer; passing it is not a proof of all relationship or credit cases. See the bank README.

BUG-0135/T-064 distinguishes internal adapters from source-defined quantities. A ruling prefixed
`interface gap` records an unresolved semantic contract, blocks qualification and contributes no
model-error noise. It is not resolved by inventing a tax reading or forcing equivalence.

The first resolved adapter, `div.screen`, now has a separate host-only engineering
contract under `adapter_contracts/2025/`. Twenty-one cases check its zero/refusal/unknown
behavior and all sixteen worksheet copies. It is omitted from blind targets and explicitly
excluded from source agreement/noise counts, without modifying historical replies/rulings.
An adapter-only form makes no new model request and earns no empty passing source review.
Run `python3 tools/transcription/adapter_contracts.py`; check-all includes it. Its behavior
and answers stay out of source prompts and it earns no tax-evidence credit. Other opaque
helpers still require explicit classification; see `adapter_contracts/README.md`.

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
corpus; a return's branches are those of its routed evaluation, the answers the interview's route asks plus
those the requested lines read, the same answers the job keeps, T-206) and writes `.classm/jobs.json` with, per case, the whole-return
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

For collection forms with printed IRS outputs, fresh jobs request those outputs only
(`worked target scope: printed IRS lines`). The full candidate rules and helper-branch selection remain intact. Incoming values are
limited to the printed calculation and its local-expression dependencies; validation-only
derived totals are withheld rather than feeding the reviewed calculation back into its request. An HSA before/after
check preserves the same four cases, facts, incoming context and branches while reducing
requested values from 432 implementation fields to 90 printed outputs. Adding positive-distribution seeds
then expands to five cases/97 branches/105 printed outputs with no lost branch. Helpers remain
available to the evaluator and branch report, but their unrequested values earn no M
assertion. Helper-only records still need their semantic interfaces reviewed; this is
not a blanket exemption or a claim that roadmap item1.5 is finished for all old reviews.

Blank/skip replies are recorded as SKIPPED and earn no numeric fixture assertion,
including when the evaluator happens to produce zero. Explicit printed zero
remains an assertion. `audit_skipped.py` checks old logs against their embedded
raw replies; `--apply` removes only skipped expectations and archives originals
with hashes. The audit is an offline check-all step (BUG-0123).


`classm.py --case-jobs 4` issues independent case requests concurrently; the default is1.
`rerun_all.py` passes that option only to class M. Each case keeps its own prompt/response
receipt and the final log retains case order. Concurrency does not repair model values.

## Carrying rulings over (T-218)

`carry.py --kind K --form F [--family X] [--from git:REV|LOG|RULINGS.json|ARCHIVE_DIR] [--dry-run]` rules an open
section with an earlier ruling when the disagreement repeats exactly: same log, handle and status, the same content
(both expression trees for transcription; the restated English for render; the case and both values for class M),
and the line's transitive subject unchanged since the earlier log's commit. The subject follows references as the
evaluator resolves them: the lines it names (a definition's lines by their local ids, within the definition), the
named line of a definition instance, the own fields (roster parent and implicit entry) of a collection it sums over,
the tables it names and only the year parameters and enums it names; a string naming a whole document stands for all
of it. Each part is hashed as the review kind sees it: citations left out, and for transcription and class M the
wording (label, help, note, display, ambiguity link) as well; an input's question is kept. By default every committed
version of the log is searched, newest first, each with the forms of its commit: the newest settled ruling on the
same disagreement whose line was then as it is now carries, and a newer finding, defect or unsettled ruling on the
same disagreement stops the search. It never carries a finding, defect, correction, interface gap or
unclassified ruling, and it labels what it carries ("(carried over from <source>, review of <date>)"), so every
carried ruling is auditable. `rerun_all.py` runs it after each review with open disagreements (`--no-carry` turns it
off). Measured precision against hand rulings: 50 of 50 on the 2026-11-03 refresh round, 39 of 43 on the backlog
round; it removes a small share of open handles (about 7%), because most repeats on an unchanged line come with a
different model reply.

Before carrying, `carry.py` rules mechanically (T-224) every open transcription disagreement whose second side
records `invalid_model_types`: the reply fails the host's schema, type or reference validation on the line or a line
it reads, so by the adjudication method (`reviews/<year>/transcription/adjudication/README.md`, "model error") it is a
model error on the declaration and the line was not executed. The ruling reads "Ruling: model error on the
declaration, ruled mechanically: ..." and quotes each validation message; it needs no earlier ruling. Measured over
the committed sidecars before the change: 917 of 5,102 transcription rulings (18%; DeepSeek 871 of 2,643) were on
such sections, and 914 of them were ruled model error by hand (the other three added an interface gap, an ambiguity
or a scope note to the model error); in the current logs 136 of 1,445 ruled sections, all model error (scveh's
DeepSeek log: 20 of 21). A reply that only omits a `shown_when` the project has is not ruled mechanically: under the
v3 prompt such sections were ruled model error 12 times of 26 (the rest scope, representation or interface gap),
because whether the source conditions the line's display is a source reading.

## Ruling stamps (T-223)

`rule.py` stamps every sidecar entry it writes (`rulings.STAMPS`): `date` (the day it was ruled), `run` (the
identity of the reply the section records: `transcribe.response_sha256`, the hash of the reply as the log embeds it,
taken from the log itself, the pass's raw reply for a line-scoped section, the case's raw reply for class M) and, for a
finding (or a ruling headed "defect"), `severity` (`high`, `medium` or `low`; rule.py refuses a finding without
one: `{"<printed>": {"ruling": "Ruling: finding; ...", "severity": "medium"}}`). Every ledger line records
`prompt_sha256` and, for a call that returned text, `response_sha256`, so `costs.py --yield` joins a stamped ruling to
the call that bought it exactly (the exact-join table) instead of by git window. Entries written before stamping are
not backfilled: their ruling date is not recorded anywhere (a commit date is later than the ruling), and the ledger
lines of their calls carry no reply identity, so a backfilled `run` would join nothing. `rulings.py --check` fails a
malformed stamp. Completeness and screen rulings (hand-written JSON) are not stamped.

## Line-scoped reviews (T-219)

`transcribe.py --form F --lines <ids|auto>` and `render_compare.py --form F --lines <ids|auto>` review only the named
lines (a compared line; any line of the form, meaning the compared lines that read it; a line of another form,
meaning this form's lines reading it; or `auto`, the lines whose subject changed) and merge the result into the
existing log of that family as a `#### Pass <prompt sha>` block under `## Line-scoped reviews`. The scoped prompt
carries the target lines, every other printed computed line by id, marker and type (and, for one with a `shown_when`, the
line id of its display condition, with a note that the line's amount is computed whether or not it is shown), all inputs, the excerpt the
targets and their helpers and inputs cite, and the source-derived catalog for those pages only
(`source-only-computation-v3+lines-v3`; logs recorded under `+lines-v1` and `+lines-v2` stay independent), narrowed as a New York catalog is: a form the excerpt names only as a form
("Form 1040") is listed whole only where the scoped lines' own citations name it; otherwise its input lines and the
lines the excerpt names by form and line are listed (reason `named form, inputs and named lines: ...`), and a
collection named only as a form only by its named lines. Definitions, shared pages, worksheets, named lines (a form feeding a line the excerpt names) and the
screening list are as in a whole review. Each log records a
`## Line subjects` table; `check_logs.py` names exactly the stale lines and suggests `--lines auto`. Owner decision
2026-11-04: a log goes stale only for the lines whose subject changed (a line no compared line reaches does not stale
it). Forms with partial-input banks (dependent, f8889) are reviewed whole. `rerun_all.py` runs the transcription and
render reviews this way by default, and refuses reruns of current logs and runs above a cost gate (tools/README.md,
"Review rerun guards").
When `--lines auto` finds every compared line current in a log written before line-subject tables existed (a whole
subject that changed only outside every line subject), it records the table it verified against the reviewed version
and makes no model call, so `check_logs.py` holds the log current by its lines.

A transcription line subject leaves out wording: the `label`, `help`, `note`, `display` and `ambiguity` fields of a line
and of the document (`subjects.WORDING`), which the request does not carry and the comparison does not read; an input's question
(`expr.source`) and the document's title, which the request carries, stay in. A wording edit therefore stales no
transcription log that has a line-subject table (the render and completeness reviews judge wording); the log's header
subject still records the whole definition it reviewed. `migrate_line_subjects.py [--jurisdiction ny] [--dry-run]`
rewrites each log's table to these subjects of the version the log reviewed, found by its recorded hashes in the
working tree or git history, and gives a log reviewed whole without a table the table of its reviewed version; no
model call, idempotent. It writes a log only when the log's state (stale or current) is unchanged, so a stale log stays
stale; a log it would turn current is named and left for `--lines auto`.

A merged log earns second-family credit only when every review in it qualifies (T-226). `compare_families.py` holds
a log with passes or a line-subject table current by its line subjects (`subjects.log_state`, as `check_logs.py` does) instead of its header's
subject, and applies the header's conditions to each pass's own record: the named family and selected model,
`source-only-computation-v3+lines-v1`, the current comparison, type-validation and input-context policies with
passing results. `audit_transcription.py` verifies the header review against its receipt (subject check replaced by
the line-subject check) and comparing it again only on the sections it still holds, and each pass against the receipt
it names: the prompt hash, the embedded reply, bound request metadata, and the reply compared again on the pass's
scope with current type and input-context checks, whose fingerprint must equal the pass's.

A transcription log also records a `## Foreign interfaces` table (T-227): per compared line, the hash of the
interfaces (id, document, printed marker, type, input question) of other documents' lines its reach names, which the
request carries. A rewording of such a question (`person.blind`, read by `sa`) stales exactly the lines whose row
changed (`check_logs.py`, `--lines auto`). A whole review writes every row; a line-scoped review rewrites the rows
of the lines it judged and keeps the others. A log, or a line, without a row is not checked, so the check applies
from each log's next review on and no existing log went stale when it was added.
