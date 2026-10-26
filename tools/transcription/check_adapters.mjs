// Fixed, bounded evaluation of authored adapter plumbing, not model output.
import { readFileSync } from 'node:fs';
import { checkExpressionTypes } from '../../engine/dist/check.js';
import { evaluate } from '../../engine/dist/eval.js';

const { context, form, cases } = JSON.parse(readFileSync(0, 'utf8'));
if (!Array.isArray(cases) || !cases.length || cases.length > 32) throw new Error('invalid adapter case count');
const errors = checkExpressionTypes(context, form);
const results = errors.length ? [] : cases.map(test => {
  const values = evaluate(context, test.inputs, Object.keys(test.expect)).values;
  const outputs = Object.entries(test.expect).map(([target, expected]) => {
    const actual = values.get(target) ?? { kind: 'unknown', reason: 'target not produced' };
    return { target, expected, actual, pass: Object.entries(expected).every(([key, value]) => actual[key] === value) };
  });
  return { id: test.id, pass: outputs.every(output => output.pass), outputs };
});
process.stdout.write(JSON.stringify({ state: errors.length ? 'invalid' : results.every(test => test.pass) ? 'pass' : 'fail', errors, cases: results }));
