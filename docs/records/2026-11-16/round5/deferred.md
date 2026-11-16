# Lane D3-deferred: patches for the deferred lows that need a model change or a new refusing question

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16. Nothing was built, walked, run or reviewed; no paid
calls. Labels: **[C path:line]** checked against that file; **[C]** checked, file named in the sentence; **[U]** relayed
from the bug entry, not re-read; **[I]** inferred.

## Summary

- **14 patches** in `patches/v4/def-*.patch` (11,198 lines, most of them fixture restatements). Built from copies by
  `scratch/round5-d3/units.py` (helpers in `lib.py`), base = `scratch/b-chain/work/<path>`, else xint `<path>`.
- **Checked mechanically** (`scratch/round5-d3/check.py`) [C]: every changed YAML and JSON file parses; no two bank
  questions share an order and seq; every touched tick group has contiguous seqs, at most 6 members, and every tick has
  12 words or fewer; `git apply --check` passes for each patch on a fresh copy of the base when applied in the order
  below (the chain), and the chained result equals the generated final state.
- **Apply order (the chain), by rank:** 0871, 0795, 0765, 0891, 0779, 0889, 0786, 0778, 0828, 0895, 0570a, 0570b,
  0791, 0719. Ten apply alone on the base. **0779, 0889, 0786 and 0778 apply only after 0891** (and in that order),
  because each renumbers order-130 seqs in `questions.yaml` and inserts next to the same fixture and coverage lines.
- **No trimmed field is touched.** The trims touch `rental.prior_any` source, `rprop.*` sources, `rental.not_at_risk`
  source and `royalty.expenses_any` source (P/round4/trimA.json, trimB.json) [C]; these patches change none of those
  fields. The new `royalty.not_at_risk` copies the post-trim wording of `rental.not_at_risk`.
- **Decision on the free `rental_rare` box:** it goes to **0779** (held mainly for sale, or open to the public in set
  hours). 0778 becomes a child of `rental.prior_any`; 0786 a box in `rental_return` (return level); 0891 a question
  of its own per building (the six-box `rprop_facts` screen stays as it is). Reasons in each unit.
- **Not drafted** (kept deferred, reasons in section 3): 0764, 0867, 0866 items 4 and 5, 0713, 0785 grouped half, 0565,
  0845, 0887, 0575, 0829, 0831, 0502, 0852, 0762, 0763, 0750, 0424, 0768 and 0802, 0774, 0508, 0568, 0555, 0386, 0925
  residual, 0915. 0812 and 0869 are already handled elsewhere.
- **Biggest risks:** 0570b can newly refuse up to 35 fixture cases that state a refund amount (line 35a 173,300 cents
  in 33 mutation cases) if their computed line 34 is smaller; it must not land without a fixture run. 0719 must wait for
  a source (what to fetch is stated). 0828's refusal fires only above the joint NIIT threshold, by design.

## 1. Ranking (severity x reach)

| Rank | Bug | Severity of the error | Reach | Patch |
|---|---|---|---|---|
| 1 | 0871 | Overtax: whole IRA distribution taxed | Common (after-tax 401(k) rollovers, inherited IRAs) | def-0871 (wording; no model shape change) |
| 2 | 0795 | Wrong AGI, earned income (8812, EIC, 2441) | Students, researchers, teachers on treaties | def-0795 |
| 3 | 0765 | Wrong advice on a reachable refusal | Every filer widowed in 2025 | def-0765 |
| 4 | 0891 | Wrong recovery period and basis | Landlords with a 1031 exchange (common among investors) [I] | def-0891 |
| 5 | 0779 | Passive loss held back or let through wrongly | Land held for appreciation with a lease; dealers; parking | def-0779 |
| 6 | 0889 | SE tax missed; capital-gain royalties; at-risk; 50% meals | Uncommon royalties | def-0889 |
| 7 | 0786 | Cash amounts given for accrual | Rare for individual landlords | def-0786 |
| 8 | 0778 | Carryover lost or unlimited | Rare (home use in 2024, none in 2025) | def-0778 |
| 9 | 0828 | NIIT on the wrong base | Rare (6013(g) couples above $250,000) | def-0828 |
| 10 | 0895 | Taxable refund understated | Rare (dual-status 2024) | def-0895 |
| 11 | 0570 | No value wrong today (nothing reads 35a, 36); builder wording | All refunds (presentation) | def-0570a, def-0570b |
| 12 | 0791 | Missing 50% allowance or class | Rare item-defined property | def-0791 |
| 13 | 0719 | Over-refusal only | 457(b) plus 401(k) savers | def-0719 (waits for source) |

## 2. Units

Each unit: decision, hunks, red-team, fixtures and coverage with predicted ends, reviews due, closure text. Closures
use the conventions of tools/README.md (`tools/new_bug.py --pending <PREFIX>`), recorded only when the patch lands.
Common to every new refusing input: a `fixtures/2025/defaults.json` entry (false, "Closed: ...") in sorted place,
class M and mutation restatements (`false`, inserted after a sibling key), and question review of the input.

### 2.1 BUG-0871 — `def-0871.patch` (95 lines)

- **Decision.** Keep one input (`retirement.ira_basis`) and widen its subject from "money you put in without deducting"
  to "money you already paid tax on", naming the three missing sources. A Yes refuses as before (through
  `retirement.special`), so a wider reading only over-refuses. No new input, no fixture change.
- **Hunks.** `forms/2025/retirement.yaml` (xint): label, source and cite of `retirement.ira_basis` (cite moves from
  i1040gi to i8606 p. 2 Who Must File and p. 9 Line 2, quotes checked [C sources/2025/i8606.cols.txt:31-32]; p. 9 [C
  findpage]); gate label. Bank tick: "A traditional IRA of yours holds money you already paid tax on" (12 words); help
  (41 words): examples, "A Form 8606 on any earlier return means Yes. A Yes ends the interview here."
- **Red-team.** Who answers No wrongly: (a) a retiree who forgot an after-tax rollover from a 401(k) twenty years ago:
  the help's example and the Form 8606 cue guard it; (b) an heir who does not know the decedent's basis: the help names
  "inherited with basis", but the heir may not know; residual [I]. Wrong Yes: a filer who thinks "I paid tax on my
  wages before contributing" for a deductible contribution: over-refusal only. "Money you already paid tax on" was
  preferred to the entry's "never deducted or taxed" because after-tax money **was** taxed; that phrase reads the
  wrong way round.
- **Coverage rows** (`interview/2025/coverage/retirement.yaml`): `retirement.ira_basis_rollover` and
  `retirement.ira_basis_inherited`, copies of `retirement.ira_basis` with new situations; predicted end
  `refused: person[taxpayer].retirement[r].special` (same answers, same input) [I].
- **Reviews due.** Transcription and render of retirement (lines `retirement.ira_basis`, `retirement.ira_basis_if_trad`,
  line-scoped); question review `retirement.ira_basis`; screen and false-no of `gate:person.ira_files_8606` is where
  it was caught, so rerun that false-no sample.
- **Closure.**
  ```
  python3 tools/new_bug.py "Closure: BUG-0871 is fixed: the IRA basis question names after-tax rollovers, divorce transfers and inherited basis" --pending <PREFIX> \
    --field "Caught by=lane D3-deferred (claude-opus-5-5, judgment), 2026-11-16." --field "Closes=BUG-0871" --field "Closure=fixed" \
    --field "Evidence=retirement.ira_basis now asks whether any traditional IRA holds money already taxed, 'such as contributions you did not deduct, after-tax money rolled over from a work plan, or basis that came with an IRA from a spouse in a divorce or from someone who died' (i8606 p. 2 Who Must File; p. 9 Line 2). A Yes refuses as before; no value changes." \
    --field "Fix lines=retirement.ira_basis" --field "Tags=closure; retirement; question-wording"
  ```

### 2.2 BUG-0795 — `def-0795.patch` (7,517 lines; 7,450 are fixture restatements)

- **Decision.** A new return-level box `scope.treaty` in the `about_you` group (4 members before, 5 after), beside
  `sa.excluded_income` ("Leaving out income earned abroad ..."), its natural neighbour. It joins `scope.other_income`'s
  `any` list, so it refuses with the existing remedy. Asking it of everyone costs one glance on a screen already shown;
  gating on `scope.noncitizen` was rejected because a citizen can hold treaty-exempt income (saving-clause exceptions)
  and the box is free on the screen.
- **Hunks.** `forms/2025/scope.yaml`: new input (cite i1040s8812 p. 3, Line 18a [C findpage]); `scope.other_income`
  any-list and cite. Bank: order 113 seq 6, tick "Income exempt under a tax treaty with another country" (9 words), help
  32 words. Defaults. Fixtures: `scope.treaty: false` after every `scope.chapter11` key: classm 346, classm.deepseek
  111, classm.gpt 6, mutation 246, NY classm 54, NY classm.deepseek 55, NY mutation 106 [C, counted by the builder].
- **Red-team.** Wrong No: a resident-alien student whose employer already left the treaty-exempt pay out of W-2 box 1
  (shown on Form 1042-S) might think "nothing to leave out": the help names Form 1042-S, and a Yes then over-refuses,
  which is acceptable since Form 8833 is generally required [I]. Wrong Yes: a filer thinking of the foreign tax
  credit, which is not an exemption: over-refusal only. The `about_you` seqs are 1, 3, 4, 5, 6: seq 2 was already
  missing on the base [C check.py]; if the tick-group check requires contiguity, renumber `about_you` to 1-5.
- **Coverage row** `scope.treaty` (coverage/scope.yaml): noncitizen Yes, nonresident No, treaty Yes; predicted
  `refused: scope.other_income`.
- **Reviews due.** Transcription and render of scope (`scope.treaty`, `scope.other_income`); question review
  `scope.treaty`; screen and false-no of the `about_you` screen (`gate:scope.other_income` sample). Class M of scope
  (new input).
- **Closure.**
  ```
  python3 tools/new_bug.py "Closure: BUG-0795 is fixed: income a tax treaty exempts is asked and refused" --pending <PREFIX> \
    --field "Caught by=lane D3-deferred (claude-opus-5-5, judgment), 2026-11-16." --field "Closes=BUG-0795" --field "Closure=fixed" \
    --field "Evidence=New input scope.treaty ('Is any 2025 income of yours (or, on a joint return, your spouse's) exempt from U.S. tax under a tax treaty ...'), a box of the about_you screen, joins scope.other_income, so a Yes refuses (i1040s8812 p. 3, Line 18a). Coverage row scope.treaty." \
    --field "Fix lines=scope.treaty, scope.other_income" --field "Tags=closure; scope; screen"
  ```

### 2.3 BUG-0765 — `def-0765.patch` (36 lines)

- **Hunks.** `f1040.yaml` remedy of `household.widowed_this_year`: "... file a joint return with your deceased spouse
  (married filing jointly) or a separate return (married filing separately)." `fixtures/2025/household.json`: the 2
  expected remedies restated [C, 2 occurrences].
- **Not in the patch, to regenerate or hand-edit:** `rendered/2025/f1040.md`, `reports/2025/interview_coverage.md`,
  `docs/COVERAGE.md` and `research/ty2026/forms-proposed/f1040.yaml` quote the old text [C grep]. Check whether
  `docs/COVERAGE.md` is generated before editing it.
- **Red-team.** The remedy now names a supported status; a widow who instead qualifies for nothing else is still told
  both options. No value changes.
- **Reviews due.** Render of f1040 (line 12e refusal, line-scoped); the expected-value change needs the owner's approval
  recorded with the scout's D2 (as the entry says) [U].
- **Closure.** `--field "Evidence=Remedy now 'file a joint return with your deceased spouse (married filing jointly) or a separate return (married filing separately)'; the two household.json expectations restated (i1040gi p. 13; p501 p. 6)." --field "Fix lines=f1040.line12e" --field "Closes=BUG-0765" --field "Closure=fixed"`.

### 2.4 BUG-0891 — `def-0891.patch` (315 lines)

- **Decision.** `rprop_facts` is full and its facts are about what happened to the building after renting began. The
  exchange is about how it was acquired, so it is a question of its own, asked right after `rprop.basis` (the cost
  question, which is where the carryover basis would otherwise be entered), and joins the derived `rprop.screen`, so
  it refuses with the same gate. Alternative considered: the free `rental_rare` box (per rental, one glance); rejected
  because the box went to 0779 and an exchange concerns the building, not the land or the rental. If the owner prefers,
  move it there: tick "Got in a like-kind (1031) exchange, or to replace lost property" (11 words).
- **Hunks.** `rprop.yaml`: new input `rprop.exchanged` (cite i4562 p. 9 [C findpage, quote C i4562.cols.txt]);
  `rprop.screen` any-list; remedy names the exchange. Bank: seq 62 (after `rprop.basis` 61), order-130 seqs from 62 up
  shifted by 1 (18 questions). Defaults. classm: 10 entries after `.coop` [C]. Coverage set `rents_house`
  `...rprop[bldg].exchanged: false`; persona 19 likewise.
- **Red-team.** Wrong No: an owner who calls it a "1031" and not a trade: the prompt says "(a like-kind or 1031
  exchange)". An owner whose house replaced one lost to fire with insurance money: "to replace property that was
  destroyed, stolen or taken by a government". An improvement (new roof): help says it is No. Cost: one yes or no per
  building, asked of every landlord (N3) [I]; it refuses rather than computes, so an old exchange whose carried-over
  recovery period has ended is over-refused.
- **Coverage row** `rental.rprop_exchanged`: predicted `refused: rental[house].rprop[bldg].screen` (the gate of the
  existing `rental.rprop_coop` row) [I].
- **Reviews due.** Transcription and render of rprop (`rprop.exchanged`, `rprop.screen`, refusal); class M of rprop;
  question review `rprop.exchanged`; false-no of `gate:rprop.screen`.
- **Closure.** `Closes=BUG-0891`; Evidence: "New input rprop.exchanged (a like-kind exchange or an involuntary
  conversion), asked after the cost, joins rprop.screen and refuses (i4562 p. 9, carryover basis over the remaining
  recovery period). Coverage row rental.rprop_exchanged."

### 2.5 BUG-0779 — `def-0779.patch` (597 lines; after def-0891)

- **Decision.** Takes the free `rental_rare` box. Exceptions 3 to 6 and dealer property are per-property facts; the
  ones a filer can recognize are "held mainly to sell" (investment land with a small lease; dealer property) and
  "open to the public in set hours" (exception 5). Not covered (residual, named in the closure as "in part"):
  extraordinary personal services (exception 3), property used in your business in 2 of the last 5 years with under 2%
  rent and employee lodging (exception 4), property given to your own partnership or S corporation (exception 6).
- **Hunks.** `rental.yaml`: input `rental.held_for_sale` (cites i8582 p. 3 and p. 4 [C findpage]; i1040se p. 5 dealer
  sentence [C i1040se.cols.txt grep]); refusal on `rental.line21_full` after `part_home`; form note. Bank: seq 24 in
  `rental_rare` (now 6 members, seqs 19-24 [C check.py]), later order-130 seqs +1 (57 questions). Tick "Held mainly to
  sell, or open to the public in set hours" (12 words); help 40 words. classm 15, coverage set and persona 19.
- **Red-team.** Wrong No: a farmer-landlord who thinks of the land as "rented" though held for its value: the help's
  first example is exactly that lease. Wrong Yes: an investor whose rent is 2% or more of the value (still a rental
  activity) is over-refused; a 2% child question would remove that, at one more input. A dealer whose rentals are held
  for investment, not for sale, is No by the wording ("held mainly to sell").
- **Coverage row** `rental.held_for_sale`: land, no buildings, box Yes; predicted `refused:
  rental[house].held_for_sale`.
- **Reviews due.** Rental transcription and render (`rental.held_for_sale`, `rental.line21_full` refusals, note); class
  M of rental; screen and false-no of `rental_rare` (`gate:rental.line21_full` sample); question review.
- **Closure.** `Closure=fixed in part`: Evidence: "rental.held_for_sale asks whether the property is held mainly to sell
  (investment or dealer) or offered in set business hours to many customers, and refuses at rental.line21_full (i8582
  pp. 3-4 Exceptions; i1040se p. 5). Exceptions 3, 4(b), 4(c) and 6 remain unscreened."

### 2.6 BUG-0889 — `def-0889.patch` (416 lines; after def-0779)

- **Hunks.** `royalty.yaml`: `royalty.business` label, source, cite and remedy widened (own business or services,
  other creators, NIL from sponsorships or services, operating interests in any mineral); three new boxes
  `royalty.capital`, `royalty.vehicle`, `royalty.depreciation` refusing on `royalty.line21`; `royalty.has_loss`,
  `royalty.no`, `royalty.not_at_risk` and its gate `royalty.not_at_risk_if_loss`, refused on `royalty.loss_abs`
  (not on line 21, which the gate reads); form note. Bank: heading "Is any of these true of this royalty?", boxes at
  seqs 78-80 (`royalty_rare` 76-80), later seqs +3, `royalty.not_at_risk` after `royalty.amt19`. 4 defaults; the one
  classm royalty case restated (3 keys) [C].
- **Red-team.** Business box: a retiree with royalties from a book written decades ago, no longer in business: the
  tick says "your own business, creative work or services" and could pull a Yes (over-refusal; the instructions' test
  is being in business) [I]. A mineral owner with a royalty (not working) interest stays No. Capital box: an
  inventor who licenses (not sells) a patent answers No, correctly. At-risk: a loan from the royalty payer named.
  Quotes for i1040se p. 3 at-risk and p. 6 patent and NIL text are the entry's [U] (pages located [C findpage]).
- **Coverage rows** `rental.royalty_capital`, `_vehicle`, `_depreciation` (each predicted refused at its own input) and
  `rental.royalty_not_at_risk` (line 4 $1,000, amt19 $1,500, loss $500, predicted `refused:
  royalty[lease].not_at_risk_if_loss`) [I].
- **Reviews due.** Royalty transcription and render (all new lines and the note); class M of royalty; screen and
  false-no of `royalty_rare` and of `gate:royalty.line21`; question reviews of the five inputs.
- **Closure.** `Closes=BUG-0889`, `Closure=fixed`; Evidence lists the widened business question, the three boxes and
  the at-risk child.

### 2.7 BUG-0786 — `def-0786.patch` (219 lines; after def-0889)

- **Decision.** The method is the filer's, not the property's, so a `rental_return` box (4 of 6 after).
- **Hunks.** `sche.yaml` (xint): `sche.accrual` input, refusal on `sche.line26` [cite p527 p. 4, When To Deduct, C
  findpage]. Bank: tick "You keep your rental books on the accrual method"; help 20 words. classm 12; both coverage sets
  and persona 19.
- **Red-team.** Wrong No: a landlord who counts December rent received in January as December's: the help defines
  both methods. Residual: a royalty-only filer's method is not asked (the tick names rentals) [I].
- **Coverage row** `rental.accrual`: predicted `refused: sche.accrual`.
- **Reviews due.** sche transcription and render (new line and refusal); question review; screen sample of
  `rental_return`.

### 2.8 BUG-0778 — `def-0778.patch` (352 lines; after def-0786)

- **Decision.** A child of `rental.prior_any` (a carryover is something "held back, not deducted"), plus one help
  sentence on the parent that sends the Worksheet 5-1 filer to Yes. Rejected: a `rental_rare` box (taken by 0779).
- **Hunks.** `rental.yaml`: `rental.prior_ws51` and `rental.prior_ws51_if_any`; refusal on `rental.prior_loss` after
  `prior_not_active_if_both` (p527 p. 28 [C findpage, quotes C p527.cols.txt]). Bank: `rental.prior_any` help; child
  after `rental.prior_not_active`, later seqs +1 (30). classm: 2 cases with `prior_any: true` [C].
- **Red-team.** Wrong No at the parent: the parent's source says "loss", a Worksheet 5-1 filer thinks "expenses"; the
  help is the only guard (help is optional, N10), so some will still answer No [I]. Wrong Yes at the child: a filer
  whose ordinary passive loss came from a year with some personal use but under the 14-day/10% limit: over-refusal.
- **Coverage row** `rental.prior_ws51`: predicted `refused: rental[house].prior_ws51_if_any` (after
  `prior_not_active: false`, since that entry is listed first on the line).
- **Reviews due.** Rental transcription and render (`prior_ws51`, gate, `prior_loss` refusals); class M; question
  reviews of `rental.prior_any` (help) and `rental.prior_ws51`; false-no of `gate:rental.prior_any`.

### 2.9 BUG-0828 — `def-0828.patch` (142 lines)

- **Decision.** The help-only option (refuse every 6013(g) couple at `scope.nonresident`) over-refuses widely. Instead:
  a question on Form 8960 asked only on a joint return with a noncitizen (`f8960.joint_noncitizen`, from
  `f1040.status` and `scope.noncitizen`), refused on `f8960.line1` beside `f8960.unsupported`. Line 1 is evaluated only
  when Form 8960 is used (MAGI over the threshold) [I from f8960.yaml lines 617-665], so couples under the threshold
  are not refused. Below the threshold the tool's $0 equals the result with the NIIT election; whether that election
  must still be shown is not checked [I]. `f8960.unsupported` itself is untouched (a 2026 cite operation targets it
  [C changes/2026/f8960.wording.yaml:83]).
- **Hunks.** `f8960.yaml` (xint): three lines and the refusal (i8960 p. 3 and p. 7 [C findpage, quotes C]). Bank
  order 278 seq 4. Default. No fixture restatement: no classm or mutation case has `scope.noncitizen: true` [C].
- **Coverage row** `other.niit_6013g` (coverage/other.yaml): a couple, noncitizen Yes, nonresident No, W-2 $300,000;
  predicted `refused: f8960.election_6013g_if_joint` [I: the couple's other questions come from the background].
- **Follow-up.** The 2026 year needs cite operations for the three new lines (i8960 2026 draft pages shift, as in
  `f8960.wording.yaml`) [I].
- **Reviews due.** f8960 transcription and render; class M of f8960; question review.

### 2.10 BUG-0895 — `def-0895.patch` (45 lines)

- **Hunks.** `refund.yaml` (xint): the 1040-NR limb becomes "a nonresident alien for all or part of 2024, whichever form
  you filed" (label and source); cite adds i1040gi p. 34, Exception 3—Dual-status alien [C findpage]. Bank: the bullet
  restated. No new input; no fixture moves.
- **Red-team.** Over-refuses a dual-status 2024 couple who chose resident treatment for all of 2024 (they had a
  standard deduction) [I]. The 2025 instructions are cited for a 2024 rule; the 2024 i1040gi is archived
  [C sources/2024/i1040gi.cols.txt exists] and should be cited instead after a page check.
- **Reviews due.** Refund transcription (`refund.exc_who`), question review, screen sample `refund.exc_who`.

### 2.11 BUG-0570 — `def-0570a.patch` (21 lines) and `def-0570b.patch` (48 lines)

- **0570a (safe).** `f1040.line3a` source loses the builder wording ("Supplied as a subtotal; qualification checks are
  outside this stage") and names the exceptions; cite quotes i1040gi pp. 25-26 [C i1040gi.cols.txt:539].
- **0570b (needs a run before landing).** `f1040.refund_split` and `f1040.split_over` (35a + 36 > 34), refusing on
  `f1040.line35a` with a correct-your-entry remedy, after the `f8960.bad_allocation` precedent. Two unknowns [I]:
  whether a refusal hosted on an input line fires (no precedent was found; an alternative host is a derived line every
  return reads), and the fixture fallout: 38 cases state a non-zero 35a or 36 (33 mutation cases at 173,300; 5
  `returns.json` cases where line 34 is 173,300, so they pass; `classm.carloan.1` line 36 165,300;
  `classm.f1040.6.deepseek` 217,600) [C, scanned]. Run `test-fixtures`; restate each newly refused case's 35a to its
  computed line 34. The lower bound (35a + 36 < 34) is left alone: the form does not say what happens to the rest.
- **Reviews due.** f1040 transcription and render (line 3a; lines 34-36), class M of f1040 for 0570b.

### 2.12 BUG-0791 — `def-0791.patch` (1,382 lines)

- **Decision.** Two boxes instead of a 30-word one: `asset.industry` stays the business box; a new item box
  `asset.industry_use` ("Recycling equipment, a gas gathering or power line, or a racetrack", 11 words) in `asset_kind`
  (5 of 6). The gate `asset.industry_item_if_industry` now reads `asset.industry_any` (either box), so
  `asset.industry_item` refuses as before. Rejected: asking `industry_item` of every asset (a long list per asset).
- **Hunks.** `asset.yaml`, bank (order 257, later seqs +1, 25 questions), default, classm 56, classm.deepseek 21,
  mutation 42 (after every `asset[...].industry` key), coverage: `industry_use: false` added beside the 14 rows stating
  `industry: false`, and row `equipment.screen_industry_use` (baler; predicted `refused: ...asset[item].screened`).
- **Red-team.** "Power line" includes a 12-kilovolt distribution line, which is not transmission property: the help
  gives the 69-kilovolt line; a Yes there then meets `industry_item`, which asks precisely, so only one step is lost.
- **Reviews due.** Asset transcription and render (new lines, gate); screen and false-no of `gate:asset.industry`
  (where it was caught) and of the new box.

### 2.13 BUG-0719 — `def-0719.patch` (13 lines; hold)

- **Hunk.** `scope.excess_deferral` help: "Count each person's jobs together; the limit is higher from age 50. A 457(b)
  plan (box 12 code G) has a limit of its own: count it apart. A Yes ends the interview here." (34 words.)
- **Hold until a source is archived.** The archived Pub. 525 (2025) p. 9 reads against a separate limit: "Amounts
  deferred under specific plan limits are part of the overall limit on deferrals", with section 457 plans in the list
  (item 7), while its 457 paragraph gives a limit of its own without saying it is separate [C sources/2025/p525.cols.txt
  :348-362]. Pub. 575 defers to Pub. 525 [C p575.cols.txt:144]. **Fetch:** 26 U.S.C. 402(g)(3) (the definition of
  elective deferrals, which does not list 457 plans) and 26 U.S.C. 457(b)(2) and (e)(18), stored as
  `sources/2025/usc-26-402.txt` and `usc-26-457.txt` like the archived `usc-26-172.txt`; optionally the IRS page
  "IRC 457(b) deferred compensation plans". Then cite the statute in the help's source note. If the owner prefers the
  conservative reading of Pub. 525, close 0719 as "not a bug: over-refusal accepted".
- **Reviews due.** Question review of `scope.excess_deferral`; false-no of `gate:scope.other_income` (w2_jobs).

## 3. Other deferred entries: not drafted

| Entry | Why still deferred | Next step |
|---|---|---|
| 0764 | s2.amt_l7 expression and two mutants: the mutation lane's (class M of s2, hand-computed Part III fixture) | Mutation lane; the entry's example is the fixture |
| 0867 | dependent.age, older-credits' file | With the next dependent change |
| 0866 items 4, 5 | Item 5 needs `changes/2026/person.sav.yaml` restated; item 4 has no place | 2026 lane |
| 0713 | Its own coverage disposition (Schedule 1 line 8j) | Owner |
| 0785 grouped half | No archived allocation rule | Source or owner decision |
| 0565, 0845, 0887 | Latent or wording at the asset and K-1 forms' next change | With those lanes |
| 0575, 0829 | Bullets in sales.yaml (new transcription round) | At sales.yaml's next change |
| 0831 | Four gate rewrites; a lane of its own with screen and false-no reviews | Own lane |
| 0502 | 2024 Form 1040-NR not archived | Archive, then help |
| 0852, 0762 | New NY question or gate; the owner chooses the design (0762 is an upgrade candidate) | Owner |
| 0763, 0750, 0424 | NY presentation; at the NY forms' next change | as stated |
| 0768, 0802, 0774 | New `sa.unsupported` input; 0774 rests on decision D3 | With the next sa.yaml change |
| 0508, 0568, 0555, 0386 | Gate change or multi-item wording at those forms' next change | as stated |
| 0925 residual, 0915 | Wording on files these patches do not touch | Next change of those forms |

0812 is lane A2's (inc-m12); 0869 is in v3 older-credits-lows.

## 4. What to run when the machine is free

1. Apply the chain in order on a worktree; build.
2. `test-fixtures` and `test-fixtures --ny`. Expected: no expected value moves, except household.json's remedy text
   (0765) and possibly the 0570b cases listed above.
3. `interview-coverage`, then `--write`: new rows `retirement.ira_basis_rollover`, `retirement.ira_basis_inherited`,
   `scope.treaty`, `rental.rprop_exchanged`, `rental.held_for_sale`, `rental.royalty_capital`, `_vehicle`,
   `_depreciation`, `_not_at_risk`, `rental.accrual`, `rental.prior_ws51`, `other.niit_6013g`,
   `equipment.screen_industry_use`.
4. `tick-groups` (about_you, rental_rare, royalty_rare, rental_return, asset_kind, ira_withdrawal, w2_jobs);
   `interview-rules`, `interview-order`; `draft-walk` for persona 19 and a royalty-only filer.
5. `tools/year_changes.py --check` (new 2025 lines need defaults in 2026 and, for f8960, re-cited locators).
6. `tools/check_all.sh` in the lane worktree.

## 5. Limits

- Nothing was executed beyond parsing and `git apply --check`. Every predicted end is inferred from the gate structure.
- Quotes marked [U] come from the bug entries; pages were located in the archived text by `scratch/round5-d3/findpage.py`
  (physical page with footer), not by reading the PDFs.
- Renumbering order-130 and order-257 seqs makes these patches touch many bank lines; any other v4 lane that edits the
  same bank region needs rebasing on this chain.
- Files: patches `patches/v4/def-*.patch`; builder `scratch/round5-d3/units.py`, `lib.py`; checks `check.py`; per-unit
  trees `scratch/round5-d3/u-<bug>/{a,b}`; bug-entry extracts `scratch/round5-d3/entries.txt`.
