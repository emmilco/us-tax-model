// A client of the evaluator: missing reachable inputs determine the questions.
// Authored data supplies wording and ordering; append-only events supply answers.
import { appendFileSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { loadCanonical, CANON_DIR } from "./canonical.js";
import { evaluate, validateInputs } from "./eval.js";
import { renderValuesSheet, resultToJson } from "./output.js";
import type { CanonicalData, CiteFilled, Inputs } from "./types.js";

export interface InterviewData {
  tax_year: number;
  targets: string[];
  initial: Inputs;
  cite: CiteFilled;
  questions: { input: string; prompt: string; help: string; order: number; cite: CiteFilled }[];
}
export function loadInterview(profile = "social-security"): InterviewData {
  if (!["social-security", "sales"].includes(profile)) throw new Error("unknown interview profile");
  return JSON.parse(readFileSync(resolve(CANON_DIR, profile === "sales" ? "interview-sales.json" : "interview.json"), "utf8")) as InterviewData;
}
export function questionTemplate(key: string): string {
  if (key.startsWith("$")) return key.split("@")[0]!;
  return key.replace(/(?:[a-zA-Z0-9_]+\[[a-zA-Z0-9_-]+\]\.)*/g, m => m ? m.split(".").filter(Boolean).at(-1)!.split("[")[0] + "." : "");
}
export function interviewState(data: CanonicalData, config: InterviewData, inputs: Inputs) {
  const result = evaluate(data, inputs, config.targets);
  const targetValues = config.targets.map(t => result.values.get(t)!);
  const refused = targetValues.find(v => v.kind === "refusal");
  const needed = new Set<string>();
  for (const der of result.derivations.values()) if (der.value.kind === "unknown" && der.value.input) needed.add(der.value.input);
  const pending = [...needed].map(key => {
    const q = config.questions.find(q => q.input === questionTemplate(key));
    if (!q) throw new Error(`no question for reachable input ${key}`);
    return { ...q, input: key, helpRequested: inputs[key] === null };
  }).sort((a,b) => a.order - b.order || a.input.localeCompare(b.input));
  const complete = targetValues.every(v => v.kind !== "unknown" && v.kind !== "refusal");
  return { status: refused ? "refused" : complete ? "complete" : "incomplete", refusal: refused ?? null,
    question: refused || complete ? null : pending[0] ?? null,
    reachableInputs: [...needed].sort(),
    scope: config.targets.includes("f1040.line7a") ? "Stage 3 securities sales, Schedule D, and tax-method selection using supplied taxable income, dividends and feeder subtotals; not a complete return." : "Stage 2 Social Security credit and supplied Schedule 3 Part II subtotals; not a complete return. Other forms are not prepared.",
    notices: "Not tax or legal advice. You are responsible for the return. Published IRS instructions are not the law itself. Not affiliated with or endorsed by the IRS.",
    values: JSON.parse(resultToJson(result)).values as unknown,
    sheet: renderValuesSheet(data, result, data.forms.map(f=>f.id)) };
}
interface Event { profile?: string; version?: number; tax_year?: number; input?: string; value?: unknown }
export function replay(config: InterviewData, events: Event[]): Inputs {
  if (events[0]?.version !== 1 || events[0]?.tax_year !== config.tax_year) throw new Error("invalid interview log header");
  const inputs: Inputs = structuredClone(config.initial);
  for (const event of events.slice(1)) {
    if (typeof event.input !== "string" || !("value" in event) || event.input in config.initial) throw new Error("invalid answer event");
    inputs[event.input] = event.value;
  }
  // Removing a roster entry makes its old answers inactive, while retaining them in the log.
  for (const key of Object.keys(inputs)) {
    const prefixes = [...key.matchAll(/([a-zA-Z0-9_]+)\[([a-zA-Z0-9_-]+)\]/g)];
    for (const match of prefixes) {
      const parent = key.slice(key.startsWith("$") ? key.indexOf("@") + 1 : 0, match.index).replace(/\.$/, "");
      const rk = `$${match[1]}${parent ? "@" + parent : ""}`;
      if (!Array.isArray(inputs[rk]) || !(inputs[rk] as string[]).includes(match[2]!)) { delete inputs[key]; break; }
    }
  }
  return inputs;
}
export function runInterview(args: string[]): void {
  const action = args[0];
  const arg = (name: string) => { const i = args.indexOf(name); return i < 0 ? undefined : args[i+1]; };
  const path = arg("--log");
  if (!path) throw new Error("interview requires --log <file.jsonl>");
  const existing = action === "start" ? undefined : JSON.parse(readFileSync(path,"utf8").split("\n")[0]! ) as Event;
  const profile = arg("--profile") ?? existing?.profile ?? "social-security";
  if (existing && profile !== (existing.profile ?? "social-security")) throw new Error("interview profile does not match log");
  const config = loadInterview(profile);
  const data = loadCanonical();
  if (action === "start") writeFileSync(path, JSON.stringify({version:1,tax_year:config.tax_year,profile}) + "\n", {flag:"wx", mode:0o600});
  else if (action !== "advance" && action !== "answer") throw new Error("interview start | advance | answer");
  const events = readFileSync(path,"utf8").trim().split("\n").map(l => JSON.parse(l) as Event);
  if (action === "answer") {
    const input = arg("--input"); const raw = arg("--value");
    if (!input || raw === undefined) throw new Error("answer requires --input <key> --value <JSON>");
    const current = replay(config, events);
    const state = interviewState(data, config, current);
    if (!state.reachableInputs.includes(input) && !(input in current)) throw new Error("answer is neither reachable nor a correction");
    const event = {input, value: JSON.parse(raw) as unknown};
    const candidate = replay(config, [...events, event]);
    validateInputs(data, candidate);
    interviewState(data, config, candidate); // validate before append
    appendFileSync(path, JSON.stringify(event) + "\n");
    events.push(event);
  }
  console.log(JSON.stringify(interviewState(data, config, replay(config, events)), null, 2));
}
