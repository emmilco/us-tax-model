// Tick-box groups: a few related yes or no questions shown as one screen of tick-boxes (docs/provisional/lanes/tick.md,
// interview/README.md "Tick-box groups"). Presentation only: each member stays its own input, with its own answer in
// the log. The bank declares a group once (`groups`: an id and a heading) and a question joins it by naming it
// (`group`) with the words shown beside its box (`tick`).
//
// This module holds what the build refuses in a declaration (`tickGroupProblems`, run by build.ts on the whole bank).
// tick-groups-check.ts checks the groups of the built interview on a walk.
import { refsOf } from "./gates.js";
import { entrySyntax } from "./interview.js";
import { personWordingProblems, spousePhraseNearMisses } from "./spouse-wording.js";
import type { Expr, Line } from "./types.js";

/** A group has at least GROUP_MIN and at most GROUP_MAX members; a label has at most LABEL_MAX_WORDS words and a
 * heading (without its collection's frame) at most HEADING_MAX_WORDS. */
export const GROUP_MIN = 2;
export const GROUP_MAX = 6;
export const LABEL_MAX_WORDS = 12;
export const HEADING_MAX_WORDS = 25;
const GROUP_ID = /^[a-z][a-z0-9_]*$/;

/** The words of a text, as `words` of interview-words.ts counts them. */
const wordCount = (text: string): number => text.split(/\s+/).filter((t) => /[\p{L}\p{N}]/u.test(t)).length;

/** A bank question as the group rules read it; `group` and `tick` are as the bank file gives them. */
export interface GroupQuestion { input: string; order: number; seq?: number; group?: unknown; tick?: unknown }
/** What the rules need to know of the form data: an input line's type, the form it belongs to (its id, whether the
 * form is a list's, and the frame the bank puts before its questions), and the gated inputs an input opens. */
export interface GroupFacts {
  typeOf: (input: string) => string | undefined;
  formOf: (input: string) => { id: string; collection: boolean; frame: string } | undefined;
  opens: (input: string) => string[];
}

/** For each input, the gated inputs it opens: those whose gate's guards read it, directly or through what Bool lines
 * compute (a guard that reads an amount figured from many answers is not an answer opening a question). A derived
 * refusal screen (a computed line that some line's refusal list refuses on) is not read through, and neither is a
 * refusal list: a yes that only refuses the return at a screen the gate stands behind opens nothing. */
export function opensMap(docs: { lines: Line[] }[]): Map<string, string[]> {
  const lines = new Map(docs.flatMap((d) => d.lines.map((l) => [l.id, l] as const)));
  const screens = new Set(docs.flatMap((d) => d.lines.flatMap((l) => (l.refuses ?? []).map((r) => r.when))));
  const out = new Map<string, string[]>();
  for (const d of docs) for (const l of d.lines) {
    if (!l.gated_by) continue;
    const gate = lines.get(l.gated_by);
    if (gate?.expr.op !== "choose") continue;
    const seen = new Set<string>();
    const visit = (ref: string): void => {
      if (seen.has(ref)) return;
      seen.add(ref);
      const x = lines.get(ref);
      if (!x || x.expr.op === "input" || x.type !== "Bool" || screens.has(ref)) return;
      for (const r of refsOf(x.expr)) visit(r);
      if (x.shown_when) visit(x.shown_when);
    };
    for (const a of (gate.expr as Extract<Expr, { op: "choose" }>).alternatives) for (const r of refsOf(a.guard)) visit(r);
    for (const ref of seen) {
      if (ref === l.id || lines.get(ref)?.expr.op !== "input") continue;
      out.set(ref, [...(out.get(ref) ?? []), l.id]);
    }
  }
  return out;
}

/** What the build refuses in the bank's tick-box groups; each problem names the group or the question. */
export function tickGroupProblems(groups: unknown, questions: GroupQuestion[], facts: GroupFacts): string[] {
  const problems: string[] = [];
  const declared = new Map<string, string>();
  if (groups !== undefined && !Array.isArray(groups)) return ["question bank: groups must be a list of {id, heading}"];
  for (const g of (groups ?? []) as { id?: unknown; heading?: unknown }[]) {
    if (!g || typeof g !== "object" || typeof g.id !== "string" || !GROUP_ID.test(g.id) || Object.keys(g).some((k) => k !== "id" && k !== "heading")) {
      problems.push(`question bank: a group is {id, heading}, its id lower-case letters, digits and "_" (${JSON.stringify(g)})`);
      continue;
    }
    const where = `group ${g.id}`;
    if (declared.has(g.id)) { problems.push(`${where}: declared twice`); continue; }
    declared.set(g.id, typeof g.heading === "string" ? g.heading : "");
    if (typeof g.heading !== "string" || g.heading.trim() === "" || g.heading !== g.heading.trim() || g.heading.includes("\n")) { problems.push(`${where}: the heading must be one non-empty line`); continue; }
    if (wordCount(g.heading) > HEADING_MAX_WORDS) problems.push(`${where}: the heading has ${wordCount(g.heading)} words; at most ${HEADING_MAX_WORDS}`);
    const syntax = entrySyntax(g.heading);
    if (syntax) problems.push(`${where}: the heading states entry syntax (${syntax}); say what to answer, not how to type it`);
    for (const miss of spousePhraseNearMisses(g.heading)) problems.push(`${where}: the heading has a near-miss of the spouse phrase ("${miss}")`);
  }
  const membersOf = new Map<string, GroupQuestion[]>();
  for (const q of questions) {
    const where = `question ${q.input}`;
    if (q.group === undefined) { if (q.tick !== undefined) problems.push(`${where}: tick is the label of a member of a tick-box group; the question names no group`); continue; }
    if (typeof q.group !== "string" || !declared.has(q.group)) { problems.push(`${where}: group ${JSON.stringify(q.group)} is not declared in the bank's groups`); continue; }
    membersOf.set(q.group, [...(membersOf.get(q.group) ?? []), q]);
    if (q.input.startsWith("$") || facts.typeOf(q.input) !== "Bool") problems.push(`${where}: a member of a tick-box group is a yes or no question; this input is ${q.input.startsWith("$") ? "a list" : facts.typeOf(q.input) ?? "undeclared"}`);
    if (typeof q.tick !== "string" || q.tick.trim() === "" || q.tick !== q.tick.trim() || q.tick.includes("\n")) { problems.push(`${where}: a member of a tick-box group needs tick, the few plain words shown beside its box, on one line`); continue; }
    if (wordCount(q.tick) > LABEL_MAX_WORDS) problems.push(`${where}: the tick label has ${wordCount(q.tick)} words; at most ${LABEL_MAX_WORDS}`);
    if (q.tick.endsWith("?")) problems.push(`${where}: the tick label is a question; the heading asks, a label states the fact ticked`);
    const syntax = entrySyntax(q.tick);
    if (syntax) problems.push(`${where}: the tick label states entry syntax (${syntax})`);
    for (const miss of spousePhraseNearMisses(q.tick)) problems.push(`${where}: the tick label has a near-miss of the spouse phrase ("${miss}")`);
    const frame = facts.formOf(q.input)?.frame ?? "";
    for (const p of personWordingProblems({ prompt: frame + q.tick, help: "" })) problems.push(`${where}: shown for the spouse or the taxpayer, the tick label is not covered: ${p}`);
  }
  for (const [id] of declared) if (!membersOf.has(id)) problems.push(`group ${id}: no question names it`);
  for (const [id, members] of membersOf) {
    const where = `group ${id}`;
    const names = members.map((m) => m.input).join(", ");
    if (members.length < GROUP_MIN || members.length > GROUP_MAX) problems.push(`${where}: ${members.length} member${members.length === 1 ? "" : "s"} (${names}); a group has ${GROUP_MIN} to ${GROUP_MAX}`);
    const labels = members.map((m) => m.tick).filter((t): t is string => typeof t === "string");
    if (new Set(labels).size !== labels.length) problems.push(`${where}: two members have the same tick label`);
    // One screen is asked of one entry: the members are inputs of one form, or all of forms asked once per return.
    const forms = members.map((m) => facts.formOf(m.input));
    if (forms.some((f) => f === undefined)) continue;
    if (new Set(forms.map((f) => f!.id)).size > 1 && forms.some((f) => f!.collection)) problems.push(`${where}: its members (${names}) are of several forms, one of them a list's; a group is of one form, or of forms asked once per return`);
    const frame = forms[0]!.frame;
    for (const p of personWordingProblems({ prompt: frame + declared.get(id)!, help: "" })) problems.push(`${where}: shown for the spouse or the taxpayer, the heading is not covered: ${p}`);
    // Side by side in one topic: one order number, and stated places (`seq`) with no other question's place between
    // the lowest and the highest, so that no other question is asked among the members (the numbers themselves may
    // leave gaps: 10, 20, 30). Stating a `seq` is also what opens a member as soon as the return needs it, whatever
    // refusal screen stands ahead of it in its form (the reach pass of interview.ts). The other questions of the order
    // number need not state one: a question without `seq` is asked after those with one.
    const order = members[0]!.order;
    if (members.some((m) => m.order !== order)) { problems.push(`${where}: its members (${names}) have different order numbers; a group is of one order number`); continue; }
    if (members.some((m) => m.seq === undefined)) { problems.push(`${where}: a member has no seq; each member states its place in the topic`); continue; }
    const seqs = members.map((m) => m.seq!).sort((a, b) => a - b);
    const last = seqs.at(-1)!;
    const block = questions.filter((q) => q.order === order);
    for (const q of block) if (!members.includes(q) && q.seq !== undefined && q.seq >= seqs[0]! && q.seq <= last) problems.push(`${where}: question ${q.input} (seq ${q.seq}) lies among its members' seq numbers (${seqs.join(", ")}) and is not a member`);
    // A group does not hold a question and the question its yes opens. Where the other questions a member opens
    // stand is not a declaration rule: the walk of tick-groups-check.ts checks when they are asked.
    for (const m of members) for (const c of facts.opens(m.input)) if (members.some((x) => x.input === c)) problems.push(`${where}: member ${c} is asked only after member ${m.input} is answered yes; a group does not hold a question and the question its yes opens`);
  }
  return problems;
}
