# Handoff: Stage 15 (other credits), built and reviewed; owner questions open

Read `HANDOFF.md` first, then `TASKS.md` (T-048), then this file. The owner's scope decisions and the premise
maps are in `sources/2025/PREMISES.md`, section "Stage 15 premise maps".

## Scope

The child and dependent care credit with dependent care benefits (Form 2441 Parts I to III, W-2 box 10, Form
1040 line 1e), the saver's credit (Form 8880, both columns) and the residential energy credits (Form 5695 Parts
I and II), with their Credit Limit Worksheets, Schedule 3 lines 2, 4, 5a and 5b, Schedule 8812 Credit Limit
Worksheet A line 2 (Schedule 3 lines 1, 2, 4 and 5b) and Credit Limit Worksheet B. `scope.credits` now refuses
only the other credits (Schedule 3 lines 3 and 6a to 6z; Form 1040 lines 29 to 31); `scope.other_income` refuses
dependent care benefits only outside W-2 box 10 (or a grace-period amount from such a plan).

## Sources archived

`f8880`, `f2441`, `i2441`, `p503`, `f5695`, `i5695` and the energy credit Fact Sheets `fs-2025-01` (January 2025)
and `fs-2025-05` (August 21, 2025), each with its printed revision in the manifest (commit 6051ec0). For the later
roadmap stages, 32 more (commit fcd2c26): Pubs. 525, 529, 590-A, 590-B, 527, 925, 974, 970, 969; Forms 8606,
Schedule E, 8582, 6198, the Schedules K-1 of Forms 1065, 1120-S and 1041, 8962, 1095-A, 8863, 5329 and their
instructions, and the 1098-E/T instructions. Not archived: Form W-2G (its current revision is for 2026) and Form
1098-T (revision unreadable in the text).

## How the stage was built

- **Premise check:** three research agents mapped the forms; every quote in the maps was checked mechanically
  against the archived text and the claims the decisions rest on by hand; the corrections are recorded in
  PREMISES.md. The owner took decisions 1 to 8 in one batch.
- **The `rate_lookup` atom** (decision 8, commit 6051ec0): printed "over / but not over" rate tables
  (`tables/2025/savers_rate.yaml`, `dc_rate.yaml`), with a checker for contiguous, open-ended bands, the Lean
  definition `rateBand` and lemmas, and mutation of each band bound and rate.
- **Authoring:** one agent per form in its own worktree from 6051ec0, each adding its own Schedule 3 line, with
  placeholders for the others' lines; this session merged the three, repointed the placeholders, narrowed the
  screens, extended Credit Limit Worksheet A and backfilled the existing fixtures with the answers that leave
  them unchanged (the scripts are not kept; the fixture diffs are the record).
- **Fixtures (`fixtures/2025/stage15.json`, 41 cases):** the scenarios were written as facts; two agents per form,
  each without the encoding, worked every return by hand from the archived text and agreed on every shared
  value (8880: 330; 2441: 392; 5695: 234); the expected values are theirs. Against the encoding every carried
  amount agreed in both evaluators; the only differences were presentation (lines after a printed "stop", an
  ineligible person's lines 1 to 5 on Form 8880, the Form 2441 column (d) total), which the fixtures do not
  assert. Fact Sheet 2025-01's Example 1 ($1,200) and the Form 8880 line 4 example ($5,000 and $7,000) are among
  them.
- **Reviews:** transcription, render and class M for the four new documents (`f8880`, `f2441`, `dcprov`, `f5695`)
  and reruns for every form whose subject changed (dependent, eic, f1040, person, retirement, s3, s8812, scope,
  w2); every disagreement ruled with its source quote. Rulings were drafted by agents per form and checked
  before they were applied.

## Findings

- **BUG-0079 (open, for the owner):** the binary atoms return an unknown first operand before a refusal in the
  second, so a refusal can arrive later in the interview than the early-refusal rule intends; no wrong return.
- **BUG-0080 (fixed):** Form 2441 line 2 column (c) was checked for a disabled qualifying person under 13, and a
  helper's label misdescribed its route; display only.
- The PTC premise map found that `amb.2025.dc_rate_nonpositive_agi`'s reason holds only while Schedule 2 Part I
  is refused: TASKS.md T-049.

## Coverage

`tools/coverage/estimate.py`: 64.7% of returns (from 58.0%); the categories `cdcc`, `savers` and `energy` are
retired (`refused: false`). Spec 2.4's remaining list is updated: the 80% goal now comes with the premium tax
credit and the 95% target with married filing separately, one step later each than before, because the other
nonrefundable credits stay refused.

## Evidence

check-all green at the close (commit 8d7c0fd): logs current with no open ruling (transcription and render 51 forms, class M 44;
907 rulings); fixtures 843/843 (41 new); integration 658; properties 6 over 400 returns, 0 failing; Lean compare
1,443 cases, 0 differing; engine differential 1,700 cases, 0 unexplained; citations 2,044 segments, 0 findings.

**Mutation, after the follow-up fixtures:** 2,087 mutants, adjusted score 97.9% after a third round (98.0% before Stage 15). The first
close left 136 new survivors (91.5%); a second blind set (45 cases: every rate-table band edge, the operands) and
33 refusal and 9 regression cases (`stage15.refuse.*`, `stage15.regress.*`) killed 122 of them, and BUG-0082 (the
mutation tool compared every rate as equal) let four more be seen. 10 Stage 15 operand survivors remain (TASKS.md
T-051): three are provably equivalent (Form 2441 lines 24 and 25 read line 22, always zero; Form 5695 line 16 is
line 13 less the smaller of lines 13 and 14, so substituting line 14 gives the same result), the rest need cases
(listed there). Two parameter mutants are killed only through a helper or an input outside its question's range
(`savers.agi_limit`, which the line 9 table already enforces; `dc.exclusion_max`, which `f2441.plan_max` caps):
near-equivalent. check-all does not fail on unexplained survivors (31 before this stage, 45 now).

## Open for the owner

Each question is self-contained; the recommendation, where one was made, is first.

**Form 8880 (the saver's credit)**
1. *Stop order on line 12.* The credit is tested for any contributions first, then the AGI limit, then the
   worksheet; this keeps a return with no contributions at zero even when its AGI is refused, but asks every
   filer the contribution questions. Keep it, or test AGI first (sparing high-income filers the questions)?
2. *Three Stage 14 SIMPLE fixtures* now get a $200 credit from their existing SIMPLE deferral, correct on their
   facts and unasserted. Keep, or answer them so they stay at zero?
3. *`w2.g_bad`*, an input check you did not ask for: a governmental code G elective part above the code G
   amount is refused. Keep it?
4. *Excess or recharacterized Roth IRA contributions* have no screen of their own (the `s2.other` screen is
   relied on for Form 5329, not verified). Should the traditional IRA screen also ask about them?
5. *Other-year distributions* are two amounts per person (joint years, other years). Enough, or one per year?
6. *Display of an ineligible person's column:* the encoding shows their contributions on lines 1 to 5 and zero
   on line 6; both blind predictors zeroed the whole column. Same credit either way. Keep?
7. *Labels of `f8880.prior_own_a` and `prior_own_b`* do not say that on a non-joint return they hold all of the
   filer's prior distributions (a render review misread one). Clarify the labels (reviews rerun after)?

**Form 2441 (child and dependent care)**
8. *Line 1e when neither spouse has box 10* (a 2024 grace-period amount): refused with the both-spouses case when
   a credit remains (the agent extended your decision 6(c) from "both" to "both or neither"). Accept, or a
   per-person grace-period input?
9. *Undetermined split with no credit:* all of line 1e is shown on your line 4. Keep, or show it in neither column?
10. *Part I in the interview:* four Part I lines were added as targets of the full profile so the provider
    answers are asked and shown. Accept, or leave Part I unasked?
11. *Employer-provided care* (an on-site facility): its value counts as benefits but not as an expense paid, so
    line 30 understates when there are other paid expenses. Refuse employer-furnished care with benefits, or
    count its value as an expense?
12. *The student-or-disabled refusal* also refuses a single or head of household full-time student (i2441 says
    "you"; Pub. 503 limits the rule to joint returns). Keep it broad, or narrow it to joint returns?
13. *A person over 12 unable to care for themselves who was born or died in 2025:* Pub. 503 counts "more than
    half the time they were alive"; `dependent.months` asks "the entire time", so such a person could be missed
    (understating; nothing refused). Leave it?
14. *"Under 13"* is asked only for a child aged 13 at the end of the year and derived for 12 and under. Accept?
15. *Column (c) for a disabled child who turned 13 during 2025:* the box is checked, which is right when some care
    came after the 13th birthday (it counts through the disability rule) and wrong when all of it came before
    (the render review's finding). Accept as is, or add a question whether any care was on or after the
    birthday? (display only)

**Form 5695 (energy credits)**
16. *Section B for a newly built home:* the agent added `f5695.b_new_home` and refuses when Yes (i5695 p. 1, Part II
    "is only available for existing homes"; Fact Sheet 2025-01); your decision 7 did not list it. Keep the
    refusal, zero Section B instead, or drop the question?
17. *"Claiming Part I" for Credit Limit Worksheet B* is read as line 13 above zero (line 15 would be circular;
    `amb.2025.clwb_claiming_part1`, no amount differs). Accept?
18. *The Form 1040 line 19 stand-in* in the Part I worksheet (the smaller of Schedule 8812 line 12 and Worksheet
    A line 3) avoids a cycle the static checker reports though it never occurs at run time. Accept, or teach the
    checker that a `choose`'s branches exclude each other?
19. *Joint occupancy in Part I* is not refused (its special rule is for fuel cells only, which are refused). Confirm?
20. *State energy incentives:* the filer judges from the fact sheet whether one is a rebate. Enough, or refuse an
    incentive of uncertain character?
21. *Section A ownership* is folded into the line 17a question (a renter answers No). Accept?

**Across the stage**
22. *Generated returns that answer a form's screen No but carry its amounts* (seen in class M for Forms 5695 and
    2441; the ruled values agree): checked after the close, the interview cannot produce them. With the screens No
    and every Form 5695 or Form 2441 input removed, every line the full profile needs is known (Form 1040 lines 18 to
    37, Schedule 8812, Worksheet B, the four Form 2441 Part I targets), so those questions are never asked; only the
    test-return generator draws such amounts. Make the generator zero a part's amounts when its screen is No
    (TASKS.md T-052; it changes the generated corpus behind properties, compare and the class M jobs)?
23. *BUG-0079:* make a refusal outrank an unknown in every atom (both evaluators, with a property test)?
24. *Premise maps for the later stages* are in `research/premises/`, each with an adversarial verification beside it (`<slug>.verification.md`: 43 errors and 36 out-of-date items across the six, several changing a recommended decision; read the two together) (Schedule 1, Schedule E, the premium tax
    credit, the education credits, the capital loss carryover with a backlog, Form 5329), each with a draft
    decision batch; the placement there, rather than PREMISES.md, was this session's choice.

## Owner's answers (2026-10-22): all recommended answers below accepted

Follow-ups: 4 is built in Stage 16 with D10 (one excess-contribution screen for traditional and Roth contributions); 7, 11 and 13 are done with T-050; the rest keep the encoding as built.

1. Keep the stop order (contributions, then the AGI limit, then the worksheet): it follows the printed order, line 7's
   stop before line 8, and the questions it costs high-income filers are a handful of no's.
2. Keep the $200: the credit is right on those fixtures' facts.
3. Keep `w2.g_bad`: it refuses only an impossible entry.
4. Yes: ask, beside the traditional IRA screen, whether any 2025 Roth contribution was more than allowed or was
   recharacterized, and refuse on Yes. Checked: no screen mentions excess contributions today (`s2.other` names the
   additional tax on early distributions, not the 6% tax on excess contributions).
5. Keep two amounts per person: one per year adds three questions per person and changes no line.
6. Keep the encoding's display: it is the reading you chose (the ineligible person's line 6 is zero).
7. Yes, clarify the two labels (their reviews are rerun with T-050's).
8. Accept the refusal for "neither spouse has box 10": a credit with a 2024 grace-period amount on a joint return is rare.
9. Keep line 1e on your line 4 when no credit remains: no amount differs.
10. Accept the four Part I targets: the form says Part I "must" be completed.
11. Refuse employer-provided care (an on-site facility) when there are also paid expenses: rare, and the alternative
    counts a value as an expense paid, which the text does not say.
12. Keep the student-or-disabled refusal broad: i2441 and Pub. 503 disagree, and refusing is the reading that cannot
    be wrong.
13. Leave it, and record the reading in the ambiguity register: rare, and it can only understate.
14. Accept: a child aged 12 or under at the end of 2025 was under 13 all year.
15. Accept as is (display only); the question when the care was given costs every parent of a disabled 13-year-old
    one more question.
16. Keep the refusal for Section B on a newly built home: i5695 says Part II "is only available for existing homes".
17. Accept (no amount differs).
18. Accept the stand-in; teaching the checker that guarded branches exclude each other is a larger change for no
    difference at run time.
19. Confirm: the joint-occupancy rule is for fuel cells only, and they are refused.
20. Keep the filer's judgment with the fact sheet's description in the help.
21. Accept: a renter answers No to "your main home that you owned".
22. Done by T-052 (approved).
23. Done by BUG-0079 (approved).
24. For reading; nothing to decide here.

## Facts a fresh session needs

- Credit order: Form 2441 (Schedule 3 line 1 only), Form 8880 (lines 1 and 2), Form 5695 Part II (lines 1, 2, 4),
  Schedule 8812 Worksheet A (lines 1, 2, 4, 5b), Form 5695 Part I (with Worksheet B line 14 for line 19 when B is
  completed).
- `rerun_all.py` reruns only forms that already have logs; a new form's reviews are run directly
  (`transcribe.py --form`, `render_compare.py --form`, `classm.py --doc`), after `npm run render`.
- A change to one form's definition can be re-compared against the saved second transcription
  (`transcribe.py --form F --from-response`, `classm.py --doc F --from-response`), which keeps every ruling
  whose disagreement is unchanged; the render review judges the English and must be rerun.
- The Form 1099-R collection is return-level; the Form 5329 map (D1) proposes making it per person, which would
  change Form 8880 line 4.
