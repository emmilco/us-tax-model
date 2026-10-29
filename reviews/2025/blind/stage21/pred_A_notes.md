# Predictor A notes: Stage 21 blind returns (Form 5329 early distributions)

Sources used: i5329 (Who Must File p.1; Line 2 exception table p.4-5; Line 4 SIMPLE 25%; Part VII lines 43/47),
p590b ch.1 Exceptions (medical p.25, higher ed p.26, first home p.27, birth/adoption, domestic abuse, emergency p.28),
i1040gi Sch 2 line 8 (p.112), standard deduction ($15,750 S / $31,500 MFJ), Tax Table pp.68-79 (rows checked in the
plain-text table), i8889 (self-only limit $4,300; line 13). IRA distributions on 1040 line 4b; 401(k)/SIMPLE: 401(k) on
5b, SIMPLE IRA on 4b. Line 16 = Tax Table; line 22 = line 16 (no credits, no Sch 2 Part I); line 23 = Sch 2 line 8;
line 24 = 22 + 23. Exception numbers decoded from the i5329 table: 02 SEPP, 05 medical, 08 higher ed, 09 first home,
12 incorrect code 1/J/S at 59 1/2+, 19 birth/adoption, 22 domestic abuse, 23 emergency, 99 more than one.
Readings: line 2 entered as 0 when no exception (rather than blank); 1040 line 5b entered 0 when no pension;
cents kept (no whole-dollar rounding), Sch 2 line 8 rounded to cents.

## E1
Both code 1, full tax owed -> i5329 Who Must File / i1040gi line 8 Exception: no Form 5329; 10% x (5,123.45+2,456.78)
= 758.023 -> 758.02, box checked. AGI 48,580.23; TI 32,830.23; Table row 32,800-32,850 single = 3,701.

## E2
SIMPLE code S within 2 years of 7/1/2024 first participation -> 25% (i5329 Line 4). Code S is not code 1, so
Form 5329 required. L1 5,500; L2 0; L3 5,500; L4 = 0.25x4,000 + 0.10x1,500 = 1,150. Box not checked.
AGI 63,500; TI 47,750; tax 5,495.

## E3
L1 17,000. L2 = 5,200 (exc 08, limited to qualified expenses) + 6,000 (exc 02 SEPP) = 11,200, exception 99.
L3 5,800 (1,800 IRA excess over tuition + 4,000 401(k)); L4 580. AGI 64,000; TI 48,250; tax 5,555.

## E4
First home: $10,000 lifetime cap less prior $1,200 (2021 distribution for mother's first home counts as a prior
qualified first-time homebuyer distribution, p590b First home req. 3) = 8,800 of 11,500 excluded.
Birth: $5,000 per taxpayer (p590b) of 7,500 excluded (IRA and 401(k) both "applicable eligible retirement plans";
not claiming the child does not matter -- she is his child). L1 19,000; L2 13,800 (99); L3 5,200; L4 520.
AGI 73,500 (4b 15,000; 5b 3,500); TI 57,750; tax 7,625.
Ambiguity: whether the $5,000 birth cap is per child/per taxpayer across plans -- read as aggregate per taxpayer.

## E5
Domestic abuse: p590b limit "lesser of $10,300 for 2025 or 50% of the present value of the IRA". Read as an
aggregate per-individual cap across the IRA and the 401(k) (statutory "aggregate amount ... by any individual") ->
10,300 of 11,500 excluded. 50% tests not binding (>15,000 / >25,000).
Emergency: one per calendar year (p590b) -> April IRA $700 qualifies (<= lesser of 1,000 or balance-1,000);
November 401(k) $600 does not. L1 12,800; L2 11,000 (99); L3 1,800; L4 180. AGI 60,800; TI 45,050; tax 5,171.
LEAST SURE: per-plan reading of the $10,300 cap would exclude all 11,500 (L2 12,200, L3 600, L4 60).

## E6
AGI 47,000 (wages + 9,000; AGI per p590b = 1040 line 11a). 7.5% = 3,525; 11,000 - 3,525 = 7,475 excluded (05).
L1 9,000; L2 7,475; L3 1,525; L4 152.50. TI 31,250; tax 3,515; line 24 3,667.50.

## E7 (MFJ)
AGI 117,000. Couple's medical limit 18,000 - 7.5% x 117,000 (8,775) = 9,225 >= 8,000 of IRA distributions, so both
IRA distributions fully excepted (05). Each spouse files own 5329 (i5329 Joint returns). You: L1 5,000, L2 5,000
(05), L3 0, L4 0 -- must file to claim exception (code 1 doesn't indicate it). Spouse: L1 7,000, L2 3,000 (05),
L3 4,000, L4 400. Sch 2 line 8 400, box no. TI 85,500; MFJ tax 9,786.

## E8
Born 5/20/1964: 61 in Aug 2025, past 59 1/2 -> code 1 incorrect; exception 12. Must file (i1040gi line 8: must file if
code 1 incorrectly shown). L1 15,000; L2 15,000 (12); L3 0; L4 0. Sch 2 line 8 = 0 (entered 0, not blank).
Standard deduction 15,750 (born after 1/1/1961). AGI 85,000; TI 69,250; tax 10,155.
Ambiguity: whether a distribution after 59 1/2 belongs on line 1 at all; followed exception-12 text ("Include on
line 2 the amount you received when you were age 59 1/2 or older"), which implies it is on line 1.

## E9 (MFJ)
Taxpayer: code 3 (disability) correctly shown -> exception indicated on 1099-R, not subject to tax -> no 5329
(Who Must File bullets 2/3). Spouse: code 1, full tax -> exception, no 5329; Sch 2 line 8 = 300, box checked.
AGI 95,000 (4b 15,000); TI 63,500; MFJ tax 7,146.
LEAST SURE: i1040gi "code 1 correctly shown in box 7 of all your Forms 1099-R" read per individual. If read as all
Forms 1099-R on the joint return (husband's code 3 included), the spouse must file 5329 (L1 3,000, L2 0, L3 3,000,
L4 300) and the box is not checked; tax unchanged.

## E10
HSA: limit 4,300 self-only (i8889); 8889 line 2 5,800, line 13 = 4,300 -> Sch 1 line 13 4,300. Excess 1,500 not
withdrawn: 5329 L47 1,500; L48 1,500 (no prior-year excess, L42 zero -> go to L47); L49 = 6% x smaller of 1,500 or
Dec 31 value 910 = 54.60. Because item (2) (excess contribution) also applies, the line 8 Exception ("If only item (1)
applies") is unavailable, so Part I is completed: L1 2,000, L2 0, L3 2,000, L4 200. Sch 2 line 8 = 254.60, box no.
HSA distributions all qualified, not income. AGI 65,000 + 2,000 - 4,300 = 62,700; TI 46,950; tax 5,399.
