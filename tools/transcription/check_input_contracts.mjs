// Optional, bounded evaluation of validated declarative IR on trusted synthetic facts.
// No model-generated JavaScript, commands, tools, paths or network calls are executed.
import { readFileSync } from 'node:fs';
import { executableCandidate } from './candidate_runtime.mjs';
import { evaluate } from '../../engine/dist/eval.js';

const { context, form, lines, cases } = JSON.parse(readFileSync(0, 'utf8'));
if (!Array.isArray(cases) || cases.length > 32) throw new Error('invalid contract case count');
if (!Array.isArray(lines) || lines.length > 5000) throw new Error('invalid candidate size');
const { runtime, errors } = executableCandidate(context, form, lines);
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
