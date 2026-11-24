// The command `spouse-phrase`: the lint of interview/README.md's rule "A joint return combines both spouses' items".
// A question asked once per return (its input's form has no `collection` block; not a roster question) whose prompt
// says "you" or "your", while neither its prompt, its help nor its tick-box group's heading and label has a phrase
// that brings in the spouse, is a hit: a joint filer reading the bare "you" answers for themselves only. Each hit is
// either worded with the spouse phrase or held in tools/spouse_phrase_baseline.json with the reason its "you" is
// right as written (an election of the return, a figure from the 2024 return, the return's one home, a question
// reached only by filers who are not filing jointly, a line the form asks about the taxpayer only).
//
// A hit not held fails, and so does a held question that is no longer a hit (in an unscoped run), so the list only
// shrinks. Both banks are read: the federal profile and the New York profile (which also carries the federal
// questions; each question is counted once).
//
//   spouse-phrase [--forms a,b] [--self-test]
//                    --forms: only the questions whose input touches one of these forms (form-scope.ts); a held
//                    question no longer a hit is not reported
//                    --self-test: the rule and the baseline on planted banks, and the forms scope
import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { CANON_DIR, loadCanonical } from "./canonical.js";
import { loadInterview, type InterviewData } from "./interview.js";
import { formScopeSelfTest, formsOption, scopeLine, touches } from "./form-scope.js";
import type { CanonicalData } from "./types.js";

const BASELINE = resolve(import.meta.dirname, "../..", "tools", "spouse_phrase_baseline.json");

/** "you", "your", "yours", "yourself" as words. */
const YOU = /\byou(?:r|rs|rself)?\b/i;
/** The words that bring the spouse into a question: the spouse named, "husband or wife", a phrase meaning both people,
 * a joint return named, or everyone on the return. */
const COUPLE = /\bspouse(?:['’]s)?\b|\bhusband(?:['’]s)? or wife(?:['’]s)?\b|\beither of you\b|\bboth of you\b|\byou both\b|\bjoint(?:ly)?\b|\b(?:any|some|every)one on this return\b/i;

/** The once-per-return questions of `config` whose prompt says "you" with no couple phrase in the prompt, the help or
 * the group's heading and label, by input; each with its prompt, for the message. Only inputs that touch `forms`. */
export function spousePhraseHits(data: Pick<CanonicalData, "forms">, config: Pick<InterviewData, "questions" | "groups">, forms: Set<string> | null = null): Map<string, string> {
  const docOf = new Map(data.forms.flatMap((d) => d.lines.map((l) => [l.id, d] as const)));
  const heading = new Map((config.groups ?? []).map((g) => [g.id, g.heading]));
  const hits = new Map<string, string>();
  for (const q of config.questions) {
    if (q.input.startsWith("$") || !touches(q.input, forms)) continue;
    const doc = docOf.get(q.input);
    if (!doc || doc.collection) continue;
    if (!YOU.test(q.prompt)) continue;
    const words = [q.prompt, q.help, q.group ? heading.get(q.group) ?? "" : "", q.tick ?? ""].join("\n");
    if (COUPLE.test(words)) continue;
    hits.set(q.input, q.prompt);
  }
  return hits;
}

/** The hits against the baseline: a hit not held, and (unscoped) a held question no longer a hit. */
export function spousePhraseProblems(hits: Map<string, string>, held: Record<string, string>, scoped: boolean): string[] {
  const out: string[] = [];
  for (const [input, prompt] of [...hits].sort()) {
    if (input in held) continue;
    out.push(`${input}: asked once per return, its prompt says "you" and neither prompt, help nor group heading names the spouse ` +
      `("${prompt.length > 120 ? `${prompt.slice(0, 117)}...` : prompt}"). Word it with the spouse phrase (interview/README.md, ` +
      `"A joint return combines both spouses' items"), or hold it in tools/spouse_phrase_baseline.json with the reason "you" is right as written`);
  }
  if (!scoped) for (const input of Object.keys(held).sort()) {
    if (!hits.has(input)) out.push(`${input}: held in tools/spouse_phrase_baseline.json but no longer a hit (reworded, or no longer asked once per return); remove it`);
  }
  return out;
}

function loadHeld(): Record<string, string> {
  const raw = JSON.parse(readFileSync(BASELINE, "utf8")) as { held?: Record<string, string> };
  return raw.held ?? {};
}

export function spousePhrase(args: string[] = []): number {
  if (args.includes("--self-test")) return selfTest();
  const forms = formsOption(args);
  const data = loadCanonical();
  const held = loadHeld();
  const hits = new Map<string, string>();
  console.log(`  ${scopeLine(forms)}`);
  for (const profile of ["full", "ny"] as const) {
    if (profile === "ny" && !existsSync(resolve(CANON_DIR, "interview-ny.json"))) { console.log("  ny: no New York interview built for this year; not checked"); continue; }
    const found = spousePhraseHits(data, loadInterview(profile), forms);
    console.log(`  ${profile}: ${found.size} once-per-return question(s) with a bare "you"`);
    for (const [k, v] of found) hits.set(k, v);
  }
  const problems = spousePhraseProblems(hits, held, forms !== null);
  for (const p of problems) console.error(`  ${p}`);
  console.log(`spouse-phrase: ${hits.size} hit(s), ${[...hits.keys()].filter((k) => k in held).length} held by the baseline, ${problems.length} problem(s)`);
  return problems.length ? 1 : 0;
}

/** The rule and the baseline on a planted bank. */
function selfTest(): number {
  formScopeSelfTest();
  const line = (id: string) => ({ id, expr: { op: "input" } });
  const data = { forms: [
    { id: "a", lines: [line("a.paid"), line("a.both"), line("a.grouped"), line("a.helped"), line("a.none"), line("a.everyone")] },
    { id: "b", lines: [line("b.paid")] },
    { id: "w", collection: { cite: {} }, lines: [line("w.paid")] },
  ] } as unknown as CanonicalData;
  const q = (input: string, prompt: string, extra: object = {}) => ({ input, prompt, help: "", order: 1, cite: {}, ...extra });
  const config = {
    groups: [{ id: "g", heading: "In 2025, did you (or, on a joint return, your spouse) have any of these?" }],
    questions: [
      q("a.paid", "Did you pay interest in 2025?"),
      q("a.both", "Did you (or, on a joint return, your spouse) pay interest in 2025?"),
      q("a.grouped", "Did you pay interest in 2025?", { group: "g", tick: "Interest paid" }),
      q("a.helped", "Did you pay interest in 2025?", { help: "Count interest your husband or wife paid." }),
      q("a.none", "Was interest paid in 2025?"),
      q("a.everyone", "Did you, or anyone on this return, pay interest?"),
      q("b.paid", "How much did you pay?"),
      q("w.paid", "On this account — how much did you pay?"),
      q("$w", "List your accounts."),
    ],
  } as unknown as InterviewData;
  const all = spousePhraseHits(data, config);
  assert.deepEqual([...all.keys()].sort(), ["a.paid", "b.paid"], "a bare you once per return; not a couple phrase in prompt, help or heading, an entry's question or a roster");
  assert.deepEqual([...spousePhraseHits(data, config, new Set(["b"])).keys()], ["b.paid"], "scoped: the scope's questions only");
  assert.equal(spousePhraseProblems(all, { "a.paid": "an election", "b.paid": "the 2024 return" }, false).length, 0, "every hit held");
  assert.match(spousePhraseProblems(all, { "a.paid": "an election" }, false).join("\n"), /^b\.paid: asked once per return/, "a hit not held fails");
  assert.match(spousePhraseProblems(all, { "a.paid": "x", "b.paid": "x", "a.both": "x" }, false).join("\n"), /^a\.both: held .* no longer a hit/, "a stale hold fails unscoped");
  assert.equal(spousePhraseProblems(new Map([["b.paid", ""]]), { "b.paid": "x", "a.both": "x" }, true).length, 0, "a scoped run does not report a stale hold");
  const held = loadHeld();
  for (const [k, why] of Object.entries(held)) assert.ok(typeof why === "string" && why.trim().length > 0, `${k}: every hold states its reason`);
  console.log(`spouse-phrase self-test: passed (a planted bank: 2 hits of 9 questions, the couple phrase found in prompt, help and group heading, an entry's question and a roster skipped; the scope; the baseline: a hit not held, a stale hold unscoped and scoped; ${Object.keys(held).length} holds each with a reason)`);
  return 0;
}
