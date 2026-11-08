# Process retrospective, slice 3: delegation, review and cost

Investigator: claude-opus-5-5 (judgment), read-only. Written 2026-11-07.
Repo: `/Users/elliotmilco/Documents/GitHub/tax-formalization`. Scratch scripts: `/tmp/process-retro/*.py`
(parsed bug inventory: `/tmp/process-retro/bugs.json`, `bugs_cls.json`; categorized agent runs:
`agents_cls.json`).

## 0. Evidence base and the gaps that bound every conclusion

| Source | Covers | Gap |
|---|---|---|
| `research/costs/agent_runs.jsonl` (119 rows) | 2026-11-03 to 11-07 only (last 5 of ~26 days) | No agent run from 10-13 to 11-02 was logged. `cost_usd` null in all 119. `class` is present only in 44 rows (from 11-05). 7 rows are "increment" continuations of earlier rows. `subagent_tokens` is what the task notification reported. I think it is end-of-run context size, not cumulative billed tokens (lane-A shows 815k tokens over 681 tool uses, so cumulative would be orders of magnitude higher), but I have not verified this. |
| `.transcription/costs.jsonl` (1,105 rows) | 2026-11-04 02:07 UTC (11-03 21:07 local) to 11-08 03:35 UTC | Nothing before the refresh round. Claude dollars are the list-price equivalents that `claude -p` reports (quota under a subscription, not cash). DeepSeek/GPT dollars are estimates from list prices (`cost_usd` null in 345 rows; `estimated_cost_usd` used throughout; null in the 57 failed GPT rows). |
| `.transcription/**/*.meta.json` | latest receipt per subject only | Receipts are overwritten, so pre-ledger spend can't be reconstructed (I tried; 1,250 receipts, ~44% null cost). |
| `.transcription/archive/` (~90 "before-X" snapshots) | 10-23 to 11-07 | Usable as a lower bound on how many times each form was re-reviewed. |
| `BUG_INVENTORY.md` (456 entries, BUG-0001 to 0456) | 10-16 to 11-07 | The format changed around BUG-0279: no **Date** field after that (178 entries), so dates come from the text of the Caught-by line. Severity tags are inconsistent ("low"/"medium" appear only from ~0400). Some entries are aggregates (0032 = 25 screens, 0402 = 26 lows, 0414, 0417, 0424). ~38 are closures or follow-ups, not new defects. |

**Consequence.** Dollar and agent-effort claims cover days 22 to 26 (the hardening, NY, UI and gates
phase), not the authoring phase. Bug-discovery claims cover the whole project.

---

## 1. Delegation pattern (agent_runs.jsonl, 11-03 to 11-07)

### 1.1 Volume and mix

| Day | Runs | Tokens (M) | Agent-hours (sum of durations) | Runs > 60 min | Sonnet runs | Sonnet token share |
|---|---:|---:|---:|---:|---:|---:|
| 11-03 | 29 | 8.12 | 14.4 | 1 | 1 | 1.1% |
| 11-04 | 42 | 10.02 | 20.6 | 7 | 1 | 0.7% |
| 11-05 | 7 | 1.79 | 12.5 | 2 | 1 | 3.3% |
| 11-06 | 14 | 3.07 | 7.8 | 0 | 3 | 11.3% |
| 11-07 | 27 | 8.41 | 65.0 | 14 | 3 | 4.6% |
| **Total** | **119** | **31.40** | **120.3** | 24 | 9 | ~3.5% |

Agent-hours greatly exceed wall-clock hours, so the agents ran as **parallel waves**: 29 and 42 runs per
day on 11-03/04 (adjudication and form-pass fan-outs), and lettered lanes A to F plus "wave2" on 11-07.

Size distribution (excluding the one zero-token increment): tokens median 252k (p10 108k, p90 420k, max
815k); duration median 28 min (p10 7, p90 115, max 517); tool uses median 109 (p10 40, p90 234, max 681).
The distribution shifted toward long runs on 11-07: median 68 min, 14 runs over an hour, and four over
3.5 hours (lane-C 517 min, lane-A 438, lane-D 214, gate-round-1 218). One more row, `g2-final-usage`,
logs 1,075 min of wall time from "stuck wait loops". That run is what produced the 11-07 CLAUDE.md
background-wait rule (commit 11883002).

### 1.2 Where agent effort went (my categorization, `/tmp/process-retro/agents.py`)

| Category | Runs | Tokens | Share (tokens) | Share (proxy: tool uses × tokens / 2) |
|---|---:|---:|---:|---:|
| Gates / mutation / engine semantics | 24 | 8.26M | 26.3% | 46.7% |
| Adjudication of paid reviews | 26 | 6.56M | 20.9% | 10.9% |
| Interview / UI / content | 19 | 4.50M | 14.3% | 11.7% |
| Review and check tooling | 16 | 4.16M | 13.2% | 15.8% |
| Form fixes | 13 | 2.84M | 9.0% | 7.2% |
| Research (TY2026, NY) | 9 | 2.39M | 7.6% | 3.4% |
| Independent second readings | 7 | 1.63M | 5.2% | 2.0% |
| Other (Lean, docs, engine maintenance) | 5 | 1.07M | 3.4% | 2.3% |

The second column is a sensitivity check. If `subagent_tokens` is end-of-run context, cumulative cost
grows roughly with turns × context. Under that proxy the eight largest runs make up ~40% of all agent
cost: lane-A 9.7%, lane-C 7.2%, T-254 items 3-4 5.9%, T-245 4.7%, mutation-t2 3.9%, gate-round-1 3.7%,
lane-D 2.8%, t159-tier3 2.6%. **Interpretation (moderate credence):** the cost center was a handful of
long judgment agents doing gates and engine-semantics work. Adjudication, the category the
process-optimization doc targeted (34% of tokens on 11-03/04), is not the largest.

### 1.3 Model and class mix

On 11-03 the owner decided that mechanical work goes to Sonnet. After that decision, 2 of 71 runs on
11-03/04 used Sonnet. The 11-04 optimization doc flagged this (item 6). The `class` field arrived
11-05 (T-241, commit 90d823da). After it, Sonnet ran 6 of 41 runs on 11-06/07, at 4.6 to 11.3% of
tokens. The class labels look generous toward "judgment": the R2/R3/R4 "restructured, no word lost or
added" runs (1.14M tokens) and `archive-missing-forms` were judgment, while the near-identical
`archive-followup` was mechanical. **Adoption was partial.** Measured effect: Sonnet's token share went
from ~1% to ~5-11%.

### 1.4 Rework share

Hand-classified from descriptions (the regex pass over-matched, so each row was checked):

| Kind | Runs (tokens) | Notes |
|---|---|---|
| Abandoned / superseded work | T-251 build, ladder proposal, ladder build, ladder review (1.01M) | Handoff: "the T-251 interview-layer topic layer is superseded and stays unmerged". The formal-gates design replaced it within a day. |
| Built but held | T-254 items 3-4 (0.62M, 222 min) | "only 45a3571 merged, the rest held for the owner"; dependency scheduler "not adopted" (BUG-0441). |
| Rebase / convention conversion | R0-rebase (0.11M), wave2-hsa-rebase (0.08M); lane-A and lane-C "converted to the keep-the-id convention and rebased", "reviews ... over two rounds" (share of 1.48M not separable) | Parallel lanes changed shared conventions mid-flight. |
| Fixups after an independent reading | ny-mutation-fixup (0.19M: the second reading failed 27 of 65 arguments), T-245-final-round (0.05M), t159-final (0.31M, partly continuation) | Real quality catches, and also first-pass defects. |
| "Lows" fix rounds (fix → review → new lows → fix) | r2-forms-a1/a2/b, r3-forms-c1/c2/c3, r3-lows-fix, r2-adjudicate-retirement-pass2 (1.18M) | The loop the 11-04 doc describes (item 4). |
| Null-result re-adjudication after a wording-only change | R2-adjudicate ×3 (0.74M), all "no finding" | Input question text (`expr.source`) is deliberately kept in the transcription subject (`tools/transcription/subjects.py:88-91, 156`), so restructuring the wording stales transcription logs. |

**Measured rework share of logged agent tokens:**
- Strict (abandoned + held + rebase + fixups): ~1.45-2.1M = **4.6-6.6%**.
- Broad (adding the lows rounds and null-result re-adjudication): ~4.0M = **~13%**.

The window covers only 5 days. Earlier rework is visible indirectly: there are 84 dated
"before-X" archive snapshots, including stage 18-21 rounds 2 to 4 (see §2.4).

---

## 2. Review economics

### 2.1 Spend (ledger, list-price equivalent)

Total **$328.30** for 1,105 calls (1,048 ok, 57 failed).

By kind:

| Kind | Calls | $ |
|---|---:|---:|
| Transcription | 298 | 166.32 (Claude 157.63, DeepSeek 3.70, GPT 4.99) |
| Render | 231 | 73.17 (Claude 70.44, DeepSeek 2.73) |
| Completeness | 142 | 46.59 |
| Class M | 275 | 25.77 (Claude 25.00, DeepSeek 0.77) |
| Screen | 111 | 11.27 |
| False-no | 48 | 5.19 |

Claude is 96% of spend ($316). DeepSeek ran 284 calls for $7.19.

By local day: 11-03 (evening only) $148.7; 11-04 $88.7; 11-05 $7.9; 11-06 $1.9; 11-07 $81.2.
**One hour, 11-03 21:00 local, cost $134.26, 41% of the whole ledger.** That hour was the refresh round
after the review-prompt change to the source-derived catalog (policy v3, commit 465bcfc7).

**Unused spend in that hour.** The commit message reads: "Only the 17 changed forms were rerun and
adjudicated; the 45 unchanged forms keep their v2 logs, and their v3 replies are archived". The archive
README (`.transcription/archive/v3-replies-unchanged-forms-2026-11-03/README`) confirms the replies were
"Not adjudicated". Joining the 45 archived subjects to that hour's ledger rows: transcription replies
for unchanged forms cost **$57.94** (Claude $52.71, DeepSeek $2.07, GPT $3.16). That is **18% of the
entire ledger, paid and then not used**, apart from a possible v2/v3 noise comparison. The rule
"review what changed; prompt changes apply prospectively" was written into CLAUDE.md the same
evening, after the spend.

Pre-ledger spend is unknown. The only proxy is committed review-log changes: 1,853 render,
transcription and class M log-file changes before 11-04 against 381 after. If cost scales with that,
the ledger is ~17% of all-time review spend, which implies on the order of $1-2k list-price equivalent
all-time. **Low credence:** prompts grew (catalog, BUG-0390), caching was on throughout, and migrations
rewrote logs without making calls.

### 2.2 Per-call cost: one measured improvement

T-237 (commit ce1e69a1, 11-05) turned prompt caching off for one-shot Claude calls and scoped the
catalog for line-scoped prompts.

Before, the ledger shows a 1-hour cache write on every Claude call, never read. The last cache write
was at 11-05 01:23 UTC and the first uncached call at 03:04 UTC.

| Claude kind | $/call before → after | Input tokens/call before → after | $ per M input-equivalent before → after |
|---|---|---|---|
| Transcription | 1.34 → 0.52 | 144k → 96k | 9.3 → 5.4 |
| Render | 0.90 → 0.26 | 105k → 55k | 8.6 → 4.8 |
| Completeness | 0.37 → 0.26 | 39k → 47k | 9.7 → 5.4 |
| Class M | 0.23 → 0.12 | 25k → 22k | 9.0 → 5.4 |
| Screen | 0.23 → 0.08 | 20k → 11k | 11.2 → 7.1 |

The per-token cost fell ~42%, matching the doc's predicted ~44% (`docs/2026-11-04_process_optimization.md`
item 1). The rest of the drop is smaller prompts. The call mix shifted toward line-scoped calls, so not
all of the per-call change is attributable. **High credence** for the caching effect. The waste ran
from the first `claude -p` review until 11-05, but its size is unmeasurable before 11-04.

### 2.3 Yield by review type and family

Sources: `reports/2025/review_yield.md` (T-220 tool output, window 11-04 02:07 to 11:09 UTC), plus my
attribution of BUG-0402 to 0456 from their Caught-by lines.

Over the whole ledger window (11-03 21:07 local to 11-07):

| Kind | $ | Bug entries caught (window) | Severity of those | $/bug entry |
|---|---:|---|---|---:|
| Completeness (Claude) | 46.59 | 15 (0402†, 0413, 0414†, 0416, 0417†, 0418, 0434, 0435, 0436, 0438, 0443, 0451, 0453, 0455, 0456) | 1 medium (0413, a wrong amount: NUA taxed); the rest low | ~3.1 |
| Screen (Claude) | 11.27 | 3-5 (0433, 0449, 0450; shares 0418, 0447) | low | ~2.3-3.8 |
| False-no (Claude) | 5.19 | 3 (0444, 0447 medium, 0452) | 1 medium | ~1.7 |
| Transcription (all families) | 166.32 | ~1 (0439, a low citation gap; share of 0424) | low | >$150 |
| Render (all families) | 73.17 | ~1 (share of 0416, 0424) | low | ~$70+ |
| Class M (all families) | 25.77 | 0 | — | ∞ |

† = aggregate entry: 0402 holds 26 findings, 0414/0417 several each.

T-220 window table: Claude transcription had 395 rulings and **0 findings**, with 50% model error.
DeepSeek transcription had 140 rulings and 0 findings, with 77% model error. Claude render: $52.87 for
1 finding. DeepSeek render: $2.03 for 2 findings. Class M: 0 findings in either family.

**Test of the CLAUDE.md claim that screen and completeness reviews have the best yield:** supported for
the ledger window, on bugs per dollar, by one to two orders of magnitude. **Credence: high for this
phase.** Disconfirming considerations, each real:

1. **Phase dependence.** All-time catches from the T-220 table: Claude render 54 bugs, Claude
   transcription 43, completeness 67, screen 47. The 10-29 root-cause analysis attributes 34 of the 68
   value-affecting defects in BUG-0001..0210 to Claude render and 4 to transcription. Completeness and
   screen did not exist then (the first completeness run was 10-30, and T-088 also ran 10-30). So
   render and transcription earned their keep while forms were being authored. Their yield collapsed
   once forms matured. The claim describes the current phase, not the project.
2. **Purpose.** Transcription logs also earn second-family qualification credit
   (`compare_families.py`). A zero-finding transcription is evidence of agreement, not pure waste.
   Bugs-per-dollar undervalues it, but the project never priced that evidence.
3. **Severity.** Window completeness findings are almost all "low": 10 of the 14 window entries with
   a disposition say "open, low ... at the form's next substantive change". Bugs per dollar is high,
   but value per dollar is unclear.
4. **Family.** DeepSeek render matched or beat Claude render per finding at ~1/30 the cost: in the
   window 2 findings for $2.03 against 1 for $52.87. All-time, "finding" rulings are 26/601 = 4.3% for
   DeepSeek against 37/993 = 3.7% for Claude. Bug attribution credits only the first catcher, and
   Claude runs first, so DeepSeek's 8 all-time render bugs understate it. DeepSeek class M supplies all
   32 class-M-only mutation kills (optimization doc). DeepSeek transcription is the exception: 1 bug in
   1,488 all-time rulings at 69% noise. **Interpretation:** the cheap family's value depended on the
   review kind; a single cost policy per family would have been wrong.

### 2.4 Rounds per form and re-review after fixes

- **Pre-ledger lower bound.** Number of archive snapshots containing a form's logs: f8889 12, asset
  12, dependent 11 (render and transcription), person 11, f8962 11, household 8, eic 8 (median 3 over
  185 subjects). Dated snapshots per day peak on 10-29 (12; stage 18-21 rounds 2-4) and 11-01 (16;
  the household passes). After 11-04 there are only 4.
- **In the ledger.** I counted Claude passes per (form, kind) per local day, splitting passes at gaps
  over 20 minutes:
  - 11-04: 26 of 90 form-kinds had ≥2 passes. sales was reviewed 4 times each for render,
    completeness and transcription, as the optimization doc noted.
  - 11-07: **81 of 208 form-kinds had ≥2 passes, despite the 11-05 rule "One review per form per
    round, run after all of that form's fixes in the round have landed".** f8889 had 7 completeness,
    5-6 transcription and 5 render passes on 11-07 (gate round 1, wave2 restructure, rebase, owner
    remedy change): $17.54 over 11-03 to 11-07. sb had 6 completeness passes.
  - **Interpretation (moderate):** the rule had no mechanism. Parallel lanes touched the same forms,
    and each lane reviewed its own branch, then reviewed again after rebase. The optional `--force`
    guard proposed in the doc (`rerun_all.py` refusing a second review in a round) was not built.
- **The completeness review behaves like a sampler.** Of the review-caught entries from 11-06/07, 10
  say outright that the defect predates the change that triggered the review: 0433, 0434, 0435, 0436,
  0438, 0443, 0452, 0453, 0455, 0456 ("Pre-existing; not caused by the R3 restructuring, which did not
  touch sales"). f8889 had completeness reviews on 11-03 and twice on 11-04, and still yielded 5 new
  pre-existing lows on 11-07 (0443, 0453). **Interpretation (moderate-high):** one completeness run
  has low recall and returns a different sample of gaps each time. "Review what changed" therefore buys
  a fresh lottery ticket on the whole form at every small change. That feeds the lows loop
  (fix → review → new pre-existing lows → deferred to "next substantive change" → review again).
  Completeness rulings on file: 146, of which 71 "out of scope", 34 "covered", 26 "presentation",
  14 "real gap" and 1 "wrong" (`reviews/2025/completeness/rulings.json`). Half the adjudication load is
  scope noise.

### 2.5 Failures

All 57 failed calls are GPT-6 Astra in one hour (11-04 02:xx UTC): usage limit ×53, websocket ×3,
input too large ×1. `rerun_all.py` kept calling. A circuit breaker landed 11-05 (T-237 item 9). No GPT
call has been made since, so the breaker has not been exercised.

---

## 3. Bug discovery

Catcher by period, from regex classification of Caught-by lines (`/tmp/process-retro/classify.py`;
rough, ±10%):

| Period | Main catchers |
|---|---|
| 10-16 to 10-21 (stages being authored) | Render (Claude) dominant: 24 of 31 on 10-17. Transcription, engine differential, class M. |
| 10-22 to 10-25 | Engine differential and Direct File (8 on 10-22), human-directed audits, DeepSeek render (5 on 10-23), tooling audits (T1/T2 classes). |
| 10-26 to 10-29 | Execution-triaged source adjudication, transcription rounds, blind predictions. Stage authoring ends with Stage 21 on 10-29 (last "Stage N" commits). |
| 10-30 to 11-03 | Completeness (21 on 10-30) and the standing screen review (23 on 10-30, many amount-affecting). Fix-round adjudication. Closures (18 on 11-02). |
| 11-04 to 11-07 | Completeness, screen, false-no, agents and check-all (infrastructure), owner's machine (NY: 0419, 0420, 0425). |

**Owner as catcher.** About 10 entries were actually found by the owner rather than recorded via an
owner decision: 0104, 0105 (packet usability), 0128 (3 MISMATCH in the human item-2 review), 0419,
0420, 0425 (NY on the owner's machine), plus 0089-0092 from audits he directed. Apart from 0128, the
owner found tooling and usability defects, not tax-content defects. Reviews and agents found those.

**Shift in root-cause classes.** Tags are inconsistent; these counts are by tag regex, so trends only:

| Range | Question/wording/definition | Value/computation | Flow/skip | Review tooling |
|---|---:|---:|---:|---:|
| 0001-0105 | 35 | 20 | 3 | 3 |
| 0106-0210 | 17 | 15 | 16 | 10 |
| 0211-0330 | 95 | 3 | 0 | 3 |
| 0331-0456 | 68 | 1 | 0 | 21 |

**Recurrence after process changes:**

- **Flow-control defects (class F)** were 19 of BUG-0001..0210 and nearly vanished afterwards (0332,
  0387/0399). The proposed fix, P2 `check_flow.py`, was **never built** (`tools/check_flow.py` absent).
  The better explanation is that new-stage authoring stopped on 10-29: the RCA itself shows F arising
  in each new stage. **Credence moderate.** This is not evidence that the class was solved; it may
  return with new forms (the NY work is the next test).
- **Incomplete fixes / missed siblings (class I).** A cluster of 8 on 10-30/31 (0250, 0255, 0256,
  0259, 0260, 0266, 0267, 0352), six of them introduced by the fix of another bug. `tools/siblings.py`
  landed 11-01 (T-150, commit 1a98539e). After that, one entry: 0306 on 11-02 ("BUG-0291's fix reached
  only asset"). **Consistent with the tool working (weak to moderate).** The fix-round volume also fell
  after 11-01, so the counts are not normalized.
- **Review-tooling defects (T1).** The RCA observed none after BUG-0146 and credited the 10-26
  tooling freeze. They returned when tooling work resumed: 0388-0392 (catalog omissions), 0407, 0421,
  0424, 0437, 0439. **Interpretation:** the freeze suppressed the class; it didn't cure it. Every
  review-prompt change since has produced its own defects.
- **Decision never reached the encoding (class K)**, P5 `check_decisions.py`: not built. I didn't
  find K entries after 0210 by tag, but tagging changed, so this is unmeasured.

**Latency.** Window entries are mostly long escapes of wording defects in forms authored 10-17 to
10-29 and reviewed several times since (see §2.4). In-stage catching was strong by 10-29 (RCA §3).
Post-hardening finds are low-severity residue.

---

## 4. Feedback loops

| Problem | First visible | Change | Lag | Measured after |
|---|---|---|---|---|
| Review-tool churn (each checker change staled logs) | through 10-26 | Tooling freeze, 10-26 | days | T1 stopped, then resumed with tooling work (§3). Suppression, not a cure. |
| Missed fix siblings | 10-30/31 cluster; RCA P3 10-29 | `siblings.py` + check, 11-01 | 2-3 days | 8 → 1 entries (weak, not normalized). |
| Flow-control defects | RCA P2 10-29 | Not built | — | Class faded with the end of authoring; untested. |
| Global re-review on a prompt change | 11-03 21:00 ($134 in an hour, $58 not used) | CLAUDE.md "review what changed", 11-03 evening | hours, but after the spend | Archive snapshots per day: 16 on 11-01, 10 on 11-03, ≤3 per day after. No hour since 11-03 has passed $36. |
| Cost not measured at all | days 1-21 | Ledger + `costs.py` (11-03), `review_yield.py` (11-04 00:38) | ~3 weeks | Enabled every later row of this table. The single largest process gap. |
| Prompt-cache waste (~44% of Claude spend) | 11-04 doc | T-237, 11-05 | ~1 day | $/M input 9.3 → 5.4 (§2.2). Strong. |
| DeepSeek transcription noise (1 bug / 1,488 rulings) | T-220, 11-04 | Owner decision 11-04: only where credit-eligible | <1 day | DeepSeek transcription calls per day 61 → 8 → 0 → 0 → 10. Effective. |
| GPT usage-limit hammering | 11-04 02:xx | Circuit breaker, 11-05 | 1 day | Untested (no GPT calls since). |
| Opus on mechanical work | 11-03 decision; 11-04 doc measured 59/61 Opus | `class` field + brief rule, 11-05 | 2 days | Sonnet share 1% → 5-11%. Partial. |
| Fix → review → lows loops | 11-04 (sales reviewed 8× in a day) | Rule: one review per form per round; lows wait, 11-05 | 1 day | Not reduced: 11-07 had 81/208 form-kinds with ≥2 passes; f8889 7× completeness. Prose rule without a guard. |
| Stuck agent waits (`pgrep -f`) | 11-07 (G2: 1,075 min wall) | CLAUDE.md rule, 11-07 20:48 | same day | Too early to measure. |
| Worktree review data copied by hand | 11-06 (T-254 item 1: partial `.transcription`, BUG-0431) | `worktree_data.py` + rule, 11-07 | ~1 day | Too early to measure. |

**Pattern.** Once the ledger and yield tool existed, the loop from measurement to change was fast
(hours to 2 days). Changes enforced in code (caching off, family restriction in tooling,
`siblings.py`) show measurable effects. Changes enforced only as prose in CLAUDE.md (one review per
round, Sonnet routing) show weak or no effect, especially under parallel lanes.

---

## 5. What would have been better

All interpretations; credence noted on each.

1. **Instrument cost from day 1** (high). A ledger row per paid call and per agent run costs almost
   nothing. Without it, 21 of 26 days of review and agent spend cannot be judged, and the caching
   waste and global re-reviews ran unpriced.
2. **Decide the re-review scope before spending, not after** (high). The $58 of unadjudicated v3
   replies, and the earlier "before-X" snapshot waves (84 of them), were global reruns triggered by
   tooling or prompt changes. A dry-run cost estimate in `rerun_all.py`, plus an owner gate above a
   threshold, would have caught it.
3. **Match review type to phase** (moderate-high). Render and transcription were the right tools
   while forms were authored. Once stages closed (10-29), spend should have moved to
   completeness/screen/false-no and the cheap family. Instead, Claude transcription remained the
   largest line item ($157.63, 48% of the ledger) for ~0 findings.
4. **Treat completeness as a sampler** (moderate). Low per-run recall plus "review what changed"
   produced recurring pre-existing lows on every small change. Better options: a fixed number of
   independent completeness samples per form per milestone, with the union adjudicated once; or keep
   the rule but don't count pre-existing lows as a reason to rerun.
5. **Put rules where they bind** (moderate-high). "One review per form per round" needed the
   `rerun_all.py --force` guard the doc proposed. Sonnet routing needed a default in the agent launch,
   not a sentence in the brief.
6. **Parallel lanes on shared forms cost rebases, convention conversions and duplicate review rounds**
   (moderate). On 11-07, lanes A and C were "converted to the keep-the-id convention and rebased",
   their reviews ran "over two rounds" ($23.65 for lane A), and f8889 was reviewed by three lanes.
   Fixing conventions before fan-out, or serializing lanes that touch the same form, would have
   avoided some of this.
7. **Design before building** (moderate). The T-251 topic layer and question ladder (1.01M tokens, 4
   runs including an independent review with 43 findings) were superseded by the formal-gates design
   the next day. A design-only proposal run (like T-251-ladder-proposal, 59k) before the build would
   have been cheaper.
8. **Give the owner a cost view per form and phase** (moderate). Today's tools report $/finding by
   kind. The decisions in this report needed $/form/day and $/severity, which needed hand joins.

---

Inspected: the full `agent_runs.jsonl` (all 119 rows, descriptions read); the full `costs.jsonl`
aggregated by kind, family, day, hour, subject and cache tokens; the archive README and subject list
of `v3-replies-unchanged-forms-2026-11-03` joined to ledger rows; archive snapshot directories by date
and subject; `BUG_INVENTORY.md` parsed (456 entries; catcher regex-classified; BUG-0402..0456 read
individually for catcher, severity and pre-existing notes); `reports/2025/review_yield.md`;
`docs/2026-11-04_process_optimization.md`; `docs/2026-10-29_bug_root_cause_analysis.md` (§1-3 and the
proposal list); `docs/2026-10-24_validation_policy.md`; `tools/transcription/subjects.py` (wording
exclusion); the existence and add-dates of `siblings.py`, `check_flow.py` and `check_decisions.py`;
git commit times for T-237, T-241, 465bcfc7 and CLAUDE.md.

Inferred (unverified):
- the meaning of `subagent_tokens`;
- the pre-ledger spend estimate;
- catcher classification for BUG-0001..0401 beyond spot checks (about ±10%);
- the class-I and class-F trend causes;
- whether same-day repeated passes on 11-07 were redundant or reviewed different line scopes. The
  20-minute gap rule is crude, and line-scoped calls on different lines would be miscounted as
  repeats.

Plausible gap: I did not open individual ruling files to verify the T-220 tool's finding counts.
