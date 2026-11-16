# Lane MSTRUCT: the unobserved-line structural rule

Model claude-opus-5-5, judgment (tool change). Year 2025, us and ny. Worktree `.claude/worktrees/mstruct`, at the tested tree 6649c637.
Patch: `round7/mstruct.patch` (engine/src/mutate.ts, tools/README.md). No commits, no check_all, no paid reviews.

**The full mutate run did NOT measure the rule.** The coordinator stopped the single federal run (pid 64423, exit 143)
after 80 minutes on a saturated machine, so it produced no report. No NY mutate run was made. Lane MINT's full mutate on
the merged tree is the measurement. The counts below come from a static pre-check that evaluated no mutant.

## The rule (`unobservedLine`, last in `structuralReason`)

A surviving mutant of a line is explained when that line:

- is a `(helper)` of a form, not of a definition. Any other marker (`(gate)`, `(question)`, `(status)`, `(screen)`,
  `(computed helper)`), a column line or a worksheet-step line counts as observed.
- carries no refusal gate and no `shown_when`, and reads no definition instance.
- is not named by the product. That means the built interview profiles (`canonical/<year>/interview-*.json`: targets,
  questions, refusal notes), the interview YAML of the year (federal and NY, including conflict_checks), and the
  product code (eval, output, interview, interview-words, serve, spouse-wording, tick-groups, gates, text, ui/app, ui/text).
  Bracketed entry keys are dropped first, so `person[t].k1p[a].sche_row` names `k1p.sche_row`.
- is named, if at all, only by lines that pass all of the above, transitively. "Named" means the line id appears as a
  string anywhere in the naming line: its expression (including `sum_over` field and `where` filter), refusal gates,
  `shown_when` or `gated_by`.

If any `opaque` line exists, the rule is off everywhere.

The rule is computed from the data on every run, so it lapses for a chain as soon as an observed line reads it.

The mutant ids sit at the end of the structural chain, after `EQUIVALENT_IF`. A survivor that an earlier rule or a
keyed argument explains therefore keeps its reason. The EQUIVALENT_IF table is untouched, and the new code sits inside
`// ---- lane mstruct begin/end ----` blocks. Outside those blocks the patch changes only:

- the imports (`existsSync`, `readdirSync`, `nyPath`, `yearPath`);
- one `?? unobservedLine(...)` in `structuralReason`;
- the metric row;
- the `continue` that drops these survivors from the general equivalent list;
- the self-test log lines;
- the exit condition.

### What "observable" means here, and the judgment call to check

The rule follows the convention mutate.ts already uses: `isHelper` and the sampled check treat a `(helper)` as on no
value sheet. In the product that convention is only partly true:

- **Interview / server UI:** only the interview targets and what they read are evaluated, so an unread helper is not
  evaluated and not shown.
- **CLI values sheet (`main.js eval`):** this evaluates every form line (`allTargets`) and prints every line,
  helpers included. A mutant explained by this rule does change those helper rows there.

The person totals at the chain ends also carry `display:` ("why an unread line is kept: shown on the values sheet").
The rule treats `display` helpers like any other helper. If the owner reads `display` as making a line an output,
every explained mutant below would be lost, because every chain ends in a `display` total.

Two choices are deliberately conservative:

- A helper that carries its own refusal gate counts as observed. The server lists consistency-check refusals from
  all values as conflicts.
- A definition line counts as observed.

Together they exclude one mutant that lane MW's no-value-sheet-reader category contains:
`operand.k1s.k1s.qbi.qbi_stmt_if_any.then0`, because `k1s.qbi` has a refusal gate.

## Report

`mutation.md` gains three things:

- a metric row, "Surviving on unobserved lines (among the provably equivalent)";
- its own section "Surviving — on unobserved lines", with the count, each mutant and its chain;
- the chain ends (helpers nothing reads) with the number of mutants resting on each.

These survivors are counted among the provably equivalent, as the other structural rules' survivors are.

## Self-test (`unobservedLineSelfTest`, run by `mutate`; a problem fails the step)

Synthetic form: H, a copy of x2 mutated to read x1, is read only by helper D, which nothing reads.

- **Accepted:** H's mutant. An evaluation of every line shows nothing but H and D changing.
- **Rejected, each planted in turn:**
  - D printed;
  - H itself printed (the "not on a value sheet" requirement);
  - D marked `(gate)`;
  - a printed line refused when D;
  - a printed line `shown_when` D;
  - D an interview target;
  - H named by product code;
  - H carrying a refusal gate;
  - a helper reading D that is read by a printed line;
  - a definition line reading H;
  - D reading a definition instance.
- **Collection filter:** a helper flag of a collection entry read only by an unread `sum_over` count's `where` is
  accepted. It is rejected once the count is printed.

Result, narrow run under nice 10 (`node` on the compiled module, no mutants evaluated): **0 problems.**
Typecheck (`tsc -p engine`) is clean.

## Pre-check, not a measurement

For each survivor listed as "not yet explained" in the committed `reports/2025/mutation.md` (372, the tested tree's
report), `equivalenceReason` was rerun on the rebuilt data.

**47 would now be explained** (k1p 8, k1s 17, person 22). That is lane MW's 48 no-value-sheet-reader mutants less
`k1s.qbi`, and none outside MW's list.

The committed NY report has 0 unexplained survivors (52 survivors, all explained), so NY should not change.

What the pre-check cannot show is whether any mutant's kill/survive outcome or existing reason changed. By
construction it cannot: outcomes are computed without the structural rules, and the new rule runs only after every
earlier rule and keyed argument has declined. MINT's run should still confirm two things:

- the metric rows other than "Surviving on unobserved lines" match the base report;
- "not yet explained" drops by exactly the new section's count.

## Chain ends: helpers read by nothing (cleanup candidates, not to delete now)

All are `display`-marked partnership or S corporation totals on `person`. The number after each is how many explained
mutants rest on it.

person.k1p_count 1, person.k1p_count_general 1, person.k1p_count_inv 1, person.k1p_count_passive_loss 3,
person.k1p_count_sche 6, person.k1p_total_backup_wh 1, person.k1p_total_collectibles 1, person.k1p_total_nonpassive 1,
person.k1p_total_nonpassive_loss 1, person.k1p_total_ord_div 1, person.k1p_total_p4_income 1, person.k1p_total_p4_loss 1,
person.k1p_total_p5_income 1, person.k1p_total_p5_prior 1, person.k1p_total_p6_loss 1, person.k1p_total_prior 2,
person.k1p_total_qbi_stmt 1, person.k1p_total_qual_div 1, person.k1p_total_se_pos 1, person.k1p_total_st_gain 1,
person.k1p_total_taxexempt_int 1, person.k1p_total_unrecap_1250 1, person.k1s_count_sche 4,
person.k1s_total_collectibles 1, person.k1s_total_p4_income 2, person.k1s_total_p4_loss 1, person.k1s_total_p4_prior 2,
person.k1s_total_p5_income 3, person.k1s_total_p5_loss 6.

(29 ends. Intermediate helpers such as `k1p.sche_row`, `k1s.sche_any` and the `k1s.p*` loss/income helpers are dead
only through these ends.)
