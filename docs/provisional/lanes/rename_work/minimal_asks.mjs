// The minimal returns of interview-rules ("every gate closed", and each existence gate opened alone), walked with the
// closed answer given where the check would stop: lists, per walk, every gated input the walk asks while its gate
// counts as closed. Run from the worktree root after a build: node docs/provisional/lanes/rename_work/minimal_asks.mjs
import { pathToFileURL } from "node:url";
const d = (m) => import(pathToFileURL(process.cwd() + "/engine/dist/" + m).href);
const { loadCanonical } = await d("canonical.js");
const { loadInterview, questionTemplate } = await d("interview.js");
const R = await d("interview-rules.js");
const { gatesOf } = await d("gates.js");
const data = loadCanonical();
const gates = R.existenceGates(data);
const hits = new Map();
function run(profile, open) {
  const config = loadInterview(profile);
  const base = R.minimalAnswers(data, config, profile, open);
  const allowed = open ? gates.get(open.input) ?? new Set() : new Set();
  const closed = new Set(gatesOf(data).map((g) => g.input).filter((i) => !allowed.has(i)));
  const answers = (key, current) => {
    const a = base(key, current);
    if (a) return a;
    const t = questionTemplate(key);
    if (closed.has(t)) (hits.get(t) ?? hits.set(t, new Set()).get(t)).add(`${profile}: ${open ? `${open.input} = ${JSON.stringify(open.value)} alone` : "every gate closed"}`);
    return { value: R.closedAnswer(data, config, key, current) };
  };
  return R.walk(data, config, answers, R.bankOrder(config), 800, () => {});
}
for (const profile of ["full", "ny"]) {
  const w = run(profile, null);
  const asked = new Map(w.events.map((e) => [e.input, e.value]));
  for (const g of [...gates.keys()].sort()) {
    if (!asked.has(g)) continue;
    const t = g;
    for (const value of [true]) { try { run(profile, { input: g, value }); } catch (e) { /* not a Bool gate */ } }
  }
}
for (const [t, where] of [...hits].sort()) console.log(`${t}\n    ${[...where].slice(0, 4).join("\n    ")}${where.size > 4 ? `\n    (${where.size} walks)` : ""}`);
