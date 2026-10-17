# EIC Table against Rev. Proc. 2024-40 — result for 2025

Method: for every band of `eic_0` to `eic_3` (extracted from i1040gi pp. 49-60 by `tools/extract_eic_table.py`)
and both status columns, the credit at the band's midpoint is the smaller of the midpoint times (maximum
credit / earned income amount) and the maximum credit, less (maximum credit / (completed phaseout amount -
threshold phaseout amount)) times the excess of the midpoint over the threshold phaseout amount, not below
zero, rounded half-up to whole dollars. The four amounts per child count and status are the year parameters
`eic.earned_amount*`, `eic.maximum*` (Rev. Proc. 2024-40 section 3.06(1)) and `eic.ws_threshold*`, `eic.limit*`
(the instructions' Worksheet A line 5 and Step 1 amounts, which equal the Rev. Proc.'s threshold and completed
phaseout amounts). The rates are those the Rev. Proc. amounts imply; the statutory percentages are not archived,
so a difference of $1 is expected where an implied rate is rounded. A larger difference would mean a misread
row or column. Two readings of the printed table are part of the method: a row split for a footnote in one
column keeps the whole row's value, figured at the whole row's midpoint, in the other column; and the band
that contains the earned income amount prints the maximum credit (checked as equality with the maximum).

- Cells tested: 11008 (of which 8 in a band containing the earned income amount)
- Equal to the formula: 10369
- Differing by $1: 639
- Differing by more than $1: 0

No cell differs by more than $1.
