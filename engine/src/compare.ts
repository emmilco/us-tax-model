// Two-evaluator agreement: run every fixture case and a deterministic corpus of generated whole returns through the
// TypeScript evaluator and the Lean reference evaluator, and fail on any difference (spec section 6.3 / design 2.6).

import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import fc from "fast-check";
import { loadCanonical } from "./canonical.js";
import { allTargets, evaluate } from "./eval.js";
import { isNyDoc } from "./fixture-inputs.js";
import { loadCases } from "./fixtures.js";
import { nyReturnArbitrary, sampleReturns } from "./generate.js";
import type { CanonicalData, Inputs } from "./types.js";
import type { Value } from "./eval.js";
import { NY_MODE, yearPath } from "./year.js";
import { reportName, reportPath } from "./year.js";
import { TYPED_CHOOSE_CASES, typedChooseData, valueText } from "./check-selftest.js";

const ROOT = resolve(import.meta.dirname, "../..");
const LEAN_BIN = join(ROOT, "lean", ".lake", "build", "bin", "taxeval");
const CANON = yearPath("canonical");

// The generated corpus comes from the general generator (generate.ts), which draws every declared input, so the
// corpus follows the model. Its seed and size are those of the properties check: the branch coverage the properties
// report lists is then the coverage of the returns compared here. At this size the number of inputs the corpus
// varies has levelled off (doubling it adds about one input in a hundred).
const SEED = 7;
const GENERATED = 400;

// The reason of the Lean evaluator's unknown for a line it ran out of steps on (Eval.lean, budgetExhausted).
const BUDGET_EXHAUSTED = "step budget exhausted";

interface Case {
  id: string;
  inputs: Inputs;
}

type LeanValues = Record<string, Record<string, unknown>>;

function fixtureCases(): Case[] {
  const file = loadCases();
  return file.cases.map((c) => ({ id: c.id, inputs: c.inputs }));
}

/** The generated whole returns: federal returns (the inputs of the federal documents only) or, with --ny, federal
 * returns that also carry the answers of the New York documents. */
function generatedCases(all: CanonicalData): Case[] {
  const federal = { ...all, forms: all.forms.filter((d) => !isNyDoc(d)), defs: all.defs.filter((d) => !isNyDoc(d)) };
  const corpus = NY_MODE ? fc.sample(nyReturnArbitrary(all), { seed: SEED, numRuns: GENERATED }) : sampleReturns(federal, GENERATED, SEED);
  return corpus.map((inputs, i) => ({ id: `generated.${String(i).padStart(3, "0")}`, inputs }));
}

function normalize(v: Value | Record<string, unknown>): string {
  const val = v as { kind?: string; cents?: number; value?: unknown };
  if (val.kind === "refusal") { const r = v as Record<string, unknown>; return `refusal:${r.gate}:${r.form}:${r.remedy}:${JSON.stringify(Object.entries(r.cite as Record<string, unknown>).sort())}`; }
  if (val.kind === "unknown") return "unknown";
  if (val.kind === "money") return `money:${val.cents}`;
  if (val.kind === "rate") { const r = v as { num?: number; den?: number }; return `rate:${r.num}/${r.den}`; }
  return `${val.kind}:${JSON.stringify(val.value)}`;
}

/** The Lean evaluator's values for one set of inputs, or the reason it gave none. */
function leanEvaluate(dir: string, name: string, inputs: Inputs): LeanValues | string {
  const inputsPath = join(dir, `${name}.inputs.json`);
  const outPath = join(dir, `${name}.lean.json`);
  writeFileSync(inputsPath, JSON.stringify(inputs));
  const proc = spawnSync(LEAN_BIN, ["--canonical", CANON, "--inputs", inputsPath, "--out", outPath], { encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
  if (proc.status !== 0) return `lean evaluator exited ${proc.status}: ${proc.stderr.slice(0, 200)}`;
  return JSON.parse(readFileSync(outPath, "utf-8")) as LeanValues;
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
 * finished it; `kinds` counts the compared lines by the kind of the TypeScript value. A line only one evaluator
 * gives (`oneSided`) and a line the Lean evaluator ran out of steps on (`unfinished`) are not compared, and each
 * is a problem. */
interface Comparison { problems: string[]; kinds: Record<string, number>; oneSided: number; unfinished: number }

function compareValues(tsValues: Record<string, Value>, leanValues: LeanValues): Comparison {
  const result: Comparison = { problems: [], kinds: {}, oneSided: 0, unfinished: 0 };
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
    TYPED_CHOOSE_CASES.forEach(({ inputs, expect }, i) => {
      const inputsPath = join(dir, `case${i}.inputs.json`);
      const outPath = join(dir, `case${i}.lean.json`);
      writeFileSync(inputsPath, JSON.stringify(inputs));
      const proc = spawnSync(LEAN_BIN, ["--canonical", dir, "--inputs", inputsPath, "--out", outPath], { encoding: "utf-8" });
      if (proc.status !== 0) { problems.push(`case ${i}: lean evaluator exited ${proc.status}: ${proc.stderr.slice(0, 200)}`); return; }
      const lean = JSON.parse(readFileSync(outPath, "utf-8")) as Record<string, Record<string, unknown>>;
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
function plantedDifferences(data: CanonicalData, rootLines: string[], generated: Case[], dir: string): { planted: number; problems: string[] } {
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
  const leanOf: Record<number, LeanValues | string> = {};
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
    const lean = leanOf[index] ??= leanEvaluate(dir, `planted.${index}`, generated[index]!.inputs);
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
  const lean = leanEvaluate(dir, "planted.answer", { ...first.inputs, [answer]: amount + 100 });
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
  const data = loadCanonical();
  const rootLines = data.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
  const fixtures = fixtureCases();
  const generated = generatedCases(data);
  const cases = [...fixtures, ...generated];
  const tmp = mkdtempSync(join(tmpdir(), "compare-"));
  let failures = 0;
  let notRun = 0;
  let oneSided = 0;
  let unfinished = 0;
  const kinds: Record<string, [number, number]> = {};
  const failureDetails: string[] = [];

  try {
    const { planted, problems } = plantedDifferences(data, rootLines, generated, tmp);
    for (const p of problems) console.error(`compare self-test (planted differences): ${p}`);
    console.log(`compare self-test: ${planted} differences planted on generated returns, ${problems.length} problem(s)`);
    if (problems.length) return 1;
    cases.forEach((c, index) => {
      const leanValues = leanEvaluate(tmp, c.id, c.inputs);
      if (typeof leanValues === "string") {
        failures++;
        notRun++;
        failureDetails.push(`${c.id}: ${leanValues}`);
        return;
      }
      const found = compareValues(tsEvaluate(data, rootLines, c.inputs), leanValues);
      oneSided += found.oneSided;
      unfinished += found.unfinished;
      for (const [kind, n] of Object.entries(found.kinds)) (kinds[kind] ??= [0, 0])[index < fixtures.length ? 0 : 1] += n;
      if (found.problems.length > 0) {
        failures++;
        failureDetails.push(`${c.id}: ${found.problems.slice(0, 4).join("; ")}${found.problems.length > 4 ? ` … +${found.problems.length - 4}` : ""}`);
      }
    });
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }

  const total = (column: 0 | 1) => Object.values(kinds).reduce((sum, n) => sum + n[column], 0);
  const comparedLines = total(0) + total(1);
  const report: string[] = [];
  report.push("# Evaluator agreement — TypeScript engine vs Lean reference");
  report.push("");
  report.push(`Every fixture case and ${GENERATED} generated whole returns${NY_MODE ? " with New York answers" : ""} (\`generate.ts\` \`${NY_MODE ? "nyReturnArbitrary" : "sampleReturns"}\`, fast-check, seed ${SEED}) were evaluated`);
  report.push("by both independently written evaluators; every root form line and every line of every confirmed collection entry");
  report.push("was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).");
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
  report.push("| Kind | Fixture cases | Generated returns |");
  report.push("| --- | --- | --- |");
  for (const kind of Object.keys(kinds).sort()) report.push(`| ${kind} | ${kinds[kind]![0]} | ${kinds[kind]![1]} |`);
  report.push(`| all | ${total(0)} | ${total(1)} |`);
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
