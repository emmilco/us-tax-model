// Pure rules of executable triage (triage.mjs), kept apart so they can be tested without
// evaluating a return.

// What the filer sees of a project line whose shown_when evaluated to `cond`: hidden when the
// condition is false; when the condition is refused or unknown, whether the line shows is itself
// refused or unknown, so the line's own amount is not what the form shows.
export function displayed(value, cond) {
  if (!cond) return value;
  if (cond.kind === 'bool') return cond.value ? value : { kind: 'hidden' };
  if (cond.kind === 'refusal' || cond.kind === 'unknown') return { kind: cond.kind };
  return value;
}

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
