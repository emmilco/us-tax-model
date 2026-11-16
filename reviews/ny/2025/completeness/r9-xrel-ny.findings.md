# Completeness review, round 9 (sampled release reviews, lane xrel): adjudication of the New York units (8 claims)

Fork `ny` of lane xrel (claude-opus-5-5, judgment), tax year 2025, jurisdiction ny. The rulings are in
`/tmp/xrel/frag/ny.completeness.json` (keys `unruled:<form>#1.<n>`), for the lead to merge; `rulings.json` was not
edited. `python3 /tmp/xrel/xrel.py merge --jurisdiction ny` (validation only) accepts all 8. Its one note is the pending
bug id of the new real gap (`BUG-0852`), which fails the gate until the numbered-bug pass, as accepted for this
release.

Each claim was checked against the archived IT-201-I (`sources/ny/2025/ny_it201i.txt`, `ny_it201i-html.txt`), the form
YAML (`forms/ny/2025/`, `forms/2025/`) and the interview wording (`interview/ny/2025/questions.yaml`,
`interview/2025/questions.yaml`). Earlier rulings on the same units were used as leads and checked against the current
lines. Separate returns (MFS) are now supported, so each spouse claim was checked against that.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| ny_city_rs | 1 | 0 | 0 | 1 | 0 | 0 |
| ny_rs | 1 | 0 | 0 | 1 | 0 | 0 |
| ny_it2 | 1 | 0 | 0 | 1 | 0 | 0 |
| ny_it201 | 5 | 2 | 1 | 1 | 0 | 1 |
| **Total** | 8 | 2 | 1 | 4 | 0 | 1 |

## Rulings

| Claim | Class | Line or gate | Bug | Summary |
|---|---|---|---|---|
| ny_city_rs#1.1 | out of scope | ny_it201.gate.spouse_nonresident | | Mixed-residency joint return. On a federal joint return, `ny_it201.ask.spouse_resident` No refuses line 1. A separate federal return keeps status 3. |
| ny_rs#1.1 | out of scope | ny_it201.gate.spouse_nonresident | | Same as ny_city_rs#1.1. |
| ny_it2#1.1 | out of scope | (federal: scope.other_income) | | Wages without a W-2 are refused federally: `scope.wages_no_form` feeds `scope.other_income`. Nonresident aliens are refused there too. Form IT-2 records wages, not self-employment income. This is BUG-0749 (c). |
| ny_it201#1.1 | covered | ny_it201.item_h_count | | `dependent.claimed` copies `dependent.meets_tests`, so every listed dependent who qualifies is claimed. The tool cannot decline a dependent, and the list asks for everyone. |
| ny_it201#1.2 | wrong | ny_it201.line69a | | Line 69a's first guard is item C Yes, which gives $0. |
| ny_it201#1.3 | real gap | | BUG-0424 | Spouse unknown or refusing to sign. Still not asked and not refused. BUG-0749 (d) defers the refusing question. |
| ny_it201#1.4 | real gap | | BUG-0852 | SCRA residence election. Covered on a joint return, where the servicemember's active duty refuses. Open on a separate return: a civilian spouse is not asked about the spouse's service. Also open for Public Health Service and NOAA officers. |
| ny_it201#1.5 | out of scope | (federal: scope.schedule1) | | Limited partners: every K-1 is refused by `scope.k1` in `scope.schedule1`; the k1p collection is not wired. Earnings without SE tax: nonresident aliens are refused by `scope.other_income`, and Form 4361/4029 or treaty cases by `person.se_screened`. |

The two federal refusals are named in the evidence but not as `gate`. The completeness validator checks gates against
the New York canonical line ids only.

## New pending bug

- **BUG-0852** (low): SCRA residence elections are not asked of a civilian spouse filing separately, nor of
  Public Health Service or NOAA officers. Proposed fix: add a New York question, asked on every return, about the filer's or
  spouse's active duty (armed forces, Public Health Service, NOAA Corps), refusing line 1 with the item G M4 to M9 codes.
  The Coast Guard wording is BUG-0902.

No form data, fixture or tool was changed. No paid call was made.
