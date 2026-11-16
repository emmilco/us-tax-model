# Completeness review, release rerun (lane xrr, family rsche): adjudication of 17 claims

Forms: `rental` (11 claims) and `royalty` (6). These are the only forms of the family whose completeness subject changed
after the xint integration; the other forms' items were already ruled. Tree: `.claude/worktrees/xint` (B1 plus
expansion). The rulings are in `/tmp/xrr/frag/rsche.completeness.json` (keys `unruled:<form>#1.<n>`, each with its form's
current `subject_sha`), for the lead to merge; `rulings.json` was not edited. `python3 /tmp/xrr/xrr.py merge` (no
`--write`) gives no REFUSED line for these keys. One note: rental#1.6 cites a pending placeholder, so it fails the gate
until the bug is numbered.

Adjudicated by claude-opus-5-5 (judgment). Every quoted sentence was found in `sources/2025/*.cols.txt` (a script check
of each sentence against its document). Encoding claims were checked against `forms/2025/rental.yaml`, `royalty.yaml`,
`sche.yaml`, `f8582.yaml`, `household.yaml` and `scope.yaml` and the help in `interview/2025/questions.yaml`. Two
witnesses were evaluated on copies of `x1sche.f2.small_loss_exception` under `/tmp/xrr/rsche/` (resolved with the
fixture defaults):
- with `sche.re_pro` true, `sche.line26` and `f1040.line11a` are refused at `sche.re_pro`;
- with `f1040.status` mfs, `household.married_dec31` true and `household.mfs_living` together_late, `f8582.exception`
  is true, `f8582.line5` is $75,000, `f8582.line8` is $12,500 and `f8582.line9` is $213.20, and `sche.line26` is
  -$213.20. The rules allow no special allowance here, so BUG-0836 is still live.

**What changed since xrel.** For these claims, nothing in the rental or royalty questions changed. The xint changes to
these forms were the `rental.has_2025` -> `rental.needs_4562` rename and the merge of `rental.part_home`. Every xrel
entry these claims cite is still open (no Fix field): BUG-0775, -0776, -0778, -0779, -0781, -0836, -0889 and -0922. The
xrel rulings were used as leads and checked again against the current lines.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| rental | 11 | 9 | 1 | 1 | 0 | 0 |
| royalty | 6 | 5 | 0 | 0 | 1 | 0 |
| **Total** | 17 | 14 | 1 | 1 | 1 | 0 |

- **Existing entries cited, not filed again:** 13 of the 14 real gaps (all but rental#1.6).
- **New:** two low entries from rental claims. Prepaid interest and points are taken in the year paid (-01). A
  co-owner renting under a shared equity financing agreement is counted as personal use (-02). The ruling for the
  second claim cites the medium entry BUG-0775.
- **Separate returns.** rental#1.1's married-filing-separately part relies on the B1 encoding. Separate returns are now
  supported, and nothing refuses or zeroes the special allowance when the spouses lived together (BUG-0836, checked by
  eval above).

## Rulings

| Claim | Item | Class | Line, gate or bug | Note |
|---|---|---|---|---|
| rental#1.1 | `part4` | real gap (medium) | BUG-0836 | Real estate professional refused at `sche.re_pro` (eval). MFS lived-together still gets the allowance (eval). |
| rental#1.2 | `stay7_if_short` | real gap (low) | BUG-0779 | Investment-incidental, business-hours and partnership-use exceptions not screened; `services` and `self_rental` reach part of the rest. |
| rental#1.3 | `kind` | real gap (low) | BUG-0779 | Dealer property not screened. Crop-share farm rental is out of scope at `scope.farm` (its help names it), through `scope.schedule1`. |
| rental#1.4 | `rents` | covered | `rental.rents` | In-kind rent is rent received; services other than repairs not named (a wording low, not filed). |
| rental#1.5 | `days_personal` | real gap (medium) | BUG-0775 | Main-home days left out of the division (BUG-0775). Sale-ended rental: BUG-0772. Shared equity co-owner: BUG-0926. The family fair-rent main home is covered by the `personal_any` help. |
| rental#1.6 | `line12` | real gap (low) | BUG-0925 | Prepaid interest and points not excluded or spread. Form 8990 not a gap: i8990 small business exclusion; QBI business refused at `sche.qbi_business`. A co-borrower's Form 1098 goes to `amt13`. |
| rental#1.7 | `amt10` | real gap (low) | BUG-0776 | Capitalized legal fees not excluded. |
| rental#1.8 | `amt17` | out of scope | `rental.part_home` | Part of the filer's home is refused. Otherwise the question asks for the rental's utilities. |
| rental#1.9 | `amt19` | real gap (low) | BUG-0776 | Capital purchases not excluded. Own labor excluded by "paid". No Form 8826 credit is computed, so the return cannot take both. |
| rental#1.10 | `not_at_risk` | real gap (low) | BUG-0781 | Guarantees, interested-party loans, related or fee-receiving lenders. |
| rental#1.11 | `line20` | real gap (low) | BUG-0778 | A Worksheet 5-1 carryover into a year without home use is neither asked nor refused. |
| royalty#1.1 | `line21` | real gap (low) | BUG-0889 | No at-risk question or refusal for royalties. |
| royalty#1.2 | `business` | real gap (low) | BUG-0889 | NIL sponsorship or service income not asked. |
| royalty#1.3 | `line4` | real gap (low) | BUG-0889 | Patent transfer, coal and iron ore not screened. |
| royalty#1.4 | `line10` | real gap (low) | BUG-0922 | Capitalized legal fees not excluded. |
| royalty#1.5 | `line19` | real gap (low) | BUG-0922 | Capital costs not excluded. A residential phone base rate is a residual of the same wording, not filed. |
| royalty#1.6 | `expenses_any` | presentation | none | Line A is a checkbox about Forms 1099; no amount. |

## Pending bugs filed (`bug_pending/xrrsche-NN.md`)

| Id | Severity | Title | Claims |
|---|---|---|---|
| BUG-0925 | low | rental interest questions take prepaid interest and points in the year paid | rental#1.6 |
| BUG-0926 | low | rental personal-use days: a co-owner renting under a shared equity financing agreement is counted as personal use | rental#1.5 |

Also cited: BUG-0772 (low), BUG-0775 (medium), BUG-0776 (low), BUG-0777 (low), BUG-0778 (low), BUG-0779 (low),
BUG-0781 (low), BUG-0836 (medium), BUG-0889 (low) and BUG-0922 (low).
