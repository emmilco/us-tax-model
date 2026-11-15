// The order the interview asks its questions in, measured (`interview-order`). Deterministic and free: it walks
// returns with the evaluator in the interview's own order (the question `interviewStatus` picks) and calls no model.
//
// A walk ends as the page's does, when the return is complete or refused. For each question asked it records the
// bank's `order` number, the form the question belongs to, and the step at which the question became reachable. From
// that, per walk:
//
//   runs            the walk as a sequence of (order number, form) runs
//   re-entries      every place an order number, or a form, is left and later entered again, with the cause:
//                     sorting   the question that re-enters and the question asked when the topic was left were both
//                               reachable, and the bank's order put the other first; or the topic was left for a
//                               child of its last question that the bank places in another topic
//                     late      a question became reachable only part-way: either the question that re-enters (it was
//                               not reachable when its topic was left) or the question the topic was left for (it
//                               sorts earlier and had not been reachable until then). The entry names that question
//                               and the answer after which it first became reachable (what it was waiting on), and
//                               says whether that answer is one its own gate reads (its parent) or not (it was held
//                               back in evaluation)
//   delayed children  every gated question not asked directly after the yes/no question that opened it: between the
//                     two, a question that is no descendant of that parent was asked. Same two causes.
//
// A question's parents are the yes/no inputs its gate line's guards read, directly or through yes/no helper lines; of
// several, the one asked last is the one that opened it. A question of a collection entry also waits on the roster
// that lists the entry; a wait on it counts as a wait on a parent, but the roster's entry questions are not counted as
// its delayed children (a person's questions lie in many topics). A question's form is the document of its input line
// (a roster's, its collection).
//
// The report also reads the bank alone (no walk): how many questions of each order number state a `seq`, and every
// gated question the bank does not place directly after its parent.
//
// Returns: the whole-return fixtures, the generated returns and the minimal returns (every gate closed, then each
// existence gate opened alone), all in the `full` profile; or, with --returns, the cases of a fixture file.
//
//   interview-order [--write FILE] [--returns FILE] [--generated N] [--no-reach | --reach-all] [--strict] | --self-test
//     --write FILE    writes the report to FILE (Markdown) as well as the summary to the terminal
//     --returns FILE  walks the cases of FILE ({cases: [{id, inputs}]}, a fixture file's form) instead
//     --generated N   how many generated returns to walk (default 12, those of interview-length)
//     --no-reach      walks without the reach pass (interview.ts, `neededInputs`): a question is then open only once
//                     the evaluation proper reaches it, as before the pass existed. For comparison only
//     --reach-all     walks with the reach pass applied to every question, as if each stated a `seq` (the interview
//                     applies it only to those that do). For comparison only: what the pass would open, bank unchanged
//     --strict        exits 1 when any walk re-enters an order number or delays a child
//     --self-test     the asking order (`askOrder`, `blockPlaces`) and the reach pass (`inputsAhead`) on small cases
import assert from "node:assert/strict";
import { readFileSync, writeFileSync } from "node:fs";
import { basename, resolve } from "node:path";
import { answerEvent, askOrder, blockPlaces, inputMeta, interviewStatus, placeOf, questionTemplate, recordedTemplates, type InterviewData, type Place, type Reach } from "./interview.js";
import { evaluate, inputsAhead } from "./eval.js";
import { SEED, existenceGates, fixtureCases, minimalAnswers, replayedState, type Answers, type Event } from "./interview-rules.js";
import { context } from "./interview-length.js";
import { sampleReturns } from "./generate.js";
import { resolveCase } from "./fixture-inputs.js";
import { gatesOf, readsOf } from "./gates.js";
import type { CanonicalData, Inputs, Line } from "./types.js";

const BOUND = 800;

/** One question asked. `since`: the first step from which it was reachable without a break until it was asked (0: from
 * the start); the answer given at step `since - 1` is the one it was waiting on. */
export interface Asked { step: number; key: string; template: string; form: string; order: number; seq?: number; since: number }
export interface OrderWalk { asked: Asked[]; status: string; stopped?: string }

/** The form a question belongs to: its input line's document; a roster's, its collection. */
export function formOf(template: string): string {
  return template.startsWith("$") ? template.slice(1) : template.slice(0, template.indexOf("."));
}

/** The entry a key lies in (`person[taxpayer].w2[acme]` for a line of that W-2; for the roster `$w2@person[taxpayer]`,
 * `person[taxpayer]`), or "" at top level. */
export function entryPath(key: string): string {
  if (key.startsWith("$")) return key.includes("@") ? key.slice(key.indexOf("@") + 1) : "";
  const m = /^((?:[a-zA-Z0-9_]+\[[^\]]+\]\.)*)/.exec(key)![1]!;
  return m.replace(/\.$/, "");
}
/** The roster key that lists the last entry of a path, or null at top level. */
export function rosterOf(path: string): string | null {
  if (!path) return null;
  const cut = path.lastIndexOf(".", path.lastIndexOf("["));
  const parent = cut < 0 ? "" : path.slice(0, cut);
  const coll = path.slice(cut + 1, path.lastIndexOf("["));
  return `$${coll}${parent ? "@" + parent : ""}`;
}

/** Each gated input's parents, by template: the yes/no inputs its gate's guards read, directly or through yes/no
 * lines that are not inputs. */
export function gateParents(data: CanonicalData): Map<string, string[]> {
  const lines = new Map<string, Line>([...data.forms, ...data.defs].flatMap((d) => d.lines.map((l) => [l.id, l] as const)));
  const out = new Map<string, string[]>();
  for (const g of gatesOf(data)) {
    const parents = new Set<string>();
    const seen = new Set<string>();
    const visit = (ref: string) => {
      if (seen.has(ref)) return;
      seen.add(ref);
      const line = lines.get(ref);
      if (!line || line.type !== "Bool") return;
      if (line.expr.op === "input") { parents.add(ref); return; }
      for (const r of readsOf(line)) visit(r);
    };
    for (const r of g.guardRefs) visit(r);
    out.set(g.input, [...parents].sort());
  }
  return out;
}

/** Walks a return in the interview's own order to completion or refusal. */
export function walkOrder(data: CanonicalData, config: InterviewData, answers: Answers, reach: Reach = "stated"): OrderWalk {
  const bank = new Map(config.questions.map((q) => [q.input, q]));
  const recorded = recordedTemplates(config);
  let state = replayedState(config, []);
  const events: Event[] = [];
  const asked: Asked[] = [];
  let since = new Map<string, number>();
  for (let step = 0; step <= BOUND; step++) {
    const st = interviewStatus(data, config, state.inputs, { reach });
    if (st.status !== "incomplete") return { asked, status: st.status };
    const open = new Set(st.reachableInputs.map((k) => recorded.get(questionTemplate(k)) ?? k));
    since = new Map([...open].map((k) => [k, since.get(k) ?? step]));
    const key = st.question!.input;
    const answer = answers(key, state.inputs);
    if (!answer) return { asked, status: "not walkable", stopped: key };
    const template = questionTemplate(key);
    const q = bank.get(template)!;
    asked.push({ step, key, template, form: formOf(template), order: q.order, ...(q.seq !== undefined ? { seq: q.seq } : {}), since: since.get(key)! });
    if (key !== [...open].map((k) => placeOf(bank.get(questionTemplate(k))!, k)).sort(askOrder)[0]!.input) throw new Error(`${key}: not the first open question in asking order`);
    events.push(answerEvent(config, state, key, answer.value));
    state = replayedState(config, events);
  }
  throw new Error("the walk did not end");
}

export interface Finding {
  kind: "order" | "form" | "child";
  cause: "sorting" | "late";
  /** The question that re-enters, or the delayed child. */
  q: Asked;
  /** order/form: the step after which the topic was left. child: the parent. */
  left: number; parent?: Asked;
  /** How many questions of other topics (child: that are no descendant of the parent) were asked in between. */
  between: number;
  /** late: the question that became reachable part-way (`q`, or the question its topic was left for), the question
   * whose answer it was waiting on, and whether that question is one of its parents. */
  culprit?: Asked; waitedOn?: Asked; waitedOnParent?: boolean;
  /** sorting: what the bank's order put first; `childOfLast`: it is a child of the topic's last question. */
  first?: Asked; childOfLast?: boolean;
}

export function findings(w: OrderWalk, parents: Map<string, string[]>): Finding[] {
  const out: Finding[] = [];
  const { asked } = w;
  const byKey = new Map(asked.map((a) => [a.key, a]));
  const pathIn = (inner: string, outer: string) => outer === "" || inner === outer || inner.startsWith(outer + ".");
  /** The asked parents of a question: its gate's, in an entry that encloses its own. */
  const gateParentsOf = (a: Asked): Asked[] => (parents.get(a.template) ?? []).flatMap((t) =>
    asked.filter((p) => p.template === t && p.step < a.step && pathIn(entryPath(a.key), entryPath(p.key))));
  const ancestorMemo = new Map<string, Set<string>>();
  const ancestors = (a: Asked): Set<string> => {
    const hit = ancestorMemo.get(a.key);
    if (hit) return hit;
    const set = new Set<string>();
    ancestorMemo.set(a.key, set);
    const roster = rosterOf(entryPath(a.key));
    const ups = [...gateParentsOf(a), ...(roster && byKey.has(roster) ? [byKey.get(roster)!] : [])];
    for (const p of ups) { set.add(p.key); for (const k of ancestors(p)) set.add(k); }
    return set;
  };
  const isParent = (q: Asked, other: Asked | undefined) => !!other && (gateParentsOf(q).some((p) => p.key === other.key) || rosterOf(entryPath(q.key)) === other.key);
  const late = (q: Asked) => ({ culprit: q, waitedOn: asked[q.since - 1]!, waitedOnParent: isParent(q, asked[q.since - 1]) });

  for (const kind of ["order", "form"] as const) {
    const topic = (a: Asked) => (kind === "order" ? String(a.order) : a.form);
    const lastSeen = new Map<string, number>();
    for (let j = 0; j < asked.length; j++) {
      const q = asked[j]!;
      const t = topic(q);
      const e = lastSeen.get(t);
      if (e !== undefined && e < j - 1) {
        const base = { kind, q, left: e, between: j - 1 - e };
        const x = asked[e + 1]!;
        if (q.since > e + 1) out.push({ ...base, cause: "late", ...late(q) });
        else if (x.since <= e) out.push({ ...base, cause: "sorting", first: x });
        else if (isParent(x, asked[e])) out.push({ ...base, cause: "sorting", first: x, childOfLast: true });
        else out.push({ ...base, cause: "late", ...late(x) });
      }
      lastSeen.set(t, j);
    }
  }
  for (let j = 0; j < asked.length; j++) {
    const q = asked[j]!;
    const ps = gateParentsOf(q);
    if (!ps.length) continue;
    const parent = ps.reduce((a, b) => (b.step > a.step ? b : a));
    const strangers = asked.slice(parent.step + 1, j).filter((x) => !ancestors(x).has(parent.key));
    if (!strangers.length) continue;
    const base = { kind: "child" as const, q, left: parent.step, parent, between: strangers.length };
    if (q.since <= parent.step + 1) out.push({ ...base, cause: "sorting", first: strangers[0]! });
    else out.push({ ...base, cause: "late", ...late(q) });
  }
  return out;
}

/** The walk as runs of (order number, form). */
export function runsOf(asked: Asked[]): { order: number; form: string; n: number }[] {
  const runs: { order: number; form: string; n: number }[] = [];
  for (const a of asked) {
    const last = runs.at(-1);
    if (last && last.order === a.order && last.form === a.form) last.n++;
    else runs.push({ order: a.order, form: a.form, n: 1 });
  }
  return runs;
}

const place = (a: Asked) => `order ${a.order}${a.seq !== undefined ? ` seq ${a.seq}` : ""}`;
function describe(f: Finding): string {
  const what = f.kind === "child"
    ? `\`${f.q.key}\` (${place(f.q)}), step ${f.q.step + 1}: child of \`${f.parent!.key}\` (step ${f.parent!.step + 1}), ${f.between} other question${f.between === 1 ? "" : "s"} between`
    : `${f.kind === "order" ? `order ${f.q.order}` : `form ${f.q.form}`} re-entered at step ${f.q.step + 1} by \`${f.q.key}\` (${place(f.q)}), left after step ${f.left + 1}, ${f.between} between`;
  if (f.cause === "sorting" && f.childOfLast) return `${what}. Sorting: left for \`${f.first!.key}\` (${place(f.first!)}), a child of the question before it, which the bank places in another ${f.kind === "order" ? "order number" : "form"}.`;
  if (f.cause === "late" && f.culprit !== f.q) {
    const x = f.culprit!;
    return `${what}. Late: left for \`${x.key}\` (${place(x)}), which sorts earlier and was reachable only after the answer to \`${f.waitedOn!.key}\` (step ${f.waitedOn!.step + 1}), ${f.waitedOnParent ? "its parent or roster" : "which its gate does not read"}.`;
  }
  if (f.cause === "sorting") {
    const o = f.first!;
    const why = o.order !== f.q.order ? `the bank puts ${place(o)} first` : f.q.seq !== undefined && o.seq !== undefined ? `within order ${o.order}, the block's entry and seq order put it first` : `within order ${o.order}, sorted by id`;
    return `${what}. Sorting: it was reachable (since step ${f.q.since + 1}), and \`${o.key}\` was asked instead (${why}).`;
  }
  const a = f.waitedOn!;
  return `${what}. Late: reachable only after the answer to \`${a.key}\` (step ${a.step + 1}), ${f.waitedOnParent ? "its parent or roster" : "which its gate does not read"}.`;
}

/** What the bank alone states. `seqs`: per order number, its questions, how many state a `seq`, and its forms.
 * `misplaced`: each gated question the bank does not place directly after its parent (the last of its parents in
 * asking order), with the reason. Between a parent and its child only the parent's descendants may stand: questions
 * gated by it, and the entry questions of a roster among them. */
export function bankPlacement(config: InterviewData, parents: Map<string, string[]>): { seqs: { order: number; n: number; withSeq: number; forms: string[] }[]; misplaced: { child: string; parent: string; why: string }[] } {
  const sorted = [...config.questions].sort(askOrder);
  const index = new Map(sorted.map((q, i) => [q.input, i]));
  const collections = new Set(config.questions.filter((q) => q.input.startsWith("$")).map((q) => q.input.slice(1)));
  const memo = new Map<string, Set<string>>();
  const ancestors = (t: string): Set<string> => {
    const hit = memo.get(t);
    if (hit) return hit;
    const set = new Set<string>();
    memo.set(t, set);
    const ups = [...(parents.get(t) ?? [])];
    if (!t.startsWith("$") && collections.has(formOf(t))) ups.push("$" + formOf(t));
    for (const p of ups) { set.add(p); for (const k of ancestors(p)) set.add(k); }
    return set;
  };
  const misplaced: { child: string; parent: string; why: string }[] = [];
  for (const q of sorted) {
    const ps = (parents.get(q.input) ?? []).filter((p) => index.has(p));
    if (!ps.length) continue;
    const parent = ps.reduce((a, b) => (index.get(b)! > index.get(a)! ? b : a));
    const p = sorted[index.get(parent)!]!;
    const between = sorted.slice(index.get(parent)! + 1, index.get(q.input)!).filter((x) => !ancestors(x.input).has(parent));
    const why = p.order !== q.order ? `the parent is in order ${p.order} and the child in order ${q.order}`
      : index.get(parent)! > index.get(q.input)! ? "the child comes before the parent"
      : between.length ? `${between.length} question${between.length === 1 ? "" : "s"} that the parent does not open stand between them (the first: \`${between[0]!.input}\`)` : "";
    if (why) misplaced.push({ child: q.input, parent, why });
  }
  const seqs = [...new Set(sorted.map((q) => q.order))].map((order) => {
    const qs = sorted.filter((q) => q.order === order);
    return { order, n: qs.length, withSeq: qs.filter((q) => q.seq !== undefined).length, forms: [...new Set(qs.map((q) => formOf(q.input)))].sort() };
  });
  return { seqs, misplaced };
}

interface Measured { group: string; id: string; w: OrderWalk; found: Finding[] }
const COUNTS = [["order", "sorting"], ["order", "late"], ["form", "sorting"], ["form", "late"], ["child", "sorting"], ["child", "late"]] as const;
const count = (found: Finding[], kind: string, cause: string) => found.filter((f) => f.kind === kind && f.cause === cause).length;
const signature = (f: Finding) => `${f.kind}|${f.cause}|${f.q.template}|${f.culprit?.template ?? ""}|${f.waitedOn?.template ?? f.first?.template ?? ""}`;

export function renderOrderReport(measured: Measured[], source: string, bank: ReturnType<typeof bankPlacement>): string {
  const out: string[] = [
    "# The interview's asking order, measured",
    "",
    `Written by \`node engine/dist/main.js interview-order --write\` (engine/src/interview-order.ts; deterministic, no model calls). Returns walked: ${source}.`,
    "",
    "Each return is walked in the interview's own order to completion or refusal. A *re-entry* is a place where an order number",
    "(or a form) is left and later entered again. A *delayed child* is a gated question not asked directly after the yes/no question",
    "that opened it (a question that is no descendant of that parent was asked between them). Causes: **sorting**, the question was",
    "already reachable and the bank's order put another first, or a topic was left for a child that the bank places in another",
    "topic; **late**, a question became reachable only part-way (the one that re-enters, or an earlier-sorted one the topic was left",
    "for), and the entry names the answer it was waiting on. A question's order number is the first thing the interview sorts by,",
    "so an order number is re-entered for the late cause, or for a child with a lower order number than its parent.",
    "",
    "## Totals",
    "",
    "| returns | walks | questions (mean) | order re-entries: sorting | late | form re-entries: sorting | late | delayed children: sorting | late |",
    "|---|---|---|---|---|---|---|---|---|",
  ];
  const groups = [...new Set(measured.map((m) => m.group))];
  for (const g of groups) {
    const ms = measured.filter((m) => m.group === g);
    const mean = ms.reduce((s, m) => s + m.w.asked.length, 0) / ms.length;
    out.push(`| ${g} | ${ms.length} | ${mean.toFixed(1)} | ${COUNTS.map(([k, c]) => (ms.reduce((s, m) => s + count(m.found, k, c), 0) / ms.length).toFixed(1)).join(" | ")} |`);
  }
  out.push("", "The counts are means per walk.", "");

  out.push("## What the late questions waited on", "", "Every late finding, by the question that became reachable part-way and the answer it waited on, with the number of walks showing it", "and what it caused (an order number re-entered, a form re-entered, a child delayed).", "",
    "| question | waited on | its parent or roster? | caused | walks |", "|---|---|---|---|---|");
  const agg = new Map<string, { q: string; on: string; parent: boolean; kinds: Set<string>; walks: Set<string> }>();
  for (const m of measured) for (const f of m.found) {
    if (f.cause !== "late") continue;
    const k = `${f.culprit!.template}|${f.waitedOn!.template}`;
    const row = agg.get(k) ?? agg.set(k, { q: f.culprit!.template, on: f.waitedOn!.template, parent: !!f.waitedOnParent, kinds: new Set(), walks: new Set() }).get(k)!;
    row.kinds.add(f.kind);
    row.walks.add(`${m.group}/${m.id}`);
  }
  for (const r of [...agg.values()].sort((a, b) => b.walks.size - a.walks.size || a.q.localeCompare(b.q))) out.push(`| \`${r.q}\` | \`${r.on}\` | ${r.parent ? "yes" : "no"} | ${[...r.kinds].sort().join(", ")} | ${r.walks.size} |`);
  out.push("");

  out.push("## Delayed children for the sorting cause", "", "By child and parent, with the number of walks.", "", "| child | place | parent | place | walks |", "|---|---|---|---|---|");
  const sorted = new Map<string, { q: Asked; p: Asked; walks: number }>();
  for (const m of measured) for (const k of new Set(m.found.filter((f) => f.kind === "child" && f.cause === "sorting").map((f) => `${f.q.template}|${f.parent!.template}`))) {
    const f = m.found.find((x) => x.kind === "child" && x.cause === "sorting" && `${x.q.template}|${x.parent!.template}` === k)!;
    const row = sorted.get(k) ?? sorted.set(k, { q: f.q, p: f.parent!, walks: 0 }).get(k)!;
    row.walks++;
  }
  for (const r of [...sorted.values()].sort((a, b) => b.walks - a.walks || a.q.template.localeCompare(b.q.template))) out.push(`| \`${r.q.template}\` | ${place(r.q)} | \`${r.p.template}\` | ${place(r.p)} | ${r.walks} |`);
  out.push("");

  out.push("## What the bank states", "", "Read from the built question bank alone. A question that states no `seq` is asked after those of its order number that do, by id.", "",
    "| order | questions | state a seq | forms |", "|---|---|---|---|");
  for (const r of bank.seqs) out.push(`| ${r.order} | ${r.n} | ${r.withSeq} | ${r.forms.join(", ")} |`);
  out.push("", `Gated questions the bank does not place directly after their parent: ${bank.misplaced.length}.`, "");
  if (bank.misplaced.length) {
    out.push("| child | parent | why |", "|---|---|---|");
    for (const m of bank.misplaced) out.push(`| \`${m.child}\` | \`${m.parent}\` | ${m.why} |`);
    out.push("");
  }

  out.push("## Each walk", "", "A walk's line of runs reads `order:form×questions`. For a minimal return with one gate opened, only the findings the", "every-gate-closed return does not also have are listed.", "");
  const closed = new Set(measured.find((m) => m.id === "every gate closed")?.found.map(signature) ?? []);
  for (const g of groups) {
    out.push(`### ${g}`, "");
    for (const m of measured.filter((x) => x.group === g)) {
      const brief = m.group === "minimal returns" && m.id !== "every gate closed";
      const shown = brief ? m.found.filter((f) => !closed.has(signature(f))) : m.found;
      out.push(`**${m.id}**: ${m.w.asked.length} questions, ${m.w.status}${m.w.stopped ? ` (asks \`${m.w.stopped}\`, which the return does not answer)` : ""}; `
        + `order re-entries ${count(m.found, "order", "sorting") + count(m.found, "order", "late")}, form re-entries ${count(m.found, "form", "sorting")} sorting and ${count(m.found, "form", "late")} late, `
        + `delayed children ${count(m.found, "child", "sorting")} sorting and ${count(m.found, "child", "late")} late.`, "");
      if (!brief) out.push(runsOf(m.w.asked).map((r) => `${r.order}:${r.form}×${r.n}`).join(" · "), "");
      for (const f of shown) out.push(`- ${describe(f)}`);
      if (shown.length) out.push("");
    }
  }
  return out.join("\n") + "\n";
}

/** The asking order and the reach pass on small constructed cases. */
function selfTest(): number {
  let checks = 0;
  // A topic of one order number: a question of the return, the person's W-2 roster, three W-2 questions, a question of
  // the person, a fourth W-2 question, and a last question of the return.
  const bank = [
    { input: "t.first", order: 3, seq: 10 }, { input: "$w2", order: 3, seq: 20 }, { input: "w2.a", order: 3, seq: 30 }, { input: "w2.b", order: 3, seq: 40 },
    { input: "w2.c", order: 3, seq: 50 }, { input: "person.mid", order: 3, seq: 60 }, { input: "w2.d", order: 3, seq: 70 }, { input: "t.last", order: 3, seq: 80 },
    { input: "t.plain_b", order: 3 }, { input: "t.plain_a", order: 3 }, { input: "t.early", order: 2 }, { input: "t.later", order: 4, seq: 1 },
  ];
  const chain = (input: string) => (input.startsWith("$w2") || input.startsWith("person.") ? ["person"] : input.startsWith("w2.") ? ["person", "w2"] : []);
  const at = blockPlaces(bank, chain);
  assert.deepEqual(at.get("$w2"), [20]); assert.deepEqual(at.get("w2.a"), [20, 30]); assert.deepEqual(at.get("w2.c"), [20, 30]);
  assert.deepEqual(at.get("person.mid"), [20]); assert.deepEqual(at.get("w2.d"), [20, 70]); assert.equal(at.get("t.first"), undefined); checks += 6;
  const q = (template: string, key: string): Place => placeOf({ ...bank.find((b) => b.input === template)!, ...(at.has(template) ? { at: at.get(template)! } : {}) }, key);
  const keys: [string, string][] = [["t.early", "t.early"], ["t.first", "t.first"]];
  for (const p of ["spouse", "taxpayer"]) {
    keys.push(["$w2", `$w2@person[${p}]`]);
    for (const w of ["acme", "beta"]) for (const l of ["a", "b", "c"]) keys.push([`w2.${l}`, `person[${p}].w2[${w}].${l}`]);
    keys.push(["person.mid", `person[${p}].mid`]);
    for (const w of ["acme", "beta"]) keys.push(["w2.d", `person[${p}].w2[${w}].d`]);
  }
  keys.push(["t.last", "t.last"], ["t.plain_a", "t.plain_a"], ["t.plain_b", "t.plain_b"], ["t.later", "t.later"]);
  const wanted = keys.map(([t, k]) => q(t, k));
  // Whatever order the open questions come in, they sort to the outline; and the order is a strict total order.
  const mixed = [...wanted].sort((a, b) => (a.input.length * 7 + a.input.charCodeAt(a.input.length - 2)) % 13 - (b.input.length * 7 + b.input.charCodeAt(b.input.length - 2)) % 13);
  assert.deepEqual([...mixed].sort(askOrder).map((x) => x.input), wanted.map((x) => x.input)); checks++;
  assert.deepEqual([...wanted].reverse().sort(askOrder).map((x) => x.input), wanted.map((x) => x.input)); checks++;
  for (let i = 0; i < wanted.length; i++) for (let j = 0; j < wanted.length; j++) {
    assert.equal(Math.sign(askOrder(wanted[i]!, wanted[j]!)), Math.sign(i - j), `${wanted[i]!.input} against ${wanted[j]!.input}`); checks++;
  }
  // The questions of the bank, by template, sort to the bank's stated order (the vetting page's cards).
  assert.deepEqual(bank.map((b) => placeOf({ ...b, ...(at.has(b.input) ? { at: at.get(b.input)! } : {}) }, b.input)).sort(askOrder).map((x) => x.input),
    ["t.early", "t.first", "$w2", "w2.a", "w2.b", "w2.c", "person.mid", "w2.d", "t.last", "t.plain_a", "t.plain_b", "t.later"]); checks++;

  // The reach pass. `r.total` adds `r.held` and `r.cond`. `r.held` (the input `r.amount`) stands behind two refusal
  // gates, `r.g1` and `r.g2`, each an input. `r.cond` is true when `r.first` is true and `r.second` is: `r.second` is
  // the input `r.deep` behind the gate `r.g3`.
  const input = (id: string, type: string, extra: object = {}) => ({ id, printed: "1", label: id, type, expr: { op: "input", source: id }, cite: null, ...extra });
  const refusal = (when: string) => ({ when, form: "x", remedy: "x", cite: null });
  const lines = [
    input("r.g1", "Bool"), input("r.g2", "Bool"), input("r.g3", "Bool"), input("r.first", "Bool"), input("r.deep", "Bool"),
    input("r.amount", "NonNegDollars"),
    { id: "r.held", printed: "2", label: "held", type: "NonNegDollars", expr: { op: "sum", of: ["r.amount"] }, cite: null, refuses: [refusal("r.g1"), refusal("r.g2")] },
    { id: "r.second", printed: "3", label: "second", type: "Bool", expr: { op: "test", eq: ["r.deep", { const: true }] }, cite: null, refuses: [refusal("r.g3")] },
    { id: "r.cond", printed: "4", label: "cond", type: "Bool", expr: { op: "test", all: [{ op: "test", eq: ["r.first", { const: true }] }, { op: "test", eq: ["r.second", { const: true }] }] }, cite: null },
    { id: "r.zero", printed: "0", label: "zero", type: "NonNegDollars", expr: { op: "param", ref: "z" }, cite: null },
    { id: "r.pick", printed: "5", label: "pick", type: "NonNegDollars", expr: { op: "choose", alternatives: [{ guard: { op: "test", eq: ["r.cond", { const: true }] }, then: "r.held" }, { guard: { op: "test", eq: ["r.cond", { const: false }] }, then: "r.zero" }] }, cite: null },
    { id: "r.total", printed: "6", label: "total", type: "NonNegDollars", expr: { op: "sum", of: ["r.held", "r.pick"] }, cite: null },
  ];
  const data = { forms: [{ id: "r", kind: "form", tax_year: 2025, title: "r", lines }], defs: [], tables: [],
    params: { tax_year: 2025, enums: {}, values: { z: { type: "NonNegDollars", value: 0, cite: null } } }, register: { tax_year: 2025, entries: [] } } as unknown as CanonicalData;
  const proper = (inputs: Record<string, unknown>) => [...new Set([...evaluate(data, inputs as Inputs, ["r.total"]).derivations.values()].flatMap((d) => (d.value.kind === "unknown" && d.value.input ? [d.value.input] : [])))].sort();
  const ahead = (inputs: Record<string, unknown>) => [...inputsAhead(data, inputs as Inputs, ["r.total"])].sort();
  // The evaluation proper stops at each line's first unanswered gate, and reads the test's second operand (its gate).
  assert.deepEqual(proper({}), ["r.first", "r.g1", "r.g3"]); checks++;
  // The reach pass reads past r.g1 to r.g2 and the amount; it does not go beneath the operand after the unanswered r.first.
  assert.deepEqual(ahead({}), ["r.amount", "r.first", "r.g1", "r.g2"]); checks++;
  // Once r.first is true, r.second is needed, and what stands behind its gate is read ahead.
  assert.deepEqual(ahead({ "r.first": true }), ["r.amount", "r.deep", "r.g1", "r.g2", "r.g3"]); checks++;
  // A later gate that already refuses: the amount will not be read, whatever r.g1 is.
  assert.deepEqual(ahead({ "r.g2": true }), ["r.first", "r.g1"]); checks++;
  // No value changes: the evaluation proper gives the same values with any of these inputs (it does not take the option).
  for (const inputs of [{}, { "r.g1": false }, { "r.g1": false, "r.g2": false, "r.amount": 500, "r.first": false }]) {
    const a = evaluate(data, inputs as Inputs, ["r.total"]).values.get("r.total");
    const kind = Object.keys(inputs).length === 4 ? "money" : "unknown";
    assert.equal(a!.kind, kind); checks++;
  }
  console.log(`interview-order self-test: ${checks} checks passed (the outline order of asking, the places of entry runs, the reach pass)`);
  return 0;
}

export async function interviewOrder(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  const arg = (name: string) => { const i = args.indexOf(name); return i < 0 ? undefined : args[i + 1]; };
  const ctx = context();
  const { data } = ctx;
  const config = ctx.configs["full"]!;
  const parents = gateParents(data);
  const returns = arg("--returns");
  let cases: { group: string; id: string; answers: Answers }[];
  if (returns) {
    const file = JSON.parse(readFileSync(resolve(returns), "utf8")) as { cases: { id: string; inputs: Record<string, unknown> }[] };
    cases = file.cases.map((c) => {
      const inputs: Inputs = resolveCase(c, basename(returns), data, "federal");
      return { group: returns, id: c.id, answers: (k: string) => (k in inputs ? { value: inputs[k] } : undefined) };
    });
  } else {
    const fromInputs = (inputs: Inputs): Answers => (k) => (k in inputs ? { value: inputs[k] } : undefined);
    cases = fixtureCases("full", data).map((c) => ({ group: "whole-return fixtures", id: c.id, answers: fromInputs(c.inputs) }));
    sampleReturns(data, Number(arg("--generated") ?? 12), SEED).forEach((inputs, i) => cases.push({ group: "generated returns", id: `generated.${i}`, answers: fromInputs(inputs) }));
    cases.push({ group: "minimal returns", id: "every gate closed", answers: minimalAnswers(data, config, "full", null) });
    for (const g of [...existenceGates(data).keys()].sort()) {
      const meta = inputMeta(data, g);
      for (const value of meta.type === "Bool" ? [true] : meta.type === "Enum" ? meta.values!.slice(1) : [])
        cases.push({ group: "minimal returns", id: `${g} = ${JSON.stringify(value)} alone`, answers: minimalAnswers(data, config, "full", { input: g, value }) });
    }
  }
  const reach: Reach = args.includes("--no-reach") ? "none" : args.includes("--reach-all") ? "all" : "stated";
  const measured: Measured[] = cases.map((c) => {
    const w = walkOrder(data, config, c.answers, reach);
    return { group: c.group, id: c.id, w, found: findings(w, parents) };
  });
  let bad = 0;
  for (const g of [...new Set(measured.map((m) => m.group))]) {
    const ms = measured.filter((m) => m.group === g);
    const sum = (k: string, c: string) => ms.reduce((s, m) => s + count(m.found, k, c), 0);
    console.log(`  ${g}: ${ms.length} walks; order re-entries ${sum("order", "sorting") + sum("order", "late")}; form re-entries ${sum("form", "sorting")} sorting, ${sum("form", "late")} late; delayed children ${sum("child", "sorting")} sorting, ${sum("child", "late")} late`);
    bad += sum("order", "sorting") + sum("order", "late") + sum("child", "sorting") + sum("child", "late");
  }
  const write = arg("--write");
  if (write) {
    writeFileSync(resolve(write), renderOrderReport(measured, (returns ? `the cases of \`${returns}\`` : "the whole-return fixtures, the generated returns and the minimal returns, in the `full` profile")
      + (reach === "none" ? ". Walked with `--no-reach`: without the reach pass, a question is open only once the evaluation proper reaches it"
        : reach === "all" ? ". Walked with `--reach-all`: the reach pass applied to every question, as if each stated a `seq`; not how the interview asks today's bank" : ""), bankPlacement(config, parents)));
    console.log(`  wrote ${write}`);
  }
  const placement = bankPlacement(config, parents);
  console.log(`  bank: ${placement.seqs.reduce((s, r) => s + r.withSeq, 0)} of ${placement.seqs.reduce((s, r) => s + r.n, 0)} questions state a seq; ${placement.misplaced.length} gated question(s) not placed directly after their parent`);
  return args.includes("--strict") && bad ? 1 : 0;
}
