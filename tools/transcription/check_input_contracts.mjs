// Optional, bounded evaluation of validated declarative IR on trusted synthetic facts.
// No model-generated JavaScript, commands, tools, paths or network calls are executed.
import { readFileSync } from 'node:fs';
import { prepareCandidate } from './model_candidate.mjs';
import { checkExpressionTypes } from '../../engine/dist/check.js';
import { evaluate } from '../../engine/dist/eval.js';

const { context, form, lines, cases } = JSON.parse(readFileSync(0, 'utf8'));
if (!Array.isArray(cases) || cases.length > 32) throw new Error('invalid contract case count');
if (!Array.isArray(lines) || lines.length > 5000) throw new Error('invalid candidate size');
const { data, candidate, errors } = prepareCandidate(context, form, lines);
if (errors.length) {
  process.stdout.write(JSON.stringify({ state: 'invalid', errors, cases: [] }));
} else {
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
      let id = `${form}.__contract_gate_${gateChecks.length}`;
      while (ids.has(id)) id += '_';
      ids.add(id);
      gateChecks.push({ id, type: 'Bool', expr: { op: 'test', eq: [when, { const: true }] } });
      return { when, form: 'model-declared refusal', remedy: 'Outside candidate scope', cite: null };
    }).filter(Boolean);
    return { id: line.id, type: line.type, expr: line.expr, refuses, cite: null };
  });
  const replace = doc => doc.id === form ? { ...candidate, lines: runtimeLines } : doc;
  const runtime = { ...data, forms: data.forms.map(replace), defs: data.defs.map(replace) };
  const checking = { ...runtime,
    forms: runtime.forms.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc),
    defs: runtime.defs.map(doc => doc.id === form ? { ...doc, lines: [...runtimeLines, ...gateChecks] } : doc) };
  errors.push(...checkExpressionTypes(checking, form).filter(error => ids.has(error.line) && gateChecks.some(line => line.id === error.line)));
  if (errors.length) {
    process.stdout.write(JSON.stringify({ state: 'invalid', errors, cases: [] }));
  } else {
    const results = cases.map(test => {
      const values = evaluate(runtime, test.inputs, Object.keys(test.expect)).values;
      const outputs = Object.entries(test.expect).map(([target, expected]) => {
        const actual = values.get(target) ?? { kind: 'unknown', reason: 'target not produced' };
        const pass = Object.entries(expected).every(([key, value]) => actual[key] === value);
        return { target, expected, actual, pass };
      });
      return { id: test.id, pass: outputs.every(output => output.pass), outputs };
    });
    process.stdout.write(JSON.stringify({ state: results.every(test => test.pass) ? 'pass' : 'fail', errors: [], cases: results }));
  }
}
