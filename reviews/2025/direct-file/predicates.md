# Direct File (TY2024) fact dictionary read against the household predicates

Integrity plan item 1.7 (`docs/2026-10-22_integrity_plan.md`). A reader from outside the model family on the
dependent tests, head of household, the EIC eligibility steps, the CTC/ODC qualifying person and the standard
deduction boxes. Direct File's arithmetic is not used; only its derived-fact logic is compared. Every difference
is checked against the 2024 and 2025 Form 1040 instructions before it counts as a finding.

## Header

**Direct File.** `IRS-Public/direct-file`, commit `e365f9f43446010af36cccf7edecc52953c00fe9` (2026-06-11,
"Update README.md"), shallow clone in `.direct-file/` (gitignored). Tax year 2024 logic. Fact dictionary
modules read (all under `.direct-file/direct-file/backend/src/main/resources/tax/`; the client's
`df-client-app/src/fact-dictionary/generate-src/xml-src` is a symlink to this directory; 37 files, 36 modules
plus `copy.xml`):

| Module | Lines | Read for |
|---|---|---|
| `familyAndHousehold.xml` | 5204 | qualifying child / relative tests, residency, citizenship, TINs, HoH and QSS qualifying person, EITC QC, CTC/ODC eligibility, CDCC qualifying person, knockouts |
| `dependentsRelationship.xml` | 1321 | relationship enums; `qcRelationshipTest`, `qrRelationshipTest`, `marriedHohRelationshipTest` |
| `dependentsBenefitSplit.xml` | 687 | children of divorced or separated parents (the "benefit split"), its knockouts |
| `filingStatus.xml` | 1116 | `eligibleForHoh`, `eligibleForMFJ`, `eligibleForQss`, status validity |
| `filers.xml` | 5544 | filer age (65, 25, 64), blindness, SSN validity for EITC, dependent-filer facts, lived-apart and separation facts, knockouts |
| `eitc.xml` | 2671 | eligibility (`maybeEligibleForEitc*`, `eitcQcTest`, `eitcNoticeTest`), limits, investment income |
| `ctcOdc.xml` | 1596 | `ctcEligibleDependents`, `odcEligibleDependents`, improper-claims disqualification |
| `standardDeduction.xml` | 355 | additional standard deduction items, MFS spouse rule, dependent filer deduction |
| `constants.xml` | 1035 | tax year, majority of days in year |
| `flow.xml` | 790 | `/flowIsKnockedOut` (the knockout list) |
| `cdcc.xml`, `ptc.xml`, `interest.xml` | — | only the three knockout facts named in the flow (`knockoutStudentOrDisabled`, `dependentsRequiredToFile`, `hasInterestIncomeAndAgiAboveThresholdForMfs`) |

Knockout screens were located in `df-client/df-client-app/src/flow/flow-chunks/you-and-your-family/*.tsx` and
`credits-and-deductions/*.tsx` (`isKnockout` screens); two option labels were read from
`df-client/df-client-app/src/locales/en.yaml`. Direct File's XML was rendered to one-line expression trees by a
script kept outside the clone (`/tmp/df/render.py`, run with `python3 -I`); no Direct File code was executed.

**Project.** HEAD `a946fae54fd4dcf118253989e4ce6293987d00a1`. Files: `forms/2025/dependent.yaml`,
`forms/2025/household.yaml`, `forms/2025/eic.yaml` (Steps 1 to 4 and the Worksheet A/B joins),
`forms/2025/s8812.yaml` (lines 4 and 6), `forms/2025/sa.yaml` (standard deduction boxes, the dependent-filer rule),
with `forms/2025/person.yaml` (per-filer inputs the household lines read), `forms/2025/f2441.yaml`
(`f2441.nondependent_gate`, read for row 36 only) and `params/2025.yaml`. Instruction texts:
`sources/2024/i1040gi.cols.txt`, `sources/2025/i1040gi.cols.txt` (Head of Household pp. 14–15; Who Qualifies as
Your Dependent pp. 17–22; EIC Steps 1–6 and Definitions pp. 40–45; Standard Deduction pp. 33–35),
`sources/2025/i1040s8812.cols.txt`, `sources/2024/i1040s8812.cols.txt`, `sources/2025/p501.cols.txt` (one
sentence), `sources/2025/i2441.cols.txt` (one sentence).

**Conventions.** Direct File paths are given relative to the module (`../x` is a sibling fact of the same
`/familyAndHousehold/*` item; `filers:` and the like name another module). "DF age" is
`taxYear − year of birth`, which is the age at the end of the tax year; "day-before age" is the same computed
from the day before the birthday, which is how Direct File gives a January 1 birthday to the prior year.
Classifications: AGREE; DIFFER; DF-NARROWER (Direct File knocks out or denies where the project computes);
PROJECT-NARROWER (the project refuses or denies where Direct File computes); NOT-IN-DF (Direct File has no fact
for the condition; it is assumed or out of scope).

## Comparison

### dependent.yaml

| # | Project line(s) | Direct File fact(s) | Class | Note |
|---|---|---|---|---|
| 1 | `dependent.qc_relationship` (child, sibling, sibling_descendant) | `../qcRelationshipTest` (dependentsRelationship.xml): biological/adopted/step/foster child, grandchild or other descendant of child, sibling, half/step sibling, child of sibling/half/step sibling, other descendant of sibling/half/step sibling | AGREE | Same set; DF enumerates 14 values where the project's three enum values carry the same relatives in their source text. |
| 2 | `dependent.qc_age`, under-19 and student-under-24 branches, with `dependent.age`, `dependent.student`, `dependent.younger` | `../ageTest` = (age < 19 ∧ dateOfBirth > `filers:/minimumFilerDateOfBirth`) ∨ `../isAStudentUnder24` (fullTimeStudent ∧ 18 < age < 24 ∧ dateOfBirth > minimumFilerDateOfBirth) ∨ (disabled branch, row 3) | AGREE | DF age is age at end of year. "Younger than you (or your spouse)" is tested against the oldest filer's date of birth (`Minimum(/filers/*/dateOfBirth)` when MFJ), i.e. younger than at least one filer: the project's `dependent.younger` text says the same. |
| 3 | `dependent.qc_age`, disabled branch (`dependent.disabled = true`, no age or "younger" test) | `../permanentTotalDisability ∧ ../disabilityStatusMayAffectBenefits`; the latter = ageAtFirstHalfOfYear ≥ 18 ∨ (ageAtFirstHalfOfYear < 18 ∧ dateOfBirth > minimumFilerDateOfBirth) | DF-NARROWER | For a disabled person under 18 on July 2 who is not younger than the oldest filer, DF never asks about disability, so the age test fails. The text ("Any age and permanently and totally disabled", 2025 p. 17; identical 2024 p. 17) has no "younger than you" clause on this branch. Reachable only for a filer aged 16–18 (DF knocks out filers under 16). Not a project issue. |
| 4 | `dependent.lived_half` (`dependent.months > 6`; months input counts temporary absences and the born/died/placed exceptions) | `../residencyTest` = residencyDuration ≠ lessThanSixMonths; options (en.yaml 18027–18029): "All year", "More than 6 months ({{majorityOfDaysInYear}} days) but less than a year", "6 months or less"; `constants:/majorityOfDaysInYear` = 184 in a leap year, else 183 | AGREE | Both are "more than half of the year". DF's exception handling is in screen text, not read here. |
| 5 | `dependent.self_support = false` | `../qcSupportTest` = ¬`../ownSupport` | AGREE | |
| 6 | `dependent.joint_return = false` (input: "filing a joint return other than only to claim a refund") | `../jointReturnTest` = ¬married ∨ ¬jointReturn ∨ (filingOnlyForRefund ∧ ¬requiredToFile) | PROJECT-NARROWER | DF adds "not required to file" to the refund-only exception (Pub. 501's condition). Moot in the project: `dependent.married` refuses every married dependent (rows 10, 31). |
| 7 | `dependent.qualifying_child` = qc_relationship ∧ qc_age ∧ ¬self_support ∧ ¬joint_return ∧ lived_half | `../qualifyingChild` = qcRelationshipTest ∧ ageTest ∧ residencyTest ∧ qcSupportTest ∧ jointReturnTest | AGREE | Same five tests, conjunction. |
| 8 | `dependent.qualifying_child` refusal `when: dependent.other_claimant` (tie-breaker rules) | `../eligibleDependent` carries "TODO: This does not account for qualifying child tiebreakers"; DF computes the dependent. Only `../eitcQualifyingChild` and `../hohQualifyingPerson` test `Any(¬isQualifyingChildOfAnother, isClaimedDependent)` | PROJECT-NARROWER | DF lets the filer claim a child who could be another person's qualifying child without applying the tie-breaker; the project refuses. |
| 9 | refusal `when: dependent.divorced_rule` | dependentsBenefitSplit.xml: `../eligibleForBenefitSplit`, `../tpCanClaimSplitBenefitsHohEitcCdcc`, `../disqualifiedDueToParentalCustody`; knockouts `/knockedOutByNonCustodialParentBenefitSplit`, `/knockedOutByContradictory8832` | PROJECT-NARROWER | DF models the custodial parent who signed Form 8332 (keeps HoH/EITC/CDCC, loses dependent and CTC) and the non-parent relative; it knocks out the noncustodial parent claiming under the release and contradictory answers. The project refuses all. |
| 10 | refusal `when: dependent.married` (Step 2 q2 / Step 4 q3) | `../married`, `../jointReturnTest` (row 6); DF computes | PROJECT-NARROWER | |
| 11 | `dependent.resident` = citizen ∨ canada_mexico; the citizen input text folds in the adopted-child exception | `../citizenOrResidentTest` = citizenOrUsResidentTest ∨ canadaMexicoResident ∨ `../adoptedChildException` (adopted ∧ `filers:/eitherFilerUSCitizenOrNational` ∧ residencyDuration = allYear) | AGREE | Same disjunction; DF asks the exception as facts, the project as question text. |
| 12 | `dependent.qc_dependent`, `dependent.qr_dependent`, `dependent.claimed` (no TIN condition) | `../eligibleDependentMinusFilerInformation` requires `(../tinType ≠ none)`; `/knockoutHohQpHasNoTin`; `/knockoutPersonBornAndDiedInTaxYearWithoutTin` | DIFFER | DF: a person with no SSN/ITIN/ATIN cannot be a dependent at all (and an HoH qualifying person without a TIN is a knockout). Project: `claimed` and `hoh_test1/2` do not read `dependent.tin`; only `ctc_child`, `odc_person` and `dc_no_tin` do. See Finding F1. |
| 13 | `qc_dependent`/`qr_dependent` require `sa.dependent = false`; `sa.dependent` refuses (Step 2 q4, Step 4 q5) | `filers:/treatFilersAsDependents` (primary: canBeClaimed ∧ (claimer must file ∨ (did file ∧ ¬refund only)); MFJ: `/isMFJDependent` = not required to file ∧ claiming refund only); `../eligibleDependent` = ¬treatFilersAsDependents ∧ … | PROJECT-NARROWER | Same nuance ("not required to file, isn't filing or files only for a refund" → not a dependent) in the project's question text; DF computes the dependent filer's return (row 65), the project refuses it. |
| 14 | `dependent.claimed` = qc_dependent ∨ qr_dependent (every eligible person is claimed) | `../isClaimedDependent` = `../tpClaims` ∧ eligibleDependent; `../isClaimedIfClaimable` = isClaimedDependent ∨ ¬eligibleDependent | DIFFER | DF has an election not to claim an eligible person; the project has none. Text: "The dependents you claim are those you list by name and SSN" (2025 p. 14, p. 17; 2024 same) — a choice, not a rule; undecidable as a rule difference. No finding; a design note. |
| 15 | `dependent.qr_relationship` (child, sibling, parent, parent_relative, in_law; household_member/sibling_descendant/other only with months = 12) | `../relationshipMemberOfHouseholdTest` = `../qrRelationshipTest` ∨ `../memberOfHouseholdTest` (residencyDuration = allYear); qrRelationshipTest excludes childOfStepSibling, otherDescendantOf*Sibling, fosterParent, noneOfTheAbove | AGREE | Same split between relatives who need not live with you and the all-year household member; both exclude grandnieces and a stepsibling's child from the first group. |
| 16 | `dependent.relationship` enum value `parent` ("father or mother") | `fosterParent` is a distinct `/relationshipOptions` value and fails `qrRelationshipTest` (must live with the filer all year) | DIFFER | The project's enum has no value that routes a foster parent to the all-year test. See Finding F2. |
| 17 | `dependent.qr_income` = gross_income < `qr.gross_income_limit` ($5,200) | `../grossIncomeTest` (writable, "less than `/grossIncomeLimit`" = 5050) | AGREE | Year change in the amount only: "less than $5,050 in 2024" (2024 p. 19) → "less than $5,200 in 2025" (2025 p. 19). |
| 18 | `dependent.income_exception` gate (disabled ∧ income ≥ limit → refuse; sheltered workshop) | none; DF asks the gross income test and leaves the exception to the filer | PROJECT-NARROWER | |
| 19 | `dependent.qualifying_relative` requires `qualifying_child = false` ("not *your* qualifying child"); "qualifying child of any taxpayer" handled by the `other_claimant` refusal on `qualifying_child`, which `qualifying_relative` reads | `../notQualifyingChildTest` = ¬`../isQualifyingChildOfAnother`, where on the QR path a person is not a QC of another if the potential claimer is not required to file and either does not file or files only for a refund (`../qcOfAnotherButNot`) | PROJECT-NARROWER | DF encodes Step 4's "a person isn't a taxpayer if …" exception; the project refuses instead. |
| 20 | `dependent.supported = true` (QR support) | `../qrSupportTest` = F if ownSupport else writable "you provided more than half" | AGREE | DF forces the QR support test false when the person provided over half of their own support; implied by the project's two inputs. |
| 21 | refusal `when: dependent.multiple_support` | none (`eligibleDependent`: "TODO: This does not account for MSAs") | NOT-IN-DF | DF never offers the Form 2120 path; a filer in an MSA who answers the support question honestly loses the dependent. |
| 22 | `dependent.under_ctc_age` (age < 17) | `../eligibleCtc`: `(../age < 17)` | AGREE | |
| 23 | `dependent.ctc_child`: qc_dependent ∧ tin ∧ citizen ∧ under 17 ∧ `dependent.work_ssn` | `../eligibleCtc` = isClaimedDependent ∧ qualifyingChild ∧ age < 17 ∧ `../citizenOrUsResidentTest` (no Canada/Mexico) ∧ tinType = ssn ∧ `../ssnValidForEmployment` (card marked neither, or "valid only with DHS authorization" in effect) | AGREE | The child-side conditions match, including the DHS-authorization card. |
| 24 | `dependent.ctc_child` requires `household.ctc_ssn` (a filer with an SSN valid for employment; other spouse SSN or ITIN) — see row 41 | none: `ctcOdc:/ctcQualified` = ¬improper-claims ban ∧ maybeEligibleForCtc; no filer-SSN fact | DIFFER | Year change; quoted under row 41. |
| 25 | `dependent.tin`, `dependent.work_ssn`, `person.tin`, `person.work_ssn`: "issued on or before the due date of your return (including extensions)" | none; DF reads the TIN type and the card legend only | NOT-IN-DF | |
| 26 | `dependent.odc_person` = claimed ∧ tin ∧ citizen ∧ ¬ctc_child ∧ `household.all_tin` | `../eligibleOdc` = isClaimedDependent ∧ ¬eligibleCtc ∧ citizenOrUsResidentTest (TIN via eligibleDependent) | AGREE | The filer SSN/ITIN condition (`household.all_tin`) has no DF fact: DF filers necessarily have a TIN (row 43). |
| 27 | `dependent.hoh_test2`: (claimed ∧ lived_half ∧ relationship ∉ {household_member, sibling_descendant, other}) ∨ (qualifying_child ∧ ¬married ∧ lived_half); home cost on `household.test2_met` | `../hohQualifyingPerson`: QC branch = qualifyingChild ∧ tpPaidMostOfHomeUpkeep ∧ (¬isQualifyingChildOfAnother ∨ isClaimedDependent) ∧ (¬married ∨ eligibleDependentMinusFilerInformation ∨ eligibleDependent ∨ benefit split ∧ ¬married); QR branch = qualifyingRelative ∧ (eligibleDependent ∨ benefit split) ∧ qrRelationshipTest ∧ residencyTest ∧ tpPaidMostOfHomeUpkeep; all under (¬`filingStatus:/eligibleForMFJ` ∨ `marriedHohRelationshipTest`) ∧ isClaimedIfClaimable | AGREE | Test 2 items 1 (with exclusion b: DF's `qrRelationshipTest` is exactly "not a dependent only because the person lived with you all year") and 2 match. DF also covers item 3 (married QC who is not a dependent only because the filer is a dependent) and item 4 (divorced rule); the project refuses those (rows 9, 13). DF's `isClaimedIfClaimable` is a DF policy (row 30). |
| 28 | `dependent.hoh_test1` = relationship = parent ∧ claimed ∧ `dependent.parent_home_paid` | parent branch: qualifyingRelative ∧ eligibleDependent ∧ relationship = parent ∧ residencyDuration = lessThanSixMonths ∧ `../tpPaidMostOfParentHomeUpkeep` | AGREE | DF routes a parent who lived with the filer more than half the year through the QR branch; the project applies Test 1 regardless ("Your parent didn't have to live with you", 2025 p. 14). Same outcome. Both exclude the MSA parent (project by refusal). |
| 29 | `dependent.eic_child` = qc_relationship ∧ qc_age ∧ ¬joint_return ∧ us_half | `../eitcRelAgeResJointTest` = qcRelationshipTest ∧ ageTest ∧ `../livedWithTpInUsMostOfYear` ∧ jointReturnTest | AGREE | Same four tests; no support test on either side. |
| 30 | (no project condition) | `../eitcQualifyingChild` also requires `../isClaimedIfClaimable` ("a claimable dependent must be claimed to act as a QP … for HOH, QSS, EITC, or CDCC", per a cited decision record) | DF-NARROWER | The text imposes no such rule (HoH Test 2 item 2 expressly allows "Your unmarried qualifying child who isn't your dependent", 2025 p. 14). DF computes a smaller EITC/denies HoH when a claimable child is left unclaimed. |
| 31 | `dependent.eic_child` refusals `when: dependent.other_claimant`, `when: dependent.married` | `Any(¬isQualifyingChildOfAnother, isClaimedDependent)`, `Any(¬married, isClaimedDependent)`, `¬disqualifiedDueToParentalCustody` | PROJECT-NARROWER | DF treats "claimed as dependent" as settling both the tie-breaker and the married-child rule ("Married child … is a qualifying child only if (a) you can claim the child as your dependent", 2025 p. 44); the project refuses. |
| 32 | `dependent.us_half` (lived with you in the US more than half of 2025) | `../livedWithTpInUsMostOfYear` = residencyTest ∧ monthsLivedWithTPInUS ∈ {six ("more than 6 months but less than 7"), seven, …, twelve} | AGREE | |
| 33 | `dependent.eic_ssn` (any SSA number unless "Not Valid for Employment" and issued solely for a federally funded benefit; DHS card only while valid) | `../ssnValidForEITCCalculation` = tinType = ssn ∧ (neither ∨ validOnlyWithDhsAuthorizationInEffect ∨ (notValid ∧ ¬ssnOnlyForFederallyFundedBenefit)) | AGREE | Identical logic. |
| 34 | `dependent.eic_ssn_child` = eic_child ∧ eic_ssn | `../eitcQualifyingChildForCalculation` = eitcQualifyingChild ∧ ssnValidForEITCCalculation | AGREE | |
| 35 | `dependent.dc_child_all_year`, `dc_age13` + `dc_under13`, `dc_disabled_qp`, `dc_qp` (care ∧ claimed ∧ …) | `../cdccQualifyingPerson`: (qualifyingChild ∧ isClaimedDependent ∧ (age < 13 ∨ `../cdccTurnedThirteenAfterJanFirst` [age = 13 ∧ not born Jan 1])) ∨ (residencyTest ∧ isClaimedDependent ∧ unableToCareForSelf) ∨ `../cdccNonDependentQualifyingPerson` | AGREE | The two dependent branches match; DF handles the child who turned 13 by excluding later expenses in screen text, the project by the `dc_under13` question. |
| 36 | `dependent.dc_qp` requires `dependent.claimed`; non-dependent qualifying persons refused by `f2441.nondependent_gate` | `../cdccNonDependentQualifyingPerson` (benefit-split child; would-be dependent except gross income / joint return / filer is a dependent: ¬eligibleDependent ∧ unableToCareForSelf ∧ citizenOrResidentTest ∧ residencyTest ∧ tinType ≠ none ∧ (QC tests ∨ QR tests without gross income)) | PROJECT-NARROWER | |
| 37 | `dependent.dc_line2c` (dc_qp ∧ age ≥ 13 ∧ dc_incapable) | `../unableToCareForSelfAndOverAge12` = unableToCareForSelf ∧ age ≥ 13 | AGREE | |

### household.yaml

| # | Project line(s) | Direct File fact(s) | Class | Note |
|---|---|---|---|---|
| 38 | `household.home_cost` (paid over half the cost of keeping up your home) | `../tpPaidMostOfHomeUpkeep` (writable per person: "did you pay more than half of the cost of keeping up the home you lived in with {name}") | AGREE | DF asks per person, the project once; the home is the filer's. |
| 39 | `household.unmarried` (input: "unmarried, or considered unmarried under the head of household rules") | `filers:/filerCouldQualifyForHoh` = ¬`filingStatus:/eligibleForMFJ` ∨ (eligibleForMFJ ∧ `filers:/livedApartLastSixMonths`); for an MFJ-eligible filer `../hohQualifyingPerson` also requires `../marriedHohRelationshipTest` (biological/adopted/step/foster child); `eligibleForHoh` also requires ¬`/eligibleForQss` | DIFFER | DF decomposes "considered unmarried" (lived apart last 6 months; the qualifying person is your child, stepchild or foster child who is your dependent); the project asks one composite question. Checked below: project reading supported; outcome-equivalent. |
| 40 | `household.test1_met`, `test2_met` (home_cost ∧ any Test 2 person), `hoh_eligible`, `hoh_fails` | `filingStatus:/eligibleForHoh` = Count(hohQualifyingPerson) > 0 ∧ filerCouldQualifyForHoh ∧ ¬eligibleForQss; `/isFilingStatusValid` | AGREE | Same "any qualifying person ∧ filer-level condition" shape. DF withholds HoH from a QSS-eligible widow(er) (a UX choice; the text allows either). |
| 41 | `household.work_ssn_count`, `any_work_ssn`, `id_count`, `ctc_ssn`, `taxpayer_work_ssn` (CTC: a filer with an SSN valid for employment; other spouse SSN or ITIN) | none for the CTC; `ctcOdc:/ctcQualified` has no filer-SSN term | DIFFER | **Year change** (quoted below). |
| 42 | `household.all_work_ssn` = every filer has `person.work_ssn` ("SSN valid for employment"), used by `eic.step1_ssn` | `filers:/filersHaveValidSSNsForEitc` (both filers if MFJ) with `filers/*/ssnValidForEitc` = tin is SSN ∧ (¬needsSSNWorkStatus [US citizen all year] ∨ card "valid only with DHS authorization" ∨ "neither" ∨ (notValid ∧ ¬ssnOnlyForFederallyFundedBenefit)) | DIFFER | DF gives the filer the same "Not Valid for Employment unless issued solely for a benefit" rule the project gives the child (row 33); the project's filer input is the narrower "valid for employment". See Finding F3. |
| 43 | `household.tin_count`, `all_tin` (ODC: every filer has an SSN or ITIN, or applied for an ITIN by the due date) | none; a DF filer has a TIN by construction (`/filers/*/tin` writable, required to file) | NOT-IN-DF | |
| 44 | `household.roster_ok` / `roster_bad` | none (DF has fixed primary/secondary filer slots) | NOT-IN-DF | Structural. |

### eic.yaml (Steps 1 to 4; worksheet joins)

| # | Project line(s) | Direct File fact(s) | Class | Note |
|---|---|---|---|---|
| 45 | `eic.qc_of_another` (input with the "not required to file, not filing, or refund only → No" gloss) | `eitc:/eitcQcTest` = ¬eitcQcOfAnother ∨ (eitcQcOfAnother ∧ ¬requiredToFile ∧ (¬isFiling ∨ refund only)) | AGREE | |
| 46 | `eic.age_range` (any person born after 12/31/1960 and before 1/2/2001) | `eitc:/filersAgeTestForEitcWithNoQC`: MFJ either filer, else primary; `filers/*/age25OrOlderForEitc` = day-before age ≥ 25; `age64OrYoungerForEitc` = age ≤ 64 | AGREE | DF's two age conventions reproduce the text's dates exactly: for 2024, born on Jan 1, 2000 → day-before age 25 (text: "before January 2, 2000"); born on Jan 1, 1960 → age 64 (text: "after December 31, 1959"). DF also handles a spouse who died in the year (`/secondaryFilerAgeDayBeforeDeath`, `/secondaryFilerAgeDayOfDeath`); the project has no such rule (text: "If your spouse died in 2025 … see Pub. 596 before you answer", 2025 pp. 41–42; Pub. 596 is not in `sources/`). Noted, not a finding. |
| 47 | `eic.us_home` (main home in the US more than half the year) | none; `filers/*/daysMainHomeInUS` = "365" ("Assumed … because taxpayers assert that they live in the state where their income was sourced all year") | NOT-IN-DF | |
| 48 | `eic.married`, `eic.married_rules` (mfs ∨ (hoh ∧ married)) | `eitc:/noEitcDueToSeparateFilingFromSpouse` = `filers:/isMarried` ∧ ¬MFJ ∧ (¬specialRuleForSeparatedSpouses ∨ no QC); `maybeEligibleForEitcWithoutQc` requires MFJ ∨ ¬isMarried | AGREE | |
| 49 | `eic.same_home`, `eic.legally_separated`, `eic.step3_married` (¬married_rules ∨ ¬same_home ∨ legally_separated) | `filers:/specialRuleForSeparatedSpouses` = livedApartLastSixMonths ∨ `/separationAgreement` ("living apart from their spouse and had a separation agreement on the last day of the year") | AGREE | |
| 50 | `eic.step3` = mfj ∨ (step3_married ∧ ¬qc_of_another) | `maybeEligibleForEitc` ∧ `eitcQcTest` with `maybeEligibleForEitcWithQc` = numEitcQualifyingChildren > 0 | AGREE | |
| 51 | `eic.step4` = ¬married_rules ∧ age_range ∧ us_home ∧ (mfj ∨ (¬qc_of_another ∧ ¬sa.dependent)); refuses `sa.dependent` | `maybeEligibleForEitcWithoutQc` = no QC ∧ (MFJ ∨ ¬isMarried) ∧ ¬`filers:/treatFilersAsDependents` ∧ age test; ∧ eitcQcTest | AGREE | Main home: row 47. DF computes "no EITC" for a dependent filer without a child and allows EITC with a child; the project refuses the return (row 13). |
| 52 | `eic.step1_income` (line 11b < limit by valid-SSN children and MFJ), `eic.limit*`, `eic.below_top` | `eitc:/belowEitcAgiLimit` = agi < `/eitcCompletedPhaseoutAmount` keyed on `familyAndHousehold:/numEitcDependentsCollectionForCalculation` (valid-SSN children) and MFJ | AGREE | Amounts are TY2024 in DF (e.g. 59,899 / 66,819) and TY2025 in the project; same keying. |
| 53 | `eic.step1_foreign` (Form 2555 → refuse) | none (foreign earned income out of DF scope) | NOT-IN-DF | Both refuse. |
| 54 | `eic.step1_resident` (nonresident alien → refuse via `scope.other_income`) | `filers:/filersUSCitizenOrRAAllYear` inside `filersCouldQualifyForEitc`; `/primaryFilerResidencyKnockout` | AGREE | Both refuse / knock out. |
| 55 | `eic.investment_income` (2a + 2b + 3b + max(7a, 0)), `eic.step2_income` (≤ $11,950) | `eitc:/belowEitcInvestmentIncomeLimit` = taxExemptInterest + interestIncome + ordinaryDividends + max(capitalGainsOrLosses, 0) ≤ 11600 | AGREE | Same four components; year change in the amount ("more than $11,600", 2024 p. 38; "more than $11,950", 2025 p. 40). |
| 56 | `eic.step2_other` (Schedule E, personal-property rental, Form 8814, passive activity → refuse) | none (out of DF scope) | NOT-IN-DF | Both refuse. |
| 57 | `eic.qc_count`, `eic.has_qc`, `eic.ssn_count`, `eic.step34` (Step 3 if any QC, else Step 4; the valid-SSN count drives the limits) | `familyAndHousehold:/numEitcQualifyingChildren` (eligibility) vs `/numEitcDependentsCollectionForCalculation` (amount); `maybeEligibleForEitcWithQc` tests the former | AGREE | Same two-tier structure; neither applies the Step 4 age test to a filer whose only QCs lack SSNs. |
| 58 | `eic.step5_income`, `eic.earned_for_limit` (earned income < the same limit) | `eitc:/belowEitcEarnedIncomeLimit` = employerIncomeSubtotal < eitcCompletedPhaseoutAmount (tested without combat pay) | AGREE | |
| 59 | `eic.separated_box` (married filer not MFJ who passes Step 3 q4–5 and answers No to q6) | `eitc:/receivingEitcWhileSeparatedCheckbox` = isMarried ∧ ¬MFJ ∧ isReceivingEitc | AGREE | The 2025 text adds "Check the box in the Dependents section that discusses the special rule for separated spouses" at Step 3 q6 (2025 p. 41); 2024 had "Skip Step 4; go to Step 5" only. DF's TY2024 fact sets the MeF indicator by the same condition. |
| 60 | `eic.self_employed`, Worksheet B lines, `eic.clergy` (refused) | none (Schedule C/SE out of DF scope) | NOT-IN-DF | |
| 61 | (no project line) — Form 8862 / prior disallowance; also `s8812.yaml` | `eitc:/eitcNoticeTest`, `/eitc8862Required`, `/eitcHadImproperClaims`, `/eitcReceivedImproperClaimsNotice` (2 or 10 years); `ctcOdc:/ctcOdcDisqualifiedForImproperClaims`, `/ctc8862Required` | DIFFER | DF asks whether the EIC or CTC/ACTC/ODC was previously reduced or disallowed, denies the credit during a 2- or 10-year ban and attaches Form 8862 otherwise. The project has no input, gate or refusal for this (grep of `forms/2025/*.yaml` for 8862/disallowed: none). See Finding F4. |

### s8812.yaml

| # | Project line(s) | Direct File fact(s) | Class | Note |
|---|---|---|---|---|
| 62 | `s8812.line4` = count of `dependent.ctc_child` | `ctcOdc:/ctcEligibleDependents` = Count(`/familyAndHousehold/*/eligibleCtc`) | AGREE | Predicate compared at rows 22–25, 41. |
| 63 | `s8812.line6` = count of `dependent.odc_person` | `ctcOdc:/odcEligibleDependents` = Count(`/familyAndHousehold/*/eligibleOdc`) | AGREE | Row 26. Per-child amounts (DF 2,000; project 2,200) are a year change, not a predicate. |

### sa.yaml

| # | Project line(s) | Direct File fact(s) | Class | Note |
|---|---|---|---|---|
| 65 | `sa.dependent` → `sa.standard` refuses (dependent filer; dual-status alien) | `standardDeduction:/standardDeduction` = `filers:/treatFilersAsDependents` ? min(`/minimumStandardDeduction` [max(1300, earned + 450) + additional], normal) : normal; dual-status: `/primaryFilerResidencyKnockout` | PROJECT-NARROWER | DF computes the Standard Deduction Worksheet for Dependents (2024 constants 1,300 / 450; 2025 text 1,350 / 450). Dual-status: both refuse. |
| 66 | `sa.boxes_age65` (`person.age65` = born before Jan 2, 1961; excluding `person.died_before_65`) | `filers/*/age65OrOlder` = day-before age ≥ 65 ("You are considered age 65 at the end of the year if your 65th birthday is on or before January 1 of the following year"); `/MFJDeceasedSpouseReachedAge65ForStandardD` = day-before age at death ≥ 65 | AGREE | Same January 1 boundary (2024: "born before January 2, 1960", p. 33; 2025: "before January 2, 1961", p. 34). DF applies the death rule to the deceased spouse only; the project to any person. |
| 67 | `sa.boxes_blind` (`person.blind` over the roster) | `filers/*/isBlind`; secondary counted when MFJ or the MFS spouse rule applies (`/isSpouseInfoApplicableForStandardDeductions`) | AGREE | |
| 68 | `sa.extra` = `sa.standard_extra` by status (2,000 single/HoH; 1,600 MFJ/MFS/QSS) | `/additionalStandardDeductionMultiplier`: 1950 single/HoH; 1550 MFJ/QSS/MFS | AGREE | Same status split; year change in amounts ("$1,550 ($1,950 if single or head of household)", 2024 p. 34; "$1,600 ($2,000 if single or head of household)", 2025 p. 35). |
| 69 | `sa.mfs_spouse_extra` gate → refuse (MFS claiming the spouse's age/blindness boxes) | `/filerMFSAndSpouseIsEligibleForStandardDeductions` = treatAsMFS ∧ ¬`filers:/MFSSpouseProvidesNoBenefits` (spouse filing a return, or has gross income, or can be claimed as a dependent) | PROJECT-NARROWER | DF's three conditions are the text's ("spouse had no income, isn't filing a return, and can't be claimed as a dependent", 2025 p. 33). |
| 70 | `sa.mfs_spouse_itemizes` → `sa.standard` = 0 and `sa.itemizes` forced | `filers:/spouseItemizesKnockout` = spouseItemizes ∧ MFSSpouseFilingReturnDerived (knockout) | DF-NARROWER | The project follows the text ("your standard deduction is zero", 2025 p. 34); DF refuses the return. |
| 71 | `sa.standardbase` by status (QSS = MFJ amount) | `/filingStatusStandardDeduction` (QSS → MFJ amount) | AGREE | Year amounts. |
| 72 | `sa.dependent` dual-status alien → refuse | `/primaryFilerResidencyKnockout` | AGREE | Both refuse. |

(Row 64 was merged into row 61; the numbering is kept so cross-references hold.)

### Counts

| Class | Rows |
|---|---|
| AGREE | 41 |
| DIFFER | 7 (rows 12, 14, 16, 39, 41 [with 24], 42, 61) |
| DF-NARROWER | 3 (rows 3, 30, 70) |
| PROJECT-NARROWER | 11 (rows 6, 8, 9, 10, 13, 18, 19, 31, 36, 65, 69) |
| NOT-IN-DF | 8 (rows 21, 25, 43, 44, 47, 53, 56, 60) |
| Total | 70 |

## The DIFFER rows against the 2024 and 2025 texts

**Row 41 (with 24) — filer SSN for the child tax credit.** *Year change.*
2024, p. 17, Before you begin: "If you want to claim the child tax credit or the credit for other dependents, you
(and your spouse if filing jointly) must have an SSN or ITIN issued on or before the due date of your 2024 return
(including extensions)." 2024, p. 18, Step 3 q4: "Did this child have an SSN valid for employment issued before the
due date of your 2024 return (including extensions)?"
2025, p. 17, Before you begin: "If you want to claim the child tax credit, you must have a valid SSN, which means it
must be valid for employment and issued before the due date of your return (including extensions). If you are
filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The
other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return
(including extensions)." 2025, p. 18, Step 3 q4: "Did you, or your spouse if filing a joint return, and this child
have SSNs valid for employment and issued before the due date of your 2025 return (including extensions)?"
Direct File's TY2024 logic has no filer-SSN term; the project's `household.ctc_ssn` is the 2025 rule. Not a
finding.

**Row 12 — a dependent with no TIN.** *Direct File reading supported; the project differs → Finding F1.*
2025, p. 22 (2024, p. 21, same words): "Social security number. You must enter each dependent's social security
number (SSN). … If your dependent child was born and died in 2025 and you do not have an SSN for the child, enter
'Died' on row (3) of the Dependents section and include a copy of the child's birth certificate, death certificate,
or hospital records." Step 3 q1 and Step 5 q2 make the TIN a condition of the credits only, but the sentence above
is a condition of listing the dependent, and the only carve-out it gives is the born-and-died child. The project
lists (and counts for HoH) a dependent for whom `dependent.tin` is false.

**Row 16 — foster parent as a qualifying relative.** *Direct File reading supported by Pub. 501; the 1040 text is
silent → Finding F2.* 2025 i1040gi, p. 19, Step 4: "Father, mother, or an ancestor or sibling of either of them (for
example, your grandmother, grandfather, aunt, or uncle)" (2024, p. 19, same). 2025 Pub. 501 (`p501.cols.txt` line
740), Relatives who don't have to live with you: "Your father, mother, grandparent, or other direct ancestor, but
not foster parent." Direct File's `fosterParent` value fails `qrRelationshipTest` and can only qualify through the
all-year household-member test; the project's `parent` ("father or mother") value does not say that a foster
parent belongs under `other`.

**Row 42 — the filer's SSN for the EIC.** *Direct File reading supported; the project differs → Finding F3.*
2025, p. 40, Step 1 q2 (2024, p. 38, same words): "Do you, and your spouse if filing a joint return, have a social
security number issued on or before the due date of your 2025 return (including extensions) that allows you to work
and is valid for EIC purposes (explained later under Definitions and Special Rules)?" 2025, p. 44, Social security
number (SSN) (2024, p. 42, same): "For the EIC, a valid SSN is a number issued by the Social Security
Administration unless 'Not Valid for Employment' is printed on the social security card and the number was issued
solely to allow the recipient of the SSN to apply for or receive a federally funded benefit." The definition the
question points to is the one the project applies to the child (`dependent.eic_ssn`); for the filer the project
reads `person.work_ssn` ("Do you have an SSN valid for employment …"), under which a card marked "Not Valid for
Employment" that was *not* issued solely for a benefit answers No. Direct File's `ssnValidForEitc` accepts that
card for the filer, as the definition does.

**Row 61 — Form 8862 and the 2-/10-year bans.** *Direct File reading supported; the project differs → Finding F4.*
2025, p. 43, Form 8862, who must file (2024, p. 40–41, same): "You must file Form 8862 if your EIC for a year after
1996 was reduced or disallowed for any reason other than a math or clerical error. … Also, don't file Form 8862 or
take the credit for the: • 2 years after the most recent tax year for which there was a final determination that
your EIC claim was due to reckless or intentional disregard of the EIC rules, or • 10 years after the most recent
tax year for which there was a final determination that your EIC claim was due to fraud." 2025 Schedule 8812
instructions (`i1040s8812.cols.txt` lines 32–34; 2024 lines 29–30 same): "If you erroneously claim the CTC, ACTC,
or ODC and it is later determined that your error was due to reckless or intentional disregard … you will not be
allowed to claim any of these credits for 2 years … fraud … 10 years. … If your CTC, ACTC, or ODC for a year after
2015 was denied or reduced for any reason other than a math or clerical error, you must attach Form 8862 to your tax
return to claim the CTC, ACTC, or ODC unless an exception applies."

**Row 39 — "considered unmarried" as one input.** *Project reading supported by the 2025 text; no finding.*
2025, p. 14: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either
Test 1 or Test 2 applies." Married persons who live apart (p. 15): "you are considered unmarried if all of the
following apply. • You lived apart from your spouse for the last 6 months of 2025. … • You file a separate return
from your spouse. • You paid over half the cost of keeping up your home for 2025. • Your home was the main home of
your child, stepchild, or foster child for more than half of 2025 … • You can claim this child as your dependent or
could claim the child except that the child's other parent can claim the child under the rule for Children of
divorced or separated parents". The project's `household.unmarried` asks exactly the composite the first sentence
names; Direct File asks the bullets as facts. Outcome check: a filer who truthfully answers "considered unmarried"
has a claimed child living in the home more than half the year (the fourth and fifth bullets) and paid over half
the cost (third), so `dependent.hoh_test2` and `household.test2_met` hold for that child; the divorced-rule variant
of the fifth bullet is refused. No reachable return where the two readings give different values was found. The
decomposition is still a candidate for the interview (item 2.5).

**Row 14 — the election not to claim.** *Undecidable as a rule.* The text describes the dependents as "those you
list"; it does not require listing every eligible person, nor forbid it. Direct File's `tpClaims` is a product
choice; the project's "every eligible person is claimed" is another. No finding.

## Findings

**F1 — `dependent.claimed` and the head-of-household tests do not require a taxpayer identification number.**
Lines: `dependent.qc_dependent`, `dependent.qr_dependent`, `dependent.claimed`, `dependent.hoh_test1`,
`dependent.hoh_test2` (forms/2025/dependent.yaml). Only `dependent.ctc_child`, `dependent.odc_person` and the
Form 2441 gate `dependent.dc_no_tin` read `dependent.tin`. A person with `dependent.tin = false` who passes Steps 1–2
or 4 is counted as a dependent on Form 1040 and can satisfy Test 1 or Test 2 for head of household. Text (2025
p. 22, 2024 p. 21): "You must enter each dependent's social security number (SSN)", with the single exception of a
child born and died in the year ("enter 'Died' … and include a copy of the child's birth certificate …"). Direct
File: `eligibleDependentMinusFilerInformation` requires `tinType ≠ none`; a head-of-household qualifying person
without a TIN is a knockout (`/knockoutHohQpHasNoTin`, screens `hoh-qp-no-tin`, `add-personhoh-qp-no-tin`); a child
born and died without a TIN is a knockout (`/knockoutPersonBornAndDiedInTaxYearWithoutTin`). Proposed handling: a
gate (refusal) on `dependent.claimed` when `dependent.tin` is false, with the born-and-died "Died" case named in the
remedy (the project already names it as outside the tool at `dependent.dc_count`); or a condition on
`qc_dependent`/`qr_dependent`. Effect today: a reachable return (dependent without TIN, HoH box checked) is
computed as HoH where the text requires an SSN entry it cannot have. Register or BUG entry.

**F2 — the relationship enum does not route a foster parent to the all-year test.** Line:
`dependent.relationship` (forms/2025/dependent.yaml), value `parent` ("father or mother"). Pub. 501 (2025, line 740
of `p501.cols.txt`): "Your father, mother, grandparent, or other direct ancestor, but not foster parent." A foster
parent is a qualifying relative only as "Any other person … who lived with you all year as a member of your
household"; a user entering `parent` for a foster parent passes `dependent.qr_relationship` with fewer than 12
months. The 1040 instructions (both years) do not state the exclusion. Direct File has `fosterParent` as its own
relationship value, excluded from `qrRelationshipTest`. Proposed handling: add "(not a foster parent; enter a foster
parent as `other`)" to the `parent` gloss, or a `foster_parent` value. Input-text ambiguity; register entry.

**F3 — the filer's SSN test for the EIC uses the employment-validity definition, not the EIC definition.** Lines:
`eic.step1_ssn` → `household.all_work_ssn` → `person.work_ssn` ("Do you have an SSN valid for employment, issued
before the due date …"; cite: Step 3 q4, the CTC rule). Text, 2025 p. 44 (2024 p. 42 same): "For the EIC, a valid
SSN is a number issued by the Social Security Administration unless 'Not Valid for Employment' is printed on the
social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a
federally funded benefit." A filer whose card says "Not Valid for Employment" but was not issued solely for a
federally funded benefit has a valid SSN for the EIC and answers `person.work_ssn` No, so the project gives no EIC
where the text allows it. The project applies the correct definition to the child (`dependent.eic_ssn`); Direct
File applies it to filers too (`filers/*/ssnValidForEitc`, with a US-citizen filer's SSN accepted without the card
question). Proposed handling: a `person.eic_ssn` input mirroring `dependent.eic_ssn`, read by `eic.step1_ssn`
(the CTC's `household.ctc_ssn` keeps `person.work_ssn`, whose definition is "valid for employment", 2025 p. 17).
Error on a reachable return by the Phase 1 stop rule, in a rare population. BUG entry.

**F4 — no input or refusal for a prior disallowance of the EIC or the CTC/ACTC/ODC (Form 8862; 2- and 10-year
bans).** Lines: none in `eic.yaml` or `s8812.yaml` (grep for 8862 / disallowed / reckless over `forms/2025/*.yaml`
finds nothing). Text: 2025 p. 43 (2024 pp. 40–41): "don't file Form 8862 or take the credit for the: • 2 years after
the most recent tax year for which there was a final determination that your EIC claim was due to reckless or
intentional disregard of the EIC rules, or • 10 years after … fraud"; and "You must file Form 8862 if your EIC for a
year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (with two exceptions).
2025 Schedule 8812 instructions lines 32–34 (2024 lines 29–30): the same bans for the CTC, ACTC and ODC, and "you
must attach Form 8862 … unless an exception applies". Direct File asks `eitcHadImproperClaims`,
`eitcReceivedImproperClaimsNotice` (twoYears / tenYears / zeroYears), `eitcImproperClaimsNoticeExpired`,
`eitcImproperClaimTakenSinceDisallowal`, and for the CTC `receivedImproperClaims`, `receivedImproperClaimsNotice`,
`improperClaimsNoticeExpired`, `hasFiledCtcOdcSinceNoticeExpired`; it zeroes the credits under an active ban and
attaches Form 8862 otherwise. A banned filer's return is reachable in the project and the credit is computed. Proposed
handling: one filer-level input ("Was your EIC, CTC, ACTC or ODC for a year after 1996 / 2015 reduced or disallowed
other than for a math or clerical error?") feeding a refusal on `eic.credit` and `s8812.line12` ("Form 8862 and the
disallowance period are outside this tool"). BUG entry (missing gate, computes where the text may forbid).

## Direct File knockouts whose situations the project computes

Knockout facts from `flow:/flowIsKnockedOut` and the `isKnockout` screens in the family, filing status, spouse,
deductions and credits flows, limited to the household subject matter. "Project" states how the project treats the
same return.

| Knockout (screen → fact) | DF condition | Project |
|---|---|---|
| `age-ko`, `spouse-age-ko` → `filers:/flowKnockoutFilerAgeYoungerThan16` | primary filer age < 16, or MFJ spouse age < 16 | Computes. No filer-age test anywhere (`person.yaml` asks birth-date boxes only). A return for a 15-year-old is reachable (possible Form 8615 exposure is not checked here). Candidate refusal. |
| `community-property-ko-go-back` (spouse and filing-status flows) → `filers:/knockoutSubjectToCommunityPropertyLaws` | lives in AZ, CA, ID, NM, NV, TX, WA or WI (`/livesInCommunityPropertyState`; the description notes it excludes the elective-community-property states) ∧ (married and eligible only for MFS, or MFS chosen, or HoH chosen while married) | Computes. No community-property fact except the Schedule C joint-venture question (`sc.yaml`). An MFS or married-HoH return in a community property state is reachable and its income is not split per state law (Pub. 555). Candidate refusal (strongest of the list). |
| (spouse flow) → `filers:/flowKnockoutHasApplicableRegisteredDomesticPartnership` | registered domestic partner in a community property state | Computes; not asked. Candidate refusal, same ground. |
| `mfs-spouse-itemizing-ko` → `filers:/spouseItemizesKnockout` | MFS ∧ spouse itemizes ∧ spouse files a return | Computes (`sa.mfs_spouse_itemizes`: standard deduction zero, itemizing forced). Project follows the text; no refusal needed. |
| `hoh-qp-no-tin`, `add-personhoh-qp-no-tin(-end)` → `familyAndHousehold:/knockoutHohQpHasNoTin` | filing HoH ∧ the chosen qualifying person has `tinType = none` | Computes HoH (Finding F1). |
| `add-person-born-died-no-tin` → `/knockoutPersonBornAndDiedInTaxYearWithoutTin` | a listed person born and died in the tax year with no TIN | Computes: the person is claimed (`claimed` needs no TIN), no CTC/ODC (both need `tin`); the "Died" entry and attachments are not produced. Named as outside the tool only in the Form 2441 remedy (`dependent.dc_count`). Candidate refusal (or part of F1). |
| `add-person-special-rule-applies-non-custodial` → `dependentsBenefitSplit:/knockedOutByNonCustodialParentBenefitSplit` | noncustodial parent whose child is released to them by Form 8332 | Refused (`dependent.divorced_rule`). Not a gap. |
| `add-person-special-rule-conflicting-information` → `/knockedOutByContradictory8832` | custodial/noncustodial answers contradict who signed Form 8332 | Refused (`dependent.divorced_rule`). Not a gap. |
| `about-you-citizen-resident-ko` → `filers:/primaryFilerResidencyKnockout` | primary filer not a citizen all year, not a citizen at year end, not a resident all year | Refused (`scope.other_income`, `sa.dependent` dual-status). Not a gap. |
| `earned-income-rule-ko-*` → `cdcc:/knockoutStudentOrDisabled` | Form 2441 earned-income rule for a student or disabled filer/spouse | Refused (`f2441.student_disabled`). Not a gap. |
| `net-investment-*-ko` → `interest:/hasInterestIncomeAndAgiAboveThresholdFor*` | interest income with AGI above the NIIT threshold | Computes Form 8960 (`f8960.yaml`). Out of this item's scope; not a gap. |
| `dep-tp-ko`, `dependents-filing-req-ko`, `allocations-ko`, … (credits flow) | premium tax credit situations (`ptc.xml`) | Out of scope (no PTC in the project). |

Not compared: qualifying surviving spouse eligibility (`familyAndHousehold:/qssQualifyingPerson`,
`filingStatus:/eligibleForQss`); the project has the `qss` status value but no eligibility predicate for it in the
five files (a gap to note for item 2.5, not a Direct File finding).

## Provenance

**Inspected:** the rendered derivation trees of every fact named above, from the XML in
`.direct-file/direct-file/backend/src/main/resources/tax/` at commit e365f9f (rendered by `/tmp/df/render.py`, a
script I wrote; the renderer prints `Dependency` paths, `Switch` cases and `All/Any/Not/Equal/…` nodes verbatim; one
leaf type, `Days()`, renders as a bare call); the `isKnockout` screen definitions and their `condition` attributes in
the five flow `.tsx` files; three option labels in `en.yaml`; the five project yaml files and `person.yaml`,
`f2441.yaml` lines 96–135, `params/2025.yaml` (the age, gross-income and standard-deduction parameters); the 2024 and
2025 `i1040gi.cols.txt` passages for Head of Household, Who Qualifies as Your Dependent, EIC Steps 1–6 with
Definitions and Special Rules, and the Standard Deduction (read in full, both years); `i1040s8812.cols.txt` lines
29–34 (both years); `p501.cols.txt` line 740 (2025); `i2441.cols.txt` line 20 (2025). Grep over `forms/2025/*.yaml`
for 8862, disallowed, reckless, community property, QSS.

**Inferred (unverified):** (a) that Direct File's screen text for `residencyDuration`, `monthsLivedWithTPInUS` and
the dependents' "exception to time lived with you" matches the two option labels I read — the rest of the interview
copy was not read; (b) Direct File's *reasons* for its knockouts (filer under 16, community property, HoH QP without
TIN, born-and-died) come from fact descriptions and screen names, not from a stated rationale; (c) that
`isClaimedIfClaimable` is a policy rather than a legal reading rests on its description's citation of an internal
decision record, which I could not open; (d) `daysMainHomeInUS` "assumed to be 365" is the fact's description;
(e) the absence of multiple-support-agreement and sheltered-workshop handling in Direct File is inferred from the
`eligibleDependent` TODO and from finding no fact for either after reading `familyAndHousehold.xml` in full, not
from the flow; (f) the project's refusal propagation (that `other_claimant` refusing `qualifying_child` also refuses
`qualifying_relative`, which reads it) is taken from the plan's statement of the evaluation-order semantics
(item 1.6), not re-read in `engine/`; (g) the "outcome-equivalent" argument for row 39 is my reasoning over the
text, not a fixture run; (h) the deceased-spouse EIC age rule (row 46) is attributed to Pub. 596, which is not in
`sources/` and was not read; (i) the knockout fact's description names five states ("Arizona, California, Nevada, Texas, or Washinton") while
`/livesInCommunityPropertyState` tests eight (AZ, CA, ID, NM, NV, TX, WA, WI; Louisiana is absent, which may reflect
Direct File's participating-state list rather than the law) — the eight-state body is what was read; (j) the classification of F3 and F4 as
errors "on a reachable return" assumes no upstream gate in forms outside the five files refuses those filers; the
grep found none, but the full refusal graph was not traced.
