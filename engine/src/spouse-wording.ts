// The spouse phrase of once-per-return questions, reworded for the filer's own return when a question is handed to
// a client. The stored question text (canonical/, which the reviews and the renderer read) always carries the
// conditional phrase; only what `interviewView` and the web UI's server send for display (question prompts and help,
// and the form-line labels of the interview's values sheet) is reworded, from the return's filing-status answer at
// that moment:
//
//   stored                                         joint return             no spouse on the return
//   "you (or, on a joint return, your spouse)"     "you or your spouse"     "you"
//   "your (or, on a joint return, your spouse's)"  "your or your spouse's"  "your"
//
// While the filing status is unanswered the stored text is shown. Nothing reworded is saved: each response is
// reworded from the answers it is computed from, so a corrected filing status changes every text on the next
// response. Other spouse wording ("(and, on a joint return, your spouse)", the per-person frame "For this person
// (you, or your spouse on a joint return) — ") is not matched and is shown as stored.
import assert from "node:assert/strict";
import { loadCanonical } from "./canonical.js";
import { loadInterview } from "./interview.js";
import { parseStructured } from "./text.js";
import type { Inputs } from "./types.js";

/** What the return's answers say about a spouse on it. */
export type JointReturn = "joint" | "not-joint" | "unknown";

/** The phrase after "you", with its leading space, and the possessive form with its "your". */
export const SPOUSE_PHRASE = " (or, on a joint return, your spouse)";
export const SPOUSE_POSSESSIVE = "your (or, on a joint return, your spouse's)";

/** The filing-status input and its values (the enum `filing_status`). Married filing jointly is the one joint
 * return. Single, head of household and qualifying surviving spouse have no spouse on the return; married filing
 * separately (which the return refuses) leaves the spouse's items off it, so its questions are about "you" alone. */
export const STATUS_INPUT = "f1040.status";
const JOINT_STATUS = "mfj";
const NOT_JOINT_STATUSES = ["single", "mfs", "hoh", "qss"];

/** Whether the return is joint, from its current answers: unknown until the filing status is answered (a help
 * request leaves it unanswered). */
export function jointReturn(inputs: Inputs): JointReturn {
  const status = inputs[STATUS_INPUT];
  if (status === JOINT_STATUS) return "joint";
  return typeof status === "string" && NOT_JOINT_STATUSES.includes(status) ? "not-joint" : "unknown";
}

/** The text to show: every exact occurrence of the two phrases reworded for the return; unchanged when the filing
 * status is unknown or the text has neither phrase. */
export function spouseWording(text: string, joint: JointReturn): string {
  if (joint === "unknown") return text;
  return text
    .replaceAll(SPOUSE_POSSESSIVE, joint === "joint" ? "your or your spouse's" : "your")
    .replaceAll(SPOUSE_PHRASE, joint === "joint" ? " or your spouse" : "");
}

/** A question as shown: its prompt and help reworded. */
export function shownQuestion<Q extends { prompt: string; help: string }>(q: Q, joint: JointReturn): Q {
  return { ...q, prompt: spouseWording(q.prompt, joint), help: spouseWording(q.help, joint) };
}

/** A values sheet as shown: each line's label reworded. */
export function shownSheet<S extends { sections: { lines: { label: string }[] }[] }>(sheet: S, joint: JointReturn): S {
  if (joint === "unknown") return sheet;
  return { ...sheet, sections: sheet.sections.map((s) => ({ ...s, lines: s.lines.map((l) => ({ ...l, label: spouseWording(l.label, joint) })) })) };
}

/** "or, on a joint return, your spouse" in that word order with any capitalisation, punctuation or spacing, and
 * with a different or missing preposition or article before "joint return". */
const LOOSE = /\bor[^A-Za-z0-9]+(?:(?:on|in|for|if|with)[^A-Za-z0-9]+)?(?:(?:a|the)[^A-Za-z0-9]+)?joint[^A-Za-z0-9]+returns?[^A-Za-z0-9]+your[^A-Za-z0-9]+spouse(?:['’]?s\b)?\)?/gi;

/** The near-misses of the spouse phrase in a text: each wording that reads as the phrase but is not exactly one of
 * the two forms `spouseWording` rewords (other capitalisation, punctuation or spacing, a curly apostrophe, a
 * possessive without its "your", no space before the parenthesis), so it would be shown as stored on every return.
 * Wording in another word order ("or your spouse, on a joint return", "and, on a joint return, your spouse") is
 * other spouse wording, not a near-miss. */
export function spousePhraseNearMisses(text: string): string[] {
  const rest = text.replaceAll(SPOUSE_POSSESSIVE, "your \u0000").replaceAll(SPOUSE_PHRASE, "\u0000");
  return [...rest.matchAll(LOOSE)].map((m) => {
    const from = Math.max(0, m.index - 12);
    const shown = rest.slice(from, m.index + m[0].length).replaceAll("\u0000", "…").replace(/\s+/g, " ");
    return (from > 0 ? shown.slice(shown.indexOf(" ") + 1) : shown).trim();
  });
}

/** `spouse-wording --self-test`: the rewording, the status reading and the near-miss rule on constructed texts; that
 * the status reading names every value of the built `filing_status` enum; and that every built question and line
 * label still parses as structured text in both readings. */
export function spouseWordingSelfTest(): number {
  const plain = "Did you (or, on a joint return, your spouse) receive interest in 2025?";
  const possessive = "Total of box 5 of all your (or, on a joint return, your spouse's) Forms SSA-1099.";
  assert.equal(spouseWording(plain, "joint"), "Did you or your spouse receive interest in 2025?");
  assert.equal(spouseWording(plain, "not-joint"), "Did you receive interest in 2025?");
  assert.equal(spouseWording(plain, "unknown"), plain);
  assert.equal(spouseWording(possessive, "joint"), "Total of box 5 of all your or your spouse's Forms SSA-1099.");
  assert.equal(spouseWording(possessive, "not-joint"), "Total of box 5 of all your Forms SSA-1099.");
  assert.equal(spouseWording(possessive, "unknown"), possessive);
  // Both forms and a repeat in one text, across the blocks of a structured text and before punctuation.
  const twice = "Did you (or, on a joint return, your spouse) sell any of your (or, on a joint return, your spouse's) shares?\n\nCount:\n- shares you (or, on a joint return, your spouse), or a nominee, held\n- none your (or, on a joint return, your spouse's) dependents held";
  assert.equal(spouseWording(twice, "joint"), "Did you or your spouse sell any of your or your spouse's shares?\n\nCount:\n- shares you or your spouse, or a nominee, held\n- none your or your spouse's dependents held");
  assert.equal(spouseWording(twice, "not-joint"), "Did you sell any of your shares?\n\nCount:\n- shares you, or a nominee, held\n- none your dependents held");
  assert.equal(spouseWording(twice, "unknown"), twice);
  // A text with neither phrase, and other spouse wording, is shown as stored on every return.
  const untouched = [
    "Total wages from all your Forms W-2.",
    "",
    "For this person (you, or your spouse on a joint return) — Were you blind at the end of 2025?",
    "Jury duty pay you (and, on a joint return, your spouse) received in 2025.",
    "Did you (or your spouse, if filing jointly) receive dependent care benefits for 2025?",
    "Does any of these apply to you (or your spouse on a joint return)?",
    "Enter the amounts of all your and your spouse's Forms 1099-DIV combined; you or your spouse may hold them.",
    "Before 2025, or, on this 2025 joint return, you and your spouse each filed.",
  ];
  for (const text of untouched) {
    for (const joint of ["joint", "not-joint", "unknown"] as const) assert.equal(spouseWording(text, joint), text, text);
    assert.deepEqual(spousePhraseNearMisses(text), [], text);
  }
  for (const text of [plain, possessive, twice]) assert.deepEqual(spousePhraseNearMisses(text), [], text);
  // Near-misses: each reads as the phrase and none is reworded.
  const nearMisses = [
    "Did you (Or, on a joint return, your spouse) receive interest?",
    "Did you (or on a joint return, your spouse) receive interest?",
    "Did you (or, on a joint return your spouse) receive interest?",
    "Did you (or,  on a joint return, your spouse) receive interest?",
    "Did you(or, on a joint return, your spouse) receive interest?",
    "Did you, or, on a joint return, your spouse, receive interest?",
    "Did you (or, in a joint return, your spouse) receive interest?",
    "Did you (or, on joint returns, your spouse) receive interest?",
    "All your (or, on a joint return, your spouse’s) Forms SSA-1099.",
    "All Your (or, on a joint return, your spouse's) Forms SSA-1099.",
    "The (or, on a joint return, your spouse's) Forms SSA-1099.",
    "Did you (or, on a joint return, your spouse's employer) pay?",
  ];
  for (const text of nearMisses) {
    assert.equal(spousePhraseNearMisses(text).length, 1, text);
    assert.equal(spouseWording(text, "joint"), text, text);
  }
  assert.deepEqual(spousePhraseNearMisses(`${plain} And you (or on a joint return your spouse)?`), ["And you (or on a joint return your spouse)"]);

  // The status reading: every value of the built enum is read as joint or not joint, and nothing else is.
  const data = loadCanonical();
  const values = data.params.enums["filing_status"]!.values;
  assert.deepEqual([...values].sort(), [JOINT_STATUS, ...NOT_JOINT_STATUSES].sort(), "the filing_status enum's values are the ones jointReturn reads");
  for (const v of values) assert.equal(jointReturn({ [STATUS_INPUT]: v }), v === JOINT_STATUS ? "joint" : "not-joint");
  for (const inputs of [{}, { [STATUS_INPUT]: null }, { [STATUS_INPUT]: "married" }, { [STATUS_INPUT]: true }, { "$person": ["taxpayer", "spouse"] }]) assert.equal(jointReturn(inputs), "unknown");
  assert.deepEqual(shownQuestion({ input: "x", prompt: plain, help: possessive, order: 3 }, "not-joint"),
    { input: "x", prompt: "Did you receive interest in 2025?", help: "Total of box 5 of all your Forms SSA-1099.", order: 3 });

  const sheet = { sections: [{ doc: "d", lines: [{ key: "d.a", label: plain }, { key: "d.b", label: "Wages" }] }], notices: ["n"] };
  assert.deepEqual(shownSheet(sheet, "joint"), { sections: [{ doc: "d", lines: [{ key: "d.a", label: "Did you or your spouse receive interest in 2025?" }, { key: "d.b", label: "Wages" }] }], notices: ["n"] });
  assert.equal(shownSheet(sheet, "not-joint").sections[0]!.lines[0]!.label, "Did you receive interest in 2025?");
  assert.equal(shownSheet(sheet, "unknown"), sheet);
  assert.equal(sheet.sections[0]!.lines[0]!.label, plain, "the sheet given is not changed");

  // The built line labels: no near-miss, and each reworded label is still well-formed structured text.
  let labelled = 0;
  for (const line of [...data.forms, ...data.defs].flatMap((d) => d.lines)) {
    assert.deepEqual(spousePhraseNearMisses(line.label), [], `${line.id} label`);
    if (!line.label.includes(SPOUSE_PHRASE) && !line.label.includes(SPOUSE_POSSESSIVE)) continue;
    labelled++;
    for (const joint of ["joint", "not-joint"] as const) assert.deepEqual(parseStructured(spouseWording(line.label, joint)).problems, [], `${line.id} label (${joint})`);
  }
  assert.ok(labelled > 0, "no built line label carries the spouse phrase");

  // The built questions: no near-miss, and each reworded text is still well-formed structured text.
  let phrased = 0;
  const seen = new Set<string>();
  for (const profile of ["social-security", "sales", "stage4", "full", "ny"]) {
    for (const q of loadInterview(profile).questions) {
      if (seen.has(q.input)) continue;
      seen.add(q.input);
      let has = false;
      for (const [field, text] of [["prompt", q.prompt], ["help", q.help]] as const) {
        assert.deepEqual(spousePhraseNearMisses(text), [], `${q.input} ${field}`);
        if (!text.includes(SPOUSE_PHRASE) && !text.includes(SPOUSE_POSSESSIVE)) continue;
        has = true;
        for (const joint of ["joint", "not-joint"] as const) {
          const shown = spouseWording(text, joint);
          assert.ok(shown !== text, `${q.input} ${field} (${joint}): not reworded`);
          assert.deepEqual(parseStructured(shown).problems, [], `${q.input} ${field} (${joint}): ${shown}`);
          assert.equal(shown.split("\n").length, text.split("\n").length, `${q.input} ${field} (${joint}): line count`);
        }
      }
      if (has) phrased++;
    }
  }
  assert.ok(phrased > 0, "no built question carries the spouse phrase");
  console.log(`spouse-wording self-test: passed (rewording, status reading, ${nearMisses.length} near-misses refused; ${phrased} of ${seen.size} built questions and ${labelled} line labels carry the phrase and parse in both readings)`);
  return 0;
}
