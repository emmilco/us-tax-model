// The interview rules (the interview never sets an input or hides a reachable one; order never changes a value), checked
// mechanically over every profile, the fixtures' interview paths and generated returns (`interview-rules`, in
// check-all). Each check prints its wall time.
//
//   no-input-set      the interview data sets no input value: every profile's `initial` is empty (the three
//                     single-filer slice profiles' fixed filer, pinned below, excepted); each roster choice's label
//                     maps to exactly one value, and each enum value label to exactly one value of its enum; no
//                     interview target reads a gated input; and replaying a log yields
//                     only answers its events gave, at their last value
//   order             the same answers in a different order give the same status and values: each walk's answers
//                     replayed reversed and in a seeded shuffle, and the same answers given by a seeded random
//                     traversal (each step answers a random reachable question, not the first)
//   completion        the interview never reports complete while the evaluator reports a reachable unknown input:
//                     at every state of every walk, and on seeded random subsets of each walk's answers. The inputs
//                     found so are named by template; those of tools/interview_rules_baseline.json (the leaking
//                     conjunctions the design rewrites as nested choose) are held, and the list may only shrink
//   reach             on a complete return, every fixture answer is classed by whether the bank-order walk asked it
//                     and whether the complete return's evaluation reads it. Asked and unread: a question a later
//                     answer made moot (a pruning opportunity, listed under walked_unused). Neither: leftover answers,
//                     withheld from the random traversals, which answer only what the bank-order walk asked. An input
//                     reachable at an incomplete state that the walk never asked, in bank order or in a random
//                     traversal, is reached only out of bank order: an order-dependent leak, listed under
//                     order_dependent_reach. Both lists are held in the baseline by template: a template not in its
//                     list fails, and one no longer seen fails until it is removed
//   minimal returns   per profile, a return answering every question with its closed answer (zero, false, an empty
//                     roster, the first enum value; the other value where that one refuses), then the same with each
//                     existence gate (an input a gate line's guard reads) opened alone. Each must complete without
//                     asking an input gated by a closed gate
//
// Walks: the full profile over the Stage 5 fixtures and generated returns (generate.ts), the New York profile over
// the New York stage fixtures and generated returns with New York answers. A generated return whose walk reaches a
// question it does not answer is counted as not walkable, not failed (the generator does not answer every input). The
// random traversals take every New York fixture of RANDOM_EVERY and every other case. On a refused return the
// questions left open at the refusal are not leaks, so its random traversal checks only order.
//
// The walks are independent: each loop's iterations run on worker threads (pool.ts's size), each with its own copy of
// the data and the seed the serial loop would give it, and their results are taken back in the loop's order, so the
// output and verdicts are those of a serial run (bar the printed times).
//
//   interview-rules [--self-test]
import assert from "node:assert/strict";
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { Worker } from "node:worker_threads";
import fc from "fast-check";
import { mapPool, poolSize } from "./pool.js";
import { loadCanonical } from "./canonical.js";
import { entryHint, inputMeta, interviewStatus, loadInterview, questionTemplate, replay, type InterviewData } from "./interview.js";
import { evaluate } from "./eval.js";
import { gateProblems, gatesOf, readsOf } from "./gates.js";
import { nyReturnArbitrary, sampleReturns } from "./generate.js";
import { resolveInputs } from "./fixture-inputs.js";
import { YEAR, nyPath, yearPath } from "./year.js";
import type { CanonicalData, Expr, Inputs, Line } from "./types.js";

const PROFILES = ["social-security", "sales", "stage4", "full", "ny"] as const;
/** Profiles allowed a non-empty `initial`, with exactly that value: slice profiles of Stages 2 to 4, whose scope is a
 * single filer. The full and New York profiles, the return a filer prepares, have none. */
const SLICE_INITIAL = JSON.stringify({ $person: ["taxpayer"], "person[taxpayer].role": "taxpayer" });
const INITIAL_ALLOWED: Record<string, string> = { "social-security": SLICE_INITIAL, sales: SLICE_INITIAL, stage4: SLICE_INITIAL };
const GENERATED = Number(process.env["INTERVIEW_RULES_RUNS"] ?? 12);
const RANDOM_EVERY = Number(process.env["INTERVIEW_RULES_RANDOM_EVERY"] ?? 3);
/** Random traversals per chosen walk, each with its own seed. */
const RANDOM_SEEDS = Number(process.env["INTERVIEW_RULES_SEEDS"] ?? 5);
const SEED = 11;
const BASELINE = resolve(import.meta.dirname, "../..", "tools", "interview_rules_baseline.json");
const PRUNING = resolve(import.meta.dirname, "../..", "reports", String(YEAR), "interview_pruning.md");
/** The held lists, each keyed by input template with a reason. */
interface Baseline { early_completion: Record<string, string>; order_dependent_reach: Record<string, string>; walked_unused: Record<string, string> }

type Event = { input: string; value: unknown };
/** `exposed`: each input reachable at an incomplete state that a later answer made unreachable before it was answered,
 * with that answer's input. */
interface Walk { events: Event[]; inputs: Inputs; status: string; valuesKey: string; states: number; exposed: Record<string, string> }
/** The answer a walk gives to an input, or undefined when it has none. */
type Answers = (key: string, current: Inputs) => { value: unknown } | undefined;
const fromInputs = (inputs: Inputs): Answers => (key) => (key in inputs ? { value: inputs[key] } : undefined);

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

/** Walks the interview answering from `answers`: `pick` chooses the next input among the open ones. While the return is
 * incomplete every reachable unanswered input is open, so a pick `answers` lacks is a question this order reaches and
 * the answers do not cover: without `reach` it throws Unanswered; with `reach` every such input open at the state is
 * reported there and the pick is made among the answered ones. A refusal is provisional (a later answer may clear it), so the walk goes on past it while a
 * reachable question has an answer, and ends complete or when none has; past a refusal only answered inputs are open.
 * Reports early completion at every state to `leak`. */
function walk(data: CanonicalData, config: InterviewData, answers: Answers, pick: (open: string[]) => string, bound: number, leak: (reachable: string[]) => void, reach?: (key: string) => void): Walk {
  let current: Inputs = structuredClone(config.initial);
  const events: Event[] = [];
  const exposed: Record<string, string> = {};
  let pending: string[] = [];
  for (let step = 0; ; step++) {
    if (step > bound) throw new Error("the walk did not end");
    const st = interviewStatus(data, config, current);
    if (st.status === "complete" && st.reachableInputs.length) leak(st.reachableInputs);
    const now = new Set(st.reachableInputs);
    for (const k of pending) if (!now.has(k) && !(k in current) && !(k in exposed)) exposed[k] = events.at(-1)!.input;
    pending = st.status === "incomplete" ? st.reachableInputs.filter((k) => !(k in current)) : [];
    const done = () => ({ events, inputs: current, status: st.status, valuesKey: targetKey(data, config, current), states: step + 1, exposed });
    if (st.status === "complete") return done();
    let open = st.status === "incomplete" ? [...pending] : st.reachableInputs.filter((k) => !(k in current) && answers(k, current));
    if (st.status === "refused" && !open.length) return done();
    if (reach && st.status === "incomplete") {
      for (const k of open) if (!answers(k, current)) reach(k);
      open = open.filter((k) => answers(k, current));
    }
    if (!open.length) throw new Error("incomplete, and no reachable question has an answer");
    const key = pick(open);
    const answer = answers(key, current);
    if (!answer) throw new Unanswered(key);
    events.push({ input: key, value: answer.value });
    current = { ...current, [key]: answer.value };
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

/** A complete walk's fixture answers, classed. `askedUnread`: asked, and not read by the complete return's evaluation (a
 * question a later answer made moot). `outOfOrder`: reachable at an incomplete state and never asked, each with the
 * answer that made it unreachable. `withheld`: how many answers were neither asked nor read (leftovers). `readUnasked`:
 * read and never asked, which a complete walk cannot leave (a problem if any). */
export interface Classes { askedUnread: string[]; outOfOrder: Record<string, string>; withheld: number; readUnasked: string[] }

/** The inputs an evaluation reads: each input line it evaluates, and each roster a collection sum confirms. */
function readInputs(data: CanonicalData, config: InterviewData, inputs: Inputs): Set<string> {
  const read = new Set<string>();
  for (const [k, der] of evaluate(data, inputs, config.targets).derivations) {
    if (der.op === "input") read.add(k);
    for (const n of der.notes) { const m = /^confirmed roster (\S+):/.exec(n); if (m) read.add(m[1]!); }
  }
  return read;
}

function classify(data: CanonicalData, config: InterviewData, inputs: Inputs, w: Walk): Classes {
  const read = readInputs(data, config, inputs);
  const asked = new Set(w.events.map((e) => e.input));
  const keys = Object.keys(inputs).filter((k) => !(k in config.initial));
  return {
    askedUnread: [...asked].filter((k) => !read.has(k)).sort(),
    outOfOrder: Object.fromEntries(Object.entries(w.exposed).filter(([k]) => !asked.has(k))),
    withheld: keys.filter((k) => !asked.has(k) && !read.has(k)).length,
    readUnasked: keys.filter((k) => read.has(k) && !asked.has(k)).sort(),
  };
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
      if (q.value_labels) {
        const meta = inputMeta(data, q.input);
        const texts = Object.values(q.value_labels);
        if (new Set(texts).size !== texts.length) errors.push(`no-input-set: ${p} ${q.input}: two values share a label`);
        if (JSON.stringify(Object.keys(q.value_labels).sort()) !== JSON.stringify([...(meta.values ?? [])].sort())) errors.push(`no-input-set: ${p} ${q.input}: the value labels are not one per value of the enum`);
      }
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
  return heldProblems(seen, baseline, (t, where) => `completion: ${where}: reported complete while ${t} is reachable and unanswered`,
    (t) => `completion: ${t} no longer leaks; remove it from early_completion in tools/interview_rules_baseline.json`);
}

/** A list of templates held by a baseline key: a template seen and not held fails (`found`), and so does one held and no
 * longer seen (`gone`), until it is removed. `seen` maps each template to the first case that showed it. */
export function heldProblems(seen: Map<string, string>, baseline: Record<string, string>, found: (t: string, where: string) => string, gone: (t: string) => string): string[] {
  const out: string[] = [];
  for (const [t, where] of [...seen].sort()) if (!(t in baseline)) out.push(found(t, where));
  for (const t of Object.keys(baseline).sort()) if (!seen.has(t)) out.push(gone(t));
  return out;
}

/** The minimal returns' closed answer to an input: an empty roster (the taxpayer alone for `$person`), false, zero, the
 * first enum value; where that answer refuses the return and another value of a Bool or enum does not, that value. */
function closedAnswer(data: CanonicalData, config: InterviewData, key: string, current: Inputs): unknown {
  if (key.startsWith("$")) return questionTemplate(key) === "$person" ? ["taxpayer"] : [];
  if (/^person\[[^\]]+\]\.role$/.test(key)) return key.slice(7, key.indexOf("]"));
  const meta = inputMeta(data, key);
  const first = meta.type === "Bool" ? false : meta.type === "Enum" ? meta.values![0] : 0;
  const refuses = (v: unknown) => interviewStatus(data, config, { ...current, [key]: v }).status === "refused";
  if (!refuses(first)) return first;
  const other = (meta.type === "Bool" ? [true] : meta.type === "Enum" ? meta.values!.slice(1) : []).find((v) => !refuses(v));
  return other === undefined ? first : other;
}

/** Answers the minimal returns fix beyond the closed answers: New York refuses every return whose federal AGI is below
 * the federal earned income credit limit (its own credit is not computed), so its minimal return has income
 * above that limit, as unemployment compensation (which asks no employer questions). */
const MINIMAL_BASE: Partial<Record<"full" | "ny", Inputs>> = { ny: { "s1.uc_paid": 5_000_000 } };

/** The existence gates: the inputs a gate line's guard reads directly, and for each the gated inputs it can open (those
 * whose gate line's guards read it, directly or through other lines). */
export function existenceGates(data: CanonicalData): Map<string, Set<string>> {
  const lines = new Map([...data.forms, ...data.defs].flatMap((d) => d.lines.map((l) => [l.id, l] as const)));
  const memo = new Map<string, Set<string>>();
  const deps = (id: string): Set<string> => {
    const hit = memo.get(id);
    if (hit) return hit;
    const out = new Set<string>([id]);
    memo.set(id, out);
    const line = lines.get(id);
    if (line) for (const r of readsOf(line)) if (lines.has(r)) for (const d of deps(r)) out.add(d);
    return out;
  };
  const gates = new Map<string, Set<string>>();
  const gated = gatesOf(data);
  for (const g of gated) for (const r of g.guardRefs) if (lines.get(r)?.expr.op === "input") gates.set(r, new Set());
  for (const [input, opens] of gates) for (const g of gated) if (g.guardRefs.some((r) => deps(r).has(input))) opens.add(g.input);
  return gates;
}

/** A minimal return's walk: `open` names the existence gate opened (with its value), or none for every gate closed.
 * Throws Unanswered when the interview asks an input gated by a closed gate. */
function minimalWalk(data: CanonicalData, config: InterviewData, profile: "full" | "ny", open: { input: string; value: unknown } | null, leak: (reachable: string[]) => void): Walk {
  const gates = existenceGates(data);
  const allowed = open ? gates.get(open.input) ?? new Set<string>() : new Set<string>();
  const closed = new Set(gatesOf(data).map((g) => g.input).filter((i) => !allowed.has(i)));
  const base = MINIMAL_BASE[profile] ?? {};
  const answers: Answers = (key, current) => {
    const t = questionTemplate(key);
    if (open && t === open.input) return { value: open.value };
    if (closed.has(t)) return undefined;
    return { value: key in base ? base[key] : closedAnswer(data, config, key, current) };
  };
  return walk(data, config, answers, bankOrder(config), 800, leak);
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
  | { kind: "subsets"; profile: "full" | "ny"; w: Walk; seed: number }
  | { kind: "minimal"; profile: "full" | "ny"; open: { input: string; value: unknown } | null };
/** `reached` (random): the inputs a complete return's traversal reached that its bank-order walk never asked. */
export type TaskResult =
  | { kind: "walked"; w: Walk; leaks: string[][]; bad: string | null; classes: Classes | null }
  | { kind: "unanswered"; input: string; leaks: string[][] }
  | { kind: "failed"; error: string; leaks: string[][] }
  | { kind: "errors"; errors: string[]; leaks: string[][]; reached: string[] };

export interface Context { data: CanonicalData; configs: Record<(typeof PROFILES)[number], InterviewData> }

export function loadContext(): Context {
  return { data: loadCanonical(), configs: Object.fromEntries(PROFILES.map((p) => [p, loadInterview(p)])) as Context["configs"] };
}

export function runTask({ data, configs }: Context, task: Task): TaskResult {
  const leaks: string[][] = [];
  const config = configs[task.profile];
  if (task.kind === "walk" || task.kind === "minimal") {
    try {
      if (task.kind === "minimal") {
        const w = minimalWalk(data, config, task.profile, task.open, (r) => leaks.push(r));
        return { kind: "walked", w, leaks, bad: onlyGiven(config, w.events), classes: w.status === "complete" ? classify(data, config, replayed(config, w.events), w) : null };
      }
      const w = walk(data, config, fromInputs(task.c.inputs), bankOrder(config), 800, (r) => leaks.push(r));
      return { kind: "walked", w, leaks, bad: onlyGiven(config, w.events), classes: w.status === "complete" ? classify(data, config, task.c.inputs, w) : null };
    } catch (e) {
      return e instanceof Unanswered ? { kind: "unanswered", input: e.message, leaks } : { kind: "failed", error: String(e), leaks };
    }
  }
  const errors: string[] = [];
  const reached = new Set<string>();
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
      const r = walk(data, config, fromInputs(replayed(config, w.events)), (open) => open[Math.floor(rand() * open.length)]!, 800, (x) => leaks.push(x), (k) => { if (w.status === "complete") reached.add(k); });
      if (r.status !== w.status || r.valuesKey !== w.valuesKey) errors.push(`order: ${group}: ${c.id}: a random answering order gives a different ${r.status !== w.status ? `status (${r.status}, not ${w.status})` : "value"}`);
    } catch (e) {
      errors.push(`order: ${group}: ${c.id}: random answering order: ${String(e)}`);
    }
  } else {
    const rand = rng(task.seed);
    for (let k = 0; k < 3; k++) {
      const kept = w.events.filter(() => rand() < 0.5);
      const st = interviewStatus(data, config, replayed(config, kept));
      if (st.status === "complete" && st.reachableInputs.length) leaks.push(st.reachableInputs);
    }
  }
  return { kind: "errors", errors, leaks, reached: [...reached].sort() };
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
  // The reach classes of complete returns, by template: the first case (and, out of order, the answer that hid it).
  const outOfOrder = new Map<string, string>();
  const askedUnread = new Map<string, { where: string; cases: number }>();
  let withheld = 0, classed = 0;
  const classIn = (where: string, cl: Classes) => {
    classed++;
    withheld += cl.withheld;
    for (const [k, by] of Object.entries(cl.outOfOrder)) if (!outOfOrder.has(questionTemplate(k))) outOfOrder.set(questionTemplate(k), `${where}: ${k}, until ${by} was answered`);
    for (const t of new Set(cl.askedUnread.map(questionTemplate))) {
      const x = askedUnread.get(t);
      if (x) x.cases++; else askedUnread.set(t, { where: `${where}: ${cl.askedUnread.find((k) => questionTemplate(k) === t)}`, cases: 1 });
    }
    for (const k of cl.readUnasked) errors.push(`reach: ${where}: the complete return reads ${k}, which the walk never asked`);
  };

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
            if (r.classes) classIn(`${g.name}: ${c.id}`, r.classes);
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
        for (let s = 0; s < RANDOM_SEEDS; s++) chosen.push({ ...x, seed: seed + s * 100003 });
      }
      traversals = chosen.length;
      const results = await mapPool(chosen, ({ group, profile, c, w, seed }) => workers.run({ kind: "random", profile, group, c, w, seed }), limit);
      for (const [k, r] of results.entries()) {
        const { group, c } = chosen[k]!;
        for (const reachable of r.leaks) leakIn(`${group}: ${c.id} (random order)`)(reachable);
        if (r.kind !== "errors") continue;
        errors.push(...r.errors);
        for (const k of r.reached) if (!outOfOrder.has(questionTemplate(k))) outOfOrder.set(questionTemplate(k), `${group}: ${c.id}: ${k}, in a random order`);
      }
    });

    await timed("completion: random subsets of the answers", async () => {
      const results = await mapPool(walks, ({ profile, w }, i) => workers.run({ kind: "subsets", profile, w, seed: SEED * 7919 + i }), limit);
      for (const [k, r] of results.entries()) {
        const { group, c } = walks[k]!;
        for (const reachable of r.leaks) leakIn(`${group}: ${c.id} (a subset of its answers)`)(reachable);
      }
    });
    const minimal: string[] = [];
    await timed("minimal returns: every gate closed, and each existence gate opened alone", async () => {
      const gates = existenceGates(data);
      const profiles = ["full", "ny"] as const;
      const closed = await mapPool([...profiles], (profile) => workers.run({ kind: "minimal", profile, open: null }), limit);
      const tasks: { profile: "full" | "ny"; open: { input: string; value: unknown } }[] = [];
      for (const [i, profile] of profiles.entries()) {
        const r = closed[i]!;
        if (!minimalResult(`${profile}: every gate closed`, r)) continue;
        const asked = new Map((r as Extract<TaskResult, { kind: "walked" }>).w.events.map((e) => [e.input, e.value]));
        const unreached: string[] = [];
        for (const g of [...gates.keys()].sort()) {
          if (!asked.has(g)) { unreached.push(g); continue; }
          const meta = inputMeta(data, g);
          const values = meta.type === "Bool" ? [true] : (meta.values ?? []).filter((v) => v !== asked.get(g));
          for (const value of values) tasks.push({ profile, open: { input: g, value } });
        }
        minimal.push(`${profile}: every gate closed asks ${asked.size} question(s); existence gates not reached there: ${unreached.join(", ") || "none"}`);
      }
      const opened = await mapPool(tasks, ({ profile, open }) => workers.run({ kind: "minimal", profile, open }), limit);
      for (const [i, { profile, open }] of tasks.entries()) minimalResult(`${profile}: ${open.input} = ${JSON.stringify(open.value)} alone`, opened[i]!);
      minimal.push(`${tasks.length} return(s) with one existence gate opened`);
    });
    return report(walks.length, traversals, counts, minimal);
  } finally {
    await workers.close();
  }

  /** A minimal return's result: it must complete; its classes join the fixtures'. Whether it completed. */
  function minimalResult(name: string, r: TaskResult): boolean {
    for (const reachable of r.leaks) leakIn(`minimal: ${name}`)(reachable);
    if (r.kind === "walked" && r.w.status === "complete") {
      if (r.bad) errors.push(`no-input-set: minimal: ${name}: ${r.bad}`);
      if (r.classes) classIn(`minimal: ${name}`, r.classes);
      return true;
    }
    errors.push(`minimal: ${name}: ${r.kind === "walked" ? `ends ${r.w.status}` : r.kind === "unanswered" ? `asks ${r.input}, an input gated by a closed gate` : r.kind === "failed" ? r.error : "no walk"}`);
    return false;
  }

  function report(walkCount: number, traversals: number, counts: string[], minimal: string[]): number {
    const held = JSON.parse(readFileSync(BASELINE, "utf8")) as Baseline;
    const baseline = held.early_completion;
    errors.push(...leakProblems(seen, baseline));
    errors.push(...heldProblems(outOfOrder, held.order_dependent_reach, (t, where) => `reach: ${where}: ${t} is reachable before the answer that hides it, and the walk in bank order never asks it`,
      (t) => `reach: ${t} is no longer reached out of bank order; remove it from order_dependent_reach in tools/interview_rules_baseline.json`));
    errors.push(...heldProblems(new Map([...askedUnread].map(([t, x]) => [t, x.where])), held.walked_unused, (t, where) => `reach: ${where}: ${t} is asked in bank order and unread by the complete return`,
      (t) => `reach: ${t} is no longer asked and unread; remove it from walked_unused in tools/interview_rules_baseline.json`));
    for (const line of counts) console.log(`  ${line}`);
    for (const line of minimal) console.log(`  minimal returns: ${line}`);
    console.log(`  early completion: ${seen.size} input template(s) left reachable at completion, ${Object.keys(baseline).length} held by the baseline`);
    console.log(`  reach: ${classed} complete returns classed; ${withheld} leftover answer(s) withheld from their random traversals; ${outOfOrder.size} template(s) reached only out of bank order (${Object.keys(held.order_dependent_reach).length} held); ${askedUnread.size} asked and unread (${Object.keys(held.walked_unused).length} held)`);
    console.log(`  pruning opportunities (asked in bank order, unread by the complete return):`);
    for (const [t, x] of [...askedUnread].sort()) console.log(`    ${t}: ${x.cases} return(s), first ${x.where}`);
    if (args.includes("--write-pruning")) writePruning();
    for (const t of times) console.log(`  time: ${t}`);
    for (const e of errors.slice(0, 60)) console.error(`  ${e}`);
    if (errors.length > 60) console.error(`  ... and ${errors.length - 60} more`);
    console.log(`interview-rules: ${errors.length} problem(s); ${walkCount} walks, each replayed reversed and shuffled; ${traversals} answered in a random order`);
    return errors.length ? 1 : 0;
  }

  function writePruning(): void {
    const rows = [...askedUnread].sort().map(([t, x]) => `| \`${t}\` | ${x.cases} | ${x.where} |`);
    writeFileSync(PRUNING, [
      "# Interview pruning opportunities",
      "",
      "Written by `node engine/dist/main.js interview-rules --write-pruning`. Each template below is a question the interview asks in bank order",
      "that the complete return's evaluation then does not read: a later answer made it moot. Asking it is allowed (only reachability hides a",
      "question), so these are not failures; each is a conjunction to rewrite as a nested choose, or an order that asks the deciding question",
      "late. They are held in `walked_unused` of `tools/interview_rules_baseline.json`, so a new one fails until it is listed.",
      "",
      `Over ${classed} complete returns (the Stage 5 and New York fixtures, generated returns and the minimal returns).`,
      "",
      "| Template | Returns | First return: input |",
      "|---|---|---|",
      ...rows,
      "",
    ].join("\n"));
    console.log(`  wrote ${PRUNING}`);
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
  const labelled = (c: Record<string, InterviewData>) => c["full"]!.questions.find((q) => q.value_labels)!.value_labels!;
  assert.match(planted((c) => { const l = labelled(c); const [a, b] = Object.keys(l); l[b!] = l[a!]!; }), /two values share a label/);
  assert.match(planted((c) => { const l = labelled(c); delete l[Object.keys(l)[0]!]; }), /value labels are not one per value/);
  const lq = configs["full"]!.questions.find((q) => q.value_labels)!;
  const hint = entryHint(data, lq.input, undefined, lq.value_labels);
  for (const [v, label] of Object.entries(lq.value_labels!)) assert.ok(hint.includes(`${JSON.stringify(v)} (${label})`), `the entry hint names ${v} with its label: ${hint}`);
  const config = configs["full"]!;
  assert.equal(onlyGiven(config, [{ input: "a.x", value: 1 }, { input: "a.x", value: 2 }]), null);
  assert.deepEqual(replayed(config, [{ input: "a.x", value: 1 }, { input: "a.x", value: 2 }]), { "a.x": 2 });
  assert.deepEqual(leakProblems(new Map([["p.a", "case 1"]]), { "p.a": "held" }), []);
  assert.match(leakProblems(new Map([["p.a", "case 1"], ["p.b", "case 2"]]), { "p.a": "held" }).join("\n"), /case 2: reported complete while p\.b is reachable/);
  assert.match(leakProblems(new Map(), { "p.a": "held" }).join("\n"), /p\.a no longer leaks/);
  const context = { data, configs: configs as Context["configs"] };

  // The minimal returns complete on the data as it is, and fail on a gate removed or inverted.
  for (const profile of ["full", "ny"] as const) {
    const r = runTask(context, { kind: "minimal", profile, open: null });
    assert.ok(r.kind === "walked" && r.w.status === "complete", `the ${profile} minimal return completes`);
  }
  const gate = divGate(data);
  const ungated = plantUngated(data, gate.input);
  assert.match(gateProblems(ungated).join("\n"), new RegExp(`${gate.input.replace(".", "\\.")} .*read by`), "the static gate check names an ungated reader");
  const inverted = plantInvertedGate(data, gate.input);
  assert.deepEqual(gateProblems(inverted), [], "an inverted gate passes the static gate check");
  for (const d of [ungated, inverted]) {
    const r = runTask({ data: d, configs: context.configs }, { kind: "minimal", profile: "full", open: null });
    assert.ok(r.kind === "unanswered" && r.input === gate.input, `the minimal return asks ${gate.input} behind a closed gate: ${JSON.stringify(r.kind === "unanswered" ? r.input : r.kind)}`);
  }

  // A leftover fixture answer masks a planted conjunction leak from the fixture values and the walk in bank order; the
  // reach class names it.
  const c = fixtureCases(yearPath("fixtures", "stage5.json"), data).find((x) => x.id === LEAK_CASE)!;
  const clean = runTask(context, { kind: "walk", profile: "full", c });
  assert.ok(clean.kind === "walked" && clean.classes, "the clean case walks to completion");
  const pair = leakPair(data, config, c.inputs, (clean as Extract<TaskResult, { kind: "walked" }>).w);
  const leaky = plantLeak(data, config.targets[0]!, pair.decider, pair.leaked);
  assert.equal(targetKey(leaky, config, c.inputs), targetKey(data, config, c.inputs), "the planted leak changes no value");
  const r = runTask({ data: leaky, configs: context.configs }, { kind: "walk", profile: "full", c });
  assert.ok(r.kind === "walked" && r.classes, "the bank-order walk over the fixture's answers completes");
  assert.ok(pair.leaked in r.classes!.outOfOrder && !(pair.leaked in clean.classes!.outOfOrder), `the reach class names ${pair.leaked}, reached before ${pair.decider} hides it`);
  assert.equal(r.classes!.outOfOrder[pair.leaked], pair.decider);
  const withheld = runTask({ data: leaky, configs: context.configs }, { kind: "random", profile: "full", group: "self-test", c, w: r.w, seed: SEED });
  assert.ok(withheld.kind === "errors" && !withheld.errors.length, "the random traversal still agrees on the values");
  console.log(`interview-rules self-test: 25 cases passed (profile initial, roster choices, value labels and their entry hint, replay, early-completion baseline; minimal returns, ${gate.input} ungated and its gate inverted; a leak of leftover ${pair.leaked} behind ${pair.decider})`);
  return 0;
}

/** The fixture the planted leak uses. */
const LEAK_CASE = "stage5.return.owed";

/** The gated input of `div.any`'s gate on Schedule B line 5: the self-test's broken gate. */
function divGate(data: CanonicalData) {
  const g = gatesOf(data).find((x) => x.guardRefs.length === 1 && x.guardRefs[0] === "div.any" && x.input === "sb.ordinary_dividends");
  if (!g) throw new Error("self-test: no gate of div.any on sb.ordinary_dividends");
  return g;
}

/** The data with every reader of `input`'s gate line reading the gated input directly (the gate removed). */
export function plantUngated(data: CanonicalData, input: string): CanonicalData {
  const d = structuredClone(data);
  const line = gatesOf(d).find((g) => g.input === input)!.line;
  const swap = (node: unknown): unknown => node === line ? input : Array.isArray(node) ? node.map(swap)
    : node && typeof node === "object" ? Object.fromEntries(Object.entries(node).map(([k, v]) => [k, k === "cite" ? v : swap(v)])) : node;
  for (const doc of d.forms) for (const l of doc.lines) if (l.id !== line) l.expr = swap(l.expr) as Line["expr"];
  return d;
}

/** The data with `input`'s gate line taking the input when its guard is false and the else when true. */
export function plantInvertedGate(data: CanonicalData, input: string): CanonicalData {
  const d = structuredClone(data);
  const line = gatesOf(d).find((g) => g.input === input)!.line;
  const l = d.forms.flatMap((f) => f.lines).find((x) => x.id === line)!;
  const alts = (l.expr as Extract<Expr, { op: "choose" }>).alternatives;
  const thens = alts.map((a) => a.then).reverse();
  alts.forEach((a, i) => { a.then = thens[i]!; });
  return d;
}

/** A leftover Bool answer of `inputs` (not asked by `w`, not read, not gated) and an earlier-ordered Bool the walk
 * answered false: a conjunction of the two is decided by the second before the first is asked. */
export function leakPair(data: CanonicalData, config: InterviewData, inputs: Inputs, w: Walk): { decider: string; leaked: string } {
  const order = new Map(config.questions.map((q) => [q.input, q.order]));
  const gated = new Set(gatesOf(data).map((g) => g.input));
  const plain = (k: string) => !k.startsWith("$") && !k.includes("[") && !gated.has(k) && inputMeta(data, k).type === "Bool";
  const asked = new Map(w.events.map((e) => [e.input, e.value]));
  const read = readInputs(data, config, inputs);
  const leftovers = Object.keys(inputs).filter((k) => plain(k) && !asked.has(k) && !read.has(k)).sort();
  const deciders = [...asked].filter(([k, v]) => plain(k) && v === false).map(([k]) => k).sort();
  for (const leaked of leftovers) for (const decider of deciders) if (order.get(decider)! < order.get(leaked)!) return { decider, leaked };
  throw new Error("self-test: no leftover Bool answer with an earlier false Bool to hide it");
}

/** The data with a refusal of `target` on all(`decider`, `leaked`), put before the target's own refusals (an earlier refusal
 * gate left unknown would stop its evaluation): the leaked input is reachable while the decider is
 * unanswered, and no value changes while the decider is false. */
export function plantLeak(data: CanonicalData, target: string, decider: string, leaked: string): CanonicalData {
  const d = structuredClone(data);
  const doc = d.forms.find((f) => f.lines.some((l) => l.id === target))!;
  const t = doc.lines.find((l) => l.id === target)!;
  const id = `${doc.id}.planted_leak`;
  const isTrue = (ref: string) => ({ op: "test", eq: [ref, { const: true }] });
  doc.lines.push({ id, printed: "(planted)", label: "planted leak", type: "Bool", expr: { op: "test", all: [isTrue(decider), isTrue(leaked)] } as unknown as Expr, cite: t.cite });
  t.refuses = [{ when: id, form: "planted", remedy: "planted", cite: t.cite }, ...(t.refuses ?? [])];
  return d;
}
