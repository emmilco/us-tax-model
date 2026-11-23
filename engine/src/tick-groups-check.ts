// The command `tick-groups`: the tick-box groups (tick-groups.ts) of the built interview, each checked on the
// background return (the filer with nothing to report, who is asked every question that is asked of everyone):
//
//   shown whole      when the group's first member is the next question, the screen shows every member (each is open,
//                    or is reached once the open ones are answered No). A member that waits on an answer outside
//                    the group would be asked afterwards, alone
//   children next    a member's Yes with every other member No: each question the answers open is asked before any
//                    question that was already waiting and has an earlier order number than the opened one. So what
//                    a ticked box opens is asked in the topic the interview is in (among that topic's questions, in
//                    seq order), not behind a topic the filer was already due to reach
//   one by one       the same answers given one question at a time, in asking order (as the CLI asks them), end as
//                    the screen's answers do
//
//   tick-groups [--forms a,b] [--self-test]
//                    --forms: only the groups with a member that touches one of these forms (form-scope.ts)
//                    --self-test: the declaration rules of tick-groups.ts on planted banks, and the forms scope
import assert from "node:assert/strict";
import { loadCanonical } from "./canonical.js";
import { answerEvent, applyAnswer, applyAnswers, inputMeta, interviewView, loadInterview, questionTemplate, replay, replayState, type Event, type InterviewData } from "./interview.js";
import { backgroundOf, type Background } from "./interview-coverage.js";
import { ABOUT_SPOUSE, ABOUT_YOU, PERSON_FRAME, personWording } from "./spouse-wording.js";
import { opensMap, tickGroupProblems, type GroupFacts, type GroupQuestion } from "./tick-groups.js";
import { formScopeSelfTest, formsOption, scopeLine, touchesAny } from "./form-scope.js";
import type { CanonicalData, Line } from "./types.js";

/** The checks of the head of this file for each group of `config`, on its background return. `problems` fail the
 * command; `notes` say what was not checked. */
export function tickGroupWalkProblems(data: CanonicalData, config: InterviewData, background: Background, forms: Set<string> | null = null): { problems: string[]; notes: string[]; checked: number } {
  const problems: string[] = [], notes: string[] = [];
  let checked = 0;
  const header: Event = { version: 1, tax_year: config.tax_year };
  for (const g of scopedGroups(config, forms)) {
    const where = `group ${g.id}`;
    const members = config.questions.filter((q) => q.group === g.id).map((q) => q.input);
    const at = background.steps.findIndex((s) => members.includes(questionTemplate(s.input)));
    if (at < 0) { notes.push(`${where}: the background return is never asked a member (the group lies behind an answer it does not give); not checked here`); continue; }
    const events: Event[] = [header];
    for (const s of background.steps.slice(0, at)) events.push(answerEvent(config, replayState(config, events), s.input, s.value));
    const before = interviewView(data, config, replay(config, events));
    const shown = before.group;
    const open = shown?.id === g.id ? shown.members.map((q) => q.input) : [];
    const missing = members.filter((m) => !open.some((k) => questionTemplate(k) === m));
    if (missing.length) {
      problems.push(`${where}: on the background return the screen shows ${open.length ? open.join(", ") : "no group"} when ${background.steps[at]!.input} is the next question; ${missing.join(", ")} ${missing.length === 1 ? "is" : "are"} not on it (answered earlier, or waiting on an answer outside the group) and would be asked apart: see docs/provisional/lanes/tick.md, "Shown together"`);
      continue;
    }
    checked++;
    const pendingBefore = new Set(before.pending.map((q) => q.input));
    for (const yes of [null, ...open]) {
      const answers = open.map((input) => ({ input, value: input === yes }));
      const what = yes === null ? "none ticked" : `${yes} ticked`;
      let together: ReturnType<typeof applyAnswers>;
      try { together = applyAnswers(data, config, events, answers); } catch (e) { problems.push(`${where}: ${what}: the answers are rejected: ${(e as Error).message}`); continue; }
      // A question the answers open is asked before every question that was already waiting and belongs to an earlier
      // order number than its own. Waiting questions of its own order number may come before it, in seq order.
      if (together.after.status !== "refused") {
        let waiting: { input: string; order: number } | undefined;
        for (const q of together.after.pending) {
          if (pendingBefore.has(q.input)) { waiting = q; continue; }
          if (waiting && waiting.order < q.order) problems.push(`${where}: ${what}: the answer opens ${q.input} (order ${q.order}), asked only after ${waiting.input} (order ${waiting.order}), which was already waiting; a question a member's yes opens is asked before the questions of earlier order numbers that were waiting: give it the group's order number`);
        }
      }
      // One at a time, in asking order, the same answers end the same way.
      const single: Event[] = [...events];
      let view = before;
      for (;;) {
        const next = view.pending.find((q) => open.includes(q.input));
        if (!next || view.status === "refused") break;
        const applied = applyAnswer(data, config, single, next.input, next.input === yes);
        single.push(applied.event);
        view = applied.after;
      }
      const gate = (v: typeof view) => (v.refusal as { gate?: string } | null)?.gate ?? null;
      if (view.status !== together.after.status || gate(view) !== gate(together.after))
        problems.push(`${where}: ${what}: asked one at a time the return is ${view.status}${gate(view) ? ` at ${gate(view)}` : ""}; answered on one screen it is ${together.after.status}${gate(together.after) ? ` at ${gate(together.after)}` : ""}`);
    }
  }
  return { problems, notes, checked };
}

/** The groups of `config` with a member that touches a form of `forms` (every group when `forms` is null). */
export function scopedGroups(config: Pick<InterviewData, "groups" | "questions">, forms: Set<string> | null): NonNullable<InterviewData["groups"]> {
  return (config.groups ?? []).filter((g) => touchesAny(config.questions.filter((q) => q.group === g.id).map((q) => q.input), forms));
}

export function tickGroups(args: string[] = []): number {
  if (args.includes("--self-test")) return selfTest();
  const forms = formsOption(args);
  const data = loadCanonical();
  let failed = 0;
  console.log(`  ${scopeLine(forms)}`);
  for (const profile of ["full", "ny"] as const) {
    const config = loadInterview(profile);
    const { problems, notes, checked } = tickGroupWalkProblems(data, config, backgroundOf(data, config, profile), forms);
    for (const n of notes) console.log(`  ${profile}: ${n}`);
    for (const p of problems) console.error(`  ${profile}: ${p}`);
    console.log(`  ${profile}: ${scopedGroups(config, forms).length} of ${(config.groups ?? []).length} group(s) checked, ${checked} shown whole on the background return, ${problems.length} problem(s)`);
    failed += problems.length;
  }
  console.log(`tick-groups: ${failed ? `${failed} problem(s)` : "passed"}`);
  return failed ? 1 : 0;
}

/** The declaration rules on planted banks. */
function selfTest(): number {
  formScopeSelfTest();
  const scopeBank = { groups: [{ id: "g", heading: "H?" }, { id: "h", heading: "H?" }], questions: [{ input: "a.one", group: "g" }, { input: "person.x", group: "h" }, { input: "b.one" }] } as unknown as InterviewData;
  assert.deepEqual(scopedGroups(scopeBank, null).map((g) => g.id), ["g", "h"], "unscoped: every group");
  assert.deepEqual(scopedGroups(scopeBank, new Set(["a"])).map((g) => g.id), ["g"], "scoped: the groups with a member of the form");
  assert.deepEqual(scopedGroups(scopeBank, new Set(["b"])).map((g) => g.id), [], "a form with no grouped question: no group");
  const types: Record<string, string> = { "a.one": "Bool", "a.two": "Bool", "a.three": "Bool", "a.child": "Bool", "a.amount": "NonNegDollars", "b.one": "Bool", "person.x": "Bool", "person.y": "Bool" };
  const facts = (opens: Record<string, string[]> = {}): GroupFacts => ({
    typeOf: (i) => types[i],
    formOf: (i) => (i.startsWith("$") ? { id: i.slice(1), collection: true, frame: "" } : { id: i.split(".")[0]!, collection: i.startsWith("person."), frame: i.startsWith("person.") ? PERSON_FRAME : "" }),
    opens: (i) => opens[i] ?? [],
  });
  const groups = [{ id: "g", heading: "Did any of these happen in 2025?" }];
  const q = (input: string, seq: number | undefined, extra: Partial<GroupQuestion> = { group: "g", tick: `Label of ${input.replace(/\W/g, " ")}` }): GroupQuestion => ({ input, order: 7, ...(seq === undefined ? {} : { seq }), ...extra });
  const plain = (input: string, seq?: number, order = 7): GroupQuestion => ({ input, order, ...(seq === undefined ? {} : { seq }) });
  const of = (qs: GroupQuestion[], gs: unknown = groups, opens: Record<string, string[]> = {}) => tickGroupProblems(gs, qs, facts(opens)).join("\n");
  const good = [q("a.one", 1), q("a.two", 2), q("a.three", 3)];
  assert.equal(of(good), "");
  assert.equal(tickGroupProblems(undefined, [plain("a.one"), plain("a.two")], facts()).join("\n"), "", "a bank with no group");
  let cases = 2;
  const refused = (problems: string, pattern: RegExp) => { assert.match(problems, pattern); cases++; };
  refused(of(good, { g: "x" }), /groups must be a list/);
  refused(of(good, [{ id: "Bad id", heading: "H?" }]), /a group is \{id, heading\}/);
  refused(of(good, [...groups, ...groups]), /group g: declared twice/);
  refused(of(good, [{ id: "g", heading: "Two\nlines" }]), /the heading must be one non-empty line/);
  refused(of(good, [{ id: "g", heading: Array(26).fill("word").join(" ") + "?" }]), /the heading has 26 words; at most 25/);
  refused(of(good, [{ id: "g", heading: "Answer true or false for each?" }]), /the heading states entry syntax/);
  refused(of(good, [...groups, { id: "empty", heading: "Any?" }]), /group empty: no question names it/);
  refused(of([...good, q("b.one", 9, { group: "nosuch", tick: "A label" })]), /question b\.one: group "nosuch" is not declared/);
  refused(of([...good, plain("b.one", 9), { ...plain("a.child", 10), tick: "A label" }]), /question a\.child: tick is the label of a member of a tick-box group; the question names no group/);
  refused(of([q("a.one", 1), q("a.amount", 2)]), /question a\.amount: a member of a tick-box group is a yes or no question; this input is NonNegDollars/);
  refused(of([q("a.one", 1), q("$a", 2)]), /question \$a: a member of a tick-box group is a yes or no question; this input is a list/);
  refused(of([q("a.one", 1), q("a.two", 2, { group: "g" })]), /question a\.two: a member of a tick-box group needs tick/);
  refused(of([q("a.one", 1), q("a.two", 2, { group: "g", tick: Array(13).fill("word").join(" ") })]), /the tick label has 13 words; at most 12/);
  refused(of([q("a.one", 1), q("a.two", 2, { group: "g", tick: "Did you sell farmland?" })]), /the tick label is a question/);
  refused(of([q("a.one", 1), q("a.two", 2, { group: "g", tick: "Sold it (or on a joint return, your spouse)" })]), /near-miss of the spouse phrase/);
  refused(of([q("a.one", 1, { group: "g", tick: "Same" }), q("a.two", 2, { group: "g", tick: "Same" })]), /two members have the same tick label/);
  refused(of([q("a.one", 1)]), /group g: 1 member \(a\.one\); a group has 2 to 6/);
  refused(of([1, 2, 3, 4, 5, 6, 7].map((n) => q(`a.m${n}`, n)), groups), /group g: 7 members/);
  refused(of([q("a.one", 1), q("person.x", 2)]), /are of several forms, one of them a list's/);
  refused(of([q("person.x", 1, { group: "g", tick: "You swim" }), q("person.y", 2)]), /the tick label is not covered: .*"You swim"/);
  refused(of([q("a.one", 1), { ...q("a.two", 2), order: 8 }]), /have different order numbers/);
  refused(of([q("a.one", undefined), q("a.two", undefined)]), /a member has no seq/);
  assert.equal(of([q("a.one", 10), q("a.two", 20), q("a.three", 30)]), "", "members' seq numbers may leave gaps");
  assert.equal(of([q("a.one", 10), q("a.two", 20), plain("b.one", 5), plain("b.two", 25), plain("a.child")]), "", "other questions of the order number before the members, after them, or without seq");
  cases += 2;
  refused(of([q("a.one", 1), q("a.two", 3), q("a.three", 4), plain("b.one", 2)]), /question b\.one \(seq 2\) lies among its members' seq numbers/);
  // What a member's yes opens is never a member. Where the other opened questions stand is not a declaration rule.
  refused(of(good, groups, { "a.one": ["a.two"] }), /member a\.two is asked only after member a\.one is answered yes/);
  assert.equal(of([...good, plain("a.child", 4)], groups, { "a.two": ["a.child", "not.in_bank"] }), "");
  assert.equal(of([...good, plain("b.one", 4), plain("a.child", 5)], groups, { "a.two": ["a.child"] }), "", "another question between the group and an opened question");
  assert.equal(of([...good, plain("a.child", 4, 8)], groups, { "a.two": ["a.child"] }), "", "an opened question of another order number");
  assert.equal(of([...good, plain("a.child")], groups, { "a.two": ["a.child"] }), "", "an opened question without seq");
  cases += 4;
  // Per person: the frame's rule covers the heading and the labels.
  assert.equal(of([q("person.x", 1, { group: "g", tick: "You have a guide dog" }), q("person.y", 2, { group: "g", tick: "Your spouse has one" })], [{ id: "g", heading: "Are any of these true of you?" }]), "");

  // A group asked of each person, planted on the built interview: two yes or no questions that are open for both
  // people of a couple's return, made the first block. Each person has a screen, under the per-person frame, with the
  // heading and the labels worded for that person; a screen's answers are that person's only.
  const data = loadCanonical();
  const built = loadInterview("full");
  const header: Event = { version: 1, tax_year: built.tax_year };
  const couple = built.questions.find((q) => q.input === "$person")?.choices?.find((c) => c.value.length === 2);
  assert.ok(couple, "the person roster has a choice of two people");
  const events: Event[] = [header, answerEvent(built, replayState(built, [header]), "$person", couple.value)];
  const open = new Set(interviewView(data, built, replay(built, events)).pending.map((x) => x.input));
  const key = (template: string, who: string) => template.replace(/^person\./, `person[${who}].`);
  const [first, second] = built.questions.filter((x) => /^person\.[a-z0-9_]+$/.test(x.input) && inputMeta(data, x.input).type === "Bool" && open.has(key(x.input, "taxpayer")) && open.has(key(x.input, "spouse"))).map((x) => x.input);
  assert.ok(first && second, "two yes or no questions are open for both people once the couple is chosen");
  const heading = "Are any of these true of you?", labels = ["You have the first", "You have the second"];
  const planted: InterviewData = { ...built, groups: [{ id: "planted", heading: PERSON_FRAME + heading }],
    questions: built.questions.map((x) => (x.input === first ? { ...x, order: -1, seq: 1, group: "planted", tick: labels[0]! } : x.input === second ? { ...x, order: -1, seq: 2, group: "planted", tick: labels[1]! } : x)) };
  const theirs = interviewView(data, planted, replay(planted, events));
  assert.deepEqual(theirs.group && { ...theirs.group, members: theirs.group.members.map((m) => [m.input, m.tick]) },
    { id: "planted", heading: `${ABOUT_SPOUSE} — ${personWording(heading, "spouse")}`, frame: ABOUT_SPOUSE, members: [[key(first, "spouse"), personWording(labels[0]!, "spouse")], [key(second, "spouse"), personWording(labels[1]!, "spouse")]] });
  assert.match(theirs.group!.heading, /true of your spouse\?$/);
  assert.equal(theirs.group!.members[0]!.tick, "Your spouse has the first");
  assert.throws(() => applyAnswers(data, planted, events, [{ input: key(first, "spouse"), value: false }, { input: key(second, "taxpayer"), value: false }]), /person\[taxpayer\]\.[a-z0-9_]+: not a box of the tick-box screen offered now/);
  const answered = applyAnswers(data, planted, events, [{ input: key(first, "spouse"), value: false }, { input: key(second, "spouse"), value: false }]);
  assert.deepEqual(answered.events, [{ input: key(first, "spouse"), value: false }, { input: key(second, "spouse"), value: false }]);
  assert.deepEqual(answered.after.group && { ...answered.after.group, members: answered.after.group.members.map((m) => [m.input, m.tick]) },
    { id: "planted", heading: `${ABOUT_YOU} — ${heading}`, frame: ABOUT_YOU, members: [[key(first, "taxpayer"), labels[0]], [key(second, "taxpayer"), labels[1]]] });
  // One person's member answered on its own leaves that person one open member: an ordinary question, no screen.
  const one = applyAnswer(data, planted, [...events, ...answered.events], key(first, "taxpayer"), false);
  assert.ok(one.after.group === null && one.after.pending[0]!.input === key(second, "taxpayer") && one.after.pending[0]!.prompt.startsWith(`${ABOUT_YOU} — `));

  // Which members a screen shows, on a constructed form: a chain of tests reads a, then b, then c (each reached only
  // once the one before is answered no), and w is reached only once z, a question outside the group, is answered no.
  const line = (id: string, expr: object) => ({ id: `t.${id}`, printed: id, label: id, type: "Bool", expr, cite: null });
  const ask = (id: string) => line(id, { op: "input", source: `${id}?` });
  const either = (id: string, test: string, otherwise: string) => line(id, { op: "choose", alternatives: [
    { guard: { op: "test", eq: [`t.${test}`, { const: true }] }, then: `t.${test}` }, { guard: { op: "test", eq: [`t.${test}`, { const: false }] }, then: `t.${otherwise}` }] });
  const small = { forms: [{ id: "t", kind: "form", tax_year: built.tax_year, title: "Chain test", lines: [ask("a"), ask("b"), ask("c"), ask("w"), ask("z"), either("from_b", "b", "c"), either("chain", "a", "from_b"), either("other", "z", "w")] }],
    defs: [], tables: [], register: { entries: [] }, params: { values: {}, enums: {} } } as unknown as CanonicalData;
  const member = (id: string, seq: number) => ({ input: `t.${id}`, prompt: `${id}?`, help: "", order: 1, seq, group: "chain", tick: `Label ${id}`, cite: null });
  const smallConfig = { tax_year: built.tax_year, targets: ["t.chain", "t.other"], initial: {}, cite: null, groups: [{ id: "chain", heading: "Any of these?" }],
    questions: [member("a", 1), member("b", 2), member("c", 3), member("w", 4), { input: "t.z", prompt: "z?", help: "", order: 2, cite: null }] } as unknown as InterviewData;
  const start = interviewView(small, smallConfig, replay(smallConfig, [header]));
  assert.deepEqual(start.pending.map((x) => x.input), ["t.a", "t.z"], "only the chain's first link and the outside question are open");
  assert.deepEqual(start.group?.members.map((m) => [m.input, m.tick]), [["t.a", "Label a"], ["t.b", "Label b"], ["t.c", "Label c"]], "the screen has the members reached through the others' no, and not the one waiting outside the group");
  // One at a time the same answers are cut short: after a yes to a the engine does not reach b.
  const aYes = applyAnswer(small, smallConfig, [header], "t.a", true);
  assert.throws(() => applyAnswer(small, smallConfig, [header, aYes.event], "t.b", false), /neither reachable nor a correction/);
  // On the screen they are taken together, in the order given; each is an ordinary event.
  const all = applyAnswers(small, smallConfig, [header], [{ input: "t.a", value: true }, { input: "t.b", value: false }, { input: "t.c", value: false }]);
  assert.deepEqual(all.events, [{ input: "t.a", value: true }, { input: "t.b", value: false }, { input: "t.c", value: false }]);
  assert.deepEqual(all.after.pending.map((x) => x.input), ["t.z"]);
  for (const [bad, pattern] of [
    [[{ input: "t.a", value: false }, { input: "t.b", value: false }], /t\.c: the screen's answers leave this box out/],
    [[{ input: "t.a", value: false }, { input: "t.b", value: false }, { input: "t.c", value: false }, { input: "t.w", value: false }], /t\.w: not a box of the tick-box screen offered now \(t\.a, t\.b, t\.c\)/],
    [[{ input: "t.a", value: false }, { input: "t.b", value: false }, { input: "t.c", value: null }], /t\.c: a tick-box is answered yes or no/],
    ["t.a", /a list of \{input, value\}/],
  ] as const) assert.throws(() => applyAnswers(small, smallConfig, [header], bad), pattern);
  // None ticked gives the state one question at a time gives; then the outside answer opens the last member, alone.
  const none = applyAnswers(small, smallConfig, [header], [{ input: "t.a", value: false }, { input: "t.b", value: false }, { input: "t.c", value: false }]);
  let stepwise: Event[] = [header];
  for (const k of ["t.a", "t.b", "t.c"]) stepwise = [...stepwise, applyAnswer(small, smallConfig, stepwise, k, false).event];
  assert.deepEqual(none.inputs, replay(smallConfig, stepwise));
  const last = applyAnswer(small, smallConfig, [header, ...none.events], "t.z", false).after;
  assert.ok(last.group === null && last.pending.length === 1 && last.pending[0]!.input === "t.w" && last.pending[0]!.tick === "Label w", "one member open is an ordinary question");
  assert.throws(() => applyAnswers(small, smallConfig, [header, ...none.events, { input: "t.z", value: false }], [{ input: "t.w", value: false }]), /the interview offers no tick-box screen now/);
  // A member answered earlier is not on the screen; the rest are.
  const cFirst = interviewView(small, smallConfig, { ...replay(smallConfig, [header]), "t.c": false });
  assert.deepEqual(cFirst.group?.members.map((m) => m.input), ["t.a", "t.b"]);
  // A member behind another member's no and, in its form, behind a refusal screen whose question is outside the group:
  // once the first member is answered no the interview asks it next (it states a seq, so it is open past the screen),
  // so it is on the screen.
  const held = { ...either("held", "b", "b"), refuses: [{ when: "t.s", form: "Screen", remedy: "None.", cite: null }] };
  const screened = { ...small, forms: [{ ...small.forms[0]!, lines: [ask("a"), ask("b"), ask("s"), held, either("chain", "a", "held")] }] } as unknown as CanonicalData;
  const screenedConfig = { ...smallConfig, targets: ["t.chain"], questions: [member("a", 1), member("b", 2), { input: "t.s", prompt: "s?", help: "", order: 2, cite: null }] } as unknown as InterviewData;
  const behind = interviewView(screened, screenedConfig, replay(screenedConfig, [header]));
  assert.deepEqual(behind.pending.map((x) => x.input), ["t.a"], "only the first member is open");
  assert.deepEqual(behind.group?.members.map((m) => m.input), ["t.a", "t.b"], "the member behind the screen is on the tick-box screen");
  assert.deepEqual(applyAnswer(screened, screenedConfig, [header], "t.a", false).after.pending.map((x) => x.input), ["t.b", "t.s"], "asked one at a time, the member comes before the screen's own question");
  assert.deepEqual(applyAnswers(screened, screenedConfig, [header], [{ input: "t.a", value: false }, { input: "t.b", value: false }]).after.pending.map((x) => x.input), ["t.s"]);
  // The walk's check of what a ticked member opens, on a constructed form: two groups one after the other (a and b,
  // then c and d) and an ordinary question y in order number 1, a question k that a yes to a opens, and a question z
  // of order number 2. With k in order number 1, after the second group and y, the walk finds nothing; with k in
  // order number 3, asked after z, it names k.
  const opening = line("k_if", { op: "choose", alternatives: [{ guard: { op: "test", eq: ["t.a", { const: true }] }, then: "t.k" }, { guard: { op: "test", eq: ["t.a", { const: false }] }, then: "t.a" }] });
  const twoGroups = { ...small, forms: [{ ...small.forms[0]!, lines: [ask("a"), ask("b"), ask("c"), ask("d"), ask("y"), ask("z"), { ...ask("k"), gated_by: "t.k_if" }, opening, either("of_b", "b", "b"), either("of_c", "c", "c"), either("of_d", "d", "d"), either("of_y", "y", "y"), either("of_z", "z", "z")] }] } as unknown as CanonicalData;
  const inGroup = (id: string, seq: number, group: string) => ({ ...member(id, seq), group });
  const walked = (kOrder: number, kSeq: number) => {
    const c = { ...smallConfig, targets: ["t.k_if", "t.of_b", "t.of_c", "t.of_d", "t.of_y", "t.of_z"], groups: [{ id: "first", heading: "Any of these?" }, { id: "second", heading: "And any of these?" }],
      questions: [inGroup("a", 1, "first"), inGroup("b", 2, "first"), inGroup("c", 3, "second"), inGroup("d", 4, "second"), { input: "t.k", prompt: "k?", help: "", order: kOrder, seq: kSeq, cite: null }, { input: "t.y", prompt: "y?", help: "", order: 1, seq: 5, cite: null }, { input: "t.z", prompt: "z?", help: "", order: 2, seq: 1, cite: null }] } as unknown as InterviewData;
    const steps = ["a", "b", "c", "d", "y", "z"].map((id, n) => ({ n: n + 1, input: `t.${id}`, value: false, from: "background" })) as unknown as Background["steps"];
    return tickGroupWalkProblems(twoGroups, c, { answers: new Map(), steps });
  };
  const inPlace = walked(1, 6);
  assert.deepEqual([inPlace.problems, inPlace.checked], [[], 2], "a question opened by the first group's member, asked after the second group and another question of the order number");
  const afterTopic = walked(3, 1);
  assert.equal(afterTopic.problems.length, 1);
  assert.match(afterTopic.problems[0]!, /group first: t\.a ticked: the answer opens t\.k \(order 3\), asked only after t\.z \(order 2\), which was already waiting/);
  // What an input opens, as the declaration rule reads it: a gated question whose gate reads the input, directly or
  // through what a yes or no line computes; not one whose gate only stands behind a derived screen that the input's yes refuses at.
  const behind_ = (screen: object) => opensMap([{ lines: [ask("m"), ask("o"), screen, { ...ask("c"), gated_by: "t.c_if" },
    line("c_if", { op: "choose", alternatives: [{ guard: { op: "test", eq: ["t.screen", { const: true }] }, then: "t.c" }, { guard: { op: "test", eq: ["t.screen", { const: false }] }, then: "t.o" }] })] as unknown as Line[] }]);
  assert.deepEqual(behind_(either("screen", "m", "o")).get("t.m"), ["t.c"], "a gate that reads the input through a yes or no line");
  const refusing = opensMap([{ lines: [ask("m"), ask("o"), either("screen", "m", "m"), { ...either("holder", "o", "screen"), refuses: [{ when: "t.screen", form: "Screen", remedy: "None.", cite: null }] }, { ...ask("c"), gated_by: "t.c_if" },
    line("c_if", { op: "choose", alternatives: [{ guard: { op: "test", eq: ["t.holder", { const: true }] }, then: "t.c" }, { guard: { op: "test", eq: ["t.holder", { const: false }] }, then: "t.o" }] })] as unknown as Line[] }]);
  assert.deepEqual([refusing.get("t.m"), refusing.get("t.o")], [undefined, ["t.c"]], "a gate behind a derived screen that the input's yes refuses at");
  console.log(`tick-groups self-test: passed (the declaration rules on planted banks: ${cases + 3} cases; a group asked of each person, planted on ${first} and ${second} of the built interview: the spouse's screen, a box of the other person refused, the filer's screen, one member left open; on a constructed form: what a ticked member opens, asked in the group's order number after a second group and another question, and named when it is asked after the next order number's question; what an input opens, read through a yes or no line and not through a derived refusal screen; on a constructed chain of tests: the members a screen shows, its answers taken together where one at a time they are cut short, 4 rejected screens, none ticked the same as one at a time, a member behind a refusal screen)`);
  return 0;
}
