# Research: `amb.2025.s179_carryover_no_property`

Question (owner, T-041): with no section 179 property placed in service in 2025, can a
section 179 carryover from 2024 (2024 Form 4562 line 13) be deducted in 2025, up to the
business income limit? More generally: does the cost of property placed in service in 2025
cap how much of a carryover can be deducted?

## Answer

Yes. The carryover is deductible up to the smaller of (a) the unused part of the dollar
limitation ($2,500,000, reduced only when 2025 section 179 property costs more than
$4,000,000, less the 2025 election) and (b) the business income limit. The cost of property
placed in service in 2025 does not cap it.

On Form 4562 this is the result lines 5 to 12 produce when line 1 holds the maximum the
line 1 instruction states ($2,500,000), not Worksheet 1's smaller of that and the cost of
2025 property. Worksheet 1's cap changes no return without a carryover. On a return with
one, it departs from the statute and the regulation.

Confidence: high on the statute and the regulation, whose text is quoted below. No IRS
ruling or case on this point is archived. The one residual reading is noted under "Limits".

## Sources (archived by `tools/fetch_sources.py`; revisions in `sources/2025/manifest.json`)

| Id | What | Used for |
|---|---|---|
| `usc-26-179` | 26 U.S.C. 179, U.S. Code 2024 edition (GovInfo) | the carryover rule, (b)(3)(B); the dollar limitation, (b)(1)–(2) |
| `plaw-119-21` | P.L. 119-21 (July 4, 2025), 139 Stat. 72 | sec. 70306, the only 2025 amendment to section 179 |
| `cfr-26-1-179-2` | Treas. Reg. 1.179-2, 26 CFR (4-1-25 edition) | the dollar limitation's definition |
| `cfr-26-1-179-3` | Treas. Reg. 1.179-3, 26 CFR (4-1-25 edition) | the carryover deduction and its example |
| `i4562` | Instructions for Form 4562 (2025) | line 1, Worksheet 1, lines 5, 10, 11, 12 |
| `i4562-2024` | Instructions for Form 4562 (2024) | Worksheet 1 is not new for 2025 |
| `p946` | Pub. 946 (2025), chapter 2 | the carryover paragraph (neutral on this point) |

## Reasoning

1. **The statute's carryover rule.** 26 U.S.C. 179(b)(3)(B) (`usc-26-179`, p. 896): "The
   amount allowable as a deduction under subsection (a) for any taxable year shall be
   increased by the lesser of— (i) the aggregate amount disallowed under subparagraph (A)
   for all prior taxable years (to the extent not previously allowed ...), or (ii) the
   excess (if any) of— (I) the limitation of paragraphs (1) and (2) (or if lesser, the
   aggregate amount of taxable income referred to in subparagraph (A)), over (II) the amount
   allowable as a deduction under subsection (a) for such taxable year without regard to
   this subparagraph."

2. **"The limitation of paragraphs (1) and (2)" is the dollar amount.** Paragraph (1): "The
   aggregate cost which may be taken into account under subsection (a) for any taxable year
   shall not exceed $1,000,000" ($2,500,000 after P.L. 119-21). Paragraph (2) reduces that
   limitation "by the amount by which the cost of section 179 property placed in service
   during such taxable year exceeds $2,500,000" ($4,000,000 after P.L. 119-21). The cost of
   2025 property enters only through that reduction. With no 2025 property there is no
   reduction, so the limitation is the full $2,500,000.

3. **P.L. 119-21 did not touch the carryover rule.** Sec. 70306 (`plaw-119-21`, 139 Stat.
   197–198) amends section 179(b) only "in paragraph (1), by striking '$1,000,000' and
   inserting '$2,500,000'", "in paragraph (2), by striking '$2,500,000' and inserting
   '$4,000,000'", and the inflation base in paragraph (6)(A). No other provision of the Act
   mentions section 179. The archived U.S. Code edition still shows the old amounts, and
   its paragraph (3) is current.

4. **The regulation says the same.** Treas. Reg. 1.179-2(b)(1) (`cfr-26-1-179-2`) defines
   the dollar limitation as the statutory amount "reduced (but not below zero) by the amount
   of any excess section 179 property ... placed in service during the taxable year". It is
   not capped at the cost of property placed in service. Treas. Reg. 1.179-3(b)(1)
   (`cfr-26-1-179-3`) increases the deduction by the lesser of the outstanding carryover or
   "the amount of any unused section 179 expense allowance for the taxable year". Paragraph
   (c) defines that allowance as the excess of "(1) The maximum cost of section 179 property
   that the taxpayer may deduct ... after applying the limitations of section 179(b) and
   § 1.179-2; over (2) The amount of section 179 property that the taxpayer actually elected
   to expense". The example in paragraph (d) computes it as "$10,000 limit less $8,000
   elected to be expensed, or $2,000": the limit less the election, not the cost less the
   election.

5. **The form computes the statute's rule when line 1 is the dollar limitation.** Write L
   for the dollar limitation after reduction, E for the 2025 election (line 8, never more
   than the cost of the property elected), C for the carryover (line 10), and I for business
   income. With line 1 = $2,500,000, line 5 = L. Then:
   - line 9 = min(E, L);
   - line 11 = min(I, L) (i4562 p. 5, Line 11: "Enter the smaller of line 5 or the total taxable
     income from any trade or business you actively conducted");
   - line 12 = min(line 9 + C, line 11) = min(min(E, L) + C, L, I).

   The statute gives A + min(C, min(L, I) − A), where A = min(E, L, I) is the deduction
   without the carryover. If I ≥ min(E, L), both are min(min(E, L) + C, L, I). If
   I < min(E, L), both are I. The two agree on every input.

6. **Worksheet 1's cap matters only when there is a carryover.** Worksheet 1 (i4562 p. 4,
   "Enter the smaller of line 1 or line 2", where its line 1 is the cost K of 2025 section
   179 property) makes Form 4562 line 1 = min(K, $2,500,000). Line 12 then becomes
   min(E + C, K, L, I), because E ≤ K.
   - **Without a carryover (C = 0):** this equals min(E, L, I) as before, since E ≤ K.
   - **With one:** the carryover is held to K − E. With no 2025 property (K = 0) it
     deducts nothing, and the same happens when the whole cost of 2025 property is elected
     (E = K). The statute allows min(C, min(L, I) − E) in those cases.
   - **When they differ:** exactly when C > 0, K < min(L, I) and E + C > K.

7. **Worksheet 1 is an aid, not the rule.** The line 1 instruction (i4562 p. 4) states the rule:
   "Generally, the maximum section 179 expense deduction is $2,500,000 for section 179
   property ... placed in service during the tax year beginning in 2025". It introduces
   the worksheet as optional: "Tip: You can use Worksheet 1 to assist you in determining the
   amount to enter on line 1." The same worksheet is in the 2024 instructions (`i4562-2024`,
   p. 4), so it is not a 2025 change.

8. **The line 5 instruction still holds where it applies.** "If line 5 is zero ... enter
   zero on line 12, and enter the carryover ... on line 13" (i4562 p. 5). With line 1 =
   $2,500,000, line 5 is zero only when the reduction uses up the limitation (2025 property
   costing $6,500,000 or more). Then the unused allowance of 1.179-3(c) is also zero, so the
   instruction and the statute agree there.

9. **Pub. 946 is consistent with either reading.** Chapter 2, "Carryover of disallowed
   deduction" (`p946`): "You use the amount you carry over to determine your section 179
   deduction in the next year. Enter that amount on line 10 of your Form 4562 for the next
   year." It sets no condition on placing new property in service.

## Limits

- Treas. Reg. 1.179-3(c)(1)'s words "maximum cost of section 179 property that the taxpayer
  may deduct" could be read as bounded by the cost of property placed in service that year.
  That reading would contradict the statute it implements ("the limitation of paragraphs
  (1) and (2)") and its own cross-reference to the limitations of section 179(b) and
  1.179-2, whose dollar limitation is not so bounded. It is not adopted.
- Formalizing the statute is a non-goal (spec 2.3). The statute and regulation are used here
  only to resolve a tension inside the instructions, between the line 1 rule and Worksheet
  1's cap, as spec principle 7 provides for ambiguous or internally inconsistent
  instructions.
- No IRS ruling, case or other secondary source on this point was archived or consulted.

## Effect on the build (if adopted)

- `s179.line1` becomes the dollar limitation `s179.max`, cited to i4562 p. 4, Line 1.
- Every fixture that asserts `s179.line1`, `line5` or `line11` with 2025 property costing
  less than $2,500,000 changes on those lines (9 cases assert one of them). Line 12 changes
  only for returns with a carryover, among them `stage14.s179.carryover_no_property`
  (line 12 becomes $3,000 when business income allows; line 13 becomes zero).
- The `s179` transcription and render reviews and its class M log go stale on line 1 and
  are rerun.
