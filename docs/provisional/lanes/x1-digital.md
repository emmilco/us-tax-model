# Lane x1-digital: digital assets (Form 8949 boxes G to L, Form 1099-DA, Schedule 1 line 8v, the Form 1040 question)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/x1-digital`, base
`refs/scratch/x1-base` (825024d8). Design: `scout-digital-assets.md`; process: `coverage_expansion_protocol.md`.
No paid reviews, no model calls from code; check-all not run (brief); mutate not run (coordinator: the base is broken;
it runs at integration). Nothing committed.

## 1. What the merge must know

- **The base snapshot was taken mid-merge** (coordinator). It does not compile cleanly (`mutate-worker.ts` imports
  `sampledShare`, absent from `mutate.ts`; tsc still emits) and its `fixtures/2025/defaults.json` lacks seven defaults
  and keeps `s2.amt_owed`. To build, the lane copied `nx-b1`'s defaults.json in and applied its own additions on top.
  **Do not take this lane's defaults.json**: apply `/tmp/x1d/defaults_patch.py` (copied below in section 2) to the
  integrated file. It adds the defaults `f1040.digital_assets` = false and `s1.digital_amount` = 0, and one consistency
  rule (never `f1040.digital_assets` false with a `sales.box` of G to L).
- **Class M and mutation cases, input only:** `"f1040.digital_assets": false` added after each `s1.digital_income`
  answer: classm.json 276, classm.deepseek.json 106, classm.gpt.json 6, mutation.json 244, ny classm.json 54, ny
  classm.deepseek.json 55, ny mutation.json 106. The nine cases that list `$sales` without `s1.digital_income`
  (classm.asset.1, classm.s179.1, classm.s179.3, classm.f8889.1.deepseek, classm.dependent.1 to .5.deepseek) were
  evaluated and do not read the new input: nothing added.
- **Restated cases (approved end change, the retired gate `sales.digital`):** `sd.json` `sales.refuse.digital.G` to `.L`
  replaced by computed cases `sales.box.G` to `sales.box.L` (same sale, now with figures; every transaction line, line
  7a, `sd.count`, `sd.filed`). `person.json` `stage14.sep.step1_other_se_income` (a box J sale) now states
  `f1040.digital_assets: true` (input only; its expectations do not read sales).
- **Coverage rows with changed ends (R5, deliberate):** `sales.crypto_sold` (refused `sales[a].digital` → proceeds)
  and `other.digital_income` (refused `s1.line8_other` → proceeds). Rows `other.professional_gambler` and
  `other.canceled_debt_exception` lose the answer `s1.digital_income: false`: the question is now asked only beneath a
  Yes to the Form 1040 question, so it was a stale answer (path restated, end unchanged).
- **Moved question:** `s1.digital_income` leaves tick group `money_b` (161/5) for 159/2, beneath `f1040.digital_assets`.
- **Shared lines changed:** `s1.line9` (adds 8v; cite), `s1.line8_other` (drops the digital disjunct and the 8v quote),
  `f1040.line7a` (a refusal entry added), three lines after `f1040.status`, `f8960.line7` (a refusal entry added) and
  a new line after it. Schedule E's s1.line10 and f8960 lines 4a/4c/unsupported are untouched. `sd.filed` changed (D6).
- **tree.json:** gates placed/retired; the Investments row of the table edited (crypto moves to covered; refused
  list empty) because `tree.py --check` refuses a table that names a retired gate. Table changes are the integrator's:
  please review.
- **tools/engines/generate_cases.py** (full tier): input-only fix so generated returns answer `f1040.digital_assets`
  False and the line 8 screen no longer lists `s1.digital_income`. G to L mapping in the engines is the L3 follow-on.
- **Personas 17 and 18** (14 is the Form 1116 scout's).
- **reviews/2025/consumers.json not edited:** `check_consumers.py` reports two new findings
  (`consumer:s1.digital_income@i1040gi:p15`, `@p16`: the new gate line reads the input and cites the page-1 question)
  and two stale rulings (`@i1040gi:p91`, `@p92`). Ruling them is review work, left to round 2. The other 36 new and
  stale findings name other lanes' lines.
- Research map: `research/ty2026/changes.md` l. 489 (i8960 "no digital-asset income path") is now false; integrator.

## 2. What changed

- `forms/2025/sales.yaml`: refusal on `sales.digital` removed from `sales.one` (the line stays, read by
  `f1040.digital_sales`); `sales.covered` adds G and J; `sales.bad_code` adds I and L to the code-B-without-a-report
  test; wording and cites (box text and the never-C-or-F rule on `sales.box`; 1099-DA boxes on proceeds, basis,
  aggregate conditions; swap proceeds; digital-asset basis; wash sales only for tokenized securities; NFT-collectible
  bullet on `sales.special`); ambiguities linked on `sales.special` and `sales.wash_loss`.
- `forms/2025/sd.yaml`: the 32 line filters pair A/G, B/H, C/I, D/J, E/K, F/L (T-003 first half); `sd.filed` (D6).
- `forms/2025/s1.yaml`: `s1.digital_income` (gated, label rewritten), `s1.digital_income_if_assets`, `s1.digital_amount`,
  `s1.line8v`; `s1.line9`, `s1.line8_other` as above. The line 9 remedy is unchanged (an edit moved an existing
  expectation, so it was reverted); it does not list line 8v among the computed items (left open).
- `forms/2025/f1040.yaml`: `f1040.digital_assets` (printed "Digital Assets"), `f1040.digital_sales`,
  `f1040.digital_conflict` (entry check, refused at line 7a).
- `forms/2025/f8960.yaml`: `f8960.digital_nii` and its refusal at line 7.
- `ambiguities/2025.yaml`: digital_wash, digital_transaction_costs (unlinked), nft_collectible, digital_income_value,
  digital_8v_nii. `interview/2025/conflict_checks.yaml`: f1040.digital_conflict.
- Questions: new `f1040.digital_assets` (159/1) "In 2025, did you (or, on a joint return, your spouse) receive, sell,
  trade, spend or give away crypto or another digital asset?"; `s1.digital_income` (159/2) "Did you (or, on a joint
  return, your spouse) receive any crypto from staking, from mining that is not a business, or when a coin split in two
  (a fork)?"; `s1.digital_amount` (159/3) "What was all of it worth, in dollars, when received?". Reworded: `$sales`,
  `sales.box` (help, prompt, C/F labels), `sales.code` W label, `sales.special` (NFT bullet, its own line),
  `sales.proceeds`, `sales.reported_basis`, `sales.correct_basis` help. Not touched (g1-f6's lines): `sales.wash_loss`
  bank entry, `sales.code` "other" label, `sd.qof`.
- Fixtures (hand-predicted; scripts `/tmp/x1d/fixtures.py`, `fixtures2.py`): sd.json 6 restated + 7 new; sales.json
  20 new; s1.json 5 new; f1040.json 3 new (listed in the report).
- `changes/2026/f1040.x1-digital.yaml` (C-X1-F1040-01), `changes/2026/f8960.x1-digital.yaml` (C-X1-F8960-01): cite
  set operations on the 2026 drafts (question on page 2, Other Information; i8960 reminder "Income from", page 2).

defaults patch (`/tmp/x1d/defaults_patch.py`): insert before `f1040.status` the default `f1040.digital_assets` false
("Closed: no digital asset received, sold, exchanged or otherwise disposed of in 2025 unless the scenario says so; a case
with a sale under box G to L states Yes."), before `s1.digital_income` the default `s1.digital_amount` 0, and first in
`consistency` the rule never [`f1040.digital_assets` is false, `sales.box` in G..L].

## 3. Decisions (settled as the scout recommends; DECISIONS.md section "X1 lane x1-digital")

D1 encode the Form 1040 question with an entry check (rejected: leave it out). D2 refuse an NFT of a collectible
(rejected: treat every NFT as ordinary). D3 refuse line 8v over the NIIT threshold (rejected: treat it as not NII).
D4 code E stays refused. D5 code W allowed on G to L (rejected: refuse). D6 done here (below). D7 accept the
unmeasured gain. D8 code M stays out of scope. Lane choices: the conflict refusal sits on line 7a, not on the input,
so `s1.digital_income` is not held back until sales are answered; 8v examples limited to the archived ones (staking,
mining, forks; "airdrop" dropped, Rev. Rul. 2019-24 not archived); the NIIT refusal's cite is unquoted (its quote
changes in 2026), the gate line carries the quote.

**D6 (T-003 second half).** `sd.filed` now tests `div.box2b_if_capital_gain` > 0 and `div.box2d_if_capital_gain` > 0
(the raw Form 1099-DIV boxes the i1040gi p. 31 exception names) instead of `sd.line18` and `sd.line19`. No fixture
expectation moved (test-fixtures below). T-003 can close.

## 4. Gates replaced and residual refusals

Retired: `sales.digital`. Narrowed: `s1.line8_other` (8v), `sales.bad_code` (I, L added), `sales.special` (NFT).
New: `f8960.digital_nii` (situation), `f1040.digital_conflict` (entry). Residual: codes E, L, D, O, N, M
(`sales.bad_code`), lost or stolen crypto (`sd.casualty`), QOF and collectibles (`sales.special`).

## 5. Next year

Two citation operations (above); the 2026 f8949, f1040sd and f1040s1 drafts change nothing here (scout, [V] word
diff); i8949, i1040sd, i1040gi, f1099da, i1099da 2026 not posted (awaited). No new parameters or tables.
`year_changes.py --check`: all 132 entries apply.

## 6. Defects

None filed. The base breakages are the coordinator's snapshot. Scout finding R3 (OpenTaxSolver overwrites A/G
totals) is an external engine defect for the L3 lane.

## 7. Requests

Integrator: defaults patch; tree.json table review; research/ty2026/changes.md l. 489; regenerate COVERAGE.md and
README. Round 2: consumers rulings (two new, two stale, above).

## 8. Verification (run on the lane tree; base failures separated)

| Command | Result |
|---|---|
| build, render, render --ny | pass |
| test-fixtures | 1428/2046; every failure but one is the base (598 `s2.amt_owed` not declared, 19 missing `sd.qof` or `s2.mortgage_subsidy`); `stage4.sb.foreign_no_filing` (sb.partIII false, expected true) not attributed: the lane touches no sb line or input, likely the copied nx-b1 defaults. Every lane case passes |
| test-fixtures --ny | 142/357; all 215 failures are the base (214 `s2.amt_owed`, 1 `sd.qof`) |
| citations.py --strict | pass |
| check_questions, check_screens, check_false_no | pass (after render --ny) |
| check_consumers | fails: 2 new and 2 stale lane findings, not ruled (above); rest other lanes |
| siblings --check, check_bug_inventory | fail on other lanes' pending entries only |
| tree.py --check | fails on six other lanes' unplaced gates only |
| year_changes --check | pass |
| tick-groups | pass |
| interview-coverage sales.yaml | 0 problems |
| interview-coverage other.yaml | every lane row passes; 3 problems left, all on other lanes' AMT rows (other.iso_kept, other.iso_vested_2025, other.amt_owed) |
| draft-walk 01, 17, 18 | 0 problems; 17 completes, 18 refused at `sales[nft].special` |
| interview-rules | 17 problems, none on a lane line (s2.amt_owed walks, NY dependent reach) |
| mutate, check_all | not run |

## 9. Review debt (round 2)

Transcription, render, class M: sales, sd, s1, f1040, f8960. Question reviews: f1040.digital_assets,
s1.digital_income, s1.digital_amount, $sales, sales.box, sales.special, sales.proceeds, sales.reported_basis,
sales.correct_basis, sales.code. Screen and false-no: f8960.digital_nii, f1040.digital_conflict, sales.special.
No dry-run estimate made (rerun_all.py not run in the lane).

## 10. Walks

No walk was recorded before the change (the lane edited first): not compared. After: 01_single_w2 completes, 126
questions on 58 screens, 1,766 prompt words; for this filer the topic is one step (the new question, 21 prompt words),
and the money_b screen loses one box. 17_crypto_investor completes (144 questions, 76 screens). 18_refused_nft_art is
refused at `sales[nft].special`.

## 11. Left open

1. Consumers rulings for s1.digital_income (round 2). 2. s1.line9 remedy does not name line 8v. 3. Archive f1099da,
i1099da, Notice 2023-27, Rev. Proc. 2024-28, Rev. Ruls. 2019-24 and 2023-14, and a count of Yes answers. 4. Engines
(L3): G to L in generate_cases and the adapters. 5. Coverage gain unmeasured (low single-digit percent of returns
[inferred]).
