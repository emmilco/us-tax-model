# Adjudication of the completeness-review claims (2026-10-30)

This file rules on the 29 claims in `call1.out` (dependents, i1040gi pp. 17–22) and `call2.out` (EIC, pp. 40–48). Each
claim gets two verdicts:

- **Experiment tree** `ac69196`. The YAML was read with `git show ac69196:forms/2025/<form>.yaml`.
- **Current tree** `HEAD` (`2ca3311`). The YAML was read in place. Witness returns were evaluated with
  `node engine/dist/main.js eval --inputs … --json`.

The witness inputs are copies of committed fixtures with one to three inputs changed. They are kept in
`/tmp/adj-completeness/w/` and were not committed. The text of `sources/2025/i1040gi.cols.txt` is the same on both trees.

## Standard applied

- **Real gap.** A source rule that changes eligibility, an amount or an entry, and that no line implements, no question
  asks and no gate refuses. This includes a question that uses a defined term of art without the operative part of its
  definition, when a filer answering in good faith would plausibly answer wrongly and the result would change. The
  project already holds questions to this standard: BUG-0023, BUG-0027 and BUG-0028 were definition omissions, and
  `person.sav_student` spells out the full-time-student definition. These are marked *(definitional)*. Precision is
  also reported without them.
- **Covered.** The rule is in the YAML, checked in the expression or gate, not in the label.
- **Out of scope.** The rule is refused by a named gate, recorded as a design limit, or is an attachment the tool does
  not produce.
- **Presentation only.** The rule concerns a printed box or row that the tool does not produce. It changes no amount.
- **Wrong.** The model misread the source or the encoding.

## 1. Verdicts

### Call 1: dependents (13 claims)

| # | Claim | Experiment tree `ac69196` | Now (`HEAD`) |
|---|---|---|---|
| 1 | Kidnapped child | **Real gap.** p. 21, "If your child is presumed by law enforcement authorities to have been kidnapped by someone who isn't a family member, you may be able to take the child into account…". Nothing in `forms/` mentions kidnapping. `dependent.months` lists only school, vacation, business, medical care, military service and juvenile detention. Changes residency for the CTC, EIC and head of household. | **Still live.** `git grep -i kidnap HEAD -- forms/` finds nothing. Witness (from `stage13.ctc_spouse_no_id`, spouse ITIN issued, child `months`=4): line 19 is $500 (credit for other dependents, ODC) instead of $2,200 (child tax credit, CTC). Witness (from `stage9.eic.one_child.at_line5_amount`, `months`=4, `us_half`=No): line 27a is $0 instead of $4,324. See D3. |
| 2 | TANF used as support | **Real gap** *(definitional; a pointer)*. p. 21 points to Pub. 501. Pub. 501 (archived, `p501.cols.txt` l. 379) says TANF payments "used … to support another person … are considered support you provided". `dependent.supported` asks only "Did you provide over half of this person's support". A filer who counts TANF as government support answers No and loses a qualifying relative. | **Still live**, unchanged. Low severity (D7). |
| 3 | Full-time student definition | **Real gap** *(definitional)*. p. 21 defines a full-time student as 5 calendar months, including on-farm courses and excluding on-the-job training, correspondence and Internet-only schools. `dependent.student` asks only "Was this person a full-time student in 2025?". | **Still live**, unchanged. Witness (stage9 one-child case, child aged 20): `student`=Yes gives line 27a $4,324; No gives $0. An Internet-only student answering Yes is wrongly counted. See D2. |
| 4 | Foster child definition | **Real gap** *(definitional)*. p. 21, "A foster child is any child placed with you by an authorized placement agency or by judgment, decree, or other order…". The gloss on `dependent.relationship` says only "foster child". | **Still live**, unchanged. An informally taken-in child entered as `child` gets the qualifying-child path. The witness is the reverse of D1: $4,324 EIC instead of $0, and a CTC instead of an ODC. See D4. |
| 5 | Adopted or placed-for-adoption child | **Real gap**, narrower than claimed. p. 20, "An adopted child is always treated as your own child. An adopted child includes a child lawfully placed with you for legal adoption." A finalized adoptee is plausibly a "son, daughter". A child placed but not yet adopted fits no gloss of `child` and fits `other` literally. | **Still live.** The gloss is unchanged; only "(not a foster parent…)" was added to `parent`. The interview prompt is the `source` text, and its help is generic (`interview/questions-2025.yaml` l. 452). Witnesses: `relationship`=`other` gives line 19 $500 instead of $2,200 (the stage13 case, `lawful`=Yes), and line 27a $0 instead of $4,324 with head of household refused through `household.hoh_fails` (the stage9 case). See D1. |
| 6 | Child's SSN "Valid for Work Only With DHS Authorization" | **Real gap** *(definitional)*. p. 22, "your child has the required SSN only as long as the DHS authorization is valid". `dependent.work_ssn` omits it. `dependent.eic_ssn` has it, but only for the EIC. | **Still live**, unchanged. A Yes answer with lapsed authorization gives line 19 $2,200; the correct No gives $500. Rare. See D6. |
| 7 | A child who was a citizen when the SSN was received | **Covered.** `dependent.work_ssn` asks whether the SSN is "valid for employment". The sentence only confirms that a citizen's SSN is. The model's failure case, a citizen child whose card carries a restrictive legend, is not a case the sentence creates. | Not applicable (unchanged; still covered). |
| 8 | Pending ITIN of the other spouse, for the CTC | **Real gap**, contested. p. 22, "If you apply for an ITIN on or before the due date … and the IRS issues you an ITIN as a result of the application, the IRS will consider your ITIN as issued on or before the due date of your return." `household.id_count` reads `person.work_ssn` or `person.tin` but not `person.itin_applied`. That choice was deliberate: BUG-0049 fixed it to "the child tax credit's other-spouse test only the first". The BUG-0049 entry does not mention the deeming sentence. | **Still live** (`household.yaml` l. 351–372). Witness (stage13 `ctc_spouse_no_id`, spouse `itin_applied`=Yes): line 19 $500. With the ITIN treated as issued: $2,200. See D5. Needs the owner's ruling against BUG-0049. |
| 9 | A child born and died in 2025 without an SSN ("Died", born-alive document) | **Real gap.** The sentence is the exception named in BUG-0095. At `ac69196`, `dependent.claimed` and the head-of-household tests never read `dependent.tin`, so a dependent with no TIN was claimed silently. | **Fixed, BUG-0095** (`a65e6af`). `dependent.claimed_no_tin` refuses, and the remedy names the "Died" case. Witness: `dependent.tin`=No gives `household.hoh_eligible` the refusal `claimed_no_tin`. |
| 10 | Enter each dependent's SSN and match the card | **Presentation only, as argued.** The claim is that no item captures the name or number or checks them against the card, and the model rated it "mainly presentation". Matching the card is the IRS's processing step. The quoted first sentence, "You must enter each dependent's SSN", does govern BUG-0095, but the claim says the existence of a number is covered. | **Fixed, BUG-0095** (for the governing sentence). Capturing the name and number is still not done; that is presentation. |
| 11 | Revoked release: attach the revocation | **Out of scope.** An attachment the tool does not produce. A custodial parent who answers `divorced_rule` Yes is refused; one who answers No gets the correct amounts and lacks only the attachment. | Not applicable. |
| 12 | More than four dependents: box and statement | **Presentation only.** The tool produces no Dependents-section rows. The only box it produces there is `f1040.separated_spouses`. | Not applicable. |
| 13 | Dependents-section rows (5)–(7) boxes | **Presentation only.** The facts exist (`student`, `disabled`, `lived_half`, `ctc_child`, `odc_person`), but no line prints the rows. | Not applicable. |

### Call 2: EIC (16 claims)

| # | Claim | Experiment tree `ac69196` | Now (`HEAD`) |
|---|---|---|---|
| 1 | 2- and 10-year bans | **Real gap.** No input or gate exists. `git grep 8862 ac69196 -- forms/` finds nothing. | **Fixed, BUG-0097** (`a65e6af`). `household.credit_disallowed` refuses `eic.credit` (eic.yaml l. 1586) and Schedule 8812 (s8812.yaml l. 252). |
| 2 | Form 8862 after a disallowance | **Real gap**, the same paragraph as claim 1. | **Fixed, BUG-0097.** |
| 3 | Worksheet B exclusions (statutory employee, notary, Forms 4029/4361, other SE-exempt amounts) | **Covered** by refusals outside the encoding the model was given. `sc.statutory` refuses statutory-employee and notary Schedule C income (sc.yaml l. 44, remedy l. 161). `person.se_screen` and `se_screened` refuse Forms 4361 and 4029 and "self-employment income exempt under an international social security agreement" (person.yaml l. 773–816). Statutory employees are also refused at `eic.step5_line1`. | Not applicable (unchanged). |
| 4 | Spouse's main home, Step 4 question 3 | **Real gap.** `eic.us_home` asked "Was your main home in the United States…". | **Fixed, BUG-0195.** The question now reads "and your spouse's if filing a joint return". |
| 5 | Joint filers skip Step 4 questions 5 and 6 | **Wrong.** `eic.step4` takes the `any` of `f1040.status = mfj` and (`qc_of_another` = No and `sa.dependent` = No), which is the bypass. The model saw only the label and flagged it "confirm in the code". A joint filer who can be claimed as a dependent is refused, but `sa.dependent` refuses the whole return anyway, through `sa.standard`/line 12e. | **Not applicable**; checked at HEAD, unchanged. Witnesses (`stage9.eic.joint.no_child.12000`): `qc_of_another`=Yes still gives line 27a $649. With `qc_of_another` removed from the inputs it still gives $649, so the question is never asked of joint filers. `sa.dependent`=Yes refuses line 12e as well as the EIC. |
| 6 | Death in 2025 and the age test (Pub. 596) | **Real gap.** Already recorded as **T-037** (open, Stage 13). `eic.age_range_count` reads birth dates only. | **Still live** and recorded (T-037). Pub. 596 is not archived, so the rule is stated from Pub. 596 as recalled, not checked: the age test is applied at death. Low severity (D8). |
| 7 | Full-time student (EIC) | **Real gap** *(definitional)*. The same input as call 1 claim 3. | **Still live** (D2). |
| 8 | Foster child (EIC) | **Real gap** *(definitional)*. The same as call 1 claim 4. | **Still live** (D4). |
| 9 | Child placed for adoption (EIC) | **Real gap.** The same as call 1 claim 5, p. 43. | **Still live** (D1). |
| 10 | Permanently and totally disabled definition | **Real gap** *(definitional, weak)*. pp. 21 and 44 require that the person "couldn't engage in any substantial gainful activity" and "a doctor has determined…". `dependent.disabled` uses the term without these. It removes the age limit. | **Still live**, unchanged. Low (D9). |
| 11 | Kidnapped child (EIC pointer) | **Real gap.** The same as call 1 claim 1. `dependent.us_half` omits it. | **Still live** (D3). |
| 12 | Filer's SSN: the DHS legend and "on or before" | **Real gap.** This is BUG-0096, which was not one of the reference bugs. `eic.step1_ssn` read `household.all_work_ssn` and so `person.work_ssn` ("valid for employment, issued before the due date"). That is the wrong definition: it omits the DHS condition and excludes an SSN issued on the due date. | **Fixed, BUG-0096** (`a65e6af`). `eic.step1_ssn` reads `household.all_eic_ssn` and so `person.eic_ssn`, with the DHS condition and "on or before". |
| 13 | Voluntary choice not to claim (line 27c) | **Out of scope:** a recorded design limit. The `eic.check_27c` label says "the filer's own choice not to claim the EIC is not asked", and T-027 records it. The model read the label correctly. | Not applicable (unchanged). Its sibling for line 28, BUG-0162, is now encoded as `f1040.line28_box`, "not asked". |
| 14 | Schedule EIC | **Out of scope:** an attachment the tool does not produce. | Not applicable. |
| 15 | Dependents-section boxes and the address-block box | **Presentation only.** The tool produces neither the rows nor the address-block box. | Not applicable. The address-block box is one more page-1 box to add before PDF filling (see note N2). |
| 16 | "EIC" written by line 27a (the IRS figures the credit) | **Presentation only.** This is an optional alternative; the tool computes the credit. | Not applicable. |

## 2. Precision

| | Call 1 | Call 2 | Overall |
|---|---|---|---|
| Claims | 13 | 16 | 29 |
| Real gaps (standard above) | 8 (1, 2, 3, 4, 5, 6, 8, 9) | 10 (1, 2, 4, 6, 7, 8, 9, 10, 11, 12) | **18 / 29 = 62%** |
| Counting claim 1.10 as a hit (its sentence governs BUG-0095) | 9 | 10 | 19 / 29 = 66% |
| Real gaps that affect a value or eligibility | 8 | 10 | **18 / 29 = 62%** (every real gap changed eligibility or an amount) |
| Real gaps, excluding *(definitional)* claims | 4 (1, 5, 8, 9) | 7 (1, 2, 4, 6, 9, 11, 12) | 11 / 29 = 38% |
| Wrong | 0 | 1 (5) | 1 |
| Covered | 1 (7) | 1 (3) | 2 |
| Out of scope or presentation only | 4 (10, 11, 12, 13) | 4 (13, 14, 15, 16) | 8 |

- **Distinct defects.** Four real gaps appear in both calls: student, foster, placed for adoption and kidnapping. That
  leaves **14 distinct real gaps**.
- **Already known.** Six of the 14 were already known by HEAD: BUG-0095, 0096, 0097 (the bans and Form 8862 counted
  as two), 0195 and T-037.
- **New candidates.** Eight are new: kidnapping, TANF, student, foster, placed for adoption, the child's DHS SSN, the
  ITIN deeming rule and the disability definition. The pressure-test document had already flagged the
  placed-for-adoption gap.
- **Self-rating.** The model's own split ("10 + 3" and "13 + 3") overstates the value-affecting count. Its
  presentation-only bins were accurate: all 6 of those claims are presentation or out of scope.
- **Why the errors happened.** Both non-gap misreadings came from reading labels instead of logic. Claim 2.5 was
  implemented in the expression but not stated in the label. The Worksheet B exclusions (2.3) were refused on forms the
  model was not shown.

## 3. Recall on the known bugs

| Bug | Claim(s) | Effect rating given | Would it lead an adjudicator to the defect? |
|---|---|---|---|
| BUG-0097 | EIC 1, 2 | "Eligibility and amount … allows a credit that is barred" | **Yes, directly.** One `grep 8862` confirms it. |
| BUG-0095 | Dependents 9; 10 | Claim 9: "Eligibility and presentation". Claim 10: "Mainly presentation". | **Probably, through claim 9 only.** Checking how a dependent with no SSN is treated leads to `dependent.claimed`, which never read `tin`. Claim 10's rating, and its premise that existence is covered, invite dismissal. |
| BUG-0195 | EIC 4 | "Eligibility for joint filers without a qualifying child" | **Yes, exactly.** The label and question are the defect. |

- **Recall on the reference set: 3 of 3.** BUG-0095 was found only through a weakly rated claim.
- **The wider post-tree set.** For defects recorded after `ac69196` in these two sections, the model found BUG-0096
  (EIC 12, rated "narrow") and T-037 (EIC 6). It missed **BUG-0192**, an `other` household member counted without the
  local-law condition (p. 19). At `ac69196` the gloss of `other` stated the condition, but no expression tested it. A
  label-only review cannot see a label that claims more than the logic does. So recall on completeness defects in these
  sections is 4 of 5.

## 4. Candidate live defects (proposed; nothing applied)

Severity is proposed, not ruled. All fixes add or reword an input, which makes the dependent and EIC reviews stale (the
BUG-0184 pattern).

### D1. A child placed for adoption has no relationship value (dependents 5, EIC 9). Medium.

- **Source.** p. 20 and p. 43: "An adopted child is always treated as your own child. An adopted child includes a child
  lawfully placed with you for legal adoption."
- **Current encoding.** `dependent.relationship`, value `child`: "child (son, daughter, stepchild, foster child or their
  descendant)". `other` reads "any other relationship". `qc_relationship` is true only for `child`, `sibling` and
  `sibling_descendant`.
- **Witnesses.**
  - The stage13 `ctc_spouse_no_id` case, with the spouse ITIN issued and `lawful`=Yes: line 19 is $2,200 as `child`
    and $500 as `other`.
  - The `stage9.eic.one_child.at_line5_amount` case: line 27a is $4,324 as `child` and $0 as `other`, and head of
    household is refused (`household.hoh_fails`).
- **Fix.** Make the gloss "child (son, daughter, including an adopted child or a child lawfully placed with you for
  legal adoption, stepchild, eligible foster child, or a descendant of any of them)". No expression changes.

### D2. Full-time student asked without its definition (dependents 3, EIC 7). Medium.

- **Source.** pp. 21 and 44: "during any part of 5 calendar months of 2025 was enrolled as a full-time student at a
  school or took a full-time, on-farm training course … It doesn't include an on-the-job training course,
  correspondence school, or school offering courses only through the Internet."
- **Current encoding.** `dependent.student`: "Was this person a full-time student in 2025?"
- **Witness.** The stage9 one-child case with the child aged 20: Yes gives line 27a $4,324, No gives $0. An
  Internet-only student aged 19–23 is common, and the same answer also drives the qualifying-child tests for the
  dependency and head of household.
- **Fix.** Put the definition into the question, as `person.sav_student` already does.

### D3. No kidnapped-child rule (dependents 1, EIC 11). Low.

- **Source.** p. 21, "Kidnapped child", cross-referenced on p. 43.
- **Current encoding.** The lists of absences in `dependent.months` and `dependent.us_half` omit it.
- **Witnesses.** `months`=4 gives line 19 $500 instead of $2,200, and line 27a $0 instead of $4,324. The source allows
  the child to be counted.
- **Fix.** A screen question that refuses, since Pub. 501's conditions are not encoded: "Is this child presumed by law
  enforcement to have been kidnapped by someone who isn't a family member?"

### D4. Foster child asked without the placement requirement (dependents 4, EIC 8). Low.

- **Source.** pp. 21 and 43: "placed with you by an authorized placement agency or by judgment, decree, or other order
  of any court of competent jurisdiction."
- **Current encoding.** The `child` gloss says "foster child".
- **Witness.** The D1 pair reversed: an informally placed child entered as `child` gets $4,324 EIC and the CTC.
- **Fix.** Make the gloss "eligible foster child (placed with you by an authorized placement agency or by court
  order)", and route others to `other`. This combines with D1.

### D5. CTC other-spouse test ignores the ITIN deeming sentence (dependents 8). Medium if the reading holds; contested.

- **Source.** p. 22: "If you apply for an ITIN on or before the due date … and the IRS issues you an ITIN as a result
  of the application, the IRS will consider your ITIN as issued on or before the due date of your return."
- **Current encoding.**
  - `household.id_count` counts people for whom `person.work_ssn` or `person.tin` is Yes.
  - `person.itin_applied` is read only by `household.tin_count`, which serves the ODC.
- **Witness.** The stage13 `ctc_spouse_no_id` case with the spouse's `itin_applied`=Yes: line 19 is $500. With
  `tin`=Yes it is $2,200.
- **Conflict with BUG-0049.** BUG-0049's fix chose the opposite reading without citing this sentence. The sentence
  follows the ODC sentence but is worded generally. The owner should rule, with an ambiguity entry if needed.
- **Fix, if ruled for.** Add `person.itin_applied` to the `any` in `household.id_count`.

### D6. A child's DHS-conditioned SSN (dependents 6). Low.

- **Source.** p. 22: "if 'Valid for Work Only With DHS Authorization' is printed on your child's social security card,
  your child has the required SSN only as long as the DHS authorization is valid."
- **Current encoding.** `dependent.work_ssn` omits the condition.
- **Effect.** $2,200 instead of $500 for that child.
- **Fix.** Add the sentence to the question, as `dependent.eic_ssn` already has it.

### D7. TANF counted as the filer's support (dependents 2). Low.

- **Source.** The p. 21 pointer, and Pub. 501 (l. 379): TANF "used … to support another person … are considered
  support you provided for that person."
- **Current encoding.** `dependent.supported` gives no guidance.
- **Effect.** Understated: a qualifying relative is lost, and with it the $500 ODC and possibly head of household.
- **Fix.** Add one sentence to the question.

### D8. The Pub. 596 death rule for the age test (EIC 6). Low; already T-037.

- **Recommendation.** Keep it under T-037. Its proposed screen and refusal is the minimal fix. Archive Pub. 596 first.

### D9. Permanently and totally disabled asked without its definition (EIC 10). Low.

- **Source.** pp. 21 and 44, the substantial gainful activity test and the doctor's determination.
- **Current encoding.** `dependent.disabled` uses the term only.
- **Effect.** Removes the age limit for the qualifying child, the EIC and head of household.
- **Fix.** Add the definition to the question.

### Notes

- **N1.** The BUG_INVENTORY entries for BUG-0095, 0096 and 0097 still read "Fix: open (owner's decision 2026-10-22)…",
  but `a65e6af` fixed all three. The inventory is stale (not edited here).
- **N2.** Before PDF filling, the tool will need these page-1 entries it does not produce: the Dependents rows, the
  more-than-four box, and the box to the right of the address block (pp. 41–42). They are presentation only.

## 5. Cost of adjudication

- **Measured.**
  - One agent session took about 9 minutes wall-clock (14:24–14:33), with about 45 tool calls and about 185k tokens of
    context read. That includes reading both trees' dependent, EIC, household and person YAML, the source pages and the
    inventory, plus 12 witness evaluations.
  - Per claim: about 20 seconds, about 1.5 tool calls and about 6.4k tokens.
  - The cost is front-loaded. About 60% went on reading the encoding and source once. After that, each claim took one
    or two greps or one evaluation. Duplicate claims across calls (4 of 29) cost almost nothing.
- **Estimated for a standing review (not measured).**
  - The model call (about 2 calls per section) is cheap next to adjudicating it.
  - Agent adjudication would cost about 6–7k tokens per claim with witnesses.
  - A human adjudicator, verifying each claim against the YAML and building a witness for each "still live", would plausibly
    take 5–10 minutes per claim, or about 3–5 hours for 29 claims.
  - The definitional class (7 of 18 real gaps) needs an owner standard first. Without one, every review will reopen
    the same question of whether a bare term of art counts as a gap.
