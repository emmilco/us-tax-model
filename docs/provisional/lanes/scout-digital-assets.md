# Scout design: digital asset dispositions (Form 8949 boxes G–L, Form 1099-DA) and Schedule 1 line 8v — TY2025, federal

Scout: claude-opus-5-5, judgment, year 2025, jurisdiction us. Read-only, working from `.claude/worktrees/sweep-tasks` (HEAD 63a20efc).
Nothing in the repository was changed. No paid calls and no network.
Page numbers are PDF page indices of the archived file. The existing cites use the same convention; I checked this for i1040gi p. 92, Line 8v.
Labels: **[V]** = verified here by reading the archived source or the tree; **[I]** = inferred, not checked against an archived source.

---

## 0. Headline findings

1. **[V] The model change is small.** Only `sd.yaml` reads the `sales` collection (grep over forms/2025). The twelve-value enum `sales_box` already holds G to L (`params/2025.yaml`), and the bank already labels G to L (`interview/2025/questions.yaml` ~l.1061). What blocks the boxes today is one refusal entry: `sales.one` refuses on `sales.digital` (sales.yaml l.617–624). Also, every Schedule D line filter tests only A to F, which is the open task **T-003** ("widen the line filters' box tests to G to L"). Schedule D (2025) itself pairs the boxes: line 1b is "Box A or Box G", line 2 is "B or H", line 3 is "C or I", line 8b is "D or J", line 9 is "E or K", line 10 is "F or L". Lines 1a and 8a include "Form 1099-B or Form 1099-DA" (f1040sd p. 1).
2. **[V] Line 8v is one amount line.** `s1.digital_income` is a Bool that refuses through `s1.line8_other` (s1.yaml l.439–482, refused at `s1.line9`). Bringing 8v into scope follows the existing `jury_any → jury_pay → line8h` pattern (s1.yaml l.656–702).
3. **[V] Form 1040 page 1 asks a "Digital Assets" Yes/No question, and the model does not encode it** (f1040.txt l.32–33; there is no "digital" or "virtual" in forms/2025/f1040.yaml). Every return needs this answer, including one paid in crypto through a W-2. The gap exists today regardless of this lane (owner decision D1).
4. **[V] The 2026 drafts change nothing in this area's form text.** A word diff of 2025 against 2026 found only revision dates in f8949 and f1040sd, and only full sub-line numbering in f1040s1. The 2026 Form 1040 keeps the question with the same wording, moved under "Other Information". No 2026 i8949, i1040sd, i1040gi or 1099-DA documents are archived.
5. **[V] The coverage estimate does not measure this situation.** `sales.digital` and line 8v have no IRS count (T-034(b) names digital assets). Removing the gate therefore moves the 78.4% figure by 0, although real coverage rises.
6. **[V] OpenTaxSolver 2025 handles G/J, H/K and I/L (`CapGains-G/J` etc.), but it writes the digital totals over the securities totals instead of adding them.** In `taxsolve_US_1040_2025.c` l.1196–1250, `SchedDd[1] = total_sales` for G/J reuses the index that A/D wrote, and the same holds for [2], [3], [8], [9], [10]. A return with both box A and box G sales is wrong in OTS. UsTaxes (pinned commit) has a 'Digital Asset' position type that goes to boxes I and L only, and its Schedule 1 `l8v` returns undefined.

---

## 1. Scope

### 1.1 Computed after the change
| Situation | How | Basis |
|---|---|---|
| Sale, exchange, spending, or swap of a digital asset held as a capital asset, on a 1099-DA or on no form, short- or long-term (boxes G–L), listed on Form 8949 | Existing `sales` row arithmetic, unchanged: col (e), code B on G/J, code W | [V] i8949 p. 1 What's New; p. 3, Digital Assets ("should be reported using box G, H, or I… J, K, or L"); i1040gi p. 16, How To Report |
| G/J rows added to Schedule D line 1a/8a without Form 8949 (Exception 1) | Existing aggregate route; `sales.covered` widened to G, J | [V] i8949 p. 4, Exception 1 (1099-DA: basis reported, no adjustments in box 1h or 1i, Ordinary box in box 6 not checked); i1040sd p. 10 |
| Code B on G/J (basis shown on 1099-DA wrong) | Existing `sales.b` | [V] i8949 p. 8 Example 4 ("Form 1099-B or Form 1099-DA"); p. 7 table |
| Code W on a G–L row, for a tokenized security | Existing `sales.w` | [V] i1040sd p. 5: "The wash sale rules generally apply to transactions involving digital assets that are also stock or securities for tax purposes (tokenized securities)"; i8949 p. 10 (box 1i on Form 1099-DA) |
| Digital asset ordinary income not reported elsewhere (staking, mining not as a business, forks, airdrops): Schedule 1 line 8v | New amount input, line 8v, summed into line 9 | [V] i1040gi p. 92, Line 8v; p550 p. 54 list |
| (D1) Form 1040 page-1 digital asset Yes/No | New Bool line `f1040.digital_assets` | [V] f1040 p. 1; i1040gi pp. 15–16 |

### 1.2 Still refused, with the gate that refuses it
| Situation | Gate (existing unless marked new) | Reason |
|---|---|---|
| Code E: digital asset transaction costs not reflected on the 1099-DA; code L (box 5, loss not allowed); code D, O, Z, M | `sales.bad_code` (code `other`) | [V] i8949 p. 9: costs can be treated differently from selling expenses ("may have differing treatment"), and the rule behind that is in i1099da or the regulations, which are not archived. Code L is i1040sd p. 4 Example 2. **Exception 2 summary rows (code M) stay refused**, which matters most for crypto filers with many trades (risk R2). |
| Code B on I/L (no 1099-DA) | `sales.bad_code`, widened from C/F to C/F/I/L | [V] same rule as C/F, i8949 p. 7 table |
| NFT whose underlying asset is a collectible (28% rate) | `sales.special` (wording widened) | [I] Notice 2023-27 (not archived). i1040sd p. 11 defines collectibles as tangible property and says nothing about NFTs. Owner decision D2. |
| Digital asset held for sale to customers in a business (ordinary), or dealer | n/a: belongs on Schedule C (supported) | [V] i1040gi p. 16 |
| Lost or stolen crypto | `sd.casualty` (existing) | [V] i1040sd p. 1 |
| QOF deferral, collectibles | `sales.special` (existing) | [V] |
| Gift of digital assets (Form 709) | not a Form 1040 computation; mention in help only | [V] i1040gi p. 16 |
| (D3) Line 8v income on a return that files Form 8960 | new narrow gate `s1.digital_nii` (proposed) or none | [V] i8960 p. 1 Reminders: digital asset income "may be subject to" NIIT. Whether staking income is NII is not settled by the archive. |

### 1.3 Gates that go away or narrow
- `sales.digital` **goes away as a refusal gate**. Remove the first `refuses:` entry of `sales.one`. Keep or delete the helper line: it has no reader after the change unless D1 uses it, and `check_consumers` would then flag it. If D1 is adopted, keep it as the reader for the f1040 entry check; otherwise delete it.
- `s1.line8_other` **narrows**: drop `s1.digital_income` from its `any:` list and from the remedy wording.
- `tools/coverage/tree.json`: delete the `{"gate": "sales.digital", ...}` row (l.121). Remove `{"label": "Crypto and other digital assets", ...}` from the Investments theme's `refused` (l.7) and add digital assets to `covered`. Regenerate `docs/COVERAGE.md` and the README table, which drops one refused theme.

### 1.4 Share of filers served
**Not measured [V].** No archived source counts digital asset filers. `gate_frequencies.yaml` includes digital assets inside `securities_sales` (13%, judgment) without splitting them out. Estimate [I, low confidence, no source]: low single-digit percent of returns answer Yes on page 1, and fewer have dispositions. Source to archive if the owner wants a number: an IRS or SOI count of Yes answers to the Form 1040 digital asset question (none in `sources/2025`).

---

## 2. Sources

### 2.1 Archived 2025 sources used (all [V], read here)
- **f8949** pp. 1–2: boxes G–L text; line 2 totals text ("line 1b (if Box A or Box G…)").
- **f1040sd** p. 1: lines 1a/8a ("Form 1099-B or Form 1099-DA"), 1b/2/3/8b/9/10 box pairs.
- **i8949** p. 1 What's New (G–L); p. 2 basis of a digital asset ("cost to acquire… including transaction fees, commissions, transfer taxes"), 1099-DA box 6 / code X for unknown term; p. 3 Digital Assets definition; "not… box C or F"; Box A or Box G; p. 4 Exception 1 (1099-DA boxes 1h/1i, box 6); p. 6 col (a) digital description; p. 7 tokenized security, average basis; p. 8 Example 4 (incorrect basis, 1099-DA); p. 9 code E "digital asset transaction costs"; p. 10 code W, box 1i; p. 11 Examples 5 and 6 (digital assets).
- **i1040sd** p. 1 What's New; p. 4 Example 2 (code L, box 5 on 1099-DA); p. 5 tokenized securities and wash sales; p. 10 Lines 1a/8a conditions (1099-DA boxes 1h, 1i, 3b, 6); Example 1; pp. 10–11 Examples 2 and 3; p. 11 column (h) examples; Line 18 collectibles.
- **i1040gi** p. 15–16 Digital Assets question, How To Report; p. 92 Line 8v.
- **p550** p. 52 Form 1099-DA; p. 54 transactions list; p. 59 cost basis; p. 60 gifts; p. 81 holding period; p. 86 wash sales ("stock or securities").
- **p525** p. 4 (wages paid in digital assets go on the W-2).
- **i8960** p. 1 Reminders (digital assets and NIIT).
- **i8283** p. 7 (digital assets need an appraisal; this matters only to Schedule A noncash gifts, which is outside this lane).

### 2.2 Sources to archive (not in sources/2025)
| Doc | Why | Priority |
|---|---|---|
| **f1099da (2025)** and **i1099da (2025)** | Box numbering cited in help (1d acquired, 1e sold, 1f proceeds, 1g basis, 1h market discount, 1i wash, 2 basis reported, 3b QOF, 5 loss not allowed, 6 term/Ordinary); the 2025 rule that only gross proceeds are reported, with basis reporting starting for covered assets acquired from 1 Jan 2026 [I]; how transaction costs are treated (code E) | high: bank prompts name these boxes |
| Notice 2014-21, Notice 2023-34 | cited by i8949 p. 3 and p550 | low |
| Rev. Proc. 2024-28 (wallet-by-wallet basis safe harbor, 2025 transition) [I] | help for `sales.correct_basis` on digital rows | medium |
| Notice 2023-27 (NFT collectible look-through) [I] | needed if D2 reads NFTs as collectibles | medium |
| Rev. Rul. 2019-24 (forks), Rev. Rul. 2023-14 (staking) [I] | 8v help (timing and amount); i1040gi p. 92 suffices for where the income goes | low |

### 2.3 2026 editions
- [V] Drafts archived: f8949 (posted 2026-05-26), f1040sd (2026-05-15), f1040s1 (2026-06-08), f1040 (2026-09-17). There are no content changes in this area: the word diff shows dates only, and Schedule 1 prints "8v" in full (C-PRI-11).
- [V] Not archived for 2026: i8949, i1040sd, i1040gi, f1099da, i1099da.

---

## 3. Encoding plan

### 3.1 forms/2025/sales.yaml (lane 1)
| Line | Change | Cite |
|---|---|---|
| `sales.one` | delete the `when: sales.digital` refusal entry | — |
| `sales.digital` | keep it, unchanged, as the reader for D1; if D1 is declined, delete it | f8949 pp. 1–2 |
| `sales.covered` | `any:` add `box == G`, `box == J` (label "Basis reported to IRS (box A, D, G or J)") | i8949 p. 3, Box A or Box G; p. 8 |
| `sales.bad_code` | inner `any:` add `box == I`, `box == L` | i8949 p. 7 table, row "basis… incorrect", B on unreported is not applicable |
| `sales.aggregate_eligible` (label/source) | add the 1099-DA conditions: "no adjustment in box 1f/1g (1099-B) or 1h/1i (1099-DA); Ordinary box (1099-B box 2 / 1099-DA box 6) not checked; QOF box (1099-B box 3 / 1099-DA box 3b) not checked" | i1040sd p. 10 |
| `sales.special` (label/source) | D2: add "a non-fungible token (NFT) whose underlying asset is a collectible" | Notice 2023-27 (to archive) |
| `sales.box`, `sales.proceeds`, `sales.reported_basis`, `sales.correct_basis`, `sales.wash_loss` (label/source text only) | add the digital asset statements: G–L must be used and C/F must not (i8949 p. 3); a swap's proceeds are the fair market value of what was received (i8949 p. 11 Ex. 5); basis is cost including transaction fees (i8949 p. 2); wash sale applies only to tokenized securities (i1040sd p. 5); 1099-DA box numbers | as listed |
No new lines, params or tables are needed; `sales_box` already lists G–L. **[V]**

### 3.2 forms/2025/sd.yaml (lane 1) — T-003 first half
Widen all **32** `sales.box` tests (8 lines × 4 columns d/e/g/h). Each `eq: [sales.box, const: X]` becomes `any: [eq X, eq X']`:
| Lines | Today | After |
|---|---|---|
| 1a.*, 1b.* | A | A or G |
| 2.* | B | B or H |
| 3.* | C | C or I |
| 8a.*, 8b.* | D | D or J |
| 9.* | E | E or K |
| 10.* | F | F or L |
Labels and cites already quote the paired text (verified for 1a, 1b). Lines 4–7, 11–22 and every reader of Schedule D (f1040.line7a, qdcg, sdtw, g28, u1250, f8960, f4952, clcw_next_year) are unchanged, because they read sd totals only. **[V]** for sd and f1040.line7a; the other readers were checked by grep only.
T-003's second half (`sd.filed` tests raw 1099-DIV boxes 2b/2d) is independent. Owner decision D6: do it in this lane or leave it open.

### 3.3 forms/2025/s1.yaml (lane 2)
| New/changed line | Printed | Type | Expr | Cite |
|---|---|---|---|---|
| `s1.digital_income` | (helper) | Bool | input (exists; rewrite its label as a plain question with no line number) | i1040gi p. 92 |
| `s1.digital_amount` (new) | (helper) | NonNegDollars | input, `gated_by: s1.line8v`. Source: "Fair market value, when received, of digital assets you (and, on a joint return, your spouse) received in 2025 as ordinary income not reported elsewhere: from staking, mining not as a business, a hard fork or an airdrop; not wages on a W-2, not business income on Schedule C, not a gift or inheritance; zero if none" | i1040gi p. 92 Line 8v; p550 p. 54; p525 p. 4 |
| `s1.line8v` (new) | 8v | NonNegDollars | choose(`s1.digital_income` true → `s1.digital_amount`; false → `s1.zero`) | f1040s1 line 8v; i1040gi p. 92 |
| `s1.line9` | 9 | — | add `s1.line8v` to `sum.of`; cite text "8s to 8u" instead of "8s to 8v" | f1040s1 line 9 |
| `s1.line8_other` | (gate) | — | remove the `s1.digital_income` disjunct; remedy no longer names 8v by omission (it lists what is computed: add "digital assets received as ordinary income") | i1040gi pp. 91–92 |
| (D3) `s1.digital_nii` (new gate, optional) | (gate) | Bool | `all: [s1.line8v > 0, f8960.filed]`; refuses at `s1.line8v`, remedy "Whether this digital asset income is net investment income on Form 8960 is outside this tool" | i8960 p. 1 Reminders |
Check whether `f8960.filed` reading `s1` makes a cycle: f8960 reads `sa.agi`, which reads s1. **[I] it probably does**, so the D3 gate would sit on `f8960.line7` instead. That would refuse in f8960 when 8v > 0, which avoids the cycle; the lane must check.

### 3.4 forms/2025/f1040.yaml (lane 2, only if D1)
- `f1040.digital_assets` (printed "Digital Assets", Bool, input). The bank asks it once per return, before line 8v. Cite: f1040 p. 1; i1040gi pp. 15–16.
- `f1040.digital_conflict` (gate, entry check): `all: [digital_assets == false, any: [count of sales rows with sales.digital > 0, s1.digital_income == true]]`, refusing at `f1040.digital_assets` with the remedy "A sale of a digital asset or digital asset income needs Yes." The count is a `sum_over sales field sales.one where sales.digital`. The entry check lists it under Entry checks, not as coverage.

### 3.5 Ambiguity entries (ambiguities/2025.yaml; distinct ids per lane)
- `amb.2025.digital_wash` (lane 1): i1040sd p. 5 limits wash sales to tokenized securities, and p550 p. 86 says "stock or securities". Reading chosen: code W stays available on G–L, and the filer decides whether the asset is a tokenized security (help). Alternative: refuse code W on G–L.
- `amb.2025.digital_transaction_costs` (lane 1): i8949 p. 9 says costs can be treated differently from selling expenses but gives no rule. Chosen: code E stays refused. The rule is to be revisited once i1099da is archived.
- `amb.2025.nft_collectible` (lane 1, if D2): the collectibles definition (i1040sd p. 11) is tangible-only, and Notice 2023-27 is not archived.
- `amb.2025.digital_8v_nii` (lane 2, D3).

### 3.6 Interactions summary
sales → sd (32 filters) → existing totals. s1.line8v → s1.line9 → s1.line10 → f1040.line8 (and thus AGI, f8960 MAGI, EIC investment income? **[I] no**: EIC investment income does not include line 8v. The lane should check eic.yaml's investment-income line list.) D1 reads sales and s1.

---

## 4. Interview plan (construction protocol §§1–2, 7)

Typical filer in this topic: a person with W-2 wages and one exchange account, who sold or swapped a few coins and received a Form 1099-DA showing proceeds and no basis (2025 is the gross-proceeds year [I]). Filer with nothing in it: no crypto at all; they should answer one step at most for the topic (the D1 question, or nothing if D1 is declined).

### 4.1 Questions (bank: interview/2025/questions.yaml)
| Input | Order/seq | Group | Prompt (≤25/40 words) | Help (≤40 words) |
|---|---|---|---|---|
| (D1) `f1040.digital_assets` | 159 / 1 (new slot just before money_a at 160) | none (once per return; its typical answer is No, but it is printed on the return and asked of everyone) | "In 2025, did you (or, on a joint return, your spouse) receive, sell, trade, spend or give away crypto or another digital asset?" | "Buying crypto with dollars and holding it, or moving it between your own wallets, is a No. Being paid in crypto, swapping one coin for another, or paying for something with it is a Yes." |
| `s1.digital_income` | 161 / 5, stays in `money_b`; if D1, move it beneath `f1040.digital_assets` as a gated child at 159/2 and out of the group | money_b (or none) | tick: "Crypto received as a reward, or from mining, staking or a fork" / prompt as today minus "pay" | "Selling or trading crypto is asked with your sales. Crypto paid as wages is on your W-2; crypto received in a business goes with that business." (remove "A Yes ends the interview here") |
| `s1.digital_amount` (new) | 161 / 8 (after the group) | none | "What was it worth, in dollars, when you received it?" | "Use the value on the day you could first sell or move it. Add up every reward or new coin received in 2025. A gift or inheritance of crypto is not income." |
| `$sales` | 274 / 1 | — | add crypto: "…sell stocks, bonds, options, fund shares or crypto outside a retirement account? Swapping one coin for another, or paying with crypto, counts as a sale." | add "A crypto exchange reports each sale on Form 1099-DA." |
| `sales.box` | 274 / 4 | — | "Under which heading does your statement (Form 1099-B or Form 1099-DA) list this sale?" | replace the refusal sentence with: "Crypto never goes under C or F: with no Form 1099-DA, choose I or L. If the 1099-DA shows code X, use your own dates." |
| `sales.proceeds` | 274 / 6 | — | "…(box 1d of Form 1099-B or box 1f of Form 1099-DA). With no statement, the sale price less fees; for a swap, the value of what you received." | — |
| `sales.reported_basis` | 274 / 7 | — | "(box 1e of Form 1099-B or box 1g of Form 1099-DA)" | — |
| `sales.correct_basis` | 274 / 8 | — | unchanged | add "For crypto, what you paid with fees, tracked for the wallet or account it was sold from." (≤40 words total; may need trimming) |
| `sales.wash_loss` | 274 / 10 | — | add "(box 1g of Form 1099-B or box 1i of Form 1099-DA)" | add "For crypto this applies only to a token that is itself a stock or security." |
| `sales.code` value_label `other` | — | — | add "costs a Form 1099-DA leaves out" | — |
| `sales.special` | 274 / 5 | — | D2: add the bullet "an NFT of art, a gem or another collectible" | — |

Who could answer No wrongly (protocol §2.3):
- At D1: a person who paid for something with crypto, and a person paid in crypto through a W-2. The help names both.
- At `$sales`: a person who swapped coins on a decentralized exchange and received no form. The prompt names swaps.
- At `s1.digital_income`: someone who received airdropped tokens. The tick names airdrops.

Parent cost (rule 1.1): D1 is required on the return, so its cost is already paid. Gating `s1.digital_income` beneath it saves one tick for about 97% or more of filers [I]; the share is judgment and the owner can overrule.

### 4.2 Coverage rows
- `interview/2025/coverage/sales.yaml` `sales.crypto_sold`: its expected end changes from `refused: sales[a].digital` to `proceeds: {sales[a].box: G, ...}`. This is a deliberate change of end; the protocol's "expected end never changes" rule is for redrafts, so record it in the lane notes. Add rows `sales.crypto_no_form_swap` (box L), `sales.crypto_basis_not_reported` (box H), `sales.crypto_code_b_no_form` (I + B → `refused: sales[a].bad_code`), `sales.crypto_cost_code` (G + other → refused `bad_code`), and (D2) `sales.nft_collectible` → `refused: sales[a].special`.
- `coverage/other.yaml` `other.digital_income`: end becomes `proceeds: {s1.digital_amount: …}`. Add (D3) `other.digital_income_niit` → refused. Rows at l.183 and l.305 that answer `s1.digital_income: false` stay as they are.
- (D1) `opening` or `other`: `f1040.digital_conflict` entry check row.

### 4.3 Persona
`interview/2025/personas/14_crypto_investor.yaml`. Single, born 1990, one W-2 (box 1 $85,000.00), one exchange 1099-DA and one self-custody wallet, end `complete`:
- `sales[eth]` H: proceeds 420000, correct_basis 300000, code none → +120000
- `sales[btc]` K: proceeds 1500000, correct_basis 1850000 → −350000
- `sales[sol_swap]` L: proceeds 260000, correct_basis 100000 → +160000
- `s1.digital_income` true, `s1.digital_amount` 41250; `f1040.digital_assets` true (D1)
Expected: sd.line7 = 120000; sd.line15 = −350000 + 160000 = −190000; sd.line16 = −70000; sd.line21 = −70000 (above the −300000 limit); f1040.line7a = −70000; s1.line8v = s1.line9 = 41250; f1040.line9 total income = 8500000 − 70000 + 41250 = 8471250 (assuming no other income).
Refused persona (D2): `15_refused_nft_art`, a box L sale of an NFT of art → `refused: sales[a].special`. Walk the baseline for both before the change (checklist §7.1).

---

## 5. Fixtures (hand-predicted; cents; route as in the existing `sales.official.*` cases)

| # | id | Inputs | Expected (arithmetic) | Evidence |
|---|---|---|---|---|
| F1 | `sales.official.da.aggregate` | J, aggregate, proceeds 600000, reported_basis 200000 | sd.line8a.d 600000; .e 200000; .h 600000 − 200000 = 400000 | A: i1040sd p. 10 Example 1, 1099-DA branch |
| F2 | `sales.official.da.two_aggregate` | F1 + second J aggregate 500000/300000 | 8a.d 1100000; .e 500000; .h 600000 | A: i1040sd p. 11, continuation |
| F3 | `sales.official.da.not_reported` | K, detail, proceeds 600000, correct_basis 200000 | sd.line9.d 600000; .e 200000; .h 400000 | A: i1040sd pp. 10–11 Example 2 + col (h) Example 1 |
| F4 | `sales.official.da.adjustment` | J, detail, code B, proceeds 600000, reported 200000, correct 300000 | e 200000; g 200000 − 300000 = −100000; h 600000 − 200000 − 100000 = 300000 → sd.line8b.{d,e,g,h} | A: i1040sd p. 11 Example 3 and col (h) Example 3 (g = −$1,000) |
| F5 | `sales.official.da.basis_worksheet` | G, code B, proceeds 100000, reported 90000, correct 10000 | g 90000 − 10000 = 80000; h 100000 − 90000 + 80000 = 90000 → sd.line1b; f1040.line7a 90000 (only sale) | A: i8949 p. 8 Example 4 (1099-DA) |
| F6 | `sales.official.da.swap` | L, proceeds 300000 (FMV of B), correct_basis 100000 | sd.line10.h 200000; sd.line15 200000; f1040.line7a 200000 | A for the amounts: i8949 p. 11 Example 5. Box L is inferred (no 1099-DA named) |
| F7 | `sales.official.da.paid_in_crypto` | I, proceeds 1200000, correct_basis 1000000 | sd.line3.h 200000 | A: i8949 p. 11 Example 6 (sale part only; the Schedule C $10,000 is a separate fixture if wanted) |
| F8 | `sales.mixed.A_G` | A: 500000/400000; G: 300000/350000, both detail | line1b.d 800000; .e 750000; .h 100000 − 50000 = 50000; f1040.line7a 50000 | synthetic; shows the A+G sum that OTS gets wrong |
| F9 | `sales.adjust.G.W` (tokenized) | G, code W, proceeds 400000, reported 500000, wash_loss 60000 | g 60000; h 400000 − 500000 + 60000 = −40000 → line1b.h −40000 | synthetic; i1040sd p. 5, i8949 p. 10 |
| F10 | `sales.adjust.{H,J,K}.{B,W,BW}`, `{I,L}.W` | mirror the 12 existing `sales.adjust.{A,B,D,E}.*` cases | the same arithmetic as each mirrored A–F case, landing on the paired G–L line | synthetic; kills the .g filter mutants |
| F11 | `sales.refuse.I.B` / `.L.B` | I (resp. L), code B | refused `sales[a].bad_code` | synthetic |
| F12 | `sales.refuse.H.aggregate` | H, route aggregate | refused `sales[a].bad_aggregate` (covered false) | i1040sd p. 10 |
| F13 | `sales.da.loss_limit` | single, L, proceeds 100000, correct_basis 600000 | h −500000; line15 −500000; line16 −500000; line21 −300000; f1040.line7a −300000 | synthetic; i1040sd line 21 |
| F14 | `s1.line8v` | digital_income true, digital_amount 123456 | s1.line8v 123456; s1.line9 123456; s1.line10 123456 (if nothing else) | synthetic; i1040gi p. 92 |
| F15 | `s1.line8v.none` | digital_income false | s1.line8v 0 (kills the choose mutant) | synthetic |

**Mutation pins to expect.**
- Each of the 32 widened `any:` disjuncts and the `sales.covered` G/J and `sales.bad_code` I/L disjuncts creates operand and constant mutants. They are killed only if a fixture puts a G–L row on every sd line with all four columns nonzero; this needs (g) ≠ 0, hence F10.
- `sales.digital` keeps one reader only under D1; without D1 it must be deleted, or it surfaces as an unread line.
- No equivalent mutants are foreseen [I].
- Keep `reports/2025/mutation.md` pinned lists in step (full tier).

**External engines.**
- OTS 2025 computes G–L but overwrites totals across A/G and similar pairs [V, source read]. The adapter should map rows to `CapGains-G/J`, `H/K` and `I/L`, and either generate only cases that keep securities and digital rows on different Schedule D lines, or record the overwrite as an exclusion with its reason. OTS has `S1_8v` [V].
- UsTaxes: rows with `positionType: 'Digital Asset'` go to I/L [V, F8949.ts l.72–144]. The adapter already compares line totals only, because all sales land on C/F (ustaxes_adapter.py l.441, 460). Line 8v cannot be compared (`l8v` undefined) [V].
- `generate_cases.py` must draw G–L boxes.

---

## 6. 2026
- [V] Form text: no operation needed for 8949, Schedule D or Schedule 1 line 8v; the 2025 lines carry forward. The page-1 question (D1) moved under "Other Information" with the same wording, so it needs only a layout or render note (per-year layouts, T-230). Wording ops are needed only if labels name the year; new ids must be year-free (`check_year_ids`).
- [I] Substance: 2026 is the first year brokers must report basis for covered digital assets (acquired from 1 Jan 2026), so G/J rows become common. This is not visible in the archived drafts; verify it from the 2026 i1099da and i8949 once posted. Expected 2026 change entries: none for sd and sales; possibly wording for help once the 2026 i8949 is posted (kind (b), waiting on instructions, like C-PRI-11).
- Operations in `changes/2026/`: none now. Add an entry to `research/ty2026/changes.md` (its l.489 currently says "no digital-asset income path in the slice") recording that the path now exists and is unchanged in the drafts.

---

## 7. Lane split (no file collisions; claims via tools/claims.py)
| Lane | Files (claims) | Model/class | Notes |
|---|---|---|---|
| L1 sales + Schedule D | forms/2025/sales.yaml, sd.yaml; fixtures/2025/sales.json, sd.json; interview/2025/coverage/sales.yaml; bank entries order 274; ambiguity ids `amb.2025.digital_wash`, `_transaction_costs`, `_nft_collectible`; personas 14/15 | Opus, judgment (source reading, help wording); the 32-filter edit inside it is mechanical and may be a Sonnet sub-step | closes T-003 (first half) |
| L2 line 8v + page 1 | forms/2025/s1.yaml, f1040.yaml (D1); fixtures s1.json, f1040.json; coverage/other.yaml; bank orders 159–161; `amb.2025.digital_8v_nii` | Opus, judgment | reads `sales.digital` (contract: L1 keeps it unchanged); D3 cycle check |
| L3 engines (after L1/L2 merge) | tools/engines/ots_adapter.py, ustaxes_adapter.py, generate_cases.py | Sonnet, mechanical | full tier; record the OTS overwrite |
| Integrator | tools/coverage/tree.json, regenerated docs/COVERAGE.md and README, TASKS.md (T-003), research/ty2026/changes.md; structural merge of questions.yaml and ambiguities | Sonnet, mechanical | bank merged by entry |

Reviews, one round per form after its fixes land (charter; line-scoped):
- transcription × {sales, sd, s1, f1040}, render × 4, class M × 4: 12 paid calls
- question reviews for the changed bank entries of sales, s1, f1040: about 3
- screen and false-no per release sample, not per lane

Cost [I, from `.transcription/costs.jsonl` averages for these forms: $0.20–$1.13 per call]: roughly $6–$15 for one round. Each run stays under the $3 per-run gate.

---

## 8. Risks and owner decisions

Decisions:
- **D1** Encode the Form 1040 page-1 digital asset question now (recommended: it is required on every return and is missing today), with the entry check?
- **D2** NFTs: refuse an NFT of a collectible through `sales.special` (recommended; archive Notice 2023-27), or treat all NFTs as ordinary digital assets?
- **D3** Line 8v with Form 8960 filed: refuse narrowly (recommended, given the archive's silence), or read staking and similar income as not NII?
- **D4** Code E for digital asset transaction costs: keep it refused (recommended until i1099da is archived)?
- **D5** Code W on G–L: allow it, limited to tokenized securities by help (recommended), or refuse?
- **D6** Fold T-003's second half (`sd.filed` raw 1099-DIV boxes) into L1, or leave it?
- **D7** Accept the coverage estimate's silence (an unmeasured gain), or archive a count source first?
- **D8** Exception 2 / code M summary rows (one row per broker per box): crypto filers often have hundreds of trades. Without code M this lane serves mostly low-volume filers. Is supporting code M in scope (a separate, small change: code M with no amount)?

Risks:
- **R1** For 2025, 1099-DAs mostly carry no basis [I], so the filer supplies basis. The tool does not compute it (no FIFO, specific identification or wallet-by-wallet allocation; Rev. Proc. 2024-28 transition). Errors therefore move to the filer's input, and help can only point at the rule.
- **R2** Volume. Per-row entry does not scale to active traders (see D8).
- **R3** The OTS overwrite defect makes the engine differential misleading for mixed A/G returns unless excluded.
- **R4** The bank prompts name 1099-B and 1099-DA boxes from i8949 and i1040sd text. The 1099-DA form itself is not archived, so box numbers are second-hand until f1099da/i1099da are fetched (testimony, AP-10).
- **R5** Restating `sales.crypto_sold` and `other.digital_income` changes their expected ends. This is deliberate, and the integrator must not read it as a regression.
- **R6** Whether EIC investment income or other income-based lines (eic, f8960, f8962 household income) should include line 8v was not checked line by line [I]. L2 must grep every reader of `s1.line9` and `s1.line10`.
