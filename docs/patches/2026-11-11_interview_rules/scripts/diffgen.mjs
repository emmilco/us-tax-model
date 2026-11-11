// usage: node diffgen.mjs <repoA> <repoB> <old id> <new id>: the 12 seed-11 generated returns of each; which keys differ once the id is mapped
import { pathToFileURL } from "node:url";
import { writeFileSync } from "node:fs";
const [A, B, oldId, newId] = process.argv.slice(2);
const load = async (repo) => { const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href); const { loadCanonical } = await imp("canonical.js"); const gen = await imp("generate.js"); return gen.sampleReturns(loadCanonical(), 12, 11); };
const a = await load(A), b = await load(B);
writeFileSync("/tmp/f1095a/out/r1_generated_0.json", JSON.stringify(b[0], null, 1));
writeFileSync("/tmp/f1095a/out/base_generated_0.json", JSON.stringify(a[0], null, 1));
const groups = {};
a.forEach((x, i) => {
  const y = b[i];
  const xm = Object.fromEntries(Object.entries(x).map(([k, v]) => [k === oldId ? newId : k, v]));
  const keys = new Set([...Object.keys(xm), ...Object.keys(y)]);
  const diff = [...keys].filter((k) => JSON.stringify(xm[k]) !== JSON.stringify(y[k]));
  const fam = [...new Set(diff.map((k) => k.replace(/\[[^\]]*\]/g, "").replace(/^\$/, "").split(/[.@]/)[0] + (/(\.edu|edu_)/.test(k) ? ".edu*" : "")))].sort();
  console.log(`generated.${i}: ${diff.length} keys differ of ${keys.size}; families: ${fam.join(", ")}`);
  for (const k of diff) (groups[k.replace(/\[[^\]]*\]/g, "[]")] ??= 0, groups[k.replace(/\[[^\]]*\]/g, "[]")]++);
});
console.log("differing key templates:", Object.keys(groups).sort().join(" "));
