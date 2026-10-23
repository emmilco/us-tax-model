# Transcription agreement

The data-layer counterpart of the engine differential (spec 6.5): every
worksheet is transcribed a second time by a model that sees only the archived
IRS pages the project's own citations name, plus the data model, and the two
transcriptions are compared line by line. Agreement is evidence that the
operand structure follows the text; a disagreement is adjudicated by the
agent reading the source page, with the quote and page recorded in the
ruling. No human reading is claimed (spec 3, requirement 11). Nothing here writes to
`forms/`; a transcription defect becomes an ordinary fix with a bug inventory
entry.

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
stem, so `--from-response --model deepseek-v4-pro` re-reads that family's
saved response. A second family's class M fixture cases carry the family as a
suffix on the case id (`classm.qdcg.1.deepseek`) so no two families' cases
share an id; their `evidence_note` records the model, which is how the
evidence report counts second-family M assertions.

`families.json` lists the families `check_logs.py` expects:

```json
{"required": ["claude"], "optional": ["deepseek"]}
```

Every required family must have a current log with no open ruling for every
form (`check-all` fails otherwise). An optional family's logs may be missing;
those present are held to the same snapshot and subject checks, and their
open rulings are counted and printed without failing the run, so a second
family's disagreements can stand open while the owner rules them. A log whose
family is in neither list fails. Counts are printed per kind and family. The
owner moves a family to `required` once every form has its log.

### Agreement floor and independence yield

```
python3 tools/transcription/compare_families.py      # offline; writes reports/<year>/second_family.md
```

For every form with a Claude log and a second family's log of the same kind,
the lines judged by both are compared and three things reported, per form and
overall, in `reports/<year>/second_family.md`:

- the **agreement floor**: the share of lines on which the two families'
  verdicts agree and neither disputes the project (transcription and class M:
  both AGREE; render: both MATCH), marked pass or below against the integrity
  plan's provisional 90% floor (item 1.3). A run below the floor does not count
  as a second-family assertion; the plan's answer is a stronger model, not a
  lower floor. A denominator of a few lines is marked as such.
- the **independence yield**: lines the second family disputed where the
  Claude log agreed or matched, each with the second family's reason. Zero is
  a visible result.
- the lines **both** families disputed, and the lines only the Claude run
  disputed.

Lines one log judged and the other did not (MISSING, or absent from one log)
are left out of the floor and counted; a log whose subject hash is no longer
current is marked stale. `check_logs.py` prints the report's summary line when
the report exists. `rerun_all.py --model <non-Claude>` runs every form that has
a log of any family through that family, leaving the Claude logs as they are.

## Running

```
python3 tools/transcription/transcribe.py --form qdcg            # one model call
python3 tools/transcription/transcribe.py --form qdcg --dry-run  # excerpt and prompt only
python3 tools/transcription/transcribe.py --form qdcg --from-response   # re-compare the saved response
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
the committed artifact is the log.

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
ambiguity register entry). Re-comparing a saved response keeps every ruling
whose disagreement is unchanged.

## What is compared

Printed computed lines, matched by printed number. In addition, helper lines
that other forms read (for example `qbi.deduction`, `ftc.credit`, the
per-person W-2 totals) and the result lines of the shared definitions
(`tax_on_amount.tax`, `tcw.tax`) are listed in the prompt by id and compared
by id after full expansion, since no printed line exposes their logic. The
prompt also lists the collections with their entry fields, the enumerations
with their permitted values, the year parameters, and every other form's
lines including helpers, so the second transcriber can reference what exists
instead of inventing it.

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

