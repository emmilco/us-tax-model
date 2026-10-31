# Completeness review: adjudication of `dependent` (30 claims) and `household` (8 claims)

The rulings are in `rulings.json` (keys `unruled:dependent#n` and `unruled:household#n`). The standard is the one in
`docs/2026-10-30_completeness_experiment/adjudication.md`:

- A question that uses a defined term without its operative definition is a real gap. The test is whether a
  good-faith answer would plausibly be wrong and change the result.
- A rule that only leads to a refusal is out of scope, even when the refusal is wider than it needs to be.

The YAML is the working tree at `0fd59d3`. Witnesses were evaluated with `node engine/dist/main.js eval --inputs …
--json` on copies of committed fixtures with one to five inputs changed. The copies are in `/tmp/adj-compl-dh/w/`.
Severities and fixes are proposals; nothing was applied. Every fix rewords or adds an input, so the `dependent` or
`household` review goes stale.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| dependent | 30 | 19 | 5 | 6 | 0 | 0 |
| household | 8 | 2 | 2 | 3 | 1 | 0 |
| **Total** | **38** | **21 (55%)** | 7 | 9 | 1 | 0 |

- **Distinct defects.** The 21 real-gap claims are **12 distinct defects**:
  - PENDING-8 groups 5 claims;
  - PENDING-9 groups 5;
  - PENDING-1 has 2, one from each form.
- **Definitional claims.** 15 of the 21 are definitional, meaning the term is asked without its definition.
- **Not definitional.** Six are not: household#1, dependent#6, household#4, dependent#3, #22 and #27.

## PENDING-1. Qualifying surviving spouse is never tested (household#1, dependent#6). Proposed severity: High

- **Source.** i1040gi p. 15: "You can check the 'Qualifying surviving spouse' box … if all of the following apply. 1.
  Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025. 2. You have a child or stepchild (not
  a foster child) whom you can claim as a dependent or could claim as a dependent except that … 3. This child lived in
  your home for all of 2025 … 4. You paid over half the cost of keeping up your home. 5. You could have filed a joint
  return with your spouse the year your spouse died, even if you didn't actually do so."
- **Current encoding.** `f1040.status` is an input that accepts `qss`.
  - No line reads any QSS condition.
  - Head of household is tested by `household.hoh_eligible` and refused by `household.hoh_fails`. QSS has neither.
- **Witness.** Base `stage8.hoh.parent.test1`: wages $120,000 and a dependent parent, with no child and no deceased
  spouse.

  | Status | Line 12e | Line 15 | Line 24 |
  |---|---|---|---|
  | `single` | $15,750 | $104,250 | $17,367 |
  | `qss` (accepted, no refusal) | $31,500 | $88,500 | $9,646 |

  A filer who cannot be a QSS gets joint rates and the joint standard deduction.
- **Severity.** High is proposed for two reasons:
  - Every amount on the return depends on the status.
  - The project already holds head of household to a full test.

  If the owner treats the filing status as the filer's own responsibility, this drops to Medium.
- **Minimal fix.** Add a `household.qss_eligible` input that states the five conditions. Add a gate
  `household.qss_fails`, true when `f1040.status = qss` and the answer is No, and refuse where `household.hoh_fails`
  already refuses.
  - A fuller version would read the child condition from `dependent` (`relationship = child`, not foster,
    `months = 12`).
  - That needs a foster flag the encoding does not have, because `child` includes foster children.

## PENDING-2. A registered domestic partner's community income is neither asked nor refused (household#4). Proposed severity: Medium

- **Source.** i1040gi p. 23: "A registered domestic partner in Nevada, Washington, or California must generally report
  half the combined community income of the individual and their domestic partner."
- **Current encoding.**
  - `household.community_property` is asked.
  - The only gate, `household.hoh_community_property`, requires `household.married` and status `hoh`.
  - `amb.2025.hoh_community_property` (owner decision 2026-10-22) says a registered domestic partner "is not asked and
    is a gap to note". No BUG or T entry records it.
- **Witness.** Base `audit.household.single_community_property`: single, wages $215,300, `community_property` Yes.
  - **Tool:** no refusal. Line 1a is $215,300 and line 24 is $39,656.70.
  - **Source:** for a California registered domestic partner whose partner earned nothing, the filer reports half the
    combined community income (Form 8958), which is $107,650 of wages. Every line from 1a on changes.
- **Minimal fix.** Add the input `household.rdp`: "Were you a registered domestic partner in Nevada, Washington or
  California at any time in 2025?". Extend the gate to refuse when `community_property` and `rdp` are both Yes, with the
  Form 8958 / Pub. 555 remedy.

## PENDING-3. A person who was the filer's spouse during 2025 can pass as a qualifying relative (dependent#2). Proposed severity: Low

- **Source.** p501 p. 19: "If at any time during the year the person was your spouse, that person can't be your
  qualifying relative."
- **Current encoding.**
  - The `household_member` gloss of `dependent.relationship` says "other than your spouse".
  - `dependent.married` asks whether the person was married at the end of 2025.
  - A spouse divorced during 2025 who stayed in the household all year passes `dependent.qr_relationship`.
- **Witness.** Base `stage8.hoh.parent.test1` filed `single`, changed to `relationship` = `household_member`,
  `months` = 12 and `age` = 45. Line 19 is $500 (ODC); the source gives $0.
- **Minimal fix.** Make the `household_member` and `other` glosses say "other than a person who was your spouse at any
  time during 2025". This can be one edit with PENDING-4 and PENDING-5.

## PENDING-4. A joint return's relatives of the spouse are not counted (dependent#3). Proposed severity: Low

- **Source.** p501 p. 19: "If you file a joint return, the person can be related to either you or your spouse."
- **Current encoding.**
  - `dependent.relationship` asks "Relationship to you".
  - A spouse's parent, sibling or child fits `in_law` or `child`.
  - A spouse's nephew, niece, aunt or uncle fits only `other`, which requires a full year in the household and the
    local-law answer.
- **Witness.** Base `stage13.ctc_spouse_ssn` (mfj), with the person aged 30, `months` 0 and not in the household:
  - `other` gives line 19 $0;
  - `sibling`, the relationship through the spouse, gives $500.
- **Minimal fix.** Add to the question: "If you file a joint return, give the relationship to you or your spouse,
  whichever is closer."

## PENDING-5. Relationships by marriage are not said to survive death or divorce (dependent#4). Proposed severity: Low

- **Source.** p501 p. 19: "Any of these relationships that were established by marriage aren't ended by death or
  divorce."
- **Current encoding.** The `in_law` gloss reads "(step-parent or in-law)". A former mother-in-law after a divorce is
  plausibly entered as `other`.
- **Witness.** Base `stage8.hoh.parent.test1` filed `single`, with `months` 0:
  - `in_law` gives line 19 $500;
  - `other` gives $0.
- **Minimal fix.** Make the gloss "(step-parent or in-law, including one whose relationship began with a marriage that
  has since ended by death or divorce)".

## PENDING-6. A rest home is not said to count as the parent's main home (dependent#7). Proposed severity: Medium

- **Source.** p501 p. 9: "If you pay more than half the cost of keeping your parent in a rest home or home for the
  elderly, that counts as paying more than half the cost of keeping up your parent's main home."
- **Current encoding.** `dependent.parent_home_paid`: "did you pay over half the cost of keeping up a home that was
  their main home for all of 2025".
- **Witness.** Base `stage8.hoh.parent.test1` (hoh):
  - `parent_home_paid` Yes gives head of household, with line 16 at $14,378;
  - No, the literal answer of a filer paying a care home, gives the refusal `household.hoh_fails`.

  The correct return is head of household.
- **Why Medium.** A parent in assisted living or a nursing home is a common Test 1 situation.
- **Minimal fix.** Append to the question: "A rest home or home for the elderly whose cost you paid over half of counts
  as their main home."

## PENDING-7. A temporary absence is not conditioned on an expected return (dependent#8). Proposed severity: Low

- **Source.** p501 p. 9, Temporary absences: "It must be reasonable to assume the absent person will return to the home
  after the temporary absence. You must continue to keep up the home during the absence."
- **Current encoding.** `dependent.months`, `part_year_home` and `us_half` count absences "for … medical care" as time
  lived with you, with no condition. A grandparent who moved permanently into a nursing home is plausibly counted.
- **Witness.** Base `stage8.hoh.parent.test1` with `relationship` = `parent_relative` and `household.home_cost` Yes:
  - `months` 12 gives head of household, with line 16 at $14,378;
  - `months` 0, the correct answer for a permanent move, gives the refusal `household.hoh_fails`.
- **Note.** The claim is definitional and weak, because "temporary" carries the condition in ordinary usage. It is ruled
  a gap because the gloss lists "medical care" without the qualifier.
- **Minimal fix.** Add "(only if it is reasonable to assume the person will return to your home)" after "temporary
  absences" in the three questions.

## PENDING-8. The support questions omit Pub. 501's support rules (dependent#10 to #14). Proposed severity: Low

- **Source.** p501 pp. 19–20. Each rule and its claim:

  | Claim | Rule |
  |---|---|
  | #11 | "A person's own funds aren't support unless they are actually spent for support." |
  | #14 | "For lodging, the amount of support is the fair rental value of the lodging." |
  | #12 | "The part of the allotment contributed by the government and the part taken out of your military pay are both considered provided by you." |
  | #13 | "Payments you receive for the support of a foster child from a child placement agency are considered support provided by the agency." |
  | #10 | "You can't include in your contribution to your child's support any support paid for by the child with the child's own wages, even if you paid the wages." |

- **Current encoding.**
  - `dependent.supported` gives only the TANF rule.
  - `dependent.self_support` gives nothing.
  - The TANF sentence, "TANF or other public assistance payments you received and used to support this person count as
    support you provided", invites a foster parent to count agency payments as their own support (#13). That is the
    opposite of the source.
- **Witnesses.**
  - **Qualifying-relative path.** Base `stage8.hoh.parent.test1` filed `single`: `supported` Yes gives line 19 $500,
    No gives $0. This is the lodging case (#14) and the allotment case (#12).
  - **Qualifying-child path.** Base `stage8.single.phaseout.partial` with the child aged 16: `self_support` No gives
    line 19 $1,400, Yes gives $0. This is a teenager who saved large earnings (#11).
- **Minimal fix.** Add one short definition to both questions: "Count lodging at its fair rental value; count a
  person's own funds only if actually spent for their support; count both parts of a military allotment as yours; do not
  count foster care payments from a placement agency as yours, or support your child paid for with wages, even wages you
  paid."

## PENDING-9. The care-expense question omits the definition of care (dependent#20 to #24). Proposed severity: Medium

- **Source.** i2441 p. 2. Each rule and its claim:

  | Claim | Rule |
  |---|---|
  | #20 | "It doesn't include the cost of food, lodging, education, clothing, or entertainment." |
  | #23 | "But don't include the cost of schooling for a child in kindergarten or above." |
  | #24 | "But don't include any expenses for sending your child to an overnight camp, a summer school, or a tutoring program." |
  | #21 | Out-of-home care for anyone other than a dependent under 13 requires the person to spend at least 8 hours a day in your home. |
  | #22 | "If the care was provided by a dependent care center, the center must meet all applicable state and local regulations." |

- **Current encoding.**
  - `dependent.dc_paid` lists exclusions: prior-year care, 2026 care, state reimbursements, ineligible providers and
    medical expenses.
  - It does not give these definitions.
  - Neither `f2441.care` nor `dcprov` gives them either.
- **Witness.** Base `stage15.f2441.s2` (mfj, children 6 and 9, $3,500 each). The changed case assumes $2,000 of each
  child's amount was kindergarten tuition or summer school.

  | Case | Line 11 | Line 24 |
  |---|---|---|
  | $3,500 each (current) | $1,200 | $346 |
  | $1,500 each (source) | $600 | $946 |

- **Why Medium.** Private-school tuition from kindergarten up, summer school and overnight camp are common entries.
- **Minimal fix.** Extend the exclusion list in `dc_paid` with:
  - "schooling for kindergarten or above, overnight camp, summer school or tutoring";
  - "food, lodging, clothing or entertainment that can be separated from the care";
  - "care outside your home for a qualifying person 13 or older who does not regularly spend at least 8 hours a day in
    your home";
  - "a dependent care center that does not meet state and local regulations".

## PENDING-10. An expired, unrenewed ITIN answers the TIN question Yes (dependent#25). Proposed severity: Low

- **Source.** p503 p. 3: "If your ITIN wasn't included on at least one U.S. federal tax return for the last 3
  consecutive tax years, it expires on December 31 of the third consecutive tax year, and must be renewed before being
  used again on a U.S. federal tax return."
- **Current encoding.** `dependent.tin` asks whether an ITIN was "issued … or have you applied for an ITIN". An expired
  ITIN was issued.
- **Witness.** Base `stage8.hoh.parent.test1` filed `single`:
  - `tin` Yes gives line 19 $500;
  - No, the correct answer when the ITIN has expired and no renewal was applied for, gives the refusal
    `dependent.claimed_no_tin`.
- **Minimal fix.** Add "An ITIN that has expired counts only if it has been renewed, or renewal applied for, by the due
  date."
- **Sibling.** `person.tin` ("an SSN or ITIN issued on or before the due date") has the same omission and could take
  the same sentence. It was outside this review.

## PENDING-11. The Form 1098-T exception omits the cooperation condition (dependent#27). Proposed severity: Low

- **Source.** i8863 p. 1: "You must fully cooperate with the educational institution's efforts to gather the
  information needed to furnish the Form 1098-T."
- **Current encoding.**
  - `dependent.edu_1098t`'s exception requires only a request after February 2, 2026 and proof of enrollment and
    payments.
  - The date half of the claim is already ruled in `amb.2025.edu_1098t_date`.
- **Witness.** Base `stage19.example.jack_kay`:
  - `edu_1098t` Yes gives line 30 $2,500 (line 29 $1,000, Schedule 3 line 3 $1,500);
  - No gives $0.

  The rule matters only to a filer who requested the form and did not cooperate, so it is rare.
- **Minimal fix.** Add "and you fully cooperated with the institution's efforts to furnish it" to the exception.
  `person.edu_1098t` should take the same change.

## PENDING-12. Sports, hobby and noncredit courses are not excluded from education expenses (dependent#30). Proposed severity: Low

- **Source.** i8863 p. 4: "Any course or other education involving sports, games, or hobbies, or any noncredit course,
  unless such course or other education is part of the student's degree program or (for the lifetime learning credit
  only) helps the student acquire or improve job skills."
- **Current encoding.**
  - `dependent.edu_inst` excludes personal expenses, expenses deducted elsewhere and expenses used for tax-free
    distributions.
  - `research/premises/stage19-education-credits.md` quotes this rule, but the question omits it.
  - `person.edu_inst` has the same omission.
- **Witness.** Base `stage19.example.jack_kay`:
  - `edu_inst` $4,300 gives line 30 $2,500;
  - removing a $1,000 noncredit hobby course outside the degree program gives $3,300, so line 30 is $2,325 and line 29
    falls from $1,000 to $930.
- **Minimal fix.** Add to both questions: "Do not include a course involving sports, games or hobbies, or a noncredit
  course, unless it is part of the student's degree program (or, for the lifetime learning credit, helps the student
  acquire or improve job skills)."

## Notes (no PENDING)

- **N1. Over-refusal from `dependent.other_claimant` (dependent#5, ruled out of scope).**
  - **The omitted carve-out.** i1040gi p. 19, Step 4, says a qualifying relative must not be the qualifying child of
    any *taxpayer*. "For this purpose, a person isn't a taxpayer if the person isn't required to file … or files only to
    get a refund."
  - **What the question asks.** `dependent.other_claimant` asks about "any other person" and omits the carve-out.
  - **What a Yes does.** It refuses every listed person, through the refusal on `dependent.qualifying_child`. Witness
    (`stage8.hoh.parent.test1` filed `single`, `other_claimant` Yes): line 19 is the refusal `other_claimant`.
  - **Effect.** A filer supporting a non-filing partner's child who lives with them all year is refused, when the
    source would allow a $500 ODC.
  - **Status.** This is an over-refusal, not a wrong amount. It could be listed as a T item. Adding the carve-out to the
    question's wording is a candidate fix.
- **N2. Checker format.** `check_completeness.py` accepts only `BUG-NNNN` for a real gap. With the `PENDING-n`
  placeholders, it reports 21 ruling errors, one per real-gap claim, and exits 1.
  - Once real ids are substituted, the file validates: checked by substituting dummy `BUG-9nnn` ids and calling
    `validate_all`, which returned no errors.
  - All 38 claims are ruled, and none of the 57 remaining unruled findings belong to these two forms.

## What this suggests about the tool

- **The unit hides refusals on other forms.**
  - Each form was shown only its own lines. 9 of the 17 non-gap claims were refused or asked on a form the model did
    not see: dependent#15, #26, #28 and #29, and household#2, #3, #5, #6 and #7.
  - The experiment saw the same failure (EIC claim 3).
  - The docstring already names this limit for collection forms, but it is broader. Every form reads gates on `scope`,
    `sa`, `f2441`, `f8863` and `eic`.
  - Adding to the prompt the refusal list of each line the form reads (`when:` gates with their form and remedy text,
    not their logic) would remove most of these claims cheaply.
- **The cited pages pull in a whole publication section.**
  - The dependent prompt included p501 pp. 19–20 and i2441 p. 2. These are worksheet-level definitions, so 10 of the
    19 dependent gaps are definitional.
  - That is accurate, but it calls for the owner standard that the experiment asked for: whether every term of art in
    a yes/no question must carry its definition.
  - Without that standard, every rerun reopens it.
- **Groups of claims share one fix.**
  - The model returned one claim per sentence: 5 claims on the support definition and 9 on `dc_paid`.
  - Asking it to group claims by the encoded item they bear on, with the sentences listed under it, would cut
    adjudication time about in half for these two forms.
