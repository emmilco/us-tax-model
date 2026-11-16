# Lane briefs for round `mf1`: landing the medium fixes from the drafted patches (lane lane-briefs)

Lane lane-briefs. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us and ny. Written 2026-11-16, 00:35-01:15.
Read only: nothing in the repository was touched; no build, check, walk or paid call. Labels: **[C path:line]** checked
against that file in this session (repo paths are in the xint worktree unless stated); **[T]** relayed from a
/tmp/nightplan file and not re-checked; **[I]** inferred.

## Summary

- **Seven lanes in two waves.** Wave 1 is six lanes in parallel, which is the most protocol 8.6 allows
  [C docs/2026-11-15_coverage_expansion_protocol.md:427]. They work on disjoint form files:
  - **L1 pay** (`scope person tipjob s1`): inc-m12 v2.
  - **L2 amtpay** (`f1040 s2 f4952 f8853c`): int-amt v2, then inc-m34 v2.
  - **L3 rental** (`rental royalty asset f8582`): sche-a v2.
  - **L4 credits** (`dependent eic f5695`): older-credits v2.
  - **L5 ny** (`ny_it201`): older-ny v2.
  - **L6 scha** (`sa`): older-scha v2, plus 0817a or 0817b.

  Wave 2 is one lane, **L7 interview**: int-n10, int-p18, int-personas, then int-n10-ticks and int-rprop if the owner
  agrees. It starts after the wave-1 merge.
- **Every patch has a v2** in `/tmp/nightplan/patches/v2/`, so no lane works from round 2 plus red-team notes. The
  v2 notes are `older.md`, `inc.md`, `sche-int.md` and `int-rprop.md`. Each v2 patch was `git apply --check`ed alone
  against frozen xint [T].
- **Three conflicts between patches are settled by the lane split.**
  - **BUG-0907** (`scope.nol` help) is in v2 inc-m12 only. sche-a v2 dropped it [T sche-int.md].
  - **`rental.not_at_risk`**: v2 int-n10 no longer overrides it [T sche-int.md].
  - **int-amt and inc-m34** touch the same `div.*` block of the bank, and both edit `forms/2025/s2.yaml`. So they go
    in one lane, int-amt first.
  - One textual clash is left for the integrator: inc-m12's `cod_why`/`cod_how` groups and int-amt's
    `interest_dividends` group are inserted at the same spot after `money_b` [T sche-int.md]. Keep both groups. No
    entry is changed by both.
- **Two places where the coordinator's brief conflicts with the rules.**
  - **(a) Paid reviews.** Protocol 6 says reviews run once per round, "on the integrated tree on `main`, after every
    fix of that form in the round has landed. Build lanes make no paid calls" [C protocol:224-225]. So each brief
    below lists its reviews for a **post-merge review step** (R1 after wave 1, R2 after wave 2). The lane does not
    run them.
  - **(b) check-all.** Protocol 8.6 (owner, 2026-11-15) says a lane "runs targeted checks only, never check-all"
    [C protocol:419]. But the pre-commit hook refuses a commit whose tree has no green fast-tier run
    [C tools/hooks/pre-commit:2-10, 50-51], and a lane must commit its branch for the merge. My reconciliation [I],
    for the coordinator to confirm: the lane runs targeted checks while working, then exactly one
    `tools/check_all.sh --tier fast`, and only when the integrator calls it in to commit. Project CLAUDE.md:76 says
    the same ("a lane verifies with `tools/check_all.sh` in its own worktree").
- **Review spend** (estimated from the ledger's recent per-call means, section 4) [I]:
  - Core plan: about **$64**.
  - With every option (0810 option B, the NY class M, the tick prompts, rprop): about **$103**.
  - Plan for about **$135** to leave room for a second round on non-low findings.
  - Not counted: up to about $115 of class M reruns if input-only fixture restatements make every class M subject
    due. That is owner decision OD-31; I recommend no rerun.
- **Owner decisions.** Section 5 lists 31, de-duplicated across the plans. **Five block or shape tomorrow's lanes:**
  - OD-1: 0810, option A or B;
  - OD-16: 0817, (a) or (b);
  - OD-7: the 0894 former-spouse split;
  - OD-23: the 25-word limit for tick prompts;
  - OD-26: rprop.
  Every lane has a stated default if the owner has not answered.
- **Source dependencies.** Some fixes cite documents that are not archived yet:
  - 0805 cites Pub. 936;
  - 0901 cites the Schedule H instructions and Pub. 926 (2025);
  - the former-spouse half of 0894 cites Pub. 505 (2025), which is not fetched.

  A small mechanical source lane **S0** (Sonnet) archives the first three before wave 1. The steps are in
  `/tmp/nightplan/sources/README.md` [C].
- **Partial or unverified.**
  - Nothing here was run.
  - Every apply order not listed in the v2 notes is [I]. The int-amt-then-inc-m34 order was not tested by anyone.
  - Spend figures are estimates, not `--dry-run` output.
  - `/tmp` is not durable. Copy `/tmp/nightplan/patches/v2/`, `/tmp/nightplan/sources/` and the edit scripts under
    `/tmp/nightplan/scratch/` somewhere durable before a reboot. On macOS, `/tmp` is cleared at boot [I].

---

## 1. Round setup (coordinator, before any lane)

1. **Base.** The lanes start after the coverage expansion lands on `main`. That is the commit the release
   `r2026.11.15.1` is cut from; check `git tag -l 'r2026.11.15.*'` [C HANDOFF-NEXT-SESSION.md:43-45]. Today `main` is
   still `acde74b5` [C git log main]. Set `refs/scratch/mf1-base` to that commit, or to the bookkeeping commit after
   it (protocol 8.3).
   - Record the hash in each brief.
   - The patches were cut from xint's working tree at about 00:30 [T]. If the landed tree differs, a lane's
     `git apply --check` fails. The lane then stops and reports (rule below). It does not hand-merge.
2. **Durable copies.** Copy `/tmp/nightplan/patches/v2/` and `/tmp/nightplan/sources/` to a durable scratch place,
   for example `~/scratch/mf1/`, and give lanes that path. The briefs below say `$P` for the patch directory.
3. **S0 sources** (Sonnet, mechanical, us, 2025). Archive p936, p926 (2025, the irs-prior URL) and i1040sh, following
   `/tmp/nightplan/sources/README.md` steps 1 to 4. That means:
   - entries in `tools/sources/2025.json`;
   - `fetch_sources.py --fetch --only ...`;
   - a hash check;
   - the manifest revision fields.

   Commit it on `main` before the lanes are cut, or as the first merge. It needs the docs or fast tier.
   **Pub. 505 (2025)** is not fetched. If it can be archived, it decides OD-7. If not, L2 takes the OD-7 default.
4. **Claims.** Each lane claims at launch (section 2). Two lanes add input ids: L1 (option B, ten `s1.cod_*`) and L2
   (`f1040.tax_exempt_any`). So the integrator calls them in to commit in turn, and runs
   `python3 tools/claims.py release inputs` between them (protocol 8.1 [C:337-343]). In wave 2, L7 adds inputs only
   if int-rprop is taken.
5. **Bookkeeping held back for the coordinator** (protocol 8.4: lanes write pending entries only):
   - closure records drafted in the notes: BUG-0629, BUG-0092 (older-ny.md [T]) and BUG-0911 (sche-a.md [T]);
   - the jr-verify pending entries, including the **medium** `household.community_property` domicile finding, which no
     lane fixes tomorrow (section 6);
   - TASKS rows for review debt.

---

## 2. Lanes, order and ownership

| Lane | Wave | Model / class | Jur. | Forms claimed (form files) | Patches (in apply order) | Entries |
|---|---|---|---|---|---|---|
| L1 pay | 1 | claude-opus-5-5 / judgment | us | scope person tipjob s1 | `inc-m12.base.patch`; then `inc-m12.cod.patch` only on OD-1 = B | 0806 0808 0822 0896 0904 0905 0906 0907; 0810 (B) |
| L2 amtpay | 1 | claude-opus-5-5 / judgment | us (also restates NY fixtures) | f1040 s2 f4952 f8853c | `int-amt.patch`, then `inc-m34.patch` | 0830 0833 0873 0894 0897 0899 0900 0901; tax-exempt screen (step regression) |
| L3 rental | 1 | claude-opus-5-5 / judgment | us | rental royalty asset f8582 | `sche-a.patch` | 0775 0789 0790 0836 0890; new not-at-risk gap |
| L4 credits | 1 | claude-sonnet (mechanical) | us | dependent eic f5695 | `older-credits.patch` | 0793 0796 0797 0861 0862 0870 |
| L5 ny | 1 | claude-opus-5-5 / judgment | ny | ny_it201 | `older-ny.patch` | 0850 0851 |
| L6 scha | 1 | claude-opus-5-5 / judgment | us | sa | `older-scha.patch`; then `older-scha-0817a.patch` (OD-16 default) or `-0817b` | 0803 0805 0815 0817 |
| L7 interview | 2 | claude-opus-5-5 / judgment | us | none (bank only); `rprop` if int-rprop is taken | `int-p18`, `int-personas`, `int-n10`; then `int-n10-ticks` (OD-23) and `int-rprop.after-v2-n10` (OD-26) | interview items 2 to 5, rprop.screen |

Notes on the table.

- **Model choice.** L4 is wording only, already decided and red-teamed, so it can run on Sonnet. CLAUDE.md puts
  "applying rulings" on Sonnet. The other lanes carry a model change or hand-predicted fixtures that may need
  investigating, which is judgment:
  - L1: option B;
  - L2: the gate line and the fixture ripple;
  - L3: the f8582 arithmetic;
  - L5: the NY gate;
  - L6: 0817a and mutate.ts;
  - L7: the reorder and rprop.

  Fable only if the owner says so for the session (CLAUDE.md).
- **Bank-only entries of other lanes' forms are fine.** The bank merges by entry id, and claims cover form files only
  [C tools/claims.py:5, 34].
  - L3 edits the `sa.mortgage_interest` and `sa.line5b` bank entries. L6 owns `sa.yaml`.
  - L4 edits `person.rmd_missed`, `household.credit_disallowed` and `f8863.ban` (bank only).
  - L7 edits entries of rental, person, scope, s2, k1s, k1p, rec, s1, sd and f1116 (bank only).
- **Twins.** L4 edits `dependent.yaml` lines that are not Form 8863 Part III (`dependent.ptc_*`
  [C older-credits.patch:25]), so the twin rule does not force a `person` claim. L4 still runs `check_twins.py`.

**Order.**
1. S0 (sources), then cut `refs/scratch/mf1-base`.
2. **Wave 1:** L1 to L6 in parallel. Run lane builds with `renice +15`, at about one build per two cores (protocol
   8.10).
3. **Merge batch B1** (integrator; section 3.3). Commits are called in this order: L4, L5, L6, L3 (no new inputs),
   then L1, release `inputs`, then L2. Then one full-tier check-all on the merged tree, and one merge commit.
4. **R1 reviews** on `main` (section 4): every transcription, render and class M review. Run the question, screen and
   false-no reviews only for forms and entries that wave 2 does not touch.
5. **Wave 2:** L7, cut from the B1 merge commit, which becomes `refs/scratch/mf1-base2`.
6. **Merge batch B2**, then **R2 reviews**: the question, screen and false-no reviews left over, plus rprop's
   transcription, render and class M if int-rprop landed.
7. Adjudication, by one lane per form or small group (protocol 6.3). A second round only if a non-low finding is open
   (6.4).

What may run alongside what:
- S0 must finish first, because L2 (0901) and L6 (0805) cite its sources.
- L1 to L6 have no ordering among themselves.
- L7 waits for B1, because its patches were tested only on top of sche-a and inc-m12 [T sche-int.md]. int-rprop also
  needs int-n10 applied first.
- R1 can overlap wave 2. L7 changes no form file that R1 reviews, unless int-rprop is taken; rprop is then reviewed
  in R2 only.

---

## 3. The briefs

### 3.0 Common block (paste into every brief; protocol 8.7 parts)

> **Who you are.** You are one of six lanes (wave 1) or the single lane of wave 2. Together you are landing fixes
> for the open medium findings of the 2026-11-15 release reviews. The drafting lanes of the night of 2026-11-16 drafted
> these fixes as patches, a red-team lane checked them, and v2 lanes corrected them. Your job is to apply your
> patch to a clean base, prove it with the project's checks, and report. You do not redesign. The owner judges the
> result by two things: whether each fixed finding is fixed without a new wrong value, and whether the interview got
> no longer for the filer who has nothing in your topic.
>
> **Where you work.**
> - Worktree `.claude/worktrees/mf1-<lane>`, branch `mf1-<lane>`, base `refs/scratch/mf1-base` (hash: `<fill in>`).
> - Never the main checkout; never push.
> - No paid reviews, no model calls from code, no `claude -p`.
> - Use absolute paths, and never `cd` inside a backgrounded command.
> - Background waits: on a pid or `tools/check_all_bg.sh --status`, with a timeout. Never `pgrep -f`.
> - Run your heavy commands under `renice +15`.
>
> **Setup.**
> 1. From the main checkout: `git worktree add .claude/worktrees/mf1-<lane> -b mf1-<lane> refs/scratch/mf1-base`.
> 2. Then `python3 tools/worktree_data.py clone .claude/worktrees/mf1-<lane>`.
> 3. In your worktree: `python3 tools/claims.py claim <your forms> --reason "mf1 <lane>"`.
> 4. Record the base hash in your note.
> 5. Run the **before** walks on the untouched base: `npm run compile && node engine/dist/main.js build && node
>    engine/dist/main.js draft-walk --out /tmp/mf1-<lane>/walks-before`. The default `--out` writes into
>    `docs/provisional/walks/after/`, which is tracked [C interview/README.md:781-784].
> 6. Then `git apply --check $P/<patch>`. Apply only if the check passes. If it fails, stop and report the failing
>    hunks. Do not hand-merge or use `--3way` unless your brief says so.
>
> **Read first, in order:**
> 1. Project `CLAUDE.md`.
> 2. `docs/2026-11-15_coverage_expansion_protocol.md` sections 6.3 (stop rule), 8.1 to 8.8 and 9.1.
> 3. `docs/2026-11-13_interview_construction_protocol.md` sections 1.2 (N1 to N12), 2 and 7. It is normative for
>    any question or help change.
> 4. Your patch's v2 note, and the round-2 note it amends.
> 5. `/tmp/nightplan/wording-redteam.md` for your entries.
> 6. `tools/README.md` for bug-inventory conventions ("Proposed fix:"; closure entries).
>
> **Do not touch** the files protocol 8.4 keeps from lanes:
> - `BUG_INVENTORY.md`, `TASKS.md`, `tools/coverage/categories.json`, `changes/2026/README.md`;
> - another lane's form files;
> - generated files (`canonical/`, `rendered/`, `reports/`, `docs/COVERAGE.md`, the README coverage block, walk
>   transcripts). Regenerate these to run your checks, but they are not merged.
>
> **The bar (absolute).** Never edit an expected value, an expected refusal, a coverage row's `end`, or a check's
> baseline to make a check pass. If one would have to change, stop and report [C protocol:378-379].
>
> **Stop rule (handoff entry 2026-11-11/12; protocol 6.3 [C:255-256]).** If you find that wording this round adds
> would give a wrong value, or wrongly accept a return, **stop and report the finding before fixing it.** That wording
> may be the patch's text or your own. This covers a prompt, help, tick, heading or form source. Two more rules:
> - A unit already edited once in this round is recorded **open**, not edited again.
> - A rule of the build or a check that blocks the patch is reported, not designed around.
>
> **Verification (targeted checks while you work; never two at once; protocol 8.6):**
> 1. `npm run compile`, then `node engine/dist/main.js build`, then `render`.
> 2. `node engine/dist/main.js test-fixtures` (add `--ny` where your brief says).
> 3. `interview-rules`.
> 4. `tick-groups`.
> 5. `interview-coverage`, then `--write`. The report quotes wording.
> 6. `python3 tools/coverage/tree.py --check`.
> 7. `python3 tools/citations.py --strict`.
> 8. `python3 tools/year_changes.py --check`.
> 9. `python3 tools/siblings.py <each fixed id>`.
> 10. `draft-walk --out /tmp/mf1-<lane>/walks-after` (after walks).
>
> **check-all** runs once, only when the integrator calls you in to commit:
> - `tools/check_all.sh --tier fast`, which waits for a machine slot;
> - then `git add -A` and `git commit -F <msgfile>`.
>
> **Defects and closures.** Use `python3 tools/new_bug.py "<title>" --pending mf1-<lane> --field ...`:
> - **A new defect** gets "Proposed fix:" if not fixed.
> - **Each entry your patch fixes** gets a closure entry: `--field "Closes=BUG-NNNN" --field "Closure=fixed"
>   --field "Evidence=<the fixture or row ids and the check results from your run>"`.
> - Write closures only after your checks pass.
> - Never edit a committed pending file.
>
> **Notes.** Write `docs/provisional/lanes/mf1-<lane>.md` as you go, with the twelve sections of protocol 8.8. In
> section 1, "What the merge must know", put every shared file you touched (fixtures by case id, coverage rows by id,
> bank entries by id, `defaults.json` keys, generators).
>
> **Context.** Write a handoff in your note before your context runs out.
>
> **Report.** Your report covers:
> - the commit;
> - which checks ran, on which tree, with what results;
> - the before and after walks (steps, questions, prompt words, help words) for the typical filer and the filer with
>   nothing in the topic;
> - the ids added, removed or renamed;
> - what is unfinished, in rank order;
> - what needs the owner.
>
> State what was run and seen apart from what is inferred.
>
> **Ledger.** Your agent-run row records `model`, `class`, `year`, `jurisdiction` (`tools/check_agent_runs.py`).

---

### 3.1 L1 pay: inc-m12 v2 (pay not on a W-2, Schedule 1 income, canceled debt, NOL help)

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-pay`, branch `mf1-pay`, base `refs/scratch/mf1-base`.
- **Claim:** `python3 tools/claims.py claim scope person tipjob s1 --reason "mf1 pay"`.
- **Patches** (v2; `$P/inc-m12.base.patch` and `$P/inc-m12.cod.patch`):
  1. `inc-m12.base.patch` (8 files). Covers 0904, 0905, 0906, 0806, 0808, 0822, 0896 and **0907**. The 0907 hunk is
     yours alone: L3's v2 dropped it [T sche-int.md].
  2. `inc-m12.cod.patch` (11 files), **only if OD-1 = B**. This is 0810 as two tick groups: ten new inputs, a derived
     `s1.cod_unsupported`, restated fixtures and `generate.ts`. Make it a second, separate commit.
  - `base + cod` equals v2 `inc-m12.patch` [T inc.md].
- **Typical filer, and the filer with nothing.**
  - Typical filers: a waiter with tips (persona 09), a crypto holder with staking rewards (17), and a home caregiver
    paid under Medicaid through an agency (coverage `pay.medicaid_agency_code_ii`).
  - The filer with nothing: persona 01. For 01 the patch must add **zero** steps and change only words.
- **The risk particular to this lane.** Widened gates and helps can invite a wrong Yes. The red team found four such
  traps, and v2 fixed them:
  - a manager entering tips (A9);
  - a gift of crypto making the printed digital-asset answer Yes (A10);
  - a contest prize entered as gambling (A14);
  - a caregiver living in the parent's home sent to No (A13).

  Read each new help for the opposite trap.
- **Measure.** Walks 01, 09 and 17 before and after (steps, questions, prompt words, help words). The expected step
  change is 0 for all three [I].
- **Owner decisions.**
  - **OD-1** (0810, A or B). Default if unanswered: land the base only and leave 0810 open. Reasons: option B makes
    s1 class M due (about $17, above the owner's $3 gate), and option A breaks N10 at about 80 words.
  - **OD-2** (0896 prompt, 30 words). Default: land v2.
  - **OD-3** (0907, rentals named, Form 8582 guard). Default: land v2.
  - **OD-4** (0905, extra step for ADR holders). Default: accept.
  - **OD-22** (N10 overruns). Default: land as drafted.
- **Work list, ranked.**
  1. Apply base. Then build, `test-fixtures`, `interview-coverage` with the 12 new base rows (their predicted ends
     are in inc-m12.md and inc.md [T]), `tick-groups` (groups `other_pay`, `money_a`, `outside_us`), siblings for
     every id in inc-m12.md "Siblings checked".
  2. If OD-1 = B, apply cod. Check:
     - `s1.json` `stage16.refuse.s1.cod_unsupported` and `f1040.json` `stage20.refuse.excluded_canceled_debt` must
       pass with no expected value edited;
     - `classm.s1.1` must stay unchanged;
     - the five `other.canceled_debt_*` rows must end `refused: s1.cod_unsupported`;
     - if the walk needs the later boxes of a group answered, add `false` answers, never change an end
       [T inc-m12.md];
     - the `cod_amount` seq moves to 32, which puts the canceled-debt questions after f8853c and rec;
     - check the commit-msg hook for any `Fixture-default-changed:` line it requires (the `s1.cod_unsupported`
       default is removed).
  3. Closures for each fixed entry, and the note.
- **Verification.** The common bar. Add `test-fixtures --ny` if cod is applied (generate.ts changes).
- **Reviews** (R1 or R2; not in the lane):
  - Transcription and render, line-scoped:
    - scope: `pay_no_w2`, `strike_pay`, `medicaid_waiver`, `foreign_shares`;
    - person: `strike`;
    - tipjob: `listed`;
    - s1: `digital_income`; with option B, also `cod_unsupported` and the ten `cod_*`.
  - Class M of s1 with option B only.
  - Question reviews: the 13 bank entries, plus 10 with option B.
  - Screen and false-no: the 9 gates in inc-m12.md "Reviews made due" and `gate:scope.nol`. With option B, also each
    new box and both groups, screened on the asked wording.
  - **scope and person reviews wait for R2**, because L7 edits scope and person bank entries.
  - Caps (`--approve-cost`):
    - transcription and render together, $8;
    - s1 class M, $20 (option B only);
    - question reviews, $4;
    - screen and false-no, $5.
- **Landing.** Call-in order: after L4, L5, L6 and L3. You hold `inputs` only if option B landed.
  - The integrator releases `inputs` after your merge, before L2 commits.
  - Shared files to name in note section 1: `fixtures/2025/{defaults,classm,classm.deepseek,classm.gpt,mutation,s1,f1040}.json`
    (option B), `engine/src/generate.ts` (option B), and coverage `other.yaml`, `pay_not_w2.yaml`, `scope.yaml` (rows by id).

### 3.2 L2 amtpay: int-amt v2, then inc-m34 v2 (tax-exempt screen; dividends, Form 4952, payments, AMT, household help, LTC)

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-amtpay`, branch `mf1-amtpay`.
- **Claim:** `python3 tools/claims.py claim f1040 s2 f4952 f8853c --reason "mf1 amtpay"`.
- **Patches, in this order.**
  1. `$P/int-amt.patch`. It adds the new input `f1040.tax_exempt_any` and the gate line
     `f1040.tax_exempt_interest_if_any`. s2 reads are redirected. It renumbers order 272 and inserts the box in 782
     fixture cases (federal and NY), the generator, four personas and six coverage files.
     - A4 is applied: the heading says "have", and the `div.any` tick is "Shares or funds owned outside a retirement
       account, or a 1099-DIV" [T sche-int.md].
  2. `$P/inc-m34.patch` (10 files; 0830, 0833 (b), 0873, 0897 with 0894, 0899, 0900, 0901).
     - **The order was not tested** [I]. sche-int.md says int-amt goes first, because inc-m34's `div.other_boxes`
       help hunk sits inside int-amt's renumbered `div.*` block [T].
     - If that one hunk fails, apply its help text by hand. It is a single `help:` value, given verbatim in inc.md
       ("D, BUG-0830"). Then confirm with a YAML parse that only that field changed. This is the one hand edit this
       lane may make.
     - Any other failure: stop and report.
  - If time is short, land inc-m34 alone. It applies to the base without int-amt [T inc.md], and int-amt moves to
    wave 2.
- **Typical filer, and the filer with nothing.**
  - Typical filers:
    - an investor with dividends and a municipal bond (persona 14, or the coverage rows `dividends.*`);
    - a self-employed filer paying estimated tax (05);
    - a filer whose state refund came back (21).
  - The filer with nothing: persona 01. **The walk measures this lane.** Expected: 01 goes from 58 to 57 steps; 07
    loses one; 03, 04 and 08 probably save one [T int-amt.md, I].
- **The risk particular to this lane.**
  - **(1)** Moving the tax-exempt amount behind a box. The runner silently ignores an input behind a gate answered No
    [T int-amt.md, citing engine/src/eval.ts:843-873]. So every case that states a non-zero or withheld amount must
    state the box `true`, and the class M and mutation files must state the box everywhere.
  - **(2)** inc-m34's helps widen what is counted. Watch three of them:
    - joint estimated payments, and the line 26 split;
    - Medicaid and the VA on Form 8853 line 24;
    - the Form 4952 carryover, which v2 reverted to the source wording.
- **Measure.** Walks 01, 03, 04, 07, 08, 14, 21 before and after.
- **Owner decisions.**
  - **OD-5** (0833, (a) a refusing child or (b) an ambiguity entry). Default: (b), as in v2,
    `amb.2025.f4952_no_2024_form`.
  - **OD-6** (0873, Medicaid and VA). Default: v2. The register entry `amb.2025.f8853c_line24_public` records the
    chosen reading, that they count.
  - **OD-7** (0894, the former-spouse split). Default if Pub. 505 (2025) is not archived and does not confirm it:
    drop "or former spouse" from the `f1040.estimated_any` and `f1040.line26` helps.
    - This removal is the lane's own wording change. Run it past the stop rule: does it create a wrong value?
      Without the clause, a divorced filer gets no instruction, which is the status quo.
  - **OD-8** (0900, the transient reading). Default: v2.
  - **OD-9** (0901, its sources). Default: if S0 has not archived i1040sh and p926, leave out the
    `s2.household_help` hunks and record 0901 open.
  - **OD-31** (class M reruns after input-only restatements). This affects R1, not the lane.
  - **OD-22** (N10). Default: land as drafted.
- **Work list, ranked.**
  1. Apply int-amt. Then build, `test-fixtures` and `test-fixtures --ny` (expect 0 failures and no expectation
     edited), `interview-rules`, `tick-groups` (the new `interest_dividends` screen shows both boxes),
     `interview-coverage` with the six restated rows' ends unchanged, and the 01 walk.
  2. Apply inc-m34. Then `interview-coverage` with the 11 new rows: their predicted ends and v2 re-derivations are in
     inc.md [T]. Row `sales.interest_carry_from_2024` replaces `..._2023`. Then `render --check` (s2 and f4952
     labels).
  3. Siblings: `f4952.carryover`, `s2.amt_boat`, `f1040.estimated_any`, `f1040.tax_exempt_any`.
  4. Closures. Note that `research/ty2026/forms-proposed/f1040.yaml:92,110` needs the same gate at adoption
     [T int-amt.md]. That is a request, not an edit.
- **Verification.** The common bar, including `--ny` (int-amt touches the NY fixtures).
- **Reviews** (R1):
  - Transcription, line-scoped:
    - f1040: `tax_exempt_any`, `tax_exempt_interest_if_any`, `line2a`;
    - s2: `amt_boat` and the three redirected reads;
    - f4952 `carryover` and f8853c `line24`, only if an ambiguity-link change makes them due (not checked [T inc.md]).
  - Render: s2 and f1040, line-scoped.
  - Class M: **f1040 and s2**, because the arithmetic path changed.
  - Question reviews: about 17 entries.
  - Screen and false-no: about 13 gate subjects, including `f1040.tax_exempt_any`. The `s2.amt_business` question
    review waits for R2, since L7 rewrites it.
  - Caps:
    - transcription and render, $8;
    - class M f1040 and s2, $12;
    - question reviews, $4;
    - screen and false-no, $4.
- **Landing.** You commit last in B1. The integrator releases `inputs` after L1 merges.
  - Shared files: about 30, all listed in int-amt.md's hunk table. They include `fixtures/2025/{classm*,mutation,defaults,f1040}.json`,
    `fixtures/ny/2025/{it201,classm*,mutation}.json`, `tools/engines/generate_cases.py`, personas 03, 04, 07, 08,
    coverage files, and `ambiguities/2025.yaml` (two new ids).
  - **Merge note for the integrator:** your `interest_dividends` group and L1's `cod_why`/`cod_how` are inserted at
    the same point after `money_b`. Keep all three.

### 3.3 L3 rental: sche-a v2 (rental, Form 8582 for a separate return, royalty, boats, Schedule A counterparts)

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-rental`.
- **Claim:** `python3 tools/claims.py claim rental royalty asset f8582 --reason "mf1 rental"`.
- **Patch.** `$P/sche-a.patch` (v2; 6 files; seven new fixtures in `fixtures/2025/rental.json`).
  - Covers 0775 (conditional frame, A1), 0789 (C2 headings), 0790 (boats refused through `asset.kind_excluded`, A11),
    0836 (f8582 Part II for MFS living together), 0890 (B3 `royalty.amt19`) and the `rental.not_at_risk` three-class
    source.
  - Bank-only additions to `sa.mortgage_interest` and `sa.line5b` (L6 owns `sa.yaml`; you do not touch it).
  - **Not 0907** (it is in L1).
- **Typical filer, and the filer with nothing.**
  - Typical filers: a landlord with one house (persona 19); a home that became a rental on June 1; an MFS landlord who
    lived with the spouse.
  - The filer with nothing: 01. Expect 0 steps and 0 words of change.
  - The refused filer: 11.
- **The risk particular to this lane.** Partial-year division done twice, or not at all.
  - The form already divides by days when personal days are counted. The help divides only when they are not.
  - The new `xsa.rental_then_home_june` case pins this [T sche-int.md].
  - The Schedule A counterparts must land in the same merge as the `amt12` and `amt16` helps. Otherwise the rental
    months are deducted twice (A1).
- **Measure.** Walks 19, 11, 13 (business assets), 02 (Schedule A) and 01. Expect about +20 words for a typical
  landlord and +0 steps [T sche-a.md].
- **Owner decisions.**
  - **OD-10** (0775, wording or refusal or a days input). Default: wording (v2).
  - **OD-11** (0790, boats). Default: refuse (v2). The round-2 alternative is in `/tmp/nightplan/patches/sche-a.patch`.
  - **OD-12** (`f8582.part2_shown`). Default: keep.
  - **OD-14** (review spend). See section 4.
  - **OD-22** (N10). Default: land. Note the `sa.mortgage_interest` help at 78 words: flag it for trimming at its
    next change.
  - The cell-phone question under "communication equipment" over-refuses only. Default: no change, and register
    `amb` text in the note.
- **Work list, ranked.**
  1. Apply. Then build, `render`, `render --check`, `test-fixtures` (all seven `xsa.*` cases).
     - Their hand-predicted values were re-derived twice with no difference [T sche-int.md].
     - Watch `classm.f8582.1-3`; they must not move.
     - Watch the three unverified points listed in sche-int.md: the defaults withheld for MFS; `"$rental": []` with
       `scope.rental` true; the refused `line21` leaving lines 9, 12 and 16 evaluated.
  2. `tick-groups`: `rental_costs_a/b/c` and `asset_kind`.
  3. `interview-coverage --write`. No gate changed, so no row should move.
  4. Siblings (sche-a.md list).
  5. File the pending entry for the not-at-risk gap. The text is in sche-a.md. Use "Fix:" if it lands. File the
     pending entry for the foreign-building ADS gap only if L7 does not.
  6. Closures for 0775, 0789, 0790, 0836 and 0890.
- **Reviews** (R1, except the rental question reviews, which wait for R2 because L7 edits rental entries):
  - **f8582:** transcription, line-scoped: `mfs_together`, `part2`, `part2_shown`, `exception`, lines 4 to 9. Class M.
    Render. The completeness subject changes.
  - **rental:** transcription and render, line-scoped (`amt17`, `not_at_risk`). Class M only if the dry-run lists it.
  - **royalty:** transcription and render (`expenses_any`, `amt19`).
  - **asset:** transcription and render (`kind_excluded`, `screen`).
  - **Questions:** about 15, including `sa.mortgage_interest` and `sa.line5b`.
  - **Screen and false-no:** the 13 `rental.has_*` ticks, `rental.vehicle`, `gate:royalty.expenses_any` and
    `gate:asset.kind_excluded`; false-no only for `rental.not_at_risk`.
  - Caps:
    - transcription and render, $8;
    - class M, $3;
    - questions, $4;
    - screen and false-no, $5.
- **Landing.** No new inputs (`mfs_together` and `part2_shown` are derived [T sche-a.md]). Shared files:
  `fixtures/2025/rental.json` (seven case ids) and the bank entries listed.

### 3.4 L4 credits: older-credits v2 (EIC, energy credit, Form 8862 bans, RMDs, a dependent's filing requirement)

```
Model: claude-sonnet (current Sonnet id per the launch hook)
Class: mechanical
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-credits`.
- **Claim:** `python3 tools/claims.py claim dependent eic f5695 --reason "mf1 credits"`.
- **Patch.** `$P/older-credits.patch` (v2; 4 files; wording only; no fixture changes).
  - Covers 0793, 0796, 0797, 0861 (65+ or blind combined test, A12), 0862 and 0870.
  - Includes bank-only entries `f8863.ban`, `household.credit_disallowed`, `person.rmd_missed` and
    `dependent.ptc_files`.
- **Typical filer, and the filer with nothing.**
  - Typical filers: a heat-pump and solar homeowner (10); a single parent with EIC (03); a retiree couple with RMDs
    (04); a Marketplace household with a dependent (08).
  - The filer with nothing: 01.
- **The risk particular to this lane.** The refusal screens (`credit_disallowed`, `rmd_missed`, `f8863.ban`) must not
  be narrowed by the shorter wording.
  - Each guard kept in v2 is there for a named false No [T older.md], for example the ACTC clause and "even if you
    made up the shortfall later".
  - Do not trim further. A trim that drops a guard is a wrong-value change, and the stop rule applies.
- **Measure.** Walks 10, 03, 04, 08, 07 and 01. Expect 0 steps and fewer help words.
- **Owner decisions.**
  - **OD-18** (0861, wording or compute Chart B). Default: wording.
  - **OD-19** (0797, spouse). Default: keep "you", and record i8862's silence on the closure.
  - **OD-22** (N10: `credit_disallowed` prompt 43, `ptc_files` help 44). Default: land.
- **Work list.**
  1. Apply. Then build, `test-fixtures` (expect no change), `check_twins.py` (expect clean), `tick-groups` (the panel
     tick is at 12 words), `interview-coverage --write`.
  2. Siblings.
  3. Closures, with the residuals named in older-credits.md:
     - 0797: the spouse silence;
     - 0861: married dependents;
     - 0796: a 2025 panel for a 2024 item;
     - 0870: a QDRO alternate payee.
  - Escalate to the coordinator (Opus) on any failure that is not a plain apply or format issue.
- **Reviews** (R1, except the `person.rmd_missed` question review, which goes in R2 with the other person entries):
  - Transcription, line-scoped: `eic.lived_with_relative`, `dependent.ptc_files`, `f5695.panel`, `f5695.line21a`.
  - Render: the same.
  - Questions: 8.
  - Screen and false-no: gates `eic.lived_with_relative`, `dependent.ptc_files`, `f5695.any`, `f5695.panel_if_any`,
    `f5695.line21a`.
  - False-no only: `f8863.aoc_claimed`, `household.claims_8862_credit`, `person.rmd_possible`.
  - Caps:
    - transcription and render, $6;
    - questions, $2;
    - screen and false-no, $3.
- **Landing.** First in B1. No shared files beyond the bank.

### 3.5 L5 ny: older-ny v2 (New York pension subtraction and 529)

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: ny
```

- **Worktree:** `.claude/worktrees/mf1-ny`.
- **Claim:** `python3 tools/claims.py claim ny_it201 --reason "mf1 ny"`.
- **Patch.** `$P/older-ny.patch` (v2; 3 files).
  - 0850: the line 26 gate reads federal 1h disability pensions; two new it201 cases.
  - 0851: `ask.ny_529` asks about any time in 2025. The `529_nonqualified` prompt is restored byte for byte (A8), and
    its help is 53 words.
- **Typical filer, and the filer with nothing.**
  - Typical filers: a retiree with a government pension (ny03); a parent with a New York 529 (ny02).
  - The filer with nothing: ny01.
- **The risk particular to this lane.** The widened gate `gov_pension_candidate` must not ask every wage earner about
  a government pension. It opens only when `dis_pension_wages > 0`.
  - The patch carries two regression cases. They fail on the unpatched tree, which is by design [T older.md].
  - The 529 help must keep K-12 tuition asked in the prompt (A8).
- **Measure.** Walks ny01 to ny05. Expect 0 steps for ny01.
- **Owner decisions.**
  - **OD-20** (name the NY plans). Default: do not.
  - **OD-21** (the 53-word help). Default: keep.
  - **OD-27** (the BUG-0629 closure). That is coordinator bookkeeping, not this lane.
- **Work list.**
  1. Apply. Then build, `test-fixtures --ny` (both new cases pass; `ny.gate.pension_line28_zero` and every pension
     case unchanged), `interview-coverage --write`, `tick-groups`.
  2. The mutation run is not available to a lane (no form filter found in mutate.ts [I]). Name the new
     `gov_pension_candidate` operands in note section 9 for the integrator's full run. An equivalent mutant may need
     an argument, and that is the integrator's.
  3. Closures for 0850 and 0851 (drafts in older-ny.md [T]).
- **Reviews** (R1):
  - Transcription, line-scoped: `has_pension_income` (note), `dis_pension_wages`, `gov_pension_candidate`,
    `gov_pension_if_income`, `gov_said_no`, `ask.ny_529`.
  - Render, line-scoped.
  - **Class M for ny_it201 if `rerun_all.py --dry-run` lists it.** The gate change alters which returns compute line 26.
  - Screen and false-no: gates `gov_pension_if_income`, `gov_said_no`.
  - Questions: `ask.ny_529`, `ask.529_nonqualified`.
  - Caps:
    - transcription and render, $3;
    - class M, $10;
    - samples, $2.
- **Landing.** Second in B1. Shared file: `fixtures/ny/2025/it201.json`, appended cases. L2's int-amt also inserts
  lines into this file; merge by case id.

### 3.6 L6 scha: older-scha v2 + 0817a (or 0817b) (Schedule A gifts, mortgage use, other state taxes, charity carryover)

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-scha`.
- **Claim:** `python3 tools/claims.py claim sa --reason "mf1 scha"`.
- **Patches.**
  1. `$P/older-scha.patch`. It covers:
     - 0803: U.S. charities only; the `sa.line11` source changes;
     - 0805: "substantially improving", with the Pub. 936 gloss;
     - 0815: A7, the SUI fund and "made in 2025"; box 19 is gone.
  2. **`$P/older-scha-0817a.patch`** (OD-16 default). It asks the carryover of every filer:
     - `sa.gift_carryover_if_no_gifts` becomes a copy;
     - it restates 298 fixture cases (`classm*.json`, `mutation.json`);
     - it removes one pinned argument from `engine/src/mutate.ts`;
     - it restates coverage `home.yaml`.

     Or `older-scha-0817b.patch` (a one-hunk rewording) if the owner picks (b). Both are byte-identical to round 2, and
     each applies after v2 older-scha [T older.md].
- **Typical filer, and the filer with nothing.**
  - Typical filers: a couple with a mortgage and children who give to charity (02); an itemizer with a state refund
    (21).
  - The filer with nothing: 01. Also check that a standard-deduction filer is not newly asked about the carryover.
- **The risk particular to this lane.** With 0817a, the line 13 refusal order matters.
  - The new row `home.gifts_and_carryover` answers `charity_limited: false` first, so the second refusal entry is read
    [T older-scha.md].
  - Unverified: whether the walk asks `sa.line11` or `$gift` before the refusal is told. If it does, the row must
    answer them. Never change its end.
  - The mutation pin removal must not leave a stale or missing argument.
- **Measure.** Walks 02, 21, 10 and 01. Expect +1 tick for gift-givers under 0817a, and 0 elsewhere.
- **Owner decisions.**
  - **OD-15** (0803, treaty charities). Default: leave out, with the residual on the closure.
  - **OD-16** (0817, (a) or (b)). Default: (a), which the plan and the red team endorse.
  - **OD-17** (Pub. 936). Default: if S0 did not archive it, drop the gloss sentence from the 0805 help and land the
    prompt only.
  - **OD-22**: `sa.state_tax_other_any` prompt 49 and help 43; the `sa.line11` text over N10 predates this round.
    Default: land.
- **Work list.**
  1. Apply older-scha. Then build, `test-fixtures` (expect no change), `interview-coverage --write`.
  2. Apply 0817a. Then `test-fixtures`: the 298 filled cases must not change. A change means a case relied on an
     unknown gate; stop and report.
  3. `interview-coverage` (the new row and `home.gifts_of_money`), `tick-groups` (`paid_more` is now reached by
     givers).
  4. Name the mutate.ts pin removal in note section 1. The integrator's full run checks it.
  5. Closures for 0803, 0805, 0815 and 0817.
- **Reviews.** sa's question reviews go in R2 together with L3's sa bank entries (one per form per round).
  - Transcription, line-scoped: `sa.line11`. With 0817a, also `sa.gift_carryover_if_no_gifts`, `sa.charity_limited`
    and `sa.charity_limited_if_gifts`.
  - Render.
  - Class M sa (0817a only).
  - Questions: `sa.line11`, `$gift`, `sa.mortgage_other_use`, `sa.state_tax_other_any`, `sa.charity_limited`.
  - Screen and false-no: `sa.has_mortgage_interest`, `sa.charity_limited_if_gifts`, `sa.gift_carryover_if_no_gifts`.
  - False-no only: `sa.gifts`, `sa.state_tax_other_any`.
  - Caps:
    - transcription and render, $4;
    - class M, $7;
    - samples, $3.
- **Landing.** Third in B1. Shared files: `fixtures/2025/{classm,classm.deepseek,classm.gpt,mutation}.json` (one
  inserted line per case, after `"sa.gifts": true`), `engine/src/mutate.ts` (the integrator merges this one by hand,
  per 8.4), and coverage `home.yaml`.

### 3.7 L7 interview (wave 2): int-p18, int-personas, int-n10, then int-n10-ticks and int-rprop if the owner agrees

```
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us
```

- **Worktree:** `.claude/worktrees/mf1-interview`, base `refs/scratch/mf1-base2` (the B1 merge commit).
- **Claim:** none for the bank-only steps. For step 5, `python3 tools/claims.py claim rprop --reason "mf1 interview"`.
- **Patches, in order.** All v2; this order was tested on scratch copies, after sche-a and int-amt [T sche-int.md]:
  1. `int-p18.patch`: the `sales_rare` screen before `$sales`, plus four coverage rows restated.
  2. `int-personas.patch`: personas 21 and 22.
  3. `int-n10.patch`: N10 rewrites, with A2, B1, C4, C5 and C7 applied. It no longer touches `rental.not_at_risk`.
  4. `int-n10-ticks.patch`: the full prompts of 13 tick members, with B2. **Only if OD-23 = yes.**
  5. `int-rprop.after-v2-n10.patch`: `rprop.screen` becomes six boxes plus a gated QIP child. This adds seven inputs
     and claims `inputs` [T int-rprop.md]. **Only if OD-26 = yes.**
     - If it does not apply, the bank edit is scripted for any base: `/tmp/nightplan/scratch/v2-int-rprop/apply_bank.py`.
     - That script only rebases the same edit. Its result must be checked by parsing and by `tick-groups`.
- **Typical filer, and the filer with nothing.**
  - Typical filers: a sales filer refused for an NFT (18); investors (06, 14, 17); a rental house (19); tips (09);
    the itemizer and the NOL filers (21, 22).
  - The filer with nothing: 01. Expect 0 change.
- **The risk particular to this lane.** Shortening a prompt can move a rule out of the filer's sight.
  - The red team caught two cases: the 12-month clause (A2), and "no social security tax taken out", which decides
    Form 8919 (B2).
  - With int-p18, a reorder whose inferred effect fails leaves four coverage rows stale. If `interview-coverage` shows
    them stopping at `proceeds`, revert int-p18's coverage hunk and report [T int-p18.md].
- **Measure.** Expected [I]:
  - persona 18: about 3 fewer steps;
  - personas 21 and 22: complete, or at their gate, with no unanswered question;
  - persona 19: about 62 fewer words if rprop is taken;
  - a nonresidential building placed in service from 2018 to 2025: +1 step (the QIP child, a deviation int-rprop.md
    names).
- **Owner decisions.**
  - **OD-23** (the 25-word limit on tick members' full prompts). Default: do not land int-n10-ticks.
  - **OD-24** (whether the frame counts toward word limits). Default: it counts.
  - **OD-25** (four prompts at exactly 40). Default: accept.
  - **OD-26** (rprop). Default: do not land; record it as a task.
  - **OD-22**: `rprop.basis` at 44; `rental.personal_any` help at 45. Default: land.
- **Work list.**
  1. Apply p18, personas and n10. Then build, `tick-groups`, `interview-coverage --write`, `interview-order` (the
     special refusal no longer late), `interview-rules`.
  2. Walks 18, 06, 14, 17, 19, 11, 09, 21, 22, 01.
  3. Then steps 4 and 5 as decided.
  4. For rprop:
     - `test-fixtures`: `xfix.r11.qip_screen` restated, and six classm cases;
     - the 8 new coverage rows;
     - `render --check`.
  5. File the pending entries drafted in the notes:
     - `refund.you_born` N8 (int-personas.md);
     - foreign building ADS (int-rprop.md);
     - the year-change note that `rprop.new_nonres` compares the recovery year with 8, for the 2026 lane
       (int-rprop.md).
- **Reviews** (R2): question reviews of every entry changed, and false-no samples of `rental.personal_any`,
  `k1s.not_at_risk`, `k1p.not_at_risk`, and the tick members if taken. With rprop:
  - transcription, render and class M of rprop;
  - `screen_review.py --screens rprop.screen` plus the gate;
  - false-no of the seven new inputs;
  - questions of the seven new inputs.

  Caps:
  - questions, $5;
  - samples, $3;
  - rprop transcription, render and class M, $5.
- **Landing.** Alone in B2. Holds `inputs` only with rprop.

---

## 3.8 The integrator (B1 and B2): protocol 8.5, with this round's specifics

1. Work in an integration worktree cut from `main`. Run `git merge --no-ff --no-commit mf1-credits mf1-ny mf1-scha
   mf1-rental mf1-pay mf1-amtpay`. If the octopus refuses, do sequential lane merges in the integration branch (8.5
   step 1).
2. Shared-file rules (8.4):
   - `classm.json`: `tools/merge_classm.py BASE THEIRS OURS OUT`.
   - `mutation.json`, `classm.deepseek.json` and `classm.gpt.json`: merge by case id. Three lanes insert or remove
     single lines in the same cases: L1 removes `s1.cod_unsupported`, L2 inserts `f1040.tax_exempt_any`, L6 inserts
     `sa.gift_carryover`. If a text merge conflicts, re-run the lanes' insertion scripts on the merged file. The
     scripts are under `/tmp/nightplan/scratch/{inc-v2,older-v2,v2-sche-int}/`; move them to durable storage first.
   - Bank: by entry id. Keep the three new groups after `money_b`.
   - `defaults.json`: by input id.
   - Coverage `other.yaml` (L1 and L2): by row id.
   - `it201.json` (L2 and L5): by case id.
   - `mutate.ts`: by hand.
3. Regenerate the generated files. Run `interview-coverage --write`, `tree.py`, `year_changes.py --check`.
4. Drop duplicate pending entries, then `new_bug.py --assign`, then `git add -A`.
5. Run `tools/check_all.sh --tier full`. Mutation needs this: L6's removed pin, L5's new operands, L1's new lines.
6. `git commit -F`. List the lanes, the `BUG-NEW -> BUG-NNNN` lines, the `inputs` release reasons and any
   `Fixture-default-changed:` lines.
7. The coordinator's bookkeeping commit (protocol 9): closures recorded by the lanes, `bug_status.py --write`, TASKS
   rows for review debt and lows, and the coverage documents if a gate changed.

---

## 4. Reviews and spend

**Where and when.** Reviews run on `main` after the batch merge, or in a review worktree with `worktree_data.py clone`
and then `carry-back --dry-run` and `carry-back` (protocol 6.2, 8.2).

**Order of commands for each subject:**
1. `python3 tools/transcription/rerun_all.py --forms <ids> --kinds transcription,render,classm --dry-run`.
2. The run, with `--approve-cost <cap>` where the estimate is above $3.00. Transcription and render are line-scoped by
   default; class M has no line scope.
3. `carry.py`, which runs automatically, and `triage.py` for transcription.

The sampled reviews (screen, false-no, question) use `--dry-run` first. Run them with `--samples` unset, meaning the
milestone's one sample [C tools/transcription/samples.py:21]. Any run above $3 needs `--approve-cost`.
`--force-rerun` is never used without a stated reason.

**Price basis.** The ledger means are per paid call, from `.claude/worktrees/xint/.transcription/costs.jsonl`, rows
since 2026-11-13 [C, read by script]:

| Review | Mean per call |
|---|---|
| transcription | $0.78 |
| render | $0.51 |
| class M | $0.31 per case |
| screen | $0.088 |
| false-no | $0.105 |
| question | $0.148 (from rows before 11-13; none since) |

Per-form figures are the last observed calls for that form, for example s1 class M at 46 cases for $17.39.

| Lane | Transcription | Render | Class M | Questions | Screen + false-no | Lane total | Optional |
|---|---|---|---|---|---|---|---|
| L1 pay (base) | 3.7 | 2.4 | 0 | 2.0 | 1.8 | **9.9** | option B +23.0 (s1 class M about 17.4) |
| L2 amtpay | 2.9 | 3.4 | 10.1 (f1040, s2) | 2.6 | 2.6 | **21.6** | — |
| L3 rental | 3.4 | 2.2 | 1.5 | 2.3 | 3.3 | **12.7** | — |
| L4 credits | 3.8 | 1.3 | 0 | 1.2 | 1.3 | **7.6** | — |
| L5 ny | 0.45 | 0.35 | (9.2 if due) | 0.3 | 0.4 | **1.5** | +9.2 |
| L6 scha (0817a) | 1.0 | 0.4 | 5.0 (sa) | 0.75 | 1.0 | **8.2** | — |
| L7 interview | 0 | 0 | 0 | 2.1 | 0.4 | **2.5** | ticks +1.9; rprop +4 |
| **Sum** | | | | | | **about $64** | **all options: about $103** |

- [I] The estimate is rough: line scoping, cache effects and the carry of repeat rulings change real cost.
  `--dry-run` decides.
- Allow about 30% for a second round on the forms with non-low findings. That makes about **$135** the figure to
  approve.
- **Not counted (OD-31).** int-amt, option B and 0817a restate fixture inputs in the class M files with no value
  change. The g1-f6 lane saw the same and wrote "D6 decides whether that reruns anything"
  [C docs/provisional/lanes/g1-f6.md:15]. I did not find how D6 was resolved. If every changed class M subject were
  rerun, that would be up to about 370 cases × $0.31 ≈ $115.
  - Recommendation: rerun class M only for forms whose arithmetic changed. Those are s1 (option B), f1040, s2, sa,
    f8582, ny_it201 if due, and rprop.
  - CLAUDE.md allows no global re-review "unless a measured defect calls for it".
  - Ask the owner whether the rest should be grandfathered or left due.

---

## 5. Owner decisions, de-duplicated across every plan in /tmp/nightplan

Each decision gives the plan's or red team's recommendation, the default a lane takes if unanswered, and its source.

### 5.1 Decisions that tomorrow's lanes depend on

| # | Decision | Recommendation | Default if unanswered | Lane | From |
|---|---|---|---|---|---|
| OD-1 | 0810 canceled debt: B (two tick groups, a model change) or A (longer prompt, breaks N10) | **B** (red team: sound) | land base only; 0810 stays open | L1 | med-income 1; inc-m12.md |
| OD-2 | 0896 printed digital-asset prompt at 30 words (parent; N10 aim 25) to exclude gift recipients | accept (a wrong printed answer outranks N10) | land | L1 | red team A10, D |
| OD-3 | 0907 NOL help: name rentals, with the Form 8582 guard (replaces med-income decision 6) | A3 text | land | L1 | med-income 6; med-k1sche; red team A3 |
| OD-4 | 0905 extra step for ADR holders | accept | accept | L1 | med-income 7 |
| OD-5 | 0833 Form 4952 with no 2024 form: (a) refusing child, or (b) ambiguity entry with the current wording | (b) now; (a) later if wanted | (b) | L2 | med-income 5; red team A6; inc.md |
| OD-6 | 0873 Medicaid or VA paid to the provider: Form 8853 line 24 reimbursements? | register `amb.2025.f8853c_line24_public`, chosen reading "they count" | v2 | L2 | med-income 3; red team A5 |
| OD-7 | 0897/0894 joint estimated payments: count with the split rule (or refuse); the former-spouse split rests on Pub. 505 (2025), not archived | count with split; archive p505 to confirm the former-spouse half | drop "or former spouse" unless confirmed | L2 | med-income 4; inc-m34.md; inc.md |
| OD-8 | 0900 "used on a transient basis" = rented for short stays | accept (only refuses) | v2 | L2 | med-income 2 |
| OD-9 | 0901 Schedule H and p926: archive before landing (dependency) | archive (S0) | omit the 0901 hunks if not archived | S0, L2 | inc-m34.md; sources README |
| OD-10 | 0775 home converted to a rental: wording, refusal, or a days input | wording (conditional frame, v2) | v2 | L3 | med-k1sche D1; red team A1; sche-int.md |
| OD-11 | 0790 boats: refuse via `asset.kind_excluded`, or name them in `asset.listed` (which computes boats used over 50%) | refuse (red team A11; med-older 6) | v2 (refuse) | L3 | med-k1sche D4; med-older 6 |
| OD-12 | f8582: also hide lines 4 to 9 for MFS living together (`part2_shown`), or arithmetic only | keep | keep | L3 | sche-a.md |
| OD-13 | Latent K-1 entries 0837, 0838, 0841, 0843, 0882, 0886: fix now or with K-1 integration; 0841 refuse with five ticks, or build; 0842/0885 open or tasks | fix now (cheap); 0841 refuse; 0842/0885 tagged | **no lane tomorrow** (no patch drafted); hand to K-1 integration | — | med-k1sche D2, D3 |
| OD-14 | Review spend for this round | approve about $135, with the per-lane caps in section 3 | lanes run no paid reviews; R1/R2 wait for approval | R1, R2 | med-k1sche D5; protocol 6.2 |
| OD-15 | 0803 gifts to treaty charities (Canada, Israel, Mexico): leave out or refuse | leave out; residual on the closure | leave out | L6 | med-older 1 |
| OD-16 | 0817 charity carryover: (a) asked of every filer, or (b) reworded (two subjects in one question) | (a) | (a) | L6 | med-older 2; older-scha.md |
| OD-17 | 0805: archive Pub. 936 so the help can gloss "substantially improve" | archive (S0) | drop the gloss sentence if not archived | S0, L6 | med-older 3 |
| OD-18 | 0861: wording (65+ and blind limits in help) or compute Chart B | wording | wording | L4 | med-older 4 |
| OD-19 | 0797: does a spouse's earlier AOC denial need Form 8862 on a joint return (i8862 silent)? | keep "you" | keep | L4 | med-older 5 |
| OD-20 | 0851: name the NY plans (the Advisor-Guided Plan is not in the archived instructions) | do not name | do not name | L5 | med-older 7 |
| OD-21 | 0851 `529_nonqualified` help at 53 words, keeping the family-transfer sentence | keep 53 | keep | L5 | older.md; red team A8 |
| OD-22 | N10 overruns accepted as guards: f1040.digital_assets prompt 30 / help 42; estimated_any help 44; gambling help 44; rec.two_returns 43; medicaid_waiver 42; tipjob.listed source 41; scope.nol 41; credit_disallowed 43; ptc_files help 44; sa.state_tax_other_any 49/43; sa.mortgage_interest help 78; rental.amt12/16 49; sa.line5b 52; rprop.basis 44; rental.personal_any 45; contractor_pay 30 | accept each where the extra words guard a wrong value; trim `sa.mortgage_interest` at its next change | land as drafted | all | inc.md; older.md; sche-int.md |
| OD-23 | Does N10's 25-word parent limit apply to a tick member's full prompt? | yes (the prompt is the question on the CLI, the last member, "answer on its own" and a reopened answer) | no change: int-n10-ticks not landed | L7 | interview item 5 |
| OD-24 | Does the entry frame count toward word limits? | yes | yes | L7 | interview.md |
| OD-25 | Four prompts at exactly 40 words ("under 40") | accept | accept | L7 | int-n10.md |
| OD-26 | `rprop.screen` taken apart (six boxes and a QIP child; +1 step for nonresidential buildings placed in service 2018 to 2025) | adopt | not landed; task row | L7 | interview item 2; int-rprop.md |
| OD-27 | BUG-0629: record the closure as fixed now (T-295), or "in part" until T-317 | fixed, citing T-317 as the end-to-end proof | coordinator's bookkeeping | coord. | med-older; older-ny.md |
| OD-28 | 0815: the tick stays 12 words without "unemployment" (residual: a PA or AK worker with SUI only) | accept | accept | L6 | older.md |
| OD-29 | `refund.you_born` derived from the birth year (N8), with a question only for 1960 | do it later (a model change); file the entry | file only | L7 | interview.md 3 |
| OD-30 | `sales.special` drops its QOF item once `sd.qof` is asked first (N8) | later | no change | — | int-p18.md |
| OD-31 | Class M subjects changed only by input-only restatements: rerun, grandfather, or leave due | do not rerun; ask whether to grandfather | leave due and list them | R1 | g1-f6.md:15; this file |

### 5.2 Decisions from the other plans (not needed by tomorrow's lanes)

| # | Decision | Recommendation | From |
|---|---|---|---|
| OD-32 | D3: always take the "no Form 1116" election when available | confirm; fix BUG-0774 with it | decisions.md 1 |
| OD-33 | BUG-0774: a Form 2555 filer is denied the election | fix as the entry proposes | decisions.md 1b |
| OD-34 | NY item C on a joint return where only the spouse is claimable | refuse narrowly (joint, federal Yes, NYC or FAGI ≤ $18,000), or ask the owner's NY knowledge first | decisions.md 2 |
| OD-35 | Farm depreciation parent model (Schedule F) | defer until Schedule F is scheduled | decisions.md 3 |
| OD-36 | K-1 decisions D-K1 to D-K16 | confirm all; watch D-K2 (basis asked, not computed) | decisions.md 4 |
| OD-37 | `amb.2025.k1p_prior_with_activity` | reverse: ask every partnership K-1, as a tick | decisions.md 5 |
| OD-38 | T-326: D1 to D14 of the TY2026 plan | confirm all 14 | decisions.md 6 |
| OD-39 | Release list: "release" means verified at run time or at tag time (age limit on entries) | owner policy; sketch: a `RELEASE_LIST_MAX_AGE_H` of 24 | tooling A.3 |
| OD-40 | Screen-review prompts use the interview wording (134 of 149 differ): (a) rerun about $14.50, (b) $0 migration, (c) a pilot of 10 for about $1.10 | (c), then choose | tooling B |
| OD-41 | Mutate: sample fewer withheld-rate copies of fixture sets | owner's call; it weakens the "every case at every rate" claim | mutate R9 |
| OD-42 | ny_mutate: skip the 22 NY band-edge arguments no sample reaches | owner's call | mutate |
| OD-43 | `person.mw_earned`: compute both ways instead of asking | consider; already in the owner's list | judgment-records; jr-verify 6 |
| OD-44 | `household.community_property` domicile (jr-verify, **medium**, new): fix with a domicile prompt plus a spouse-domicile child, or ask domicile only (undoes design D1) | the first; a later lane, not tomorrow | jr-verify 1 |
| OD-45 | `sa.dependent` help (jr-verify 3, low): about 60 words of help, or a child question | the owner's walk | jr-verify 3 |

Effort ratings for questions (T-334) and the owner's walk of the new areas (T-332) stay as the handoff lists them.
They are not repeated here.

---

## 6. Not covered by any lane tomorrow (so the coordinator can decide)

- Open mediums with no drafted patch:
  - the K-1 latent set (OD-13);
  - the jr-verify medium `household.community_property` (OD-44; its pending text is drafted in jr-verify.md);
  - BUG-0842 and 0885 (K-1 integration).
- Bookkeeping-only closures: BUG-0911 (two Fix fields; a closure entry, not a relabel [T sche-a.md]), BUG-0629 and
  BUG-0092.
- Siblings flagged for the next change of their forms, not this round:
  - the `f4952.has_interest` label;
  - the `s2.amt_could` and related labels;
  - the `k1s.past_years` form source;
  - the `gift.deduction` source (foreign organizations);
  - the vacation-home Schedule A steering;
  - the pre-1987 at-risk exemption;
  - BUG-0891 in the new rprop screen.

## 7. Checked versus inferred in this file

- **Checked:**
  - protocol sections 6 and 8 and the stop rule;
  - the pre-commit tier requirement;
  - claims cover form files only;
  - the review tools' flags (`--dry-run`, `--samples`, `--force-rerun`, `--approve-cost`);
  - one sample per milestone;
  - the ledger means;
  - the hunk lists of every v2 patch;
  - no `scope.nol` hunk in v2 sche-a (by grep, after sche-int.md's coordinator change);
  - `draft-walk`'s default output path.
- **Relayed [T]:** every apply-order and fixture-value claim from the v2 notes.
- **Inferred [I]:**
  - the int-amt-then-inc-m34 order;
  - that L7's patches apply on the B1 merge;
  - the spend figures;
  - my reconciliation of "lanes never run check-all" with the pre-commit hook.
