# Review B: independent re-transcription of the New York IT-201 encoding (tax year 2025)

Scope: forms/ny/2025/ny_it201.yaml, ny_rs.yaml, ny_city_rs.yaml, ny_tcw.yaml, ny_tcw_first.yaml, ny_it2.yaml;
params/ny/2025.yaml; tables/ny/2025/*.yaml; ambiguities/ny/2025.yaml. Each line was first derived from the
archived sources (IT-201-I web edition for tables, schedules, worksheets and the filing-status digits; PDF
cols/layout text for page cites; IT-201 layout text for line labels; tax-table web page; IT-270-I; IT-2), then
compared with the encoding. No model or API calls were made, no files were changed except this report. The only
scripts run were my own `python3 -I` checks in the scratchpad.

## Summary

| severity | count |
| --- | --- |
| high | 1 |
| medium | 1 |
| low | 5 |

## Findings

### H1 (high, small amounts): lines 72 and 73: IT-2 withholding is not rounded to whole dollars

- **Source.** Form IT-2 (2025), back, "Entering whole dollar amounts – When entering amounts, enter whole dollar
  amounts only (zeros have been preprinted). Use the following rounding rules when entering your amounts; drop
  amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar. For example, $1.39 becomes $1
  and $2.50 becomes $3." The same back page says "Include the total NYS tax withheld amounts ... from all your
  Form(s) IT-2" on IT-201 line 72, and the NYC totals on line 73. IT-201 shows ".00" boxes on lines 72 and 73.
- **Encoding.** `ny_it2.state_withheld` and `ny_it2.city_withheld` are raw `input` NonNegDollars, with no
  rounding. `ny_it201.line72` and `ny_it201.line73` are `sum_over` of those raw values. `ny_fixtures.py` feeds
  values in cents. Lines 1 to 18 round each federal amount (amb.ny.2025.whole_dollars), but the IT-2 records do not.
- **Effect.** Federal Form W-2 boxes 17 and 19 usually show cents. When they do, lines 72 and 73 carry cents, and so
  do lines 76, 77, 78, 78b and 80. With several W-2s, the total can also differ by $1 or more from the sum of
  per-record rounded entries that IT-2 requires.
- **Fix.** Add per-record lines that round each entry half-up to the dollar, for example
  `ny_it2.state_withheld_rounded: { op: round, of: ny_it2.state_withheld, unit: 100, rule: half_up }` and the same
  for City. Sum the rounded lines on lines 72 and 73, and cite the IT-2 back page.

### M1 (medium): tax computation worksheets 1–5, 7–10, 12–15: line 8/9 is rounded twice

- **Source.** Worksheet 1 (web edition): "7. Divide line 6 by $50,000 and round the result to the fourth decimal
  place", then "8. Multiply line 5 by line 7". Worksheet 2 (and the other recapture worksheets) step 9: "Multiply
  line 5 by line 8". The register's chosen reading (amb.ny.2025.whole_dollars) says "A product of a rate and an
  amount is rounded once to the dollar (multiply_rate with unit 100), not first to the cent."
- **Encoding.** `ny_tcw_first.line8_cents` and `ny_tcw.line9_cents` use `prorate`, which rounds the product to the
  cent. `line8` and `line9` then round that result half-up to the dollar. The register entry
  amb.ny.2025.fourth_decimal states the double rounding and accepts it.
- **Effect.** Line 5 (or the Incremental Benefit amount) is in whole dollars, and the ratio has four decimals, so the
  exact product has four decimals. When its fractional part is from .4950 to .4999, the encoding gives $1 more than
  a single half-up rounding. That is about 50 of every 10,000 ratio values in each phase-in band. Measured cases:

  | worksheet | line 33 | exact product | encoding | single rounding |
  | --- | --- | --- | --- | --- |
  | 2 (MFJ, TI 161,551–323,200) | $162,820 | 807 × 0.0254 = 20.4978 | 21 | 20 |
  | 3 | $324,465 | 69.4991 | 70 | 69 |
  | 8 (single) | $222,650 | 265.495 | 266 | 265 |
  | 13 (HOH) | $271,255 | 89.4999 | 90 | 89 |

  Line 39 is $1 too high on those returns.
- **Fix.** Compute the product in one rounding:
  1. Keep the 4-decimal ratio as its own line.
  2. Multiply with `multiply_rate` (unit 100), or give `prorate` a dollar product unit.
  3. Align amb.ny.2025.fourth_decimal with the whole-dollar reading, or record a deliberate deviation from it.

### L1 (low): lines 40 and 48: the "over 7" refusals also fire for Single filers

- **Source.** "Filing status ① only (Single): Use New York State household credit table 1." Table 1 has no
  number-of-people column; Note 3 ("For each individual over 7…") applies to tables 2, 3, 5 and 6. Table 1 allows no
  credit over $28,000, and Table 4 none over $12,500.
- **Encoding.** `gate.hh_state_over7` and `gate.hh_city_over7` test `hh_people > 7` with the table 2/5 limits
  ($32,000 / $22,500) for every status, Single included.
- **Effect.** A Single filer with 7 or more dependents and federal AGI of $32,000 or less is refused although
  tables 1 and 4 apply without any column. No wrong amount results.
- **Fix.** Add `f1040.status ∈ {mfj, hoh, qss}` to both gates.

### L2 (low): lines 40 and 48, married filing separately: the gate uses own line 19, not the total of both returns

- **Source.** Table 3/6 heading: "If your federal adjusted gross income (see Note 4) total from both returns is:".
  Note 4: "If your spouse was not required to file … use your spouse's federal adjusted gross income".
- **Encoding.** `hh_state_in_range` and `hh_city_in_range` test own `line19` ≤ $32,000 / $22,500, and outside that
  range the MFS credit is 0.
- **Effect.** If the spouse's AGI is negative, the combined AGI can be in range while own AGI is not. The encoding
  then enters 0 instead of refusing. This needs a negative spouse AGI, so it is very rare.
- **Fix.** Either refuse every MFS filer with item C No (the simplest), or ask for the spouse's federal AGI.

### L3 (low, latent): lines 77 and 80: line 81 would be counted twice

- **Source.** Line 77 is the overpayment less the penalty. "If your estimated tax penalty on line 81 is greater than
  your overpayment on line 77, enter the difference on line 80." Line 81: "Add the same amount to any tax due" (when
  tax is due).
- **Encoding.** `line77 = floor0(overpaid − line81)` and `line80 = tax_due + line81 + line82` in every case. With an
  overpayment and a nonzero line 81, the penalty would reduce line 77 and also appear in full on line 80.
- **Effect.** None today: line 81 is always `ny.zero` (refused).
- **Fix.** If line 81 is ever computed, make line 80 = `floor0(line62 + line81 − line76) + line82`, or guard the
  line 81 term on tax_due > 0, and add only the excess of line 81 over the overpayment otherwise.

### L4 (low): line 59: part-year abode proration not modelled

- **Source.** Sales and use tax chart, after the table: "If you maintained a permanent place of abode in New York
  State for sales and use tax purposes for only part of the year, multiply the tax amount from the chart by the
  number of months … and divide the result by 12."
- **Encoding.** The chart amount is used unprorated, and no question or refusal covers it. A full-year income-tax
  resident by domicile can still lack an abode for part of the year.
- **Fix.** Add a refusal question for it, or prorate.

### L5 (low): line 81 gate, and two unused parameters

- **Source (line 81).** "You may owe a penalty: if line 80 is $300 or more and represents more than 10% of the income
  tax shown on your 2025 return; or if you underpaid your estimated tax liability for any payment period." Also:
  "It is possible for you to owe an estimated tax penalty and also be due a refund."
- **Encoding.** `gate.estimated_penalty` refuses only when tax_due > 0 and the annual prepayments are below
  100%/110% of the 2024 tax.
  - It refuses more often than the $300/10% test would: `ny.est.min_due` and `ny.est.share` are defined in params
    but read nowhere.
  - It never refuses the penalty-with-refund case, or the case where the annual safe harbour is met but an
    installment was late (estimated payments on line 75).
  - This follows the instructions' "In general, you are not subject to a penalty if…", so the gap concerns only
    filers whose estimated payments were late.
- **Fix.**
  - Either remove the two unused params or use them.
  - Consider refusing when line 75 > 0 and the payments were not made by each installment date.

## Checked and found right

**Arithmetic (IT-201).**
- **Federal lines.** Lines 1–7, 9, 10, 14–16 and 18 round the right federal lines (1z, 2b, 3b, Sch 1 lines 1, 2a, 3,
  1040 7a, 4b, 5b, Sch 1 line 7, 6b, Sch 1 lines 9 and 26). Lines 8, 11, 12 and 13 are zero.
- **Lines 17–38.** Line 17 adds lines 1–11 and 13–16, excluding 12. Line 19 = 17 − 18. Line 24 adds 19–23. Line 27
  is line 15. Line 32 adds 25–31. Line 33 = 24 − 32. Line 35 is floored at 0. Line 36 is $1,000 × item H count.
  Line 37 is floored at 0 ("leave blank"). Line 38 = line 37.
- **Lines 43–58.** Lines 43, 44 (floor), 46, 47 (= line 38, worksheet only with itemizing), 49 (floor), 52, 54
  (floor), 54c/d (0.60%/0.34%), 54e and 58 (54 + 54e + 55–57).
- **Lines 61–78b.** Lines 61, 62, 76 (63–75 including 69 and 69a), 77 (net of 81), 78 = 77 − 79 (refused if
  79 > 77), and 78b = 78 − 78a.

**Line 34.** Standard deduction table: 6 cells. $3,100 applies only to Single with item C Yes; MFS gets $8,000
whatever item C says.

**Line 39 selection.**
- **Boundaries.** "$107,650 or less" is `le`. "$65,000 or more" for the schedule is the complement of `lt` 65,000.
  Worksheets 6/11/16 apply when line 33 > $25,000,000 (10.9% × line 38).
- **Status grouping.** MFJ and QSS use worksheets 1–5. Single and MFS use 7–10. HOH uses 12–15.
- **Taxable-income ranges.** ≤ $161,550 / $215,400 / $269,300, then the printed "more than … but not more than"
  ranges. The AGI conditions in the worksheet headings are implied, because line 38 < line 33 whenever a standard
  deduction is taken.

**Worksheets.**
- **Worksheets 1, 7 and 12.** Flat rate 5.5%/6%/6%; Stop at line 33 ≥ $157,650; excess over $107,650; ratio
  ÷ $50,000 to 4 places; line 4 + line 8. The line 5 floor never acts, which I verified.
- **Worksheets 2–5, 8–10 and 13–15.** Schedule tax + Recapture Base + Incremental × min(excess, $50,000)/$50,000.
- **Printed amounts.** All 11 start amounts, 9 taxable-income limits and 20 Recapture/Incremental amounts match the
  web edition (333/807, 1,140/2,747, 3,887/60,350, 64,237/32,500, 568/1,831, 2,399/30,172, 32,571/32,500,
  787/2,289, 3,076/45,261, 48,337/32,500).

**State rate schedule.** 3 groups × 9 bands: 9 rates, 26 over/upper/base values per group. All 108 band lines and
the 27 band guards (≤ upper, > previous upper) were checked by script against the params. QSS uses the MFJ
schedule and MFS the Single schedule.

**City schedule.** 3 groups × 4 bands. The 3.078/3.762/3.819/3.876% rates and the bases 665/1,545/3,264,
369/858/1,813 and 443/1,030/2,176 match. All 48 band lines and 12 guards were checked. Line 47a uses the table
below $65,000.

**Tax tables.**
- **Contents.** The State and City tables (1,302 bands each, three columns) were re-parsed independently from
  `ny_it201_tax_tables.txt`. Every band and cell is identical, and the bands are contiguous up to $65,000.
- **Columns.** Single+MFS, Joint+QSS ("*This column must also be used by a qualifying surviving spouse") and HOH.
- **Printed examples.** $38,275 MFJ gives $1,773 State and $1,292 City; both reproduce.
- **Agreement with the schedules.** Both tables agree with the schedules within rounding over $50,000–$65,000.

**Household credit.**
- **Cells.** Tables 1, 2, 4 and 5 were compared cell by cell: 6 + 56 + 2 + 28 credit cells, plus band edges as
  [X + 1¢, Y + 1¢) and a zero "No credit" band. All match.
- **Selection.**
  - **Status.** Single uses tables 1/4. MFJ, HOH and QSS use tables 2/5. MFS (tables 3/6) is refused in range.
  - **Item C.** Yes gives 0.
  - **People.** Item H count + 1 + 1 for MFJ only (QSS 0).
  - **AGI.** Line 19 floored at 0 per Note 2.

**Line 69.** Income = line 19 − line 9. The amount is 0 if item C is Yes or income > $250,000. Table 1 gives $63 for
①③④ and $125 for ②⑤.

**Line 69a.**
- **Bands.** 0.171% up to $21,600/$12,000/$14,400 (②⑤ / ①③ / ④). Above that, $37/$21/$25 plus 0.228% of the
  excess.
- **Rounding.** Rounded once to the dollar.
- **Limit.** The $500,000 test is refused under either reading (B7).

**Line 59 (sales and use tax chart).** 8 bands: up to $15,000 inclusive (negative floored), then "15,001–30,000" and
so on as > / ≤. Amounts 3, 6, 10, 15, 18, 26, 34. Above $200,000: min(0.000175 × AGI, $125). Input is line 19.

**Line 70a gate.** The IT-270-I largest thresholds + $5,000: $96,902 (②⑤, "7 or more" $91,902) and $93,361 (others,
"8 or more" $88,361).

**Parameters.** All 213 entries in params/ny/2025.yaml were compared with the printed amounts; no value
disagreement. The `sut.cap` quote "whichever amount is smaller" is the PDF wording; the web edition prints "whichever
is smaller".

**Not re-derived.** Pure refusal screens and inputs: lines 20–23, 25, 26, 28–31, 41, 42, 45, 50, 51, 53, 55–57, 60,
63–68, 70, 71 and 74 are `ny.zero` with screens.
