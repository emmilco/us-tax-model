# Human source-reading logs

`reviews/<year>/human/<form>.md` hold the human source readings: a named person's verdict, line by line,
on whether the encoded rule matches the archived IRS pages, with the reason in the reader's own words. They
are H evidence in the evidence report, distinct from class B (human worked values). Human readings are
optional (`docs/2026-10-24_validation_policy.md`).

The reading packets that produced these logs, with their own renderer of the canonical data as English and
their local server, are retired. The logs are kept as they were written; nothing rewrites them.

## What the log records

A header table (date, reader, items, receipt format, lines judged, the verdict counts), the source pages read
(document, revision, pages, text sha256, cols sha256), then per line its printed number and id, the IRS
label, the English that was read, the citation, the pages, the helpers folded into it, the reading-list item,
its `Review sha256` receipt, and the reader's verdict (MATCH, MISMATCH or UNCLEAR) and reason verbatim.

## Validation

`logs.py` is the validation `tools/transcription/check_logs.py` and the evidence report
(`node engine/dist/main.js evidence`) share. Both fail on a record problem: a reader who is not a named
person (empty, or a name that looks like a model's), a log with no line records, duplicate or malformed
records, and a committed log whose last commit's author is not its reader.

H credit needs a current receipt, a MATCH with a reason, and the log's exact contents committed by the named
reader. A receipt is current only if the reading tool, run on today's data, would issue the same hash; no
tool issues receipts now, so no line earns H. Every record is listed as pending in both outputs, with its
verdict where it is not MATCH (the finding is kept for investigation) and a note where the reason is missing
or the log is not committed as it stands. Engineering responses to the readings are in
`reviews/<year>/human_findings.md`.

`python3 tools/human_review/test_logs.py` (a self-test of check-all) tests this on copies of the logs with a
synthetic reader, in a temporary repository: committed logs pass with every reading pending and H 0 in the
evidence report; a wrong commit author or a duplicate record fails the report; a model as reader, an empty
reader and a log with no records are problems; a log edited after its commit is pending.
