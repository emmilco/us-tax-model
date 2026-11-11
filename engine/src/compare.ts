// Two-evaluator agreement: run every fixture case and a deterministic corpus of generated whole returns through the
// TypeScript evaluator and the Lean reference evaluator, and fail on any difference (spec section 6.3 / design 2.6).

import { existsSync, mkdtempSync, rmSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { allTargets, evaluate } from "./eval.js";
import { isNyDoc } from "./fixture-inputs.js";
import { loadCases } from "./fixtures.js";
import { CORPUS_SEED, CORPUS_SIZE, corpusReturns } from "./generate.js";
import { coverageCorpus } from "./properties.js";
import type { CanonicalData, Inputs } from "./types.js";
import type { Value } from "./eval.js";
import { NY_MODE, YEAR, YEAR_ARGS, yearPath } from "./year.js";
import { reportName, reportPath } from "./year.js";
import { TYPED_CHOOSE_CASES, typedChooseData, valueText } from "./check-selftest.js";

const ROOT = resolve(import.meta.dirname, "../..");
const LEAN_BIN = join(ROOT, "lean", ".lake", "build", "bin", "taxeval");
const CANON = yearPath("canonical");

// The generated corpus comes from the general generator (generate.ts), which draws every declared input, so the
// corpus follows the model. It is the corpus of the properties check (generate.ts corpusReturns, which both
// commands call): the branch coverage the properties report lists is then the coverage of the returns compared here.
// At the default size the number of inputs the corpus varies has levelled off (doubling it adds about one input in a
// hundred).
//
// Both evaluators read the whole canonical build, so each run compares the lines of every document, federal and
// New York. On a federal case, which gives no New York answers, most New York lines are unknown; the rest (constants,
// lines that read federal lines only, refusals that reach them) have values, and the federal fixture cases are
// compared by no other run, so the New York lines stay in the federal run. The report counts them apart.

// The reason of the Lean evaluator's unknown for a line it ran out of steps on (Eval.lean, budgetExhausted).
const BUDGET_EXHAUSTED = "step budget exhausted";

interface Case {
  id: string;
  inputs: Inputs;
}

type LeanValues = Record<string, Record<string, unknown>>;

/** What the Lean evaluator gave for one case: its values, or the reason it gave none. */
type LeanResult = LeanValues | string;

// The cases one process of the Lean evaluator is given. A process reads the canonical build once, which takes
// about as long as evaluating one or two cases, and its whole answer (about 280 kB a case) is held in memory here
// until it is compared: a larger batch saves little time and costs memory.
const BATCH_SIZE = 50;

// How long one process of the Lean evaluator may take, in minutes. A process that has not ended by then is stopped
// and the run fails, where it would otherwise wait for ever. A batch takes seconds; the limit is longer than a whole
// run of the comparison takes on a machine with many times more runnable work than cores.
const BATCH_LIMIT_MINUTES = 20;

/** How the Lean evaluator is started: the command (the program, then any arguments before the comparison's own),
 * the time one process may take, and, once a process has passed that time, why no further process is started. */
interface LeanRunner { command: string[]; limitMinutes: number; stopped?: string }
const LEAN: LeanRunner = { command: [LEAN_BIN], limitMinutes: BATCH_LIMIT_MINUTES };

function fixtureCases(): Case[] {
  const file = loadCases();
  return file.cases.map((c) => ({ id: c.id, inputs: c.inputs }));
}

/** The generated whole returns the comparison runs on: the corpus shared with the properties check. Federal returns
 * (the inputs of the federal documents only) or, with `ny`, the same returns each with the answers of the New York
 * documents. */
export function comparedCorpus(all: CanonicalData, ny: boolean): Inputs[] {
  return corpusReturns(all, ny);
}

function generatedCases(all: CanonicalData): Case[] {
  return comparedCorpus(all, NY_MODE).map((inputs, i) => ({ id: `generated.${String(i).padStart(3, "0")}`, inputs }));
}

// The size the corpus self-test's second process is given, to see that both commands follow PROPERTY_RUNS.
const OVERRIDE_SIZE = 3;

/** `compare --corpus-self-test`: the comparison's generated returns are the properties check's. For federal returns
 * and for returns with New York answers, the returns this module compares (comparedCorpus) and the returns the
 * properties report's coverage is of (properties.ts coverageCorpus) must be the same returns, as many as the shared
 * size; a return with New York answers must carry every answer of the federal return of its index; and a second
 * process, given another size in PROPERTY_RUNS, must find both corpora of that size, so neither command keeps a
 * size of its own. Returns the exit status. */
export function corpusSelfTest(): number {
  const all = loadCanonical();
  const problems: string[] = [];
  const federal = comparedCorpus(all, false);
  const withNy = comparedCorpus(all, true);
  for (const [name, compared, covered] of [["federal", federal, coverageCorpus(all, false)], ["New York", withNy, coverageCorpus(all, true)]] as const) {
    if (compared.length !== CORPUS_SIZE) problems.push(`${name}: the comparison has ${compared.length} generated returns, the shared size is ${CORPUS_SIZE}`);
    if (covered.length !== CORPUS_SIZE) problems.push(`${name}: the properties check has ${covered.length} generated returns, the shared size is ${CORPUS_SIZE}`);
    const differing = compared.findIndex((inputs, i) => JSON.stringify(inputs) !== JSON.stringify(covered[i]));
    if (compared.length !== covered.length || differing >= 0) problems.push(`${name}: the comparison's generated returns are not the properties check's (${compared.length} and ${covered.length} returns${differing >= 0 ? `, first difference at return ${differing}` : ""})`);
  }
  const apart = federal.findIndex((inputs, i) => Object.entries(inputs).some(([k, v]) => JSON.stringify(withNy[i]?.[k]) !== JSON.stringify(v)));
  if (apart >= 0) problems.push(`return ${apart} with New York answers does not carry every answer of federal return ${apart}`);
  if (process.env["PROPERTY_RUNS"] === undefined) {
    const proc = spawnSync(process.execPath, [process.argv[1]!, "compare", "--corpus-self-test", ...YEAR_ARGS], { encoding: "utf-8", env: { ...process.env, PROPERTY_RUNS: String(OVERRIDE_SIZE) } });
    const want = `compare corpus self-test: ${OVERRIDE_SIZE} federal returns and ${OVERRIDE_SIZE} with New York answers`;
    if (proc.status !== 0 || !proc.stdout.startsWith(want)) problems.push(`with PROPERTY_RUNS=${OVERRIDE_SIZE} the two commands do not both use ${OVERRIDE_SIZE} returns: ${(proc.stdout + proc.stderr).trim()}`);
  }
  for (const p of problems) console.error(`compare corpus self-test: ${p}`);
  console.log(`compare corpus self-test: ${federal.length} federal returns and ${withNy.length} with New York answers (seed ${CORPUS_SEED}) are the properties check's, ${problems.length} problem(s)`);
  return problems.length ? 1 : 0;
}

function normalize(v: Value | Record<string, unknown>): string {
  const val = v as { kind?: string; cents?: number; value?: unknown };
  if (val.kind === "refusal") { const r = v as Record<string, unknown>; return `refusal:${r.gate}:${r.form}:${r.remedy}:${JSON.stringify(Object.entries(r.cite as Record<string, unknown>).sort())}`; }
  if (val.kind === "unknown") return "unknown";
  if (val.kind === "money") return `money:${val.cents}`;
  if (val.kind === "rate") { const r = v as { num?: number; den?: number }; return `rate:${r.num}/${r.den}`; }
  return `${val.kind}:${JSON.stringify(val.value)}`;
}

/** The results of the cases with the given ids from the lines the Lean evaluator answered them with. The answer
 * must be as many lines as cases, the line in each place naming the case in that place and giving either its
 * values or the reason it has none: then every case is answered once and nothing else is. Any other answer (a case
 * not answered, answered twice or out of turn, an answer for a case that was not sent, a line that is no answer)
 * leaves no line of it to be trusted: every case then has no values, for that reason. */
function readAnswers(ids: string[], lines: string[]): LeanResult[] {
  const problems: string[] = [];
  const results = lines.map((line, i): LeanResult => {
    let answer: Record<string, unknown> = {};
    try {
      const parsed: unknown = JSON.parse(line);
      if (typeof parsed === "object" && parsed !== null) answer = parsed as Record<string, unknown>;
    } catch { /* not JSON: it names no case, which is reported below */ }
    const { id, values, failed } = answer;
    const hasValues = typeof values === "object" && values !== null && !Array.isArray(values);
    if (id !== ids[i]) problems.push(`answer ${i + 1} is for ${typeof id === "string" ? id : "no case"}, where ${ids[i] ?? "no case"} was sent`);
    else if (hasValues === (typeof failed === "string")) problems.push(`the answer for ${ids[i]} has neither values nor a reason for having none, or has both`);
    return hasValues ? values as LeanValues : `lean evaluator gave no values: ${String(failed)}`;
  });
  if (lines.length !== ids.length) problems.push(`${lines.length} answers for ${ids.length} cases`);
  if (problems.length === 0) return results;
  const reason = `the lean evaluator's answers are not the cases sent: ${problems.slice(0, 3).join("; ")}${problems.length > 3 ? `; and ${problems.length - 3} more` : ""}`;
  return ids.map(() => reason);
}

/** The Lean evaluator's result for each case, in the cases' order. A process of the evaluator reads the build in
 * `canon` once, then the cases, a line each, and answers a line each (lean/Main.lean); readAnswers holds its
 * answer to the cases sent. A process that ends with an error is charged to the first case it left unanswered:
 * the answers before that case stand, the case has no values, and the cases after it go to a new process. A
 * process that has not ended within the runner's time limit is stopped and charged in the same way, and no process
 * is started after it: the cases after it, in this call and in later ones, have no values, for that reason. */
function leanEvaluate(canon: string, cases: Case[], runner: LeanRunner = LEAN): LeanResult[] {
  const results: LeanResult[] = [];
  while (results.length < cases.length) {
    const rest = cases.slice(results.length);
    if (runner.stopped !== undefined) {
      results.push(...rest.map(() => runner.stopped!));
      break;
    }
    const ids = rest.map((c) => c.id);
    const input = rest.map((c) => `${JSON.stringify({ id: c.id, inputs: c.inputs })}\n`).join("");
    const proc = spawnSync(runner.command[0]!, [...runner.command.slice(1), "--canonical", canon],
      { input, encoding: "utf-8", maxBuffer: 1024 * 1024 * 1024, timeout: runner.limitMinutes * 60_000, killSignal: "SIGKILL" });
    // A last line without its newline was cut short and is no answer.
    const lines = (proc.stdout ?? "").split("\n").slice(0, -1);
    if (proc.status === 0 && !proc.error) {
      results.push(...readAnswers(ids, lines));
      continue;
    }
    const unanswered = ids[lines.length] ?? "no case";
    const late = (proc.error as NodeJS.ErrnoException | undefined)?.code === "ETIMEDOUT";
    const died = late
      ? `lean evaluator stopped: its process had not ended after ${runner.limitMinutes} minutes, with ${unanswered} the first case unanswered`
      : `lean evaluator exited ${proc.status ?? proc.signal}: ${proc.error ? `${proc.error.message}: ` : ""}${(proc.stderr ?? "").slice(0, 200)}`;
    if (late) runner.stopped = `not evaluated: the lean evaluator was stopped after ${runner.limitMinutes} minutes on ${unanswered}`;
    if (lines.length >= rest.length) results.push(...rest.map(() => died));
    else results.push(...readAnswers(ids.slice(0, lines.length), lines), died);
  }
  return results;
}

/** The self-test of the time limit: in place of the Lean evaluator, a process that reads nothing and answers
 * nothing, given three cases and a limit of a second. It must be stopped: the first case has no values because the
 * process was stopped on it, the others because no process was started after it, and a later call starts none
 * either. The process ends by itself after half a minute, so that with the limit not applied this self-test fails
 * and does not wait for ever. Returns the problems found. */
function neverAnswering(): string[] {
  const dir = mkdtempSync(join(tmpdir(), "compare-limit-"));
  const problems: string[] = [];
  try {
    const script = join(dir, "never.mjs");
    writeFileSync(script, "setTimeout(() => {}, 30000);\n");
    const runner: LeanRunner = { command: [process.execPath, script], limitMinutes: 1 / 60 };
    const cases = ["a", "b", "c"].map((id) => ({ id, inputs: {} }));
    const started = Date.now();
    const results = leanEvaluate(dir, cases, runner);
    const later = leanEvaluate(dir, cases.slice(0, 1), runner);
    const seconds = (Date.now() - started) / 1000;
    if (typeof results[0] !== "string" || !results[0].startsWith("lean evaluator stopped: ") || !results[0].endsWith("with a the first case unanswered")) problems.push(`the case the process was stopped on has: ${JSON.stringify(results[0])}`);
    for (const result of [results[1], results[2], later[0]]) {
      if (typeof result !== "string" || !result.startsWith("not evaluated: the lean evaluator was stopped ") || !result.endsWith(" on a")) problems.push(`a case after the stopped process has: ${JSON.stringify(result)}`);
    }
    if (results.length !== 3 || later.length !== 1) problems.push(`${results.length} and ${later.length} results for 3 cases and 1`);
    if (seconds < 0.9) problems.push(`the process was given up after ${seconds} s, before its limit of a second`);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
  return problems;
}

/** The self-test of readAnswers on a batch of three cases. Answers that are not the cases sent are planted, and
 * each must leave every case without values; answers that are the cases sent must give each case its own values,
 * and a case answered with a reason must have that reason and leave the other two their values. Returns the number
 * of answers planted and the problems found. */
function plantedAnswers(): { planted: number; problems: string[] } {
  const ids = ["a", "b", "c"];
  const line = (id: unknown, rest: Record<string, unknown>) => JSON.stringify({ id, ...rest });
  const good = ids.map((id) => line(id, { values: { [`${id}.line`]: { kind: "money", cents: 0 } } }));
  const [a, b, c] = good as [string, string, string];
  const problems: string[] = [];
  const own = (result: LeanResult | undefined, id: string) => typeof result === "object" && Object.keys(result).join() === `${id}.line`;
  if (!readAnswers(ids, good).every((result, i) => own(result, ids[i]!))) problems.push("answers that are the cases sent did not give each case its values");
  const reasoned = readAnswers(ids, [a, line("b", { failed: "planted" }), c]);
  if (!own(reasoned[0], "a") || reasoned[1] !== "lean evaluator gave no values: planted" || !own(reasoned[2], "c")) {
    problems.push("a case answered with a reason did not have the reason, or its neighbours did not keep their values");
  }
  const plants: [string, string[]][] = [
    ["the last answer missing", [a, b]],
    ["a middle answer missing", [a, c]],
    ["no answer at all", []],
    ["an answer more, for a case that was not sent", [a, b, c, line("d", { values: {} })]],
    ["an answer for a case that was not sent, in the place of one that was", [a, line("d", { values: {} }), c]],
    ["a case answered twice, in the place of another", [a, a, c]],
    ["a case answered twice, after every case was answered", [a, b, c, b]],
    ["two answers in each other's place", [b, a, c]],
    ["a line that is not JSON", [a, b.slice(0, 20), c]],
    ["an answer that names no case", [a, line(null, { failed: "the line has no id" }), c]],
    ["an answer with neither values nor a reason", [a, line("b", {}), c]],
    ["an answer with both values and a reason", [a, line("b", { values: {}, failed: "planted" }), c]],
  ];
  for (const [what, lines] of plants) {
    const results = readAnswers(ids, lines);
    if (results.length !== ids.length || !results.every((result) => typeof result === "string" && result.startsWith("the lean evaluator's answers are not the cases sent: "))) {
      problems.push(`${what}: a case was given values`);
    }
  }
  return { planted: plants.length, problems };
}

/** The TypeScript evaluator's values on the compared surface: every line of every form and every line of every
 * confirmed collection entry (the set the Lean evaluator emits). Internal aliases for cross-form references are
 * not part of it. */
function tsEvaluate(data: CanonicalData, rootLines: string[], inputs: Inputs): Record<string, Value> {
  const ts = evaluate(data, inputs, allTargets(data, inputs));
  const values: Record<string, Value> = {};
  for (const target of rootLines) {
    const der = ts.derivations.get(target);
    if (der) values[target] = der.value;
  }
  for (const [key, der] of ts.derivations) if (key.includes("[")) values[key] = der.value;
  return values;
}

/** What one case's comparison found. A line is compared when both evaluators give it and the Lean evaluator
 * finished it; `kinds` counts the compared lines by the kind of the TypeScript value, and `nyKinds` those of them
 * that are lines of the New York documents. A line only one evaluator gives (`oneSided`) and a line the Lean
 * evaluator ran out of steps on (`unfinished`) are not compared, and each is a problem. */
interface Comparison { problems: string[]; kinds: Record<string, number>; nyKinds: Record<string, number>; oneSided: number; unfinished: number }

function compareValues(tsValues: Record<string, Value>, leanValues: LeanValues): Comparison {
  const result: Comparison = { problems: [], kinds: {}, nyKinds: {}, oneSided: 0, unfinished: 0 };
  const tsKeys = Object.keys(tsValues).sort();
  const missingInLean = tsKeys.filter((k) => !(k in leanValues));
  const missingInTs = Object.keys(leanValues).sort().filter((k) => !(k in tsValues));
  result.oneSided = missingInLean.length + missingInTs.length;
  if (result.oneSided > 0) result.problems.push(`key sets differ (missing in lean: ${missingInLean.join(",")}; missing in ts: ${missingInTs.join(",")})`);
  for (const key of tsKeys) {
    const lean = leanValues[key];
    if (!lean) continue;
    if (lean.kind === "unknown" && lean.reason === BUDGET_EXHAUSTED) {
      result.unfinished++;
      result.problems.push(`${key}: lean ${BUDGET_EXHAUSTED}`);
      continue;
    }
    const kind = tsValues[key]!.kind;
    result.kinds[kind] = (result.kinds[kind] ?? 0) + 1;
    if (isNyDoc({ id: key })) result.nyKinds[kind] = (result.nyKinds[kind] ?? 0) + 1;
    const a = normalize(tsValues[key]!);
    const b = normalize(lean);
    if (a !== b) result.problems.push(`${key}: ts=${a} lean=${b}`);
  }
  return result;
}

/** The self-test: the Bool and enum `choose` lines of check-selftest's synthetic document, evaluated by both
 * evaluators on each of its cases. Every line must agree, and each choose line must have the value the case states.
 * Returns the problems found. */
function typedChooseAgreement(): string[] {
  const data = typedChooseData();
  const dir = mkdtempSync(join(tmpdir(), "compare-typed-"));
  const problems: string[] = [];
  try {
    mkdirSync(join(dir, "tables"));
    writeFileSync(join(dir, "c.json"), JSON.stringify({ form: data.forms[0] }));
    writeFileSync(join(dir, "params.json"), JSON.stringify({ params: data.params }));
    const targets = data.forms[0]!.lines.map((l) => l.id);
    const answers = leanEvaluate(dir, TYPED_CHOOSE_CASES.map(({ inputs }, i) => ({ id: `case${i}`, inputs: inputs as Inputs })));
    TYPED_CHOOSE_CASES.forEach(({ inputs, expect }, i) => {
      const lean = answers[i]!;
      if (typeof lean === "string") { problems.push(`case ${i}: ${lean}`); return; }
      const ts = evaluate(data, inputs as Inputs, targets).values;
      for (const id of targets) {
        const a = ts.get(id), b = lean[id];
        if (!a || !b) problems.push(`case ${i}: ${id} missing (ts ${a ? "present" : "absent"}, lean ${b ? "present" : "absent"})`);
        else if (normalize(a) !== normalize(b)) problems.push(`case ${i}: ${id}: ts=${normalize(a)} lean=${normalize(b)}`);
      }
      for (const [id, want] of Object.entries(expect)) {
        const got = ts.get(id);
        if (!got || valueText(got) !== want) problems.push(`case ${i}: ${id} is ${got ? valueText(got) : "absent"}, not ${want}`);
      }
    });
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
  return problems;
}

// The kinds of value the comparison tells apart (normalize).
const VALUE_KINDS = ["money", "count", "rate", "bool", "enum", "refusal", "unknown"];

/** Values that differ from `v`, a Lean value of the given kind, each with what was changed: one per field the
 * comparison reads (a refusal's gate, form, remedy and citation; a rate's numerator and denominator). For an
 * unknown, whose reason is not compared, the differing value is a known amount. */
function differingValues(kind: string, v: Record<string, unknown>): [string, Record<string, unknown>][] {
  if (kind === "money") return [["a money amount one cent higher", { ...v, cents: (v.cents as number) + 1 }]];
  if (kind === "count") return [["a count one higher", { ...v, value: (v.value as number) + 1 }]];
  if (kind === "bool") return [["the other Bool", { ...v, value: !v.value }]];
  if (kind === "enum") return [["another enum value", { ...v, value: `${v.value}_planted` }]];
  if (kind === "unknown") return [["a known amount where the line is unknown", { kind: "money", cents: 0 }]];
  if (kind === "rate") {
    return [["a rate with another numerator", { ...v, num: (v.num as number) + 1 }], ["a rate with another denominator", { ...v, den: (v.den as number) + 1 }]];
  }
  const cite = (v.cite ?? {}) as Record<string, unknown>;
  const field = Object.keys(cite).sort()[0] ?? "planted";
  return [
    ...["gate", "form", "remedy"].map((f): [string, Record<string, unknown>] => [`a refusal with another ${f}`, { ...v, [f]: `${v[f]}_planted` }]),
    ["a refusal with another citation", { ...v, cite: { ...cite, [field]: `${cite[field]}_planted` } }],
  ];
}

/** The self-test on generated returns: planted differences, each of which the comparison must report on the line
 * it was planted on, with the values planted. For each kind of value, the Lean evaluator's value of a computed
 * line of that kind (the first, by return and then by line, among the generated returns; an answered line when no
 * computed line has the kind) is replaced by each of differingValues. The unknown of an exhausted step budget is
 * planted on the money line and on the unknown line. The money line is removed from the Lean values, and a line
 * the TypeScript evaluator does not give is added to them. And the Lean evaluator is given the first return with
 * one money answer a dollar higher, so that the two evaluators compute from different answers. Returns the number
 * of differences planted and the problems found. */
function plantedDifferences(data: CanonicalData, rootLines: string[], generated: Case[]): { planted: number; problems: string[] } {
  const inputLines = new Set(data.forms.flatMap((d) => d.lines.filter((l) => l.expr.op === "input").map((l) => l.id)));
  // The line a compared key is a value of: the key itself, or for a line of a collection entry the collection's line.
  const lineOf = (key: string) => key.includes("]") ? key.slice(0, key.lastIndexOf("[")).split(".").pop() + key.slice(key.lastIndexOf("]") + 1) : key;
  const tsOf: Record<string, Value>[] = [];
  const site: Record<string, { index: number; key: string }> = {};
  for (const computed of [true, false]) {
    for (let i = 0; i < generated.length && VALUE_KINDS.some((k) => !site[k]); i++) {
      const ts = tsOf[i] ??= tsEvaluate(data, rootLines, generated[i]!.inputs);
      for (const key of Object.keys(ts).sort()) {
        if (!site[ts[key]!.kind] && inputLines.has(lineOf(key)) !== computed) site[ts[key]!.kind] = { index: i, key };
      }
    }
    if (computed) for (const k of VALUE_KINDS) if (!site[k]) console.log(`compare self-test: no computed line of a generated return is of kind ${k}; planting on an answered line`);
  }
  const problems: string[] = VALUE_KINDS.filter((k) => !site[k]).map((k) => `no line of a generated return is of kind ${k}`);
  const leanOf: Record<number, LeanResult> = {};
  let planted = 0;
  // One plant: the return's TypeScript values compared with altered Lean values must give the problem.
  const plant = (index: number, what: string, key: string, lean: LeanValues, problem: string, counted: (found: Comparison) => boolean = () => true) => {
    planted++;
    const found = compareValues(tsOf[index]!, lean);
    if (!found.problems.includes(problem) || !counted(found)) problems.push(`${generated[index]!.id}: ${what} on ${key} was not reported`);
  };
  for (const kind of VALUE_KINDS) {
    if (!site[kind]) continue;
    const { index, key } = site[kind]!;
    const lean = leanOf[index] ??= leanEvaluate(CANON, [generated[index]!])[0]!;
    if (typeof lean === "string") { problems.push(`${generated[index]!.id}: ${lean}`); continue; }
    const value = lean[key];
    if (!value || value.kind !== kind) { problems.push(`${generated[index]!.id}: ${key} is not of kind ${kind} in the Lean values`); continue; }
    const ts = normalize(tsOf[index]![key]!);
    for (const [what, other] of differingValues(kind, value)) plant(index, what, key, { ...lean, [key]: other }, `${key}: ts=${ts} lean=${normalize(other)}`);
    if (kind === "money" || kind === "unknown") {
      plant(index, `an exhausted step budget (the line is ${kind} in TypeScript)`, key, { ...lean, [key]: { kind: "unknown", reason: BUDGET_EXHAUSTED } },
        `${key}: lean ${BUDGET_EXHAUSTED}`, (found) => found.unfinished === 1);
    }
    if (kind === "money") {
      const { [key]: _removed, ...without } = lean;
      plant(index, "a line missing from the Lean values", key, without, `key sets differ (missing in lean: ${key}; missing in ts: )`, (found) => found.oneSided === 1);
      plant(index, "a line only the Lean evaluator gives", "planted.line", { ...lean, "planted.line": value },
        "key sets differ (missing in lean: ; missing in ts: planted.line)", (found) => found.oneSided === 1);
    }
  }
  const first = generated[0]!;
  const ts = tsOf[0] ??= tsEvaluate(data, rootLines, first.inputs);
  const answer = Object.keys(first.inputs).sort().find((k) => typeof first.inputs[k] === "number" && ts[k]?.kind === "money");
  if (!answer) return { planted, problems: [...problems, `${first.id}: no money answer to change for the Lean evaluator`] };
  const amount = first.inputs[answer] as number;
  const lean = leanEvaluate(CANON, [{ id: first.id, inputs: { ...first.inputs, [answer]: amount + 100 } }])[0]!;
  if (typeof lean === "string") return { planted, problems: [...problems, `${first.id}: ${lean}`] };
  plant(0, "an answer a dollar higher for the Lean evaluator", answer, lean, `${answer}: ts=money:${amount} lean=money:${amount + 100}`);
  return { planted, problems };
}

export function compareEvaluators(): number {
  if (!existsSync(LEAN_BIN)) {
    console.error(`lean binary not found at ${LEAN_BIN}; run: cd lean && lake build`);
    return 2;
  }
  const selfTest = typedChooseAgreement();
  for (const p of selfTest) console.error(`compare self-test (Bool and enum choose): ${p}`);
  console.log(`compare self-test: ${TYPED_CHOOSE_CASES.length} cases of Bool and enum choose, ${selfTest.length} problem(s)`);
  if (selfTest.length) return 1;
  const answers = plantedAnswers();
  for (const p of answers.problems) console.error(`compare self-test (planted answers): ${p}`);
  console.log(`compare self-test: ${answers.planted} answers that are not the cases sent, ${answers.problems.length} problem(s)`);
  if (answers.problems.length) return 1;
  const limit = neverAnswering();
  for (const p of limit) console.error(`compare self-test (time limit): ${p}`);
  console.log(`compare self-test: a process that never answers was stopped at its time limit, ${limit.length} problem(s)`);
  if (limit.length) return 1;
  const data = loadCanonical();
  const rootLines = data.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
  const fixtures = fixtureCases();
  const generated = generatedCases(data);
  const cases = [...fixtures, ...generated];
  const repeated = cases.map((c) => c.id).filter((id, i, ids) => ids.indexOf(id) !== i);
  if (repeated.length) {
    console.error(`compare: case ids are not unique: ${[...new Set(repeated)].join(", ")}`);
    return 1;
  }
  let failures = 0;
  let notRun = 0;
  let oneSided = 0;
  let unfinished = 0;
  const kinds: Record<string, [number, number]> = {};
  const nyKinds: Record<string, [number, number]> = {};
  const failureDetails: string[] = [];

  const { planted, problems } = plantedDifferences(data, rootLines, generated);
  for (const p of problems) console.error(`compare self-test (planted differences): ${p}`);
  console.log(`compare self-test: ${planted} differences planted on generated returns, ${problems.length} problem(s)`);
  if (problems.length) return 1;
  for (let start = 0; start < cases.length; start += BATCH_SIZE) {
    const batch = cases.slice(start, start + BATCH_SIZE);
    const results = leanEvaluate(CANON, batch);
    batch.forEach((c, i) => {
      const column = start + i < fixtures.length ? 0 : 1;
      const leanValues = results[i]!;
      if (typeof leanValues === "string") {
        failures++;
        notRun++;
        failureDetails.push(`${c.id}: ${leanValues}`);
        return;
      }
      const found = compareValues(tsEvaluate(data, rootLines, c.inputs), leanValues);
      oneSided += found.oneSided;
      unfinished += found.unfinished;
      for (const [kind, n] of Object.entries(found.kinds)) (kinds[kind] ??= [0, 0])[column] += n;
      for (const [kind, n] of Object.entries(found.nyKinds)) (nyKinds[kind] ??= [0, 0])[column] += n;
      if (found.problems.length > 0) {
        failures++;
        failureDetails.push(`${c.id}: ${found.problems.slice(0, 4).join("; ")}${found.problems.length > 4 ? ` … +${found.problems.length - 4}` : ""}`);
      }
    });
  }

  const total = (column: 0 | 1, of = kinds) => Object.values(of).reduce((sum, n) => sum + n[column], 0);
  const comparedLines = total(0) + total(1);
  const nyLines = total(0, nyKinds) + total(1, nyKinds);
  const nyUnknown = (nyKinds["unknown"]?.[0] ?? 0) + (nyKinds["unknown"]?.[1] ?? 0);
  const report: string[] = [];
  report.push("# Evaluator agreement — TypeScript engine vs Lean reference");
  report.push("");
  report.push(`Every fixture case and ${generated.length} generated whole returns${NY_MODE ? " with New York answers" : ""} (\`generate.ts\` \`${NY_MODE ? "nyReturnArbitrary" : "sampleReturns"}\`, fast-check, seed ${CORPUS_SEED}: the corpus of the properties check) were evaluated`);
  report.push("by both independently written evaluators; every root form line and every line of every confirmed collection entry");
  report.push("was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).");
  report.push("");
  if (NY_MODE) {
    report.push("This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,");
    report.push("each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York");
    report.push(`documents alike, so the lines of the federal documents are compared here too: of the ${comparedLines} values, ${nyLines} are lines of`);
    report.push(`the New York documents (${nyUnknown} of them unknown) and ${comparedLines - nyLines} are lines of the federal documents. The federal run`);
    report.push(`(\`compare\`, \`reports/${YEAR}/evaluator_agreement.md\`) compares every line on the federal fixture cases and on the same`);
    report.push("generated returns without New York answers.");
  } else {
    report.push("This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York");
    report.push("answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York");
    report.push(`documents are compared here too: ${nyLines} of the ${comparedLines} values, of which ${nyUnknown} are unknown for lack of New York answers`);
    report.push(`and ${nyLines - nyUnknown} have a value (a constant, a figure from federal lines only, or a refusal). The New York run (\`compare --ny\`,`);
    report.push(`\`reports/ny/${YEAR}/evaluator_agreement.md\`) compares the New York lines on cases that give New York answers.`);
  }
  report.push("");
  report.push("| Metric | Value |");
  report.push("| --- | --- |");
  report.push(`| Cases | ${cases.length} |`);
  report.push(`| Fixture cases | ${fixtures.length} |`);
  report.push(`| Generated returns | ${generated.length} |`);
  report.push(`| Line values compared | ${comparedLines} |`);
  report.push(`| Cases with differences | ${failures} |`);
  report.push(`| Result | ${failures === 0 ? "**agreement on every value**" : "**DIFFERENCES FOUND**"} |`);
  report.push("");
  report.push("Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not");
  report.push("given, for example); the two evaluators agree that it is unknown, and its reason is not compared.");
  report.push("");
  report.push("The last two columns count, among them, the lines of the New York documents.");
  report.push("");
  report.push("| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |");
  report.push("| --- | --- | --- | --- | --- |");
  for (const kind of Object.keys(kinds).sort()) report.push(`| ${kind} | ${kinds[kind]![0]} | ${kinds[kind]![1]} | ${nyKinds[kind]?.[0] ?? 0} | ${nyKinds[kind]?.[1] ?? 0} |`);
  report.push(`| all | ${total(0)} | ${total(1)} | ${total(0, nyKinds)} | ${total(1, nyKinds)} |`);
  report.push("");
  report.push("Not compared. Each of these counts as a difference and fails the run.");
  report.push("");
  report.push("| Reason | Count |");
  report.push("| --- | --- |");
  report.push(`| Cases the Lean evaluator gave no values for | ${notRun} |`);
  report.push(`| Line values only one evaluator gave | ${oneSided} |`);
  report.push(`| Line values the Lean evaluator ran out of steps on | ${unfinished} |`);
  if (failures > 0) {
    report.push("");
    report.push("Differences:");
    for (const d of failureDetails.slice(0, 50)) report.push(`- ${d}`);
  }
  report.push("");
  const outDir = reportPath();
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "evaluator_agreement.md"), report.join("\n"));
  console.log(`compare: ${cases.length} cases, ${comparedLines} line values, ${failures} differing case(s)`);
  console.log(`report: ${reportName("evaluator_agreement.md")}`);
  return failures === 0 ? 0 : 1;
}
