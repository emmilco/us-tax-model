# Transcription agreement

The data-layer counterpart of the engine differential (spec 6.5): every
worksheet is transcribed a second time by a model that sees only the archived
IRS pages the project's own citations name, plus the data model, and the two
transcriptions are compared line by line. Agreement is evidence that the
operand structure follows the text; a disagreement is adjudicated by a person
reading the source page, and the ruling is recorded. Nothing here writes to
`forms/`; a transcription defect becomes an ordinary fix with a bug inventory
entry.

## Isolation

Fixed-prompt, curated input, unattended, non-secret, no credential beyond the
CLI's own: `claude -p --setting-sources "" --tools "" --no-session-persistence
--permission-prompts none --model <pinned>`, system prompt task-only. The tool
list in the init event is empty and a request to read a file is refused;
verified before the first run. Output is parsed as YAML and compared; it drives
no write path.

## Running

```
python3 tools/transcription/transcribe.py --form qdcg            # one model call
python3 tools/transcription/transcribe.py --form qdcg --dry-run  # excerpt and prompt only
python3 tools/transcription/transcribe.py --form qdcg --from-response   # re-compare the saved response
```

This is a deliberate network step like the source fetcher; it is not run by
`check-all`. `check_logs.py` runs in `check-all` and fails on an open ruling
or a log made against a different source snapshot. Until every form has a log
it reports the missing ones and is allowed to pass
(`TRANSCRIPTION_LOGS_OPTIONAL=1` in `package.json`); that allowance goes away
when the stage's done-condition is met.

Raw prompts and responses are kept under the git-ignored `.transcription/`;
the committed artifact is the log.

## Excerpt selection

The pages a form's citations name (`p. N`, `pp. N–M`), cut at the archived
text's page breaks; a whole document when it has six pages or fewer; and for
a locator that names a worksheet or an instruction line without a page, the
page whose heading starts a line. The log records which pages were used.

## Comparison

Each printed line of both transcriptions is expanded into a tree over inputs,
parameters, constants and references outside the form, so helper naming on
either side does not matter. Shared parameterised definitions are inlined with
their bindings; another form's helper lines are expanded in place; guards are
normalised (`X == true` is `X`, negation pushed through `all`/`any`,
comparisons oriented one way, a zero test on a non-negative line read as a
bound); literal-valued parameters compare as constants. Lines agree when the
canonical trees are equal.

Representational differences the comparison cannot see through remain as
disagreements and get a ruling: typically a value the project derives from
another form where the second transcriber asked a question, or a line the
project pins to zero because the spec refuses that part of the return.
