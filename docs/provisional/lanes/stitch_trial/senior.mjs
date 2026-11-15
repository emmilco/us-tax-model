// One walk at the map's numbers: a filer of 65 or over who bought a vehicle from a dealer that took the credit.
import { readFileSync } from "node:fs";
import { join } from "node:path";
const [root, placementsPath] = process.argv.slice(2);
const dist = join(root, "engine/dist");
const { loadCanonical } = await import(join(dist, "canonical.js"));
const iv = await import(join(dist, "interview.js"));
const cov = await import(join(dist, "interview-coverage.js"));
const placements = JSON.parse(readFileSync(placementsPath, "utf8")); delete placements["#lists"];
const data = loadCanonical();
const config = iv.loadInterview("full");
for (const q of config.questions) { const p = placements[q.input]; if (p) { q.order = p[0]; if (p.length > 1) q.seq = p[1]; else delete q.seq; } }
const background = cov.backgroundOf(data, config, "full");
const ctx = cov.loadCtx(); ctx.data = data; ctx.configs.full = config; ctx.backgrounds.full = background;
const bank = new Map(config.questions.map((q) => [q.input, q]));
for (const [name, answers] of [
  ["under 65, dealer took the vehicle credit", { "s3.ev": true, "s3.ev_dealer": true }],
  ["65 or over, dealer took the vehicle credit", { "person[taxpayer].age65": true, "person[taxpayer].died_before_65": false, "s3.ev": true, "s3.ev_dealer": true, "s3.elderly_credit": false }],
]) {
  let w; const added = [];
  for (let i = 0; i < 60; i++) {
    w = cov.walkRow(ctx, { id: "x", design: "", situation: "", answers, expect: { refused: "s3.ev_dealer_if_ev" } }, { profile: "full", sets: {} });
    if (w.end.kind === "unanswered") { answers[w.end.input] = false; added.push(`${w.end.input}=false`); continue; }
    if (w.end.kind === "rejected" && answers[w.end.input] === false) { answers[w.end.input] = 0; added.push(`${w.end.input}=0`); continue; }
    break;
  }
  if (added.length) console.log(`  (answers added so the walk can go on: ${added.join(", ")})`);
  console.log(`${name}: ${w.steps.length} answers, end ${w.end.kind}${w.end.gate ? " at " + w.end.gate : ""}${w.end.input ? " " + w.end.input : ""}`);
  const at = w.steps.findIndex((s) => s.input === "s3.ev_dealer");
  for (const s of w.steps.slice(at)) console.log(`   ${s.n}  order ${bank.get(iv.questionTemplate(s.input)).order}  ${s.input} = ${JSON.stringify(s.value)} (${s.from})`);
}
