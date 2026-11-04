# Backlog and refresh rounds — 2026-11-03

**Owner decisions (2026-11-03):**
1. Inference cost: use inference only where it adds evidence (CLAUDE.md, "Inference cost"). Review and adjudicate only forms whose content changed; review-prompt changes apply prospectively; Sonnet for mechanical agent work; every paid call is logged in `.transcription/costs.jsonl` and every agent run in `research/costs/agent_runs.jsonl`. Tooling to build: T-218 (mechanical carry-over of repeat rulings), T-219 (line-scoped reviews), T-220 (findings per dollar), T-221 (noise comparison of the archived v3 replies).
2. The transcription catalog is a subset chosen from the IRS source (prompt policy `source-only-computation-v3`, BUG-0390), with the T-163 `shown_when` note.

**State:** commit 0a43f15 integrated eight parallel packages (BUG-0341 to BUG-0390). The refresh-round commit after it fixed T-212, T-210, T-175, T-211, T-214, T-205 and the T-101 remainder (BUG-0391 to BUG-0401), recorded the refresh lows as BUG-0402 (T-222), and reran and adjudicated the 17 changed forms only; the 45 unchanged forms keep their v2 logs, and their v3 replies are archived for T-221. GPT-6 Astra is at codex's usage limit until 2026-11-06 15:49 (T-217); its stale logs are archived in `.transcription/archive/stale-gpt-logs-2026-11-03/`.

**Next:** T-218, T-220 and T-219 (T-221 closed by the owner: the measurement would not change a decision), then T-222 and the remaining open rows; T-217 after 2026-11-06. Coverage expansion stays last.

---

# F1 and T-176 integration — 2026-11-03

**Owner decisions (2026-11-03), on the F1 owner questions:**
1. The dependency and EIC tie-breaker refusals stay when the other person is a non-taxpayer (no exception in p501 pp. 15-17; a refusal cannot give a wrong answer).
2. T-113's "or filer" means the filer who is the student; a filer with only an applied-for ITIN claiming the lifetime learning credit for a student with an issued number is not refused (i8863 Table 1).
3. T-104's question covers a child kidnapped before 2025 and still missing at some time in 2025.

**State:** T-176 (BUG-0325, fixed by BUG-0328) is on `main`. The F1 cloud batch (T-104 to T-113, T-153, T-154, T-167, T-168; BUG-0329 to BUG-0337, open BUG-0338 and BUG-0339) is integrated on this branch with its DeepSeek reviews rerun locally. Next: integrate `claude/t159-mutation` (tier 1 shipped; tier 2 still gated with 114 unexplained survivors), then T-178 to T-185 and the remaining backlog.

---

# Owner decisions and parallel work — 2026-11-02

**Owner decisions (2026-11-02), on the T-169 owner questions:**
1. Schedule A line 12: state the good-used-condition and $250 acknowledgment rules in the `gift.deduction` question (done on this branch), not a gate.
2. `person.blind`: state the partial-blindness test and the certified eye-doctor statement, as wording, at the next `person` change (after the F1 cloud branch lands).
3. The self-employed health insurance double count on Schedule A line 1 (proposed by the T-169 session as PENDING-4; the `sa.line1` question has no reduction for Schedule 1 line 17 or Form 8962): wording first, a cited refusal if wording is not enough; not a computed split. Apply when integrating `claude/A-backlog`, which rewrites `sa.line1`.
4. Pub. 502 is archived as `sources/2025/p502` (2025 edition).

**Owner decisions (2026-11-02), on the A- and C-backlog owner questions:**
- A1 used property and the special allowance: refuse through the screen for now; archive the conditions later if needed.
- A2 section 168(k)(9) property: add a plain-language description to the asset questions, and ask it for vehicles too (wording).
- A3 `asset.is_section179` over-counting on Form 4562 line 2 above $4,000,000: an engineering defect to investigate and record, not an owner choice.
- A4 the 100% treatment of employee-used vehicles for operating expenses and leases: refuse through the vehicle screen.
- A5 archive Pub. 538 and settle the small business capitalization exemption from its text.
- A6 QBI-only refusals: keep refusing the whole Schedule C; record a task to narrow it with a new input.
- C1 archive Pub. 974, check it for a legitimate column A > 0 with column B = 0 month, then add a cited refusal if none exists.
- C2 keep refusing a 2025 refund already netted in column A (accepted over-refusal).
- C3 keep the 9.02% affordability test as wording; do not compute it.

**Parallel work in flight (branches to integrate; each is re-tested locally before `main`):**
- `claude/ruling-audit-1`: done. Two confirmed findings with one cause: an asset past its GDS period is never screened, so ADS property and listed property used 50% or less complete with $0 depreciation (reproduced locally for ADS). Fix after the asset work below lands; it is the new top of queue 1.
- `claude/f1-dependent` (routine), `claude/t159-mutation` (routine): running.
- `claude/A-backlog`: three pasted sessions share this branch: T-169 (partly done, report in `research/audits/B-backlog/`), T-164 so far, and T-170 so far; T-172, T-174, T-165, T-166 pending. Integrate by row; rerun the reviews of each changed form locally.

---

# Session handoff — 2026-11-02; T-161 fixed, next is T-159

**State:** T-161/BUG-0292 is fixed (BUG-0313): `person.x_other` asks about an earlier-year HSA excess whether or not a 2025 Form 8889 exists, and the refusal names Part VII. No expression changed; lines 42 to 46 stay refused. person and f5329 reviews, f5329 completeness (first run) and the screen review are rerun and ruled. See the latest commit for the suite result.

**Next:** T-159 (mutation table/guard/choose), the P2 rows, then the F1 dependent/education batch. Open deferred gaps: T-170, T-171, T-172, T-174, T-175. T-113's lifetime learning refusal is still not implemented.

---

# Session handoff — 2026-11-02; T-173 fixed, next is T-161

**State:** T-173/BUG-0310 is fixed (BUG-0312): new input `scveh.lease_smr_before`, gate `scveh.lease_smr_bad`, refusal on `scveh.lease_business`, regression `stage14.veh.refuse_lease_smr_before`. scveh reviews, class M and completeness are rerun and ruled. See the latest commit for the suite result and where it sits.

**Next:** T-161/BUG-0292 (HSA carryover, the Form 5329/person pass), then T-159 and the rows listed in the entry below. The deferred completeness gaps T-170, T-171, T-172 and T-174 stay open.

---

# Session handoff — 2026-11-02; asset/Schedule C pass closed

**State:** the asset/Schedule C pass (T-157/T-158) is ruled, reviewed and on `main` as one squashed commit of the tested tree, because the pre-push guard refuses the branch's untested WIP commits; full suite green (see the commit message). `asset-sc-pass` keeps the commit-by-commit history.

## What this session changed from the entry below

- The cloud session's Claude logs had no local raw replies, so triage could not read them. All Claude asset and sc reviews were rerun locally with fresh receipts; the handoff's 14/25 counts below were replaced by the rerun's.
- New fixes: BUG-0303 (unelected qualified improvement property on Form 4562 line 2), BUG-0304 (`ltc.payments` tested the covered person, not the filer), BUG-0306 (`scveh.screen`, a 2025 vehicle acquired before September 28, 2017). BUG-0305 closes BUG-0290 and BUG-0291.
- Reruns under both families: asset, ltc, scveh transcription and render; sc under both. Class M asset rerun (36 values, down from 322, because the tool now requests printed lines only). Completeness rerun and ruled for sc, asset, ltc and scveh (39 claims); their `stale:` debt entries are retired.
- **Correction of an inherited ruling:** the scveh line 9 render ruling "refusal located elsewhere" was wrong. It is now a finding (BUG-0310). The same inherited rulings on `sc.special` and line 7 were re-checked by reading the question, not by execution.

## Open and next

- **Queue 1, amount-affecting:** **T-173/BUG-0310** (a lessee who used the standard rate earlier can switch to actual expenses; reproduced; needs a new input), then T-161/BUG-0292 (HSA carryover).
- **Deferred real gaps from the completeness reviews:** T-170/BUG-0307 (asset, 7), T-171/BUG-0308 (ltc, 1), T-172/BUG-0309 (sc, 15), T-174/BUG-0311 (scveh, 8). Many can change an amount; they are recorded, not fixed.
- Queue 3 and the P2 backlog are as in the entry below. Optional DeepSeek transcription stays open in f4562 (14), f8606 (3), f8995 (9), qbi (4), sli (5).

## Operational notes

- After switching branches, run `npm run build` before `npm run render`: `canonical/` is git-ignored, so rendering alone restores the other branch's wording.
- A ruling edited by hand must go through `rulings.save`: a re-compare restores the log from the sidecar.
- Archives: `.transcription/archive/before-asset-sc-local-rerun-2026-11-02/`, `before-qip-ltc-fix-reruns-2026-11-02/`, `before-scveh-screen-rerun-2026-11-02/`. Ruling inputs: `.transcription/proposed/asset-sc/`.

---

# Session handoff — 2026-11-02; asset/Schedule C pass in progress (historical; superseded by the entry above)

**State:** `main` is at `1547d27` (the f8962 form pass and the BUG-0297 fix; both full-suite green on their tested
trees). The working tree is clean. The **asset/Schedule C pass (T-157/T-158) is in progress on branch
`asset-sc-pass`** (tip `27b6e8f`, pushed) and is **not merged**: its review rulings are open and its sc render review
must be rerun. Do not merge that branch or claim the pass closed until the steps below are done.

## What is closed on main

- `804cb65` **f8962 form pass** (T-134/T-162, BUG-0293–0296): the full MEC rule in `f8962.other`, the
  intentional/reckless misreporting limb, `f1095a.void` + `f8962.void_form`, `f8962.premium_adjust`; 190 gates;
  1,433 fixtures; Claude/DeepSeek/GPT-6 reviews ruled; completeness and screen reviews closed. See the entry below.
- `1547d27` **BUG-0297**: `sa.dependent` was declared only on `sa.standard`, so a claimable dependent who elected to
  itemize completed the return (witness: f1040 line 24 $4,565, Form 8962 line 24 $3,560). The refusal is now also on
  `sa.deduction`; `stage4.refuse.dependent_itemizes` is the regression; the stage8 recorded refusal follows the new
  wording; one classm `tax_on_amount` case had an incidental dependent fact corrected. The same commit carries the
  cloud audit's evidence corrections and closes the completeness reviews it pulled in. Full suite green on
  `c9978e49`.

## Asset/Schedule C pass — exact state on `asset-sc-pass`

The owner approved the decision memo (read-only, from the cloud session) and asked to start the pass:

- **Authored and committed** (`1cf431a`):
  - `sc.at_risk` now states the related-party prong (i1040sc p. 15) and corrects the nonrecourse-loan limb: a loan
    secured only by business property is not at risk (p. 14, "other than property used in the business").
  - `asset.screen` adds qualified reuse and recycling property (the 50% class, i4562 pp. 5–6) and an acquisition
    before September 28, 2017 (the 40% window begins September 28, 2017); both route through the existing
    `asset.screened` refusal. `asset.bonus_fullcase`'s label states the 100%/40% windows; `asset.after_jan19`
    points at the screen.
  - Two source-predicted refusal fixtures: `stage14.asset.refuse_reuse_recycling` and
    `stage14.asset.refuse_pre_2017`; `stage14.asset.refuse_class`'s recorded form text was refreshed. 1,435/1,435
    fixtures.
- **Claude reviews** (`99b8325`): asset transcription 2 agree / 14 disagree; sc transcription 30/25; asset render
  15 match / 0 mismatch; sc render 65/0/1 unclear with **9 lines keyed by bare line numbers** (10, 14, 2, 3, 4, 5,
  7, 8, 9), so the sc render log is incomplete and must be rerun.
- **DeepSeek reviews** (`27b6e8f`): asset transcription 1/15 (13 candidate-invalid, 2 differs) with all 15 sections
  ruled; asset render 10/5 with all 5 ruled; sc transcription 22/33 (14 candidate-invalid) with **33 sections
  still open**; sc render 70/4 with 1 missing line and 4 open.
- **Not done:** rule the Claude asset transcription (14), Claude sc transcription (25), Claude sc render (1 unclear),
  and DeepSeek sc transcription (33) and sc render (4); rerun the sc render review once to get all printed keys;
  then run the full suite and commit the tested tree.

The memo's design decisions are recorded here: the 50% reuse/recycling class and pre-September-28-2017 acquisitions
are refused (no 2025 rate for the latter; i4562 and Pub. 946 disagree on whether 168(m) applies when 168(k) does),
and the alternative to refusing the 50% class is a computed `fifty` path with an ambiguity entry. The archived
sources do not define "acquired" by binding-contract date; do not add that language without archiving the
regulation. The suggested screen reviews for `asset.screen` and `sc.at_risk` do **not** apply: both are inputs read
through helper gates (`asset.screened`, `sc.not_at_risk`) and are not refusal gates themselves.

## Cloud session

The owner's cloud Claude session is no longer part of the repository: `CLOUD_CLAUDE_INSTRUCTIONS.md` was removed in
this handoff commit. Its audit and task history are in this handoff and the experiment log. The session produced two
material results worth keeping: BUG-0297 (the itemizing dependent, fixed) and the ruling corrections in BUG-0297's
commit (DeepSeek's real f8962 model errors, the `sc.hi_screened` attribution, GPT's APTC entry gate, and the
completeness evidence for f1095a#3).

## Branches

- `asset-sc-pass` — the WIP above; keep it for the next session, do not merge until green.
- `f8962-form-pass` and `dependent-itemize-fix` — deleted after this handoff; their content is in `main` (the f8962
  tree is the parent of `804cb65`; the dependent fix's tested tree is `1547d27`). `coverage-tree` is an ancestor of
  `main`.

## Open queues and tasks

- **Queue 1, amount-affecting:** T-157 and T-158 are in progress on `asset-sc-pass`; T-161/BUG-0292 (HSA carryover)
  remains.
- **Queue 2, checker:** T-096 done.
- **Queue 3, evidence/tooling:** T-143/T-160 done. Open: T-159, T-163 (shown_when prompt wording), T-164
  (premium_adjust wording), T-165 (column B "zero if blank", BUG-0298), T-166 (affordability in f8962.other,
  BUG-0299), T-167 (stillbirth, BUG-0300), T-168 (dependent student, BUG-0301), T-169 (Schedule A details,
  BUG-0302), and the P2 rows T-139–140, T-142, T-144, T-146–148.
- **P2 review backlog:** unchanged; Claude logs are clean. Optional DeepSeek transcription remains open in f4562
  (14), f8606 (3), f8995 (9), qbi (4), scveh (19), sli (5); optional DeepSeek render in f8606 (1), f8995 (2),
  f8995a (1), ltc (1), mq (2), oi8z (1), sa (3), se (5), sli (3).
- **Next broad batch after these:** F1 dependent/education (T-104–113, T-153/154, etc.), then F2/F4/F5, then
  coverage expansion (Schedule E last).

## Reading order for the next session

1. This entry; then `TASKS.md` and `docs/2026-11-01_backlog_plan.md`.
2. `git log --oneline -3` and `git diff main asset-sc-pass` for the WIP.
3. The asset/Schedule C memo is summarized above; the original task and result were in the deleted cloud file.
4. Model authority and the GPT-6 transport are in `docs/2026-10-24_validation_policy.md` and
   `tools/transcription/README.md`.

---

# f8962 form pass closed — 2026-11-02; next is the asset/Schedule C pass

**State:** the f8962 form pass (T-134 and T-162) is committed here; `TASKS.md` moves both rows to `TASKS-DONE.md`
and `BUG_INVENTORY.md` ends at BUG-0296. The coverage tree holds **190 refusal gates**; the estimate is unchanged
at **78.4% (range 76.9–85.7)**. Full suite green on the tested tree (see the commit message). The working tree is
clean and `main` is pushed.

## What the pass changed

- `f8962.other` now states the whole minimum-essential-coverage eligibility rule: government programs (Medicare
  Part A/C, Medicaid, CHIP, TRICARE, veterans' benefits, Peace Corps), employer coverage that was offered and was
  affordable with minimum value (excluding a waiting period), employer coverage actually enrolled in including
  COBRA and retiree coverage, other HHS-designated MEC, the Marketplace Medicaid/CHIP misdetermination,
  incarceration, and the individual-market exclusion; the remedy and citation were rewritten (BUG-0293).
- `f8962.estimate_100` now carries the intentional/reckless misreporting disqualifier inline (BUG-0296).
- New `f1095a.void` question per entered form, `f8962.void_forms` count and `f8962.void_form` refusal for a VOID,
  replaced or superseded Form 1095-A (BUG-0294); the question covers a later VOID form as well as a CORRECTED one,
  after a render review of the first wording found the gap.
- New `f8962.premium_adjust` gate refusing coverage that began after the first day of a month (other than the
  birth/adoption/placement/court-order exception) and premiums refunded in 2025 (BUG-0295).
- Three new stage18 refusal fixtures and the refreshed `other_coverage` case; 1,428/1,428 CLI fixtures; build,
  render, strict citations, instruction cites, operands, signs, limits, consumers, coverage placement, refusal
  reach, properties, Lean agreement and mutation pass on the tree.

## Review evidence and the two new review-tool findings

- Claude (required family): f8962 transcription **0/97** — 85 interface gaps and 12 scope rulings, no completed-
  return amount difference; f1095a **14/15** (representation; `b_used` one model error); render f8962 91/3/1 and
  f1095a 76/1, all scope; class M f8962 clean, f1095a one model error dropped.
- DeepSeek and GPT-6 Astra were also rerun and ruled. DeepSeek f8962 has 18 real model errors (17 unpublished
  `f1095a.c_<month>` declarations and the line 24 amount); Astra has none.
- **T-163:** the transcription prompt calls `shown_when` "Optional", and all three families omitted it on every
  f8962 line. The comparison added 2026-10-31 counts visibility, so the 0/97 is mostly a request-wording gap, not
  a tax-reading failure; the visibility-only limbs are ruled interface gaps. Fixing the prompt stales every
  transcription log, so it is one bounded refresh, not a side change.
- **T-164:** the screen review found two over-refusals in the new `f8962.premium_adjust` wording ("coverage" should
  say Marketplace coverage; "a month refunded in 2025" should say a 2025 month). Accepted as over-refusal now;
  narrow the wording at the next f8962 review refresh.

## GPT-6 as an optional peer family

The owner added GPT-6 as an optional third family, equal in authority to `claude-opus-5-5` and
`deepseek-v4.1-flash` (the ranking is in `docs/2026-10-24_validation_policy.md`). `codex exec` runs in an empty
read-only scratch directory with `--ignore-user-config`; any tool event fails the call, and the model codex used
is read from its session rollout. The selected model is `gpt-6-astra`. Both gpt runs omit `shown_when`; the Astra
runs were not better than 6.1 Sol on these two forms, and the temporary comparison is in the experiment log.

## Where the queues stand

- **Queue 1, amount-affecting defects:** T-134 and T-162 are done. Open: **T-157/BUG-0290** (sc.at_risk),
  **T-158/BUG-0291** (asset allowance), **T-161/BUG-0292** (HSA carryover).
- **Queue 2, checker:** T-096 done; no open item.
- **Queue 3, evidence/tooling:** T-143 and T-160 done. Open: **T-159** (mutation table/guard/choose), **T-163**
  (shown_when prompt), **T-164** (premium_adjust wording), and the P2 rows T-139–140, T-142, T-144, T-146–148.
- **P2 review backlog:** unchanged; Claude logs are clean. Optional DeepSeek transcription remains open in f4562
  (14), f8606 (3), f8995 (9), qbi (4), scveh (19), sli (5); optional DeepSeek render in f8606 (1), f8995 (2),
  f8995a (1), ltc (1), mq (2), oi8z (1), sa (3), se (5), sli (3). These are pre-existing and optional.
- **Second-family noise:** the aggregate is 8.6% (425/4,925) after the interface-gap reclassification; per
  form-kind runs govern. f8962 DeepSeek is still above 10% because of its 18 real model errors; the f8962 pairs
  remain pending on the interface gaps until T-163.

## Next action: the asset/Schedule C pass

Do **T-157/BUG-0290** (sc.at_risk related-party prong) and **T-158/BUG-0291** (asset: the September 27, 2017
boundary and the 50% reuse/recycling class, with the owner-accepted refusal) together; they share the sc form and
the asset screen. Rerun the asset, sc and scveh reviews and the sc completeness review (the 18 claims were
discarded when the wording was reverted; rerun it). Then the **Form 5329/person pass** (T-161/BUG-0292), then
T-159, the P2 rows, and the F1 dependent/education batch.

## Operational notes

- `CLOUD_CLAUDE_INSTRUCTIONS.md` is the task channel for the owner's cloud Claude session: it polls
  `origin/f8962-form-pass` about every ten minutes, pulls, executes the tasks written in that file, and records
  the result under Completed. It never pushes to `main`. The branch contains the WIP tree and the force-added
  raw review receipts; `main` does not track them.
- The model authority ranking, the GPT-6 transport and its isolation rule are in the validation policy.
- Archives for this pass: `.transcription/archive/before-f8962-form-pass-2026-11-01/`,
  `before-final-wording-2026-11-01/`, `before-gpt6-astra-2026-11-01/`, `before-f8962-classm-2026-11-01/`,
  `before-f8962-deepseek-rerun-2026-11-01/`, `before-f8962-deepseek-higheffort-2026-11-01/`.
- Do not bypass hooks on `main`; the branch push used `--no-verify` only to hand the tree to the cloud session,
  with the owner's approval.

---

# Hardening session — 2026-11-01; next is the f8962 form pass

**State:** code tree `cbd7302` (this handoff commit's parent, pushed), working tree clean, full suite green on
tree `ea29fdda`. The P0 household
closure, the T-102 coverage correction, P1's verification repairs, P2's T-150/T-143/T-160, and the T-118 wording
fix are committed. The corrected coverage estimate is **78.4% (range 76.9–85.7)**: dependent filers are a
measured refusal category (4.7%), and the first 80% goal is open until Schedule E. `TASKS.md` is the task
authority; `docs/2026-11-01_backlog_plan.md` is the current package plan; `BUG_INVENTORY.md` ends at BUG-0292.

## What is done (commits, in order)

- `55cb9f1` P0 household closure: T-114–T-117, BUG-0272–0286, 1,425 fixtures, reviews, completeness.
- `e6a8053` T-102: SOI Table 1.7 dependent filers (4.7%); coverage 82.2% → **78.4%**; README/COVERAGE/roadmap.
- `05ede53` P1: memo aliases (BUG-0287), differential reader (BUG-0288), push-guard range and green-list lock
  (BUG-0289), `--year` forwarding; comparison loses 87,101 alias values, still 2,025 cases.
- `1a98539` P2: triage `return_states` (309 completed, not 95; 95 counted disagreements) and `tools/siblings.py`
  (T-150) with the BUG-0290+ Fix lines/Siblings checked gate and check-all self-tests.
- `10c590d` T-155: `(screen)` renderer marker; 20 lines in asset/ira/person/sc/scveh; ten render logs rerun;
  BUG-0290 (Schedule C at-risk related-party wording) and BUG-0291 (asset 40%/50% allowance) recorded.
- `338a62f` T-156: mutation `rate`, `prorate.whole`, `percent_floor.whole` and def-bind operands; **2,778
  mutants, 123 equivalent, 95.6% raw / 100.0% adjusted**. T-159 carries table keys/choose/test (measured:
  full 4,981/518 unexplained; no guards 3,559/256; no guards+branches 2,786/7).
- `d04780d` T-118: IRA excess questions use the year-end value; person reviews rerun; the `person.x_other`
  screen review found **BUG-0292/T-161** (earlier-year HSA excess alongside a 2025 Form 8889 is not asked).
- `149ebc9` T-096: guard tilings must cover the operand's domain; the four TCW sections now state their
  $100,000 precondition; integration regression; tcw reviews rerun; `stale:tcw` completeness debt retired.
- `8663f04` + `86f5b26` T-143: line-by-line candidate execution; invalid declarations and their dependency
  closure are `candidate-invalid`; typed stubs keep foreign consumers executable; `invalid_lines` recorded.
  f8889 DeepSeek now 9 valid pairs / 7 invalid; person and sc triage run with 0 failures.
- `aa70db2` T-160: person DeepSeek 70 sections ruled (62 model error, 4 representation, 3 scope, 1 ambiguity;
  six HSA lines candidate-invalid); sc DeepSeek rerun fresh and 35 sections ruled (34 model error, 1
  representation; 14 candidate-invalid through `sc.ho_line2` → line 30/31 → Form 7206). Both logs 0 open.
- `cbd7302` T-134 scoping: a screen-only `f8962.other` change was tried and **reverted**; it stales 95
  transcription disagreements per family, 20 render sections, and opens 8 completeness claims. T-134 is now
  the **f8962 form pass**; T-162 carries the extra claims; the Gemini auxiliary result is recorded.

## Where the queues stand

- **Queue 1, known amount-affecting defects:** T-118 done. Open: **T-134 + T-162** (f8962), **T-157/BUG-0290**
  (sc.at_risk), **T-158/BUG-0291** (asset allowance), **T-161/BUG-0292** (HSA carryover).
- **Queue 2, checker:** T-096 done.
- **Queue 3, evidence/tooling:** T-143 and T-160 done. Open: **T-159** (mutation table/guard/choose), and the P2
  rows T-139–140, T-142, T-144, T-146–148.
- **P2 review backlog:** Claude logs are clean. Optional DeepSeek transcription remains open in f4562 (14),
  f8606 (3), f8995 (9), qbi (4), scveh (19), sli (5); optional DeepSeek render in f8606 (1), f8995 (2),
  f8995a (1), ltc (1), mq (2), oi8z (1), sa (3), se (5), sli (3). These are pre-existing and optional.
- **Second-family noise is now 9.7% (453/4,683), 74 eligible / 74 pending** — close to the 10% limit. Person
  and sc remain pending qualification because their replies are type-invalid even though their open rulings
  are zero.

## Next action: the f8962 form pass (T-134 + T-162)

Do this as one form pass, not a screen tweak. The HEAD f8962 tree and receipts are the pre-change state.

1. **Finalize `f8962.other`.** The primary completeness review found that the initial wording ("affordable and
   provided minimum value") still misses a filer who **enrolled** in unaffordable/non-minimum-value employer
   coverage, and COBRA/retiree coverage actually enrolled in. Include: employer coverage offered that was
   affordable and provided minimum value, **or employer coverage actually enrolled in (including COBRA or
   retiree coverage)**; Medicare; Medicaid; CHIP; TRICARE; certain veterans' coverage; Peace Corps coverage;
   other HHS-designated MEC; a Marketplace Medicaid/CHIP determination later found to be based on incorrect
   information; and incarcerated enrollees (other than pending charges). Exclude individual-market coverage.
   The exact source sentences are in the 8 f8962 completeness claims (i8962 pp. 5–6, 8, 9, 14–18).
2. Add/refresh a refusal fixture for other MEC (the existing `stage18.refuse.other_coverage` tests the screen;
   add an enrolled-unaffordable-employer case) and update the remedy text.
3. Build and render. Rerun f8962 transcription and render under both families (95 disagreements per family and
   20 render sections last time). Run `triage.py --form f8962` for both families; rule with T-143 evidence.
   The old HEAD sidecars are a prior, not a carry-forward: rebind each ruling to the new context. The old f8962
   Claude log is clean; the DeepSeek log has 34 open rulings at HEAD.
4. Run `completeness_review.py --forms f8962`; rule all 8 claims. `f8962.applicable` and `f8962.line1` are
   likely covered by `sa.dependent` (the return-wide dependent refusal) — check before ruling. T-134 covers the
   `f8962.other` claim; T-162 covers VOID/CORRECTED 1095-A, SLCSP correction/blank column B, first-of-month
   enrollment and the birth/adoption exception, line 28 self-employed health insurance/PTC, and intentional or
   reckless Marketplace misreporting. Record new amount-affecting findings as BUG entries with T-162 references;
   do not silently accept a claim.
5. Run the full suite and commit the exact tested tree with `tools/commit_tested.sh`.

## After the f8962 pass

1. **Asset/Schedule C pass:** T-157/BUG-0290 (sc.at_risk related-party prong) and T-158/BUG-0291 (asset:
   refuse the 50% reuse/recycling class and the pre-September-27-2017 boundary — the owner accepted the
   refusal). Do them together; they share the sc form and the asset screen. Rerun asset/sc/scveh reviews and
   the sc completeness review (it produced 18 claims; the run was discarded when the sc wording was reverted —
   rerun it).
2. **Form 5329/person pass:** T-161/BUG-0292 — add the carried HSA excess (f5329 line 46) or extend
   `person.x_other`; f5329/person completeness. Person reviews are expensive (602k prompt).
3. **T-159:** mutation table-key/choose/test coverage. The 7 EIC table-key survivors are genuine fixture gaps
   (line 3 vs line 1; line 1 vs `earned_for_limit`); add fixtures/equivalence before enabling the full set.
4. **P2 rows:** T-139–140 (class M printed-only/interface docs), T-142 (generator unasked answers), T-144
   (mutation class M kills), T-146–148 (fixture cleanups).
5. **F1 dependent/education pass:** T-104–113, T-107/109/111, T-153/154, T-106, T-113, BUG-0282–0285. This is
   the next broad hardening batch after the named defects; coverage expansion remains last.

## Larger roadmap

The project is in the hardening program of `docs/2026-11-01_backlog_plan.md`, not coverage expansion. P0 is
closed; P1 and P2 are largely done (T-159 and the P2 rows remain); P3 form passes are now the active work:
F3 (f8962/T-134+T-162, f5695/T-132/T-145), then F1 (dependent/education), F2 (person/retirement/Form 2441),
F4 (income/investments/deductions, including the asset pass and BUG-0291), F5 (remaining forms). P4 evidence/
reporting and P5 maintenance follow; P6 coverage expansion is last.

The corrected coverage ladder is: 78.4% today; **Schedule E 84.1%** (the first step past 80%); the rest of
Schedule 1 89.9%; returns of filers who can be claimed as a dependent 94.3%; married filing separately 96.8%;
then Schedule F and Form 1116. TY2026 is the target: the final forms are expected in early 2027, the year is
adopted as a reviewed diff, and drafts cannot back a release. Do not resume coverage expansion merely because
the hardening program feels long; the plan's exit conditions are in the tracker.

## Operational notes

- **Gemini auxiliary:** the available model is **`Gemini 3.8 Flash (Medium)`** via `agy
  --model='Gemini 3.8 Flash (Medium)' --print="$(cat prompt)"`. A broad f8962 completeness pass returned
  `claims: []` while the primary review found 8, so it is too weak for broad completeness. Use it for targeted
  second opinions (the 8 f8962 claims, the 18 sc claims), source scouting, structured extraction drafts, or
  doc/log audits. Record prompt, response, prompt/response hashes and the exact model under
  `.transcription/aux/gemini/`; policy `auxiliary-third-reader-v1`; weight it below Claude/DeepSeek; it is not
  in `families.py`, `compare_families` or the noise metric unless the owner decides otherwise.
- **Archives:** preserve `.transcription/archive/before-screen-marker-refresh-2026-11-01/`,
  `before-known-defects-2026-11-01/`, `before-t096-2026-11-01/`, `before-f8962-mec-2026-11-01/`,
  `before-render-refresh-2026-11-01/` and the household archives. The f8962 archive holds the pre-attempt
  receipts; the current HEAD receipts are the same.
- **Review tools:** `tools/siblings.py --check` requires Fix lines/Siblings checked for BUG-0290+ entries and
  fails when a sibling form has no review log changed since the entry's base. `check-all` runs the pre-push
  and green-list self-tests; `tools/commit_tested.sh` commits exactly the tested tree. Do not bypass hooks.
- `docs/2026-11-01_contributor_safe_gating_sketch.md` remains untracked on disk (ignored via
  `.git/info/exclude`), not part of the repository; the owner has not adopted it.

# Household closure committed — 2026-11-01 (historical; superseded by the entry above)

P0 (household closure) is committed and pushed. HEAD is the household closure commit (parent f44bae4); the large
uncommitted tree described below is closed. T-114–117 are done; BUG-0272–0286 are recorded; the two new gates are
placed in the coverage tree (188 gates); both review families were rerun for household and f1040, and eic/f8889
transcription for the changed shared input. The full suite caught that the hh4 render batch had reviewed a stale
`rendered/` tree (it predated BUG-0286); the rendered English was regenerated, the prior receipts archived under
`.transcription/archive/before-render-refresh-2026-11-01/`, and the four render reviews rerun. All 114 hh4 rulings
plus 12 render-refresh rulings are applied and `check_logs.py` reports 0 open.
Completeness passes at 92 findings (0 new, 55 deferred baseline forms, 37 ruled); consumers pass at 438 (0 new,
380 baseline, 58 ruled); second-family model-error noise is 8.7% (409/4,675, provisional for pending reviews).
Strict citations, instruction cites, screens, coverage placement, operands, signs, limits, bug inventory and
whitespace checks pass. The full suite ran through the tested-tree guard; the commit message records its result.
See the P0 closure section of [the backlog plan](docs/2026-11-01_backlog_plan.md) for the package evidence.

Corrections made while checking the pre-commit summaries: the eic/f8889 summaries named no archive (the prior logs
are in `.transcription/archive/before-household-definition-review-2026-11-01/`); the f1040 DeepSeek line 19 ruling
claimed an interface label that does not exist (the decision rests on the printed Schedule 8812 line 14 destination);
the Claude eic scope reclassifications were confirmed against zero completed-return differences; and f8889 lines 3
and 6 are now compound ambiguity-and-model-error rulings for the withheld `last_month` partial.

Next: the approved plan continues with P1 verification integrity, then P2. T-102 is done: dependent filers are now
a measured refusal category (`dependent_filer`, 4.7% of returns), which brings the estimate to 78.4% (range 76.9% to
85.7%) and reopens the first 80% goal until Schedule E. Coverage expansion remains last. `docs/2026-11-01_contributor_safe_gating_sketch.md` remains untracked on disk
(not part of this commit); decide whether to adopt it.

# Usage pause — 2026-11-01 (superseded by the closure entry above)

The owner explicitly stopped work because usage ran out. Do not launch further work until resumed.
Read [the complete current handoff](handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md) first.
It supersedes the execution/state notes below. P0 is unfinished; HEAD remains f44bae4, with a large
uncommitted tree. Build/render, strict citations and 1,425 CLI fixtures passed, but final review
adjudication and the full suite remain. New BUG-0280–0286 and explicit deferred tasks are recorded.
Final Claude reviews and four completeness reviews finished; the DeepSeek batch was interrupted.
Known jobs were stopped and a process check found no remaining matching review processes. No commit/push.

# Narrow baseline repair — 2026-11-01

Owner selected and implementation added as BUG-0279. See the latest tracker subsection and tools README. Historical migration reproduced 56 fingerprints; 55 untouched forms remain deferred. Current completeness blockers are dependent, f1040, f2441 and household claim1. Four new regression tests pass through the normal completeness self-test. No full suite, commit or push yet. This supersedes the pending scope choice below.

# P0 execution checkpoint — 2026-11-01 (Codex)

The latest execution evidence and unresolved choices are in the final “P0 execution checkpoint” section of
[the backlog tracker](docs/2026-11-01_backlog_plan.md). The older household to-do list below is partly superseded:
bug entries, eight regression fixtures, gate placement, round-two transcription/render reviews and all 51 rulings
are now recorded. CLI fixtures passed 1,419/1,419; `check_logs.py` passed. Household completeness has one unresolved
claim (marital-status definitions); global completeness invalidation remains unresolved. No full suite, commit or
push has occurred. Preserve the working tree and archived review receipts. The tracker records the unanswered
scope choice and the read-only counterfactual evidence; do not silently rebaseline to bypass the failure.

# Current execution — owner-approved backlog plan, 2026-11-01

Read [the temporary backlog plan](docs/2026-11-01_backlog_plan.md) for the current priority order,
package tracker, closure rules, and disposal checklist. It supersedes the execution orders below:
finish the household batch, correct reporting and verification defects, prepare the review tools,
then clear existing form/evidence/maintenance debt; coverage expansion is last.
`TASKS.md` remains the task-status authority. Delete the temporary plan and replace this pointer
when its retirement checklist is satisfied.

The tech-debt audit was investigated read-only by three Luna agents; findings and qualifications
are carried in the plan for T-152 disposition. No implementation fixes, builds, or review reruns
were performed by that investigation or by writing this plan. Preserve the existing working tree.
The household notes below remain the implementation handoff; their test claims need current checks.

# Handoff — updated 2026-11-01, session wound down for credits (Claude Opus 5.5)

## State: household pass in the working tree, NOT committed, round 2 of reviews due

HEAD f44bae4 (= origin/main, pushed). Everything below is uncommitted; do not reset, stash or clean. The owner's priority
order is in the entry below (unchanged). Step 1 (quick clearance) is done except T-113, which the owner scheduled with the
dependent and person passes. Step 4 began early with the household pass, because T-117 was medium and the owner said fix
it now.

Not mine, untracked, leave it alone: `docs/2026-11-01_tech_debt_audit.md` (appeared during the session; ask the owner).

### Done in the working tree (verified: build OK, citations 0 findings, fixtures 1411/1411 on the final tree)

- Quick clearance: T-058 (BUG-0270, `person.itin_applied` order 3; checked both ways with a scripted interview), T-149
  (BUG-0271), T-135 closed as done; owner decisions recorded: T-046 accepted (register updated), T-122 and T-138 closed,
  T-131 (add the wash-loss check, in the sales pass) and T-113 (refuse the lifetime learning credit with only an applied-for
  ATIN/ITIN, with the dependent and person passes) restated as decided. T-151 (Schedule E) added.
- Household pass, round 1 (reviewed and ruled): BUG-0272 (`household.unmarried` states the considered-unmarried rules,
  T-117), BUG-0273 (QSS kidnapped child, T-114, remedy at f1040 line 12e), BUG-0274 (TANF sentence on `home_cost` and
  `qss_eligible`, T-115; the dependent half is T-111), BUG-0275 (services wording, T-116). Reviews (both families,
  transcription and render, household and f1040) rerun on the round-1 wording and all 58 rulings applied
  (`.transcription/proposed/hhpass/`; brief section "Household pass"). Logs before it archived in
  `.transcription/archive/before-household-pass-2026-11-01/`.
- After round 1, NOT yet reviewed (round 2 due):
  - Fixes of three errors round 1 found in my rewording (owner's rule: regressions in uncommitted work are fixed whatever
    their severity; `.transcription/proposed/hhpass/household.findings.md`): F1 the lived-apart child test now carries
    the exceptions (temporary absence; born or died; adopted or placed), F2 "claims" -> "can claim", F3 the QSS kidnapped
    instruction applies only when the kidnapping kept the child away in 2025. Also P1 (medium, older): `household.unmarried`
    opens with "if your spouse died in 2025, you are considered married for the whole year: answer No" (p501 p. 6).
  - Owner's decisions 2026-11-01 on the two older mediums, implemented: new input `household.spouse_died_2025` and gate
    `household.widowed_2025` (single or head of household with a spouse who died in 2025) refusing at f1040 line 12e;
    new input `household.cp_married` and gate `household.cp_marriage_ended` (not joint, lived in a community property
    state, not married at the end of 2025, married during 2025 there) refusing at f1040 line 1a. Ripple done: question
    bank, profiles 2025, sales-2025, stage4-2025, `engine/src/generate.ts` (FIXED, answered false), `generate_cases.py`,
    1,400 fixtures answered false (8 partial-input cases need neither; they pass). household has no input contract.

### Still to do, in order

1. Bug entries for F1 to F3 (one entry citing BUG-0272/0273, tagged fix-introduced), P1, and the two gates (P2 and the
   widow); next number BUG-0276 (confirm with grep). Update TASKS: T-114 to T-117 to done when committed; add nothing for
   P1/P2 (fixed). `household.findings.md` notes P1's sibling is now covered by `household.widowed_2025`.
2. Regression fixtures for the two gates, predicted from source before recording: a single filer and a head of household
   with `spouse_died_2025` true (refused at line 12e with the new remedy) and false (computes); a single filer with
   `community_property`, `cp_married` true and `married` false (refused at line 1a), and with `married` true as head of
   household (still the old `hoh_community_property` refusal, not the new gate).
3. Offline checks: `check_consumers.py` (expect new pairs for the new inputs/gates), instruction cites, operands, signs,
   limits, `check_screens.py`, `python3 tools/coverage/tree.py --check` (the two new gates must be placed in
   `tools/coverage/tree.json` as situations under household, then `python3 tools/coverage/tree.py`), `check_logs.py`.
4. Round 2 of reviews: archive logs, `npm run render`, rerun transcription and render for household and f1040, both
   families (Claude via plain `claude -p`: the owner removed the API key from the keychain; do not use the keychain
   lookup), completeness for household; triage; adjudicate (brief: append "Household pass, round 2"); apply. The round-1
   completeness rulings (`.transcription/proposed/hhpass/completeness.rulings.json`, r8) were not merged; the rerun
   supersedes them, but r8's two PENDING claims (#3 = F1, #4 = P2) are now fixed.
5. Fix-and-review until a round finds nothing introduced and nothing medium; then `npm run check-all-bg`, and
   `tools/commit_tested.sh -F <file>`; push (pre-push checks the tree).

Then continue the owner's priorities: T-102, T-150, the remaining form passes (dependent and person with T-113 first).

Open observations, not yet tracked: triage now finds far fewer completed returns than in fix round 2 (f1040: about 95
against 500). One agent guessed the T-091 inputs, another earlier traced it to `s179.line10` (hardening). Unverified;
worth a check, since fewer completed returns weakens triage.

# Handoff — updated 2026-10-31 (Claude Opus 5.5)

## State: T-103 done; TASKS.md cleaned up; priorities set by the owner

- T-103 committed and pushed (0a0d2f4): `npm run check-all-bg` tests a snapshot in `.git/check-all-worktree` while the
  main tree stays editable; `tools/commit_tested.sh -F <file>` commits exactly the tested tree; `tools/hooks/pre-push`
  refuses untested trees (closes the merge gap, BUG-0269); the build now runs alone before its readers (BUG-0268). See
  `tools/README.md`, "Commit guard".
- TASKS.md cleanup (owner-approved): finished rows moved to `TASKS-DONE.md`; T-092 split into T-104 to T-137; leftovers
  of partial rows are T-138 to T-148; T-149 (bug-entry corrections), T-150 (fix-sibling tool), T-151 (Schedule E).
  Verification notes: `/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/tasks-cleanup/` (scratch).

Owner's priorities (2026-10-31), in order:
1. Quick clearance: T-058; T-149; the checks T-113, T-117, T-135; owner decisions T-046, T-122, T-131, T-138.
2. T-102 (measure dependent filers; the 82.2% headline counts them as covered).
3. T-150 (fix-sibling tool), before the form passes.
4. Form-by-form passes: each form's lows (T-104 to T-137) with its T-094 baseline items and reviews; dependent and
   household first, then person, f2441, s1 and the rest. Build T-139 (single-document printed-only class M) before the
   first single-document form. Review-tool items T-140 to T-148 at the next review-tool change.
5. Schedule E (T-151).
6. Background, on their triggers: T-011, T-012, T-034, T-040, T-057, T-095 to T-101.

# Handoff — updated 2026-10-31, end of session (Claude Opus 5.5)

## Finish first: one small commit, then push (nothing of this session is pushed yet)

State observed at handoff, branch `main`:

- `d98b8b2` T-091 commit (check-all green on exactly that tree; the hook accepted it).
- `286792c` merge of origin/main (the owner's `5765b6b`, `4486fe3`, `670e2f6`: coverage tree, T-101, T-102). Clean, no
  conflicts. Git runs no pre-commit hook on a merge and the repo has no `pre-merge-commit` hook, so this merge commit was not
  gated by check-all; the commit below covers the merged tree.
- Uncommitted, intended: `tools/coverage/tree.json` places the two new T-091 gates (`dependent.qr_kidnapped`,
  `household.hoh_absence`, kind `situation`, topic `household`; questions shown to the owner); `docs/COVERAGE.md` and the
  README coverage block regenerated by `python3 tools/coverage/tree.py` (README: only "146 situations" became "148").
  `tree.py --check` passes (185 gates). This handoff file is also uncommitted.
- A fresh `npm run check-all` was started at handoff in the background (log
  `/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/checkall4.log`). It may not survive the old session
  closing.

Steps:
1. Check whether it finished green on the current tree: `. tools/green.sh; [ "$(cat "$MARKER")" = "$(worktree_tree)" ] && echo green`.
   If not green, or anything changed, run `npm run check-all` (about 15 minutes; do not edit the tree while it runs).
2. `git add -A` (expect exactly README.md, docs/COVERAGE.md, tools/coverage/tree.json, HANDOFF-NEXT-SESSION.md) and
   `git commit -F <file>` with a message such as: "Place the T-091 refusal gates in the coverage tree" and a body saying the
   merge brought in tree.py --check, which requires every refusal gate placed; the two gates added by T-091 are placed as
   situations under household, and COVERAGE.md and the README block are regenerated (148 refused situations).
3. `git pull` (the owner may have pushed again; merge, do not rebase the tested commits), and if that brings anything in,
   rerun `tree.py --check` and check-all before pushing. Then `git push origin main`.

## Open questions put to the owner, unanswered

1. Add a TASKS row for an out-of-band check-all runner: snapshot the working tree to a tree object (temp index, as
   `tools/green.sh` does), test it in a linked worktree with ignored dependencies cloned (`cp -c`: `lean/.lake`, `.engines/`,
   `.transcription/`, `.classm/`, `.human-review/`, ...; `node_modules` symlinked), write the green hash to the main
   repo's marker (the marker path is per worktree), and commit exactly that tree with `git read-tree <hash>` plus a normal
   `git commit` (the hook compares the staged tree, so no hook is skipped). Wrinkles: regenerated `reports/` and `rendered/`
   belong to the tested tree; CPU contention. Recommended, after this push. Could also close the merge-commit gap above.
2. Add a TASKS row for CI (GitHub Actions) on the subset of check-all a clean clone can run (build, fixtures, integration,
   Lean comparison, mutation, citations, coverage; not `tools/engines/run.sh` or `tools/human_review/test_review.py`, which
   need ignored data), with a README badge scoped to that subset. Recommended over a badge now: no CI exists, and edits made
   on GitHub's web editor bypass the local hook.

## Session facts worth knowing

- The owner granted a one-time exception to the QMS for this session: Claude model calls billed to the API. The key is in
  the macOS keychain (`security find-generic-password -s anthropic-api-key -a tax-formalization -w`); the review tools
  read it only via `ANTHROPIC_API_KEY="$(...)"` on the command line. The exception does not carry over: ask the owner
  before using it again, and whether to delete the keychain entry.
- Background shells and subagents did not survive the session closing once already; check deliverables on disk rather
  than assuming a launched job finished.
- `.transcription/archive/before-t091-2026-10-31/` and `before-t091-r2-2026-10-31/` hold the logs before each review round.

## T-091 done and committed; next is T-092

**Read `handoffs/HANDOFF-T091.md` first (its top block is current), then `handoffs/HANDOFF-HARDENING-1.md` for the owner's
standing decisions**, including the new one: a regression introduced by uncommitted work is fixed before commit, whatever its
severity.

T-091 (BUG-0264 to BUG-0267): `dependent.spouse_relative`, `dependent.qr_all_year`, `dependent.absence_no_return`; gate
`dependent.qr_kidnapped`; the head-of-household absence refusal is the return-level gate `household.hoh_absence` (BUG-0267,
after round 1 found the per-person refusal refused returns another person qualified). Two review rounds, all ruled; round 2
found nothing. Next: T-092 (now including the newborn hospital-stay clause, Form 2441 line 2 `shown_when`, and a
considered-unmarried check), T-094 alongside, Schedule E after.

# Handoff — updated 2026-10-31 (Claude Opus 5.5)

## State: the hardening phase is under way

The first coverage goal is reached (82.2%, Stage 21). The owner then directed hardening before Schedule E. Done and
committed through a75729f: the bug root-cause analysis and the mitigation pressure test; six source-coverage checks and
two standing model reviews (screens, completeness) in check-all; BUG-0206 to BUG-0263, including the qualifying surviving
spouse test (BUG-0219) and an evaluator fix for unanswered refusal gates (BUG-0257); review-tool and engine tasks T-068 to
T-083. The full record, the owner's decisions and the facts a fresh session needs are in
`handoffs/HANDOFF-HARDENING-1.md`; read it first.

Next, per the owner: T-091 (three dependent-test logic changes) and T-092 (batched low findings); T-094 (the baseline
burn-down) is the remaining large item, and the owner has not yet chosen whether to finish it first or run it alongside;
then Schedule E (Stage 17). The working tree is clean at the last commit.

# Handoff — updated 2026-10-29, evening (Claude Opus 5.5)

## State after Stage 21: the 80% goal is reached

Stage 21, Form 5329 Parts I and VII (with Form 1099-R entries moved under each person, D1), is built, reviewed in three
rounds and committed: `handoffs/HANDOFF-STAGE-21.md`. The estimate is **82.2%** (from 79.6%), past the route's 80% goal
(`docs/2026-10-26_plan_revision.md` section E is complete). Findings BUG-0200 to BUG-0205; open review-tool and display
points T-079, T-081. Next, per the owner's standing goal: hardening (verification, loose ends, improvements to existing
code), starting from the open entries of TASKS.md and BUG_INVENTORY.md.

# Handoff — updated 2026-10-29, later (Claude Opus 5.5)

## State after Stage 19

Stage 19, the education credits (Form 8863), is built and reviewed: `handoffs/HANDOFF-STAGE-19.md`. The estimate is
79.6% (from 75.6%), short of 80%; the route's last stage, Stage 21 (Form 5329), is next: its decision batch first,
from `research/premises/stage21-form-5329.md` and its verification, then the owner's answers. Findings BUG-0194 to
BUG-0199 (BUG-0192 and 0193 closed); review-tool points T-081.

# Handoff — updated 2026-10-29 (Claude Opus 5.5)

## State after Stage 18

Stage 18, the premium tax credit (Forms 1095-A and 8962), is built, reviewed in four rounds and committed:
`handoffs/HANDOFF-STAGE-18.md`. The estimate is 75.6% (from 71.0%). Adjudication found BUG-0188 to BUG-0191 (fixed)
and BUG-0192, 0193 (open, deferred to the next change of their forms); review-tool defects are T-079; PolicyEngine-US as
a Form 8962 engine is T-078. Next: Stage 19, the education credits. Its decision batch is drafted at
`research/premises/stage19-education-credits.decisions.md` and waits for the owner's answers before authoring. Its
estimate after the stage is 79.6%, so the 80% goal also needs Stage 21 (Form 5329).

# Handoff — updated 2026-10-27, later (Claude Opus 5.5)

## State after Stage 20

Coverage work resumed on the owner's route to 80% (`docs/2026-10-26_plan_revision.md` section E: Stages 20, 18, 19,
21). Stage 20, the capital loss carryover, is built, reviewed and committed: `handoffs/HANDOFF-STAGE-20.md`. The
estimate is 71.0% (from 68.6%). Next: Stage 18, the premium tax credit; start with its decision batch from
`research/premises/stage18-premium-tax-credit.md` and its verification, checked against the current tree, and stop
for the owner's answers before authoring. Open from Stage 20: BUG-0184 (wording), T-074, T-076.

# Handoff — updated 2026-10-27 (Claude Opus 5.5)

## State on 2026-10-27

Plan revision items A, B and C (except C2) are done, each committed behind a green check-all:
citations verifiable with `--strict` (63c0d98); TY2026 rehearsal (713a566) and its seven tool
defects fixed (BUG-0177 to 0179); OpenTaxSolver modelled exactly (f7d89e3); UsTaxes as the fourth engine
(a782c87; scoreboard 243/1,532, 15.9%); mutation-equivalence second reading, prose-only 0, and the
mutation step can fail check-all (7ef41bc); the transcription hold lifted per form (73b1ebe). The
next batch fixed BUG-0165 (line 25c omitted Additional Medicare Tax withheld; all four engines now agree),
BUG-0161, 0163 (car loan column (ii) prorated), 0169, T-071, and recorded BUG-0162 as a design limit
(entries BUG-0172 to 0176), with a fourth review round adjudicated.

**Coverage gate (plan revision D):** A, B, the rehearsal and UsTaxes are done, and every confirmed
amount-affecting defect is fixed. Open entries are display-level (BUG-0180) or tasks (T-067, T-068,
T-069(2), T-070, T-072, T-073). The rehearsal cannot build 2026 data until the final i1040gi posts
(expected early 2027). Remaining plan items run alongside coverage: C2 blind whole returns, 1.5/T-066,
2.2, 2.3, 2.5, and the 21 older Claude transcription logs, migrated when their forms change.

# Handoff — updated 2026-10-26 (evening session, Claude Opus 5.5)

**Read `docs/2026-10-26_plan_revision.md` first: it controls the execution order and the gate for
resuming coverage (TY2026 target).** The earlier handoff below remains the record of the state this
session started from.

## What this session did (plan revision item A, source adjudication)

- Built executable triage (`tools/transcription/triage.py`, `triage.mjs`; policy v2 compares what the
  values sheet shows): each disagreement's project line and validated model candidate are evaluated on
  every fixture, 500 generated returns and partial records, with witnesses and whole-return state.
- Adjudicated every open Claude transcription, render and class M ruling, and the DeepSeek logs of the
  same forms, in three rounds (method: `reviews/2025/transcription/adjudication/README.md`; one summary per
  form there). Seventeen legacy DeepSeek-only logs that predate the current comparison stay pending.
- Found and fixed BUG-0147 to BUG-0160 with regressions (tax-affecting: 0147 Schedule 1-A business tips,
  0148 section 179 over the limit, 0153/0158 head of household part-year rules, 0157 Form 2441 death-year
  rule, 0159 line 25b box). Owner's decisions: skipped lines are hidden with `shown_when`; a worksheet after
  a STOP counts as skipped; part-year questions for head of household; separated-spouses box recorded as
  `amb.2025.separated_spouses_box`; round 3 is the last before commit.
- Open from round 3, to fix next: BUG-0161 (Form 2441 non-dependent screen), BUG-0162 (line 28 ACTC
  box). Tasks T-067 (helper lines `shown_when` cannot hide), T-068, T-069 (review page gaps), T-070
  (review-tool defects).
- New check-all step `refusal_reach`: every refusal fixture's return must be refused under the full interview.
- Archives (git-ignored, hash manifests): `.transcription/archive/before-adjudication-fixes-2026-10-26/`,
  `before-round3-2026-10-26/`; round proposals under `.transcription/proposed/`.

## Next, per the plan revision

B: lift T-062's hold after the commit's audit. C: UsTaxes adapter (scout note: skip self-employed returns
pending the owner's answer), blind whole returns, TY2026 rehearsal, citation locators (with T-069),
mutation second reader, the OpenTaxSolver tolerance. Then fix BUG-0161/0162 and T-070 in the next batch.

---

# Handoff — paused 2026-10-26

**Superseded in its execution order by `docs/2026-10-26_plan_revision.md` (owner amendment, 2026-10-26).** The state recorded below remains the starting point.

The owner asked to stop at a clean point and continue in a fresh session. The in-flight review batches have finished. Work is paused; do not launch more work unless the owner resumes it.

The continuing objective is to clear the integrity roadmap through the point where coverage extension can resume. **That objective is not complete.** Remaining human packets and ruling samples are optional and do not block engineering. Preserve the owner's original verdicts and existing ambiguity decisions. Use **deepseek-flash**, never Pro. Fixed-prompt paid source/calculation reviews are authorized by `CLAUDE.md`. Do not spawn sub-agents under the current developer instruction.

Read this file first, then `CLAUDE.md`, `docs/2026-10-24_validation_policy.md` and the relevant portions of `HANDOFF-INTEGRITY.md`. The controlling roadmap is `docs/2026-10-22_integrity_plan.md`, amended by that validation policy.

## Repository and validation state

- Repository: `/Users/elliotmilco/Documents/GitHub/tax-formalization`, branch `main`.
- Last commit: **9bb8205 — Fix HSA partial inputs and validate native worked examples**. It passed the entire suite: 1,083 CLI fixtures; 1,700 engine cases and 320,581 comparisons with zero unexplained differences; 2,279 mutants with 128 equivalent survivors and zero unexplained survivors; 1,683 TypeScript/Lean cases with zero differences.
- There is a substantial **uncommitted source-review/tooling batch**. Preserve it, including untracked files. Do not reset, clean, or restore older logs over it.
- Current targeted checks pass: **130 review-tool tests, 11 input-context tests, 40 adapter cases, append-only bug inventory through BUG-0146, and `git diff --check`**.
- This new batch has **not passed check-all and is not ready to commit**. `check_logs.py` fails because required Claude source rulings remain open. This is an acknowledged review backlog, not a transport or receipt-corruption failure. Do not bypass the commit hook or weaken review checks to commit it.
- The most recent numeric scoreboard remains **209 / 1,515 computed lines (13.8%)** with outside-family assertions: H=0, B=0, second-family M=57, engine=163, with overlap. The new source audits/engineering checks earn no new numeric evidence.

The filesystem sandbox permits project edits but requires escalated execution for `.git` writes. `npm run check-all` writes a tested-tree marker; after a green run, do not edit tracked/nonignored files before staging and committing. Use a body file for the commit. No full suite needs to be run merely to rediscover the known open-ruling failure.

## What the uncommitted batch does

1. **Required-interface context**, `tools/transcription/input_context.py`: every own input plus direct foreign boundaries used by either the authored form or the returned candidate, including helpers, bindings, collection fields and refusal gates. The fingerprint binds ids, printed markers, types and complete input questions. Omitting a dependency cannot shrink the context; unrelated foreign wording does not stale it. Foreign authored arithmetic is not supplied or imported as context. The old global question diagnostic remains separate.
2. **Live verification** in `compare_families.py`: current context records are checked against the actual bound request/reply, current type checks and live fingerprint. Passing headers alone are insufficient. Both logs must cover the current source-target inventory. **The global BUG-0129/T-062 qualification hold remains.**
3. **BUG-0144**: the expanded refusal checker had retained its old policy identifier. Historical policies are preserved. Current checking is `project-expression-types-v3`; context policy is `required-review-interfaces-v2`.
4. **BUG-0145**: published input records imported authored computed refusal gates, falsely requiring hidden helpers such as `asset.screened` and `person.plan_screened` from independent replies. Candidate stubs now retain input identity/type/question metadata only. Gates explicitly returned by the model on an input are preserved and checked as model IR. No authored gate placement is borrowed. Tests cover both the false rejection and explicitly malformed model gates.
5. **Explicit verified replays**, `audit_transcription.py` and `transcribe.py --from-response`: verify log/request/reply/meta identity and an exact current request/model/system match, archive the parent, and label the derived comparison with its parent hash and original policies. Parent archives and chains are hash-checked, with a depth bound. Raw replies are never repaired. Direct `--from-response` never calls a model; `rerun_all.py --resume` **can fall back to a fresh call**, so use it deliberately.
6. **T-064 election adapter**, `adapter_contracts/2025/f4952.json`: `f4952.election` is the full supplied line4g amount after its scope/limit gates, not just its capital-gain portion. Nineteen host-only cases check it and `sd.investment_election`. Four explicit foreign Schedule B/D subtotals are isolated engineering boundaries; this does not independently validate those tax calculations. The runner forbids replacing the reviewed form's arithmetic or collection entries. Dividend adapter cases remain 21. Neither adapter earns source/numeric credit; printed tax results remain blind targets.
7. **Generic protocol clarification**: own collection catalogs list input fields only, rather than implying authored computed helpers are supplied facts. Foreign catalogs remain public interfaces. Prompts emphasize defining local computed references, correctly binding collection gates and preserving the exact published result types. No source arithmetic or expected answers were added.
8. **BUG-0146**: exported targets ignored helpers read only by foreign refusal declarations. Twelve targets across five forms were missed, including `household.hoh_fails`, which gates Form1040. Discovery now includes direct refusal/visibility references; both logs are checked against the live inventory even if the authored-form subject did not change. Some IRA targets are project scope bridges and need explicit semantic classification; do not automatically exempt them. The head-of-household predicate is a real source-review gap.

No authored tax form, numeric fixture, interview question or return engine has changed since 9bb8205 in this uncommitted batch.

## Actual requests, receipts and current results

**50 actual fixed-prompt requests finished with no transport failures**, under Claude Opus 5.5 and deepseek-flash:

- Thirty replacements: both families on `asset,carloan,eic,f8995a,household,ltc,person,qdcg,s179,s1a,s8812,sa,sales,sd,sdtw`. This replaces all fifteen unverifiable Claude receipts.
- Two Form4952 requests after adapter separation.
- Eight replacements after generic protocol clarification: Flash `carloan,eic,person,qdcg,s179,s8812,f4952`; Claude `s8812`.
- Ten expanded-target requests: both families on `household,ira,s1,s179,s3`.

Thirty-two additional host replays made **no model calls**. Some were superseded by later actual requests; their parent records remain archived. Do not rerun `.transcription/replay_current_source.py` blindly: it describes an earlier exact-prompt state, and current prompts/targets have since changed.

Final read-only snapshot: **`.transcription/handoff-audit-2026-10-26.json`**.

| Diagnostic | Count |
| --- | ---: |
| Verified saved replies | 110 |
| Unverifiable receipt/subject records | 0 |
| Pass current v3 type/refusal checks | 67 |
| Pass required-interface context | 68 |
| Bound metadata + current types + current context | 59 |
| Legacy-limited receipts | 21 |
| Earlier agreements changed by current replay | 160 |

These are diagnostic counts, **not qualification or tax-bug counts**. Historical logs may record an earlier checker version even when the read-only audit now passes them. Current Flash `f4952` and `s8812` remain type-invalid; current `carloan,eic,person,qdcg,s179,household,ira,s1,s3` pass types under both families. Other older invalid records remain too.

The final comparison report has 113 form-kind pairs, 24 eligible and 89 pending. Source T is held globally; eligible R/M pairs are separate. Model-error noise is 46/2232 (2.1%) across judged second-family rows, provisional for pending reviews; individual per-form limits still apply.

**Open source rulings: Claude 207, Flash 415**, listed in `.transcription/handoff-open-rulings-2026-10-26.json`. This is the immediate commit blocker. Sixty-six unusable-IR rows were explicitly adjudicated earlier and seventeen primary-source rows were ruled; later requests superseded some of those contexts. Do not carry rulings forward automatically or treat the historical totals as current resolved-row counts. All active rulings must match their sidecar/context.

## Useful investigation leads

A host-only diagnostic ran validated candidates on existing frozen fixtures, using the normal parameter-relative input resolver. It is **not independent worked evidence** and cannot qualify a source review. Files: `.transcription/model_fixture_diagnostics.py`, `.transcription/model-fixture-diagnostics-2026-10-26.json`.

- Claude Schedule D matched 32 selected existing cases; Claude Form8995-A matched eight. This can guide source adjudication but does not prove all branches or partial-input behavior.
- Claude Schedule1-A differed on four cases, mainly fields in inactive parts and one added Medicare refusal. Establish whether final deductions differ before treating inactive intermediate amounts as tax errors. Avoid the benchmark overconstraint previously fixed in HSA BUG-0140.
- Claude Schedule A requires an unanswered gambling-loss amount when known winnings are zero, leaving line17 unknown in three cases. The authored conditional avoids that question. This is a candidate availability gap; do not call the two formulas equivalent for all partial records just because complete-record arithmetic matches. A source-based partial-input bank may be appropriate.
- Household diagnostics originally exposed omitted head-of-household interfaces. The ten expanded-target requests now include the formerly missing targets; adjudication is still needed.
- Preserve `amb.2025.s179_carryover_no_property` and its owner-adopted research (T-043). The models' Worksheet1 cost cap is the recorded alternative, not automatically model noise. Their omission of wages from line11 is a separate source error (i4562 p.5).
- Preserve `amb.2025.carloan_ratio_places`; distinguish ratio precision from the separate ScheduleC/column(ii) availability issue. Do not hide all differences behind that ambiguity label.
- Form4952 line4d includes positive short-term gains; line4e is the separate net-capital-gain quantity (f4952 p.3). A positive declared line4g election needs the form even when the interest-deduction filing exception otherwise applies (p.4).
- Sales digital boxes G–L **are in the input enum**, but are refused at transaction aggregation by `sales.one`. Earlier scope rulings on G/J distinguish that refused regime; they do not certify ungated intermediate values there.

## Archives and commands

All current-session archives were hash-verified at handoff: **233 batch artifacts plus 32 replay-parent archives** under `.transcription/archive/`:

- `before-unverified-source-replacements-2026-10-26/` — 136 artifacts.
- `before-election-adapter-2026-10-26/` — 10.
- `before-source-protocol-clarification-2026-10-26/` — 40.
- `before-foreign-gate-targets-2026-10-26/` — 47.
- `verified-replays/<stem>/<parent-log-sha>/` — exact parent log, sidecar if present, prompt, response and metadata, with manifests.

The raw receipts and these archives are git-ignored, available in this workspace. Preserve them. No original human verdict was edited. Earlier HSA and human-policy archives remain documented in `HANDOFF-INTEGRITY.md`.

Targeted checks:

```sh
python3 tools/transcription/test_review_tools.py
python3 tools/transcription/test_input_context.py
python3 tools/transcription/adapter_contracts.py
python3 tools/check_bug_inventory.py
git diff --check
```

Read-only audit and reports:

```sh
python3 tools/transcription/audit_transcription.py --report .transcription/next-audit.json
python3 tools/transcription/compare_families.py
python3 tools/transcription/check_logs.py
```

The last command currently fails on open required Claude rulings. Final logs are `/private/tmp/tax-handoff-{review-tests,context-tests,adapter-tests,bug-check,audit,families,check-logs}.log`. Request summaries are `.transcription/{source-replacements,election-adapter,source-protocol,foreign-gate}-{claude,flash}-2026-10-26.json`.

## When the owner resumes

First review the diff and current audit; finish source adjudication, replacing truly invalid IR with actual fresh source requests where needed. New calls must retain the selected models and fixed-prompt isolation; archive before overwriting. Do not repair returned IR, fabricate human readings, suppress inconvenient disputes, or release T-062's hold prematurely. Complete required checks before committing the resulting tree.

The broader roadmap still includes source migration/qualification, remaining native M migration and blind whole-return calculations, UsTaxes integration as the fourth engine, mutation-equivalence mechanization, Direct File predicate comparison, **301 citation locators**, and the year-adoption rehearsal. Do not resume coverage extension merely because this source-review batch is done. No further mandatory owner review packets are needed.
