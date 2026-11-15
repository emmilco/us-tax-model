// usage: node search.mjs <worktree> <targets.json> [--ny]
//   targets.json: {caseId: person}. For each case, tries every candidate birth (year and the narrow answers its year asks)
//   for that person, the case's other inputs as they now stand, and prints {caseId: [passing candidates]}.
import { readFileSync } from "node:fs";
import { isDeepStrictEqual } from "node:util";
import { join } from "node:path";
const root = process.argv[2];
const targets = JSON.parse(readFileSync(process.argv[3], "utf8"));
const ny = process.argv.includes("--ny");
const { loadCanonical } = await import(join(root, "engine/dist/canonical.js"));
const fi = await import(join(root, "engine/dist/fixture-inputs.js"));
const { evaluateAll } = await import(join(root, "engine/dist/eval.js"));
const { resultToJson } = await import(join(root, "engine/dist/output.js"));
const data = loadCanonical();
const j = ny ? "ny" : "federal";
const dir = join(root, ny ? "fixtures/ny/2025" : "fixtures/2025");
const CUTS = [1961, 2001, 2002, 2007, 2008];
const NARROW = ["birth_year", "born_jan1", "under16_at_year_end", "age50_at_year_end", "age55_at_year_end", "died_at_64", "simple_age_at_year_end"];
const CANDS = [];
for (let y = 1930; y <= 2015; y++) {
  let base = [{ y }];
  if (CUTS.includes(y)) base = [{ y, j: false }, { y, j: true }];
  if (y === 1976) base = [{ y, a: false }, { y, a: true }];
  if (y === 1971) base = [{ y, a55: false }, { y, a55: true }];
  if (y === 2010) base = [{ y, u: true }, { y, u: false }];
  for (const b of base) {
    if (y === 1960 || (y === 1961 && b.j)) CANDS.push({ ...b, d: false }, { ...b, d: true });
    else CANDS.push(b);
  }
}
function keys(p, c) {
  const o = { [`person[${p}].birth_year`]: c.y };
  if (CUTS.includes(c.y)) o[`person[${p}].born_jan1`] = c.j ?? false;
  if (c.y === 2010) o[`person[${p}].under16_at_year_end`] = c.u ?? true;
  if (c.y === 1976) o[`person[${p}].age50_at_year_end`] = c.a ?? false;
  if (c.y === 1971) o[`person[${p}].age55_at_year_end`] = c.a55 ?? false;
  if (c.y === 1960 || (c.y === 1961 && c.j)) o[`person[${p}].died_at_64`] = c.d ?? false;
  return o;
}
const out = {};
for (const f of fi.caseFiles(dir)) {
  const cases = JSON.parse(readFileSync(join(dir, f), "utf8")).cases ?? [];
  for (const c of cases) {
    if (!(c.id in targets)) continue;
    const p = targets[c.id];
    const base = Object.fromEntries(Object.entries(c.inputs).filter(([k]) => !NARROW.some((n) => k === `person[${p}].${n}`)));
    const pass = [];
    for (const cand of CANDS) {
      const inputs = { ...base, ...keys(p, cand) };
      let ok = true;
      try {
        const resolved = fi.resolveCase({ id: c.id, inputs }, f, data, j);
        const parsed = JSON.parse(resultToJson(evaluateAll(data, resolved)));
        for (const [k, e] of Object.entries(c.expect ?? {})) { const a = parsed.values[k]?.value; if (!a || !isDeepStrictEqual(a, e)) { ok = false; break; } }
        if (ok && c.expect_refusal !== undefined) ok = false; // refusal cases are checked by the fixture run itself
      } catch (e) { ok = false; }
      if (ok) pass.push(cand);
    }
    out[c.id] = pass;
  }
}
console.log(JSON.stringify(out));
