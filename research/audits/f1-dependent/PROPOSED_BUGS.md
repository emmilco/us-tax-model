# Proposed bug inventory entries, F1 dependent/education batch

Placeholder ids `PENDING-n`; the integrator assigns sequential ids when appending to `BUG_INVENTORY.md`. Each entry
was written on branch `claude/f1-dependent`; commits are named in REPORT.md.

## PENDING-1 — A returned kidnapped child who lived with you more than half of 2025 was refused

- **Caught by:** T-105 (T-092 split, fixr2 dependent F1); premise reproduced on the current tree by reading the
  refusals (`dependent.lived_half` and `dependent.eic_child` refused on `dependent.kidnapped` alone), 2026-11-03.
- **Source:** p501 p. 13, Kidnapped child, "You can treat your child as meeting the residency test even if the child
  has been kidnapped, but the following statements must be true."; i1040gi p. 17, Step 1, "Who lived with you for
  more than half of 2025"; p. 41, Step 3.
- **Symptom:** a child presumed kidnapped and since returned, who lived with you 11 or 12 months of 2025, was refused
  at the residency tests although the kidnapped-child treatment is not needed to meet them. Over-refusal; no wrong
  amount.
- **Fix:** gates `dependent.kidnap_residency` (kidnapped and fewer than 7 months) on `dependent.lived_half` and
  `dependent.kidnap_eic` (kidnapped, EIC relationship, not in the United States for more than half of 2025) on
  `dependent.eic_child`. `dependent.months` and `dependent.us_half` now say that time a kidnapped child was missing
  does not count, so the refusal still catches every case that needs the treatment. T-104 rewords
  `dependent.kidnapped`: a child missing because of a kidnapping at some time in 2025, whenever law enforcement first
  presumed it (p501 p. 13 ties the year to the kidnapping). The row's suggested wording ("kidnapped in 2025") would
  have dropped a child kidnapped earlier and returned in 2025, whose year of return still applies the rule; the new
  question keeps that case.
- **Fix lines:** `dependent.kidnapped`, `dependent.kidnap_residency`, `dependent.kidnap_eic`, `dependent.lived_half`,
  `dependent.eic_child`, `dependent.months`, `dependent.us_half`
- **Siblings checked:** `dependent.qr_kidnapped` (unchanged: the qualifying-relative branch still refuses any child
  under 19 presumed kidnapped), `household.qss_child` wording (unchanged, its own kidnapped sentence),
  `f1040.line12e` QSS remedy (unchanged), `dependent.hoh_lived_half`, `dependent.dc_lived_half` (both read
  `lived_half`, so they inherit the narrower refusal).
- **Regression predictions:** `f1.kidnapped.returned_11` (11 months, in the United States more than half the year):
  qualifying child, EIC qualifying child, EIC $3,261 (i1040gi p. 53 table rows $25,000 and $30,000, one child).
  `stage21.d3.kidnapped_child_refused` moves to 4 months and not in the United States for more than half the year and
  is refused at line 16 (`kidnap_residency`) and line 27a (`kidnap_eic`). The two `stage21.f1.where_kidnapped_withheld_*`
  evaluator regressions move their withheld child to 4 months (and the EIC case out of the U.S. half-year) so the
  kidnapped answer still decides an unanswered gate; their expectations are unchanged. Predictions written before the
  evaluator was run.
- **Validation:** CLI fixtures; dependent transcription/render reviews rerun (Claude); completeness rerun.
- **Tags:** over-refusal; residency; fixed

## PENDING-2 — BUG-0283 is fixed: a non-taxpayer's qualifying child can be your qualifying relative

- **Caught by:** BUG-0283 (T-153), recorded open; this entry closes it because the inventory is append-only.
- **Source:** i1040gi p. 19, Step 4, "Who wasn’t a qualifying child (see Step 1) of any taxpayer for 2025. For this
  purpose, a person isn’t a taxpayer if the person isn’t required to file a U.S. income tax return and either doesn’t
  file such a return or files only to get a refund of withheld income tax or estimated tax paid."; p501 p. 18, Child of
  person not required to file a return, Examples 1 to 3, and Child in Canada or Mexico; p501 p. 15, Qualifying Child of
  More Than One Person.
- **Symptom:** as recorded in BUG-0283; in addition, the EIC tie-breaker refusal on `dependent.eic_child` fired for any
  listed person answering `other_claimant` Yes, including one who is not your EIC qualifying child.
- **Fix:** new input `dependent.other_nontaxpayer`. Gate `dependent.qc_tiebreak` replaces `other_claimant` on
  `dependent.qualifying_child`: it refuses when the person is the qualifying child of another person and either is
  also your qualifying child (the tie-breaker rules have no non-taxpayer exception, so the refusal stands whatever the
  other person's filing) or the other person is a taxpayer. Gate `dependent.eic_tiebreak` replaces it on
  `dependent.eic_child` and refuses only a child who passes your EIC relationship, age, joint-return and residency
  tests. The row's suggested fix (define the taxpayer in `other_claimant` itself) would also have lifted the
  tie-breaker refusal for your own qualifying child whose other parent does not file, which p501 pp. 15-16 do not
  support; the split avoids that.
- **Fix lines:** `dependent.other_nontaxpayer`, `dependent.qc_tiebreak`, `dependent.eic_tiebreak`,
  `dependent.qualifying_child`, `dependent.eic_child`
- **Siblings checked:** `dependent.qualifying_relative` (unchanged; it reads `qualifying_child`, whose refusal is now
  the gate), `eic.qc_of_another` (the filer as another's qualifying child; separate input, unchanged),
  `dependent.other_claimant` question (unchanged; still includes the EIC rules, so a Yes under the EIC rules alone and
  a taxpayer other person still refuses: accepted over-refusal).
- **Regression predictions:** `f1.t153.friend_child_nontaxpayer` (p501 p. 18 Example 1 on a joint return): not your
  qualifying child, your qualifying relative, line 19 $500. `f1.t153.friend_child_taxpayer` (Example 3): refused at
  `qc_tiebreak`. `f1.t153.own_child_nontaxpayer_other`: your own child, other person not a taxpayer, still refused at
  `qc_tiebreak`. `stage8.refuse.dependent.other_claimant` and `stage9.eic.refuse.child_of_another` keep their refusals
  under the new gate ids without answering the new input. Written before the evaluator was run.
- **Validation:** CLI fixtures; eight consumer pairs ruled `same` in `reviews/2025/consumers.json`.
- **Tags:** over-refusal; qualifying-relative; fixed

## PENDING-3 — BUG-0285 is fixed: the lifetime learning credit is refused for a student whose ITIN or ATIN was only applied for

- **Caught by:** BUG-0285 (T-113), recorded open; owner decision T-113 (2026-11-01).
- **Source:** i8863 p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or
  her 2025 return (including extensions)."; i8863 p. 3, Table 1, lifetime learning column, "Students must have been
  issued a TIN by the due date of their 2025 return (including extensions)"; p970 p. 11 (the deeming sentence, in the
  American opportunity credit chapter only).
- **Symptom:** as recorded in BUG-0285; the person side had the same reading (`person.edu_student` accepts
  `person.itin_applied`).
- **Fix:** gates `dependent.edu_llc_tin_refused` (new input `dependent.edu_tin_issued` No) and
  `person.edu_llc_tin_refused` (`person.tin` No, so only `itin_applied`) refuse line 31 of a lifetime learning credit
  student. `edu_student` and the American opportunity credit are unchanged (p970 p. 11's deeming). Table 1's lifetime
  learning column requires only the student's TIN, so "or filer" in the owner decision is read as the filer who is
  the student; a filer whose ITIN was only applied for and who claims the credit for a dependent student with an
  issued number is not refused.
- **Fix lines:** `dependent.edu_tin_issued`, `dependent.edu_llc_tin_refused`, `dependent.edu_line31`,
  `person.edu_llc_tin_refused`, `person.edu_line31`
- **Siblings checked:** `dependent.edu_aoc`, `person.edu_aoc` (deeming kept through `household.all_tin`),
  `dependent.edu_llc`, `person.edu_llc`, `f8863.line10`, `household.tin_count`.
- **Regression predictions:** `f1.t113.dep_llc_applied` (stage19.blind.e3, daughter's ATIN applied for) and
  `f1.t113.person_llc_itin_applied` (stage19.example.llc_phaseout, taxpayer's ITIN applied for) refuse at line 31 and
  Part II line 10. `f1.t113.dep_aoc_applied` (stage19.example.jack_kay) and `f1.t113.person_aoc_itin_applied`
  (stage19.example.aoc_phaseout) keep every value. Written before the evaluator was run.
- **Fixture context repair:** `stage19.blind.e3`, `stage19.blind.e9`, `stage19.refuse.period_over_dependent` and
  `stage21.pending1.qss_valid_computes` answer the new input Yes (inferred from their "has a TIN" answer), annotated
  in each evidence note; no expected value changed.
- **Over-refusal accepted:** the return is refused rather than prepared without the lifetime learning credit for that
  student, as the owner decided.
- **Validation:** CLI fixtures; dependent and person transcription/render reviews rerun (Claude).
- **Tags:** eligibility; education; owner-decision; fixed

## PENDING-4 — Form 2441 line 2 columns (c) and (d) were shown for a person who is not a qualifying person

- **Caught by:** T-112 (t091 dependent.classm L1); premise confirmed: neither line had `shown_when`.
- **Source:** i2441 p. 3, Line 2, "Don't list a person on line 2 unless they are listed as an eligible person under
  Qualifying Person(s), earlier".
- **Symptom:** the values sheet showed a line 2 row for every listed dependent; on
  `stage15.regress.f2441.nonqualifying_dependent` four line 2 entries instead of two. No amount changed.
- **Fix:** `shown_when: dependent.dc_qp` on `dependent.dc_line2c` and `dependent.dc_line2d`.
- **Fix lines:** `dependent.dc_line2c`, `dependent.dc_line2d`
- **Siblings checked:** `f2441.line2d_total` (sums `dc_line2d` over qualifying persons only; unchanged), `dependent.dc_qp`.
- **Regression predictions:** `f1.dc.line2_shown_qualifying_only` asserts the condition (`dc_qp` true and false) and
  line 3 $3,000; the values-sheet count (four to two) was checked by hand with `eval --html`, since fixtures cannot
  assert visibility.
- **Validation:** CLI fixtures; render review rerun.
- **Tags:** display; source-transcription; fixed

## PENDING-5 — BUG-0282 is fixed: support-definition details in the dependent support questions

- **Caught by:** BUG-0282 (T-107, T-108, T-109), recorded open.
- **Source:** p501 p. 15 (foster care payments and expenses), p. 20 (total support, tax-exempt income, year support is
  provided, armed forces allotments and quarters allowances, state support of a needy person, home for the aged),
  p. 21 (own home, rent free, property, capital expenses, medical insurance premiums and benefits, GI Bill, childcare,
  Don't Include in Total Support items 1 to 6).
- **Symptom:** as recorded in BUG-0282; T-108's sentence could be read as the state supporting the filer.
- **Fix:** `dependent.supported` and `dependent.self_support` state the total-support definition and the listed rules;
  "Benefits a state provides to this person as a needy person". Wording only; a filer who answered from the shorter
  text and now counts differently may move between a computed dependent and none. Not a support worksheet.
- **Fix lines:** `dependent.supported`, `dependent.self_support`
- **Regression predictions:** none (no expression changed).
- **Validation:** dependent render and completeness reviews rerun.
- **Tags:** source-definition-debt; wording; fixed

## PENDING-6 — BUG-0284 is fixed: the care-expense question names child support and the allocation rules

- **Caught by:** BUG-0284 (T-154), recorded open.
- **Source:** i2441 p. 2 ("Child support payments aren't qualified expenses."; "you must figure your expenses for each
  day"); p503 p. 6 (temporary absence, part-time work); p503 p. 8 (expenses partly work related).
- **Fix:** `dependent.dc_paid` adds the child-support exclusion, day-by-day allocation with its two exceptions, and the
  mixed-purpose division; existing exclusions kept. Wording only.
- **Fix lines:** `dependent.dc_paid`
- **Tags:** source-definition-debt; wording; fixed

## PENDING-7 — BUG-0300 is fixed: a stillborn child is excluded and a live birth is required

- **Caught by:** BUG-0300 (T-167). **Source:** p501 p. 13, Child born alive and Stillborn child.
- **Fix:** `dependent.born_died` states the live-birth requirement (state or local law, official record) and says not
  to list a stillborn child. Consumer pairs `born_died@p501:p9` and `born_died@p503:p3` ruled `same`. Wording only.
- **Tags:** source-definition-debt; wording; fixed

## PENDING-8 — BUG-0301 is fixed: the dependent student question defines a school and treats co-op students as full-time

- **Caught by:** BUG-0301 (T-168). **Source:** p501 p. 13, Student defined, Full-time student, School defined,
  Vocational high school students.
- **Fix:** `dependent.student` adds the school definition, the school's own full-time standard, non-consecutive months
  and the co-op rule. Wording only.
- **Tags:** source-definition-debt; wording; fixed

## PENDING-9 — Dependent question wording: newborn hospital stay, revoked release, TANF for a parent's home

- **Caught by:** T-106 (completeness r7), T-110 (completeness r3/r4), T-111 (fixr4).
- **Source:** p501 p. 13, Death or birth of child ("except for any required hospital stay following birth"); p501
  p. 22, Revocation of release of claim to an exemption ("written notice of the revocation to the noncustodial parent in
  2024 or earlier"); p501 p. 9, Note (TANF).
- **Fix:** `dependent.months` counts a newborn's required hospital stay; `dependent.divorced_rule` says a release
  revoked without notice in 2024 or earlier still applies for 2025; `dependent.parent_home_paid` counts TANF used for the
  home as paid by you (the household question already carried this sentence, T-115). Wording only.
- **Fix lines:** `dependent.months`, `dependent.divorced_rule`, `dependent.parent_home_paid`
- **Tags:** source-definition-debt; wording; fixed
