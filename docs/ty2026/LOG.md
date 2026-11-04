# TY2026 preparation log

## 2026-11-04, cloud session (branch `ty2026/prep`)

Brief: `docs/ty2026/2026-11-04_ty2026_cloud_brief.md`. All six steps done; the branch is pushed. `main`,
`years.json` (`[2025]`) and the 2025 encoding are unchanged. At the start and at the end, `node engine/dist/main.js
build` passed and `test-fixtures` passed 1637/1637. `python3 tools/fetch_sources.py` verifies 158 (2025) and
`--year 2026` 91 archived documents. No paid model calls; no review tool under `tools/transcription/` was run.

| Commit | Step |
|---|---|
| a860627 | the brief |
| e02c421 | 1. Archive refresh: all 57 rehearsal drafts unchanged; 8 replaced by final 2026 editions; 3 new drafts (Pubs 503, 575, 590-B); 6 new final editions (W-2, 1099-R, 1098-T and instructions, Pubs 15 and 505); 13 continuous-use revisions; 9 final guidance documents (Rev. Procs. 2025-32, 2025-19, 2025-25, 2026-15; Notices 2025-67, 2026-10; IRB 2026-29; the 2025 HHS poverty guidelines; Public Law 119-21). Record: `reports/2026/archive_refresh_2026-11-04.md` |
| b3b70ab | 2. Year diff regenerated (2,236 of 3,703 items on the worklist); split into 426 kind-(a) and 1,810 kind-(b) items (`reports/2026/worklist_split.md`) |
| d58ca90 | 3. Change map, `research/ty2026/changes.md` (133 entries), and its verification; the Schedule 3-A and Form 1062 drafts archived |
| 55bb53f | 4. Proposed parameters (92 final, 70 draft, 109 without a 2026 source) |
| 98a97de | 5. Proposed definitions for Form 1040, Schedule A, Form W-2 and Schedule 3-A; 16 source-predicted cases |
| (this commit) | 6. `docs/ty2026/ADOPTION.md` and this log |

**Most important findings** (details and quotes in `changes.md`): Form 1040 adds line 12f (charitable deduction for
non-itemizers), lines 24b–24c (Form 1062) and 32b–32c (new Schedule 3-A, "Federal Public Benefit"), and exchanges
13a and 13b. Schedule A has the $40,400 SALT limit, mortgage insurance premiums, the 0.5% charitable floor worksheet,
gambling losses at 90%, and the 2/37 itemized-deduction limit. Schedules 1-A and 2 are renumbered; tips and overtime
come from new W-2 box 12 codes TP and TT. Form 5695 is carryforward only. Form 8962 loses the repayment limitation and
the credit above 400%. The education credits require an SSN. The mileage rate is two rates (72.5 and 76 cents).

**Environment.** The session's setup script failed (`npm ci` ran outside the repository). The Default environment's
script was corrected, and a personal `us-tax-model` environment was created with network access to www.irs.gov and
www.govinfo.gov (needed for step 1) and the corrected setup script. That script is unproven until a fresh session
starts on it.

**Cost.** No dollar cost was shown in this environment. Five Opus subagents ran (four change-map sections and one
verification): 1,634,268 subagent tokens in all, logged in `research/costs/agent_runs.jsonl` with `cost_usd: null`.
The main session's own usage was not shown.

**Next.** Nothing until the IRS posts the final 2026 documents (the Form 1040 instructions first). Then follow
`docs/ty2026/ADOPTION.md` on the owner's machine, beginning with the owner's questions at its end. Optional before
then, if the owner wants it: draft patches for the non-priority forms in the order the plan lists, and a full read of
Public Law 119-21's 2026 provisions (question 6).
