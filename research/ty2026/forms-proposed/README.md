# Proposed 2026 definition changes (TY2026 step 5)

Proposals only. Nothing here is read by the build, and nothing under `forms/2025/` changes. Each file is either a
copy of the 2025 definition with the 2026 definition changes from `research/ty2026/changes.md` applied (`*.yaml`,
with `*.diff` against `forms/2025/`) or a new form. Year constants, page relocations and citations that only move are
left to `tools/year_diff.py --adopt` and `tools/citations.py --relocate`. Every rule here rests on an IRS 2026 draft
unless the cite is Public Law 119-21 as printed (`plaw-119-21`, final). Re-verify each one against the final forms
before adoption (`docs/ty2026/ADOPTION.md`).

## Files

| File | Change map entries | What it does |
|---|---|---|
| `f1040.yaml` / `.diff` | C-PRI-01 to C-PRI-08, C-PRI-18 | new line 12f, refused (`f1040.gate.nonitemizer_gifts`); line 14 adds 12f; lines 13a and 13b exchange printed numbers (ids unchanged; Schedule 1-A line 44); line 24 printed 24a, new 24b (Form 1062, refused on `f1040.form1062`) and 24c; lines 34 and 37 read 24c; the ACTC opt-out box removed; line 32 printed 32a, new 32b (Schedule 3-A) and 32c; line 33 reads 32c; labels of lines 23 and 29; the Schedule A line 18 screen as a refusal on line 15 (`f1040.gate.itemized_limit`) |
| `s3a.yaml` | C-PRI-05 | new form, Schedule 3-A, Federal Public Benefit, lines 1a to 8; line 8 refused whenever it is reached (`s3a.gate.qualified_alien`; owner decision 2026-11-04) |
| `sa.yaml` / `.diff` | C-PRI-13 to C-PRI-17 | line 8d (mortgage insurance premiums, held at zero and refused through the screen question, whose wording adds them and state-declared disasters); 8e adds 8d; new line 13 (lines 11 plus 12 less the 0.5% floor of the statute, `sa.gift_floor`; owner decision 2026-11-04); the carryover printed 14; the gifts total printed 15 and adding 13 and 14; casualty printed 16; gambling losses printed 17a at 90% of losses limited to winnings; new 17z; total printed 18 reading 17z |
| `w2.yaml` / `.diff` | C-PRI-24 | inputs for box 12 codes TP and TT (no reader yet) |
| `scveh.yaml` / `.diff` | C-BUS-01 | business miles asked for January 1 to June 30 and July 1 to December 31 (line 44a their sum); each period's miles times its exact rate (72.5 and 76 cents, `Rate` parameters), rounded half-up to the cent, then added; `scveh.rate` removed (owner decision 2026-11-04) |

The SALT, standard deduction, HSA and other amounts are parameters (step 4,
`research/ty2026/params-2026.proposed.yaml`), not definition changes. Schedules 1, B and D, Form 8949 and Form 8889
change only in labels, printed sub-line numbers, help text and parameters (C-PRI-11, C-PRI-19 to C-PRI-23, C-PRI-26):
no definition patch is proposed for them. The help text of the HSA coverage questions (C-PRI-22) and of
`f8889.medical` (C-PRI-23) must be rewritten from the 2026 instructions at adoption.

## Quotes behind the new rules

- Form 1040 (2026 draft, `f1040` p. 3): "12f Charitable contribution deduction for non-itemizers (see instructions)";
  "24b Enter amount from Form 1062, line 15"; "24c Add lines 24a and 24b"; "32b Amount from Schedule 3-A";
  "32c Subtract line 32b from line 32a"; "33 Add lines 25d, 26, and 32c".
- Schedule 3-A (2026 draft, `f1040s3a` p. 2): lines 1a to 8 as quoted in `s3a.yaml`.
- Schedule A (2026 draft, `f1040sa` pp. 2–3): "8d Mortgage insurance premiums (see instructions)"; "13 Enter the amount
  from line 6 of the Charitable Contribution Limitation Worksheet"; "17a Deductible gambling losses"; "Is the amount on
  Form 1040 or 1040-SR, line 11b, minus the amounts on lines 13a and 13b of that form, more than $384,350?".
- Public Law 119-21 (final): section 70114, "shall be equal to 90 percent of the amount of such losses during such
  taxable year" (p. 96); section 70425, "exceeds 0.5 percent of the taxpayer’s contribution base" (p. 165); section
  70111, "shall be reduced by 2⁄37 of the lesser of" (p. 94); section 70424 (p. 165), the $1,000 ($2,000) amounts of
  section 170(p).
- Mileage (final): `n-26-10` p. 3, "The standard mileage rate for transportation or travel expenses for 2026 is 72.5 cents per
  mile for all miles of business use"; `irb26-29` p. 13, "(1) Business 76 cents per mile", for expenses "on or after July 1,
  2026"; the split by date, `i1040sc` p. 7 (draft).

## Refusals proposed (new provisions the tool will not compute until their instructions post)

| Refusal | Why |
|---|---|
| `f1040.line12f` when `f1040.gate.nonitemizer_gifts` | the line's rule is in the 2026 Form 1040 instructions (not posted); section 170(p)'s base text is not archived |
| `f1040.line24b` when `f1040.form1062` | Form 1062 is not prepared by this tool |
| `f1040.line15` when `f1040.gate.itemized_limit` | the Itemized Deductions Worksheet is in the 2026 Schedule A instructions (not posted) |
| `s3a.line8_wanted` when `s3a.gate.qualified_alien` | Schedule 3-A line 8 asks about "qualified alien", defined only in instructions not posted (owner decision 2026-11-04: refuse those returns until the instructions define it). Refused only when line 8 is reached: line 6 more than zero and line 7 Yes |
| `sa.line8d` through `sa.unsupported` | the limits on deductible mortgage insurance premiums are in the 2026 Schedule A instructions |

## New parameters and inputs (the five-place ripple of `handoffs/HANDOFF-HARDENING-1.md`)

- New parameters in `params-2026.proposed.yaml` (`new_in_2026: true`): `sc.mileage_rate_h1` (725/1000) and
  `sc.mileage_rate_h2` (76/100), which replace `sc.mileage_rate` (listed under `retired`), and `sa.gift_floor_rate`
  (5/1000). Not yet there: `sa.gambling_rate` (90/100; `plaw-119-21` p. 96, final) and `sa.limit_screen` ($384,350;
  `f1040sa` p. 3, draft); add both at adoption.
- `scveh.dollar` reads `sc.hundred_cents` ($1.00, a 2025 parameter whose 2026 cite waits on `i4562`) as the unit the
  dollars-per-mile rates multiply.
- New inputs: `f1040.form1062` (Bool), `s3a.wants_benefit` (Bool), `w2.box12_tp`, `w2.box12_tt`,
  `scveh.miles_business_h1` and `scveh.miles_business_h2` (Count; `scveh.miles_business` stops being an input, so its
  interview questions and fixture values become the two new ones). `s3a.eligible` is dropped (line 8 is refused). Each must reach every fixture, the interview bank and profiles, `engine/src/generate.ts`,
  `tools/engines/generate_cases.py` and the input contracts.
- The work-authorization question on Form 1040 page 1 (C-PRI-06) is not proposed: the draft does not say what reads
  it.

## Build test

In a scratch copy of the repository (not this checkout), the proposed `f1040.yaml`, `sa.yaml`, `w2.yaml` and
`s3a.yaml` replaced the 2025 files (with `tax_year: 2025`, the 2026 drafts `f1040s3a`, `f1062` and `i1062` added to
the 2025 manifest, the two new parameters added, and `s3a.line4` pointed at `s2.line21` because the 2025 encoding has
no Schedule 2 line 20). `node engine/dist/main.js build` passed every structural check: references, types, cycles,
and guards (one guard form on Schedule 3-A line 8 was restructured into two Bool choices). The only errors were
missing interview questions for the new inputs (`s3a.wants_benefit` and the others above), as expected before the
ripple. Fixtures were not run. This is a structural check only. It says nothing about whether the 2026 rule is
right.

Re-run 2026-11-04 after the owner's decisions, the same way (scratch copy; the proposed `f1040.yaml`, `sa.yaml`,
`w2.yaml`, `s3a.yaml` and now `scveh.yaml` in place of the 2025 files; the five new parameters added; `n-26-10` and
`irb26-29` added to the 2025 manifest). The structural checks (references, types, cycles, guards) passed. The
first build's errors were an unregistered ambiguity id (`amb.2026.gift_floor_base`, on `sa.gift_floor` and
`sa.line13_ws`) and the interview question still naming `scveh.miles_business`; with a stub ambiguity entry and
questions for the two mileage inputs, the only errors left were the missing interview question for
`s3a.wants_benefit` (expected before the ripple). The source-predicted cases were not evaluated.

## Ambiguity notes (to enter in `ambiguities/2026.yaml` at adoption)

1. **Schedule 3-A line 4** reads "Schedule 2 (Form 1040), line 20". The 2026 Schedule 2 is renumbered (C-SCHED-10), and
   line 20 is "Total additional employment and other taxes. Add lines 16c, 17d, 18, and 19c". The encoding has no such
   line yet; `s3a.line4` names a future `s2.line20`.
2. **Schedule 3-A line 8, "qualified alien"**: the term is defined only in instructions not posted. Refused when line 8
   is reached (owner decision 2026-11-04). Do not reuse the Form 1040 work-authorization question for it.
3. **Form 1040 line 24b** reads "Form 1062, line 15", which itself says "Enter 25% (0.25) of line 14 here and on Form
   1120, line 32, or the applicable line of your return". Refused in any case.
4. **Gambling losses**: 90% of losses, then limited to winnings: the statute's order, and the 2026 drafts of the
   Schedule E and Schedule C instructions say so ("You must apply the 90% limitation first then apply the gambling
   winnings limitation", `i1040se` p. 2). The 2025 reading (`amb.2025.gambling_losses`) must be re-ruled. Losses and winnings reported on Schedule C or E (the new checkbox
   on line 17a) are not handled by this proposal; at adoption, refuse them or encode the checkbox from the 2026 instructions.
5. **Line 12f gate** reads `sa.line11`. Whether a non-itemizer is asked Schedule A line 11 depends on the interview
   order; check at adoption that the gate's inputs are always asked.
7. **Form 1062 on Schedule 3**: the 2026 Schedule 3 draft's line 13e takes Form 1062 line 14 into payments
   (C-PRI-04 correction, C-SCHED-39). With the election refused, line 13e is zero; the Schedule 3 patch is not drafted.
8. **Section 71304** (C-PEOP-27): a Form 1095-A plan enrolled in during an income-based special enrollment period
   gives no credit for 2026; Form 8962 needs a refusal (not drafted).
9. **The 0.5% charitable floor** (`amb.2026.gift_floor_base`, C-PRI-15): the contribution base is taken as Form 1040
   line 11b, not less than zero; the floor is rounded half-up to the cent; the carryover is outside the floor (the
   draft's line 15 adds it after line 13). Recheck all three against the 2026 Schedule A instructions.
10. **Mileage rounding** (C-BUS-01): each period's product is rounded half-up to the cent (`amb.2025.multiplication_subcent`);
   only the 72.5-cent product can carry half a cent, so rounding the sum instead gives the same result.
6. **13a and 13b**: the 2026 Form 8995 instructions (draft) still name Form 1040 line 13a for the QBI deduction
   (C-SCHED-31); the Form 1040 draft prints it at 13b.

## Other forms (not drafted in this session)

The definition changes of the other sections of the change map are not drafted as patches, except the mileage split
(C-BUS-01, `scveh.yaml`). They are listed in
`docs/ty2026/ADOPTION.md` in the order to do them: Schedule 1-A renumbering and the per-employer tips and overtime
(C-SCHED-01 to -05), Schedule 2 renumbering (C-SCHED-10, -11, -13), Forms 8995 and 8995-A (C-SCHED-31 to -33),
Form 5695 carryforward only (C-CRED-01 to -09), Form 2441 rates and lines (C-CRED-10 to -12), the education credit SSN
rule (C-CRED-18, C-PEOP-16), Form 8962 without the repayment limitation and above 400% (C-PEOP-12, -14), the Form 5329
split and exception 24 (C-PEOP-03, -05), the Form 1099-R boxes and Trump accounts (C-PEOP-04, -11), Schedule C line 16 (C-BUS-02), meals (C-BUS-04), and Form 4562 (C-BUS-11, -12).
