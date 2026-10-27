# Source adjudication of transcription disagreements

Method for ruling the open disagreements in `reviews/2025/transcription/<form>[.<family>].md`, under
`docs/2026-10-26_plan_revision.md` item A. Each adjudicated log has a summary here,
`<form>[.<family>].md`, listing every ruling with its class and evidence. The rulings themselves are
written into the log and its sidecar by `tools/transcription/rule.py`.

## Evidence

1. **The archived source.** `sources/2025/<doc>.cols.txt`, pages separated by form feeds (page N
   is the Nth page). The pages a review was given are listed in the log's "Source pages" table.
   A ruling quotes the sentence that decides it, with document and page.
2. **Executable triage.** `tools/transcription/triage.py` evaluates the project's line and the
   model's validated candidate on every fixture case, 500 generated returns (seed 20261026) and
   partial records that withhold one answer the reviewed document asks. Records are in
   `triage/<stem>.json`; policy `executable-triage-v2` compares what the values sheet shows, so a
   project line hidden by `shown_when` agrees with a candidate's zero. Agreement there is observed equivalence on that sample, not proof.
   `triage.py --form F [--family deepseek] --explain <handle> --witness N` rebuilds a recorded
   witness and prints both derivation trees and the inputs read.
3. **Project records.** The form YAML and its citations, `forms/2025/scope.yaml`, the ambiguity
   register `ambiguities/2025.yaml` and earlier rulings in the sidecars.
4. **Secondary interpretation**, only where the source leaves a reading doubtful, recorded under
   `research/secondary/` in the format of its README. It is soft evidence and is disclosed in the
   ruling; it never substitutes for the primary quotation.

## Difference kinds reported by triage

| kind | meaning |
| --- | --- |
| value | both sides give a value and the values differ |
| project-refuses / candidate-refuses | one side refuses the return, the other computes |
| project-unknown / candidate-unknown | one side needs an answer that was not supplied, the other gives a value |
| candidate-shows-skipped | the project hides the line (`shown_when` false) and the candidate shows a nonzero amount (v2) |

## Classes

A ruling begins with its class; `compare_families.py` reads the prefix.

- **representation** — the two lines compute the same tax quantity on every return the interview
  can produce. Either triage found no difference, or every difference is on records the interview
  cannot produce (for example an answer supplied that the interview never asks), and the ruling
  says why. Representation also covers differences in an intermediate quantity that cannot reach any
  printed amount, shown by the derivation.
- **scope** — the only differences are refusals. A project refusal is acceptable when its gate is a
  cited scope screen. A candidate refusal where the project computes needs a check: if the source
  names a condition the project neither screens nor computes correctly, the ruling is a finding.
- **model error** — the candidate contradicts the source: a wrong value, or an answer required
  that the source does not need to determine the result. A line whose candidate expression, or a
  line or refusal declaration it depends on, fails schema, type or reference validation is a model
  error on that failure; the ruling says it adjudicates the declaration, not the tax reading. Other
  lines of the same reply are still ruled on their merits by reading the expressions against the
  source; triage cannot execute a reply with any validation error, and the ruling says so.
- **finding** — the project contradicts the source on a reachable return, or defaults an answer the
  source needs. Findings get a BUG entry, a fix and a source-backed regression.
- **ambiguity** — the difference is a reading recorded in the ambiguity register (cite its id) or an
  owner's ruling.
- **interface gap** — the candidate could not express the source reading because the published
  interface lacks something it needs, or the pages given to the reviewer omit the text that decides
  the line (a coverage gap of the review, not noise).

A line the source says to skip, or a line of a worksheet the filer never reaches because an
earlier instruction says STOP, must not show an amount on a reachable return. A nonzero amount
shown there is a defect of the side that produces it (a finding for the project, a model error for
the candidate), even when no later amount changes. The project meets this by hiding the line with
`shown_when` (owner's decision, 2026-10-26) or, where a later line reads it as blank, by entering
zero. A hidden line's internal value is not a difference. Boolean flow predicates are shown even
when their printed line is skipped (the documented convention, for example `forms/2025/sd.yaml`),
so the rule does not apply to them.

A line with several difference kinds is ruled on each of them. The ruling names the triage record
(`executable-triage-v1`, comparison counts, witness sources) beside the source quotation.
