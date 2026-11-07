// The interview rules (the interview never sets an input or hides a reachable one; order never changes a value), checked
// mechanically over every profile, the fixtures' interview paths and generated returns (`interview-rules`, in
// check-all). Each check prints its wall time.
//
//   no-input-set      the interview data sets no input value: every profile's `initial` is empty (the three
//                     single-filer slice profiles' fixed filer, pinned below, excepted); each roster choice's label
//                     maps to exactly one value; no interview target reads a gated input; and replaying a log yields
//                     only answers its events gave, at their last value
//   order             the same answers in a different order give the same status and values: each walk's answers
//                     replayed reversed and in a seeded shuffle, and the same answers given by a seeded random
//                     traversal (each step answers a random reachable question, not the first)
//   completion        the interview never reports complete while the evaluator reports a reachable unknown input:
//                     at every state of every walk, and on seeded random subsets of each walk's answers. The inputs
//                     found so are named by template; those of tools/interview_rules_baseline.json (the leaking
//                     conjunctions the design rewrites as nested choose) are held, and the list may only shrink
//
// Walks: the full profile over the Stage 5 fixtures and generated returns (generate.ts), the New York profile over
// the New York stage fixtures and generated returns with New York answers. A generated return whose walk reaches a
// question it does not answer is counted as not walkable, not failed (the generator does not answer every input). The
// random traversals take every New York fixture of RANDOM_EVERY and every other case.
//
// The walks are independent: each loop's iterations run on worker threads (pool.ts's size), each with its own copy of
// the data and the seed the serial loop would give it, and their results are taken back in the loop's order, so the
// output and verdicts are those of a serial run (bar the printed times).
//
//   interview-rules [--self-test]
import assert from "node:assert/strict";
import { readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { Worker } from "node:worker_threads";
import fc from "fast-check";
import { mapPool, poolSize } from "./pool.js";
import { loadCanonical } from "./canonical.js";
import { interviewStatus, loadInterview, questionTemplate, replay, type InterviewData } from "./interview.js";
import { evaluate } from "./eval.js";
import { gateProblems } from "./gates.js";
import { nyReturnArbitrary, sampleReturns } from "./generate.js";
import { resolveInputs } from "./fixture-inputs.js";
import { YEAR, nyPath, yearPath } from "./year.js";
import type { CanonicalData, Inputs } from "./types.js";

const PROFILES = ["social-security", "sales", "stage4", "full", "ny"] as const;
/** Profiles allowed a non-empty `initial`, with exactly that value: slice profiles of Stages 2 to 4, whose scope is a
 * single filer. The full and New York profiles, the return a filer prepares, have none. */
const SLICE_INITIAL = JSON.stringify({ $person: ["taxpayer"], "person[taxpayer].role": "taxpayer" });
const INITIAL_ALLOWED: Record<string, string> = { "social-security": SLICE_INITIAL, sales: SLICE_INITIAL, stage4: SLICE_INITIAL };
const GENERATED = Number(process.env["INTERVIEW_RULES_RUNS"] ?? 12);
const RANDOM_EVERY = 3;
const SEED = 11;
const BASELINE = resolve(import.meta.dirname, "../..", "tools", "interview_rules_baseline.json");

type Event = { input: string; value: unknown };
interface Walk { events: Event[]; inputs: Inputs; status: string; valuesKey: string; states: number }

/** A seeded generator in [0, 1) (mulberry32). */
function rng(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function shuffled<T>(xs: T[], rand: () => number): T[] {
  const out = [...xs];
  for (let i = out.length - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [out[i], out[j]] = [out[j]!, out[i]!]; }
  return out;
}

class Unanswered extends Error {}

/** Walks the interview answering from `answers`: `pick` chooses the next input among the reachable ones that have an
 * answer. A refusal is provisional (a later answer may clear it), so the walk goes on past it while a reachable
 * question has an answer, and ends complete or when none has. Reports early completion at every state to `leak`. Throws
 * Unanswered when the interview's next question has no answer in `answers` and the return is not refused. */
function walk(data: CanonicalData, config: InterviewData, answers: Inputs, pick: (open: string[]) => string, bound: number, leak: (reachable: string[]) => void): Walk {
  let current: Inputs = structuredClone(config.initial);
  const events: Event[] = [];
  for (let step = 0; ; step++) {
    if (step > bound) throw new Error("the walk did not end");
    const st = interviewStatus(data, config, current);
    if (st.status === "complete" && st.reachableInputs.length) leak(st.reachableInputs);
    const open = st.reachableInputs.filter((k) => k in answers && !(k in current));
    if (st.status === "complete" || (st.status === "refused" && !open.length)) return { events, inputs: current, status: st.status, valuesKey: targetKey(data, config, current), states: step + 1 };
    if (st.status === "incomplete" && st.question && !(st.question.input in answers)) throw new Unanswered(st.question.input);
    if (!open.length) throw new Error("incomplete, and no reachable question has an answer");
    const key = pick(open);
    events.push({ input: key, value: answers[key] });
    current = { ...current, [key]: answers[key] };
  }
}

/** The profile's target values, serialized: what two walks over the same answers must agree on. */
function targetKey(data: CanonicalData, config: InterviewData, inputs: Inputs): string {
  const values = evaluate(data, inputs, config.targets).values;
  return JSON.stringify(config.targets.map((t) => values.get(t)));
}

function replayed(config: InterviewData, events: Event[]) {
  return replay(config, [{ version: 1, tax_year: config.tax_year }, ...events]);
}

/** Replay yields only the answers the events gave: every key is in `initial` or is an event's input at its last value. */
function onlyGiven(config: InterviewData, events: Event[]): string | null {
  const last = new Map(events.map((e) => [e.input, JSON.stringify(e.value)]));
  for (const [k, v] of Object.entries(replayed(config, events))) {
    const given = last.get(k) ?? (k in config.initial ? JSON.stringify(config.initial[k]) : undefined);
    if (given === undefined) return `replay set ${k}, which no event answered`;
    if (given !== JSON.stringify(v)) return `replay gave ${k} a value its last event did not`;
  }
  return null;
}

/** The interview's own order: the open question first in bank order (then by key), as interviewStatus picks. */
function bankOrder(config: InterviewData): (open: string[]) => string {
  const order = new Map(config.questions.map((q) => [q.input, q.order]));
  const rank = (k: string) => order.get(questionTemplate(k)) ?? Infinity;
  return (open) => open.reduce((a, b) => (rank(b) < rank(a) || (rank(b) === rank(a) && b.localeCompare(a) < 0) ? b : a));
}

interface Case { id: string; inputs: Inputs }
function fixtureCases(file: string, data: CanonicalData): Case[] {
  return (JSON.parse(readFileSync(file, "utf8")) as { cases: Case[] }).cases.map((c) => ({ id: c.id, inputs: resolveInputs(c.inputs, data.params, c.id) }));
}

/** The static part of no-input-set: each profile's initial, its roster choices, and the gate conventions with the
 * profiles' targets. */
export function staticProblems(data: CanonicalData, configs: Record<string, InterviewData>): string[] {
  const errors: string[] = [];
  for (const [p, c] of Object.entries(configs)) {
    const initial = JSON.stringify(c.initial);
    if (Object.keys(c.initial).length && initial !== INITIAL_ALLOWED[p]) errors.push(`no-input-set: profile ${p}: initial ${initial} sets input values; the interview sets none`);
    for (const q of c.questions) {
      if (!q.choices) continue;
      const labels = q.choices.map((ch) => ch.label);
      const values = q.choices.map((ch) => JSON.stringify([...ch.value].sort()));
      if (new Set(labels).size !== labels.length) errors.push(`no-input-set: ${p} ${q.input}: two choices share a label`);
      if (new Set(values).size !== values.length) errors.push(`no-input-set: ${p} ${q.input}: two choices give the same value`);
    }
  }
  errors.push(...gateProblems(data, [...new Set(Object.values(configs).flatMap((c) => c.targets))]).map((e) => `no-input-set: ${e}`));
  return errors;
}

/** Early completion against the baseline: `seen` maps each leaked input template to the first case that showed it. */
export function leakProblems(seen: Map<string, string>, baseline: Record<string, string>): string[] {
  const out: string[] = [];
  for (const [t, where] of [...seen].sort()) if (!(t in baseline)) out.push(`completion: ${where}: reported complete while ${t} is reachable and unanswered`);
  for (const t of Object.keys(baseline).sort()) if (!seen.has(t)) out.push(`completion: ${t} no longer leaks; remove it from tools/interview_rules_baseline.json`);
  return out;
}

/** One unit of the walks' work, done by a worker thread (interview-rules-worker.ts) on its own copy of the data. Each
 * kind is the body of one serial loop over cases or walks, for one case or walk; its seed comes from the main thread,
 * so the work is the same whichever thread does it. Leaks come back as lists of reachable inputs, in the order the
 * serial loop met them, and the main thread applies them in case order, so the first case named for each template is
 * the serial run's. */
export type Task =
  | { kind: "walk"; profile: "full" | "ny"; c: Case }
  | { kind: "order"; profile: "full" | "ny"; group: string; c: Case; w: Walk }
  | { kind: "random"; profile: "full" | "ny"; group: string; c: Case; w: Walk; seed: number }
  | { kind: "subsets"; profile: "full" | "ny"; w: Walk; seed: number };
export type TaskResult =
  | { kind: "walked"; w: Walk; leaks: string[][]; bad: string | null }
  | { kind: "unanswered"; input: string; leaks: string[][] }
  | { kind: "failed"; error: string; leaks: string[][] }
  | { kind: "errors"; errors: string[]; leaks: string[][] };

export interface Context { data: CanonicalData; configs: Record<(typeof PROFILES)[number], InterviewData> }

export function loadContext(): Context {
  return { data: loadCanonical(), configs: Object.fromEntries(PROFILES.map((p) => [p, loadInterview(p)])) as Context["configs"] };
}

export function runTask({ data, configs }: Context, task: Task): TaskResult {
  const leaks: string[][] = [];
  const config = configs[task.profile];
  if (task.kind === "walk") {
    try {
      const w = walk(data, config, task.c.inputs, bankOrder(config), 800, (r) => leaks.push(r));
      return { kind: "walked", w, leaks, bad: onlyGiven(config, w.events) };
    } catch (e) {
      return e instanceof Unanswered ? { kind: "unanswered", input: e.message, leaks } : { kind: "failed", error: String(e), leaks };
    }
  }
  const errors: string[] = [];
  const { w } = task;
  if (task.kind === "order") {
    const { group, c } = task;
    const rand = rng(SEED + w.events.length);
    for (const [how, events] of [["reversed", w.events.toReversed()], ["shuffled", shuffled(w.events, rand)]] as const) {
      const inputs = replayed(config, events);
      const st = interviewStatus(data, config, inputs);
      if (st.status !== w.status || targetKey(data, config, inputs) !== w.valuesKey) errors.push(`order: ${group}: ${c.id}: the answers ${how} give a different ${st.status !== w.status ? `status (${st.status}, not ${w.status})` : "value"}`);
      const bad = onlyGiven(config, events);
      if (bad) errors.push(`no-input-set: ${group}: ${c.id} (${how}): ${bad}`);
    }
  } else if (task.kind === "random") {
    const { group, c } = task;
    const rand = rng(task.seed);
    try {
      const r = walk(data, config, c.inputs, (open) => open[Math.floor(rand() * open.length)]!, 800, (x) => leaks.push(x));
      if (r.status !== w.status || r.valuesKey !== w.valuesKey) errors.push(`order: ${group}: ${c.id}: a random answering order gives a different ${r.status !== w.status ? `status (${r.status}, not ${w.status})` : "value"}`);
    } catch (e) {
      errors.push(`order: ${group}: ${c.id}: random answering order: ${e instanceof Unanswered ? `asks ${e.message}, which the answers in bank order never reach` : String(e)}`);
    }
  } else {
    const rand = rng(task.seed);
    for (let k = 0; k < 3; k++) {
      const kept = w.events.filter(() => rand() < 0.5);
      const st = interviewStatus(data, config, replayed(config, kept));
      if (st.status === "complete" && st.reachableInputs.length) leaks.push(st.reachableInputs);
    }
  }
  return { kind: "errors", errors, leaks };
}

/** Threads that each load the data once and do tasks one at a time (interview-rules-worker.ts). */
class Workers {
  private idle: Worker[] = [];
  private all: Worker[] = [];
  constructor(count: number) {
    for (let i = 0; i < count; i++) {
      const w = new Worker(new URL("./interview-rules-worker.js", import.meta.url), { workerData: { year: YEAR } });
      this.all.push(w);
      this.idle.push(w);
    }
  }
  run(task: Task): Promise<TaskResult> {
    const w = this.idle.pop();
    if (!w) throw new Error("interview-rules: no idle worker (the pool's limit is the worker count)");
    return new Promise((done, fail) => {
      const onError = (e: Error) => { w.off("message", onMessage); fail(e); };
      const onMessage = (m: { ok: true; result: TaskResult } | { ok: false; error: string }) => {
        w.off("error", onError);
        this.idle.push(w);
        if (m.ok) done(m.result); else fail(new Error(m.error));
      };
      w.once("message", onMessage);
      w.once("error", onError);
      w.postMessage(task);
    });
  }
  /** Asks each worker to end and waits for it: a worker that ends of itself runs its exit handlers, as a terminated
   * one does not. */
  async close(): Promise<void> {
    await Promise.all(this.all.map((w) => new Promise<void>((done) => { w.once("exit", () => done()); w.postMessage(null); })));
  }
}

export async function interviewRules(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  const { data, configs } = loadContext();
  const errors: string[] = [];
  const times: string[] = [];
  const timed = async <T>(name: string, f: () => T | Promise<T>): Promise<T> => {
    const t0 = performance.now();
    const r = await f();
    times.push(`${name} ${((performance.now() - t0) / 1000).toFixed(1)} s`);
    return r;
  };

  await timed("no-input-set (profiles, choices, gated targets)", () => errors.push(...staticProblems(data, configs)));
  const seen = new Map<string, string>();
  const leakIn = (where: string) => (reachable: string[]) => { for (const k of reachable) if (!seen.has(questionTemplate(k))) seen.set(questionTemplate(k), where); };

  // The walks: (profile, case) pairs from the fixtures and generated returns.
  const nyFiles = readdirSync(nyPath("fixtures")).filter((n) => n.endsWith(".json") && !n.startsWith("classm") && n !== "mutation.json").sort();
  const groups: { name: string; profile: "full" | "ny"; cases: Case[]; generated: boolean }[] = await timed("generate returns", () => [
    { name: "full: Stage 5 fixtures", profile: "full", cases: fixtureCases(yearPath("fixtures", "stage5.json"), data), generated: false },
    { name: "ny: New York fixtures", profile: "ny", cases: nyFiles.flatMap((f) => fixtureCases(join(nyPath("fixtures"), f), data)), generated: false },
    { name: "full: generated returns", profile: "full", cases: sampleReturns(data, GENERATED, SEED).map((inputs, i) => ({ id: `generated.${i}`, inputs })), generated: true },
    { name: "ny: generated returns", profile: "ny", cases: fc.sample(nyReturnArbitrary(data), { seed: SEED, numRuns: GENERATED }).map((inputs, i) => ({ id: `ny.generated.${i}`, inputs })), generated: true },
  ]);

  // Each loop below sends its iterations to the workers and takes the results back in the loop's order.
  const limit = poolSize();
  const workers = new Workers(limit);
  try {
    const walks: { group: string; profile: "full" | "ny"; c: Case; w: Walk }[] = [];
    const counts: string[] = [];
    await timed("completion and no-input-set: walks in bank order", async () => {
      const flat = groups.flatMap((g) => g.cases.map((c) => ({ g, c })));
      const results = await mapPool(flat, ({ g, c }) => workers.run({ kind: "walk", profile: g.profile, c }), limit);
      for (const g of groups) {
        let walked = 0, unwalkable = 0, states = 0;
        for (const [i, { c }] of flat.entries()) {
          if (flat[i]!.g !== g) continue;
          const r = results[i]!;
          for (const reachable of r.leaks) leakIn(`${g.name}: ${c.id}`)(reachable);
          if (r.kind === "walked") {
            walks.push({ group: g.name, profile: g.profile, c, w: r.w });
            walked++; states += r.w.states;
            if (r.bad) errors.push(`no-input-set: ${g.name}: ${c.id}: ${r.bad}`);
          } else if (r.kind === "unanswered" && g.generated) {
            unwalkable++;
          } else {
            errors.push(`walk: ${g.name}: ${c.id}: ${r.kind === "unanswered" ? `no answer for asked question ${r.input}` : r.kind === "failed" ? r.error : ""}`);
          }
        }
        counts.push(`${g.name}: ${walked} walked (${states} states)${g.generated ? `, ${unwalkable} not walkable` : ""}`);
      }
    });

    await timed("order: reversed and shuffled replays", async () => {
      const results = await mapPool(walks, ({ group, profile, c, w }) => workers.run({ kind: "order", profile, group, c, w }), limit);
      for (const r of results) if (r.kind === "errors") errors.push(...r.errors);
    });

    let traversals = 0;
    await timed("order: random traversals", async () => {
      let i = 0, ny = 0;
      const chosen: { group: string; profile: "full" | "ny"; c: Case; w: Walk; seed: number }[] = [];
      for (const x of walks) {
        const seed = SEED * 1000 + i++;
        if (x.group === "ny: New York fixtures" && ny++ % RANDOM_EVERY) continue;
        chosen.push({ ...x, seed });
      }
      traversals = chosen.length;
      const results = await mapPool(chosen, ({ group, profile, c, w, seed }) => workers.run({ kind: "random", profile, group, c, w, seed }), limit);
      for (const [k, r] of results.entries()) {
        const { group, c } = chosen[k]!;
        for (const reachable of r.leaks) leakIn(`${group}: ${c.id} (random order)`)(reachable);
        if (r.kind === "errors") errors.push(...r.errors);
      }
    });

    await timed("completion: random subsets of the answers", async () => {
      const results = await mapPool(walks, ({ profile, w }, i) => workers.run({ kind: "subsets", profile, w, seed: SEED * 7919 + i }), limit);
      for (const [k, r] of results.entries()) {
        const { group, c } = walks[k]!;
        for (const reachable of r.leaks) leakIn(`${group}: ${c.id} (a subset of its answers)`)(reachable);
      }
    });
    return report(walks.length, traversals, counts);
  } finally {
    await workers.close();
  }

  function report(walkCount: number, traversals: number, counts: string[]): number {
    const baseline = (JSON.parse(readFileSync(BASELINE, "utf8")) as { early_completion: Record<string, string> }).early_completion;
    errors.push(...leakProblems(seen, baseline));
    for (const line of counts) console.log(`  ${line}`);
    console.log(`  early completion: ${seen.size} input template(s) left reachable at completion, ${Object.keys(baseline).length} held by the baseline`);
    for (const t of times) console.log(`  time: ${t}`);
    for (const e of errors.slice(0, 60)) console.error(`  ${e}`);
    if (errors.length > 60) console.error(`  ... and ${errors.length - 60} more`);
    console.log(`interview-rules: ${errors.length} problem(s); ${walkCount} walks, each replayed reversed and shuffled; ${traversals} answered in a random order`);
    return errors.length ? 1 : 0;
  }
}

/** Each rule flags a planted violation and passes the clean case. */
function selfTest(): number {
  const data = loadCanonical();
  const configs = Object.fromEntries(PROFILES.map((p) => [p, loadInterview(p)])) as Record<string, InterviewData>;
  assert.deepEqual(staticProblems(data, configs), []);
  const planted = (edit: (c: Record<string, InterviewData>) => void) => { const c = structuredClone(configs); edit(c); return staticProblems(data, c).join("\n"); };
  assert.match(planted((c) => { c["full"]!.initial = { "s1.line7": 0 }; }), /profile full: initial .* sets input values/);
  assert.match(planted((c) => { c["sales"]!.initial = { ...c["sales"]!.initial, "s1.line7": 0 }; }), /profile sales: initial/);
  const choices = (c: Record<string, InterviewData>) => c["full"]!.questions.find((q) => q.choices)!.choices!;
  assert.match(planted((c) => { const ch = choices(c); ch[1]!.label = ch[0]!.label; }), /two choices share a label/);
  assert.match(planted((c) => { const ch = choices(c); ch[1]!.value = [...ch[0]!.value]; ch[1]!.labels = { ...ch[0]!.labels }; }), /two choices give the same value/);
  const config = configs["full"]!;
  assert.equal(onlyGiven(config, [{ input: "a.x", value: 1 }, { input: "a.x", value: 2 }]), null);
  assert.deepEqual(replayed(config, [{ input: "a.x", value: 1 }, { input: "a.x", value: 2 }]), { "a.x": 2 });
  assert.deepEqual(leakProblems(new Map([["p.a", "case 1"]]), { "p.a": "held" }), []);
  assert.match(leakProblems(new Map([["p.a", "case 1"], ["p.b", "case 2"]]), { "p.a": "held" }).join("\n"), /case 2: reported complete while p\.b is reachable/);
  assert.match(leakProblems(new Map(), { "p.a": "held" }).join("\n"), /p\.a no longer leaks/);
  console.log("interview-rules self-test: 10 cases passed (profile initial, roster choices, replay, early-completion baseline)");
  return 0;
}
