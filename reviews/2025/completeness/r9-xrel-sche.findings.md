# Completeness review, release round (lane xrel, family sche): adjudication of 18 claims

Forms: `k1s` (7 claims), `royalty` (6), `rprop` (2), `sche` (3). Tree: `.claude/worktrees/xint` (B1 plus expansion). The
rulings are in `/tmp/xrel/frag/sche.completeness.json` (keys `unruled:<form>#1.<n>`, each with its form's current
`subject_sha`), for the lead to merge; `rulings.json` was not edited. `python3 /tmp/xrel/xrel.py merge` (no `--write`)
accepts every key: no REFUSED line, and 13 notes, one for each real gap, because its bug is still a pending
placeholder. Those 13 fail the gate until the bugs are numbered.

Adjudicated by claude-opus-5-5 (judgment). Every quoted sentence was found in `sources/2025/*.txt` (a script check of
each sentence against its document). Every encoding claim was checked against `forms/2025/*.yaml` (expressions and
refusals read) and the help in `interview/2025/questions.yaml`. No witness was evaluated. The k1s claims are latent, and
the royalty, rprop and sche findings turn on which questions and refusals exist, not on computed amounts.

**Reachability.** Every K-1 still refuses at `scope.k1` through `scope.schedule1`. No return-level line reads the
`person.k1s_*` totals. So the k1s gaps are latent, as the k1p fork found for k1p. The royalty, rprop and sche forms are live.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| k1s | 7 | 6 | 1 | 0 | 0 | 0 |
| royalty | 6 | 5 | 0 | 0 | 1 | 0 |
| rprop | 2 | 1 | 0 | 1 | 0 | 0 |
| sche | 3 | 1 | 2 | 0 | 0 | 0 |
| **Total** | 18 | 13 | 3 | 1 | 1 | 0 |

- **Introduced by married filing separately (B1).** k1s#1.2 and sche#1.3. Form 8582 applies the separate-return
  amounts but has no lived-together test. This is the existing pending entry BUG-0836, cited here and not
  filed again.
- **Siblings of the k1p findings.** k1s#1.1, #1.6 and #1.7 match the k1p entries -08, -04 and -07. They are filed
  separately for k1s because those entries name only `k1p.yaml`.
- **Existing entry.** royalty#1.4 is BUG-0922 (pending; its proposed fix has not been made).
- **Wrong premises in the claims.** sche#1.1 to #1.3 say Schedule E asks nothing about personal use, days or passive
  limits. Those are on the `rental` entries that `sche` sums. Only the separate-return part of #1.3 stands.

## Rulings

| Claim | Item | Class | Line, gate or bug | Note |
|---|---|---|---|---|
| k1s#1.1 | `p2_loss` | real gap (medium) | BUG-0882 | Box 2 always passive; `sche.re_pro` does not reach the K-1. Sibling of BUG-0843. Latent. |
| k1s#1.2 | `part4` | real gap (medium) | BUG-0836 | No lived-together test in `k1s.part4` or Form 8582. Latent for the K-1; live on Schedule E rentals. |
| k1s#1.3 | `p4_prior_raw` | real gap (low) | BUG-0883 | No counterpart of `rental.prior_not_active`. Latent. |
| k1s#1.4 | `p3_loss` | real gap (medium) | BUG-0882 | Personal-use dwelling and trading not screened. Latent. |
| k1s#1.5 | `work` | covered | `k1s.work` | The help excludes investor work; the anti-abuse prong turns on intent and is not filed. |
| k1s#1.6 | `box1` | real gap (low) | BUG-0884 | No question on a fiscal-year corporation. Sibling of BUG-0839. Latent. |
| k1s#1.7 | `col_i` | real gap (medium) | BUG-0885 | `s1.ebl_total` takes no K-1 loss. Sibling of BUG-0842. Latent. |
| royalty#1.1 | `loss` | real gap (low) | BUG-0889 | No at-risk question for royalties (rental has one). |
| royalty#1.2 | `line4` | real gap (low) | BUG-0889 | Patent and coal or iron ore royalties not screened; the Form 8873 part is not filed. |
| royalty#1.3 | `business` | real gap (low) | BUG-0889 | NIL sponsorship or service income not asked. |
| royalty#1.4 | `amt10` | real gap (low) | BUG-0922 | Existing pending entry; its proposed fix is not yet made. |
| royalty#1.5 | `amt19` | real gap (low) | BUG-0889 | Car and travel costs not refused (rental refuses them); labor and capital costs under BUG-0922. |
| royalty#1.6 | `expenses_any` | presentation | — | Line A is a checkbox; no amount. |
| rprop#1.1 | `basis` | out of scope | `rental.part_home` | Part of a home is refused; later title costs are a basis change refused at `rprop.screen`. |
| rprop#1.2 | `screen` | real gap (low) | BUG-0891 | An earlier exchange keeps the old recovery period; a 2025 exchange refuses at `sd.like_kind`. No short year on a calendar-year return. |
| sche#1.1 | `line23a` | covered | `rental.excluded` | Rentals under 15 days, personal property, services and home use are handled on the rental entries. Services received as rent is a rare residual, not filed. |
| sche#1.2 | `line23e` | covered | `rental.div19` | Expenses divided by days (`rental.div5` to `div19`); home use refused at `rental.ws51`. |
| sche#1.3 | `rent_loss` | real gap (medium) | BUG-0836 | Passive limits are computed on the rental entries; only the separate-return lived-together test is missing. |

## Pending bugs filed (`bug_pending/xrelsche-NN.md`)

| Id | Severity | Title | Claims |
|---|---|---|---|
| BUG-0882 | medium (latent) | k1s: box 2 and box 3 are always passive (real estate professional, personal-use dwelling, trading) | k1s#1.1, #1.4 |
| BUG-0883 | low (latent) | k1s: held-back box 2 loss with box 2 blank goes to Part V; loss-year active participation; prior passive credits | k1s#1.3 |
| BUG-0884 | low (latent) | k1s: fiscal-year S corporation | k1s#1.6 |
| BUG-0885 | medium (latent) | k1s: losses not in the excess business loss limit | k1s#1.7 |
| BUG-0889 | low | royalty: at-risk loss, capital-gain royalties, business royalties, depreciation, car and travel | royalty#1.1, #1.2, #1.3, #1.5 |
| BUG-0891 | low | rprop: carryover basis from a like-kind exchange or involuntary conversion | rprop#1.2 |

Also cited: BUG-0836 (medium) and BUG-0922 (low). The screen and false-no adjudication files
-05, -06, -07, -09 and -11 (`reviews/2025/screens/adjudication/xrel-sche.md`).
