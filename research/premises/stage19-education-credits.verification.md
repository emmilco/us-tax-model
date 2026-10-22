> Adversarial verification of `stage19-education-credits.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 2 errors and 7 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification: research/premises/stage19-education-credits.md

Checked against the tree at 1c465c2 (Stage 15 landed) and `sources/2025/`. Read-only. Quote checks used a
normalising matcher over both text layers (`.cols.txt` and `.txt`), the same two layers `tools/citations.py`
accepts. The SOI cells were read with `.engines/venv/bin/python`.

## Errors

1. **Section 7, the MFS parameter note.** The claim: "give MFS the single amount (as `sli.base_other` does
   through its `choose`)". What the code does: `sli.line5`'s `choose` sends `mfs` to `sli.zero`. It does not send
   it to `sli.base_other` (`forms/2025/sli.yaml`, the `sli.line5` alternatives: single, hoh and qss go to
   `sli.base_other`, mfj to `sli.base_joint`, mfs to `sli.zero`). So the cited precedent points the other way. The
   status-keyed parameter precedent is `savers.agi_limit` (`params/2025.yaml`), which gives `mfs` a value of its
   own (3950000). Affects: the parameter design in section 7, which no numbered decision covers. Low impact,
   because MFS is refused either way.
2. **Section 4.10, Jane row: the scholarship variants offered as fixtures.** The claim: "four scholarship variants
   on the same page" are usable as fixtures. What the source says (p970 p. 16, Example 5): Jane is the filer and
   the student. In three of the four variants she "includes" $5,500, $3,500 or $1,500 of the scholarship in income.
   Under the map's own section 4.8 and D8, that amount goes to Schedule 1 line 8r (it is not in Form W-2 box 1),
   and `scope.schedule1` refuses line 8r unless Stage 16 brings it in. So only the "excludes the entire
   scholarship" variant is computable under the recommended D8. The row states the fixture supply more broadly than
   the recommended scope allows. Affects: D8, and the fixture plan behind D1.

No quote was found to be absent from its cited document and page. No number differed from its source.

## Out of date after Stage 15

1. **Header and section 1.** The claim: "spec 2.4 roadmap item 5". Now: `spec/spec.md` 2.4 lists "4. The education
   credits (88%)". At 6051ec0 it was "5. The education credits (89%)".
2. **Section 1.1, the roadmap step.** The claim: "step 5: 'Education credits (Form 8863) | 88.9% (+4.1) | +2.7'".
   Now: `reports/2025/filer_coverage.md` line 31 reads "| 4 | Education credits (Form 8863) | 88.1% (+4.1) | +3.0 |".
   In the json, `greedy_order[3].coverage_after` is 0.8809 and `gain_if_covered_alone.education` is 0.0304. These
   figures are unchanged: the share (4.5%, `share` 0.04490196447608361), the IRS count 7,211,349 and the microdata
   share 0.0053. The headline is now 64.7%.
3. **Section 5.2, `s3.line8` "Now" column.** The claim: "`sum(s3.line1, s3.zero)` here". Now: it is
   `sum(s3.line1, s3.line2, s3.line4, s3.line5a, s3.line5b, s3.zero)`. Its refusal form text is "Other credit forms
   (Schedule 3 lines 3 and 6a to 6z; Form 1040 lines 29 to 31)" (`forms/2025/s3.yaml`).
4. **Section 5.2, the `scope.ready` refusal "Now" text.** The claim: 'Other credit forms (Schedule 3 lines 2 to 4,
   5b, 6d, 6f, 6l and 6m; Form 1040 lines 29 to 31)'. Now: 'Other credit forms (Schedule 3 lines 3 and 6a to 6z;
   Form 1040 lines 29 to 31)' (`forms/2025/scope.yaml`). The same string, with the same remedy, sits on
   `f1040.line29`, `f1040.line30` and `s3.line8`. The remedy lists the supported credits ("... the child and
   dependent care credit, the saver's credit and the residential energy credits"), so it needs education added
   in all four places, and so does the `scope.credits` label.
5. **Sections 5.1, 5.2 and 10: the Stage 15 placeholder ids are now resolvable.** The rows need rewording as well
   as a new `s3.line3` operand:
   - Form 8880 CLW line 2 is `f8880.clw2`, `sum(s3.line1, s3.line2)`. It has **no `refuses` clause of its own**:
     the omission of lines 3, 6d and 6l is only a note in its cite locator ("(lines 3, 6d and 6l are refused by
     scope.credits)"). The map's "line 3 refused" should be read as "omitted, refused upstream".
   - The Form 5695 Part I worksheet line 2 is `f5695.rce_ws2`, `sum(s3.line1, s3.line2, s3.line4, s3.line5b,
     f5695.ctc)`. Its label and refusal text list "Schedule 3 lines 3, 6c, 6d, 6f, 6g, 6h, 6l and 6m".
   - The Form 5695 Part II worksheet line 2 is `f5695.eehi_ws2`, `sum(s3.line1, s3.line2, s3.line4)`. Its refusal
     text is "(Schedule 3 lines 3, 6d and 6l)".
   - `s8812.clw_a2` is `sum(s3.line1, s3.line2, s3.line4, s3.line5b)`. Its label ("in this tool lines 1, 2, 4 and
     5b") and its refusal text "(Schedule 3 lines 3, 6d, 6f, 6l, 6m)" both name line 3.
   - `f2441.clw2` is `copy s3.line1` and needs no change.
6. **D13 and section 4.1: there is now a second "claimed as a dependent" input.** Stage 15 added
   `person.sav_claimed`, per person: "Are you claimed as a dependent on someone else's 2025 tax return?". It feeds
   `person.sav_ineligible` only when `sa.dependent` is true (`forms/2025/person.yaml`). It sits beside the
   return-level `sli.claimed` that the map recommends reusing. D13 should choose between the two, or reconcile
   them, rather than present `sli.claimed` as the only candidate.
7. **D7 and Q3/Q5: per-person student and birth-date inputs now exist.** Stage 15 added `person.sav_student` (the
   5-calendar-month full-time student test) and `person.sav_born` ("born before January 2, 2008"). Neither is a
   drop-in for line 7:
   - Form 8880's student definition counts "a school" and on-farm training courses, while i8863 p. 7 says "an
     eligible educational institution".
   - The birth-date cutoff is not the age 18 or age 24 test.

   They are still the nearest precedent, and the interview would otherwise ask overlapping questions.

## Unverifiable

- **Whether a `def` instance's lines appear on the values sheet as the student's Part III (D2 option B).**
  `engine/src/eval.ts` evaluates a def through `copy` of an instance line, with the parameters bound in the caller.
  I did not trace how `output.ts` prints instance lines, and I did not run the engine.
- **Whether the Bill and Jane examples reproduce under the project's Tax Table and EIC Table.** This needs an
  engine run, which the read-only brief does not cover.
- **Whether Stage 16 computes Schedule 1 line 8r.** It is undecided, and D8 depends on it.
- **The effect of the thin microdata (0.53% flagged against 4.49%) on the +4.1 and +3.0 figures.** These are the
  report's figures and are not quantified anywhere.

## Confirmed

About 210 premises: about 180 quote fragments found on their cited page, and about 30 project, number and
archive facts. The decision-critical ones:

- **Form 8863 text:** every line text of f8863 pp. 1 to 2. Lines 2, 3, 4, 5 and 15 are found only in the layout
  layer (`.txt`), on the same page, which `tools/citations.py` accepts.
- **Credit Limit Worksheet:** line 5 reads "lines 1, 2, 6d, and 6l" (i8863 p. 8). With `ftc.limited` ≤
  `f1040.line16` and Form 2441 limited by its own CLW, lines 1 + 2 ≤ line 18. That supports Q4/D10's premise that
  CLW line 6 is never negative.
- **Credit order (5.1), checked against the code:** 2441 → 8863 → 8880 → 5695 Part II → 8812 → 5695 Part I. There
  is no cycle, because s3.line3 would read only `f1040.line18`, `s3.line1` and `s3.line2`. Schedule 8812 Credit
  Limit Worksheet B (new in Stage 15) reads `s3.line5a`, `f1040.line27a` and `s3.line11`, not line 3 or line 29, so
  it needs no change.
- **Schedule 3 and Form 1040:** Schedule 3 line 3 is "Education credits from Form 8863, line 19" and line 8 is "Add
  lines 1 through 4, 5a, 5b, and 7" (f1040s3 p. 1). Form 1040 line 29 is "American opportunity credit from Form
  8863, line 8" (f1040 p. 2). `f1040.line29` is currently `param sales.zero` with the `scope.credits` refusal.
- **The worksheets that subtract line 3:** CLW A line 2 includes Schedule 3 line 3 (i1040s8812 p. 4). Both Form
  5695 worksheets list "Nonrefundable Education Credits, Schedule 3 (Form 1040), line 3" (i5695 pp. 5, 7). Form
  8880 CLW line 2 reads "lines 1 through 3, 6d, and 6l" (f8880 p. 2). Form 2441 CLW line 2 reads line 1 and line 6l
  only (i2441 p. 5).
- **Parameters:** $180,000 / $90,000, $20,000 / $10,000, 40%, $10,000, 20%, $4,000, $2,000 and 25%, as printed on
  f8863. MFS is not printed. The second printings are on i8863 pp. 2 and 3.
- **`prorate` matches lines 6 and 17:** the ratio is rounded half-up, kept in [0, 1] and given places. The three
  places of `amb.2025.sli_ratio_places` are an "Owner ruling, Stage 11". Lines 6 and 17 both say "(rounded to at
  least three places)".
- **The AOC requirements and the refundability test:** the seven requirements (i8863 pp. 3 to 4), the Tip routing a
  failed AOC student to the LLC (p. 4), the line 7 conditions and definitions (p. 7), and p970 p. 20's item 3 (the
  same statuses).
- **Who cannot claim:** the five items on i8863 p. 3. The i1040gi p. 115 wording matches the `sli.claimed` label.
  `sli.eligible` reads `sli.claimed`.
- **Form 1098-T:** the requirement and its exceptions (i8863 p. 1). The dates differ, "After January 31, 2026"
  against p970 p. 2's "After February 2, 2026". p970 is the later revision (Jan 27, 2026, against Sep 16, 2025).
- **The AQEE worksheet:** it is per student per academic period, floored at zero (i8863 p. 9). That is the premise
  of D3/R7.
- **Form 8862 and the ban:** the Form 8862 rule and its exception (i1040gi p. 61), and the 2- and 10-year ban
  (i8863 p. 3).
- **AOC against LLC (4.4):** the AOC is at least the LLC per student. Checked by arithmetic, and asserted by the
  i8863 p. 3 Tip.
- **Official examples:** all reproduce arithmetically: $1,875 (decimal 0.750), $1,254 (decimal 0.950), the $2,500
  of Jack and Kay, the $1,000 of Bruce and Toni, and Bill's $1,500 + $1,000 split.
- **Existing gates:** `scope.other_line16` names education recapture. `scope.other_income` names nonresident alien
  status. `sa.excluded_income` covers Forms 2555 and 4563 and Puerto Rico. `s3.mfs` is in `scope.ready`.
  `scope.schedule1` names "other income for Schedule 1 line 8". `s2.other` covers the Form 5329-type additional
  tax.
- **Existing inputs:** `dependent.tin` (it includes an ITIN or ATIN applied for), `dependent.claimed`,
  `dependent.age` (Count), `person.tin`, `person.itin_applied`, `person.role`, and `household.all_tin` with the
  label quoted in the map.
- **Data model:** spec 4.4 allows a line to read only its enclosing entry, which is D2 option A's premise. The `def`
  mechanism exists (`se`, `tcw`, `tax_on_amount`). `retirement` is a return-level collection.
- **Coverage category:** `education` has gates `[scope.credits]` and combine `max` of soi-23in33ar columns 8 and
  40. Column 8 is 7,211,349 returns and $7,554,668 thousand. Column 40 is 5,821,688 returns and $5,090,364
  thousand. Column 40's own header cell reads "American opportunity credit" under "Total refundable credits"
  (rows 3 to 4). That settles the map's merged-cell caveat in its favour. The precedent for retiring a
  category (`refused: false`, `gates: []`) is used by `schedule_c` and now also by `cdcc`, `savers` and `energy`.
- **Not archived, as the map says:** Form 1098-T, Form 8862 and i8862, i1099q, Pub. 519. None is in the manifest.
  plaw-119-21 sec. 70606 applies to "taxable years beginning after December 31, 2025" (p. 219).
