# Owner decisions open after the night of 2026-11-15/16

Lane POST (claude-fable-5-2, judgment, text only), 2026-11-16 about 12:20. One block, de-duplicated from the
coordinator log, the lane reports and `records-staging/MORNING-REPORT.md`. Ordered by how much each blocks.

How to read an item: **Decision** is the question. **Evidence** names the file and page. **Options** are the
choices. **Default** is what the coordinator does if you do not answer. Where the records hold no default, the
item says so and gives a proposed one, marked as proposed.

`P` = `.claude/nightplan-2026-11-16/nightplan`. "Round F" is the combined fix round F1 + F2 + F3; "round K" is the
K-1 integration stack. Source quotes for A2, A3, B3, C1 and D2 are in `P/round6/owner-sources.md`.

Already decided and not repeated here: canceled debt as tick screens (0810 = B), the charity carryover asked of
every giver (0817a), the 25-word limit applies to a tick member's full prompt, the `rprop.screen` restructure
lands, rental counts as covered in the estimate, the release waits for the mutation survivors, new subagents on
Fable for the session of 11-16.

---

## A. Block round F (needed before or during its first steps)

**A1. Review budget for round F.**
- Decision: approve a spending ceiling for the one paid review round of F1 + F2 + F3.
- Evidence: any review run estimated above $3.00 needs `--approve-cost` (CLAUDE.md, inference cost). Earlier
  estimates: F1's lines about $64 core, $103 with options, approval sought $135 (`P/lane-briefs.md`, OD-14);
  re-review of all 161 screens about $21 (log, lane A10); F2 and F3 were never priced; the sampled release reviews
  cost $85.82 for the expansion (log 23:55). The night's total was $388.90 over 1,574 calls
  (`records-staging/MORNING-REPORT.md` section 5).
- Options: (a) approve a ceiling now, for example $200, with a dry-run report before anything is spent;
  (b) approve only after seeing the dry-run estimate; (c) split the round to spend less at once.
- Default: (b). The lanes run no paid review; the dry run is produced and the round waits for your figure.

**A2. Owner decision 8: Form 8853 lines 22 and 24, payments made straight to the care provider.**
- Decision: do Medicaid or VA payments made straight to a nursing home count as line 24 reimbursements?
- Evidence: the release asks line 22 for the care cost "whoever paid" and line 24 for what was "paid back to you",
  so such a payment is on line 22 and not on line 24, which overstates the limit whenever the cost exceeds $420 a
  day. The two lines disagree under either reading. i8853 (2025) p. 9, Line 24 ("reimbursements you received or
  expect to receive through insurance or otherwise"); Pub. 525 (2025) p. 19; Medicaid and the VA are named nowhere
  in i8853 or the form. F1 already carries the answer "they count": it rewrites the line 24 prompt and adds the
  register entry `amb.2025.f8853c_line24_public` (`P/patches/v3/fix-round.patch:148` and `:16632`). Draft entry:
  `records-staging/bug_pending/rec-02.md`. Persona 23 (per diem) rests on this.
- Options: (A) count them on both lines (F1 as drafted); (B) count them on neither: line 22 becomes the cost you
  bore, line 24 stays "paid back to you", and F1's hunks for 0873 and the register entry are rewritten.
- Default: (A), as F1 carries it.

**A3. The thrift-store donor and the item "art or other belongings the charity will not use".**
- Decision: narrow this refusing item to property worth more than the donor paid, or land it as drafted?
- Evidence: the item is not on `main`; F1 adds it (BUG-0818; `P/patches/v3/fix-round.patch:15471`), and F2's
  `tf-a-f1` keeps it as the tick `gift.unrelated_use`. A donor of used clothing can truthfully answer Yes ("Goodwill
  sells it") and is refused, although the rule reduces only appreciation: Pub. 526 (2025) p. 19, Capital Gain
  Property, Exceptions, item 5; p. 18 ("clothing, furniture" decrease in value); i8283 (Rev. 12-2025) pp. 3-4.
  Reading: strong that the text does not require the refusal. Draft entry: `rec-03.md`. Note:
  `P/round5/trimfollow.md:31` calls the over-refusal "pre-existing"; that is true of the fix chain, not of the
  release (`owner-sources.md` Q2).
- Options: (a) land as drafted and file the low entry; (b) narrow the wording to "worth more than you paid and
  held over a year" before F1 lands; (c) take the item out of F1 until it is designed.
- Default: (a). The research lane recommended (b). Under (a) round F adds a refusal that the release does not have,
  for a common kind of donor among itemizers with noncash gifts.

**A4. A derived "any" line stops reading at its first Yes (F2: digital assets, listed property).**
- Decision: accept that a member after the first Yes is never asked in a walk, or change the derived lines?
- Evidence: `P/round6/v1.md` section 3. With `f1040.digital_got` Yes, `f1040.digital_disposed` is never asked
  outside the tick screen, and interview-rules reports the return "complete while f1040.digital_disposed is
  reachable and unanswered"; `asset.listed_computer` is reachable before `listed_rec` and then hidden. Three
  interview-rules problems. The printed answer is Yes either way (inferred, not run). `gift.special` (tf-a-f1) has
  the same shape and was not tested. Separately, the digital split costs every filer one more question and 22 more
  help words; the design had predicted "about equal".
- Options: (a) hold the three problems in the interview-rules baseline; (b) rewrite the derived lines so every
  member is read (the nested pattern lane V2 used for the K-1 rosters); (c) leave `tf-b-f1` and `tf-a-f4` out of
  round F.
- Default: none recorded. Proposed: (c) now and (b) for a later round. The night's ruling on the two dependent
  completion leaks was "fix and pin, not baselined" (log 02:15), which speaks against (a).

**A5. The gift tick screens show their refusal late (F2, `tf-a-f1`).**
- Decision: accept that a Yes on the first of the two gift screens shows its refusal only after the second?
- Evidence: `P/round5/trimfollow.md:252` (3.1(a)): one refusal line stands behind two screens.
- Options: (a) accept; (b) split the refusal per screen; (c) leave `tf-a-f1` out.
- Default: (a). If A4 = (b) or (c), check `tf-a-f1` for the same "any" problem before it lands.

**A6. Model for the next session's agents.**
- Decision: do new subagents run on Fable again?
- Evidence: CLAUDE.md allows Fable for either class only when you say so for the session; your instruction of 10:02
  covered the session of 11-16.
- Options: (a) Fable for all new subagents; (b) the standing defaults (Sonnet mechanical, Opus judgment).
- Default: (b).

---

## B. Block round K (the K-1 integration)

**B1. Where a K-1 filer meets the K-1 questions (tick-group order).**
- Decision: the tick `scope.k1` sits in the group `own_income` at order 130, but the K-1 rosters and their roughly
  170 entries sit at order 264. tick-groups fails on it (4 problems, one defect). Which way is it repaired?
- Evidence: `P/round6/v2.md` section 3, defect 3 (D12). The rule: a question that a member's Yes opens takes the
  group's order. The fault was hidden until V2 fixed a roster leak.
- Options: (a) move the rosters and entries to order 130, after rental and royalty (K-1 filers meet them earlier;
  no one else is affected); (b) take `scope.k1` out of the tick group as its own question (one more step for every
  filer); (c) hold the problem in a baseline, if tick-groups has one (not checked).
- Default: none recorded; the stack does not land without this. Proposed: (a).

**B2. Partnerships and S corporations in the coverage figure, and the README wording.**
- Decision: confirm that `partnership_scorp` stays counted as refused until box 14 code A (self-employment) is
  wired, and approve the README item.
- Evidence: `P/round5/k1block.md:326` (the drafting lane chose to count it covered); the coordinator overrode it
  (log 03:00); V2 applied the override in `k1block-9-coverage.v2.patch` and wrote the item: "Self-employment
  earnings from a partnership (Schedule K-1 box 14, code A); the share counts every partnership and S corporation
  return until these are handled" (`v2.md` section 4). The headline stays 85.9% (reasoned, not rerun).
- Options: (a) keep refused, with V2's wording or yours; (b) count as covered now (overstates while box 14 A
  refuses).
- Default: (a) with V2's wording.

**B3. S corporation K-1 box 17 codes A and B.**
- Decision: these are neither refused nor carried to Form 4952. What happens when K-1s open?
- Evidence: i1120ssk (2025) p. 15 ("Code A. Investment income. Report this amount on Form 4952, line 4a. Code B
  ... line 5"); Form 4952 instructions pp. 3-4. xint `forms/2025/k1s.yaml:921-932`. A missing code B can overstate
  the investment-interest deduction. Draft entry `rec-04.md`.
- Options: (a) a new per-K-1 tick asked only when box 17 has an amount; (b) refuse Form 4952 whenever an S
  corporation K-1 shows box 17 (over-refuses: code V is common); (c) accept the gap.
- Default: the records disagree. The coordinator's interim was "refuse" (log 03:00, repeated in MORNING-REPORT
  item 4), but V2 added nothing because neither (a) nor a narrow refusal is trivial (`v2.md` section 4). The
  patches as they stand are (c). Proposed: add (b) to the stack as the interim, since (c) can produce a wrong
  amount on a computed return.

**B4. Coverage-row ends changed by the lift.**
- Decision: confirm the end changes of `scope.k1`, `credits.partnership_credit` and `business.qbi_other_income`.
- Evidence: `P/round5/k1block.md:384` (O-3); they are deliberate exceptions to N9. V2 rewrote the `scope.k1` row
  to one partnership with box 5 interest of $300 (`v2.md` D9).
- Options: confirm, or name the rows to keep.
- Default: confirmed (pre-authorized under your earlier pattern for restated ends).

**B5. A W-2 tip earner with any K-1 is refused the tips deduction.**
- Decision: accept the over-refusal of `s1a.line5_calc` on `scope.k1`, or build a narrower gate on nonpassive
  K-1 income?
- Evidence: `P/round5/k1block.md:330`; found when `scope.schedule1` stopped refusing K-1s.
- Options: (a) accept (rare); (b) narrower gate.
- Default: (a).

---

## C. Do not block; a default is in force

**C1. Rental-only costs divided by days.**
- Decision: on a rental with personal-use days that was not used as a home, do advertising and commissions go to
  Schedule E whole?
- Evidence: the release divides every expense line by rental days over total days (xint
  `forms/2025/rental.yaml:517-529`, `663-675`). Pub. 527 (2025) Worksheet 5-1 p. 29 line 2d and its instruction
  p. 31 deduct "rental agency fees, advertising" in full; pp. 23-24; against: pp. 25 and 28 say "divide your
  expenses" with no carve-out. Reading: moderate that they stay whole. Also the cite says p. 26; the rule is on
  p. 25. Draft `rec-01.md`. Persona 31 avoids such costs.
- Options: (a) whole for rental-only lines, decided line by line; (b) keep dividing and add the Schedule E p. 5
  sentence to the cite.
- Default: shipped as is; the entry is filed as medium, pending your reading.

**C2. A mutation kill that asserts an out-of-scope refusal (Form 1116 line 35).**
- Decision: is a fixture acceptable whose expected result is the model's own refusal, where the mutant gives the
  legally right $0?
- Evidence: `P/round7/mint.md`, case `f1116.mint_line33_refused_line20_zero_line18`, kills
  `operand.f1116.f1116.line35.line33`; `round7/m1116.md` (the alternative is an argument resting on "Form 1040 line
  16 is never negative" plus a rounding bound).
- Options: (a) keep the case; (b) replace it with the argument; (c) list the mutant as open.
- Default: (a), ruled by the coordinator (log 10:45). It is in the release.

**C3. Stage fixtures that answer a question the interview never asks (EIC line 27c on MFS).**
- Decision: may `mexist.eic.check_27c.mfs_no_us_home` and `.mfs_qc_of_another` answer `eic.us_home` on a married
  filing separately return, where the interview stops before asking it?
- Evidence: `P/round7/mexist.md:69-73`. The expected result (box not checked) holds whatever the answer
  (i1040gi p. 41).
- Options: (a) keep; (b) rebuild the cases on answers an interview can produce, or argue the mutants
  answered-only.
- Default: (a). They are in the release.

**C4. Two flagged equivalence arguments.**
- Decision: keep the answered-only argument for `operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0`, and
  keep `person.f8919_line10` under the open defect instead of its drafted argument?
- Evidence: `P/round7/mint.md` (arguments table; coordinator item 2a). The ira argument fails only on a not-joint
  roster that lists a spouse, which the model refuses at line 1a. The f8919 argument is false on a hand-listed
  roster, the same class as the k1s Form 7203 mutants.
- Options: keep both as ruled, or hold the ira mutant to the same line as the k1s ones (list it as open).
- Default: as ruled by the coordinator (log 10:45).

**C5. BUG-0570b and BUG-0719 held out of F3.**
- Decision: land, hold or close each.
- Evidence: `P/round5/deferred.md:27-29`, `252-291`. 0570b refuses when the refund split exceeds line 34: up to 35
  fixture cases may newly refuse, and there is no precedent for a refusal on an input line. 0719 waited for IRC 402
  and 457; both are now archived by S0, but Pub. 525 (2025) p. 9 reads against a separate limit.
- Options: 0570b: (a) run it in scratch after F3 and land if the count is acceptable, (b) drop. 0719: (a) land,
  citing the statute, (b) close as "not a bug: over-refusal accepted".
- Default: both stay held.

**C6. BUG-0765: the widowed-this-year remedy text and two restated expectations.**
- Decision: approve restating the two `household.json` expectations to the new remedy text.
- Evidence: `P/round5/deferred.md:116-126` ("the expected-value change needs the owner's approval"); i1040gi
  p. 13; Pub. 501 p. 6. No value changes.
- Options: approve, or leave 0765 out of F3.
- Default: lands with F3 (the coordinator accepted the lane's design choices, log 02:50).

**C7. The dependent read order.**
- Decision: keep reading `household_all_year` before `spouse_relative`?
- Evidence: log 04:20; it changes the case `stage8.mut.mfj_spouse_relative_all_year_unanswered`. It came with the
  completion-leak fix in `dependent.yaml` and is in the release.
- Options: keep, or restore the order and repair the leak another way.
- Default: keep.

**C8. The foreign-tax question moved earlier (`ftc.taxes` to order 272).**
- Decision: accept that a filer who is refused later answers one more amount first?
- Evidence: log 04:40; `f1/msg4.txt` (tick group `interest_dividends`, pending entry `fix-round-1-01`). The
  alternative weakens the tick-group check. Related: the `home.gifts_and_carryover` refusal now waits on
  `s3.foreign_any`.
- Options: accept, or weaken the check for this group.
- Default: accept. It lands with F1.

**C9. Redesign of the medical-cost question (`sa.line1`, follow-up A-F2).**
- Decision: sign off a new formula that computes the Marketplace term so the 325-word question becomes about 45.
- Evidence: `P/round5/trimfollow.md:340-371`: the largest saving in the set; about 1,000 fixture references; a
  new formula needs your sign-off and the full review set for sa.
- Options: (a) open its own lane; (b) keep the long question.
- Default: not started; nothing in round F depends on it.

**C10. Release-list policy and the missing-engine gate.**
- Decision: (i) a release entry expires after 24 hours (tooling-4); (ii) a run with a missing engine fails the
  release (tooling-3), which blocks 2026 releases until the engines support 2026.
- Evidence: `P/tooling.md`; log 00:55 and 01:15; `run_engines.py:628` records a release even when engines were
  skipped.
- Options: approve, hold or reject each.
- Default: (i) lands after the release; (ii) deferred.

**C11. Standing defaults that ride in F1 (answer only to overrule).** Each is one line of
`P/lane-briefs.md`, table at lines 815-851, where the evidence is cited:
- 0790 boats: every boat is refused (OD-11). The red team chose this; the first draft named boats in the listed
  property question instead.
- 0833 Form 4952 with no 2024 form: an ambiguity entry with the current wording, not a refusing child (OD-5).
- 0894/0897 joint estimated payments: counted with the split rule; "or former spouse" is dropped because Pub. 505
  (2025) is not archived (OD-7).
- 0900 "transient basis" read as rented for short stays (OD-8). 0905: one more step for ADR holders (OD-4).
- 0775 home converted to a rental: wording only (OD-10). `f8582.part2_shown` kept (OD-12).
- 0803 treaty charities left out (OD-15). 0861 wording, not Chart B (OD-18). 0797 keeps "you" (OD-19).
- 0851 NY 529 plans not named; 53-word help kept (OD-20, OD-21). 0815 tick without "unemployment" (OD-28).
- N10 overruns kept as guards, listed in OD-22 and in the trim lanes' seven kept overruns; the entry frame does
  not count toward a prompt's words (trimB follow-up F5; note OD-24 had said it counts).
- Class M subjects changed only by restated inputs are left due and listed, not rerun (OD-31).
- Community property is asked by domicile, with a spouse-domicile question kept off the ended-marriage path
  (OD-44; log, lane A1).

**C12. Left from earlier plans, no round depends on them.**
- NY item C on a joint return where only the spouse can be claimed: add the case to `amb.ny.2025.item_c` (log
  23:12; OD-34). The earlier scope ruling rested on a federal refusal that no longer exists.
- `amb.2025.ira_age50`: its reason against the i1040gi child-age rule (log, lane A4).
- The Form 1116 election: always take "no Form 1116" when available, and the Form 2555 filer sent to Form 1116
  (OD-32, OD-33; pending low `xint-ftc2555-01`).
- `amb.2025.k1p_prior_with_activity`, K-1 decisions D-K1 to D-K16, the TY2026 plan's D1 to D14 (OD-36 to OD-38).
- Mutation sampling (OD-41, OD-42); `person.mw_earned` computed both ways (OD-43); `sa.dependent` help (OD-45).
- The 42 open mediums: a bug plan after the release (your instruction of 22:45). Round F is that plan's first
  part; confirm or reorder.

---

## D. Block Form 8615 (after round K)

**D1. Whether to build Form 8615 now.**
- Decision: the area is 0.143% of returns, below the stop rule; build it anyway?
- Evidence: log, lane A7 (scout); `P/round5/f8615.md`. The patches exist and are unbuilt; about 1,330 fixture lines
  retire.
- Options: build after round K; defer.
- Default: queued after the K-1 integration and k1e.

**D2. Clear the Form 8615 sources for encoding.**
- Decision: change `f8615` and `i8615` in `sources/2025/manifest.json` from "archived for form designations and
  purposes, not cleared for encoding" to cleared.
- Evidence: `owner-sources.md`, last section: both are printed 2025 revisions (form footer "Form 8615 (2025)
  Created 9/9/25"; instructions page 1 footer "Oct 22, 2025"), with suggested locator text. Without clearance the
  area cannot count as covered (`f8615.md:47-50`).
- Options: clear both; or name what else must be inspected.
- Default: not cleared; the area stays uncounted.

**D3. Which children the AMT exemption cap reaches.**
- Decision: every child meeting the section 1(g) age, parent and joint-return tests (reading 1, as patched), or
  only children who file Form 8615 (unearned income over $2,700)?
- Evidence: Rev. Proc. 2024-40 section 3.12, p. 11 ("a child to whom the § 1(g) 'kiddie tax' applies"); i8615
  (2025) p. 1, Who Must File; i6251 is silent. Reading: moderate for reading 1. Two cautions: the questions behind
  `f8615.kid` are reached only above $2,700, so the patch may behave as reading 2 (not traced); and the cap makes
  the AMT screen refuse, not compute, so the served share shrinks (`f8615.md` finding 1).
- Options: reading 1 (and widen the reach of the questions); reading 2 (and reword the register entry).
- Default: reading 1 as patched, checked when the form is validated.

**D4. Smaller Form 8615 items.**
- A `kiddie_tax` category in the coverage estimate (left to you, `f8615.md:75`).
- The reason text of `amb.2025.filer_under_16` goes stale; proposed: "Form 8615 is computed from age 16; a return
  for a child under 16 is one the slice does not model well" (`f8615.md:76`).
- Default: no category; the proposed wording.

---

## Provenance

Inspected: the coordinator log (whole); `round6/v1.md`, `v2.md`, `owner-sources.md`; `round7/mint.md`,
`mexist.md` lines 60-117; `records-staging/MORNING-REPORT.md`, `bug_pending/rec-01.md`, `rec-02.md` and the headers
of `rec-04.md`; `round5/k1block.md:320-386`; the owner lines of `trimfollow.md`, `deferred.md` and `f8615.md`
(by search); `lane-briefs.md:815-861`; `fix-round.patch` at the three lines cited; xint
`tools/transcription/screen_review.py` (by search).

Inferred (unverified): that every OD default in C11 is what `fix-round.patch` actually contains (taken from the
table, not from the patch); A6's reading of the 10:02 instruction as session-scoped; the proposed defaults in A4,
B1 and B3, which are mine and not the coordinator's.

Gap: `decisions.md`, `med-*.md` and `round4/*.md` were not read, so an owner question raised only there and
never carried into the log or `lane-briefs.md` would be missing.
