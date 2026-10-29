# Twenty 2025 returns with Marketplace coverage, to work by hand from the IRS text

Each return is for tax year 2025, on Form 1040, with Form 8962. Unless a return says otherwise:

- Filers are 40 years old, not blind, U.S. citizens with valid SSNs, who lived all year in one of the 48 contiguous
  states. Nobody can claim them as dependents. Everyone enrolled is lawfully present; nobody was offered or covered by
  a QSEHRA or an individual coverage HRA; every premium was paid on time; nobody married, divorced or separated in
  2025; no policy covered anyone outside the tax family.
- Income is wages only (Form W-2 box 1), with no other income, adjustments or tax-exempt interest. Children listed are
  qualifying children claimed as dependents who lived with the filer all year and are not required to file a return.
- "Same every month" means the Form 1095-A shows coverage in all 12 months with the stated column A and column B amount
  in every month; column C is given as the line 33 annual total. Otherwise the months are listed. Column B is correct as
  printed. Amounts are whole dollars.
- Head of household returns qualify for that status.

Work from the archived 2025 documents under `sources/2025/` only (pages split by form-feed characters):
`f8962.cols.txt` (also `f8962.txt`), `i8962.cols.txt` (also `i8962.txt`: Worksheets 1-1, 1-2 and 2, Tables 1-1 to 1-3,
2 and 5), `f1095a.cols.txt`, `i1095a.cols.txt`, `p974.cols.txt`, `i1040gi.cols.txt` (Social Security Benefits Worksheet,
Schedule 2 line 1a, Schedule 3 line 9), `f1040s2.cols.txt`, `f1040s3.cols.txt`, `rp-2024-40.cols.txt`.

## The returns

- **P1.** Single. Wages $40,000. One Form 1095-A, same every month: column A $500, column B $450; line 33C $3,500.
- **P2.** Single. Wages $25,000. One form, same every month: A $400, B $420; line 33C $4,200.
- **P3.** Single. Wages $55,000. One form, same every month: A $600, B $550; line 33C $6,000.
- **P4.** Single. Wages $70,000. One form, same every month: A $700, B $650; line 33C $3,000.
- **P5.** Head of household with two children (ages 6 and 9). Wages $50,000. One form, same every month: A $1,100,
  B $1,000; line 33C $9,000.
- **P6.** Married filing jointly with two children (ages 5 and 8). Wages $50,000 and $40,000. One form, same every
  month: A $1,500, B $1,400; line 33C $15,000.
- **P7.** Single. Wages $12,000. One form, same every month: A $450, B $430; line 33C $5,000. When the filer enrolled,
  the Marketplace estimated that household income would be at least 100% of the federal poverty line.
- **P8.** As P7, except the Marketplace did not estimate household income of at least 100% of the poverty line (its
  estimate was below 100%).
- **P9.** Single. Wages $35,000. One form: no coverage January to March; April to December each month A $480,
  B $460, C $300.
- **P10.** Married filing jointly, no children. Wages $45,000 and $30,000. One form: January to June each month A $900,
  B $850, C $500; July to December each month A $900, B $950, C $550.
- **P11.** Single. Wages $38,000. Two Forms 1095-A from the same state's Marketplace (two policies covering the
  filer), each same every month: form 1 A $350, B $500, line 33C $2,400; form 2 A $150, B $500, line 33C $600.
- **P12.** Single. Wages $38,000. Two Forms 1095-A from two states (the filer moved): form 1, January to May each month
  A $500, B $480, C $300, nothing after May; form 2, nothing January to May, June to December each month A $520,
  B $510, C $320.
- **P13.** Single. Wages $30,000. Lived in Alaska all year. One form, same every month: A $650, B $640; line 33C $6,000.
- **P14.** Head of household with one child (age 10). Wages $32,000. Lived in Hawaii all year. One form, same every
  month: A $800, B $760; line 33C $7,800.
- **P15.** Head of household with one child (age 17) whom the filer claims and who is required to file a 2025 return
  because of their income; the child's modified AGI is $8,000. Filer's wages $42,000. One form, same every month:
  A $900, B $880; line 33C $8,000.
- **P16.** Single. Wages $28,000, tax-exempt interest $1,200 (Form 1099-INT box 8) and social security benefits $9,000
  (Form SSA-1099 box 5). One form, same every month: A $520, B $500; line 33C $4,000.
- **P17.** Single. Wages $30,000. One form, same every month: A $380, B $400; line 33C $0 (no advance payments).
- **P18.** Single. Wages $60,240. One form, same every month: A $600, B $580; line 33C $1,000.
- **P19.** Single. Wages $60,347. One form, same every month: A $800, B $780; line 33C $2,000.
- **P20.** Married filing jointly with seven children (ages 2, 4, 6, 8, 10, 12, 14). Wages $60,000 and $40,000. One
  form, same every month: A $2,200, B $2,100; line 33C $20,000.

## What to report

For each return, in dollars and cents (Rates as decimals): Form 8962 lines 1, 2a, 2b, 3, 4, 5, 7, 8a, 8b, line 10
("yes" or "no"), and line 11 columns (a) to (f) when line 10 is yes, or lines 12 to 23 columns (a) to (f) when it is
no; lines 24 to 29; Schedule 3 line 9; Schedule 2 line 1a. Use "skipped" or "blank" where the form or instructions say
to skip a line or leave it blank, and say why. For every value, a short derivation naming the line, worksheet or table
and page. Where the text is ambiguous, say so and give the reading you used.
