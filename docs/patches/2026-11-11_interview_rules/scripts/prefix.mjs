// usage: node prefix.mjs <repo> : are the first 12 of sampleReturns(n, 11) the same for n = 12, 200? how many distinct returns?
import { pathToFileURL } from "node:url";
const repo = process.argv[2];
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const { loadCanonical } = await imp("canonical.js");
const gen = await imp("generate.js");
const data = loadCanonical();
const t0 = performance.now();
const a = gen.sampleReturns(data, 12, 11).map((x) => JSON.stringify(x));
const b = gen.sampleReturns(data, 2000, 11).map((x) => JSON.stringify(x));
console.log(`generate 2000: ${((performance.now() - t0) / 1000).toFixed(1)} s`);
console.log("first 12 of 2000 equal the 12:", a.every((x, i) => x === b[i]));
console.log("distinct among 12:", new Set(a).size, "distinct among 2000:", new Set(b).size);
const rs = b.map((x) => JSON.parse(x));
const has = rs.filter((r) => (r["$f1095a"] ?? []).length);
console.log("of 2000: with a Form 1095-A", has.length, "with a monthly one", has.filter((r) => r["$f1095a"].some((k) => r[`f1095a[${k}].uniform`] === false)).length);
console.log("of first 12: indexes with a Form 1095-A", rs.slice(0, 12).map((r, i) => [(r["$f1095a"] ?? []).map((k) => r[`f1095a[${k}].uniform`] ? "uniform" : "monthly"), i]).filter(([u]) => u.length).map(([u, i]) => `${i}:${u}`).join(" "));
