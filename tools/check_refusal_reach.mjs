// A refusal fixture must describe a return the interview actually refuses: evaluate the full
// interview's targets on its inputs and require a refusal among them. Fixture checks evaluate
// helper lines the interview never reaches, so a refusal asserted only on such a helper can pass
// while the real return completes (BUG-0147). Exceptions are listed with their reason and fail
// once the return does refuse, so a stale exception cannot linger.
import { readFileSync } from 'node:fs';
import { evaluate } from '../engine/dist/eval.js';
import { loadCanonical } from '../engine/dist/canonical.js';
import { loadCases } from '../engine/dist/fixtures.js';
import { loadInterview } from '../engine/dist/interview.js';

const exceptions = JSON.parse(readFileSync(new URL('./refusal_reach_exceptions.json', import.meta.url), 'utf8'));
const data = loadCanonical();
const targets = loadInterview('full').targets;
const failures = [];
let checked = 0;
for (const c of loadCases().cases) {
  if (!Object.values(c.expect ?? {}).some(e => e.kind === 'refusal')) continue;
  checked += 1;
  const values = evaluate(data, c.inputs, targets).values;
  const refused = targets.some(t => values.get(t)?.kind === 'refusal');
  if (!refused && !(c.id in exceptions)) failures.push(`${c.id}: asserts a refusal, but the full interview does not refuse this return`);
  if (refused && c.id in exceptions) failures.push(`${c.id}: listed in refusal_reach_exceptions.json but the return is refused; remove the exception`);
}
for (const id of Object.keys(exceptions)) if (!loadCases().cases.some(c => c.id === id)) failures.push(`${id}: exception names no fixture`);
console.log(`refusal reach: ${checked} refusal fixtures checked against the full interview; ${Object.keys(exceptions).length} listed exception(s)`);
for (const f of failures) console.log('FAIL ' + f);
process.exit(failures.length ? 1 : 0);
