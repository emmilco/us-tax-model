// What a given filer is asked (`draft-walk`). Deterministic and free: no model is called. A persona
// (interview/<year>/personas/<name>.yaml) is a filer named in one sentence with the answers that filer gives, keyed by
// question id as the answer log has them. The tool walks the built interview (profile full, or the persona's `profile`:
// ny, the federal questions then the New York ones) as that filer, in the
// interview's own asking order, and writes a transcript: every question asked, as the page shows it, with the answer
// given, the words read and the places where the topic changes.
//
// The walk. Each step reads the next question from `interviewView` and answers through `applyAnswer`, as the page and
// the command-line interview do, and words the question with `shownAt` (interview-words.ts). It ends at the first
// refusal or at completion.
//
// Steps. A step is one screen of the page. A tick-box screen (`group` of `interviewView`: the members of the next
// question's group that the page shows together) is one step: its members are answered together through `applyAnswers`, as the page answers them,
// each from the source below. The step is printed with the heading and the labels the page shows, and its words (the
// heading's and the labels', not the members' own prompts, which the page keeps behind a disclosure) are counted once.
// Every other question is a step of its own. "Questions" still counts every question answered.
//
// Where an answer comes from, in this order:
//   the persona     its own `answers`, by the question's exact id
//   the background  the answer interview-coverage's background return (a filer with nothing to report) gave to the same
//                   kind of question (the same input template)
//   the closed answer (no, zero, none, the first option; the other option where that one refuses), for a question the
//                   background return never met. Such a question was opened by an earlier answer; the walk goes on, and
//                   the question is reported as OPENED AND UNANSWERED with the answer that opened it
//
// A persona fails, loudly, when
//   - an answer of the persona is never asked: a stale answer (the id names no question, or the walk never asks it)
//   - a question is opened and unanswered
//   - the interview rejects an answer
//   - the walk does not end as the persona's `end` says
// The transcript is written all the same, with the problems at its head, so the next reader sees what to add.
//
// A persona may name `extends: <persona>`: the answers of that persona (in the same directory) are taken first and its
// own answers are laid over them, so a New York filer is a federal persona plus the New York answers. A walk of the ny
// profile also reports its New York stretch: the questions whose input is a New York line (form ny_*), wherever asked.
//
// A topic is the form an input belongs to (a roster question's, its list's form). A topic switch is a question whose
// topic differs from the question before it; a return is a switch to a topic the walk had already left.
//
//   draft-walk [--personas DIR] [--out DIR] [--only NAME]... [--summary] [--self-test]
//     --personas DIR  the persona files (default interview/<year>/personas)
//     --out DIR       where the transcripts and SUMMARY.md go (default docs/provisional/walks/after). A file that
//                     exists in docs/provisional/walks/before, the baseline, is never overwritten
//     --only NAME     walk only this persona (SUMMARY.md is then not written)
//     --summary       print the table over all personas and write SUMMARY.md; no transcripts
import assert from "node:assert/strict";
import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { basename, join, relative, resolve } from "node:path";
import { parse } from "yaml";
import { templateKey } from "./branches.js";
import { applyAnswer, applyAnswers, interviewView, questionTemplate, replay, type Event, type InterviewData } from "./interview.js";
import { loadCtx, backgroundOf, type Background, type Ctx } from "./interview-coverage.js";
import { closedAnswer } from "./interview-rules.js";
import { shownAt, words, type Shown } from "./interview-words.js";
import { loadInterview } from "./interview.js";
import { YEAR } from "./year.js";
import type { CanonicalData, Inputs } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const PERSONAS = resolve(ROOT, "interview", String(YEAR), "personas");
const WALKS = resolve(ROOT, "docs", "provisional", "walks");
const OUT = join(WALKS, "after");
export const BASELINE = join(WALKS, "before");
const BOUND = 800;
const LONGEST = 10;

/** How a persona's walk must end: completion, or a refusal at a gate. */
export type ExpectedEnd = "complete" | { refused: string };
export type WalkProfile = "full" | "ny";
export interface Persona { name: string; who: string; end?: ExpectedEnd; profile?: WalkProfile; extends?: string; answers: Record<string, unknown> }

/** Where an answer came from. `unanswered`: a question the background return never met and the persona does not
 * answer, given the closed answer. */
export type From = "persona" | "background" | "unanswered";
export interface Asked {
  n: number;
  /** The screen the question is answered on; the members of a tick-box group shown together share one. */
  step: number;
  /** For a question answered on a tick-box screen: the group, its heading as shown, and the label beside this box. */
  tick?: { group: string; heading: string; label: string };
  shown: Shown;
  /** The form the input belongs to, and the line as printed where it has a number or a name. */
  topic: { id: string; title: string; printed: string };
  /** The topic differs from the question before; `returns`, to a topic the walk had already left. */
  switched: boolean;
  returns: boolean;
  value: unknown;
  from: From;
  /** The last answer given before the question was first reachable (null: reachable from the start). */
  openedBy: { n: number; input: string; value: unknown; from: From } | null;
}
export type WalkEnd =
  | { kind: "complete" }
  | { kind: "refused"; gate: string; form: string; remedy: string; note: string | null; conflict: string | null }
  | { kind: "rejected"; input: string; value: unknown; from: From; message: string }
  | { kind: "stuck"; message: string };
export interface PersonaWalk { persona: Persona; asked: Asked[]; end: WalkEnd; problems: string[] }

export interface WalkCtx { ctx: Ctx; config: InterviewData; background: Background; topicOf: (key: string) => Asked["topic"] }

export function walkCtx(ctx: Ctx = loadCtx(), config: InterviewData = loadInterview("full"), background?: Background, profile: WalkProfile = "full"): WalkCtx {
  const data: CanonicalData = ctx.data;
  const forms = new Map(data.forms.map((f) => [f.id, f] as const));
  const lineForm = new Map(data.forms.flatMap((f) => f.lines.map((l) => [l.id, { form: f, line: l }] as const)));
  const topicOf = (key: string): Asked["topic"] => {
    const t = questionTemplate(key);
    const hit = lineForm.get(t);
    const form = t.startsWith("$") ? forms.get(t.slice(1)) : hit?.form;
    if (!form) return { id: t.startsWith("$") ? t.slice(1) : t.split(".")[0]!, title: "(no form)", printed: "" };
    const printed = hit?.line.printed && !hit.line.printed.startsWith("(") ? `${/^\d/.test(hit.line.printed) ? "line " : ""}${hit.line.printed}` : "";
    return { id: form.id, title: form.title, printed };
  };
  return { ctx, config, background: background ?? backgroundOf(data, config, profile), topicOf };
}

const show = (v: unknown): string => JSON.stringify(v);
const fromText = (f: From): string => (f === "persona" ? "the persona's answer" : f === "background" ? "a background answer" : "a closed answer given to an unanswered question");

/** Walks the built interview as the persona: see the head of this file. */
export function walkPersona(w: WalkCtx, persona: Persona): PersonaWalk {
  const { ctx, config, background, topicOf } = w;
  const events: Event[] = [{ version: 1, tax_year: config.tax_year }];
  const asked: Asked[] = [];
  const problems: string[] = [];
  const opener = new Map<string, Asked["openedBy"]>();
  const left = new Set<string>();
  let inputs: Inputs = replay(config, events);
  let view = interviewView(ctx.data, config, inputs);
  let end: WalkEnd;
  for (;;) {
    if (asked.length > BOUND) { end = { kind: "stuck", message: "the walk did not end" }; break; }
    const last = asked.at(-1);
    for (const k of view.reachableInputs) if (!opener.has(k)) opener.set(k, last ? { n: last.n, input: last.shown.input, value: last.value, from: last.from } : null);
    if (view.status === "refused") {
      const r = view.refusal as { gate: string; form: string; remedy: string };
      end = { kind: "refused", gate: r.gate, form: r.form, remedy: r.remedy, note: view.refusalNote, conflict: ctx.conflicts[templateKey(r.gate)] ?? null };
      break;
    }
    if (view.status === "complete") { end = { kind: "complete" }; break; }
    const next = view.question?.input;
    if (next === undefined) { end = { kind: "stuck", message: "the return is incomplete and the interview has no question" }; break; }
    // One screen: the tick-box group the next question is shown in, or the next question alone.
    const keys = view.group?.members.map((q) => q.input) ?? [next];
    const step = (last?.step ?? 0) + 1;
    const answers = keys.map((key): { value: unknown; from: From } => {
      const template = questionTemplate(key);
      return key in persona.answers ? { value: persona.answers[key], from: "persona" }
        : background.answers.has(template) ? { value: background.answers.get(template), from: "background" }
        : { value: closedAnswer(ctx.data, config, key, inputs), from: "unanswered" };
    });
    const shown = keys.map((key) => shownAt(ctx.data, config, inputs, key));
    let after: { events: Event[]; inputs: Inputs; view: typeof view };
    try {
      if (view.group) { const a = applyAnswers(ctx.data, config, events, keys.map((input, i) => ({ input, value: answers[i]!.value }))); after = { events: a.events, inputs: a.inputs, view: a.after }; }
      else { const a = applyAnswer(ctx.data, config, events, next, answers[0]!.value); after = { events: [a.event], inputs: a.inputs, view: a.after }; }
    } catch (e) {
      // A screen's answers are rejected together; the one the message names is reported, else the first.
      const message = e instanceof Error ? e.message : String(e);
      const i = Math.max(0, keys.findIndex((k) => message.startsWith(`${k}:`)));
      end = { kind: "rejected", input: keys[i]!, value: answers[i]!.value, from: answers[i]!.from, message };
      break;
    }
    keys.forEach((key, i) => {
      const before = asked.at(-1);
      const topic = topicOf(key);
      const switched = before !== undefined && before.topic.id !== topic.id;
      if (switched) left.add(before!.topic.id);
      const label = view.group ? view.group.members[i]!.tick ?? shown[i]!.prompt : undefined;
      asked.push({ n: asked.length + 1, step, ...(view.group && label !== undefined ? { tick: { group: view.group.id, heading: view.group.heading, label } } : {}),
        shown: shown[i]!, topic, switched, returns: switched && left.has(topic.id), value: answers[i]!.value, from: answers[i]!.from, openedBy: opener.get(key) ?? null });
    });
    events.push(...after.events);
    inputs = after.inputs;
    view = after.view;
  }

  // The problems, each naming the persona.
  const who = `persona ${persona.name}`;
  for (const a of asked) {
    if (a.from !== "unanswered") continue;
    const by = a.openedBy;
    problems.push(`${who}: OPENED AND UNANSWERED: question ${a.n}, ${a.shown.input}, is asked of this filer and the persona does not answer it (a filer with nothing to report is never asked it). ${by === null ? "It is asked from the start." : `It was opened by question ${by.n}, ${by.input} = ${show(by.value)} (${fromText(by.from)}).`} The walk gave it the closed answer ${show(a.value)}; add the answer this filer gives: ${show(a.shown.input)}: …`);
  }
  if (end.kind === "rejected") problems.push(`${who}: the interview rejects the answer ${show(end.value)} to ${end.input} (${fromText(end.from)}), after ${asked.length} answers: ${end.message}`);
  if (end.kind === "stuck") problems.push(`${who}: ${end.message}`);
  const askedIds = new Set(asked.map((a) => a.shown.input));
  const instanceOf = new Map(asked.map((a) => [a.shown.template, a.shown.input]));
  const bank = new Set(config.questions.map((q) => q.input));
  const ended = endText(end);
  for (const k of Object.keys(persona.answers)) {
    if (askedIds.has(k)) continue;
    const t = questionTemplate(k);
    if (!bank.has(t)) { problems.push(`${who}: STALE ANSWER: ${k} names no question of the interview (no question ${t}): it was renamed, split or removed. Give the answer under the question's new id, or drop it.`); continue; }
    const instance = instanceOf.get(t) ?? instanceOf.get(k);
    problems.push(`${who}: STALE ANSWER: ${k} is never asked on this walk (it ${ended} after ${asked.length} answers): an earlier answer no longer opens it, or the walk ended first.${instance && instance !== k ? ` The walk asked ${instance}: a persona names the question's exact id, with its entries.` : ""}`);
  }
  const x = persona.end;
  if (x === "complete" && end.kind !== "complete") problems.push(`${who}: expected the return to be completed; the walk ${ended} after ${asked.length} answers`);
  if (x !== undefined && x !== "complete" && (end.kind !== "refused" || end.gate !== x.refused)) problems.push(`${who}: expected a refusal at ${x.refused}; the walk ${ended} after ${asked.length} answers`);
  // The refusal comes on the last screen: on a tick-box screen, on any of its answers.
  if (x !== undefined && x !== "complete" && end.kind === "refused" && end.gate === x.refused && !asked.some((a) => a.step === asked.at(-1)!.step && a.from === "persona"))
    problems.push(`${who}: the refusal at ${end.gate} came on ${fromText(asked.at(-1)?.from ?? "background")} (question ${asked.length}, ${asked.at(-1)?.shown.input}), not on an answer of the persona`);
  return { persona, asked, end, problems };
}

function endText(end: WalkEnd): string {
  switch (end.kind) {
    case "complete": return "completed the return";
    case "refused": return `was refused at ${end.gate} (${end.form})`;
    case "rejected": return `had the answer ${show(end.value)} to ${end.input} rejected`;
    case "stuck": return end.message;
  }
}

// ---- the figures ----

/** `steps`: the screens (a tick-box group shown together is one). `prompt`: the words read to answer: each question's
 * prompt, and for a tick-box screen its heading once and its labels. */
export interface Figures { asked: number; steps: number; prompt: number; help: number; options: number; switches: number; returns: number; topics: number; closed: number; own: number; unanswered: number }

/** An answer of no, zero or none. */
export const isClosed = (v: unknown): boolean => v === false || v === 0 || (Array.isArray(v) && v.length === 0);

/** A question of the New York stretch: its input is a line of a New York form. */
export const isNy = (a: Asked): boolean => a.topic.id.startsWith("ny_");

export function figures(asked: Asked[]): Figures {
  const f: Figures = { asked: asked.length, steps: new Set(asked.map((a) => a.step)).size, prompt: 0, help: 0, options: 0, switches: 0, returns: 0, topics: new Set(asked.map((a) => a.topic.id)).size, closed: 0, own: 0, unanswered: 0 };
  for (const [i, a] of asked.entries()) {
    f.prompt += readWords(a, asked[i - 1]);
    f.help += words(a.shown.help);
    if (a.shown.type !== "Bool") f.options += (a.shown.options ?? []).reduce((n, o) => n + words(o.label), 0);
    if (a.switched) f.switches++;
    if (a.returns) f.returns++;
    if (isClosed(a.value)) f.closed++;
    if (a.from === "persona") f.own++;
    if (a.from === "unanswered") f.unanswered++;
  }
  return f;
}

/** The words read to answer `a`: its prompt; on a tick-box screen its label, and with the screen's first box (`before`
 * is the question before it) the heading. */
export function readWords(a: Asked, before: Asked | undefined): number {
  if (!a.tick) return words(a.shown.prompt);
  return words(a.tick.label) + (before?.step === a.step ? 0 : words(a.tick.heading));
}

// ---- the transcript ----

const money = (cents: number): string => `${cents < 0 ? "-" : ""}$${(Math.abs(cents) / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;

/** An answer in the words the page shows for it. */
export function answerText(s: Shown, value: unknown): string {
  if (value === true) return "Yes";
  if (value === false) return "No";
  if (Array.isArray(value)) {
    const choice = s.type === "Roster" ? s.options?.find((o) => JSON.stringify(o.value) === JSON.stringify(value)) : undefined;
    return choice ? `“${choice.label}”` : value.length ? `the list ${value.map((v) => `\`${String(v)}\``).join(", ")}` : "none (an empty list)";
  }
  if (typeof value === "number") return s.type === "Dollars" || s.type === "NonNegDollars" ? money(value) : String(value);
  if (typeof value === "string") { const o = s.options?.find((x) => x.value === value); return o && o.label !== value ? `“${o.label}” (\`${value}\`)` : `\`${value}\``; }
  return `\`${show(value)}\``;
}

function offeredText(s: Shown): string {
  if (s.type === "Bool") return "Yes / No";
  if (s.options) return s.options.map((o) => `“${o.label}”`).join(" / ");
  switch (s.type) {
    case "Roster": return "a list the filer builds, naming each entry";
    case "NonNegDollars": return "a dollar amount, zero or more";
    case "Dollars": return "a dollar amount, which may be negative";
    case "Count": return "a whole number";
    default: return `a value of the type ${s.type}`;
  }
}

/** The first sentence of a help text (of its first line). */
export function firstSentence(help: string): string {
  const line = help.split("\n").find((l) => l.trim() !== "")?.trim() ?? "";
  return /^.*?[.?!](?=\s|$)/.exec(line)?.[0] ?? line;
}

const quoted = (text: string): string => text.split("\n").map((l) => (l === "" ? ">" : `> ${l}`)).join("\n");
const fromMark = (f: From): string => (f === "persona" ? "persona" : f === "background" ? "background" : "**OPENED AND UNANSWERED**: the closed answer, given so the walk goes on");
const topicText = (t: Asked["topic"]): string => `${t.title} (\`${t.id}\`)`;

function endSection(end: WalkEnd, asked: number): string[] {
  switch (end.kind) {
    case "complete": return [`**Complete.** The return is completed after ${asked} questions.`];
    case "refused": return [
      `**${end.conflict !== null ? "Stopped as conflicting answers" : "Refused"}** at the gate \`${end.gate}\`, after ${asked} questions. The wording shown:`,
      "",
      quoted([`${end.form}`, "", end.remedy, ...(end.conflict !== null ? ["", end.conflict] : []), ...(end.note !== null ? ["", end.note] : [])].join("\n")),
    ];
    case "rejected": return [`**The walk broke off** after ${asked} questions: the interview rejected the answer ${show(end.value)} to \`${end.input}\` (${fromText(end.from)}): ${end.message}`];
    case "stuck": return [`**The walk broke off** after ${asked} questions: ${end.message}`];
  }
}

export function renderTranscript(w: PersonaWalk): string {
  const f = figures(w.asked);
  const out: string[] = [
    `# Walk: ${w.persona.name}`,
    "",
    w.persona.who,
    "",
    `Written by \`node engine/dist/main.js draft-walk\` from \`interview/${YEAR}/personas/${w.persona.name}.yaml\`${w.persona.extends ? ` (extending \`${w.persona.extends}\`)` : ""}: the built interview (profile \`${w.persona.profile ?? "full"}\`, ${w.persona.profile === "ny" ? "the federal questions, then the New York ones" : "the federal questions"}, ${YEAR}) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as \`interview-words\` counts them. Help is shown and optional to read: only its length and first sentence are given.`,
    "",
  ];
  if (w.problems.length) out.push("## PROBLEMS WITH THIS PERSONA", "", ...w.problems.map((p) => `- ${p}`), "");
  out.push("## The walk", "");
  for (const [i, a] of w.asked.entries()) {
    const s = a.shown;
    if (a.tick) {
      // A tick-box screen, printed once, at its first box: the heading and the labels as the page shows them.
      if (w.asked[i - 1]?.step === a.step) continue;
      const boxes = w.asked.filter((b) => b.step === a.step);
      const ticked = boxes.filter((b) => b.value === true);
      const sources = [...new Set(boxes.map((b) => fromMark(b.from)))].join("; ");
      out.push(
        `### ${a.n}–${boxes.at(-1)!.n}. Tick-boxes \`${a.tick.group}\`: ${boxes.length} questions on one screen`,
        "",
        ...(boxes.some((b) => b.switched) ? [`**⟶ topic switch${boxes.some((b) => b.returns) ? " (returns)" : ""}**`, ""] : []),
        `Topic: ${[...new Set(boxes.map((b) => topicText(b.topic)))].join("; ")}${s.about ? `. About: ${s.about}` : ""}`,
        "",
        quoted(a.tick.heading),
        ">",
        ...boxes.map((b) => `> - [${b.value === true ? "x" : " "}] ${b.tick!.label}  (\`${b.shown.input}\`)`),
        "",
        `- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”`,
        `- Answer: ${ticked.length ? `ticked ${ticked.map((b) => `“${b.tick!.label}”`).join(", ")}; the other${boxes.length - ticked.length === 1 ? "" : "s"} recorded No` : `“None of these”: each recorded No`} (${sources})`,
        `- Words: heading ${words(a.tick.heading)}, labels ${boxes.reduce((n, b) => n + words(b.tick!.label), 0)}. Behind each box, optional to read: the question's own prompt (${boxes.map((b) => words(b.shown.prompt)).join(", ")} words) and help (${boxes.map((b) => words(b.shown.help)).join(", ")})`,
        "",
      );
      continue;
    }
    out.push(
      `### ${a.n}. \`${s.input}\``,
      "",
      ...(a.switched ? [`**⟶ topic switch${a.returns ? " (returns)" : ""}**`, ""] : []),
      `Topic: ${topicText(a.topic)}${a.topic.printed ? `, ${a.topic.printed}` : ""}${s.about ? `. About: ${s.about}` : ""}`,
      "",
      quoted(s.prompt),
      "",
      `- Offered: ${offeredText(s)}`,
      `- Answer: ${answerText(s, a.value)} (${fromMark(a.from)})`,
      `- Words: prompt ${words(s.prompt)}, help ${words(s.help)}${s.help ? `. Help begins: “${firstSentence(s.help)}”` : ""}`,
      "",
    );
  }
  const longest = [...w.asked].sort((a, b) => words(b.shown.prompt) - words(a.shown.prompt) || a.n - b.n).slice(0, LONGEST);
  out.push(
    "## The end reached",
    "",
    ...endSection(w.end, w.asked.length),
    "",
    "## Totals",
    "",
    "| | |",
    "|---|---|",
    `| Questions asked | ${f.asked} |`,
    `| Steps (screens; a tick-box group shown together is one) | ${f.steps} |`,
    `| Answered by the persona / by the background / opened and unanswered | ${f.own} / ${f.asked - f.own - f.unanswered} / ${f.unanswered} |`,
    `| Prompt words (a tick-box screen: its heading and labels) | ${f.prompt} |`,
    `| Help words (optional to read) | ${f.help} |`,
    `| Words of the answers offered (Yes and No not counted) | ${f.options} |`,
    `| Questions answered no, zero or none | ${f.closed} |`,
    `| Topics met | ${f.topics} |`,
    ...(w.persona.profile === "ny" ? (() => { const n = figures(w.asked.filter(isNy)); return [`| New York stretch (questions of New York forms): questions / steps / prompt words / help words | ${n.asked} / ${n.steps} / ${n.prompt} / ${n.help} |`]; })() : []),
    `| Topic switches | ${f.switches} |`,
    `| of them, returns to a topic already left | ${f.returns} |`,
    "",
    `## The ${Math.min(LONGEST, w.asked.length)} longest prompts met`,
    "",
    "| # | Question | Prompt words | Answer |",
    "|---|---|---|---|",
    ...longest.map((a) => `| ${a.n} | \`${a.shown.input}\`${a.tick ? " (its own prompt, behind a tick-box)" : ""} | ${words(a.shown.prompt)} | ${answerText(a.shown, a.value).replace(/\|/g, "\\|")} |`),
    "",
    "## The whole walk, one line per question",
    "",
    "Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.",
    "",
    "```",
    ...compact(w.asked),
    "```",
    "",
  );
  return out.join("\n");
}

function compact(asked: Asked[]): string[] {
  const idWidth = Math.min(58, Math.max(0, ...asked.map((a) => a.shown.input.length)));
  return asked.map((a, i) => {
    const mark = (a.returns ? ">>" : a.switched || i === 0 ? "> " : "  ") + (a.from === "persona" ? "*" : a.from === "unanswered" ? "!" : " ");
    const v = show(a.value);
    return `${mark}${String(a.n).padStart(3)}  ${a.shown.input.padEnd(idWidth)} ${String(readWords(a, asked[i - 1])).padStart(4)}w${a.tick ? "+" : " "} ${v.length > 28 ? v.slice(0, 27) + "…" : v.padEnd(28)}${a.switched || i === 0 ? `  [${a.topic.id}]` : ""}${a.tick ? `  (screen ${a.step}, ${a.tick.group})` : ""}`.trimEnd();
  });
}

function endCell(end: WalkEnd): string {
  switch (end.kind) {
    case "complete": return "complete";
    case "refused": return `${end.conflict !== null ? "conflicting answers" : "refused"} at \`${end.gate}\``;
    default: return "**broke off**";
  }
}

export function renderSummary(walks: PersonaWalk[]): string {
  const out: string[] = [
    "# The persona walks: summary",
    "",
    `Written by \`node engine/dist/main.js draft-walk\` (engine/src/draft-walk.ts; deterministic, no model calls) from the personas in \`interview/${YEAR}/personas/\`, on the built interview (profile \`full\`, ${YEAR}). A step is one screen: a tick-box group shown together is one step, and its prompt words are its heading and labels, counted once. A topic is the form a question's input belongs to; a switch is a question whose topic differs from the one before it, and a return is a switch to a topic already left. “No, zero, none” counts the questions answered no, zero or with an empty list. A refused persona's figures end at its refusal.`,
    "",
    "| Persona | Questions | Steps | Prompt words | Help words | No, zero, none | Topics | Switches | Returns | End | Problems |",
    "|---|---|---|---|---|---|---|---|---|---|---|",
  ];
  for (const w of walks) {
    const f = figures(w.asked);
    out.push(`| \`${w.persona.name}\` | ${f.asked} | ${f.steps} | ${f.prompt} | ${f.help} | ${f.closed} | ${f.topics} | ${f.switches} | ${f.returns} | ${endCell(w.end)} | ${w.problems.length || ""} |`);
  }
  const ny = walks.filter((w) => w.persona.profile === "ny");
  if (ny.length) {
    out.push("", "The New York stretch of the personas of profile `ny`: the questions whose input is a line of a New York form (wherever asked; a tick-box screen of them is one step).", "",
      "| Persona | New York questions | Steps | Prompt words | Help words | No, zero, none | First New York question at | End |", "|---|---|---|---|---|---|---|---|");
    for (const w of ny) {
      const nyAsked = w.asked.filter(isNy);
      const f = figures(nyAsked);
      out.push(`| \`${w.persona.name}\` | ${f.asked} | ${f.steps} | ${f.prompt} | ${f.help} | ${f.closed} | ${nyAsked.length ? `question ${nyAsked[0]!.n} of ${w.asked.length}` : "none"} | ${endCell(w.end)} |`);
    }
  }
  out.push("", "Who each persona is:", "", ...walks.map((w) => `- \`${w.persona.name}\`: ${w.persona.who}`), "");
  return out.join("\n");
}

// ---- the files ----

/** A persona file read and checked; throws naming the file. */
export function readPersona(path: string): Persona {
  const name = basename(path).replace(/\.(yaml|json)$/, "");
  let v: unknown;
  try { v = parse(readFileSync(path, "utf8")); } catch (e) { throw new Error(`${path}: not readable as YAML: ${e instanceof Error ? e.message : String(e)}`); }
  return checkPersona(v, name, path);
}

export function checkPersona(v: unknown, name: string, where: string): Persona {
  const bad = (what: string): never => { throw new Error(`${where}: ${what}`); };
  if (v === null || typeof v !== "object" || Array.isArray(v)) bad("a persona is a mapping with name, who and answers");
  const p = v as Record<string, unknown>;
  for (const k of Object.keys(p)) if (!["name", "who", "end", "profile", "extends", "answers"].includes(k)) bad(`unknown key ${k} (a persona has name, who, end, profile, extends and answers)`);
  if (p["profile"] !== undefined && p["profile"] !== "full" && p["profile"] !== "ny") bad("profile must be full or ny");
  if (p["extends"] !== undefined && (typeof p["extends"] !== "string" || !p["extends"])) bad("extends must name a persona");
  if (p["name"] !== name) bad(`name is ${show(p["name"])}; it must be the file's name, ${show(name)}`);
  if (typeof p["who"] !== "string" || !p["who"].trim() || p["who"].includes("\n")) bad("who must be one plain sentence saying who this is");
  const answers = p["answers"];
  if (answers === null || typeof answers !== "object" || Array.isArray(answers)) bad("answers must be a mapping from question id to answer");
  for (const [k, a] of Object.entries(answers as Record<string, unknown>)) if (a === null || a === undefined) bad(`the answer to ${k} is empty (an answer is a value, as the answer log has it; null asks for help and is not an answer)`);
  const end = p["end"];
  const refused = end !== null && typeof end === "object" ? (end as Record<string, unknown>)["refused"] : undefined;
  if (end !== undefined && end !== "complete" && !(typeof refused === "string" && Object.keys(end as object).length === 1)) bad("end must be `complete` or `{ refused: <gate> }`");
  return { name, who: (p["who"] as string).trim(), ...(end !== undefined ? { end: end as ExpectedEnd } : {}), ...(p["profile"] !== undefined ? { profile: p["profile"] as WalkProfile } : {}),
    ...(p["extends"] !== undefined ? { extends: p["extends"] as string } : {}), answers: answers as Record<string, unknown> };
}

/** Writes a transcript or a summary. A file of the baseline that exists is never overwritten. */
export function writeWalkFile(path: string, text: string, baseline: string = BASELINE): void {
  if (resolve(path).startsWith(resolve(baseline) + "/") && existsSync(path))
    throw new Error(`${path} exists and is a baseline walk, which is never overwritten. Write to another directory (--out), by default ${relative(ROOT, OUT)}`);
  writeFileSync(path, text);
}

// ---- the command ----

export async function draftWalk(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  const option = (name: string): string[] => args.flatMap((a, i) => (a === name && args[i + 1] !== undefined ? [args[i + 1]!] : []));
  const dir = resolve(option("--personas")[0] ?? PERSONAS);
  const out = resolve(option("--out")[0] ?? OUT);
  const only = option("--only");
  const summaryOnly = args.includes("--summary");
  if (summaryOnly && only.length) { console.error("draft-walk: --summary is the table over all personas; it does not take --only"); return 2; }
  if (!existsSync(dir)) { console.error(`draft-walk: no persona directory ${dir}`); return 2; }
  const files = readdirSync(dir).filter((f) => /\.(yaml|json)$/.test(f)).sort();
  const problems: string[] = [];
  const personas: Persona[] = [];
  for (const f of files) try { personas.push(readPersona(join(dir, f))); } catch (e) { problems.push(e instanceof Error ? e.message : String(e)); }
  // extends: the named persona's answers first (resolved through its own extends), the persona's own laid over them.
  const byName = new Map(personas.map((p) => [p.name, p] as const));
  const resolved = (p: Persona, seen: string[] = []): Record<string, unknown> => {
    if (p.extends === undefined) return p.answers;
    const base = byName.get(p.extends);
    if (!base || seen.includes(p.extends)) { problems.push(`persona ${p.name}: extends ${p.extends}, ${base ? "a cycle" : "which is no persona of " + dir}`); return p.answers; }
    return { ...resolved(base, [...seen, p.name]), ...p.answers };
  };
  for (const p of personas) p.answers = resolved(p);
  for (const n of only) if (!personas.some((p) => p.name === n)) problems.push(`--only ${n}: no persona of that name in ${dir}`);
  const chosen = only.length ? personas.filter((p) => only.includes(p.name)) : personas;
  if (!chosen.length) problems.push(`no persona to walk in ${dir}`);
  const t0 = performance.now();
  const ctxs = new Map<WalkProfile, WalkCtx>();
  const ctxOf = (profile: WalkProfile): WalkCtx => {
    if (!ctxs.has(profile)) { const first = ctxs.values().next().value; ctxs.set(profile, walkCtx(first?.ctx ?? loadCtx(), loadInterview(profile), undefined, profile)); }
    return ctxs.get(profile)!;
  };
  const walks = chosen.map((p) => walkPersona(ctxOf(p.profile ?? "full"), p));
  mkdirSync(out, { recursive: true });
  const rel = (p: string) => (relative(ROOT, p).startsWith("..") ? p : relative(ROOT, p));
  try {
    if (!summaryOnly) for (const pw of walks) writeWalkFile(join(out, `${pw.persona.name}.md`), renderTranscript(pw));
    if (!only.length && walks.length) writeWalkFile(join(out, "SUMMARY.md"), renderSummary(walks));
  } catch (e) { console.error(`draft-walk: ${e instanceof Error ? e.message : String(e)}`); return 1; }
  if (summaryOnly) console.log(renderSummary(walks));
  else for (const pw of walks) { const f = figures(pw.asked); console.log(`  ${pw.persona.name}: ${f.asked} questions on ${f.steps} screens, ${f.prompt} prompt words, ${f.help} help words, ${f.switches} topic switches, ${endText(pw.end)}${pw.problems.length ? `; ${pw.problems.length} PROBLEM(S)` : ""}`); }
  console.log(`  wrote ${summaryOnly ? "" : `${walks.length} transcript(s) and `}${only.length ? "no summary (--only)" : "SUMMARY.md"} in ${rel(out)}, ${((performance.now() - t0) / 1000).toFixed(1)} s`);
  for (const pw of walks) problems.push(...pw.problems);
  for (const p of problems) console.error(`  ${p}`);
  console.log(`draft-walk: ${walks.length} persona(s) walked, ${problems.length} problem(s)`);
  return problems.length ? 1 : 0;
}

/** The failure reports on planted personas, on the built interview: the planted answers are written against the
 * background return's own questions, so they hold whatever the question bank asks beyond them. */
function selfTest(): number {
  // The parts that need no interview.
  assert.equal(firstSentence("Enter box 1. Then box 2."), "Enter box 1.");
  assert.equal(firstSentence("See Pub. 17 for more"), "See Pub.");
  assert.equal(firstSentence("No sentence end"), "No sentence end");
  assert.equal(firstSentence("\nAre you sure? Yes."), "Are you sure?");
  assert.ok(isClosed(false) && isClosed(0) && isClosed([]) && !isClosed(true) && !isClosed(["a"]) && !isClosed("single") && !isClosed(100));
  assert.throws(() => checkPersona({ name: "a", who: "A filer.", answers: {} }, "b", "planted"), /name is "a"; it must be the file's name, "b"/);
  assert.throws(() => checkPersona({ name: "a", answers: {} }, "a", "planted"), /who must be one plain sentence/);
  assert.throws(() => checkPersona({ name: "a", who: "A filer.", answers: { "x.y": null } }, "a", "planted"), /the answer to x\.y is empty/);
  assert.throws(() => checkPersona({ name: "a", who: "A filer.", answers: {}, end: "refused" }, "a", "planted"), /end must be/);
  assert.throws(() => checkPersona({ name: "a", who: "A filer.", answers: {}, expect: "complete" }, "a", "planted"), /unknown key expect/);
  assert.deepEqual(checkPersona({ name: "a", who: "A filer. ", answers: { "x.y": 0 }, end: { refused: "g.h" } }, "a", "planted"), { name: "a", who: "A filer.", end: { refused: "g.h" }, answers: { "x.y": 0 } });

  // The baseline is never overwritten; another directory is.
  const tmp = mkdtempSync(join(tmpdir(), "draft-walk-"));
  try {
    const before = join(tmp, "before"), after = join(tmp, "after");
    mkdirSync(before); mkdirSync(after);
    writeWalkFile(join(before, "a.md"), "one", before);
    assert.throws(() => writeWalkFile(join(before, "a.md"), "two", before), /is a baseline walk, which is never overwritten/);
    assert.equal(readFileSync(join(before, "a.md"), "utf8"), "one");
    writeWalkFile(join(after, "a.md"), "one", before);
    writeWalkFile(join(after, "a.md"), "two", before);
    assert.equal(readFileSync(join(after, "a.md"), "utf8"), "two");
  } finally { rmSync(tmp, { recursive: true, force: true }); }

  const w = walkCtx();
  const { ctx, config, background } = w;
  const bg = background.steps;
  const persona = (answers: Record<string, unknown>, end?: ExpectedEnd): Persona => ({ name: "planted", who: "A planted filer.", ...(end !== undefined ? { end } : {}), answers });
  const problemsOf = (answers: Record<string, unknown>, end?: ExpectedEnd): string => walkPersona(w, persona(answers, end)).problems.join("\n");

  // A persona with no answer of its own walks the background return, and completes.
  const plain = walkPersona(w, persona({}, "complete"));
  assert.deepEqual(plain.problems, []);
  assert.equal(plain.end.kind, "complete");
  assert.deepEqual(plain.asked.map((a) => a.shown.input), bg.map((s) => s.input), "the questions of the background return, in its order");
  assert.ok(plain.asked.every((a) => a.from === "background"));
  const f = figures(plain.asked);
  // A tick-box screen is one step, read as its heading and labels; every other question is a step read as its prompt.
  const screens = new Map<number, Asked[]>();
  for (const a of plain.asked) screens.set(a.step, [...(screens.get(a.step) ?? []), a]);
  assert.equal(f.steps, screens.size);
  assert.equal(f.steps, plain.asked.at(-1)!.step, "steps are numbered from 1 with no gap");
  assert.equal(f.prompt, [...screens.values()].reduce((n, boxes) => n + (boxes[0]!.tick ? words(boxes[0]!.tick.heading) + boxes.reduce((m, b) => m + words(b.tick!.label), 0) : words(boxes[0]!.shown.prompt)), 0));
  for (const boxes of screens.values()) {
    assert.ok(boxes.length === 1 ? !boxes[0]!.tick : boxes.every((b) => b.tick?.group === boxes[0]!.tick?.group && b.shown.type === "Bool"), "a step of several questions is one tick-box group's");
    if (boxes.length > 1) assert.ok(renderTranscript(plain).includes(`### ${boxes[0]!.n}–${boxes.at(-1)!.n}. Tick-boxes \`${boxes[0]!.tick!.group}\`: ${boxes.length} questions on one screen`), "a tick-box screen is printed once");
  }
  assert.equal(f.switches, plain.asked.filter((a, i) => i > 0 && a.topic.id !== plain.asked[i - 1]!.topic.id).length);
  assert.ok(f.switches >= f.topics - 1 && f.returns === f.switches - (f.topics - 1), "every switch opens a new topic or returns to one already left");
  assert.ok(!plain.asked[0]!.switched, "the first question is not a switch");

  // 1. A stale answer: an id that names no question (a renamed question), and a question this walk never asks.
  assert.match(problemsOf({ "nosuch.question": true }), /^persona planted: STALE ANSWER: nosuch\.question names no question of the interview \(no question nosuch\.question\): it was renamed, split or removed/);
  const personal = bg.find((s) => /^person\[taxpayer\]\./.test(s.input))!;
  assert.match(problemsOf({ [personal.input.replace("[taxpayer]", "[nobody]")]: personal.value }), /persona planted: STALE ANSWER: person\[nobody\]\..* is never asked on this walk \(it completed the return after \d+ answers\).* The walk asked person\[taxpayer\]\./);
  assert.match(problemsOf({ [questionTemplate(personal.input)]: personal.value }), /STALE ANSWER: .* a persona names the question's exact id, with its entries\./);

  // 2. An opened and unanswered question: a list the background leaves empty is given an entry, whose questions only
  // this filer is asked. The walk goes on to its end, each such question flagged with the answer that opened it.
  const roster = bg.find((s) => s.input.startsWith("$") && Array.isArray(s.value) && s.value.length === 0 && !config.questions.find((q) => q.input === questionTemplate(s.input))?.choices);
  assert.ok(roster, "the background return leaves an open list empty");
  const opened = walkPersona(w, persona({ [roster!.input]: ["planted"] }));
  const flagged = opened.asked.filter((a) => a.from === "unanswered");
  assert.ok(flagged.length > 0 && opened.problems.length === flagged.length, "each opened and unanswered question is a problem");
  assert.match(opened.problems[0]!, /^persona planted: OPENED AND UNANSWERED: question \d+, .*, is asked of this filer and the persona does not answer it .*It was opened by question \d+, .* = \["planted"\] \(the persona's answer\)\. The walk gave it the closed answer .*; add the answer this filer gives/);
  assert.ok(opened.end.kind === "complete" || opened.end.kind === "refused", "the walk still ends");
  assert.ok(opened.asked.length > bg.length);
  const text = renderTranscript(opened);
  assert.ok(text.includes("## PROBLEMS WITH THIS PERSONA") && text.includes("**OPENED AND UNANSWERED**"), "the transcript carries the problems and marks the question");
  assert.ok(/^.{2}!\s*\d+  /m.test(text), "the one-line listing marks it");
  // Answered by the persona, the same question is not flagged.
  const first = flagged[0]!;
  assert.ok(!walkPersona(w, persona({ [roster!.input]: ["planted"], [first.shown.input]: first.value })).problems.some((p) => p.includes(`question ${first.n}, ${first.shown.input},`)));

  // 3. The end. A yes/no question of the background return whose yes refuses the return at once.
  const grouped = new Set(config.questions.filter((q) => q.group !== undefined).map((q) => q.input));
  const refusing = bg.map((s, i) => ({ s, i })).filter(({ s }) => s.value === false && !grouped.has(questionTemplate(s.input))).map(({ s, i }) => {
    const before: Inputs = Object.fromEntries(bg.slice(0, i).map((b) => [b.input, b.value]));
    const view = interviewView(ctx.data, config, { ...replay(config, [{ version: 1, tax_year: config.tax_year }]), ...before, [s.input]: true });
    // A refusal, not a stop for conflicting answers (a consistency check), which the summary words differently.
    const gate = view.status === "refused" ? (view.refusal as { gate: string }).gate : null;
    return gate !== null && !(templateKey(gate) in ctx.conflicts) && i + 1 < bg.length ? { input: s.input, n: i + 1, next: bg[i + 1]!, gate } : null;
  }).find((r) => r !== null);
  assert.ok(refusing, "the background return has a yes/no question whose yes refuses the return");
  const { input: Q, gate: GATE, n: N, next: NEXT } = refusing!;
  const refused = walkPersona(w, persona({ [Q]: true }, { refused: GATE }));
  assert.deepEqual(refused.problems, []);
  assert.equal(refused.asked.length, N, "the walk ends at the refusal");
  assert.ok(refused.end.kind === "refused" && refused.end.gate === GATE && refused.end.remedy.length > 0);
  assert.ok(renderTranscript(refused).includes(`at the gate \`${GATE}\`, after ${N} questions. The wording shown:`));
  assert.match(problemsOf({ [Q]: true }, "complete"), /persona planted: expected the return to be completed; the walk was refused at /);
  assert.match(problemsOf({ [Q]: false }, { refused: GATE }), /persona planted: expected a refusal at .*; the walk completed the return after \d+ answers/);
  assert.match(problemsOf({ [Q]: true, [NEXT.input]: NEXT.value }, { refused: GATE }), /STALE ANSWER: .* is never asked on this walk \(it was refused at /);

  // 4. An answer the interview rejects: a yes/no question given a number.
  assert.match(problemsOf({ [Q]: 7 }), /persona planted: the interview rejects the answer 7 to .* \(the persona's answer\), after \d+ answers/);

  // The summary has a row per persona, with its end and its problems.
  const summary = renderSummary([plain, refused, opened]);
  assert.ok(summary.includes(`| \`planted\` | ${bg.length} | ${f.steps} | ${f.prompt} | ${f.help} |`) && summary.includes(`refused at \`${GATE}\``) && summary.includes(`| ${opened.problems.length} |`));
  console.log(`draft-walk self-test: passed (persona files, 5 malformed; the baseline is not overwritten; on the built interview, planted on ${Q} and ${roster!.input}: a plain walk of ${bg.length} questions on ${f.steps} screens, ${[...screens.values()].filter((b) => b.length > 1).length} of them tick-box screens; a stale answer, 3 cases; an opened and unanswered question, ${flagged.length} flagged, and answered; the end, 4 cases; a rejected answer; the summary)`);
  return 0;
}
