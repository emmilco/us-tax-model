// A client of the evaluator: missing reachable inputs determine the questions.
// Authored data supplies wording and ordering; append-only events supply answers.
import { appendFileSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { loadCanonical, CANON_DIR } from "./canonical.js";
import { templateKey } from "./branches.js";
import { evaluate, inputsAhead, validateInputs, type Value } from "./eval.js";
import { renderValuesSheetText, resultToJson, valuesSheet } from "./output.js";
import { jointReturn, shownFor, shownLabel, shownSheet } from "./spouse-wording.js";
import type { CanonicalData, CiteFilled, Inputs } from "./types.js";

export interface InterviewData {
  tax_year: number;
  targets: string[];
  initial: Inputs;
  cite: CiteFilled;
  questions: { input: string; prompt: string; help: string; order: number; seq?: number; at?: number[]; cite: CiteFilled; choices?: RosterChoice[]; value_labels?: Record<string, string>; value_order?: string[];
    /** The tick-box group the question is a member of, and the words shown beside its box (`TickGroup`). */
    group?: string; tick?: string }[];
  /** The tick-box groups the profile's questions name. */
  groups?: TickGroup[];
  /** What the interview adds to a refusal, by gate line: what the filer can do next (interview/<year>/refusal_notes.yaml). */
  refusal_notes?: Record<string, string>;
}
/** A tick-box group: a few yes or no questions of one topic, side by side, that a client may show on one screen, under the heading,
 * one box per open member with the member's `tick` label. Presentation only: each member stays its own input, with
 * its own answer in the log. `heading` is stored as a prompt is (its collection's frame first). */
export interface TickGroup { id: string; heading: string }
/** A roster question with a fixed set of answers (`$person`: just you, or you and your husband or wife): each
 * choice's label, its entry keys, each key's label and the answers the choice records. */
export interface RosterChoice { label: string; value: string[]; labels: Record<string, string>; records?: ChoiceRecord[] }
/** An answer a roster choice records with the roster: the input, its value, and the sentence that tells the filer what
 * was recorded. The choice's label states the fact, so the filer is not asked it again. */
export interface ChoiceRecord { input: string; value: unknown; shown: string }

/** The inputs a roster choice may record that are not inputs of the entries it creates: each one input, recorded with
 * one value by one choice (named by its entry keys) of one roster question. Everything else the interview does not
 * set. */
export const RECORD_ALLOWED: readonly { input: string; roster: string; choice: readonly string[]; value: unknown }[] = [
  { input: "f1040.status", roster: "$person", choice: ["taxpayer", "spouse"], value: "mfj" },
];

const sameKeys = (a: readonly unknown[], b: readonly unknown[]) => a.length === b.length && JSON.stringify([...a].map(String).sort()) === JSON.stringify([...b].map(String).sort());

/** The problems of a question's recorded answers (`where` names the question). A choice may record only an input of
 * an entry it creates (`person[spouse].role` for a choice that lists `spouse`) or an input on RECORD_ALLOWED, each
 * once, with a value the input can take and a sentence to show; a gated input is never recorded. An entry input one
 * choice records is recorded by every choice for every entry, so that input is never asked. `lines`: the input lines
 * by id; `collections`: the ids of the top-level collections; `enums`: each enum's values. */
export function recordProblems(q: { input: string; choices?: RosterChoice[] }, lines: ReadonlyMap<string, { type: string; gated_by?: string }>,
  collections: ReadonlySet<string>, enums: Record<string, { values: string[] }>, where = `question ${q.input}`): string[] {
  const problems: string[] = [];
  const choices = Array.isArray(q.choices) ? q.choices : [];
  if (!choices.some((c) => c.records !== undefined)) return problems;
  const coll = q.input.startsWith("$") && !q.input.includes("@") ? q.input.slice(1) : null;
  if (coll === null || !collections.has(coll)) return [`${where}: only a choice of a top-level roster question records answers`];
  const entryTemplates = new Set<string>();
  for (const c of choices) {
    const name = `${where}: choice ${JSON.stringify(c.value)}`;
    if (c.records === undefined) continue;
    if (!Array.isArray(c.records) || c.records.some((r) => !r || typeof r !== "object" || typeof r.input !== "string" || !("value" in r))) { problems.push(`${name}: records must be a list of {input, value, shown}`); continue; }
    const seen = new Set<string>();
    for (const r of c.records) {
      if (seen.has(r.input)) problems.push(`${name}: records ${r.input} twice`);
      seen.add(r.input);
      if (typeof r.shown !== "string" || r.shown.trim() === "" || r.shown.includes("\n")) problems.push(`${name}: the record of ${r.input} needs one line saying what is recorded (shown)`);
      const allowed = RECORD_ALLOWED.find((a) => a.input === r.input);
      const entry = r.input.startsWith(`${coll}[`) ? /^\[([a-zA-Z0-9_-]+)\]\.([a-z0-9_]+)$/.exec(r.input.slice(coll.length)) : null;
      let template: string;
      if (allowed) {
        template = r.input;
        if (allowed.roster !== q.input || !sameKeys(allowed.choice, c.value) || JSON.stringify(allowed.value) !== JSON.stringify(r.value)) {
          problems.push(`${name}: records ${r.input} = ${JSON.stringify(r.value)}; the allow-list permits it only as ${JSON.stringify(allowed.value)}, recorded by the choice ${JSON.stringify(allowed.choice)} of ${allowed.roster}`);
          continue;
        }
      } else if (entry) {
        template = `${coll}.${entry[2]}`;
        if (!c.value.includes(entry[1]!)) { problems.push(`${name}: records ${r.input}, an input of an entry this choice does not create`); continue; }
        entryTemplates.add(template);
      } else {
        problems.push(`${name}: records ${r.input}, which is neither an input of an entry this choice creates nor on the allow-list; the interview sets no other input`);
        continue;
      }
      const line = lines.get(template);
      if (!line) { problems.push(`${name}: records ${r.input}, which is not an input`); continue; }
      if (line.gated_by) problems.push(`${name}: records ${r.input}, a gated input`);
      const enumName = /^Enum\(([a-z_]+)\)$/.exec(line.type)?.[1];
      const ok = line.type === "Bool" ? typeof r.value === "boolean"
        : enumName ? typeof r.value === "string" && (enums[enumName]?.values ?? []).includes(r.value)
        : typeof r.value === "number" && Number.isSafeInteger(r.value) && (line.type === "Dollars" || r.value >= 0);
      if (!ok) problems.push(`${name}: records ${r.input} = ${JSON.stringify(r.value)}, a value this ${line.type} input cannot take`);
    }
  }
  for (const t of entryTemplates) for (const c of choices) for (const k of c.value) {
    const key = `${coll}[${k}].${t.slice(coll.length + 1)}`;
    if (!(c.records ?? []).some((r) => r.input === key)) problems.push(`${where}: choice ${JSON.stringify(c.value)} does not record ${key}; an entry input one choice records is recorded by every choice for every entry`);
  }
  return problems;
}

/** `recordProblems` over built data: the input lines, top-level collections and enums come from `data`. */
export function recordProblemsIn(data: CanonicalData, q: { input: string; choices?: RosterChoice[] }, where?: string): string[] {
  const lines = new Map(data.forms.flatMap((d) => d.lines.filter((l) => l.expr.op === "input").map((l) => [l.id, l] as const)));
  const collections = new Set(data.forms.filter((d) => d.collection && !d.collection.parent).map((d) => d.id));
  return recordProblems(q, lines, collections, data.params.enums, where);
}

/** The entry inputs a profile's roster choices record (`person.role`), each with its roster question: these are never
 * asked. */
export function recordedTemplates(config: InterviewData): Map<string, string> {
  let index = recordedIndex.get(config);
  if (!index) {
    index = new Map();
    for (const q of config.questions) for (const c of q.choices ?? []) for (const r of c.records ?? []) {
      const t = templateKey(r.input);
      if (t !== r.input) index.set(t, q.input);
    }
    recordedIndex.set(config, index);
  }
  return index;
}
const recordedIndex = new WeakMap<InterviewData, Map<string, string>>();

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
/** The entries a question's key lies in, outermost first (`person[taxpayer]`, `w2[acme]` for a line of that W-2;
 * `person[taxpayer]` for the roster `$w2@person[taxpayer]`). */
export function entriesOf(key: string): string[] {
  const path = key.startsWith("$") ? key.slice(key.indexOf("@") + 1 || key.length) : key.slice(0, Math.max(0, key.lastIndexOf(".")));
  return path.match(/[a-zA-Z0-9_]+\[[a-zA-Z0-9_-]+\]/g) ?? [];
}
/** What `askOrder` reads of a question: its key, its topic's position (`order`), its place in the topic (`seq`) and,
 * for a question of a collection entry, the place of each run of entry questions it belongs to (`at`, from the build). */
export interface Place { input: string; order: number; seq?: number; at?: number[] }
/** A bank question's place under the key it is asked by. */
export function placeOf(q: { order: number; seq?: number; at?: number[] }, key: string): Place {
  return { input: key, order: q.order, ...(q.seq !== undefined ? { seq: q.seq } : {}), ...(q.at ? { at: q.at } : {}) };
}
/** The asking order of two open questions. First the topic: the lower `order` number. Within one order number the
 * questions that state a place (`seq`) come first, in the order the bank states, read as an outline: at each level
 * (the return, then an entry of a collection, then an entry of a collection inside it) the lower number comes first,
 * where a question of that level counts by its `seq` and a run of entry questions by the lowest `seq` in it (`at`);
 * within a run, one entry's questions are asked through before the next entry's (entries by key). So one W-2's
 * questions are asked through before the next W-2's, and one person's before the other's. A question that states no
 * `seq` comes after those of its order number that do, by key. */
export function askOrder(a: Place, b: Place): number {
  if (a.order !== b.order) return a.order - b.order;
  if (a.seq === undefined || b.seq === undefined) return a.seq !== undefined ? -1 : b.seq !== undefined ? 1 : a.input.localeCompare(b.input);
  const ea = entriesOf(a.input);
  const eb = entriesOf(b.input);
  for (let i = 0; ; i++) {
    const inA = i < ea.length;
    const inB = i < eb.length;
    const na = inA ? a.at?.[i] ?? a.seq : a.seq;
    const nb = inB ? b.at?.[i] ?? b.seq : b.seq;
    if (na !== nb) return na - nb;
    if (!inA || !inB) return inA !== inB ? (inA ? 1 : -1) : a.input.localeCompare(b.input);
    const c = ea[i]!.localeCompare(eb[i]!);
    if (c) return c;
  }
}
/** The `at` of every question that states a `seq` and lies in a collection: for each order number, the questions in
 * `seq` order are cut, level by level, into runs of consecutive questions of one collection, and a question's `at`
 * holds, outermost first, the lowest `seq` of the run it is in at each level. `chainOf` gives the collections a
 * question's entry lies in, outermost first (none for a question of the return). */
export function blockPlaces(questions: { input: string; order: number; seq?: number }[], chainOf: (input: string) => string[]): Map<string, number[]> {
  const out = new Map<string, number[]>();
  type Item = { input: string; seq: number; chain: string[] };
  const assign = (items: Item[], depth: number): void => {
    let run: Item[] = [];
    const close = () => {
      if (!run.length) return;
      for (const it of run) (out.get(it.input) ?? out.set(it.input, []).get(it.input)!)[depth] = run[0]!.seq;
      assign(run, depth + 1);
      run = [];
    };
    for (const it of items) {
      if (it.chain.length <= depth) { close(); continue; }
      if (run.length && run[0]!.chain[depth] !== it.chain[depth]) close();
      run.push(it);
    }
    close();
  };
  for (const order of new Set(questions.map((q) => q.order))) {
    const items = questions.filter((q) => q.order === order && q.seq !== undefined)
      .map((q) => ({ input: q.input, seq: q.seq!, chain: chainOf(q.input) })).sort((x, y) => x.seq - y.seq || x.input.localeCompare(y.input));
    assign(items, 0);
  }
  return out;
}
export function questionTemplate(key: string): string {
  if (key.startsWith("$")) return key.split("@")[0]!;
  return templateKey(key);
}
/** Per-(data, config) indexes: a question by its input template, an input line by its template. The first match wins. */
const questionIndex = new WeakMap<InterviewData, Map<string, InterviewData["questions"][number]>>();
const inputLineIndex = new WeakMap<CanonicalData, Map<string, CanonicalData["forms"][number]["lines"][number]>>();
function questionFor(config: InterviewData, template: string) {
  let index = questionIndex.get(config);
  if (!index) {
    index = new Map();
    for (const q of config.questions) if (!index.has(q.input)) index.set(q.input, q);
    questionIndex.set(config, index);
  }
  return index.get(template);
}
function inputLine(data: CanonicalData, template: string) {
  let index = inputLineIndex.get(data);
  if (!index) {
    index = new Map();
    for (const d of data.forms) for (const l of d.lines) if (l.expr.op === "input" && !index.has(l.id)) index.set(l.id, l);
    inputLineIndex.set(data, index);
  }
  return index.get(template);
}
/** The question that asks for a reachable input: its own, or, for an entry input the roster's choices record
 * (`person[taxpayer].role`, unknown only on a return whose roster answer recorded nothing), the roster question
 * again, whose answer records it. */
function askFor(config: InterviewData, key: string): { key: string; q: InterviewData["questions"][number] } {
  const template = questionTemplate(key);
  const roster = recordedTemplates(config).get(template);
  const asked = roster ?? template;
  const q = questionFor(config, asked);
  if (!q) throw new Error(`no question for reachable input ${key}`);
  return { key: roster ?? key, q };
}

/** The values of a question that are not offered: a value that a choice of an answered roster question records, when the
 * filer answered that question with another choice that does not record it. Married filing jointly is what the
 * couple's choice of the person roster records, so a filer who answered "Just me" is not offered it: to give it, they
 * change that answer. Presentation only: the value given now is always offered, and an answer is accepted whether or
 * not it was offered. */
export function withheldValues(config: InterviewData, inputs: Inputs, key: string): string[] {
  const withheld: string[] = [];
  for (const q of config.questions) {
    const answer = inputs[q.input];
    if (!q.choices || !Array.isArray(answer)) continue;
    const chosen = q.choices.find((c) => sameKeys(c.value, answer as unknown[]));
    if (!chosen) continue;
    const own = new Set((chosen.records ?? []).filter((r) => r.input === key).map((r) => r.value));
    for (const c of q.choices) for (const r of c.records ?? []) {
      if (c !== chosen && r.input === key && typeof r.value === "string" && !own.has(r.value) && r.value !== inputs[key] && !withheld.includes(r.value)) withheld.push(r.value);
    }
  }
  return withheld;
}

export interface Question { input: string; prompt: string; help: string; order: number; seq?: number; at?: number[]; cite: CiteFilled; choices?: RosterChoice[]; value_labels?: Record<string, string>; value_order?: string[];
  /** The tick-box group the question is a member of, and its label as shown. */
  group?: string; tick?: string;
  /** The per-person frame as shown ("About you", "About your spouse"), when the question is asked of a person on a return with two. */
  frame?: string;
  /** The enum values not offered (`withheldValues`). */
  withheld?: string[];
  helpRequested: boolean; entry: string }
/** The entry a question's key is asked of (`person[spouse].f8889[hsa]` for `person[spouse].f8889[hsa].line2`), or ""
 * for a question asked once per return. */
export function entryPath(key: string): string {
  return /^(.*\])\.[^.\[\]]+$/.exec(key)?.[1] ?? "";
}
/** The tick-box screen a client shows in place of the next question: the group's heading as shown and its members to
 * show, as questions, in asking order. */
export interface ShownGroup { id: string; heading: string; frame?: string; members: Question[] }
/** The tick-box screen for the first pending question, or null when that question is in no group or the screen would
 * have one box (the question is then asked as an ordinary question). The members shown are those of the next
 * question's group, asked of the same entry, that are open or would be once the open ones are answered No: a member
 * the engine reaches only after another member's No (two lines of one chain of tests) belongs on the same screen,
 * since on the typical answer, none of these, it is asked next in any case. An answered member is not shown, nor one
 * that waits on an answer outside the group. `shown` words a question for its key. */
function tickScreen(data: CanonicalData, config: InterviewData, inputs: Inputs, pending: Question[], shown: (key: string) => Question): ShownGroup | null {
  const first = pending[0];
  const group = first?.group === undefined ? undefined : config.groups?.find((g) => g.id === first.group);
  if (!first || !group) return null;
  // The key of another member for the same entry: the members of a group asked per entry are inputs of one form.
  const path = entryPath(first.input);
  const template = questionTemplate(first.input);
  const form = path === "" ? "" : template.slice(0, template.length - (first.input.length - path.length - 1));
  const keyOf = (member: string): string | null => (path === "" ? member : member.startsWith(form) ? `${path}.${member.slice(form.length)}` : null);
  const keys = config.questions.filter((q) => q.group === group.id).sort(askOrder).flatMap((q) => keyOf(q.input) ?? []);
  const open = new Set(pending.filter((q) => q.group === group.id && entryPath(q.input) === path).map((q) => q.input));
  const waiting = (k: string) => !open.has(k) && (!(k in inputs) || inputs[k] === null);
  for (let round = 0; round < keys.length && keys.some(waiting); round++) {
    const probe: Inputs = { ...inputs };
    for (const k of open) probe[k] = false;
    // What the interview would ask then: the reach pass included, as for the pending questions themselves.
    const result = evaluate(data, probe, config.targets);
    const needed = neededInputs(data, config, probe, result, config.targets.map((t) => result.values.get(t)!));
    const more = keys.filter((k) => waiting(k) && needed.has(k));
    if (!more.length) break;
    for (const k of more) open.add(k);
  }
  const members = keys.filter((k) => open.has(k)).map((k) => pending.find((q) => q.input === k) ?? shown(k));
  if (members.length < 2) return null;
  const heading = shownFor({ prompt: group.heading, help: "" }, first.input, inputs);
  return { id: group.id, heading: heading.prompt, ...(heading.frame ? { frame: heading.frame } : {}), members };
}
/** A derivation as `resultToJson` writes it. */
export interface JsonDerivation { value: Value; op: string; cite: CiteFilled | null; operands: { ref: string; value: Value }[]; guardsNotTaken: { guard: string; value: Value }[]; notes: string[] }
/** The interview's state, with the values sheet as data (`interviewState` prints it as text). `question` is the next
 * question while the return is incomplete; `pending` is every question still reachable, in asking order, which
 * continues after a refusal because a later answer may clear it; `group` is the tick-box screen the first pending
 * question may be shown in (`tickScreen`), for a client that shows one. Each question's prompt and help, and each sheet
 * line's label, are as shown to the filer: the spouse phrase reworded from these inputs' filing status
 * (spouse-wording.ts). */
export function interviewView(data: CanonicalData, config: InterviewData, inputs: Inputs) {
  const result = evaluate(data, inputs, config.targets);
  const targetValues = config.targets.map(t => result.values.get(t)!);
  const refused = targetValues.find(v => v.kind === "refusal");
  const needed = neededInputs(data, config, inputs, result, targetValues);
  const joint = jointReturn(inputs);
  const shown = (key: string): Question => {
    const q = askFor(config, key).q;
    const withheld = withheldValues(config, inputs, key);
    return { ...shownFor(q, key, inputs), input: key, ...(q.tick !== undefined ? { tick: shownLabel(q.tick, q.prompt, key, inputs) } : {}), ...(withheld.length ? { withheld } : {}), helpRequested: inputs[key] === null, entry: entryHint(data, key, q.choices, q.value_labels, q.value_order, withheld) };
  };
  const pending: Question[] = [...new Set([...needed].map((k) => askFor(config, k).key))].map(shown).sort(askOrder);
  const complete = targetValues.every(v => v.kind !== "unknown" && v.kind !== "refusal");
  return { status: refused ? "refused" : complete ? "complete" : "incomplete", refusal: refused ?? null,
    refusalNote: refused?.kind === "refusal" ? config.refusal_notes?.[templateKey(refused.gate)] ?? null : null,
    question: refused || complete ? null : pending[0] ?? null,
    pending,
    group: tickScreen(data, config, inputs, pending, shown),
    reachableInputs: [...needed].sort(),
    scope: config.targets.includes("ny_it201.line80") ? "New York Form IT-201 for a full-year New York City resident on the New York standard deduction, computed from the whole federal return, with cited refusals for New York items this tool does not compute. No filing or transmission." : config.targets.includes("f1040.line37") ? "Whole return: Form 1040 lines 1a–37 computed end to end for single, head of household, qualifying surviving spouse and married filing jointly returns, with cited refusals for unsupported items (married filing separately among them). No filing or transmission." : config.targets.includes("scope.ready") ? "Stage 4 form slices with eligibility/valuation screening and allocation inputs; AGI and taxable income are computed for the single-person slice. Not a complete return." : config.targets.includes("f1040.line7a") ? "Stage 3 securities sales, Schedule D, and tax-method selection; AGI and taxable income are computed. Not a complete return." : "Stage 2 Social Security credit, with the other Schedule 3 Part II amounts refused where they apply; not a complete return. Other forms are not prepared.",
    notices: config.targets.includes("ny_it201.line80") ? "Not tax or legal advice. You are responsible for the return. Published IRS and New York State instructions are not the law itself. Not affiliated with or endorsed by the IRS or the New York State Department of Taxation and Finance." : "Not tax or legal advice. You are responsible for the return. Published IRS instructions are not the law itself. Not affiliated with or endorsed by the IRS.",
    values: JSON.parse(resultToJson(result)).values as Record<string, JsonDerivation>,
    sheet: shownSheet(valuesSheet(data, result, data.forms.map(f=>f.id)), joint) };
}
/** The inputs a return needs and lacks: each unknown input a line of the evaluation reads; and, while the return is
 * incomplete, those the reach pass finds (`inputsAhead`: the inputs held behind a refusal gate that awaits its answer)
 * whose question states its place in its topic (`seq`). Such a question is open as soon as the return is certain to
 * need it, and the bank's order alone decides when it is asked. A question that states no `seq` is open only once the
 * evaluation itself reaches it, so where the bank states no order the forms' order of refusal gates still decides
 * (a screen before what stands behind it). A complete or refused return has the evaluation's own only.
 * `reach`: "none" leaves the pass out and "all" takes every input it finds; both are for measuring (interview-order). */
export type Reach = "stated" | "none" | "all";
function neededInputs(data: CanonicalData, config: InterviewData, inputs: Inputs, result: { derivations: Map<string, { value: Value; op: string }> }, targetValues: Value[], reach: Reach = "stated"): Set<string> {
  const needed = new Set<string>();
  // The reach pass adds something only where a line is held behind an unanswered gate.
  let held = false;
  for (const der of result.derivations.values()) {
    if (der.value.kind !== "unknown") continue;
    if (der.value.input) needed.add(der.value.input);
    held ||= der.op === "gate";
  }
  const incomplete = !targetValues.some((v) => v.kind === "refusal") && targetValues.some((v) => v.kind === "unknown");
  if (reach === "none" || !incomplete || !held) return needed;
  if (reach !== "all" && !config.questions.some((q) => q.seq !== undefined)) return needed;
  const recorded = recordedTemplates(config);
  for (const k of inputsAhead(data, inputs, config.targets)) {
    if (needed.has(k)) continue;
    const template = questionTemplate(k);
    if (reach === "all" || questionFor(config, recorded.get(template) ?? template)?.seq !== undefined) needed.add(k);
  }
  return needed;
}
/** What a caller that only steps through or compares states reads: status, refusal, the next question's input, the
 * reachable inputs and, as the function `valuesKey`, computed on demand, the derivations of `interviewView`'s `values` serialized in key order, so two
 * states' derivations are equal exactly when their keys are; no sheet, entry hints or question wording.
 * `reach` is for measuring what the reach pass changes (`neededInputs`; interview-order); every client of the
 * interview takes the default. */
export function interviewStatus(data: CanonicalData, config: InterviewData, inputs: Inputs, options: { reach?: Reach } = {}) {
  const result = evaluate(data, inputs, config.targets);
  const targetValues = config.targets.map(t => result.values.get(t)!);
  const refused = targetValues.find(v => v.kind === "refusal");
  const needed = neededInputs(data, config, inputs, result, targetValues, options.reach);
  const complete = targetValues.every(v => v.kind !== "unknown" && v.kind !== "refusal");
  let first: Place | null = null;
  for (const reachable of needed) {
    const { key, q } = askFor(config, reachable);
    const open = placeOf(q, key);
    if (!first || askOrder(open, first) < 0) first = open;
  }
  return { status: refused ? "refused" : complete ? "complete" : "incomplete", refusal: refused ?? null,
    question: refused || complete ? null : first,
    reachableInputs: [...needed].sort(),
    valuesKey: () => {
      const values: Record<string, unknown> = {};
      for (const [key, der] of [...result.derivations.entries()].sort((a, b) => (a[0] < b[0] ? -1 : 1)))
        values[key] = { value: der.value, op: der.op, cite: der.cite, operands: der.operands, guardsNotTaken: der.guardsNotTaken, notes: der.notes };
      return JSON.stringify(values);
    } };
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
  const line = inputLine(data, template);
  if (!line) throw new Error(`${key}: not an input`);
  if (line.type.startsWith("Enum(")) return { type: "Enum", values: data.params.enums[line.type.slice(5, -1)]!.values };
  return { type: line.type };
}
/** How to type an answer at the command line (`--value` is JSON), from the input's type. */
export function entryHint(data: CanonicalData, key: string, choices?: RosterChoice[], valueLabels?: Record<string, string>, valueOrder?: string[], withheld: string[] = []): string {
  const meta = inputMeta(data, key);
  const help = "; null asks for help";
  switch (meta.type) {
    case "Bool": return `true or false${help}`;
    case "NonNegDollars": return `integer cents, e.g. 620000 for $6,200.00${help}`;
    case "Dollars": return `integer cents, negative for a loss, e.g. -150000 for -$1,500.00${help}`;
    case "Count": return `a whole number, e.g. 2${help}`;
    case "Enum": return `one of: ${offeredValues(meta.values!, valueOrder, withheld).map((v) => JSON.stringify(v) + (valueLabels?.[v] ? ` (${valueLabels[v]})` : "")).join(", ")}${help}`;
    case "Roster": return choices
      ? `one of: ${choices.map((c) => `${JSON.stringify(c.value)} (${c.label})`).join(", ")}${help}`
      : `a JSON list of distinct entry keys (letters, digits, _ and -), e.g. ["acme_corp"], or [] for none${help}`;
    default: return `a ${meta.type} value${help}`;
  }
}
/** The values of an enum question in the order they are offered: the bank's label order where it has one, the enum's
 * otherwise, without the withheld ones. */
export function offeredValues(values: string[], valueOrder?: string[], withheld: string[] = []): string[] {
  return (valueOrder ?? values).filter((v) => !withheld.includes(v));
}
/** An answer event. `labels`, on a roster answer, maps each entry key to the label the user typed; replay ignores it.
 * `records`, on the answer to a roster question with choices, are the answers the chosen choice records (`answerEvent`
 * takes them from the question bank); replay applies them from the event, so a log gives the same state whatever the
 * bank says later. */
export interface Event { profile?: string; version?: number; tax_year?: number; input?: string; value?: unknown; labels?: Record<string, string>; records?: ChoiceRecord[] }
/** A log replayed: the inputs, and for each input a choice recorded (and no later answer replaced), the roster
 * question that recorded it and the sentence shown for it. */
export interface Replayed { inputs: Inputs; recorded: Record<string, { by: string; shown: string }> }

/** The event an answer becomes. This is the one place a roster choice's recorded answers are attached, and every
 * client answers through it: the command-line interview and the server (`applyAnswer`), and the walks of the fixtures,
 * the generated returns and the tests (interview-rules.ts, interview-check.ts).
 *
 * An answer to a roster question with choices must be one of them (in any key order), and carries that choice's
 * records. An input a choice recorded cannot be answered directly: the filer changes it by changing the choice.
 * Throws when the answer is not one the interview accepts. */
/** An answer event as `answerEvent` makes it. */
export interface AnswerEvent { input: string; value: unknown; labels?: Record<string, string>; records?: ChoiceRecord[] }
export function answerEvent(config: InterviewData, state: Replayed, input: string, value: unknown, labels?: Record<string, string>): AnswerEvent {
  const held = state.recorded[input];
  if (held) throw new Error(`${input} was recorded by the answer to ${held.by} (“${held.shown}”); change that answer to change it`);
  const q = questionFor(config, questionTemplate(input));
  let records: ChoiceRecord[] | undefined;
  if (q?.choices && value !== null) {
    const choice = Array.isArray(value) ? q.choices.find((c) => sameKeys(c.value, value as unknown[])) : undefined;
    if (!choice) throw new Error(`${input}: the answer is one of ${q.choices.map((c) => `${JSON.stringify(c.value)} (${c.label})`).join(", ")}`);
    value = [...choice.value];
    if (choice.records?.length) records = structuredClone(choice.records);
  }
  return { input, value, ...(labels === undefined ? {} : { labels }), ...(records ? { records } : {}) };
}
/** Checks an answer against the log's events without writing it: the input must be reachable or already answered (a
 * correction), the answer must be one `answerEvent` accepts, and the inputs with it must validate and evaluate. Throws
 * when the answer is rejected, so nothing is appended. Returns the event to append, the inputs with it, and the views
 * before and after it. */
export function applyAnswer(data: CanonicalData, config: InterviewData, events: Event[], input: string, value: unknown, labels?: unknown) {
  const state = replayState(config, events);
  const current = state.inputs;
  const before = interviewView(data, config, current);
  if (!before.reachableInputs.includes(input) && !(input in current)) throw new Error("answer is neither reachable nor a correction");
  if (labels !== undefined) {
    const keys = Array.isArray(value) ? value : null;
    const ok = input.startsWith("$") && keys !== null && labels !== null && typeof labels === "object" && !Array.isArray(labels)
      && Object.keys(labels).length === keys.length && keys.every((k) => typeof k === "string" && typeof (labels as Record<string, unknown>)[k] === "string"
        && ((labels as Record<string, string>)[k]!.trim() !== "") && (labels as Record<string, string>)[k]!.length <= 200);
    if (!ok) throw new Error(`${input}: labels must give each listed entry a label of 1 to 200 characters`);
  }
  const event = answerEvent(config, state, input, value, labels as Record<string, string> | undefined);
  const candidate = replay(config, [...events, event]);
  validateInputs(data, candidate);
  const after = interviewView(data, config, candidate);
  return { event, inputs: candidate, before, after };
}
/** Checks the answers given on one tick-box screen without writing them: one answer, Yes or No, for each box of the
 * screen the interview offers now (`group` of `interviewView`), and no other. They are judged together, against the
 * state before any of them, because the filer gave them together: an answer stands though another box's answer, taken
 * first, would refuse the return or leave its question unreachable. Throws when the answers are rejected, so nothing is
 * appended. Returns the events to append, in the order given, the inputs with them, and the views before and after. */
export function applyAnswers(data: CanonicalData, config: InterviewData, events: Event[], answers: unknown) {
  const state = replayState(config, events);
  const before = interviewView(data, config, state.inputs);
  const shape = "the answers of a tick-box screen are a list of {input, value}, one for each box, each value yes or no";
  if (!Array.isArray(answers) || answers.some((a) => !a || typeof a !== "object" || typeof (a as { input?: unknown }).input !== "string" || !("value" in a))) throw new Error(shape);
  const given = answers as { input: string; value: unknown }[];
  const boxes = before.group?.members.map((q) => q.input);
  if (!boxes) throw new Error("the interview offers no tick-box screen now; answer the next question on its own");
  const stray = given.find((a) => !boxes.includes(a.input));
  if (stray) throw new Error(`${stray.input}: not a box of the tick-box screen offered now (${boxes.join(", ")})`);
  const twice = given.find((a, i) => given.findIndex((b) => b.input === a.input) !== i);
  if (twice) throw new Error(`${twice.input}: answered twice`);
  const missing = boxes.find((k) => !given.some((a) => a.input === k));
  if (missing) throw new Error(`${missing}: the screen's answers leave this box out; a tick-box screen is answered whole (${boxes.join(", ")})`);
  const odd = given.find((a) => typeof a.value !== "boolean");
  if (odd) throw new Error(`${odd.input}: a tick-box is answered yes or no`);
  const made = given.map((a) => answerEvent(config, state, a.input, a.value));
  const candidate = replay(config, [...events, ...made]);
  validateInputs(data, candidate);
  const after = interviewView(data, config, candidate);
  return { events: made, inputs: candidate, before, after };
}
/** Replays a log. Events apply in order: an answer replaces the input's value; an answer to a roster question first
 * withdraws what that question's earlier answer recorded, then applies its own records, so changing a choice replaces
 * its recorded answers and leaves no recorded answer of the choice given up (an input left without a value is asked
 * again). A direct answer to an input that was recorded stands as an ordinary answer. Removing a roster entry makes
 * its answers inactive while they stay in the log. */
export function replayState(config: InterviewData, events: Event[]): Replayed {
  if (events[0]?.version !== 1 || events[0]?.tax_year !== config.tax_year) throw new Error("invalid interview log header");
  const inputs: Inputs = structuredClone(config.initial);
  const recorded: Replayed["recorded"] = {};
  for (const event of events.slice(1)) {
    if (typeof event.input !== "string" || !("value" in event) || event.input in config.initial) throw new Error("invalid answer event");
    const records = event.records ?? [];
    if (!Array.isArray(records) || records.some((r) => !r || typeof r.input !== "string" || !("value" in r) || typeof r.shown !== "string" || r.input in config.initial || r.input === event.input)) throw new Error("invalid answer event");
    for (const [key, held] of Object.entries(recorded)) if (held.by === event.input) { delete inputs[key]; delete recorded[key]; }
    inputs[event.input] = event.value;
    delete recorded[event.input];
    for (const r of records) { inputs[r.input] = r.value; recorded[r.input] = { by: event.input, shown: r.shown }; }
  }
  // Removing a roster entry makes its old answers inactive, while retaining them in the log.
  for (const key of Object.keys(inputs)) {
    const prefixes = [...key.matchAll(/([a-zA-Z0-9_]+)\[([a-zA-Z0-9_-]+)\]/g)];
    for (const match of prefixes) {
      const parent = key.slice(key.startsWith("$") ? key.indexOf("@") + 1 : 0, match.index).replace(/\.$/, "");
      const rk = `$${match[1]}${parent ? "@" + parent : ""}`;
      if (!Array.isArray(inputs[rk]) || !(inputs[rk] as string[]).includes(match[2]!)) { delete inputs[key]; delete recorded[key]; break; }
    }
  }
  return { inputs, recorded };
}
export function replay(config: InterviewData, events: Event[]): Inputs {
  return replayState(config, events).inputs;
}
/** The answers a return's choices recorded, as the clients list them: each input, its value, the question that
 * recorded it and the sentence shown for it. */
export function recordedAnswers(state: Replayed): { input: string; value: unknown; by: string; shown: string }[] {
  return Object.entries(state.recorded).map(([input, held]) => ({ input, value: state.inputs[input], ...held })).sort((a, b) => a.by.localeCompare(b.by) || a.input.localeCompare(b.input));
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
  const state = replayState(config, events);
  console.log(JSON.stringify({ ...interviewState(data, config, state.inputs), recorded: recordedAnswers(state) }, null, 2));
}
