# Screen and false-no adjudication, release round (lane xrel, family sche)

Units: the screens and gates of `k1s`, `royalty`, `rprop` and `sche` sampled for the release. Tree:
`.claude/worktrees/xint` (B1 plus expansion). The rulings are in `/tmp/xrel/frag/sche.screens.json` and
`/tmp/xrel/frag/sche.false_no.json`. Keys are `unruled:<unit>#1`, each with its unit's current `subject_sha` and one entry
per finding, for the lead to merge. `rulings.json` was not edited. `python3 /tmp/xrel/xrel.py merge` (no `--write`) gives no
REFUSED line for these keys.

Adjudicated by claude-opus-5-5 (judgment). Every encoding claim was checked against `forms/2025/*.yaml` (gate
expressions read: `k1s.work_if_b1`, `k1s.active_if_b2`, `k1s.part4`, `k1s.p5_b2_prior`, `k1s.b2_prior_if_any`,
`royalty.line16`) and the help in `interview/2025/questions.yaml`. No witness was evaluated. The k1s defects are
latent, and the live royalty defect follows directly from a `choose` on `royalty.expenses_any`.

**Reachability.** Every K-1 still refuses at `scope.k1`, so the k1s defects are latent until the integration lane wires
the K-1 totals. The royalty, rprop and sche units are live.

**Patterns, each ruled once in the tables and filed once:**
- "Show an amount" read against a code printed with `*` STMT, or against items on a continuation statement. Code V is
  usually reported this way. Also a Schedule K-3 received on request. Defect, low (-06; sibling of BUG-0846).
- Items of the trade or business outside box 1 (boxes 9 to 12, box 13 other codes, box 17 other codes) are refused at
  their own ticks, and several activities at `k1s.multi`. Covered.
- A real estate professional's box 2: the participation questions are reached only through box 1, and `sche.re_pro` does
  not reach the K-1. Defect, medium (-01).
- Fiscal-year corporations: the questions say "in 2025". Defect, low (-03).
- Spouse participation counts on any return, but the k1s questions name the spouse only on a joint return. Defect,
  medium (-05).
- A held-back box 2 loss with box 2 blank goes to Part V, because `k1s.active_if_b2` is false. A passive credit carried
  from 2024 is not screened. Defect, low (-02).
- `k1s.not_at_risk` asks only about borrowed money: property, capital contributions, a stop-loss on the filer's own money,
  and a lender with an interest who is not an owner are missed. Defect, low (-07).
- `royalty.expenses_any` asks "Did you pay any costs". Since line 4 became gross (BUG-0921), taxes the payer
  withheld are answered No, and line 16 is zero. Defect, medium, live (-09).
- `royalty.business` names four trades and only oil or gas working interests. Royalty depreciation has no line.
  Defect, low (-08).
- `rprop.screen` does not name property from a like-kind exchange or involuntary conversion. Defect, low (-10).
- `sche.re_pro` does not say which work counts. Defect, low (-11).

Classes as group 9: covered, accepted WIDE, model error, out of scope, presentation (wording only, or a rare case not
filed), defect, and open residual. The bug numbers in the tables are the pending suffixes `xrelsche-NN` (and
`BUG-0922` for the existing entry).

## Screen reviews

Samples: 35. Findings: 108. Classes: defect 38, presentation 31, covered 19, accepted WIDE 12, model error 8.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `k1s.basis_carry#1` | 0: presentation; 1: presentation; 2: presentation; 3: accepted WIDE; 4: presentation | no gate defect; carryovers outside the filer's own earlier return are rare |
| `k1s.box10#1` | 0: defect (BUG-0887); 1: covered; 2: presentation | defect: a code with STMT can be answered as no amount (low) |
| `k1s.box11_12#1` | 0: defect (BUG-0887); 1: covered | defect: a code with STMT can be answered as no amount (low) |
| `k1s.box13_other#1` | 0: defect (BUG-0883); 1: model error | defect: a passive credit carried from 2024 is not screened (low) |
| `k1s.box14#1` | 0: defect (BUG-0887); 1: presentation | defect: a Schedule K-3 received on request is missed (low) |
| `k1s.box15#1` | 0: defect (BUG-0887); 1: presentation | defect: a code with STMT can be answered as no amount (low) |
| `k1s.box16ef#1` | 0: covered | no gate defect; debt basis is asked at f7203.loans |
| `k1s.box17_other#1` | 0: presentation; 1: model error | no gate defect |
| `k1s.box8_stmt#1` | 0: presentation | no gate defect |
| `k1s.box9#1` | 0: covered; 1: covered | no gate defect |
| `k1s.disposed#1` | 0: defect (BUG-0884); 1: presentation | defect: fiscal-year corporations (low) |
| `k1s.mp_other#1` | 0: presentation; 1: presentation; 2: accepted WIDE; 3: presentation | no gate defect |
| `k1s.multi#1` | 0: presentation | no gate defect |
| `k1s.not_at_risk#1` | 0: defect (BUG-0888); 1: defect (BUG-0888); 2: defect (BUG-0888); 3: defect (BUG-0888); 4: covered; 5: accepted WIDE; 6: presentation | defect: property, contributions, stop-loss on own money and non-owner interested lenders are missed (low) |
| `k1s.risk_carry#1` | 0: covered; 1: covered; 2: accepted WIDE; 3: presentation | no gate defect |
| `k1s.v_other#1` | 0: presentation; 1: presentation | no gate defect |
| `royalty.business#1` | 0: defect (BUG-0889); 1: defect (BUG-0889); 2: defect (BUG-0889); 3: presentation | defect: the business question names too few trades (low) |
| `royalty.depletion#1` | 0: presentation; 1: model error; 2: defect (BUG-0889) | no gate defect; depreciation of a royalty property is filed (low) |
| `rprop.screen#1` | 0: covered; 1: defect (BUG-0891); 2: presentation | defect: carryover basis from a like-kind exchange (low) |
| `sche.grouped#1` | 0: presentation; 1: accepted WIDE; 2: presentation; 3: covered | no gate defect |
| `sche.qbi_business#1` | 0: accepted WIDE; 1: presentation | no gate defect |
| `sche.re_pro#1` | 0: defect (BUG-0892); 1: defect (BUG-0892); 2: accepted WIDE; 3: accepted WIDE; 4: presentation; 5: presentation | defect: which work counts is not said (low) |
| `gate:k1s.active_if_b2#1` | 0: covered; 1: defect (BUG-0883); 2: model error; 3: presentation | defect: a held-back box 2 loss with box 2 blank (low) |
| `gate:k1s.box17_any#1` | 0: defect (BUG-0887); 1: defect (BUG-0887); 2: defect (BUG-0887) | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box17v_any_if_17#1` | 0: defect (BUG-0887) | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box1_any#1` | 0: covered; 1: covered; 2: defect (BUG-0887); 3: defect (BUG-0884) | defect: STMT and fiscal-year cases (low) |
| `gate:k1s.box2_any#1` | 0: defect (BUG-0883); 1: covered; 2: accepted WIDE | defect: a held-back box 2 loss with box 2 blank (low) |
| `gate:k1s.box8_any#1` | 0: defect (BUG-0887); 1: defect (BUG-0887) | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.has_loss#1` | 0: covered; 1: covered; 2: defect (BUG-0888); 3: accepted WIDE | defect: at-risk cases outside borrowed money (low) |
| `gate:k1s.other_ask#1` | 0: defect (BUG-0882); 1: defect (BUG-0884); 2: model error; 3: accepted WIDE | defect: real estate professional and fiscal-year cases (medium) |
| `gate:k1s.past_ask#1` | 0: defect (BUG-0882); 1: covered; 2: accepted WIDE | defect: a real estate professional's box 2 (medium) |
| `gate:k1s.prior_any#1` | 0: presentation; 1: model error | no gate defect |
| `gate:k1s.under500#1` | 0: covered; 1: defect (BUG-0882); 2: defect (BUG-0886); 3: defect (BUG-0884); 4: presentation; 5: model error | defect: real estate professional, separate-return spouse, fiscal year (medium) |
| `gate:k1s.work_if_b1#1` | 0: defect (BUG-0882); 1: covered; 2: defect (BUG-0884); 3: presentation; 4: model error | defect: real estate professional and fiscal-year cases (medium) |
| `gate:royalty.expenses_any#1` | 0: defect (BUG-0890); 1: presentation; 2: defect (BUG-0922) | defect: withheld taxes answered No (medium) |

## False-no reviews

Samples: 19. Findings: 81. Classes: defect 34, presentation 26, covered 14, model error 7.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:k1s.active_if_b2#1` | 0: presentation; 1: model error; 2: defect (BUG-0883); 3: presentation; 4: presentation | defect: a held-back box 2 loss with box 2 blank (low) |
| `gate:k1s.box13o_any#1` | 0: defect (BUG-0887); 1: presentation; 2: model error | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box16_any#1` | 0: defect (BUG-0887); 1: presentation; 2: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box16a_any_if_16#1` | 0: defect (BUG-0887); 1: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box16b_any_if_16#1` | 0: defect (BUG-0887); 1: presentation; 2: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box16c_any_if_16#1` | 0: defect (BUG-0887); 1: defect (BUG-0887); 2: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box16d_any_if_16#1` | 0: defect (BUG-0887); 1: presentation; 2: model error | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box17_any#1` | 0: defect (BUG-0887); 1: defect (BUG-0887); 2: defect (BUG-0887); 3: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box17v_any_if_17#1` | 0: defect (BUG-0887); 1: defect (BUG-0887); 2: defect (BUG-0887); 3: presentation | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.box1_any#1` | 0: covered; 1: defect (BUG-0882); 2: covered; 3: covered | defect: a real estate professional's box 2 (medium) |
| `gate:k1s.box2_any#1` | 0: defect (BUG-0883); 1: covered; 2: covered; 3: defect (BUG-0887) | defect: a held-back box 2 loss with box 2 blank (low) |
| `gate:k1s.box8_any#1` | 0: defect (BUG-0887); 1: defect (BUG-0887); 2: model error | defect: a code with STMT can be answered as no amount (low) |
| `gate:k1s.has_loss#1` | 0: covered; 1: covered; 2: covered; 3: covered; 4: defect (BUG-0888); 5: defect (BUG-0888); 6: presentation; 7: defect (BUG-0888) | defect: at-risk cases outside borrowed money (low) |
| `gate:k1s.other_ask#1` | 0: covered; 1: defect (BUG-0882); 2: defect (BUG-0886); 3: covered; 4: defect (BUG-0884); 5: presentation; 6: presentation | defect: real estate professional, fiscal year (medium) |
| `gate:k1s.past_ask#1` | 0: defect (BUG-0886); 1: presentation; 2: presentation; 3: covered; 4: defect (BUG-0884) | defect: separate-return spouse (medium) |
| `gate:k1s.prior_any#1` | 0: presentation; 1: model error; 2: presentation; 3: presentation; 4: model error | no gate defect |
| `gate:k1s.under500#1` | 0: covered; 1: defect (BUG-0882); 2: defect (BUG-0884); 3: covered; 4: presentation | defect: real estate professional, fiscal year (medium) |
| `gate:k1s.work_if_b1#1` | 0: defect (BUG-0884); 1: defect (BUG-0884); 2: defect (BUG-0882); 3: presentation; 4: model error | defect: fiscal year and a real estate professional's box 2 (medium) |
| `gate:royalty.expenses_any#1` | 0: defect (BUG-0890); 1: defect (BUG-0890); 2: presentation; 3: presentation; 4: presentation | defect: withheld taxes answered No (medium) |

## Pending bugs filed here

| Id | Severity | Title |
|---|---|---|
| BUG-0886 | medium (latent) | k1s: the participation questions count the spouse only on a joint return |
| BUG-0887 | low (latent) | k1s box questions: a code with * STMT can be answered as no amount; K-3 received on request |
| BUG-0888 | low (latent) | k1s.not_at_risk: property, contributions, stop-loss on own money, interested non-owner lenders |
| BUG-0890 | medium | royalty.expenses_any: taxes the payer withheld are answered No, so line 16 is zero |
| BUG-0892 | low | sche.re_pro: which work counts as a real estate business is not said |

Also cited from the completeness file: -01, -02, -03, -08 and -10, and the existing BUG-0922.
