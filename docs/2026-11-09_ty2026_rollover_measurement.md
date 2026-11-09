# TY2026 rollover measurement (T-256 phase 0)

Read-only measurement at `8191c947` (2026-11-09) of what moving the project from tax year 2025 to 2026 has cost
so far and what the rest of it will cost, so the consolidation charter can target what makes a year rollover
expensive. Written by a judgment-class agent (claude-opus-5-5). No paid calls. Nothing in the repository was
changed except this file. The adoption experiments in section 6 ran in a scratch copy
(`/tmp/ty26/scratch`, an rsync of this worktree without `.git`).

**Labels.** **[M]** means measured, and the command or file is given beside the number. **[E]** means estimated,
and the basis is stated. **[T]** means testimony: a number quoted from a project document and not re-measured
here. Git numbers come from `git log --numstat` saved to `/tmp/ty26/*.txt` and classified by path with
`/tmp/ty26/classify.py`. The path classes are:

- authored: `forms/`, `params/`, `tables/`, `interview/`, `ambiguities/`, `schema/`, `years.json`;
- authored-proposed: `research/ty2026/forms-proposed/`, `research/ty2026/params-2026*`;
- derived: `fixtures/`, `reviews/`, `reports/`, `rendered/`;
- tooling: `tools/`, `engine/`, `lean/`, `ui/`;
- sources: `sources/` and `tools/sources-*.json`;
- research: other `research/` files;
- docs: everything else.

## 0. The premise, checked

The brief calls the work of 11-04 "the move to tax year 2026". **There was no move.**

- `years.json` is `[2025]` [M: `cat years.json`].
- None of `forms/2026`, `params/2026.yaml`, `tables/2026`, `fixtures/2026` or `reviews/2026` exists [M: `ls forms params
  tables fixtures reviews`].
- The 11-04 work was a *preparation* on IRS drafts. It produced proposals under `research/ty2026/` that the build does
  not read.

So the real rollover has not happened yet. The evidence for its cost comes from three episodes:

| Episode | Commits | Date | What it was |
|---|---|---|---|
| A. Year plumbing (T-045) | `402dff21`, `ef53cb0a`, `3f022b7d`, `94ff90f3`, `b2b79b16` | 10-20 21:55 to 10-21 14:56 | `--year` everywhere; citation check and relocation; one question bank; `year_diff.py`; `fixtures_year.py` |
| B. Rehearsal on drafts | `713a5662`, plus tool fixes in `6cae6818` | 10-27 09:13 and 11:49 | full `--adopt` on 57 drafts in a worktree, not committed; tool defects F1 to F6 and O1 to O7 |
| C. Preparation | `a860627a`..`9a96214b` on `origin/ty2026/prep`, squashed into main as `d6017626` | 11-04 20:11Z to 23:08Z | archive refresh, year diff, change map, proposed parameters and definitions, owner decisions |

A fourth measurement was added here (section 6): the mechanical part of an adoption, rerun today on the current tree
in a scratch copy.

The measured cost of a year rollover is therefore the cost of B and C plus a projection. It is not a closed account.

## 1. What changed, by kind

### 1.1 Episode C, the preparation (`d6017626`, 200 files)

[M: `git show --numstat d6017626`, classified]

| Kind | Files | Lines + / − | What |
|---|---:|---:|---|
| sources | 171 | +76,206 / −6,791 (42 binary) | 91 documents in `sources/2026/` (55 drafts); `tools/sources-2026.json` +211/−32 |
| authored-proposed | 11 | +8,657 / 0 | 4 full copies of 2025 forms plus `s3a.yaml`; 4 `.diff` files; `params-2026.proposed.yaml` (2,294 lines) |
| derived | 4 | +10,275 / −5,787 | `reports/2026/year_diff_from_2025.md` (+9,456/−5,782), `worklist_split.md`, archive-refresh record |
| fixtures-proposed | 1 | +438 | `2026-predicted.json`, 22 cases |
| research | 9 | +66,192 | `worklist.json` 62,761 lines; `changes.md` 2,456; `changes.verification.md` 107; 4 one-off scripts, 565 lines |
| docs | 4 | +244 / −1 | brief, ADOPTION, LOG, TASKS |
| **authored (the build's data)** | **0** | **0** | nothing adopted |

The real authored delta is in the `.diff` files [M: `grep -c '^+[^+]'` and `'^-[^-]'` on each]:

| Form | + | − |
|---|---:|---:|
| `f1040` | 181 | 32 |
| `sa` | 125 | 28 |
| `scveh` | 97 | 16 |
| `w2` | 25 | 1 |
| `s3a.yaml` (new form) | 163 | |
| **Total** | **591** | **77** |

These five forms are 5 of the 62 federal forms [M: `ls forms/2025 | wc -l` counts 62 yaml files]. Inside those
diffs, the new inputs are `w2.box12_tp`, `w2.box12_tt`, `f1040.form1062`, `scveh.miles_business_h1` and `_h2` (one
removed), and one in `s3a` [M: `grep 'op: input'` in the diffs].

Parameters, from `params-2026.proposed.yaml`:

- 273 values [M: `yaml.safe_load`];
- 45 carried by the auto-match "2025 quote printed unchanged" [M: `grep -c`];
- 108 with `source: none` [M];
- 70 with `source: draft` [M];
- 3 new [M];
- the rest read by hand into the `V` table of `research/ty2026/build_params.py`, which says: "The values below were
  read from the cited pages by hand".

### 1.2 Episodes A and B: tooling

[M: numstat per commit]

| Commit | Tooling files | Tooling lines + / − | Other |
|---|---:|---:|---|
| `402dff21` `--year` as one setting | 47 | +466 / −251 | |
| `ef53cb0a` citations checked and relocation | 4 | +598 / −1 | 28 authored files (+116/−124): citations re-anchored |
| `3f022b7d` one question bank | 1 | +51 / −33 | authored +1,706 / −7,315 |
| `94ff90f3` year diff | 4 | +554 / −12 | 230 files of `sources/2024` |
| `b2b79b16` fixtures across years | 8 | +296 / −7 | |
| **T-045 total** | | **+1,965 / −304** | |
| `713a5662` rehearsal | 5 | +334 / −41 | 230 source files (57 drafts); 9 derived reports, +19,685 |
| `6cae6818`, the O1 to O7 share | 12 | +593 / −129 [E: the rehearsal files picked from the commit's list; the same commit also fixes four unrelated bugs] | |
| `05ede53c` `--year` forwarding (with other P1 work) | 9 | +152 / −39 | |

The year tooling now in the tree comes to 4,932 lines [M: `wc -l`]. That is `year_diff.py` 651, `fixtures_year.py` 395,
`citations.py` 1,319, `archive_text.py` 158, `taxyear.py` 54, `jurisdiction.py` 126, `fetch_sources.py` 358, the five
table extractors 921, the two table checks 318, `engine/src/year.ts` 67, and the one-off `research/ty2026/*.py` 565.

`--year` reaches 55 Python tools (`grep -rl 'taxyear'`) and 18 engine files (`grep -rl YEAR engine/src`). `--jurisdiction`
reaches 38 tools [M]. The New York retrofit (`bdac4121`) changed 59 tooling files (+3,749/−259) [M]. It is the same
kind of plumbing cost, for a jurisdiction rather than a year.

### 1.3 What a full adoption copies

`year_diff.py --adopt` copies the whole year tree [M: `tools/year_diff.py:472-503`]. These are the per-year trees that
would be duplicated [M: `/tmp/ty26/trees.py` over `git ls-files`]:

| Tree | Files | Lines | Copied by |
|---|---:|---:|---|
| `forms/2025` | 62 | 53,035 | `--adopt` |
| `params/2025.yaml` | 1 | 2,270 | `--adopt` |
| `tables/2025` | 20 | 9,328 | `--adopt` |
| `interview/*2025*` | 7 of 10 | 4,917 for all 10 | `--adopt` |
| `ambiguities/2025.yaml` | 1 | 1,608 | `--adopt` |
| `fixtures/2025` | 55 | 252,898 | `fixtures_year.py` |
| `reviews/2025` | 783 | 2,290,070 | only `citations.json` is carried; the rest must be produced again (section 3) |
| `rendered/2025`, `reports/2025` | 84, 61 | 34,310, 89,378 | regenerated |
| New York (`forms/ny`, `params/ny`, `tables/ny`, `fixtures/ny`, `reviews/ny`) | 85 | 182,802 | nothing yet (section 4) |

## 2. Mechanical work and hand work

### 2.1 What the tools did [M]

- **`fetch_sources.py`** fetched and verified the archive: 158 (2025) and 91 (2026) documents verified [T: LOG].
  Draft rows carry flags (F1).
- **`year_diff.py`** on 11-04 found 2,236 of 3,703 citing items on the worklist
  [M: `reports/2026/year_diff_from_2025.md` line 3]. Rerun today: 2,272 of 3,811 [M: section 6]. It finds changed
  quotes, headings and amounts only where a 2025 citation exists. **49 of the 135 change-map entries (36%) have
  "Worklist items: none (found by reading the form…)"** [M: `grep -c` in `changes.md`]. New lines, new forms and
  new rules that no 2025 citation rests on were found by reading the drafts, not by the tool.
- **`--adopt` with `citations.py --relocate`** copies the definitions, rewrites `tax_year:` and "(2025)", and moves
  page numbers. Today it moved 994 of 1,688 segments and left 553 (33%) for review [M: section 6].
- **`fixtures_year.py`** re-evaluates and re-records fixtures and keeps evidence where nothing changed. Today: 1,590 of
  1,634 cases (97.3%) would be re-recorded [M: section 6].
- **Table extractors** (`extract_tax_table`, `extract_eic_table`, `extract_ptc_tables`, `extract_macrs_tables`,
  `extract_class_lives`) produce 9 of the 19 federal table YAMLs [M: `grep -l 'Generated by|extract' tables/2025/*.yaml`].
  For New York, 2 of 19 are produced by a tool. In the preparation they did nothing: `i1040gi`, `i4562`, `p946` and
  `i8962` had no 2026 edition.
- **`research/ty2026/split_worklist.py`, `build_params.py`, `check_params.py`, `check_quotes.py`** (565 lines) are
  one-off tooling written during the preparation. They live in `research/` rather than `tools/`, so they have no
  self-test in check-all.

### 2.2 Every place someone rewired by hand, and why the tooling did not cover it

| # | Hand work | Size | Why no tool covered it |
|---|---|---|---|
| H1 | Source catalog `tools/sources-2026.json`: a URL and draft flags per document; on adoption, every draft row is rewritten to its final | +211/−32 on 11-04 [M]; 57 rows on 10-27 [T] | the IRS posting schedule is not machine-readable; F1 added the flags but not the discovery |
| H2 | The change map: 133 entries written by four Opus agents, then a fifth to verify them, then 2 more from the statute read | 135 entries [M: `grep -c '^### C-'`]; 2 high, 11 medium and 7 low corrections [T: ADOPTION] | judgment. 36% of entries had no worklist item (2.1) |
| H3 | Parameter values: the `V` table, about 69 `put` calls plus the tax-computation-worksheet loop, typed from the pages | 273 values: 45 auto, 108 none, the rest by hand [M] | `year_diff` flags which parameters sit on changed text but does not propose the new amount |
| H4 | Definition patches for 5 forms, written as full copies plus `.diff` files | +591/−77 [M] | design, inherent. The *format* is the problem (H10) |
| H5 | Year literals in the adopted definitions | 1,030 lines on 10-27 [M: `reports/2026/year_literals_from_2025.json`]; **1,731 today** [M: section 6] | `--adopt` rewrites only `tax_year:` and "(2025)". Ids such as `eic.died_2025`, `f2441.paid_2026`, `person.edu_a2025`, `refund.line5d_2024` and `asset.is2025` (30 ids [M: `grep -o` over `forms/2025`, `interview`, `params`]), the 93 `amb.2025.*` register ids with 258 references [M], and question text are left for review |
| H6 | Citation segments the relocation could not place | 379 after O1 to O7 [T: `rehearsal_defects.md`]; 553 today [M] | quotes that changed or moved across pages; anchors only "in force" |
| H7 | Per-year page layouts hard-coded in tools | 7 year-keyed dicts with only a 2025 key [M: `grep for_year\|LAYOUT`]: `extract_tax_table.py:36`, `extract_eic_table.py:43`, `extract_ptc_tables.py:44`, `extract_class_lives.py:31`, `transcription/transcribe_tables.py:45`, `check_instruction_cites.py:44`, plus `extract_macrs_tables` via its checks | owner ruling under T-045: extractors take the year "for paths only, unverified for other years". Each fails, naming itself, for 2026 |
| H8 | Hand-made tables that vary by year | 10 of 19 federal tables have no extractor [M]. Year-varying among them: `auto_limit*`, `dc_rate`, `ltc_limit`, `rate_schedule`, `savers_rate`, `simple_catchup` [T: ADOPTION step 6]. New York: 17 of 19 by hand [M] | no extractor was written |
| H9 | New inputs and their ripple: fixtures, the interview bank and profiles, `engine/src/generate.ts`, `tools/engines/generate_cases.py`, `tools/transcription/input_contracts/` | about 5 new inputs in the 5 proposed forms [M, 1.1]; more from the other definition-changing entries [E] | five places, one owner per input (HANDOFF-HARDENING-1). Since `ea25cc6a` the fixture part is one line in `defaults.json` |
| H10 | Proposals decay against a moving 2025 base | since `d6017626`, 21 commits changed 43 authored files by +6,777/−2,445 [M: `git log --numstat d6017626..HEAD -- forms/2025 params/2025.yaml interview tables/2025`]. `sa.diff`: 2 of 10 hunks no longer apply [M: `patch --dry-run` on a copy]. 14 parameters added to 2025 are absent from the proposal (`household.no`, `div.no`, `hsa.year_*`, …) [M] | proposals are full copies and line diffs, not operations keyed by line id, and no check revalidates them |
| H11 | Year-specific code outside data | section 5 | |
| H12 | The `params/2026.yaml` format conversion: drop `source`, `note`, `new_in_2026`, `unsourced`, `retired` | 285 values [M] | `build_params.py` writes a research format, not the build format [T: ADOPTION step 4] |

## 3. Verification cost

**Paid review calls for 2026: none so far.**

- `.transcription/costs.jsonl` in the main checkout has 1,261 rows, 2026-11-04T02:07Z to 11-08T16:00Z, $357.85
  [M: `/tmp/ty26/costs.py`].
- No subject is a 2026 subject. Note that the ledger has **no year field** (its keys are listed by the same script),
  so a 2026 review could not be told apart from a 2025 one by the ledger alone.
- No `reviews/2026` exists [M].
- LOG states that no paid calls were made and no `tools/transcription/` review tool was run [T].

**Agents.** Six Opus agents worked on 11-04: four change-map sections, one verification and the owner-decisions
pass.

- Tokens: 1,964,720 subagent tokens in all (257,007 + 301,300 + 293,915 + 394,618 + 387,428 + 330,452)
  [M: `research/costs/agent_runs.jsonl` lines 55 to 59 and 61].
- Agent time: 4,951 s (3,526 s for the five step-3 agents, which ran four in parallel and then one; 1,425 s for
  decisions).
- Dollar cost: `cost_usd: null` on every row. It is not measurable from the record.
- The main session's own usage was not shown [T: LOG].

**Elapsed time** [M: commit timestamps]:

- Preparation: first commit `a860627a` at 20:11Z, squash `d6017626` at 23:08Z, so about **3 h** wall-clock. Steps
  3 to 6 were committed within 64 s of each other (21:04:09 to 21:05:13), so per-step times cannot be read from git.
- Rehearsal: `713a5662` at 09:13 and the defect fixes in `6cae6818` at 11:49 the same day, about **2.6 h**, sharing
  the session with other work.
- T-045: about 17 h from first to last commit, overnight, with other commits in between.

**Checks that had to change** [T: `reports/2026/rehearsal_defects.md`, its fixes visible in `713a5662` and
`6cae6818` M]. 13 tool defects:

- F1: draft flags in `fetch_sources`;
- F2: draft watermarks;
- F3: the relocation rewrite;
- F4: lost value findings;
- F5: year-named quotes;
- F6: `fixtures_year` crash and `--plan`;
- O1 to O3: relocation;
- O4: table checkers crashed on a missing source;
- O5: draft marks in 7 more readers, giving a new `archive_text.py`;
- O6: noisy value findings;
- O7: soft hyphens.

Five self-tests were added to check-all as a result.

**What a real adoption's reviews will cost [E].** `tools/transcription/check_logs.py` fails "unless every form has a
transcription-agreement log and a render-comparison log from every required model family … with … current source
hashes" [M: its docstring], read from `reviews/<year>/`. A new year has new source snapshots for every document and
no `reviews/2026`. **Every form therefore needs a fresh review, whether or not its content changed.** ADOPTION
step 7's "reviews of changed forms only" is not what the check enforces.

One Claude round, priced as the median cost of one call per subject and kind in the ledger [M: `/tmp/ty26/costs.py
… claude-opus-5-5`]:

| Kind | Cost of one round |
|---|---:|
| transcription | $69.72 |
| render | $24.53 |
| class M | $19.27 |
| completeness | $16.10 |
| screen | $5.66 |
| false-no | $2.05 |
| **Total** | **≈ $137** |

DeepSeek render, transcription and class M add ≈ $5. Forms have historically needed more than one round. In the
ledger's 4.5 days, Claude spent $345 across these kinds. So a rollover's review bill is **≈ $140 to $400** [E: 1 to 3
rounds]. Adjudication agents and fix agents come on top.

## 4. How complete it is

**Not rolled over. Federal is prepared in part; New York is not started.**

| Part | State | Record |
|---|---|---|
| Archive | 91 of the needed 2026 documents archived, 55 of them drafts. Missing: `i1040gi` (937 kind-(b) items and 60 parameters wait on it), `i1040sca`, `i1040sd`, `i8949`, `i8995a`, `i4562`, `i8582`, `i1065sk1`, `i8962`, 18 publications | ADOPTION "Documents still missing" [T] |
| Worklist | 410 kind (a), 1,826 kind (b) [T, matching the counts in `worklist_split.md` M] | `reports/2026/worklist_split.md` |
| Change map | 135 entries [M]. By kind [M: `grep '^- \*\*Kind:\*\*'`]: 47 wording only, 32 new line or form, 24 rule, 20 amount, 9 not encoded, 2 waiting, 1 mixed | `research/ty2026/changes.md` |
| Definitions | 5 of 62 forms proposed. The other definition-changing entries (Schedules 1-A and 2 renumbering, 8995/8995-A, 8960, 8812, 5695, 2441, 8863, 8962, 5329, 1099-R, Schedule C lines 16 and meals, 4562 …) are not drafted | ADOPTION "Definition changes in the order to do them" |
| Parameters | 273 proposed; 108 unsourced; 70 to re-verify; 14 added to 2025 since then and missing [M] | `params-2026.proposed.yaml` |
| Tables | none re-extracted (no 2026 `i1040gi`, `i4562`, `p946`, `i8962`) | ADOPTION step 6 |
| Fixtures | 22 predicted cases; carry plan only | `research/ty2026/fixtures-proposed/` |
| Reviews | none | |
| `years.json` | `[2025]` | |
| **New York** | **nothing**: no `sources/ny/2026`, no NY section in ADOPTION or LOG [M: `grep -i 'new york\|ny' docs/ty2026/*`], and NY tools hard-code 2025 (section 5) | **no record** |

Open tasks: T-011 (the adoption) and T-230 (the year-aware completeness prompt) [M: TASKS.md]. The federal remainder
has a record (ADOPTION's 9 steps). The New York remainder has none.

## 5. Year-specific code

[M: `grep -rIEn '\b20(24|25|26|27)\b' tools engine/src lean ui`: 207 lines in 61 files. Most are tests,
comments, quoted source text and owner-decision dates. The ones that would need a hand edit at rollover are these.]

- **Engine: clean.**
  - The only year-keyed logic is `generate.ts:218,225`, vehicle and asset years relative to `YEAR` (−6, −20). It
    is to be checked when the auto-limit and MACRS tables change [T: T-045].
  - The text references to Rev. Proc. 2024-40 in `conjecture.ts` are 2025-specific report wording.
- **Tools: year-keyed dicts with only 2025.** The seven layouts of H7, plus `transcription/adapter_contracts.py:14`
  and `transcription/input_contracts.py:15`, both `REQUIRED = {"2025": …}`, and `human_review/packet.py:245`
  `Y == "2025"`.
- **Prompts and UI.**
  - `transcription/completeness_review.py:43`: "pages of the 2025 IRS instructions" (T-230).
  - `ui/app.ts:396`: "2025 return".
- **New York tools hard-code 2025 paths**, without `taxyear`:
  - `ny_fixtures.py:30,51,139,402`;
  - `engines/ny_policyengine.py:33,34,90,108`;
  - `ny_predict.py:21`;
  - `extract_ny_tax_table.py:180-181`.
- **check-all**: 22 of 92 `step` lines do not pass `"$@"` (`--year`) [T: consolidation inventory 5, 1.3].
- **Authored data**, outside params and forms' values: H5's year-named ids. `forms/2025/clcw26.yaml` is named for the
  following year. `fixtures/2025/defaults.json` holds 13 year-named inputs (`dependent.edu_a2025`/`a2026`,
  `eic.died_2025`, `f2441.paid_2026`, `refund.line17_2024`, …) [M: `grep -n '20(2[4-7])'`].
- **Duplicated per-year files**: the whole year tree (1.3) by design. `reviews/2025` alone is 2.29 M lines.

## 6. Effect of today's changes on the cost of a rollover

**Measured today, in the scratch copy** [M]:

- `python3 tools/year_diff.py --from 2025 --to 2026 --adopt` ran in 10 s:
  - relocate: 1,688 segments; 141 in place, 994 moved, **553 not placed**;
  - **1,731** year-literal lines (1,030 on 10-27, +68% in 13 days);
  - worklist 2,272 of 3,811.
- `node engine/dist/main.js build --year 2026` failed with 5,448 error lines [M: `grep -c '^  - '`]. 1,915 of them name
  a document that is not in the 2026 manifest (987 of those are `i1040gi`). Most of the rest are citations with no
  snapshot or revision.
- `python3 tools/fixtures_year.py --from 2025 --to 2026 --plan` ran in 112 s:
  - **1,590 of 1,634 cases re-recorded (97.3%)**, against 1,062 of 1,090 (97.4%) on 10-27
    [M: the saved 10-27 report];
  - 372 rest only on documents with no 2026 edition.
- An instrumented copy of the plan (scratch only) counted the re-records again under two exemptions:
  - excluding the 34 structural-constant parameters (`sales.zero`, `sc.hundred_cents`, …, value 0 to 5 or 100):
    1,577;
  - excluding items whose only finding is a missing document: 1,218 (75%);
  - excluding both: 1,217.
  - Worklist lines fall in 65 form prefixes, 27 of them with kind-(a) lines.

**What this means for `ea25cc6a` and `0b369551`.**

- **Per-form fixtures with `defaults.json` (`ea25cc6a`)**:
  - They do **not** reduce how many fixtures a rollover re-records. The share is unchanged at 97%, because a
    case's derivation still runs through `person`, `household`, `sales` and `f1040` lines that sit on the worklist.
    Re-recording is mechanical in any case.
  - What they cut is H9: a new input now costs one `defaults.json` line plus the cases that exercise it, not an edit
    to every whole-return case. Before, the dividends gate touched 153 files [T: retrospective 3.3].
  - `fixtures_year.py` carries `defaults.json` and sets its `tax_year` [M: `fixtures_year.py:275-278`].
  - The 13 year-named defaults still need renaming by hand (H5).
- **The leak check (`0b369551`)**:
  - It mechanically checks the gating of every new input, and 2026 adds several gates (`f1040.gate.*`,
    `s3a.gate.qualified_alien`, `sa` screens).
  - Its baselines may only shrink, so a 2026 input that is reachable out of bank order fails the build instead of
    waiting for a screen review.
  - Expected effect: fewer screen and completeness rounds for the new gates [E]. The work moves earlier but is not
    avoided.

**Estimated cost of the real federal adoption now, by kind [E]:**

| Kind | Estimate | Basis |
|---|---|---|
| Authored definitions | ≈ 2,400 hand-changed lines over ≈ 25 forms | ≈ 42 lines per entry (668 lines for the ≈ 16 entries proposed) × ≈ 57 definition-changing entries (32 new line or form, 24 rule, mixed) |
| Parameters | ≈ 180 values read or re-verified by hand (108 unsourced + 70 draft), ≈ 45 to 60 auto | 1.1 |
| Tables | 9 extractor runs after 7 layout edits; ≈ 7 hand tables | H7, H8 |
| Year literals and citations | ≈ 1,700 literal lines and ≈ 550 segments to review | measured today; both grow with the tree |
| New inputs | ≈ 10 to 15, each one defaults line plus four other places | 5 measured in 5 forms, extrapolated |
| Fixtures | ≈ 1,600 re-recorded mechanically; class M (paid) for ≈ 65 documents, ≈ $19 a round | 6; ledger medians |
| Reviews | full round on all 62 forms, ≈ $140 to $400 | 3 |
| Agents | ≈ 2 to 4 M Opus tokens (preparation used 2.0 M for the change map alone) | 3 |
| New York | not estimable: no change map, no 2026 sources; 17 of 19 tables by hand | 4 |

## 7. Top 5 levers, ranked by expected cost saved per year

**1. Carry review logs across years when the subject and the year-normalized cited text are unchanged.**

- Evidence:
  - `check_logs.py` requires a current log for every form and every source hash per year (3), so all 62 forms
    are reviewed again every year.
  - Only 27 form prefixes have kind-(a) worklist lines (6).
  - Reviews are the largest paid item: $137 a round and $345 in 4.5 days of the ledger.
- Mechanism: `year_diff` already aligns sentences across years. A log could be carried when every sentence its
  subject cites is unchanged after year normalization, as `fixtures_year` does for fixtures. Combine with T-219
  (line-scoped reviews).
- Saving: roughly half of a review round and its adjudication each year [E: (62 − ~30 changed) / 62]. ≈ $70 to $200 a
  year, plus agent time.

**2. Remove year literals from identifiers and from text the adoption must rewrite.**

- Evidence:
  - 1,731 year-literal lines after `--adopt`, up from 1,030 in 13 days (6). The count grows with every feature.
  - 30 year-named ids and 93 `amb.2025.*` register ids with 258 references (H5).
  - 13 year-named fixture defaults.
- Mechanism: relative names (`prior_year`, `this_year`, `next_year`) and a `{year}` token in question text that
  `--adopt` substitutes; a build check that forbids new year literals in ids.
- Saving: the ≈ 1,700-line hand review and its rename ripple through forms, interview, defaults, fixtures and reviews
  [E: hours of judgment-agent time a year, and it removes a growing cost].

**3. Make the parameter proposal a tool: same sentence in the new edition, extract the amount.**

- Evidence:
  - 45 of 273 values were carried automatically; ≈ 120 were typed by hand, and 108 are still to fill (1.1, H3).
  - The four preparation scripts (565 lines) sit in `research/` with no self-test.
  - The proposal is already 14 parameters behind the tree (H10).
- Mechanism: promote `build_params.py`, `check_params.py`, `check_quotes.py` and `split_worklist.py` to `tools/`. For
  each parameter, find its 2025 quote's aligned 2026 sentence (`year_diff`) and propose the amount in the same
  position. Add a parser for the Rev. Proc. tables. Have it write the build format (H12) and regenerate against the
  current tree.
- Saving: most of ≈ 180 hand-read values a year [E], and the decay of the proposal.

**4. Keep year deltas as operations keyed by line id, validated in check-all, not as full copies and line diffs.**

- Evidence:
  - Within 5 days `sa.diff` lost 2 of 10 hunks, and the 2025 base moved +6,777/−2,445 lines in 43 files (H10).
  - Every adoption copies 53 k form lines and 253 k fixture lines and needs a 2.29 M-line review tree (1.3).
- Mechanism: a 2026 overlay (added, changed and removed lines and parameters by id) applied to the 2025 tree at build
  time, or at least checked for applicability on every commit while the proposal waits for the finals.
- Saving: the rework of stale proposals between preparation and adoption (≈ 2 months on this calendar) and the
  duplication in later years [E: hard to quantify; large if the project lives several years].

**5. Year-key every hard-coded layout and path from data, and give New York the same plumbing.**

- Evidence:
  - 7 page-layout dicts and 2 contract dicts with only a 2025 key, plus `packet.py`, the completeness prompt (T-230)
    and the UI title (H7, 5).
  - NY tools hard-code 2025 in 4 files.
  - NY has 17 of 19 tables by hand and no rollover record (4).
  - 22 check-all steps drop `--year` (5).
- Mechanism: put page ranges in the source catalog (`tools/sources-<year>.json`) next to the document, found by
  heading search the way `citations.py --relocate` finds pages; route NY tools through `taxyear`; run the
  year-forwarding check on every step.
- Saving: ≈ 15 hand edits a year, each of which currently fails one tool at a time during adoption [E], and it
  avoids a second, New York plumbing retrofit like the 59-file `bdac4121`.

**Not ranked, a prerequisite for measuring the next rollover.** Add `year` and `jurisdiction` fields to
`.transcription/costs.jsonl` and `research/costs/agent_runs.jsonl`, and a `cost_usd` where one can be computed. Today
neither ledger can attribute spend to a tax year (3).
