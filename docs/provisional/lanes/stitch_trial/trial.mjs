// Trial of the stitch lane (docs/provisional/lanes/stitch.md, part 3): gives questions of the built "full" interview
// other places (order, seq) in memory, then walks the background return, checks the tick-box groups, and walks the
// coverage rows of credits.yaml. Writes nothing. Run after a build.
// Usage: node trial.mjs <worktree> <placements.json> [--rows [--ends]] [--reorder | --split] [--drop-group]
//   placements.json   { "<input>": [order, seq] | [order], ..., "#lists": { "<line>": [gate, ...] } }
//                     ([order] alone removes seq; "#lists" is read by --reorder)
//   --rows            walk the rows of interview/2025/coverage/credits.yaml; --ends prints every row's end
//   --reorder         the refusal entries of the lines named in "#lists", in the order given there
//   --split           each refusal entry of s3.line7 and s3.line14 on a line of its own, the line their sum
//   --drop-group      the bank without its tick-box groups
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { join } from "node:path";
const [root, placementsPath, ...flags] = process.argv.slice(2);
const dist = join(root, "engine/dist");
const require = createRequire(join(root, "package.json"));
const { parse } = require("yaml");
const { loadCanonical } = await import(join(dist, "canonical.js"));
const iv = await import(join(dist, "interview.js"));
const cov = await import(join(dist, "interview-coverage.js"));
const tick = await import(join(dist, "tick-groups-check.js"));

const placements = JSON.parse(readFileSync(placementsPath, "utf8"));
const data = loadCanonical();
const config = iv.loadInterview("full");
// The form variants, in memory.
const s3 = data.forms.find((d) => d.id === "s3");
const lists = placements["#lists"] ?? {}; delete placements["#lists"];
if (flags.includes("--reorder")) for (const [id, order] of Object.entries(lists)) {
  const line = s3.lines.find((l) => l.id === id);
  const by = new Map(line.refuses.map((r) => [r.when, r]));
  if (order.length !== line.refuses.length || order.some((w) => !by.has(w))) throw new Error(`${id}: the order must name each of ${[...by.keys()].join(", ")}`);
  line.refuses = order.map((w) => by.get(w));
}
if (flags.includes("--split")) for (const id of ["s3.line7", "s3.line14"]) {
  const line = s3.lines.find((l) => l.id === id);
  const parts = line.refuses.map((r, i) => ({ ...line, id: `${id}_part${i + 1}`, printed: "(helper)", label: `${line.label}: ${r.form}`, refuses: [r] }));
  s3.lines.splice(s3.lines.indexOf(line), 0, ...parts);
  line.expr = { op: "sum", of: parts.map((p) => p.id) };
  delete line.refuses;
}
for (const q of config.questions) {
  const p = placements[q.input];
  if (!p) continue;
  q.order = p[0];
  if (p.length > 1) q.seq = p[1]; else delete q.seq;
  if (flags.includes("--drop-group")) { delete q.group; delete q.tick; }
}
if (flags.includes("--drop-group")) delete config.groups;
for (const k of Object.keys(placements)) if (!config.questions.some((q) => q.input === k)) throw new Error(`no question ${k}`);

const background = cov.backgroundOf(data, config, "full");
const bank = new Map(config.questions.map((q) => [q.input, q]));
console.log(`background return: ${background.steps.length} questions`);
const watch = (t) => /^(s3|ftc)\./.test(t) || placements[t];
let last = null;
for (const s of background.steps) {
  const t = iv.questionTemplate(s.input);
  const q = bank.get(t);
  if (watch(t)) console.log(`  ${String(s.n).padStart(3)}  order ${q.order}${q.seq !== undefined ? ` seq ${q.seq}` : ""}  ${s.input} = ${JSON.stringify(s.value)}${last !== null && q.order < last ? "   <-- order re-entered (asked late)" : ""}`);
  last = q.order;
}
// Orders asked out of sequence anywhere in the background walk.
let prev = -Infinity; const late = [];
for (const s of background.steps) { const q = bank.get(iv.questionTemplate(s.input)); if (q.order < prev) late.push(`${s.n} ${s.input} (order ${q.order} after ${prev})`); prev = Math.max(prev, q.order); }
console.log(`asked after a later order number had begun: ${late.length ? "\n  " + late.join("\n  ") : "none"}`);

if (config.groups) {
  const t = tick.tickGroupWalkProblems(data, config, background);
  console.log(`tick-groups: ${t.checked} shown whole, ${t.problems.length} problem(s)`);
  for (const p of [...t.notes, ...t.problems]) console.log(`  ${p}`);
}
if (flags.includes("--rows")) {
  const ctx = cov.loadCtx();
  ctx.data = data; ctx.configs.full = config; ctx.backgrounds.full = background;
  const file = parse(readFileSync(join(root, "interview/2025/coverage/credits.yaml"), "utf8"));
  const run = cov.checkFiles(ctx, [{ name: "credits.yaml", file }]);
  let bad = 0;
  for (const r of run.results) {
    const end = r.walk ? (r.walk.end.kind === "refused" ? `refused ${r.walk.end.gate}` : r.walk.end.kind === "asks" ? `asks ${r.walk.end.input}` : r.walk.end.kind) : "not walked";
    if (r.problems.length) { bad++; console.log(`  FAIL ${r.row.id}: after ${r.walk?.steps.length} q: ${end}\n      ${r.problems.join("\n      ")}`); }
    else if (flags.includes("--ends")) console.log(`  ok   ${r.row.id}: after ${r.walk.steps.length} q: ${end}`);
  }
  for (const p of run.problems) console.log(`  file: ${p}`);
  console.log(`credits rows: ${run.results.length} walked, ${bad} failing, ${run.problems.length} file problem(s)`);
}
