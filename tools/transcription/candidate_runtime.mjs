// Executable form of a validated model candidate: the declarative lines substituted into the
// canonical data, with the reply's refusal declarations mapped to evaluator refusal objects.
// No model-generated JavaScript, commands, tools, paths or network calls are executed.
import { prepareCandidate } from './model_candidate.mjs';
import { checkExpressionTypes } from '../../engine/dist/check.js';

export function executableCandidate(context, form, lines) {
  const { data, candidate, errors } = prepareCandidate(context, form, lines);
  // A reply with one bad declaration is still executable line by line: keep the valid lines,
  // record the invalid ones, and let triage report them as candidate-invalid (T-143).
  const invalid = new Set(errors.map(error => error.line).filter(Boolean));
  const inputIds = new Set(candidate.lines.filter(line => line.expr.op === "input").map(line => line.id));
  const allIds = new Set(candidate.lines.map(line => line.id));

  const assemble = () => {
    const gateChecks = [];
    const gateOwners = new Map();
    const localErrors = [];
    const ids = new Set(allIds);
    const runtimeLines = [];
    let invalidated = 0;
    for (const line of candidate.lines) {
      const publishedInput = inputIds.has(line.id);
      if (!publishedInput && invalid.has(line.id)) continue;
      let bad = false;
      const refuses = (line.refuses ?? []).map(refusal => {
        const when = typeof refusal === 'string' ? refusal : refusal?.when;
        if (typeof when !== 'string') {
          localErrors.push({ line: line.id, message: 'invalid refusal gate id' });
          bad = true;
          return null;
        }
        if (typeof refusal === 'object' && (Object.keys(refusal).some(key => !['when', 'when_known', 'form', 'remedy', 'cite'].includes(key)) || ('when_known' in refusal && refusal.when_known !== true))) {
          localErrors.push({ line: line.id, message: 'invalid consistency-check declaration' });
          bad = true;
          return null;
        }
        let id = `${form}.__contract_gate_${gateChecks.length}`;
        while (ids.has(id)) id += '_';
        ids.add(id);
        gateChecks.push({ id, type: 'Bool', expr: { op: 'test', eq: [when, { const: true }] } });
        gateOwners.set(id, line.id);
        return { when, ...(refusal?.when_known ? { when_known: true } : {}), form: 'model-declared refusal', remedy: 'Outside candidate scope', cite: null };
      }).filter(Boolean);
      if (bad && !publishedInput) {
        invalid.add(line.id);
        invalidated += 1;
        continue;
      }
      runtimeLines.push({ id: line.id, type: line.type, expr: line.expr, refuses, cite: null });
    }
    const replace = doc => doc.id === form ? { ...candidate, lines: runtimeLines } : doc;
    const runtime = { ...data, forms: data.forms.map(replace), defs: data.defs.map(replace) };
    const checking = { ...runtime,
      forms: runtime.forms.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc),
      defs: runtime.defs.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc) };
    return { runtime, checking, runtimeLines, gateChecks, gateOwners, errors: localErrors, invalidated };
  };

  let built = assemble();
  for (let round = 0; round < 8; round++) {
    const typeErrors = checkExpressionTypes(built.checking, form);
    let changed = built.invalidated > 0;
    for (const error of typeErrors) {
      const owner = built.gateOwners.get(error.line) ?? error.line;
      if (!allIds.has(owner) || inputIds.has(owner) || invalid.has(owner)) continue;
      invalid.add(owner);
      built.errors.push(error);
      changed = true;
    }
    if (!changed) break;
    built = assemble();
  }
  errors.push(...built.errors);
  return { runtime: built.runtime, candidate, errors, invalid };
}
