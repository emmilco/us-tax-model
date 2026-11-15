// Trial tool of lane rc (docs/provisional/lanes/rc.md). It reads the working copy of interview/2025/questions.yaml and
// gives the built "full" interview, in memory, the bank's order, seq, group and tick (and its groups), so that a bank
// change can be walked without the build. It writes nothing but the walks asked for. Run after a build of the forms as
// they stand; a change to a form, a prompt or a help text needs the build (prompts and help are the built ones here).
// Usage: node trial.mjs <worktree> [--personas a,b | --all] [--rows file.yaml,...] [--range lo-hi] [--lists lists.json]
//                                   [--out DIR] [--list]
//   --personas   walk these personas (names without .yaml); --all walks every one
//   --rows       walk the rows of these files of interview/2025/coverage/
//   --range      the order numbers whose questions are counted apart for each persona (default 250-319)
//   --lists      { "<line>": [gate, ...] }: the refusal entries of these lines in this order, in memory
//   --out        write each persona's transcript there
//   --list       print each persona's questions in the range, one line each
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
import { join } from "node:path";
const [root, ...args] = process.argv.slice(2);
const opt = (n) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : undefined; };
const dist = join(root, "engine/dist");
const require = createRequire(join(root, "package.json"));
const { parse } = require("yaml");
const iv = await import(join(dist, "interview.js"));
const cov = await import(join(dist, "interview-coverage.js"));
const tick = await import(join(dist, "tick-groups-check.js"));
const rules = await import(join(dist, "tick-groups.js"));
const walk = await import(join(dist, "draft-walk.js"));

const ctx = cov.loadCtx();
const data = ctx.data;
const config = iv.loadInterview("full");
const bank = parse(readFileSync(join(root, "interview/2025/questions.yaml"), "utf8")).bank;
const forms = data.forms;
if (opt("--lists")) for (const [id, order] of Object.entries(JSON.parse(readFileSync(opt("--lists"), "utf8")))) {
  const line = forms.flatMap((f) => f.lines).find((l) => l.id === id);
  const by = new Map(line.refuses.map((r) => [r.when, r]));
  if (order.length !== line.refuses.length || order.some((w) => !by.has(w))) throw new Error(`${id}: the order must name each of ${[...by.keys()].join(", ")}`);
  line.refuses = order.map((w) => by.get(w));
}
const byInput = new Map(bank.questions.map((q) => [q.input, q]));
for (const q of config.questions) {
  const b = byInput.get(q.input);
  if (!b) throw new Error(`the bank has no ${q.input}`);
  q.order = b.order;
  if (b.seq !== undefined) q.seq = b.seq; else delete q.seq;
  if (b.group) { q.group = b.group; q.tick = b.tick; } else { delete q.group; delete q.tick; }
}
const collectionChain = (id) => { const parent = forms.find((d) => d.id === id)?.collection?.parent; return parent ? [...collectionChain(parent), id] : [id]; };
const chainOf = (input) => {
  if (input.startsWith("$")) return collectionChain(input.slice(1)).slice(0, -1);
  const doc = forms.find((d) => d.lines.some((l) => l.id === input));
  return doc?.collection ? collectionChain(doc.id) : [];
};
for (const q of config.questions) delete q.at;
const live = new Map(config.questions.map((q) => [q.input, q]));
for (const [input, at] of iv.blockPlaces(config.questions, chainOf)) { const q = live.get(input); if (q) q.at = at; }
const seen = new Map();
for (const q of config.questions) if (q.seq !== undefined) { const k = `${q.order}/${q.seq}`; if (seen.has(k)) console.log(`BUILD WOULD REFUSE: ${q.input} and ${seen.get(k)} both at ${k}`); seen.set(k, q.input); }
const inputLines = new Map(forms.flatMap((d) => d.lines.filter((l) => l.expr.op === "input").map((l) => [l.id, { line: l, form: d }])));
const opened = rules.opensMap([...forms, ...(data.defs ?? [])]);
const problems = rules.tickGroupProblems(bank.groups, config.questions, {
  typeOf: (input) => inputLines.get(input)?.line.type,
  formOf: (input) => { const d = inputLines.get(input)?.form; return d ? { id: d.id, collection: d.collection !== undefined, frame: bank.frames[d.id] ?? "" } : undefined; },
  opens: (input) => opened.get(input) ?? [],
});
for (const p of problems) console.log(`BUILD WOULD REFUSE: ${p}`);
config.groups = (bank.groups ?? []).flatMap((g) => {
  const member = config.questions.find((q) => q.group === g.id);
  const form = member ? inputLines.get(member.input)?.form : undefined;
  return form ? [{ id: g.id, heading: (bank.frames[form.id] ?? "") + g.heading }] : [];
});
if (!config.groups.length) delete config.groups;

const background = cov.backgroundOf(data, config, "full");
console.log(`background return: ${background.steps.length} questions`);
if (config.groups) {
  const t = tick.tickGroupWalkProblems(data, config, background);
  console.log(`tick-groups: ${t.checked} shown whole on the background return, ${t.problems.length} problem(s)`);
  for (const p of [...t.notes, ...t.problems]) console.log(`  ${p}`);
}
const [lo, hi] = (opt("--range") ?? "250-319").split("-").map(Number);
const names = args.includes("--all")
  ? require("node:fs").readdirSync(join(root, "interview/2025/personas")).filter((f) => f.endsWith(".yaml")).map((f) => f.slice(0, -5)).sort()
  : (opt("--personas") ?? "").split(",").filter(Boolean);
if (names.length) {
  const w = walk.walkCtx(ctx, config, background);
  for (const name of names) {
    const pw = walk.walkPersona(w, walk.readPersona(join(root, "interview/2025/personas", `${name}.yaml`)));
    const f = walk.figures(pw.asked);
    const mine = pw.asked.filter((a) => { const o = live.get(iv.questionTemplate(a.shown.input))?.order ?? -1; return o >= lo && o <= hi; });
    const g = walk.figures(mine);
    const end = pw.end.kind === "refused" ? `refused at ${pw.end.gate}` : pw.end.kind;
    console.log(`${name}: ${f.asked} questions on ${f.steps} steps, ${f.prompt} prompt words, ${f.help} help words, ${end}; in ${lo}-${hi}: ${g.asked} questions on ${g.steps} steps, ${g.prompt} prompt words, ${g.help} help words; ${pw.problems.length} problem(s)`);
    for (const p of pw.problems) console.log(`    ${p}`);
    if (args.includes("--list")) {
      let prev = -1;
      for (const a of mine) {
        const q = live.get(iv.questionTemplate(a.shown.input));
        console.log(`    ${String(a.n).padStart(3)} ${a.step === prev ? " +" : "  "} ${q.order}/${q.seq ?? "-"}  ${a.shown.input} = ${JSON.stringify(a.value)}${a.tick ? `   [${a.tick.group}: ${a.tick.label}]` : ""}`);
        prev = a.step;
      }
    }
    if (opt("--out")) { mkdirSync(opt("--out"), { recursive: true }); writeFileSync(join(opt("--out"), `${name}.md`), walk.renderTranscript(pw)); }
  }
}
if (opt("--rows")) {
  ctx.configs.full = config; ctx.backgrounds.full = background;
  let bad = 0, n = 0;
  for (const name of opt("--rows").split(",")) {
    const file = parse(readFileSync(join(root, "interview/2025/coverage", name), "utf8"));
    const run = cov.checkFiles(ctx, [{ name, file }]);
    for (const r of run.results) {
      n++;
      if (!r.problems.length) continue;
      bad++;
      const end = r.walk ? (r.walk.end.kind === "refused" ? `refused ${r.walk.end.gate}` : r.walk.end.kind === "asks" ? `asks ${r.walk.end.input}` : r.walk.end.kind) : "not walked";
      console.log(`  FAIL ${name} ${r.row.id}: after ${r.walk?.steps.length} q: ${end}\n      ${r.problems.join("\n      ")}`);
    }
    for (const p of run.problems) console.log(`  file ${name}: ${p}`);
  }
  console.log(`rows: ${n} walked, ${bad} failing`);
}
