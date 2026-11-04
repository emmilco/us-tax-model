# Brief: classify surviving tier-2 mutants (T-159, package mutation-t2)

Repo worktree (read-only for you): /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/agent-a6e970022fe3a8b6b
(call it WT). Do NOT edit any file under WT. Do NOT run git, check-all, or `node engine/dist/main.js mutate`.
Do NOT run `npm run compile` (the parent owns the build). Write only under your own directory /tmp/mut2/specs/<your-name>/.

## What a mutant is
`MUTATE_TIER=2` mutants replace the `then` value X of one alternative i of a `choose` line L with another line Y of the same
document and type (the mutant id is `operand.<doc>.<L>.<X last segment>.then<i>`; the note says `X -> Y`). A mutant
"survives" when no fixture expectation changes. Each survivor in your list must end in exactly one of:
- (a) **a fixture** that kills it: a case whose inputs come from an existing corpus case (fixtures/2025/*.json), optionally
  with a few inputs changed, and whose `expect` names printed lines whose values you predicted BY HAND FROM THE ARCHIVED
  SOURCE before running the evaluator. The prediction and the source quote (with page) go in the note.
- (b) **an equivalence argument**: the mutant cannot change any printed line at any input, including incomplete inputs
  (an unanswered input gives "unknown"; a refusal gate gives a refusal; spec/spec.md section 4.7 gives the evaluation
  order rules: which operand's refusal/unknown wins). Give the precise argument; the parent will encode it as a rule.
- (c) **a defect**: the mutant reveals that the current encoding gives a value the source contradicts on a reachable
  return. Describe it with the source quote and a witness input.
A difference that appears only on incomplete inputs (unknown vs a value, or which refusal shows) is NOT equivalence; such
mutants need a fixture (a partial-input case, or a case where two different refusals compete), or are reported as
"refusal-order only" with a witness so the parent can decide.

## Tools (all under /tmp/mut2; run with `MUTATE_TIER=2`; they chdir into WT themselves)
- `python3 /tmp/mut2/show.py <line ids...>`: a line's expression, type, printed marker and refusal gates (canonical JSON).
- YAML with labels and citations: WT/forms/2025/<doc>.yaml.
- `python3 /tmp/mut2/case.py <case id> <input-prefixes,comma-sep> [line ids,comma-sep]`: a corpus case's inputs (filtered),
  expectations, and the evaluator's values for the given lines. (Looking at values of upstream lines is fine; the value
  of the line you are predicting must be written down from the source first.)
- `python3 /tmp/mut2/q.py <doc> '<regex>' [len]`: search an archived source (WT/sources/2025/<doc>.cols.txt), prints page.
- `python3 /tmp/mut2/wshow.py /tmp/mut2/wb1.jsonl <substring>`: earlier witness search (fixture corpus + 400 generated
  returns): for each mutant, a case where a printed line differs. `/tmp/mut2/fz1.jsonl` (same format with `examples[].v`
  the input change) is a fuzz search around corpus cases; `cat /tmp/mut2/fz1.txt | grep <substring>` for a summary.
- `MUTATE_TIER=2 node /tmp/mut2/h.mjs witness <mutant id> [n generated]` (single thread, ~1 min): printed differences.
- `MUTATE_TIER=2 node /tmp/mut2/dbg.mjs <mutant id>`: readers, path facts, and the structural prover's view.
- Checking a spec: `python3 /tmp/mut2/trycase.py <spec.json>` evaluates your spec (without writing it into the repo)
  against the baseline AND the listed mutants, printing mismatches and which mutants it kills. Use it only after the
  prediction is written in the spec. If the baseline disagrees with your prediction, do not silently change the
  prediction: re-read the source; if the source supports you, it may be a defect (c); otherwise record the mismatch and
  correct it, saying so in your report.

## Spec format (one JSON list per file, in /tmp/mut2/specs/<your-name>/)
```
[{"id": "mutation.t2.<form>.<short>", "from": "<corpus case id>", "covers": ["<doc>", ...],
  "set": {"<input key>": value, ...}, "drop": ["<input key>"], "drop_prefix": ["f1095a[mkt_a]."],
  "note": "Mutation fixture (choose branch values: <what>), inputs of <case> <unchanged|with ...>; expected values predicted by hand from the archived <doc> (p. N, <quoted text>) before running the evaluator: <the reasoning and numbers>.",
  "expect": {"<line key>": {"kind": "money", "cents": 12345}, "<bool line>": {"kind": "bool", "value": true}}, "kills": ["<mutant id>", ...]}]
```
Money is in cents. Keys of collection lines look like `person[taxpayer].f8889[hsa].line3`. Prefer the simplest corpus case
(stage*.json cases are simpler than classm.*.deepseek ones); prefer expectations that are direct source statements ($0
when a line does not apply, a copy, a fixed amount) over long computations. Expect only printed lines.

## Report
Finish with a report listing, per mutant: outcome (a/b/c or unresolved), spec file and case id, prediction vs evaluator
(matched first time or not), and for (b) the full argument with the lines and facts it relies on.
