// The words a filer is shown on the way through the interview (`interview-words`). Deterministic and free: it walks
// returns with the evaluator in the interview's own order and calls no model. It stands beside interview-length,
// which counts questions under three orders: this counts reading, under the one order the interview has, and needs
// each question as shown (reworded for the filing status answered, with the answers offered), which that tool
// never builds.
//
// For every question asked, counted each time it is asked (a question asked per person or per entry counts once per
// entry): the words of its prompt, of the answers offered with it (an enum's labels, a fixed roster's choices; Yes
// and No are not counted), and of its help, which is shown and optional to read, so it is counted apart.
// A return is walked as the page walks it: it ends when the return is complete or refused.
// "Before the first own item" is the prompt words of the questions asked before the first question the filer
// answers with something of their own (an amount, a number or a list) rather than by choosing an offered answer.
//
// The report also lists the longest sentences of the question bank (a sentence is the text between sentence ends
// within one line of a prompt; a list item is a line of its own).
//
// Returns: those interview-length walks (the Stage 5 whole returns, the generated returns, the minimal returns, and
// each slice profile's walked fixtures).
//
//   interview-words [--write] [--self-test]
//     --write       writes reports/<year>/interview_words.md
import assert from "node:assert/strict";
import { writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { answerEvent, inputMeta, interviewStatus, loadInterview, offeredValues, questionTemplate, replayState, withheldValues, type AnswerEvent, type InterviewData, type RosterChoice } from "./interview.js";
import { Unanswered, type Answers } from "./interview-rules.js";
import { casesOf, context } from "./interview-length.js";
import { shownFor } from "./spouse-wording.js";
import { YEAR } from "./year.js";
import type { CanonicalData, Inputs } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const REPORT = resolve(ROOT, "reports", String(YEAR), "interview_words.md");
const BOUND = 800;
const LONGEST = 3;

/** One answer the page offers: the value saved and the label shown. */
export interface Option { value: unknown; label: string }
/** A question as the page shows it. `about` is the page's "About:" line (the entries the question lies in, by
 * label); `options` the answers offered (Yes and No, an enum's labels or, where it has none, its values, a fixed
 * roster's choices), null where the filer types an amount, a number or a list of names. */
export interface Shown { input: string; template: string; order: number; about: string; prompt: string; help: string; type: string; options: Option[] | null }

/** The words a reader reads in a text: its tokens that hold a letter or a digit (list markers and dashes are not words). */
export function words(text: string): number {
  return text.split(/\s+/).filter((t) => /[\p{L}\p{N}]/u.test(t)).length;
}

const SEGMENT = /([a-zA-Z0-9_]+)\[([a-zA-Z0-9_-]+)\]/g;
/** Each listed entry's label, by entry path (`person[taxpayer].f8889[hsa]`): the label of the chosen answer of a
 * roster with fixed choices, else the caller's label for the path. A roster the profile fixes without asking has none. */
export function entryLabels(config: InterviewData, inputs: Inputs, given: Record<string, string> = {}): Record<string, string> {
  const out: Record<string, string> = { ...given };
  for (const [rk, keys] of Object.entries(inputs)) {
    if (!rk.startsWith("$") || !Array.isArray(keys)) continue;
    const choice = config.questions.find((x) => x.input === questionTemplate(rk))?.choices?.find((c: RosterChoice) => JSON.stringify(c.value) === JSON.stringify(keys));
    if (!choice) continue;
    const [coll, parent] = rk.slice(1).split("@") as [string, string | undefined];
    for (const k of keys as string[]) if (choice.labels[k]) out[`${parent ? parent + "." : ""}${coll}[${k}]`] = choice.labels[k]!;
  }
  return out;
}

/** The page's "About:" line of a question: the labels of the entries its key lies in ("You › HSA"); an entry with
 * no label reads as its collection and key, as on the page. */
export function aboutOf(key: string, labels: Record<string, string>): string {
  const body = key.startsWith("$") ? key.split("@")[1] ?? "" : key;
  const parts: string[] = [];
  for (const m of body.matchAll(SEGMENT)) parts.push(labels[body.slice(0, m.index! + m[0].length)] ?? `${m[1]} ${m[2]}`);
  return parts.join(" \u203a ");
}

/** The question for `key` as shown at these answers (`shownFor`: the spouse phrase reworded for the filing status
 * answered, the per-person frame and the person named for the entry), the entries it is about, and the answers
 * offered: an enum's labels in the order shown, without the values withheld. */
export function shownAt(data: CanonicalData, config: InterviewData, inputs: Inputs, key: string, given: Record<string, string> = {}): Shown {
  const stored = config.questions.find((x) => x.input === questionTemplate(key));
  if (!stored) throw new Error(`no question for ${key}`);
  const q = shownFor(stored, key, inputs);
  const meta = inputMeta(data, key);
  const options: Option[] | null =
    meta.type === "Bool" ? [{ value: true, label: "Yes" }, { value: false, label: "No" }]
    : meta.type === "Enum" ? offeredValues(meta.values!, q.value_order, withheldValues(config, inputs, key)).map((v) => ({ value: v, label: q.value_labels?.[v] ?? v }))
    : meta.type === "Roster" && q.choices ? q.choices.map((c) => ({ value: c.value, label: c.label }))
    : null;
  return { input: key, template: questionTemplate(key), order: q.order, about: aboutOf(key, entryLabels(config, inputs, given)), prompt: q.prompt, help: q.help ?? "", type: meta.type, options };
}

/** The words of a shown question: its prompt, its help (shown, optional to read) and the labels of its answers. */
export function shownWords(s: Shown): { prompt: number; help: number; options: number } {
  return { prompt: words(s.prompt), help: words(s.help), options: (s.options ?? []).reduce((a, o) => a + words(o.label), 0) };
}

/** One walk's reading. `beforeOwn` is null when the walk ends before any question about the filer's own items. */
export interface Reading {
  asked: number;
  prompt: number;
  options: number;
  help: number;
  beforeOwn: number | null;
  longest: { input: string; words: number }[];
}

/** Whether the filer answers with something of their own (an amount, a number, a list) rather than an offered answer. */
export function ownItem(s: Shown): boolean {
  return s.options === null;
}

/** The reading of the questions shown, in the order asked. */
export function reading(shown: Shown[]): Reading {
  const r: Reading = { asked: shown.length, prompt: 0, options: 0, help: 0, beforeOwn: null, longest: [] };
  const each: { input: string; words: number }[] = [];
  for (const s of shown) {
    const w = shownWords(s);
    if (r.beforeOwn === null && ownItem(s)) r.beforeOwn = r.prompt;
    r.prompt += w.prompt;
    r.help += w.help;
    if (s.type !== "Bool") r.options += w.options;
    each.push({ input: s.input, words: w.prompt });
  }
  r.longest = each.sort((a, b) => b.words - a.words || a.input.localeCompare(b.input)).slice(0, LONGEST);
  return r;
}

/** The words of the longest sentence of a text: the text between sentence ends (. ? !) within one line. */
export function longestSentence(text: string): number {
  return Math.max(0, ...text.split("\n").flatMap((line) => line.split(/(?<=[.?!])\s+/)).map(words));
}

/** A return walked as the page walks it: the interview's next question answered from `answers` until the return is
 * complete or refused (the page asks nothing more once a return is refused). Each question as shown when asked. Each
 * answer becomes its event through `answerEvent` and the state is the log replayed, as for every client of the
 * interview, so what a roster choice records is recorded here and is not asked. */
export function pageWalk(data: CanonicalData, config: InterviewData, answers: Answers, labels: Record<string, string> = {}): { shown: Shown[]; status: string } {
  const events: AnswerEvent[] = [];
  const replayed = () => replayState(config, [{ version: 1, tax_year: config.tax_year }, ...events]);
  let state = replayed();
  let inputs: Inputs = state.inputs;
  const shown: Shown[] = [];
  for (;;) {
    const st = interviewStatus(data, config, inputs);
    if (!st.question) return { shown, status: st.status };
    const key = st.question.input;
    const answer = answers(key, inputs);
    if (!answer) throw new Unanswered(key);
    shown.push(shownAt(data, config, inputs, key, labels));
    events.push(answerEvent(config, state, key, answer.value));
    state = replayed();
    inputs = state.inputs;
    if (shown.length > BOUND) throw new Error("the walk did not end");
  }
}

interface Row { group: string; id: string; profile: string; status: string; reading: Reading; prompts: Map<string, number> }

const mean = (xs: number[]) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : 0);
const median = (xs: number[]) => { const s = [...xs].sort((a, b) => a - b); return s.length ? s[Math.floor((s.length - 1) / 2)]! : 0; };
const f0 = (x: number) => Math.round(x).toLocaleString("en-US");
const f1 = (x: number) => x.toFixed(1);

function standardRows(): { rows: Row[]; unwalkable: number } {
  const ctx = context();
  const rows: Row[] = [];
  let unwalkable = 0;
  for (const c of casesOf(ctx)) {
    const config = ctx.configs[c.profile]!;
    try {
      const w = pageWalk(ctx.data, config, c.answers);
      const shown = w.shown;
      const prompts = new Map<string, number>();
      for (const s of shown) if (!prompts.has(s.template)) prompts.set(s.template, words(s.prompt));
      rows.push({ group: c.group, id: c.id, profile: c.profile, status: w.status, reading: reading(shown), prompts });
    } catch (e) { if (e instanceof Unanswered) unwalkable++; else throw e; }
  }
  return { rows, unwalkable };
}

function groupLine(name: string, rows: Row[]): string {
  const done = rows.filter((r) => r.status === "complete");
  const col = (pick: (r: Reading) => number, of: Row[]) => of.map((r) => pick(r.reading));
  const own = done.map((r) => r.reading.beforeOwn).filter((x): x is number => x !== null);
  return `| ${name} | ${done.length} | ${rows.length - done.length} | ${f1(mean(col((r) => r.asked, done)))} | ${f0(mean(col((r) => r.prompt, done)))} | ${f0(median(col((r) => r.prompt, done)))} | ${f0(Math.max(0, ...col((r) => r.prompt, done)))} | ${f0(mean(col((r) => r.options, done)))} | ${f0(mean(col((r) => r.help, done)))} | ${own.length ? f0(mean(own)) : "-"} | ${f0(mean(col((r) => r.prompt, rows.filter((r) => r.status !== "complete"))))} |`;
}

function render(std: { rows: Row[]; unwalkable: number }, bank: InterviewData): string {
  const sentences = bank.questions.map((q) => ({ input: q.input, prompt: words(q.prompt), help: words(q.help ?? ""), sentence: longestSentence(q.prompt) }));
  const longSentences = [...sentences].sort((a, b) => b.sentence - a.sentence || a.input.localeCompare(b.input)).slice(0, 12);
  const over = (n: number) => sentences.filter((q) => q.sentence > n).length;
  const groups = [...new Set(std.rows.map((r) => r.group))];
  const fullReal = std.rows.filter((r) => r.profile === "full" && r.group !== "minimal returns");
  // The longest prompts met: each question template by the words of its prompt as first shown, with the walks that ask it.
  const met = new Map<string, { words: number; walks: Set<string> }>();
  for (const r of std.rows) {
    if (r.profile !== "full") continue;
    for (const [template, n] of r.prompts) {
      const m = met.get(template) ?? { words: n, walks: new Set<string>() };
      m.walks.add(`${r.group}/${r.id}`);
      met.set(template, m);
    }
  }
  const fullWalks = std.rows.filter((r) => r.profile === "full").length;
  const longest = [...met.entries()].sort((a, b) => b[1].words - a[1].words || a[0].localeCompare(b[0])).slice(0, 15);
  const everywhere = [...met.entries()].filter(([, m]) => m.walks.size === fullWalks).sort((a, b) => b[1].words - a[1].words || a[0].localeCompare(b[0])).slice(0, 10);
  const out: string[] = [
    "# Interview words: what a filer reads",
    "",
    "Written by `node engine/dist/main.js interview-words --write` (engine/src/interview-words.ts; deterministic, no model calls).",
    "Every return is walked in the interview's own order, and each question asked is counted as the page shows it: the prompt",
    "reworded for the filing status answered, counted once per time it is asked (a question asked per person or per entry counts",
    "once per entry). **Prompt words** are the words of the prompts. **Option words** are the words of the answers offered with a",
    "question (an enum's labels or values, a fixed list's choices; Yes and No are not counted). **Help words** are the words of the",
    "help shown with each question, which a filer may skip. **Before the first own item** is the prompt words read before the first",
    "question answered with something of the filer's own (an amount, a number or a list) rather than by choosing an offered answer.",
    "A word is a run of characters holding a letter or a digit. The returns are synthetic.",
    "",
    "## The returns the project walks",
    "",
    "Means are over complete returns; the last column is the mean prompt words of the refused returns, which end at their refusal.",
    "",
    "| Returns | Complete | Refused | Questions asked (mean) | Prompt words (mean) | Prompt words (median) | Prompt words (max) | Option words (mean) | Help words (mean) | Before the first own item (mean) | Prompt words, refused (mean) |",
    "|---|---|---|---|---|---|---|---|---|---|---|",
    ...groups.map((g) => groupLine(g, std.rows.filter((r) => r.group === g))),
    groupLine("**full profile, Stage 5 and generated**", fullReal),
    "",
    `${std.unwalkable} return(s) could not be walked.`,
    "",
    "## The longest prompts met on the full profile",
    "",
    `The 15 longest prompts among the questions the ${fullWalks} full-profile walks ask, with how many of those walks ask each.`,
    "",
    "| Question | Prompt words | Walks that ask it |",
    "|---|---|---|",
    ...longest.map(([t, m]) => `| \`${t}\` | ${m.words} | ${m.walks.size} |`),
    "",
    `The longest prompts every one of the ${fullWalks} full-profile walks asks:`,
    "",
    "| Question | Prompt words |",
    "|---|---|",
    ...everywhere.map(([t, m]) => `| \`${t}\` | ${m.words} |`),
    "",
    "## The longest sentences in the question bank",
    "",
    `Of the ${sentences.length} questions the page's profile can ask, ${over(40)} have a sentence of more than 40 words in their prompt, ${over(80)} one of more than 80 and ${over(120)} one of more than 120.`,
    "The twelve longest:",
    "",
    "| Question | Longest sentence (words) | Prompt words |",
    "|---|---|---|",
    ...longSentences.map((q) => `| \`${q.input}\` | ${q.sentence} | ${q.prompt} |`),
    "",
  ];
  return out.join("\n");
}

export async function interviewWords(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  const t0 = performance.now();
  const std = standardRows();
  const text = render(std, loadInterview("ny"));
  if (args.includes("--write")) { writeFileSync(REPORT, text); console.log(`  wrote ${REPORT}`); } else console.log(text);
  console.log(`interview-words: ${std.rows.length} returns read, ${((performance.now() - t0) / 1000).toFixed(1)} s`);
  return 0;
}

/** The count on constructed questions, and on a real walk: a joint filer's reading is the sum of its questions as
 * shown, and a question asked of two people is counted twice. */
function selfTest(): number {
  const q = (input: string, prompt: string, help: string, type: string, options: Shown["options"]): Shown => ({ input, template: input, order: 0, about: "", prompt, help, type, options });
  const r = reading([
    q("a", "Who is on this return?", "Choose one.", "Roster", [{ value: ["x"], label: "Just me" }, { value: ["x", "y"], label: "Me and my spouse" }]),
    q("b", "Do you have any pets?\n\n- a cat\n- a dog", "", "Bool", [{ value: true, label: "Yes" }, { value: false, label: "No" }]),
    q("c", "Wages, tips, other compensation", "Box 1 of the form.", "NonNegDollars", null),
    q("d", "One more yes or no?", "", "Bool", [{ value: true, label: "Yes" }, { value: false, label: "No" }]),
  ]);
  assert.deepEqual({ ...r, longest: r.longest.map((l) => l.input) }, { asked: 4, prompt: 5 + 9 + 4 + 5, options: 2 + 4, help: 2 + 5, beforeOwn: 14, longest: ["b", "a", "d"] });
  assert.equal(words("Do you \u2014 or your spouse \u2014 have:\n\n- a cat\n- 2 dogs (Form 8889)?"), 12);
  assert.equal(aboutOf("person[taxpayer].f8889[hsa].line2", { "person[taxpayer]": "You", "person[taxpayer].f8889[hsa]": "HSA" }), "You \u203a HSA");
  assert.equal(aboutOf("$w2@person[spouse]", {}), "person spouse");
  assert.equal(reading([]).beforeOwn, null);
  assert.equal(longestSentence("Any of these: a cat; a dog, or a fish? No.\n\n- one two three four five six seven eight nine ten eleven\n- x"), 11);
  assert.equal(longestSentence(""), 0);
  assert.equal(reading([q("b", "Any pets?", "", "Bool", [{ value: true, label: "Yes" }])]).beforeOwn, null);
  const ctx = context();
  const config = ctx.configs["full"]!;
  const given: Inputs = { $person: ["taxpayer", "spouse"], "f1040.status": "mfj", "person[spouse].role": "spouse", "person[taxpayer].role": "taxpayer", "scope.other_line16": true };
  const walked = pageWalk(ctx.data, config, (k) => (k in given ? { value: given[k] } : undefined));
  assert.equal(walked.status, "refused");
  // A couple's first answer records the filing status and both roles (the stated ones are not asked); one person is asked the status.
  assert.deepEqual(walked.shown.map((s) => s.input), ["$person", "scope.other_line16"]);
  assert.throws(() => pageWalk(ctx.data, config, (k) => (k === "$person" ? { value: ["taxpayer"] } : undefined)), Unanswered);
  const alone: Inputs = { $person: ["taxpayer"], "f1040.status": "single", "scope.other_line16": true };
  const shown = pageWalk(ctx.data, config, (k) => (k in alone ? { value: alone[k] } : undefined)).shown.slice(0, 2);
  assert.deepEqual(shown.map((s) => s.input), ["$person", "f1040.status"]);
  assert.deepEqual(shown.map((s) => s.options!.length), [2, 4], "who the return is for has two choices; one person is offered four filing statuses, not married filing jointly");
  assert.ok(!shown[1]!.options!.some((o) => o.value === "mfj"));
  // A question asked of a person is counted as shown for that person's entry.
  const blind = shownAt(ctx.data, config, { $person: ["taxpayer", "spouse"], "person[taxpayer].role": "taxpayer", "person[spouse].role": "spouse", "f1040.status": "mfj" }, "person[spouse].blind");
  assert.ok(blind.prompt.startsWith("About your spouse \u2014 Was your spouse blind"), blind.prompt);
  const joint = reading(shown);
  assert.equal(joint.prompt, shown.reduce((a, s) => a + words(s.prompt), 0));
  assert.equal(joint.asked, 2);
  assert.ok(joint.options > 0, "the filing statuses and the two choices of who is on the return are options");
  assert.equal(joint.beforeOwn, null);
  console.log(`interview-words self-test: ${4 + walked.shown.length} questions counted, ok`);
  return 0;
}
