# The owner's verdicts on the interview's questions

`verdicts.json` is written by the vetting page (`/vet` of `node engine/dist/main.js serve`;
`interview/README.md`, "Vetting the questions"), one change at a time. It holds the owner's
judgment of each question the interview asks: on target (thumbs up) or not (thumbs down),
with a note. `node engine/dist/main.js vetting-report --write` lists it as
`reports/2025/owner_vetting.md`.

```json
{
  "records": {
    "f1040.status": {
      "changed": "2025-01-31T14:03:22Z",
      "digest": "<SHA-256 of judged, as JSON with sorted keys>",
      "judged": {
        "help": "<the help as the question bank stored it>",
        "options": [
          { "label": "<an answer offered, as labelled>", "value": "<the value it saves>" }
        ],
        "prompt": "<the question as the question bank stored it>",
        "type": "Enum"
      },
      "note": "<the owner's note, or an empty string>",
      "verdict": "down"
    }
  },
  "tax_year": 2025,
  "version": 1
}
```

- `records` has one record per question id (the input key, without entry keys). A question
  with no verdict and no note has no record.
- `verdict` is `up`, `down` or `none` (a note without a verdict).
- `changed` is when the verdict or the note last changed, in UTC.
- `judged` is exactly what the verdict was given on: the stored prompt (a form line's label
  where the bank gives no wording of its own), the help, the answer type and the answers
  offered in the order shown (`null` where the filer types the answer or it is Yes or No).
  `digest` is its digest. A verdict ties the record to the wording shown when it was given; a
  note changed later does not move it.

A record whose `digest` is not the digest of the question as stored today is **stale**: it
was given on earlier wording, and is shown and reported as such, never as a verdict on
today's question. A record whose id the interview no longer asks is kept. The server never
removes either.

The file is written with sorted keys, a two-space indent and a trailing newline, through a
temporary file renamed into place, so a diff of a vetting session shows the records that
changed and a crash cannot leave half a file. The server refuses to read or replace a file
whose records do not have this form, or whose `digest` is not that of its `judged` (a file
edited by hand must keep the two in step).
