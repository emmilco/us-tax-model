// A client of the evaluator: missing reachable inputs determine the questions.
// Authored data supplies wording and ordering; append-only events supply answers.
import { appendFileSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { loadCanonical, CANON_DIR } from "./canonical.js";
import { templateKey } from "./branches.js";
import { evaluate, validateInputs, type Value } from "./eval.js";
import { renderValuesSheetText, resultToJson, valuesSheet } from "./output.js";
import type { CanonicalData, CiteFilled, Inputs } from "./types.js";

export interface InterviewData {
  tax_year: number;
  targets: string[];
  initial: Inputs;
  cite: CiteFilled;
  questions: { input: string; prompt: string; help: string; order: number; cite: CiteFilled; choices?: RosterChoice[] }[];
}
/** A roster question with a fixed set of answers (`$person`: just you, or you and your spouse): each choice's label,
 * its entry keys and each key's label. */
export interface RosterChoice { label: string; value: string[]; labels: Record<string, string> }

/** Wording that tells the user how to type an answer rather than what to answer: the build refuses it in a question's
 * prompt or help, since each client states entry syntax itself. Returns what was found, or null. */
export function entrySyntax(text: string): string | null {
  const patterns: [RegExp, string][] = [
    [/\bcents\b/i, "cents"],
    [/\binteger\b/i, "integer"],
    [/\bwhole number\b/i, "whole number"],
    [/\b(?:true\s*(?:\/|or)\s*false|false\s*(?:\/|or)\s*true)\b/i, "true or false"],
    [/\bJSON\b/i, "JSON"],
    [/\bnull\b/i, "null"],
    [/\[\s*\]|\[\s*["']/, "a list literal"],
    [/\bstable\s+(?:\w+\s+)?keys?\b|\bkeyed\b|\bentry keys?\b/i, "entry keys"],
  ];
  for (const [re, what] of patterns) if (re.test(text)) return what;
  return null;
}
export function loadInterview(profile = "social-security"): InterviewData {
  if (!["social-security", "sales", "stage4", "full", "ny"].includes(profile)) throw new Error("unknown interview profile");
  return JSON.parse(readFileSync(resolve(CANON_DIR, profile === "social-security" ? "interview.json" : `interview-${profile}.json`), "utf8")) as InterviewData;
}
export function questionTemplate(key: string): string {
  if (key.startsWith("$")) return key.split("@")[0]!;
  return templateKey(key);
}
export interface Question { input: string; prompt: string; help: string; order: number; cite: CiteFilled; choices?: RosterChoice[]; helpRequested: boolean; entry: string }
/** A derivation as `resultToJson` writes it. */
export interface JsonDerivation { value: Value; op: string; cite: CiteFilled | null; operands: { ref: string; value: Value }[]; guardsNotTaken: { guard: string; value: Value }[]; notes: string[] }
/** The interview's state, with the values sheet as data (`interviewState` prints it as text). `question` is the next
 * question while the return is incomplete; `pending` is every question still reachable, in asking order, which
 * continues after a refusal because a later answer may clear it. */
export function interviewView(data: CanonicalData, config: InterviewData, inputs: Inputs) {
  const result = evaluate(data, inputs, config.targets);
  const targetValues = config.targets.map(t => result.values.get(t)!);
  const refused = targetValues.find(v => v.kind === "refusal");
  const needed = new Set<string>();
  for (const der of result.derivations.values()) if (der.value.kind === "unknown" && der.value.input) needed.add(der.value.input);
  const pending: Question[] = [...needed].map(key => {
    const q = config.questions.find(q => q.input === questionTemplate(key));
    if (!q) throw new Error(`no question for reachable input ${key}`);
    return { ...q, input: key, helpRequested: inputs[key] === null, entry: entryHint(data, key, q.choices) };
  }).sort((a,b) => a.order - b.order || a.input.localeCompare(b.input));
  const complete = targetValues.every(v => v.kind !== "unknown" && v.kind !== "refusal");
  return { status: refused ? "refused" : complete ? "complete" : "incomplete", refusal: refused ?? null,
    question: refused || complete ? null : pending[0] ?? null,
    pending,
    reachableInputs: [...needed].sort(),
    scope: config.targets.includes("ny_it201.line80") ? "New York Form IT-201 for a full-year New York City resident on the New York standard deduction, computed from the whole federal return, with cited refusals for New York items this tool does not compute. No filing or transmission." : config.targets.includes("f1040.line37") ? "Whole return: Form 1040 lines 1a–37 computed end to end for single, head of household, qualifying surviving spouse and married filing jointly returns, with cited refusals for unsupported items (married filing separately among them). No filing or transmission." : config.targets.includes("scope.ready") ? "Stage 4 form slices with eligibility/valuation screening and allocation inputs; AGI and taxable income are computed for the single-person slice. Not a complete return." : config.targets.includes("f1040.line7a") ? "Stage 3 securities sales, Schedule D, and tax-method selection; AGI and taxable income are computed. Not a complete return." : "Stage 2 Social Security credit and supplied Schedule 3 Part II subtotals; not a complete return. Other forms are not prepared.",
    notices: config.targets.includes("ny_it201.line80") ? "Not tax or legal advice. You are responsible for the return. Published IRS and New York State instructions are not the law itself. Not affiliated with or endorsed by the IRS or the New York State Department of Taxation and Finance." : "Not tax or legal advice. You are responsible for the return. Published IRS instructions are not the law itself. Not affiliated with or endorsed by the IRS.",
    values: JSON.parse(resultToJson(result)).values as Record<string, JsonDerivation>,
    sheet: valuesSheet(data, result, data.forms.map(f=>f.id)) };
}
/** The state the CLI prints: `interviewView` with the values sheet as text. */
export function interviewState(data: CanonicalData, config: InterviewData, inputs: Inputs) {
  const view = interviewView(data, config, inputs);
  return { ...view, sheet: renderValuesSheetText(view.sheet) };
}
/** What an input's answer is: its line's value type (`Roster` for a roster key) and, for an enum, the permitted values. */
export function inputMeta(data: CanonicalData, key: string): { type: string; values?: string[] } {
  if (key.startsWith("$")) return { type: "Roster" };
  const template = questionTemplate(key);
  const line = data.forms.flatMap(d => d.lines).find(l => l.id === template && l.expr.op === "input");
  if (!line) throw new Error(`${key}: not an input`);
  if (line.type.startsWith("Enum(")) return { type: "Enum", values: data.params.enums[line.type.slice(5, -1)]!.values };
  return { type: line.type };
}
/** How to type an answer at the command line (`--value` is JSON), from the input's type. */
export function entryHint(data: CanonicalData, key: string, choices?: RosterChoice[]): string {
  const meta = inputMeta(data, key);
  const help = "; null asks for help";
  switch (meta.type) {
    case "Bool": return `true or false${help}`;
    case "NonNegDollars": return `integer cents, e.g. 620000 for $6,200.00${help}`;
    case "Dollars": return `integer cents, negative for a loss, e.g. -150000 for -$1,500.00${help}`;
    case "Count": return `a whole number, e.g. 2${help}`;
    case "Enum": return `one of: ${meta.values!.map((v) => JSON.stringify(v)).join(", ")}${help}`;
    case "Roster": return choices
      ? `one of: ${choices.map((c) => `${JSON.stringify(c.value)} (${c.label})`).join(", ")}${help}`
      : `a JSON list of distinct entry keys (letters, digits, _ and -), e.g. ["acme_corp"], or [] for none${help}`;
    default: return `a ${meta.type} value${help}`;
  }
}
/** An answer event. `labels`, on a roster answer, maps each entry key to the label the user typed; replay ignores it. */
export interface Event { profile?: string; version?: number; tax_year?: number; input?: string; value?: unknown; labels?: Record<string, string> }
/** Checks an answer against the log's events without writing it: the input must be reachable or already answered (a
 * correction), and the inputs with it must validate and evaluate. Throws when the answer is rejected, so nothing is
 * appended. Returns the event to append, the inputs with it, and the views before and after it. */
export function applyAnswer(data: CanonicalData, config: InterviewData, events: Event[], input: string, value: unknown, labels?: unknown) {
  const current = replay(config, events);
  const before = interviewView(data, config, current);
  if (!before.reachableInputs.includes(input) && !(input in current)) throw new Error("answer is neither reachable nor a correction");
  if (labels !== undefined) {
    const keys = Array.isArray(value) ? value : null;
    const ok = input.startsWith("$") && keys !== null && labels !== null && typeof labels === "object" && !Array.isArray(labels)
      && Object.keys(labels).length === keys.length && keys.every((k) => typeof k === "string" && typeof (labels as Record<string, unknown>)[k] === "string"
        && ((labels as Record<string, string>)[k]!.trim() !== "") && (labels as Record<string, string>)[k]!.length <= 200);
    if (!ok) throw new Error(`${input}: labels must give each listed entry a label of 1 to 200 characters`);
  }
  const event: Event & { input: string } = labels === undefined ? { input, value } : { input, value, labels: labels as Record<string, string> };
  const candidate = replay(config, [...events, event]);
  validateInputs(data, candidate);
  const after = interviewView(data, config, candidate);
  return { event, inputs: candidate, before, after };
}
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
    const { event } = applyAnswer(data, config, events, input, JSON.parse(raw) as unknown);
    appendFileSync(path, JSON.stringify(event) + "\n");
    events.push(event);
  }
  console.log(JSON.stringify(interviewState(data, config, replay(config, events)), null, 2));
}
