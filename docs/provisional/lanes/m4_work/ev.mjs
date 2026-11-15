// Lane m4 scratch: evaluate case inputs (JSON file: {id: {inputs, targets}} or a cases file) and print the values of
// the named lines. usage: node ev.mjs CASES.json [--ny]
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
const ROOT = resolve(import.meta.dirname, "../../../..");
const { loadCanonical } = await import(join(ROOT, "engine/dist/canonical.js"));
const { evaluate } = await import(join(ROOT, "engine/dist/eval.js"));
const data = loadCanonical();
const cases = JSON.parse(readFileSync(process.argv[2], "utf8"));
for (const [id, c] of Object.entries(cases)) {
  const r = evaluate(data, c.inputs, c.targets);
  const out = {};
  for (const t of c.targets) out[t] = r.derivations.get(t)?.value;
  console.log(JSON.stringify({ id, values: out }));
}
