# Completeness review, release round (lane xrel, family k1p): adjudication of 24 claims

Forms: `f7203` (6 claims), `f8582` (8), `k1p` (8), `f8995` (1), `qbi` (1). Tree: `.claude/worktrees/xint` (B1 plus
expansion). The rulings are in `/tmp/xrel/frag/k1p.completeness.json` (keys `unruled:<form>#1.<n>`, each with its
form's current `subject_sha`), for the lead to merge; `rulings.json` was not edited. `python3 /tmp/xrel/xrel.py merge`
(no `--write`) accepts every key: no REFUSED line, and 12 notes, one for each real gap, because its bug is still a
pending entry (xrelk1p-NN; numbered BUG-0836 to BUG-0849 in order, 01 to 14, at integration). Those 12 fail the gate until the bugs are numbered.

Adjudicated by claude-opus-5-5 (judgment). Every quote was checked against `sources/2025/*.txt`, and every encoding
claim against `forms/2025/*.yaml`, `interview/2025/questions.yaml` and evaluations. Witnesses are copies of fixture
cases with one to three inputs changed, resolved with `main.js fixture-inputs` and evaluated with
`main.js --year 2025 eval --json`. They are in `/tmp/xrel/k1p/` (`W*.json`, `fk3_repro.json`).

**Reachability.** Every K-1 still refuses at `scope.k1`, through `scope.schedule1`. No return-level line reads
`person.k1p_*` or `person.k1s_*` yet (DECISIONS.md, x2-k1s "Scope of the lane"; the k1p wiring contract). So the
k1p and f7203 gaps are latent: they become live when the integration lane lifts `scope.k1`. Form 8582 is reachable now
through Schedule E Part I rentals.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f7203 | 6 | 2 | 0 | 3 | 1 | 0 |
| f8582 | 8 | 3 | 1 | 4 | 0 | 0 |
| k1p | 8 | 7 | 1 | 0 | 0 | 0 |
| f8995 | 1 | 0 | 1 | 0 | 0 | 0 |
| qbi | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | 24 | 12 | 3 | 7 | 1 | 1 |

- **Introduced by married filing separately (B1).** f8582#1.3 to #1.5. Married filing separately is now in scope.
  f8582 applies the separate-return amounts ($12,500, $75,000, $50,000), but it never tests whether the spouses lived
  together. A separate filer who lived with the spouse at any time gets the special allowance and the filing
  exception. The rules deny both (i8582 p. 10, Part II caution; p. 4; p. 1).
- **Repeats.** f8995#1.1 and qbi#1.1 repeat earlier claims. Each was rechecked on the current lines and keeps the
  same class (covered `qbi.dividends`; wrong).
- **Premise now false.** The brief warns that "a separate return is refused" no longer holds. No claim in this family
  relied on `s3.mfs`.

## Rulings

| Claim | Item | Class | Line, gate or bug | Note |
|---|---|---|---|---|
| f7203#1.1 | `required` | out of scope | `k1s.basis_carry` | The basis carryover is refused by `k1s.basis_carry` and a loan repayment (box 16 code E) by `k1s.box16ef_if_16`. Both are asked on every K-1. |
| f7203#1.2 | `a47` | out of scope | `k1s.basis_carry` | Column (b) is refused, as the f7203 note says. |
| f7203#1.3 | `a47` | out of scope | `k1s.box11_12` | Lines 39 to 46 take boxes 11 and 12, 16 F and 17 R, and each of these is refused. The claim that "nothing is noted" is wrong: the form note states it. |
| f7203#1.4 | `line2` | real gap (low) | BUG-0848 | The help covers inherited and gifted stock, and the line 1 help covers the first year. Property contributed (section 351, 357(c)) and stock received for services are not covered. |
| f7203#1.5 | `loans` | real gap (low) | BUG-0848 | The help excludes guaranteed loans without the exception for payments made under the guarantee. |
| f7203#1.6 | `one` | presentation | — | Form 7203 is one entry per K-1, so each spouse with a K-1 gets one. Item D is a checkbox. |
| f8582#1.1 | `line1b_rental` | out of scope | `sche.re_pro` | Each case is refused: `rental.ws51`, `stay7_if_short`, `services`, `under_tenth`, and `scope.k1` for limited partners. |
| f8582#1.2 | `line1a_rental` | out of scope | `sd.business_property_if_sold` | A sale of rental property goes on Form 4797, which is refused. |
| f8582#1.3 | `exception` | real gap (medium) | BUG-0836 | Lived-apart test missing. The separate-return limits are applied through the parameters. |
| f8582#1.4 | `line5` | real gap (medium) | BUG-0836 | $75,000 is applied (`f8582.phaseout_end` mfs). The together case is not handled. |
| f8582#1.5 | `line8` | real gap (medium) | BUG-0836 | $12,500 is applied (`f8582.special_max` mfs). Nothing denies the allowance to spouses who lived together. |
| f8582#1.6 | `line6` | out of scope | `sb.unsupported_if_income` | Form 8815 is refused there, and employer adoption benefits at `scope.adoption_benefits`. Dispositions are refused. |
| f8582#1.7 | `line9` | out of scope | — | CRD: the `f8582.line3` note says none can arise after 2009. |
| f8582#1.8 | `p7_C` | covered | `rental.allowed` | The per-activity Parts VII and VIII are on the rental entries (`rental.p7c`, `rental.allowed`, `rental.carryforward`). |
| f8995#1.1 | `line6` | covered | `qbi.dividends` | The question excludes shares held 45 days or less and amounts the filer must pay over. Repeat. |
| qbi#1.1 | `eligible` | wrong | — | Schedule C QBI is computed (`sc.qbi` less `sc.qbi_ded`). The former-employee presumption is refused at `sc.special`, and current suspensions at `sc.passive`, `sc.at_risk` and `s1.ebl`. Repeat. |
| k1p#1.1 | `col_i` | real gap (medium) | BUG-0841 | No screen for unreimbursed partnership expenses, interest to buy the interest, or basis and at-risk carryovers. Form 461 is not applied to K-1 losses: BUG-0842. |
| k1p#1.2 | `box14a` | real gap (medium) | BUG-0841 | Box 14 A reaches Schedule SE without the reduction for unreimbursed partnership expenses. |
| k1p#1.3 | `col_k` | real gap (low) | BUG-0841 | A 2024 fuel tax credit from the partnership is not added back as income. |
| k1p#1.4 | `b1_passive` | real gap (low) | BUG-0844 | Oil and gas working interests, and significant participation income, are not handled. |
| k1p#1.5 | `hours500` | covered | `k1p.work` | The help excludes investor work. The anti-abuse prong turns on intent and is not filed. |
| k1p#1.6 | `b2_net_loss` | real gap (medium) | BUG-0843 | `sche.re_pro` does not reach K-1 box 2 (W: fk3_repro). |
| k1p#1.7 | `box20z` | real gap (medium) | BUG-0842 | The QBI share of a held-back loss (D-K7) is not encoded. It is in the wiring contract. |
| k1p#1.8 | `one` | real gap (low) | BUG-0839 | No question on a fiscal-year partnership. Participation is asked for calendar 2025. |

## Witnesses

| Witness | Base and change | Result |
|---|---|---|
| W1 | `x1sche.f2.small_loss_exception` (single) | `f8582.exception` true, line 8 $25,000, line 9 $213.20 |
| W2 | W1, `f1040.status` mfs, `married_dec31` true, `mfs_living` together_late | `f8582.exception` true, line 5 $75,000, line 8 $12,500, line 9 $213.20, `sche.line26` −$213.20 (should be held back) |
| W3 | W2 with `mfs_living` apart_all_year | same as W2 (correct for lived apart) |
| fk3_repro | `x2k1p.fk3_limited_rental_loss`, `sche.re_pro` true | `sche.line26` refusal; `f1040.line24` computed; `k1p.p5_loss` $12,000 |
| W4 | `x2k1p.test5_five_of_ten`, `k1p.work` false | `k1p.material` false, `col_h` $40,000 (base: `col_k` $40,000), used for screens |

## Pending bugs cited

BUG-0836 (medium), -04 (low), -06 (medium), -07 (medium, latent), -08 (medium, latent), -09 (low),
-13 (low). The screen and false-no adjudication files the others (`reviews/2025/screens/adjudication/xrel-k1p.md`).
