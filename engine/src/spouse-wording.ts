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
// response. Other spouse wording ("(and, on a joint return, your spouse)") is not matched and is shown as stored.
//
// The per-person frame, "For this person (you, or your spouse on a joint return) — " before every question asked of a
// person on the return, is shown from the entry's role and the number of people on the return (`shownFor`):
//
//   the entry's role          two people on the return     one person on the return
//   taxpayer                  "About you — "               no frame
//   spouse                    "About your spouse — "       "About your spouse — "
//   not answered              as stored                    as stored
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

/** The frame the question bank puts before every question asked of a person on the return (the build checks the
 * bank's `person` frame is this text), and the frames shown in its place. */
export const PERSON_FRAME = "For this person (you, or your spouse on a joint return) — ";
export const ABOUT_YOU = "About you";
export const ABOUT_SPOUSE = "About your spouse";
const ROLE_OF = (person: string) => `person[${person}].role`;

/** The frame a per-person question is shown with: for a question whose stored prompt begins with PERSON_FRAME and
 * whose key lies in a person's entry, from that entry's role and the number of people on the return. "About your
 * spouse" for the spouse's entry; "About you" for the taxpayer's entry when the return lists more than one person;
 * the empty string (no frame) for the taxpayer's entry on a one-person return. Undefined (the stored frame is shown)
 * when the prompt has no frame, the key is in no person's entry, or the entry's role is not answered. */
export function personFrame(prompt: string, key: string, inputs: Inputs): string | undefined {
  if (!prompt.startsWith(PERSON_FRAME)) return undefined;
  const person = /(?:^|@|\.)person\[([a-zA-Z0-9_-]+)\]/.exec(key)?.[1];
  if (person === undefined) return undefined;
  const role = inputs[ROLE_OF(person)];
  if (role === "spouse") return ABOUT_SPOUSE;
  if (role !== "taxpayer") return undefined;
  const people = inputs["$person"];
  return Array.isArray(people) && people.length === 1 ? "" : ABOUT_YOU;
}

/** A prompt with its stored per-person frame replaced by `frame`: "About you — …", or, with no frame, the question
 * alone, its first letter a capital. */
export function framedPrompt(prompt: string, frame: string): string {
  const rest = prompt.slice(PERSON_FRAME.length);
  return frame ? `${frame} — ${rest}` : rest.charAt(0).toUpperCase() + rest.slice(1);
}

// ---- the person a framed question is about ----
// A framed question is stored in the second person: "you" and "your" are the person whose entry it is, "your spouse"
// is that person's husband or wife, and "this person" is the person again. It is shown for the entry it is asked of:
//
//   stored                          the taxpayer's entry     the spouse's entry
//   you (subject)                   you                      your spouse, the verb after it made to agree
//                                                            ("you have" -> "your spouse has", "you were" -> "your spouse was")
//   Were you / Do you / Have you    as stored                Was your spouse / Does your spouse / Has your spouse
//   you (object: "paid to you")     you                      your spouse
//   your                            your                     your spouse's
//   yours                           yours                    your spouse's
//   yourself                        yourself                 himself or herself
//   this person                     you, the verb agreeing   your spouse
//   this person's                   your                     your spouse's
//   you (this person)               you                      your spouse
//   your spouse                     your spouse              you, the verb agreeing ("your spouse was" -> "you were")
//   your spouse's                   your spouse's            your before a noun, yours otherwise
//   a phrase that means both people (COUPLE_PHRASES: "you and your spouse", "you or your spouse", "you both",
//   "either of you", ...)           as stored                as stored
//
// The rule works from closed lists. A subject ("you", "this person", "your spouse") must be followed by a verb the
// lists change (SECOND_TO_THIRD, THIRD_TO_SECOND) or by a word listed as needing no change (UNCHANGED_AFTER); a second
// verb joined by "or"/"and" ("had or were treated") and a verb after an apposition ("you, the HSA owner, are") are
// changed too. Anything else is reported by `personWordingProblems`, which the build runs on every framed prompt and
// help: a "you" before a word in neither list, a contraction ("you're"), and a verb the lists change standing after a
// preposition and its object ("of this person reports"), where the rule cannot tell whose verb it is. So a framed
// question the rule does not cover fails the build until it is reworded or its word is listed here.

/** Phrases of a framed question that mean both people, the same whichever entry the question is asked of. */
export const COUPLE_PHRASES = ["you (or your spouse, on a joint return)", "you, or your spouse on a joint return", "you and your spouse", "you or your spouse",
  "yours or your spouse's", "your or your spouse's", "your and your spouse's", "either of you", "both of you", "you both"];
/** The auxiliary before "you" in a question, as it reads before "your spouse". */
const AUXILIARY: Record<string, string> = { were: "was", are: "is", do: "does", have: "has", did: "did", can: "can", could: "could" };
/** A verb after "you", as it reads after "your spouse". */
export const SECOND_TO_THIRD: Record<string, string> = { are: "is", were: "was", have: "has", "weren't": "wasn't", "aren't": "isn't", "don't": "doesn't",
  file: "files", teach: "teaches", contribute: "contributes", receive: "receives", stop: "stops" };
/** A verb after "this person" or "your spouse", as it reads after "you". */
export const THIRD_TO_SECOND: Record<string, string> = { is: "are", was: "were", has: "have", does: "do", "isn't": "aren't", "wasn't": "weren't", "doesn't": "don't" };
/** The words that may follow a subject and read the same for either person: past forms, modals, and the words after
 * an object ("gave you a", "paid you overtime"). */
export const UNCHANGED_AFTER: ReadonlySet<string> = new Set(["a", "an", "and", "or", "for", "to", "on", "if", "as", "by", "in", "of", "at", "under", "with", "more", "age", "blind",
  "fully", "never", "overtime", "born", "made", "had", "took", "received", "enrolled", "filed", "applied", "applying", "can", "can't", "cannot", "could", "contributed", "did",
  "paid", "died", "acquired", "repaid", "served", "rolled", "became", "claimed", "deducted", "recharacterized", "covered", "deferred", "agreed"]);
const PREPOSITIONS: ReadonlySet<string> = new Set(["of", "for", "to", "by", "from", "with", "about", "on", "in"]);
/** Whose entry a framed question is shown for. */
export type PersonRole = "taxpayer" | "spouse";

const escapeRe = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const capitalLike = (s: string, like: string) => (/^[A-Z]/.test(like) ? s.charAt(0).toUpperCase() + s.slice(1) : s);
const WORD = "[A-Za-z][A-Za-z'’-]*";
const PERSON_RE = new RegExp([
  `(?<couple>\\b(?:${COUPLE_PHRASES.map(escapeRe).join("|")})(?![A-Za-z]))`,
  `(?<sp>\\byour spouse(?<sps>['’]s)?)(?![A-Za-z])`,
  `(?<aux>\\b(?:${Object.keys(AUXILIARY).join("|")}))\\s+you\\b(?!['’])`,
  `(?<tp>\\bthis person(?<tps>['’]s)?)(?![A-Za-z])`,
  `(?<self>\\byourself\\b)`,
  `(?<yours>\\byours\\b)`,
  `(?<your>\\byour\\b)`,
  `(?<you>\\byou\\b)(?!['’])`,
].join("|"), "gi");

/** A framed question's text (its prompt after the frame, or its help) as shown for an entry of `role`; what the rule
 * does not cover is added to `problems`. A curly apostrophe is read as a straight one; the text's own kind is written. */
export function personWording(stored: string, role: PersonRole, problems: string[] = []): string {
  const apostrophe = stored.includes("’") && !stored.includes("'") ? "’" : "'";
  const verb = (table: Record<string, string>, w: string): string | undefined => table[w.toLowerCase().replaceAll("’", "'")]?.replaceAll("'", apostrophe);
  const text = stored.replace(/\b([Yy])ou \(this person\)/g, "$1ou");
  for (const m of text.matchAll(/\byou['’][a-z]+/gi)) problems.push(`"${m[0]}": write the verb out ("you are", "you have")`);
  let out = "", last = 0;
  for (const mm of text.matchAll(PERSON_RE)) {
    const g = mm.groups!, m = mm[0], at = mm.index;
    if (at < last) continue;
    let end = at + m.length, rep = m;
    const prev = /([A-Za-z']+)\W*$/.exec(text.slice(0, at))?.[1]?.toLowerCase() ?? "";
    // A subject and the verb after it: a verb of `table` is made to agree; any other word must need no change.
    const subject = (base: string, table: Record<string, string>): string => {
      let made = capitalLike(base, m);
      const rest = text.slice(end);
      const apposition = new RegExp(`^(, [^,.;:?()]{1,40}, )(${WORD})`).exec(rest);
      if (apposition && verb(table, apposition[2]!)) { end += apposition[0].length; return made + apposition[1]! + verb(table, apposition[2]!)!; }
      const next = new RegExp(`^(\\s+)(${WORD})`).exec(rest);
      if (!next) return made;
      const w = next[2]!.toLowerCase().replaceAll("’", "'");
      if (verb(table, w)) {
        if (PREPOSITIONS.has(prev)) { problems.push(`"${prev} ${m} ${next[2]}": after a preposition the rule cannot tell whose verb "${next[2]}" is; reword it`); return made; }
        end += next[0].length; made += next[1]! + verb(table, w)!;
      } else if (!UNCHANGED_AFTER.has(w)) { problems.push(`"${m} ${next[2]}": "${next[2]}" is in neither list of spouse-wording.ts (a verb that changes with the subject, or a word that does not)`); return made; }
      else { end += next[0].length; made += next[0]; }
      const second = new RegExp(`^(\\s+(?:or|and)\\s+)(${WORD})`).exec(text.slice(end));
      if (second && verb(table, second[2]!)) { end += second[0].length; made += second[1]! + verb(table, second[2]!)!; }
      return made;
    };
    if (g["couple"]) rep = m;
    else if (role === "spouse") {
      if (g["sp"]) rep = g["sps"] ? capitalLike(new RegExp(`^\\s+(?!(?:or|and)\\b)${WORD}`).test(text.slice(end)) ? "your" : "yours", m) : subject("you", THIRD_TO_SECOND);
      else if (g["aux"]) rep = capitalLike(AUXILIARY[g["aux"].toLowerCase()]!, g["aux"]) + " your spouse";
      else if (g["tp"]) rep = capitalLike(g["tps"] ? `your spouse${apostrophe}s` : "your spouse", m);
      else if (g["self"]) rep = "himself or herself";
      else if (g["yours"] || g["your"]) rep = capitalLike(`your spouse${apostrophe}s`, m);
      else rep = subject("your spouse", SECOND_TO_THIRD);
    } else if (g["tp"]) rep = g["tps"] ? capitalLike("your", m) : subject("you", THIRD_TO_SECOND);
    out += text.slice(last, at) + rep;
    last = end;
  }
  return out + text.slice(last);
}

/** What the person rule does not cover in a framed question (none for a question without the frame): each problem
 * names the words. The build fails on any. */
export function personWordingProblems(q: { prompt: string; help: string }): string[] {
  if (!q.prompt.startsWith(PERSON_FRAME)) return [];
  const problems: string[] = [];
  for (const text of [q.prompt.slice(PERSON_FRAME.length), q.help]) for (const role of ["taxpayer", "spouse"] as const) personWording(text, role, problems);
  return [...new Set(problems)];
}

/** A question as shown for the input `key` on the return with these answers: the spouse phrase reworded for the
 * filing status, the per-person frame for the entry's role, and the person the question is about named for that
 * role (`personWording`). `frame` is set when the stored frame was replaced by a shown one ("About you", "About
 * your spouse"). */
export function shownFor<Q extends { prompt: string; help: string }>(q: Q, key: string, inputs: Inputs): Q & { frame?: string } {
  const shown = shownQuestion(q, jointReturn(inputs));
  const frame = personFrame(q.prompt, key, inputs);
  if (frame === undefined) return shown;
  const role: PersonRole = frame === ABOUT_SPOUSE ? "spouse" : "taxpayer";
  const rest = personWording(shown.prompt.slice(PERSON_FRAME.length), role);
  return { ...shown, prompt: framedPrompt(PERSON_FRAME + rest, frame), help: personWording(shown.help, role), ...(frame ? { frame } : {}) };
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

  // The per-person frame as shown: from the entry's role and the number of people on the return.
  const blind = { prompt: `${PERSON_FRAME}Were you blind at the end of 2025?`, help: "All your (or, on a joint return, your spouse's) answer." };
  const two = { "$person": ["taxpayer", "spouse"], "person[taxpayer].role": "taxpayer", "person[spouse].role": "spouse", [STATUS_INPUT]: JOINT_STATUS };
  const one = { "$person": ["taxpayer"], "person[taxpayer].role": "taxpayer", [STATUS_INPUT]: "single" };
  assert.deepEqual(shownFor(blind, "person[taxpayer].blind", two), { prompt: "About you — Were you blind at the end of 2025?", help: "All your or your spouse's answer.", frame: ABOUT_YOU });
  assert.deepEqual(shownFor(blind, "person[spouse].blind", two), { prompt: "About your spouse — Was your spouse blind at the end of 2025?", help: "All your or your spouse's answer.", frame: ABOUT_SPOUSE });
  assert.deepEqual(shownFor(blind, "person[taxpayer].blind", one), { prompt: "Were you blind at the end of 2025?", help: "All your answer." });
  // A roster under a person and an entry under it take the person's frame; the frame's removal capitalises the question.
  assert.equal(shownFor({ prompt: `${PERSON_FRAME}List the employers.`, help: "" }, "$w2@person[spouse]", two).prompt, "About your spouse — List the employers.");
  assert.equal(shownFor({ prompt: `${PERSON_FRAME}the part allocated to this person.`, help: "" }, "person[taxpayer].f8889[hsa].allocated", one).prompt, "The part allocated to you.");
  assert.equal(shownFor({ prompt: `${PERSON_FRAME}the part allocated to this person.`, help: "" }, "person[taxpayer].f8889[hsa].allocated", two).prompt, "About you — the part allocated to you.");
  // The role decides, not the entry's key or the filing status; two people on a return that is not joint are still told apart.
  const swapped = { "$person": ["a", "b"], "person[a].role": "spouse", "person[b].role": "taxpayer", [STATUS_INPUT]: "single" };
  assert.equal(shownFor(blind, "person[a].blind", swapped).frame, ABOUT_SPOUSE);
  assert.equal(shownFor(blind, "person[b].blind", swapped).frame, ABOUT_YOU);
  // The stored frame is shown while the entry's role is unanswered, on a key in no person's entry, and where the prompt has no frame.
  for (const [key, inputs] of [["person[taxpayer].blind", { "$person": ["taxpayer"] }], ["person[taxpayer].blind", { ...one, "person[taxpayer].role": null }], ["f1040.line2a", one]] as const) {
    assert.deepEqual(shownFor(blind, key, inputs), { prompt: blind.prompt, help: spouseWording(blind.help, jointReturn(inputs)) }, key);
  }
  assert.deepEqual(shownFor({ prompt: "For this business — What did it sell?", help: "" }, "person[taxpayer].sc[shop].sells", two), { prompt: "For this business — What did it sell?", help: "" });
  assert.equal(personFrame(`Note. ${PERSON_FRAME}Were you blind?`, "person[spouse].blind", two), undefined, "a frame is at the start of the prompt");

  // The person a framed question is about, named for the entry: each row of the rule, for the spouse and for the taxpayer.
  const rows: [string, string, string][] = [
    // stored, shown for the spouse, shown for the taxpayer
    ["Were you born before 1961? If you were, say so.", "Was your spouse born before 1961? If your spouse was, say so.", "Were you born before 1961? If you were, say so."],
    ["Do you have an SSN? Have you applied, or are you applying?", "Does your spouse have an SSN? Has your spouse applied, or is your spouse applying?", "Do you have an SSN? Have you applied, or are you applying?"],
    ["Did you file Form CT-2 before you file this return, and can you show it?", "Did your spouse file Form CT-2 before your spouse files this return, and can your spouse show it?", "Did you file Form CT-2 before you file this return, and can you show it?"],
    ["If you weren't blind and you have a statement that you can't see, answer yes.", "If your spouse wasn't blind and your spouse has a statement that your spouse can't see, answer yes.", "If you weren't blind and you have a statement that you can't see, answer yes."],
    ["The coverage you had or were treated as having; if you, the owner, are under 65, zero.", "The coverage your spouse had or was treated as having; if your spouse, the owner, is under 65, zero.", "The coverage you had or were treated as having; if you, the owner, are under 65, zero."],
    ["The employers that gave you a Form W-2, the tips paid to you, and wages paid by you.", "The employers that gave your spouse a Form W-2, the tips paid to your spouse, and wages paid by your spouse.", "The employers that gave you a Form W-2, the tips paid to you, and wages paid by you."],
    ["Your wages in box 1 of your Form W-2; another HSA of yours.", "Your spouse's wages in box 1 of your spouse's Form W-2; another HSA of your spouse's.", "Your wages in box 1 of your Form W-2; another HSA of yours."],
    ["Contributions you made for yourself to your SEP IRA.", "Contributions your spouse made for himself or herself to your spouse's SEP IRA.", "Contributions you made for yourself to your SEP IRA."],
    ["Yes if this person was born before 1961; this person's age counts. This person has a card.", "Yes if your spouse was born before 1961; your spouse's age counts. Your spouse has a card.", "Yes if you were born before 1961; your age counts. You have a card."],
    ["Did you (this person) contribute?", "Did your spouse contribute?", "Did you contribute?"],
    ["A year you did not file a joint return with your spouse; your spouse was abroad; your spouse's plan, or coverage under a plan (your spouse's or a parent's).", "A year your spouse did not file a joint return with you; you were abroad; your plan, or coverage under a plan (yours or a parent's).", "A year you did not file a joint return with your spouse; your spouse was abroad; your spouse's plan, or coverage under a plan (your spouse's or a parent's)."],
    // Phrases that mean both people read the same for either entry, inside a longer clause too.
    ["If you and your spouse were both eligible and either of you had family coverage, answer family for both of you; you both agree.", "If you and your spouse were both eligible and either of you had family coverage, answer family for both of you; you both agree.", "If you and your spouse were both eligible and either of you had family coverage, answer family for both of you; you both agree."],
    ["Expenses of you or your spouse, yours or your spouse's; you (or your spouse, on a joint return) could be claimed; you, or your spouse on a joint return.", "Expenses of you or your spouse, yours or your spouse's; you (or your spouse, on a joint return) could be claimed; you, or your spouse on a joint return.", "Expenses of you or your spouse, yours or your spouse's; you (or your spouse, on a joint return) could be claimed; you, or your spouse on a joint return."],
    ["If you’re not sure, don’t guess; your spouse’s plan and your card.", "If you’re not sure, don’t guess; your plan and your spouse’s card.", "If you’re not sure, don’t guess; your spouse’s plan and your card."],
  ];
  for (const [stored, forSpouse, forTaxpayer] of rows) {
    assert.equal(personWording(stored, "spouse"), forSpouse, stored);
    assert.equal(personWording(stored, "taxpayer"), forTaxpayer, stored);
  }
  // What the rule does not cover is a problem the build fails on: a verb in neither list, a contraction, a verb after a
  // preposition's object; a covered text and a question without the frame have none.
  const framedQ = (text: string, help = "") => ({ prompt: PERSON_FRAME + text, help });
  const uncovered: [{ prompt: string; help: string }, RegExp][] = [
    [framedQ("The courses you swim in."), /"you swim": "swim" is in neither list/],
    [framedQ("Answer.", "Yes if this person reports it."), /"this person reports": "reports" is in neither list/],
    [framedQ("If you're not sure, answer no."), /"you're": write the verb out/],
    [framedQ("If any Form W-2 of this person is wrong."), /"of this person is": after a preposition the rule cannot tell whose verb "is" is/],
    [framedQ("The amount paid to you are wages."), /"to you are": after a preposition/],
    [framedQ("Your spouse thinks so."), /"Your spouse thinks": "thinks" is in neither list/],
  ];
  for (const [q, flagged] of uncovered) assert.match(personWordingProblems(q).join("\n"), flagged, q.prompt + q.help);
  for (const [stored] of rows.slice(0, -1)) assert.deepEqual(personWordingProblems(framedQ(stored)), [], stored);
  assert.deepEqual(personWordingProblems({ prompt: "The courses you swim in, if you're sure.", help: "" }), [], "a question without the frame is not held to the rule");
  // As shown: the spouse phrase first, then the person; the help too.
  assert.deepEqual(shownFor({ prompt: `${PERSON_FRAME}Did you take a distribution your employer reported?`, help: "Your spouse's plan is not yours. Ask if you have one." }, "person[spouse].x", two),
    { prompt: "About your spouse — Did your spouse take a distribution your spouse's employer reported?", help: "Your plan is not your spouse's. Ask if your spouse has one.", frame: ABOUT_SPOUSE });

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
  let phrased = 0, framed = 0;
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
      // The per-person frame: only at the start of a prompt, and each shown form is still well-formed structured text.
      assert.ok(!q.help.includes(PERSON_FRAME) && q.prompt.lastIndexOf(PERSON_FRAME) <= 0, `${q.input}: the per-person frame is only at the start of a prompt`);
      if (!q.prompt.startsWith(PERSON_FRAME)) continue;
      framed++;
      assert.deepEqual(personWordingProblems(q), [], `${q.input}: the person rule covers its wording`);
      for (const [title, person, inputs] of SHOWN_ON) {
        const shown = shownFor(q, keyFor(q.input, person), inputs);
        for (const field of ["prompt", "help"] as const) {
          assert.deepEqual(parseStructured(shown[field]).problems, [], `${q.input} ${field} (${title}): ${shown[field]}`);
          assert.equal(shown[field].split("\n").length, q[field].split("\n").length, `${q.input} ${field} (${title}): line count`);
          assert.ok(!shown[field].includes("this person") && !shown[field].includes(PERSON_FRAME), `${q.input} ${field} (${title}): no "this person" and no stored frame is shown`);
        }
        assert.ok(/^[^a-z]/.test(shown.prompt), `${q.input} prompt (${title}) begins with a capital or a figure: ${shown.prompt}`);
      }
    }
  }
  assert.ok(phrased > 0, "no built question carries the spouse phrase");
  assert.ok(framed > 0, "no built question carries the per-person frame");
  console.log(`spouse-wording self-test: passed (rewording, status reading, ${nearMisses.length} near-misses refused; ${phrased} of ${seen.size} built questions and ${labelled} line labels carry the phrase and parse in both readings; the per-person frame by role and number of people; the person named for the entry, ${rows.length} constructed texts and ${uncovered.length} uncovered wordings refused; ${framed} built questions carry the frame, are covered by the rule and parse in each shown form)`);
  return 0;
}

// ---- the report of shown forms ----

/** A key of the input template `template` in the entry of the person `person` (shownFor reads only the person). */
function keyFor(template: string, person: string): string {
  if (template.startsWith("$")) return `${template}@person[${person}]`;
  const [doc, field] = template.split(".") as [string, string];
  return doc === "person" ? `person[${person}].${field}` : `person[${person}].${doc}[entry].${field}`;
}

const COUPLE_RETURN: Inputs = { "$person": ["taxpayer", "spouse"], "person[taxpayer].role": "taxpayer", "person[spouse].role": "spouse", [STATUS_INPUT]: JOINT_STATUS };
/** The three ways a framed question is shown: on a return with one person; on a couple's, for the taxpayer's entry and for the spouse's. */
const SHOWN_ON: [string, string, Inputs][] = [
  ["Shown on a one-person return", "taxpayer", { "$person": ["taxpayer"], "person[taxpayer].role": "taxpayer", [STATUS_INPUT]: "single" }],
  ["Shown for you on a couple's return", "taxpayer", COUPLE_RETURN],
  ["Shown for your spouse", "spouse", COUPLE_RETURN],
];

/** reports/<year>/person_wording.md: every framed question as stored and in each form it is shown in, prompt and help,
 * made through `shownFor`, so a change of the rule or of a stored question is a readable difference. */
export function personWordingReport(): string {
  const seen = new Set<string>();
  const questions = ["full", "ny"].flatMap((p) => loadInterview(p).questions).filter((q) => !seen.has(q.input) && seen.add(q.input) && q.prompt.startsWith(PERSON_FRAME));
  const quote = (text: string) => text.split("\n").map((l) => `> ${l}`.trimEnd()).join("\n");
  const list = (words: Iterable<string>) => [...words].map((w) => `"${w}"`).join(", ");
  const pairs = (table: Record<string, string>) => Object.entries(table).map(([a, b]) => `"${a}" to "${b}"`).join(", ");
  const out = [
    "# Questions asked of a person, as stored and as shown",
    "",
    "Written by `node engine/dist/main.js spouse-wording --report`; check-all fails when it is not current (`--report --check`).",
    "",
    `A question asked of a person on the return is stored once, in the second person, after the frame "${PERSON_FRAME.trim()}". It is shown for`,
    "the entry it is asked of (`shownFor` in `engine/src/spouse-wording.ts`): with no frame on a return with one person, after \"About you\" for the",
    "taxpayer's entry of a couple's return, and after \"About your spouse\" for the spouse's entry, where the person is named in the third person.",
    "The reviews read the stored text; this report is the record of the shown text.",
    "",
    "How each word of the stored text is shown for the spouse's entry:",
    "",
    "| Stored | Shown for the spouse | Example |",
    "|---|---|---|",
    `| "you" as a subject | "your spouse", and the verb after it agrees | "you have" to "your spouse has"; "you were" to "your spouse was" |`,
    `| a question's auxiliary and "you" | the auxiliary agrees | ${pairs(Object.fromEntries(Object.entries(AUXILIARY).filter(([a, b]) => a !== b).map(([a, b]) => [`${a} you`, `${b} your spouse`])))}; "did you", "can you" and "could you" keep their auxiliary |`,
    `| a second verb joined by "or" or "and" | agrees too | "you had or were treated" to "your spouse had or was treated" |`,
    `| a verb after an apposition | agrees too | "you, the HSA owner, are" to "your spouse, the HSA owner, is" |`,
    `| "you" as an object | "your spouse" | "paid to you" to "paid to your spouse"; "gave you a Form W-2" to "gave your spouse a Form W-2" |`,
    `| "your" | "your spouse's" | "your Form W-2" to "your spouse's Form W-2" |`,
    `| "yours" | "your spouse's" | "another HSA of yours" to "another HSA of your spouse's" |`,
    `| "yourself" | "himself or herself" | "contributions you made for yourself" to "contributions your spouse made for himself or herself" |`,
    `| "this person", "this person's", "you (this person)" | "your spouse", "your spouse's", "your spouse" | "allocated to this person" to "allocated to your spouse" |`,
    `| "your spouse" (the husband or wife of the person asked about) | "you", and the verb after it agrees | "a joint return with your spouse" to "a joint return with you" |`,
    `| "your spouse's" | "your" before a noun, "yours" otherwise | "your spouse's Archer MSA" to "your Archer MSA"; "(your spouse's or a parent's)" to "(yours or a parent's)" |`,
    `| a phrase that means both people | as stored | ${list(COUPLE_PHRASES)} |`,
    "",
    "For the taxpayer's entry only \"this person\" changes: \"this person\" to \"you\" with the verb agreeing (\"this person was\" to \"you were\"),",
    "\"this person's\" to \"your\", \"you (this person)\" to \"you\".",
    "",
    "The closed lists the rule works from (a framed question with a subject before a word in neither list fails the build):",
    "",
    `- verbs after "you" that change for "your spouse": ${pairs(SECOND_TO_THIRD)}`,
    `- verbs after "this person" or "your spouse" that change for "you": ${pairs(THIRD_TO_SECOND)}`,
    `- words after a subject or an object that need no change: ${list([...UNCHANGED_AFTER].sort())}`,
    "",
    `${questions.length} questions carry the frame.`,
    "",
  ];
  for (const q of questions) {
    out.push(`## \`${q.input}\``, "");
    for (const field of ["prompt", "help"] as const) {
      if (!q[field]) continue;
      out.push(`**${field === "prompt" ? "Question" : "Help"}, as stored**`, "", quote(q[field]), "");
      for (const [title, person, inputs] of SHOWN_ON) out.push(`${title}:`, "", quote(shownFor(q, keyFor(q.input, person), inputs)[field]), "");
    }
  }
  return out.join("\n");
}
