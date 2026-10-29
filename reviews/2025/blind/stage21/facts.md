# Ten 2025 returns with early retirement distributions, to work by hand from the IRS text

Each return is for tax year 2025, on Form 1040. Unless a return says otherwise:

- Filers are 40 years old at the end of 2025 (born in 1985), not blind, U.S. citizens with valid SSNs (valid for
  employment), who lived all year in one of the 48 contiguous states. Nobody can claim them as dependents, and nobody
  does. Nobody married, divorced or separated in 2025. There are no dependents. Single filers do not qualify as head of
  household.
- Income is wages (Form W-2 box 1) and the distributions listed, with no other income, adjustments, tax-exempt
  interest or excluded foreign or Puerto Rico income. The standard deduction is taken. There are no credits.
- Each distribution is reported on its own 2025 Form 1099-R with the box 7 code given. Box 2a (taxable amount) equals
  box 1 (gross distribution); box 5 is empty. For an IRA, the IRA/SEP/SIMPLE box is checked. Nobody ever made
  nondeductible contributions to any IRA or has any other basis in any account. Nothing was rolled over, converted,
  recharacterized or repaid, and no distribution was a qualified disaster recovery distribution, a corrective
  distribution, a plan loan offset, or from an annuity or modified endowment contract. No account is a Roth account.
  A "401(k)" is a distribution from an employer's 401(k) plan; the filer separated from that employer in 2024 at age
  39 unless the return says otherwise.
- Only the exceptions that a return states apply. Each distribution falls under at most one exception. Any statement
  that an exception applies means that its conditions in the instructions are met, except for the amount limits,
  which are for you to apply.
- Nobody has excess contributions to any IRA (for 2025 or an earlier year), Coverdell ESA, Archer MSA or ABLE
  account; nobody received a distribution from a Coverdell ESA, a qualified tuition program or an ABLE account; nobody
  failed to take a required minimum distribution. Nobody has an HSA unless the return says so.
- Ages are at the end of 2025. Where a birth date is given, use it.

Work from the archived 2025 documents under `sources/2025/` only (pages split by form-feed characters):
`f5329.cols.txt` (also `f5329.txt`), `i5329.cols.txt` (also `i5329.txt`; Who Must File, Part I and its exception
table, Part VII), `p590b.cols.txt` (chapter 1, Early Distributions, Additional 10% Tax and the exceptions), 
`f1099r.cols.txt` (the box 7 codes in the Instructions for Recipient), `f1040s2.cols.txt`, `i1040gi.cols.txt`
(Schedule 2 line 8 on p. 112; lines 4a to 5b; the Standard Deduction Chart; lines 11a to 16 and 22 to 24; the 2025
Tax Table on pp. 68 to 79), `f1040.cols.txt`, `f1040s1.cols.txt` (line 13, for E10), and for the HSA in E10
`f8889.cols.txt` and `i8889.cols.txt`.

## The returns

- **E1.** Single. Wages $41,000.00. A traditional IRA distribution of $5,123.45, code 1. A 401(k) distribution of
  $2,456.78, code 1. No exception applies to either.
- **E2.** Single. Wages $58,000. A distribution of $4,000 from her SIMPLE IRA, code S; she first participated in her
  employer's SIMPLE IRA plan on July 1, 2024. A distribution of $1,500 from her traditional IRA, code 1. No exception
  applies to either.
- **E3.** Single. Wages $47,000. Three distributions, each code 1:
  (a) traditional IRA, $7,000. In 2025 she paid $5,200 of tuition and required fees for her own graduate program at
  an eligible educational institution, with no scholarships, grants, employer assistance or other tax-free
  educational assistance; she claims no education credit or deduction. The higher education expense exception applies.
  (b) another traditional IRA, $6,000: the 2025 payment of a series of substantially equal periodic payments from that
  IRA, begun in 2023 under the required minimum distribution method and never modified.
  (c) 401(k), $4,000. No exception applies.
- **E4.** Single (a man). Wages $55,000. Four distributions, each code 1:
  (a) traditional IRA, $7,000, and (b) another traditional IRA, $4,500, both used within 120 days to pay qualified
  acquisition costs of his first main home (he and his home meet the first-time homebuyer conditions). In 2021 he took
  a $1,200 IRA distribution to help his mother buy her first home, and it was excluded from the additional tax as a
  first-home distribution on his 2021 return; he has no other earlier first-home distributions.
  (c) traditional IRA, $4,000, and (d) 401(k) (an in-service distribution; he still works there), $3,500, both taken
  within one year after the birth of his daughter on March 2, 2025, as qualified birth distributions for her. She is
  his only child. She lives all year with her mother, to whom he is not married, and he does not claim her.
- **E5.** Single. Wages $48,000. Four distributions, each code 1:
  (a) traditional IRA, $6,000, and (b) 401(k) (in-service; she still works there), $5,500, both eligible
  distributions to a domestic abuse victim (the abuse by her former domestic partner was in February 2025; both were
  received within the following year). Her IRA was worth more than $30,000 and her 401(k) account more than $50,000
  throughout 2025.
  (c) traditional IRA, $700, received in April, and (d) 401(k), $600, received in November: she requested each as an
  emergency personal expense distribution for unforeseeable family emergency expenses. She took no emergency personal
  expense distribution in 2022, 2023 or 2024.
- **E6.** Single. Wages $38,000. A traditional IRA distribution of $9,000, code 1, used to pay her medical bills. Her
  2025 unreimbursed medical and dental expenses that would qualify for the medical deduction on Schedule A total
  $11,000. The medical expense exception applies, within its limit.
- **E7.** Married filing jointly. Wages $60,000 (the taxpayer) and $45,000 (the spouse). The taxpayer: a traditional
  IRA distribution of $5,000, code 1. The spouse: a traditional IRA distribution of $3,000, code 1, and a 401(k)
  distribution of $4,000, code 1 (she separated from that employer in 2024 at age 39). The two IRA distributions were
  used to pay the couple's medical bills, and the medical expense exception applies to each of them, within its limit;
  no exception applies to the 401(k) distribution. The couple's 2025 unreimbursed medical and dental expenses that
  would qualify for the medical deduction on Schedule A total $18,000.
- **E8.** Single, born May 20, 1964. Wages $70,000. A traditional IRA distribution of $15,000 received in August 2025.
  The IRA custodian put code 1 in box 7 by mistake.
- **E9.** Married filing jointly. The taxpayer, aged 45, has been totally and permanently disabled since 2023 (he
  cannot do any substantial gainful activity; a physician has determined that his condition is of long, continued and
  indefinite duration) and had no wages. He received a traditional IRA distribution of $12,000, code 3. The spouse,
  aged 40: wages $80,000 and a traditional IRA distribution of $3,000, code 1; no exception applies to it.
- **E10.** Single. Wages $65,000. Self-only high deductible health plan coverage every month of 2025, no other health
  coverage, not enrolled in Medicare. During 2025 she contributed $5,800 to her HSA herself (not through her employer);
  her employer contributed nothing, and nothing was contributed for 2025 in 2026. She received $4,900 of HSA
  distributions in 2025 (Form 1099-SA), all used for qualified medical expenses. She did not withdraw any excess
  contribution. Her HSA was worth $910 on December 31, 2025. She also received a traditional IRA distribution of
  $2,000, code 1; no exception applies to it.

## What to report

For each return, in dollars and cents: for each person with a distribution or an HSA excess, Form 5329 lines 1 to 4
(and the exception number entered on line 2), and for E10 lines 47 to 49; whether that person files Form 5329;
Schedule 2 line 8 and whether its box ("If not required, check here") is checked; Form 1040 lines 4b, 5b, 11a, 15, 16,
22, 23 and 24. Use "not filed" where a form is not filed and "blank" where the form or instructions say to leave a line
blank, and say why. For every value, a short derivation naming the line, worksheet or table and page. Where the text is
ambiguous, say so and give the reading you used.
