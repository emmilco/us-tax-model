// Pure rules of executable triage (triage.mjs), kept apart so they can be tested without
// evaluating a return.

// What the filer sees of a line (the project's or the reply's) whose shown_when evaluated to `cond`: hidden when the
// condition is false; when the condition is refused or unknown, whether the line shows is itself
// refused or unknown, so the line's own amount is not what the form shows.
export function displayed(value, cond) {
  if (!cond) return value;
  if (cond.kind === 'bool') return cond.value ? value : { kind: 'hidden' };
  if (cond.kind === 'refusal' || cond.kind === 'unknown') return { kind: cond.kind };
  return value;
}

// How two values of one line compare: what the filer sees on each side.
const blank = v => v && ((v.kind === 'money' && v.cents === 0) || (v.kind === 'bool' && !v.value) || (v.kind === 'count' && v.value === 0));
function shape(value) {
  if (!value) return { kind: 'absent' };
  if (value.kind === 'refusal') return { kind: 'refusal' };
  if (value.kind === 'unknown') return { kind: 'unknown' };
  return value;
}

// A line hidden on one side shows no amount: it agrees with the other side's blank (zero) or hidden line.
export const same = (a, b) => a?.kind === 'hidden' ? blank(b) || b?.kind === 'hidden'
  : b?.kind === 'hidden' ? blank(a) : JSON.stringify(shape(a)) === JSON.stringify(shape(b));
// Kinds name the side that is narrower: a refusal outranks an unknown, as in the evaluator.
export const difference = (a, b) => {
  if (a?.kind === 'hidden') return b?.kind === 'refusal' ? 'candidate-refuses' : b?.kind === 'unknown' ? 'candidate-unknown' : 'candidate-shows-skipped';
  if (b?.kind === 'hidden') return a?.kind === 'refusal' ? 'project-refuses' : a?.kind === 'unknown' ? 'project-unknown' : 'candidate-hides-shown';
  const [x, y] = [shape(a).kind, shape(b).kind];
  if (x === 'refusal' || y === 'refusal') return x === 'refusal' && y === 'refusal' ? 'value' : x === 'refusal' ? 'project-refuses' : 'candidate-refuses';
  if (x === 'unknown' || y === 'unknown') return x === 'unknown' ? 'project-unknown' : 'candidate-unknown';
  return 'value';
};

// Witnesses of one line's differences: a sample of at most `max` per difference kind, chosen in
// the order found, and a separate sample of at most `max` per kind on completed returns (the
// differences that can show a value error), so those are not crowded out by refused or incomplete
// returns. Keeping every completed witness would make a record megabytes long.
export function recordWitness(stats, kind, projectReturn, make, max) {
  const sampled = stats.witnesses.filter(w => w.kind === kind).length < max;
  const completed = projectReturn === 'completed' && stats.completed_witnesses.filter(w => w.kind === kind).length < max;
  if (!sampled && !completed) return;
  const witness = make();
  if (sampled) stats.witnesses.push(witness);
  if (completed) stats.completed_witnesses.push(witness);
}
