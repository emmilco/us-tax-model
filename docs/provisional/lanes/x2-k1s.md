# Lane x2-k1s: Schedule K-1 (Form 1120-S) and Form 7203

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/x2-k1s`, base
`825024d8` (x1-base, B1 batch-1 merge) plus the newly archived sources (f7203/i7203 Rev. Dec 2022). Nothing
committed. No paid reviews, no model calls from code; `check_all.sh` not run (brief); `mutate` not run (base
caution: it runs at integration). Design: `scout-k1.md` (testimony; the cited pages were re-read here).

## 1. What the merge must know

- **New form files (owned):** `forms/2025/k1s.yaml` (collection under `person`, 170 lines),
  `forms/2025/f7203.yaml` (implicit collection under `k1s`, 61 lines), `fixtures/2025/k1s.json` (17 cases).
- **Shared files, additions only (merge by id):**
  - `forms/2025/person.yaml`: 21 lines `person.k1s_total_*` and `person.k1s_count_sche`, one block delimited by
    `# --- x2-k1s ... ---`, after `# --- end Stage 21 ---`. Each carries `display` (no reader until integration).
    Lane x2-k1p adds its own `person.k1p_total_*` in the same place: distinct ids, adjacent text.
  - `interview/2025/questions.yaml`: frames `k1s`, `f7203`; seven groups `k1s_facts`, `k1s_box_a`, `k1s_box_b`,
    `k1s_box_c`, `k1s_box16`, `k1s_box17`, `k1s_prior` (inserted before `questions:`); 63 bank entries at order
    264, seq 20 to 83 (appended). The scout gives seq 1 to 13 of order 264 to k1p: no collision on my side.
  - `ambiguities/2025.yaml`: four entries appended (`amb.2025.f7203_capital_lines`, `f7203_prorata_places`,
    `f7203_required`, `k1s_qbi_basis`).
  - `fixtures/2025/defaults.json`: 63 defaults appended (`$k1s` empty; every Bool false; every amount 0). The base
    file was replaced by `nx-b1`'s as the brief says; my additions are the script `/tmp/x2-k1s/defaults_patch.py`
    (idempotent; appends, never reorders). Apply it to the integrated file rather than taking this file.
  - `docs/provisional/DECISIONS.md`: section "x2-k1s" appended.
- **No line outside these files reads the new lines**, so no existing value can move; `scope.k1` still refuses
  every K-1 and the k1s questions are not reached by any profile until the integration lane wires
  `person.k1s_total_*` (contract: `/tmp/k1-wiring-k1s.md`, copied in section 7 below).
- Generators (reproducible): `/tmp/x2-k1s/gen/{k1s,f7203,person_k1s,bank,fixtures}.py` (PyYAML from
  `~/.pyenv/versions/3.13.6`). Regenerating `person.yaml` strips and rewrites only the delimited block.

## 2. What changed (computed now, on the K-1 entry; flows wired at integration)

Per Schedule K-1 (Form 1120-S), one activity per box:
- Boxes 1, 2, 3 after the **stock basis limitation** (Form 7203 Part III column (c)), classified:
  box 1 nonpassive when materially participated (tests 1, 3, 5, 6) → Schedule E 28 (k)/(i); otherwise passive;
  box 2 passive, Form 8582 Part IV with active participation (management decisions and at least 10% all year),
  Part V otherwise; box 3 passive (Part V). Prior-year unallowed passive losses (2024 Form 8582 VII (c)) per box.
- Portfolio and other: box 4, 5a, 5b, 7, 8a, 8b, 8c (business-asset type), 13 O, 16 A; 16 B, 16 C, 16 D feed basis;
  17 V QBI (before the passive limitation).
- **Form 7203** (D-K1): Part I lines 1 to 15 and Part III lines 35 to 38, 47, columns (a), (c), (e), figured when the
  K-1 has a loss item or a distribution (amb `f7203_required`); pro rata column (c) by the `prorate` atom, six
  places (amb `f7203_prorata_places`); line 11 capped at line 10; line 15 is the ending basis (display).

Still refused (gate → form; all on `k1s.ok` unless noted, so every exposed line refuses):
`k1s.multi` (box 18/19), `k1s.disposed` (sale, gift, redemption), `k1s.box6` (royalties), `k1s.box8_stmt_if_any`
(8c statement types), `k1s.box9`, `k1s.box10`, `k1s.box11_12`, `k1s.box13_other`, `k1s.box14` (K-3), `k1s.box15`
(AMT), `k1s.box16ef_if_16` (loan repayment, foreign taxes), `k1s.box17_other_if_17`, `k1s.v_other_if_any` (199A
dividends, PTP income), `k1s.mp_other_if_ask` (tests 2, 4, 7), `k1s.former_passive` (prior passive loss of a box-1
activity now materially participated), `k1s.basis_carry` (basis carryover; Schedule E line 27), `k1s.risk_carry`,
`k1s.not_at_risk_if_loss` (Form 6198); on `f7203.one`: `f7203.election_if_req` (1.1367-1(g)),
`f7203.loans_if_req` (Part II), `f7203.dist_over` (distribution above basis → Form 8949),
`f7203.cap_limited` (capital loss limited by basis); on `k1s.qbi`: `k1s.qbi_cut` (QBI loss with a basis cut).

## 3. Decisions (each with the alternative rejected)

Recorded in `docs/provisional/DECISIONS.md` section x2-k1s: D-K1 encode Form 7203 Parts I and III (vs refuse all
S-corp losses/distributions); D-K3 at-risk asked on a loss (vs encode 6198); D-K5 layered material participation
(vs one question); D-K6 allow-list; D-K7 basis part refused, passive part to integration; D-K11 order 264 seq 20+;
D-K16 suffix lines. Lane readings, for the owner: the four ambiguity entries above; capital gains/losses by box,
not netted (3g / 38).

## 4. Gates replaced and residual refusals

None replaced in this lane (no reader yet); `scope.k1` and the `scope.schedule1` list are the integration lane's.
Residuals: section 2. `tools/coverage/tree.json` placement of the new gates: see section 8 (result of
`tree.py --check`).

## 5. Next year (protocol 7.1)

No `changes/2026/` operation is needed for the new forms: every quote they cite from `i1120ssk` and `i8582` was
checked present in the 2026 drafts (one quote shortened to the part both years print: box 16 code D; the i8582
prior-loss quote shortened to drop "2024"). No-change rows for `changes/2026/README.md` (coordinator): f1120ssk
(draft, no change of substance), i1120ssk (draft; only the 17 V threshold changed, not cited), i8582 (cited text
unchanged). **To archive for 2026:** f7203 and i7203 (Rev. Dec 2022 has no 2026 copy in `sources/2026`). Year
literals in prompts ("2024 Form 7203", "2024 Form 8582", "the 10 years before 2025") are moved at adoption by
`year_diff.py`'s candidates. The 2026 active-QBI minimum (`f8995.min_qualifies`) must count K-1 QBI only where
`k1s.material`: integration lane's operation (f8995 is not mine).

## 6. Defects

None found.

## 7. For other lanes and requests (integration)

Wiring contract: `/tmp/k1-wiring-k1s.md` (naming shared with x2-k1p). Requests:
1. Wire `person.k1s_total_*` into Schedules B, D (line 5, 12), the 28% and §1250 worksheets, Schedule E Part II,
   Form 8582 Parts IV/V (and the per-activity VI–VIII chain from `k1s.p{1,2,3}_*`), Form 1040 lines 2a/2b/3a/3b/25c,
   Form 8960 line 4b, Form 8995 line 1 (passive proration of QBI).
2. Box 2 is passive for every shareholder here: refuse a real estate professional (`sche.re_pro`) on any K-1 with
   box 2.
3. Take `scope.k1` out of `scope.schedule1`; then add coverage rows for the k1s refusals (drafts below) and a target
   that reaches the topic. Coverage rows were not added here: no k1s question is reachable while `scope.k1` refuses,
   so `interview-coverage` could not walk them.
4. Excess business loss: `k1s.nonpassive` (box 1 after basis) is the S-corp operand for `s1.ebl_total`.

Draft coverage rows (situation → end): owner with distribution within basis → computed; loss within basis →
computed; loss above basis → computed (13,000 carried); passive investor → computed; each gate of section 2 →
refused at that gate. The 17 fixture cases state the answers for each.

## 8. Verification

| Command | Result |
|---|---|
| `node engine/dist/main.js build` | build OK (after fixes: Count constant type, unread helpers) |
| `python3 tools/citations.py --strict` | exit 0, 0 findings (after fixing 3 quotes) |
| lane cases (`/tmp/x2-k1s/run/k1cases.mjs`: the 17 `k1s.*` cases, defaults resolved by `loadCases`, evaluated by `main.js eval`) | 17/17 match the hand predictions (money, bool, refusal gate/form/remedy) |
| `node engine/dist/main.js test-fixtures` | 1397/2028; every failure outside my cases is the base caution (`s2.amt_owed: input is not declared`, 598) or a pre-existing class M mismatch; my cases' only failures in that run were the missing implicit roster and cite metadata, fixed and re-run above |
| `python3 tools/year_changes.py --check` | exit 0, all 2026 operations apply (no k1s/f7203 operation needed) |
| `python3 tools/check_consumers.py` | 25 new pairs on `k1s` inputs ruled "same" in `reviews/2025/consumers.json` (generator `/tmp/x2-k1s/gen/consumers.py`); 0 open on k1s/f7203 afterwards. Its other findings (sc, sd, s2, f8863) are the base's |
| `python3 tools/coverage/tree.py --check` | the 23 new gates placed in `tools/coverage/tree.json` (topic `other_income`, one line each, inserted after `s1.jury_over`); 0 findings on k1s/f7203; the six remaining findings are base gates of other lanes |
| `node engine/dist/main.js tick-groups` | passed; the seven k1s groups are unreachable on the background return ("not checked here") until integration |
| `siblings.py --check`, `check_bug_inventory.py` | fail on base entries only (none of this lane's) |
| `interview-rules`, `test-fixtures --ny`, `transcription/check_{questions,screens,false_no}.py`, `render` | **not run / not completed**: stopped at the coordinator's deadline (the three transcription checks only reported stale rendered text, since `render` was not rerun) |
| `mutate` | not run (base caution; integration) |

**Shared files touched in addition to section 1:** `reviews/2025/consumers.json` (25 rulings, keys
`consumer:k1s.*`), `tools/coverage/tree.json` (23 gate lines). The integrator should move the 23 placements into a
K-1 topic once one exists (no topic was added here, to avoid colliding with x2-k1p/x2-k1e).

## 9. Review debt (round 2)

New forms: `k1s` and `f7203`: transcription, render, class M (whole). `person`: transcription line-scoped (21 new
lines). Question review of the 63 new questions. Screen and false-no samples for the new gates. Dry-run estimate
not run (no paid calls in a lane).

## 10. Walks

Not recorded: the topic is unreachable until integration (`scope.k1` refuses first). Expected typical walk for an
S-corp owner-operator (box 1, 16 C, 16 D, 17 V): roster, facts screen, three box screens, box 1, box-16 screen,
two amounts, box-17 screen, QBI, statement question, work, 500 hours, prior screen, election, loans, line 1,
line 2: about 19 steps per K-1 [estimate].

## 11. Left open, in rank order

1. Integration wiring (section 7) and the coverage rows/personas it makes walkable.
2. Box 15 (AMT) refuses many owner-operators with depreciation adjustments: the largest residual [inferred].
3. Basis carryovers from earlier years (Form 7203 column (b), Schedule E line 27) refused.
4. Form 7203 Part II (loans from the shareholder).
5. Distributions above basis (Form 8949 capital gain).

## Lane xfix (2026-11-15): review findings fixed

claude-opus-5-5, judgment, tax year 2025, us. Uncommitted.

- BUG-0913: `k1s.past_years` worded as `k1p.five_of_ten` ("materially participate ... its income or loss
  was nonpassive"), tests 5 and 6 kept in one question; help defines a personal service business as i1120ssk p. 4 does.
- BUG-0914: `k1s.not_at_risk` adds money borrowed from another owner or someone related to one. The k1p
  sibling is fixed in worktree x2-k1p (BUG-0772).
- Reviews: line-scoped transcription (20 lines: representation 16, model error 4: the reply requires 2025 work for
  test 5) and render (5 lines: 4 match; 28 (h) scope, the real estate professional case as in round 1).
