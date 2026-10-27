// Executable form of a validated model candidate: the declarative lines substituted into the
// canonical data, with the reply's refusal declarations mapped to evaluator refusal objects.
// No model-generated JavaScript, commands, tools, paths or network calls are executed.
import { prepareCandidate } from './model_candidate.mjs';
import { checkExpressionTypes } from '../../engine/dist/check.js';

export function executableCandidate(context, form, lines) {
  const { data, candidate, errors } = prepareCandidate(context, form, lines);
  if (errors.length) return { runtime: null, candidate, errors };
  // The review transport names gate ids; the evaluator uses objects. Map that
  // representation only, without importing any authored refusal placement.
  const gateChecks = [];
  const ids = new Set(candidate.lines.map(line => line.id));
  const runtimeLines = candidate.lines.map(line => {
    const refuses = (line.refuses ?? []).map(refusal => {
      const when = typeof refusal === 'string' ? refusal : refusal?.when;
      if (typeof when !== 'string') {
        errors.push({ line: line.id, message: 'invalid refusal gate id' });
        return null;
      }
      if (typeof refusal === 'object' && (Object.keys(refusal).some(key => !['when', 'when_known', 'form', 'remedy', 'cite'].includes(key)) || ('when_known' in refusal && refusal.when_known !== true))) {
        errors.push({ line: line.id, message: 'invalid consistency-check declaration' });
        return null;
      }
      let id = `${form}.__contract_gate_${gateChecks.length}`;
      while (ids.has(id)) id += '_';
      ids.add(id);
      gateChecks.push({ id, type: 'Bool', expr: { op: 'test', eq: [when, { const: true }] } });
      return { when, ...(refusal?.when_known ? { when_known: true } : {}), form: 'model-declared refusal', remedy: 'Outside candidate scope', cite: null };
    }).filter(Boolean);
    return { id: line.id, type: line.type, expr: line.expr, refuses, cite: null };
  });
  const replace = doc => doc.id === form ? { ...candidate, lines: runtimeLines } : doc;
  const runtime = { ...data, forms: data.forms.map(replace), defs: data.defs.map(replace) };
  const checking = { ...runtime,
    forms: runtime.forms.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc),
    defs: runtime.defs.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc) };
  errors.push(...checkExpressionTypes(checking, form).filter(error => ids.has(error.line) && gateChecks.some(line => line.id === error.line)));
  return { runtime: errors.length ? null : runtime, candidate, errors };
}
