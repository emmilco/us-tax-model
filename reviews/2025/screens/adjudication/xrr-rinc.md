# Screen and false-no adjudication, xrr family rinc (2026-11-16)

Brief: `/tmp/xrr/brief.rinc.md` (lane xrr, release rerun after the xint integration, B1 plus expansion tree
`.claude/worktrees/xint`). Family `rinc`: forms `s1`, `sa`, `oi8z`, `w2`, `tipjob`, `otjob`, `f4137`, `f4137row`, `f8919`,
`f8919firm`, `scope`, `f1040`, `refund`, `s2`, `rec`, `g28`, `tcw`, `s1a`, `ltc`, `mq`, `sdtw`. Of the family's 57 screen and 58
false-no items, one was unruled: the screen of `sa.excluded_income` (subject `8ed816d1e4fe`), changed since xrel because
`ftc.needs1116` now reads it. Every false-no item already carried a ruling, so `/tmp/xrr/frag/rinc.false_no.json` is empty.
The ruling is in `/tmp/xrr/frag/rinc.screens.json`; `xrr.py merge` (no `--write`) refuses none. The finding was checked
against the interview prompt and help (`interview/2025/questions.yaml`) and the archived source (`sources/2025/i2555.txt`);
the earlier ruling (the Puerto Rico year-of-move case, BUG-0458) was a lead only.

## Counts

Screens: 1 sample, 2 findings: defect 1, presentation 1.

False-no: no unruled samples.

## Defects (pending entries in `bug_pending/`)

| id | severity | title |
| --- | --- | --- |
| BUG-0924 | low | sa.excluded_income: the help steers a filer excluding 2024 foreign pay received in 2025 to answer No |

## sa.excluded_income#1 (NARROW, 2 findings)

| n | Kind | Class | Ruling |
|---|---|---|---|
| 0 | NARROW | defect (BUG-0924) | i2555 p. 3, "Income earned in prior year": pay received in 2025 for work done abroad in 2024 can be excluded on a 2025 Form 2555. The prompt asks about living or working abroad in 2025, and the help says a filer who lived in the 50 states all year answers No. Entered as shown on the W-2, the return is right without the elective exclusion, which is forgone silently; a filer who leaves the pay out on their own gets zero add-backs and the EIC. Proposed fix: widen the prompt to pay received in 2025 for work done abroad in 2024 and narrow the help sentence. |
| 1 | UNCLEAR | presentation | A District of Columbia resident plainly answers No: the prompt names only abroad, Puerto Rico and American Samoa. The help's "50 states" sentence is a shortcut; the proposed fix of BUG-0924 adds the District of Columbia. |
