// How long the federal interview is per return, and how much of it a different question order could save
// (`interview-length`). Deterministic and free: it walks returns with the evaluator, as interview-rules does, and
// calls no model. Only the evaluator's reachability hides a question and order never changes a value, so the one
// saving open to the interview is order: asking first a question whose answer makes other open questions
// unreachable. Each return is walked three ways, and each walk must end with the same status and values:
//
//   static     the interview's own order (bank order, then key)
//   oracle     knowing the return's answers: at each state the first open question (bank order) that the complete
//              return's evaluation reads. No order can ask fewer questions than the inputs the complete return
//              reads (an input it reads is reachable, unanswered, at every state that lacks it; see `floorOf`), and
//              this order asks exactly those, so it is the least any answer-dependent order can ask
//   expected   not knowing the answers: at each state, for every open question, the evaluator is asked which other
//              open questions a closed answer (false, 0, an empty roster) would make unreachable; the question
//              asked is the one with the most expected removals, P(closed) times that count, P from
//              interview/<year>/gate_frequencies.yaml (the share answering yes, by input template; DEFAULT_SHARE
//              where the file has none), ties in bank order. It probes; it never answers for the filer
//
// Returns: the Stage 5 whole returns and the generated returns (sampleReturns, as interview-rules) on the full
// profile, and the minimal returns of interview-rules (every existence gate closed, then each opened alone). A refused return is counted under static only. An answer is "closed" when it is
// false, zero or an empty roster.
//
//   interview-length [--write] [--self-test] [--what-if]
//     The returns are measured on INTERVIEW_WORKERS worker threads (default defaultWorkers() of pool.ts); the report
//     and the problems are the same for every count, and 1 measures them in one thread.
//     --write       writes reports/<year>/interview_length.md, keeping the hand-written findings below its marker
//     --what-if     today's order only, as built and with each proposed umbrella gate applied in memory
//                   (umbrella-what-if.ts), then with the recommended ones together; with --write, writes
//                   reports/<year>/umbrella_savings.md
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { parse } from "yaml";
import { loadCanonical } from "./canonical.js";
import { inputMeta, loadInterview, questionTemplate, statusParts, type InterviewData } from "./interview.js";
import {
  bankOrder, existenceGates, fixtureCases, GENERATED, leakPair, minimalAnswers, plantLeak, readInputs, replayed, replayedState, SEED, Unanswered, walk,
  type Answers, type Walk,
} from "./interview-rules.js";
import { sampleReturns } from "./generate.js";
import { gatesOf } from "./gates.js";
import { TaskWorkers, walkWorkers } from "./pool.js";
import { YEAR } from "./year.js";
import { applyUmbrellas, RECOMMENDED, UMBRELLAS, umbrellaAnswer, unGated, type Umbrella } from "./umbrella-what-if.js";
import type { CanonicalData, Inputs } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const REPORT = resolve(ROOT, "reports", String(YEAR), "interview_length.md");
const WHAT_IF_REPORT = resolve(ROOT, "reports", String(YEAR), "umbrella_savings.md");
const FREQUENCIES = resolve(ROOT, "interview", String(YEAR), "gate_frequencies.yaml");
/** The share answering yes assumed for a question the frequency file does not name: no information. */
const DEFAULT_SHARE = 0.5;
const MARKER = "<!-- Hand-written findings below this line are kept when the tool rewrites the report. -->";
/** The hand-written text below the marker of a report, its leading newlines reduced to one: the report puts it on the
 * line after the marker, so one blank line separates them however often the report is rewritten. */
const keptAfterMarker = (old: string): string =>
  old.includes(MARKER) ? old.slice(old.indexOf(MARKER) + MARKER.length).replace(/^\n+/, "\n") : "\n";
const BOUND = 800;

/** A closed answer: false, zero or an empty roster. */
export function isClosed(value: unknown): boolean {
  return value === false || value === 0 || (Array.isArray(value) && value.length === 0);
}

/** The share answering yes, by input template, from the frequency file's situations: each ref that names an input
 * template (it has a dot or starts with `$`) takes the situation's share, the largest where several name it. */
export function sharesFrom(text: string): Map<string, number> {
  const doc = parse(text) as { situations: Record<string, { refs?: unknown[]; share?: number }> };
  const out = new Map<string, number>();
  for (const s of Object.values(doc.situations)) {
    if (typeof s.share !== "number") continue;
    for (const r of s.refs ?? []) {
      if (typeof r !== "string" || !(r.startsWith("$") || r.includes("."))) continue;
      out.set(r, Math.max(out.get(r) ?? 0, s.share));
    }
  }
  return out;
}

/** The answer the expected order probes with: false, zero or an empty roster; none for an enum or `$person`. */
function probeAnswer(data: CanonicalData, key: string): unknown {
  if (key.startsWith("$")) return questionTemplate(key) === "$person" ? undefined : [];
  const t = inputMeta(data, key).type;
  return t === "Bool" ? false : t === "Enum" ? undefined : 0;
}

/** A state's inputs as a key: its entries in key order, hashed. */
export function stateKey(inputs: Inputs): string {
  return createHash("sha1").update(JSON.stringify(Object.keys(inputs).sort().map((k) => [k, inputs[k]]))).digest("base64");
}

/** A state as the walks and probes read it: its status, the reachable inputs the evaluation reads, and those the reach
 * pass adds, computed only when asked for (statusParts in interview.ts). */
interface State { status: string; read: Set<string>; pass: (() => string[]) | null; ahead?: Set<string>; reachable?: string[] }
const aheadOf = (st: State): Set<string> => { if (!st.ahead) { st.ahead = new Set(st.pass!()); st.pass = null; } return st.ahead; };
const reachableOf = (st: State): string[] => (st.reachable ??= [...st.read, ...aheadOf(st)].sort());

/** The states met, by data and bank, then by state (stateKey): the expected order's probes, and the states of the
 * walks. A state's status and reachable inputs are a function of the data, the bank and the state, and the walks of
 * returns that have answered alike so far meet the same states (the minimal returns share nearly all of theirs), so
 * each is evaluated once per thread. Cleared when it holds STATES_KEPT states. */
const met = new WeakMap<CanonicalData, WeakMap<InterviewData, Map<string, State>>>();
const STATES_KEPT = 100_000;
function statesOf(data: CanonicalData, config: InterviewData): (inputs: Inputs) => State {
  let byConfig = met.get(data);
  if (!byConfig) met.set(data, (byConfig = new WeakMap()));
  let memo = byConfig.get(config);
  if (!memo) byConfig.set(config, (memo = new Map()));
  const states = memo;
  return (inputs) => {
    const key = stateKey(inputs);
    const hit = states.get(key);
    if (hit) return hit;
    const { status, read, ahead } = statusParts(data, config, inputs);
    const st: State = { status, read, pass: ahead };
    if (states.size >= STATES_KEPT) states.clear();
    states.set(key, st);
    return st;
  };
}

/** What walk() reads of a state, from the states met: interviewStatus's status and reachable inputs. */
export function statusOf(data: CanonicalData, config: InterviewData): (inputs: Inputs) => { status: string; reachableInputs: string[] } {
  const state = statesOf(data, config);
  return (inputs) => { const st = state(inputs); return { status: st.status, reachableInputs: reachableOf(st) }; };
}

/** The expected order: the open question with the most expected removals under a closed answer, ties in bank order.
 * A probe's removals are the open questions unreachable after it, so an open question the evaluation reads after it
 * (`read`) is not removed, and the reach pass is run only for a probe whose other open questions could give a score
 * as high as the best found: the probes are taken by that bound, highest first. The questions with the best score,
 * in the order of `open`, are the same as when every probe is scored in that order. */
export function expectedOrder(data: CanonicalData, config: InterviewData, shares: Map<string, number>): (open: string[], current: Inputs) => string {
  const bank = bankOrder(config);
  const state = statesOf(data, config);
  return (open, current) => {
    if (open.length === 1) return open[0]!;
    const probes: { q: string; st: State; left: string[]; weight: number; bound: number }[] = [];
    for (const q of open) {
      const probe = probeAnswer(data, q);
      if (probe === undefined) continue;
      const st = state({ ...current, [q]: probe });
      const left = open.filter((k) => k !== q && !st.read.has(k));
      const weight = 1 - (shares.get(questionTemplate(q)) ?? DEFAULT_SHARE);
      probes.push({ q, st, left, weight, bound: weight * left.length });
    }
    probes.sort((a, b) => b.bound - a.bound);
    let bestScore = 0;
    const scores = new Map<string, number>();
    for (const { q, st, left, weight, bound } of probes) {
      if (bound === 0 || bound < bestScore) break;
      const after = aheadOf(st);
      const score = weight * left.filter((k) => !after.has(k)).length;
      scores.set(q, score);
      if (score > bestScore) bestScore = score;
    }
    const best = bestScore > 0 ? open.filter((q) => scores.get(q) === bestScore) : [];
    return bank(best.length ? best : open);
  };
}

/** The answered inputs the complete return reads (its initial keys, and the answers a roster choice recorded, which are
 * not questions, excepted): the least any order asks. Every walk of a
 * complete return ends with these answered; an evaluation that lacks one of them meets it unknown before any input
 * outside the set, so it is reachable at every state that lacks it. (readInputs also names a roster a collection sum
 * confirms without an answer; such a roster is never asked, so it is not counted.) */
function floorOf(data: CanonicalData, config: InterviewData, answered: Inputs, recorded: Record<string, unknown>): Set<string> {
  return new Set([...readInputs(data, config, answered)].filter((k) => k in answered && !(k in config.initial) && !(k in recorded)));
}

export interface Measure {
  group: string; profile: string; id: string; status: string;
  asked: number; closed: number;
  floor: number | null; oracle: number | null; expected: number | null;
  /** Templates asked, read by the complete return and answered closed: what no order avoids. */
  unavoidableClosed: string[];
  /** Templates asked in static order and unread by the complete return: what some order avoids. */
  avoidable: string[];
}

export type Ctx = { data: CanonicalData; configs: Record<string, InterviewData>; shares: Map<string, number> };

/** One return measured; null when the static walk asks a question the return does not answer (not walkable). */
export function measure(ctx: Ctx, group: string, profile: string, id: string, answers: Answers, errors: string[]): Measure | null {
  const { data, configs, shares } = ctx;
  const config = configs[profile]!;
  let w: Walk;
  const status = statusOf(data, config);
  try { w = walk(data, config, answers, bankOrder(config), BOUND, () => {}, undefined, status); } catch (e) { if (e instanceof Unanswered) return null; throw e; }
  const state = replayedState(config, w.events);
  const given = state.inputs;
  const closed = w.events.filter((e) => isClosed(e.value)).length;
  const m: Measure = { group, profile, id, status: w.status, asked: w.events.length, closed, floor: null, oracle: null, expected: null, unavoidableClosed: [], avoidable: [] };
  if (w.status !== "complete") return m;
  const floor = floorOf(data, config, given, state.recorded);
  m.floor = floor.size;
  const closedKeys = new Set(w.events.filter((e) => isClosed(e.value)).map((e) => e.input));
  m.unavoidableClosed = [...new Set([...floor].filter((k) => closedKeys.has(k)).map(questionTemplate))].sort();
  m.avoidable = [...new Set(w.events.map((e) => e.input).filter((k) => !floor.has(k)).map(questionTemplate))].sort();
  // The other orders answer from the static walk's answers first, then from the return's own.
  const known: Answers = (k, cur) => (k in given ? { value: given[k] } : answers(k, cur));
  const bank = bankOrder(config);
  const others: [string, (open: string[], current: Inputs) => string][] = [
    ["oracle", (open) => bank(open.filter((k) => floor.has(k)).length ? open.filter((k) => floor.has(k)) : open)],
    ["expected", expectedOrder(data, config, shares)],
  ];
  for (const [name, pick] of others) {
    let o: Walk;
    try { o = walk(data, config, known, pick, BOUND, () => {}, undefined, status); } catch (e) {
      errors.push(`${group}: ${id}: the ${name} order asks ${e instanceof Unanswered ? `${e.message}, which the return does not answer` : String(e)}`);
      continue;
    }
    if (o.status !== w.status || o.valuesKey !== w.valuesKey) errors.push(`${group}: ${id}: the ${name} order gives a different ${o.status !== w.status ? "status" : "value"}`);
    if (name === "oracle") m.oracle = o.events.length; else m.expected = o.events.length;
  }
  if (m.oracle !== null && m.oracle !== m.floor) errors.push(`${group}: ${id}: the oracle order asks ${m.oracle}, not the floor ${m.floor}`);
  return m;
}

export function context(): Ctx {
  const data = loadCanonical();
  const configs = Object.fromEntries(["full"].map((p) => [p, loadInterview(p)]));
  return { data, configs, shares: sharesFrom(readFileSync(FREQUENCIES, "utf8")) };
}

interface Run { measures: Measure[]; unwalkable: Record<string, number>; errors: string[] }

/** One return to walk: its group, profile and answers. */
export interface Case { group: string; profile: string; id: string; answers: Answers; open?: { input: string; value: unknown } | null }

/** The returns measured, in report order. */
export function casesOf(ctx: Ctx): Case[] {
  const { data, configs } = ctx;
  const out: Case[] = [];
  const fromInputs = (inputs: Inputs): Answers => (k) => (k in inputs ? { value: inputs[k] } : undefined);
  for (const c of fixtureCases("full", data)) out.push({ group: "Stage 5 whole returns", profile: "full", id: c.id, answers: fromInputs(c.inputs) });
  sampleReturns(data, GENERATED, SEED).forEach((inputs, i) => out.push({ group: "generated returns", profile: "full", id: `generated.${i}`, answers: fromInputs(inputs) }));
  out.push({ group: "minimal returns", profile: "full", id: "every gate closed", answers: minimalAnswers(data, configs["full"]!, "full", null), open: null });
  for (const g of [...existenceGates(data).keys()].sort()) {
    const meta = inputMeta(data, g);
    const values = meta.type === "Bool" ? [true] : meta.type === "Enum" ? meta.values!.slice(1) : [];
    for (const value of values) out.push({ group: "minimal returns", profile: "full", id: `${g} = ${JSON.stringify(value)} alone`, answers: minimalAnswers(data, configs["full"]!, "full", { input: g, value }), open: { input: g, value } });
  }
  return out;
}

/** One return measured, with the problems its walks found, in the order measure() finds them. */
export interface Measured { m: Measure | null; errors: string[] }

export function measureCase(ctx: Ctx, c: Case): Measured {
  const errors: string[] = [];
  return { m: measure(ctx, c.group, c.profile, c.id, c.answers, errors), errors };
}

/** What identifies the list of returns: a worker that built another list is refused. */
export function casesDigest(cases: Case[]): string {
  return createHash("sha256").update(JSON.stringify(cases.map((c) => [c.group, c.profile, c.id, c.open ?? null]))).digest("hex");
}

/** Measures every return (or those at the indices `only`, for the self-test), on `workers` worker threads
 * (interview-length-worker.ts), each of which builds the same list of returns and measures those it is sent by
 * index; one measures them here. The results are taken in the list's order whichever thread measured them, so the
 * run is the same for every worker count. */
export async function runAll(ctx: Ctx, workers: number, only?: number[]): Promise<Run> {
  const all = casesOf(ctx);
  const indices = only ?? all.map((_, i) => i);
  const cases = indices.map((i) => all[i]!);
  let results: Measured[];
  if (workers <= 1) results = cases.map((c) => measureCase(ctx, c));
  else {
    const pool = new TaskWorkers<number, Measured>(new URL("./interview-length-worker.js", import.meta.url), Math.min(workers, cases.length), { year: YEAR });
    try {
      const digest = casesDigest(all);
      if ((await pool.ready).some((d) => d !== digest)) throw new Error("interview-length: a worker built a different list of returns");
      results = await pool.map(indices, (i) => i);
    } finally { await pool.close(); }
  }
  const errors: string[] = [];
  const measures: Measure[] = [];
  const unwalkable: Record<string, number> = {};
  results.forEach(({ m, errors: e }, i) => {
    errors.push(...e);
    if (m) measures.push(m); else unwalkable[cases[i]!.group] = (unwalkable[cases[i]!.group] ?? 0) + 1;
  });
  return { measures, unwalkable, errors };
}

const mean = (xs: number[]) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : 0);
const f1 = (x: number) => x.toFixed(1);
const pct = (part: number, whole: number) => (whole ? `${((100 * part) / whole).toFixed(0)}%` : "-");

function summaryRow(name: string, ms: Measure[], unwalkable: number): string {
  const done = ms.filter((m) => m.status === "complete");
  const asked = done.map((m) => m.asked), sum = (k: "asked" | "closed" | "floor" | "expected") => done.reduce((a, m) => a + (m[k] ?? 0), 0);
  return `| ${name} | ${done.length} | ${ms.length - done.length} | ${unwalkable} | ${f1(mean(asked))} | ${asked.length ? Math.max(...asked) : "-"} | ${f1(mean(done.map((m) => m.closed)))} (${pct(sum("closed"), sum("asked"))}) | ${f1(mean(done.map((m) => m.floor!)))} | ${f1(mean(done.map((m) => m.expected ?? m.asked)))} | ${pct(sum("asked") - sum("floor"), sum("asked"))} | ${pct(sum("asked") - sum("expected"), sum("asked"))} |`;
}

export function renderReport(run: Run, gates: Set<string>, gated: Set<string>, shares: Map<string, number>, cut: number, kept: string): string {
  const groups = [...new Set(run.measures.map((m) => m.group))];
  const out: string[] = [
    "# Interview length: what question order could save",
    "",
    "Written by `node engine/dist/main.js interview-length --write` (engine/src/interview-length.ts; deterministic, no model calls).",
    "Every return is walked in three orders, and each order must give the same status and values (it does; a difference fails the run):",
    "",
    "- **static**: today's order (bank order, then key).",
    "- **floor**: the least any order can ask, knowing the answers: the inputs the complete return's evaluation reads. An order that",
    "  asks only those (the oracle walk) is run and asks exactly that many on every return, so the floor is attained, not just bounded.",
    "- **expected**: an order that does not know the answers: at each step it asks the open question whose closed answer (false, 0,",
    `  none) would make the most other open questions unreachable, weighted by the share answering no from \`interview/${YEAR}/gate_frequencies.yaml\``,
    `  (${DEFAULT_SHARE} where the file names no share), ties in bank order. It probes the evaluator; it never answers for the filer.`,
    "",
    "Only the evaluator's reachability hides a question, so these are the only savings open to order. A question asked in every order and",
    "answered no or 0 is one only a missing gate (a formal-model change) could hide. **Closed** answers are false, 0 or an empty list.",
    "The returns are synthetic (fixtures, generated returns, minimal returns), not real filers.",
    "",
    "## Summary",
    "",
    "Means are per complete return; refused returns are counted but not measured beyond static. *Saved* is the share of all static",
    "questions in the group that the order does not ask.",
    "",
    "| Returns | Complete | Refused | Not walkable | Static asked (mean) | Static max | Closed answers (mean, share) | Floor (mean) | Expected order (mean) | Saved at floor | Saved by expected |",
    "|---|---|---|---|---|---|---|---|---|---|---|",
    ...groups.map((g) => summaryRow(g, run.measures.filter((m) => m.group === g), run.unwalkable[g] ?? 0)),
    summaryRow("**full profile, Stage 5 and generated**", run.measures.filter((m) => m.profile === "full" && m.group !== "minimal returns"), (run.unwalkable["generated returns"] ?? 0)),
    summaryRow("**all**", run.measures, Object.values(run.unwalkable).reduce((a, b) => a + b, 0)),
    "",
  ];
  // Unavoidable closed answers: templates read and answered closed, counted over the full-profile returns.
  const count = (pred: (m: Measure) => boolean, key: "unavoidableClosed" | "avoidable") => {
    const c = new Map<string, number>();
    for (const m of run.measures) if (pred(m)) for (const t of m[key]) c.set(t, (c.get(t) ?? 0) + 1);
    return c;
  };
  const real = (m: Measure) => m.profile === "full" && m.group !== "minimal returns" && m.status === "complete";
  const minimal = (m: Measure) => m.group === "minimal returns" && m.status === "complete";
  const realN = run.measures.filter(real).length, minN = run.measures.filter(minimal).length;
  const ua = count(real, "unavoidableClosed"), um = count(minimal, "unavoidableClosed");
  const rows = [...new Set([...ua.keys(), ...um.keys()])].sort((a, b) => (ua.get(b) ?? 0) - (ua.get(a) ?? 0) || (um.get(b) ?? 0) - (um.get(a) ?? 0) || a.localeCompare(b));
  const kind = (t: string) => (gates.has(t) ? "gate guard" : gated.has(t) ? "behind a gate" : "ungated");
  const listed = rows.filter((t) => (ua.get(t) ?? 0) * 2 >= realN);
  const always = listed.filter((t) => ua.get(t) === realN);
  const rare = always.filter((t) => (shares.get(t) ?? 1) < cut);
  out.push(
    "## Closed answers no order avoids (missing-gate candidates)",
    "",
    `Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the ${realN} complete`,
    `Stage 5 and generated returns ask them closed (count of ${minN} complete minimal returns beside). *Kind*: \`gate guard\` is read by a gate's guard`,
    "(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a",
    "new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all",
    `returns in \`gate_frequencies.yaml\` where the file names the template (- where it does not).`,
    "",
    `${always.length} templates are asked and answered closed on every one of the ${realN} returns; ${rare.length} of them have a recorded share`,
    `yes below the rare-situation cut (${cut}).`,
    "",
    "| Template | Kind | Share yes | Stage 5 and generated | Minimal |",
    "|---|---|---|---|---|",
    ...listed.map((t) => `| \`${t}\` | ${kind(t)} | ${shares.has(t) ? shares.get(t) : "-"} | ${ua.get(t) ?? 0} | ${um.get(t) ?? 0} |`),
    "",
  );
  const av = count((m) => m.status === "complete", "avoidable");
  out.push(
    "## Questions order could avoid",
    "",
    "Templates asked in static order and not read by the complete return, by number of complete returns (all groups): the questions a",
    "better order (or a nested `choose`) would not ask. On the full profile these are the templates interview-rules holds under",
    "`walked_unused`.",
    "",
    "| Template | Returns |",
    "|---|---|",
    ...[...av].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).map(([t, n]) => `| \`${t}\` | ${n} |`),
    "",
    "## Per return",
    "",
  );
  for (const g of groups) {
    out.push(`### ${g}`, "", "| Return | Status | Static | Closed | Floor | Expected |", "|---|---|---|---|---|---|");
    for (const m of run.measures.filter((x) => x.group === g)) out.push(`| ${m.id} | ${m.status} | ${m.asked} | ${m.closed} | ${m.floor ?? "-"} | ${m.expected ?? "-"} |`);
    out.push("");
  }
  out.push(MARKER, kept);
  return out.join("\n").replace(/\n+$/, "\n");
}

export async function interviewLength(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  if (args.includes("--what-if")) return whatIf(args.includes("--write"));
  const ctx = context();
  const t0 = performance.now();
  const workers = walkWorkers("INTERVIEW_WORKERS");
  const run = await runAll(ctx, workers);
  const done = run.measures.filter((m) => m.status === "complete");
  console.log(`  ${run.measures.length} returns measured (${done.length} complete), ${Object.values(run.unwalkable).reduce((a, b) => a + b, 0)} not walkable, ${((performance.now() - t0) / 1000).toFixed(1)} s on ${workers} worker(s)`);
  if (args.includes("--write")) {
    const old = existsSync(REPORT) ? readFileSync(REPORT, "utf8") : "";
    const kept = keptAfterMarker(old);
    const gates = new Set(existenceGates(ctx.data).keys());
    const gated = new Set(gatesOf(ctx.data).map((g) => g.input));
    const cut = (parse(readFileSync(FREQUENCIES, "utf8")) as { cut: { share: number } }).cut.share;
    writeFileSync(REPORT, renderReport(run, gates, gated, ctx.shares, cut, kept));
    console.log(`  wrote ${REPORT}`);
  }
  for (const e of run.errors) console.error(`  ${e}`);
  console.log(`interview-length: ${run.errors.length} problem(s)`);
  return run.errors.length ? 1 : 0;
}

/** The orders on a fixture, and on the same fixture with a planted question asked before the answer that makes it
 * moot: static asks it, the floor does not, and the expected order (whose probe sees the removal) does not either. */
async function selfTest(): Promise<number> {
  assert.ok(isClosed(false) && isClosed(0) && isClosed([]) && !isClosed(true) && !isClosed(1) && !isClosed(["a"]) && !isClosed("single"));
  const planted = sharesFrom("situations:\n  a: {refs: [x.y, ladder 3, \"$w2\"], share: 0.2}\n  b: {refs: [x.y], share: 0.4}\n  c: {refs: [z.w]}\n");
  assert.deepEqual([...planted].sort(), [["$w2", 0.2], ["x.y", 0.4]]);
  const ctx = context();
  for (const [t, s] of ctx.shares) assert.ok(s >= 0 && s <= 1, `share of ${t}`);
  assert.ok(ctx.shares.size > 0, "the frequency file names input templates");
  const { data, configs } = ctx;
  const config = configs["full"]!;
  const c = fixtureCases("full", data).find((x) => x.id === "stage5.return.owed")!;
  const fromInputs: Answers = (k) => (k in c.inputs ? { value: c.inputs[k] } : undefined);
  const errors: string[] = [];
  const clean = measure(ctx, "self-test", "full", c.id, fromInputs, errors)!;
  assert.deepEqual(errors, []);
  assert.ok(clean.status === "complete" && clean.floor! <= clean.expected! && clean.expected! <= clean.asked && clean.oracle === clean.floor, JSON.stringify(clean));
  // Plant all(decider, leaked) and ask the leaked question first: the decider (false) makes it moot.
  const w = walk(data, config, fromInputs, bankOrder(config), BOUND, () => {});
  const pair = leakPair(data, config, c.inputs, w);
  const leaky = plantLeak(data, config.targets[0]!, pair.decider, pair.leaked);
  const reordered = structuredClone(config);
  const decider = reordered.questions.find((q) => q.input === questionTemplate(pair.decider))!;
  reordered.questions.find((q) => q.input === questionTemplate(pair.leaked))!.order = decider.order - 0.5;
  const m = measure({ ...ctx, data: leaky, configs: { ...configs, full: reordered } }, "self-test", "full", c.id, fromInputs, errors)!;
  assert.deepEqual(errors, []);
  assert.equal(m.asked, clean.asked + 1, "static asks the planted question");
  assert.equal(m.floor, clean.floor, "the floor does not");
  assert.ok(m.avoidable.includes(questionTemplate(pair.leaked)), "it is listed as avoidable");
  assert.ok(m.expected! <= clean.expected!, `the expected order avoids it (${m.expected} > ${clean.expected})`);
  // What-if: the line 8 umbrella answered no asks one question in place of the line 8 questions, with the same values;
  // answered no while a line 8 amount is non-zero, it changes the values (the run's check would fail).
  const u = UMBRELLAS.find((x) => x.id === "s1.line8_any")!;
  const applied = applyUmbrellas(data, configs, [u]);
  const covered = w.events.filter((e) => u.covers.includes(questionTemplate(e.input)));
  assert.ok(covered.length > 1 && covered.every((e) => isClosed(e.value)), "the fixture answers the line 8 questions no");
  const no: Answers = (k, cur) => (k === u.id ? { value: false } : fromInputs(k, cur));
  const wi = walk(applied.data, applied.configs["full"]!, no, bankOrder(applied.configs["full"]!), BOUND, () => {});
  assert.ok(wi.status === w.status && wi.valuesKey === w.valuesKey, "the umbrella keeps the values");
  assert.equal(wi.events.length, w.events.length - covered.length + 1, "the umbrella replaces the questions it covers");
  const prize: Inputs = { ...c.inputs, "s1.winnings_any": true, "s1.prizes": 100000 };
  const withPrize: Answers = (k) => (k in prize ? { value: prize[k] } : undefined);
  const wp = walk(data, config, withPrize, bankOrder(config), BOUND, () => {});
  const wrong = walk(applied.data, applied.configs["full"]!, (k, cur) => (k === u.id ? { value: false } : withPrize(k, cur)), bankOrder(applied.configs["full"]!), BOUND, () => {});
  assert.ok(umbrellaAnswer(u, wp.events, isClosed) && wrong.valuesKey !== wp.valuesKey, "a wrong no changes the values");
  // Workers: the first SAMPLED generated returns (complete and refused ones), measured in this thread and on two
  // workers, give the same run and report.
  const SAMPLED = 5;
  const cases = casesOf(ctx);
  const picks = cases.flatMap((x, i) => (x.group === "generated returns" ? [i] : [])).slice(0, SAMPLED);
  const one = await runAll(ctx, 1, picks), two = await runAll(ctx, 2, picks);
  assert.ok(one.measures.length + Object.values(one.unwalkable).reduce((a, b) => a + b, 0) === picks.length && picks.length > 1);
  assert.ok(one.measures.some((m) => m.status === "complete") && one.measures.some((m) => m.status !== "complete"), "the sample has complete and refused returns");
  assert.deepEqual(two, one, "two workers measure the returns as one thread does");
  const report = (r: Run) => renderReport(r, new Set(existenceGates(data).keys()), new Set(gatesOf(data).map((g) => g.input)), ctx.shares, 0.05, "\n");
  assert.equal(report(two), report(one), "and give the same report");
  console.log(`interview-length self-test: passed (closed answers, frequency shares, orders on ${c.id}: static ${clean.asked}, floor ${clean.floor}, expected ${clean.expected}; ${pair.leaked} planted before ${pair.decider}; ${u.id} asks ${wi.events.length} for ${w.events.length}; ${picks.length} generated returns the same on two workers)`);
  return 0;
}

/** One scenario's walk of one return beside the walk as built. */
interface Delta { c: Case; status: string; before: number; after: number; umbrellaAsked: number; umbrellaYes: number }

/** Walks every return in today's order as built and under each scenario of umbrellas (each alone, then the recommended
 * together); each scenario's walk must give the same status and values as the walk as built. */
export function whatIfRun(ctx: Ctx, scenarios: [string, Umbrella[]][]): { results: Map<string, Delta[]>; errors: string[]; unwalkable: number } {
  const errors: string[] = [];
  const base: { c: Case; w: Walk }[] = [];
  let unwalkable = 0;
  for (const c of casesOf(ctx)) {
    const config = ctx.configs[c.profile]!;
    try { base.push({ c, w: walk(ctx.data, config, c.answers, bankOrder(config), BOUND, () => {}) }); } catch (e) { if (e instanceof Unanswered) unwalkable++; else throw e; }
  }
  const results = new Map<string, Delta[]>();
  for (const [name, us] of scenarios) {
    const applied = applyUmbrellas(ctx.data, ctx.configs, us);
    const out: Delta[] = [];
    for (const { c, w } of base) {
      const config = applied.configs[c.profile]!;
      // A minimal return's closed answers are probed on the data they are asked of. An umbrella is answered only on a
      // return whose walk as built asked one of its inputs (a refused return stops asking what it does not answer).
      const own = c.open !== undefined ? minimalAnswers(applied.data, config, "full", c.open) : c.answers;
      const answers: Answers = (k, cur) => {
        const u = us.find((x) => x.id === k);
        if (!u) return own(k, cur);
        return w.events.some((e) => u.covers.includes(questionTemplate(e.input))) ? { value: umbrellaAnswer(u, w.events, isClosed) } : undefined;
      };
      let o: Walk;
      try { o = walk(applied.data, config, answers, bankOrder(config), BOUND, () => {}); } catch (e) {
        errors.push(`${name}: ${c.group}: ${c.id}: ${e instanceof Unanswered ? `asks ${e.message}, which the return does not answer` : String(e)}`);
        continue;
      }
      // A refusal names the line its gate read, which is now the gate line: compare with the gate line's name undone.
      // A refused return is compared on its refusals only: its other targets may stay unknown, and an answered
      // umbrella can settle more of them than the walk as built did.
      const key = (k: string) => (w.status === "refused" ? JSON.stringify((JSON.parse(k) as { kind?: string }[]).filter((v) => v?.kind === "refusal")) : k);
      if (o.status !== w.status || key(unGated(o.valuesKey, us)) !== key(w.valuesKey)) errors.push(`${name}: ${c.group}: ${c.id}: a different ${o.status !== w.status ? `status (${w.status} to ${o.status})` : "value"}`);
      const ids = new Set(us.map((u) => u.id));
      const asked = o.events.filter((e) => ids.has(e.input));
      out.push({ c, status: w.status, before: w.events.length, after: o.events.length, umbrellaAsked: asked.length, umbrellaYes: asked.filter((e) => e.value === true).length });
    }
    results.set(name, out);
  }
  return { results, errors, unwalkable };
}

function whatIfReport(results: Map<string, Delta[]>, unwalkable: number, kept: string): string {
  const typical = (d: Delta) => d.c.profile === "full" && d.c.group !== "minimal returns" && d.status === "complete";
  const views: [string, (d: Delta) => boolean][] = [
    ["Full profile, complete (Stage 5 and generated)", typical],
    ["Minimal: every gate closed", (d) => d.c.id === "every gate closed"],
    ["All complete returns", (d) => d.status === "complete"],
    ["All returns, refused included", () => true],
  ];
  const out: string[] = [
    "# Umbrella gates: questions saved (what-if)",
    "",
    "Written by `node engine/dist/main.js interview-length --what-if --write` (engine/src/interview-length.ts and",
    "engine/src/umbrella-what-if.ts; deterministic, no model calls). Each proposed umbrella of the",
    "umbrella gates design (2026-11-10) is put into a copy of the built data in memory (a new Bool input; a gate line",
    "`<input>_if_<umbrella>` in place of each gated input in every reader; a roster's readers under the same `choose`), and",
    "every return of `interview_length.md` is walked in today's order as built and with the umbrella. The umbrella is",
    "answered yes exactly when the walk as built answered one of its inputs with something other than false, 0 or none,",
    "which is the truthful answer for these returns; both walks reach the same status and values on every return (checked;",
    "a difference fails the run). The forms in the repository are unchanged.",
    "",
    "*Saved* is questions asked as built minus questions asked with the umbrella (the umbrella question counted), as a mean",
    "per return of the view. The returns are synthetic and answer nearly every rare question no, so the saving here is close",
    "to the most an umbrella can save; the design weighs it by the share answering yes.",
    "",
    `Returns not walkable as built (skipped): ${unwalkable}.`,
    "",
    "| Scenario | Umbrella asked (returns) | Answered yes | " + views.map(([v]) => `${v}: saved (mean)`).join(" | ") + " | Full profile: before → after |",
    "|---|---|---|" + views.map(() => "---|").join("") + "---|",
  ];
  for (const [name, ds] of results) {
    const asked = ds.filter((d) => d.umbrellaAsked > 0).length;
    const yes = ds.filter((d) => d.umbrellaYes > 0).length;
    const cells = views.map(([, f]) => { const xs = ds.filter(f); return xs.length ? f1(mean(xs.map((d) => d.before - d.after))) : "-"; });
    const t = ds.filter(typical);
    out.push(`| ${name} | ${asked} of ${ds.length} | ${yes} | ${cells.join(" | ")} | ${f1(mean(t.map((d) => d.before)))} → ${f1(mean(t.map((d) => d.after)))} |`);
  }
  out.push("", "## Per return, full profile", "", "Questions asked as built, then the saving under each scenario.", "");
  const names = [...results.keys()];
  const first = results.get(names[0]!)!;
  out.push(`| Return | Status | As built | ${names.join(" | ")} |`, `|---|---|---|${names.map(() => "---|").join("")}`);
  first.forEach((d, i) => {
    if (d.c.profile !== "full") return;
    out.push(`| ${d.c.id} | ${d.status} | ${d.before} | ${names.map((n) => { const x = results.get(n)![i]!; return String(x.before - x.after); }).join(" | ")} |`);
  });
  out.push("", MARKER, kept);
  return out.join("\n").replace(/\n+$/, "\n");
}

function whatIf(write: boolean): number {
  const ctx = context();
  const t0 = performance.now();
  const scenarios: [string, Umbrella[]][] = [
    ...UMBRELLAS.map((u): [string, Umbrella[]] => [`\`${u.id}\``, [u]]),
    ["**recommended together**", UMBRELLAS.filter((u) => RECOMMENDED.includes(u.id))],
  ];
  const { results, errors, unwalkable } = whatIfRun(ctx, scenarios);
  console.log(`  ${scenarios.length} scenarios over ${results.get(scenarios[0]![0])!.length} returns, ${((performance.now() - t0) / 1000).toFixed(1)} s`);
  for (const [name, ds] of results) {
    const t = ds.filter((d) => d.c.profile === "full" && d.c.group !== "minimal returns" && d.status === "complete");
    console.log(`  ${name}: full-profile complete mean saved ${f1(mean(t.map((d) => d.before - d.after)))}`);
  }
  if (write) {
    const old = existsSync(WHAT_IF_REPORT) ? readFileSync(WHAT_IF_REPORT, "utf8") : "";
    const kept = keptAfterMarker(old);
    writeFileSync(WHAT_IF_REPORT, whatIfReport(results, unwalkable, kept));
    console.log(`  wrote ${WHAT_IF_REPORT}`);
  }
  for (const e of errors) console.error(`  ${e}`);
  console.log(`interview-length --what-if: ${errors.length} problem(s)`);
  return errors.length ? 1 : 0;
}
