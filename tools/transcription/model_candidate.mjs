// Prepare model data with the shared schema/reference/type rules; no evaluation here.
import { readFileSync } from 'node:fs';
import { Ajv2020 } from 'ajv/dist/2020.js';
import { checkExpressionTypes } from '../../engine/dist/check.js';

const schema = JSON.parse(readFileSync(new URL('../../schema/data.schema.json', import.meta.url), 'utf8'));
const ajv = new Ajv2020({ allErrors: true, strict: false });
const validateExpression = ajv.compile({ $schema: schema.$schema, $defs: schema.$defs, $ref: '#/$defs/expr' });

export function prepareCandidate(context, form, lines) {
const all = [...context.forms, ...context.defs];
const original = all.find(doc => doc.id === form);
if (!original) throw new Error(`unknown review document ${form}`);
const published = new Map(original.lines.map(line => [line.id, line]));
const inputs = original.lines.filter(line => line.expr.op === 'input');
const errors = [], computed = [];
const seen = new Set();
for (const line of lines) {
  if (seen.has(line.id)) errors.push({ line: line.id, message: 'duplicate model line id' });
  seen.add(line.id);
  if (!line.expr || typeof line.expr !== 'object') {
    errors.push({ line: line.id, message: 'malformed model expression' });
    continue;
  }
  if (!validateExpression(line.expr)) {
    const details = [...validateExpression.errors].sort((a, b) => b.instancePath.length - a.instancePath.length).slice(0, 3);
    errors.push({ line: line.id, message: `malformed expression (project schema): ${ajv.errorsText(details)}` });
  }
  const namespace = line.id.split('.')[0];
  if (namespace !== form && all.some(doc => doc.id === namespace))
    errors.push({ line: line.id, message: 'model redefined a foreign interface' });
  const existing = published.get(line.id);
  if (existing && line.type !== existing.type)
    errors.push({ line: line.id, message: 'model changed a published result type' });
  if (existing?.expr.op === 'input') {
    if (line.expr.op !== 'input' || line.type !== existing.type)
      errors.push({ line: line.id, message: 'model changed a published input interface' });
    continue; // Use the published input's type, never let the model redefine it.
  }
  if (line.expr.op === 'input') errors.push({ line: line.id, message: 'model introduced an input outside the closed interface' });
  computed.push(line);
}
const candidate = { ...original, lines: [...inputs, ...computed] };
const replace = docs => docs.map(doc => doc.id === form ? candidate : doc);
const data = { ...context, forms: replace(context.forms), defs: replace(context.defs) };
errors.push(...checkExpressionTypes(data, form));
// Refusal syntax is outside the expression schema, but is still executable IR.
// Validate every declared gate, including unused helpers, without evaluating it.
const gateOwners = new Map(), checks = [];
for (const line of candidate.lines) {
  if (line.refuses !== undefined && !Array.isArray(line.refuses)) {
    errors.push({ line: line.id, message: 'invalid refusal list' });
    continue;
  }
  for (const refusal of line.refuses ?? []) {
    const when = typeof refusal === 'string' ? refusal : refusal?.when;
    if (typeof when !== 'string' || !when || (typeof refusal === 'object' && (
      Object.keys(refusal).some(key => !['when', 'when_known', 'form', 'remedy', 'cite'].includes(key)) ||
      ('when_known' in refusal && refusal.when_known !== true)))) {
      errors.push({ line: line.id, message: 'invalid refusal or consistency-check declaration' });
      continue;
    }
    let id = `${form}.__type_gate_${checks.length}`;
    while (seen.has(id) || published.has(id)) id += '_';
    gateOwners.set(id, line.id);
    checks.push({ id, type: 'Bool', expr: { op: 'test', eq: [when, { const: true }] } });
  }
}
if (checks.length) {
  const checked = { ...candidate, lines: [...candidate.lines, ...checks] };
  const replacing = docs => docs.map(doc => doc.id === form ? checked : doc);
  errors.push(...checkExpressionTypes({ ...data, forms: replacing(data.forms), defs: replacing(data.defs) }, form)
    .filter(error => gateOwners.has(error.line)).map(error => ({ ...error, line: gateOwners.get(error.line) })));
}
return { data, candidate, errors };
}
