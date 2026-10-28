# Ten 2025 federal returns to work by hand from the IRS text

Each return is for tax year 2025, filed on Form 1040. Unless a return says otherwise:

- The filer is single, 40 years old, not blind, a U.S. citizen with a valid SSN, living in the United States all
  year. Nobody can claim the filer as a dependent. There are no dependents.
- The filer's only income is the wages from one employer on Form W-2, plus the items listed. Federal income tax
  withheld is $0, and there are no estimated payments or other payments.
- The filer takes the standard deduction unless itemized deductions are larger.
- Nothing else: no other income, adjustments, credits or taxes, and no qualified business income deduction.
- Sales of stock are on Form 1099-B with basis reported to the IRS: box A for short-term, box D for long-term.
  There are no adjustments, so each sale's gain or loss is the proceeds less the basis.
- "2024 return" figures are as printed on the return the filer filed for 2024. Schedule D lines 7 and 15 are
  signed: a loss is negative. Line 21 is shown as the loss printed in parentheses.

Work from the archived 2025 IRS documents only:

- `sources/2025/f1040.cols.txt` and `sources/2025/i1040gi.cols.txt` (Form 1040 and its instructions, including the
  Tax Table and the Qualified Dividends and Capital Gain Tax Worksheet);
- `sources/2025/f1040sd.cols.txt` and `sources/2025/i1040sd.cols.txt` (Schedule D and its instructions, including the
  Capital Loss Carryover Worksheet, the 28% Rate Gain Worksheet and the Schedule D Tax Worksheet);
- `sources/2025/p550.cols.txt` (Pub. 550);
- `sources/2025/f4952.cols.txt`;
- `sources/2025/f1040sa.cols.txt` and `sources/2025/i1040sca.cols.txt`;
- `sources/2025/f8960.cols.txt` and `sources/2025/i8960.cols.txt`;
- `sources/2025/f8959.cols.txt` and `sources/2025/i8959.cols.txt`;
- and any other file under `sources/2025/`. Pages are separated by form-feed characters.

## The returns

**R1.** Wages $60,000. In 2025 sold stock held 6 months: proceeds $5,000, basis $4,000 (box A). 2024 return: Form
1040 line 11 $55,000, line 14 $14,600; Schedule D line 7 −$8,000, line 15 $0, line 21 ($3,000).

**R2.** Wages $80,000. In 2025 sold stock held 3 years: proceeds $12,500, basis $10,000 (box D). 2024 return: Form
1040 line 11 $70,000, line 14 $14,600; Schedule D line 7 $0, line 15 −$12,000, line 21 ($3,000).

**R3.** Wages $9,000. No sales in 2025. No tax-exempt interest. 2024 return: Form 1040 line 11 $4,000, line 14
$14,600; Schedule D line 7 −$2,000, line 15 −$5,000, line 21 ($3,000). (The filer also qualifies for the earned
income credit; you need not figure it.)

**R4.** Wages $20,000. No sales in 2025. 2024 return: Form 1040 line 11 $13,600, line 14 $14,600; Schedule D line 7
−$6,000, line 15 $0, line 21 ($3,000).

**R5.** Wages $90,000. In 2025 sold stock held 3 years: proceeds $16,000, basis $10,000 (box D). 2024 return: Form
1040 line 11 $90,000, line 14 $14,600; Schedule D line 7 −$10,000, line 15 $3,000, line 21 ($3,000).

**R6.** Wages $50,000. No sales in 2025, but a mutual fund paid $500 of capital gain distributions (Form 1099-DIV
box 2a $500; box 1a ordinary dividends $0). 2024 return: Form 1040 line 11 $50,000, line 14 $14,600; Schedule D
line 7 $2,000, line 15 −$9,000, line 21 ($3,000).

**R7.** Married filing jointly; both spouses 40, not blind. Wages $70,000 (one spouse) and $50,000 (the other),
with $7,000 and $5,000 of federal income tax withheld. In 2025 sold stock held 3 years: proceeds $45,000, basis
$25,000 (box D). Their 2024 joint return: Form 1040 line 11 $110,000, line 14 $29,200; Schedule D line 7 $0, line
15 −$15,000, line 21 ($3,000).

**R8.** Wages $45,000. Form 1099-DIV: box 1a ordinary dividends $2,000, box 1b qualified dividends $1,500, box 2a
capital gain distributions $1,000, of which box 2d collectibles (28%) gain $400. No sales. 2024 return: Form 1040
line 11 $40,000, line 14 $14,600; Schedule D line 7 $0, line 15 −$6,000, line 21 ($3,000).

**R9.** Wages $150,000. Interest $3,000 (Form 1099-INT box 1). Ordinary dividends $2,000, none qualified, no capital
gain distributions. Paid in 2025: state income tax $9,000, home mortgage interest on Form 1098 $12,000 (an ordinary
acquisition mortgage within the limits), and investment interest (margin interest) $4,000. The 2024 Form 4952 line 7
was $2,500. No other investment income or expenses; no election on Form 4952 line 4g. No capital loss carried from
2024 (the 2024 Schedule D line 21 was not a loss).

**R10.** Wages $250,000 (Medicare wages $250,000). Interest $20,000. In 2025 sold stock held 6 months: proceeds
$14,000, basis $10,000 (box A). 2024 return: Form 1040 line 11 $240,000, line 14 $14,600; Schedule D line 7 −$10,000,
line 15 $0, line 21 ($3,000). The filer figured no net investment income tax adjustment on the 2024 Net Gains and
Losses Worksheet (no amount on its line 2(i)).

## What to report

For each return, in dollars and cents, give:

- **Capital Loss Carryover Worksheet (2024 to 2025)** lines 1 to 13, or "skipped" for a line the worksheet tells you
  to skip, or "not used" if the worksheet does not apply. (R9: not used.)
- **Schedule D** lines 6, 7, 13, 14, 15, 16, 18 and 21 (signed: a loss negative; "skipped" where the form skips it).
- **Form 1040** lines 7a, 9, 11a (adjusted gross income), 12e, 15 and 16 (the tax).
- **The carryovers from 2025 to 2026**, short-term and long-term, by the method i1040sd (Line 21) points to.
- R8 also: the 28% Rate Gain Worksheet lines 4 to 7 and Schedule D line 18.
- R9 also: Form 4952 lines 1 to 8 and Schedule A lines 9 and 17.
- R10 also: Form 8960 lines 1, 5a, 8, 12, 13, 15 and 17, and Form 8959 line 18.

For every value, a short derivation naming the line or worksheet and page it comes from. Where the text is
ambiguous, say so and give the reading you used.
