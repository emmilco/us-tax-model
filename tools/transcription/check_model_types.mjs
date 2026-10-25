// Source-review validation. Only parses data and invokes the build's reference/type checker.
// No candidate expression is executed; the model receives none of this host-side context.
import { readFileSync } from 'node:fs';
import { Ajv2020 } from 'ajv/dist/2020.js';
import { checkExpressionTypes } from '../../engine/dist/check.js';

const schema = JSON.parse(readFileSync(new URL('../../schema/data.schema.json', import.meta.url), 'utf8'));
const ajv = new Ajv2020({ allErrors: true, strict: false });
const validateExpression = ajv.compile({ $schema: schema.$schema, $defs: schema.$defs, $ref: '#/$defs/expr' });

const request = JSON.parse(readFileSync(0, 'utf8'));
const { context, form, lines } = request;
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
process.stdout.write(JSON.stringify({ policy: 'project-expression-types-v1', errors }));
