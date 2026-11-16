# Screen and false-no adjudication, xrr rinv family (2026-11-16, release rerun after the xint integration)

Family `rinv`: forms `sb`, `div`, `interest`, `sd`, `qdcg`, `qdcg_amount`, `f4952`, `f8960`, `clcw`, `clcw_next_year`, `ftc`,
`f1116`, `f1116col`, `f1116sb`, `f1116sbyr`, `gift`, `sales` and `tax_on_amount`, tax year 2025, us. One fork,
claude-opus-5-5, judgment.

## Counts

| Tool | Samples listed | Already ruled at the current subject | Ruled here | Due or short |
|---|---|---|---|---|
| screens | 29 | 29 | 0 | 0 |
| false_no | 22 | 22 | 0 | 0 |

Every screen and false-no sample in the work list (`/tmp/xrr/units/rinv.json`) already carries a ruling at its unit's
current `subject_sha`, so this round has nothing to rule for these two tools. The fragments
`/tmp/xrr/frag/rinv.screens.json` and `/tmp/xrr/frag/rinv.false_no.json` are empty objects; `xrr.py merge` (no `--write`)
reports 0 to merge and no refusal for them. No defect was found and no pending bug was filed.
