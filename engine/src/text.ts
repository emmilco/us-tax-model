// Structured text: the small Markdown subset that form text shown as a question or help may use (a line's
// `label`, an input's `source`, a `note`, and a question bank's `prompt` and `help`).
//
// Text with no line break is plain text, as before, and every consumer shows it unchanged. Text with a line
// break is structured and must be, line by line:
//
//   - a paragraph: one line of text (no hard wrapping); the first line is always a paragraph, the question;
//   - a heading: one line ending in ":", of at most HEADING_MAX characters, directly above a list;
//   - a bullet: "- " and its text;
//   - a nested bullet: "  - " and its text, directly below a bullet or another nested bullet (one level);
//   - a blank line, between blocks: one, never two, never first or last.
//
// A list follows a heading or a blank line and ends at a blank line. Nothing else is markup: no other
// indentation, no "#", "*", "+", ">", "|", numbered or code lines, no inline emphasis, code, links or HTML.
// The text as authored is canonical: it is already the plain-text form, so plain consumers indent its
// continuation lines (indentRest) and the page renders the same blocks as HTML.

export const HEADING_MAX = 80;

export type Block =
  | { kind: "paragraph"; text: string }
  | { kind: "list"; heading: string | null; items: { text: string; items: string[] }[] };

/** Whether text uses the structured form (has a line break). */
export function isStructured(text: string): boolean {
  return text.includes("\n");
}

/** The first line: how a structured text is named where one line is wanted (a reference, a heading, a link). */
export function textSummary(text: string): string {
  const i = text.indexOf("\n");
  return i < 0 ? text : text.slice(0, i);
}

/** The text with every continuation line prefixed by `pad` (blank lines stay empty), for a plain-text
 * consumer that prints it after a prefix. Plain text is returned unchanged. */
export function indentRest(text: string, pad: string): string {
  if (!isStructured(text)) return text;
  return text.split("\n").map((l, i) => (i === 0 || l === "" ? l : pad + l)).join("\n");
}

/** The text on one line, each line break and the indentation around it a single space, for a consumer that has
 * only one line (a table cell). Plain text is returned unchanged. */
export function flatText(text: string): string {
  return isStructured(text) ? text.replace(/\s*\n\s*/g, " ") : text;
}

const BULLET = /^- (\S.*)$/;
const NESTED = /^ {2}- (\S.*)$/;
// Inline characters with a Markdown meaning; `_` only where it could open or close emphasis.
const INLINE = /[`*<>\\|]|\]\(|(^|[^A-Za-z0-9])_|_([^A-Za-z0-9]|$)/;
const BLOCK_START = /^(#|\+ |\* |\d+[.)] |>|-{3,}$|={3,}$|_{3,}$)/;

function inlineProblem(text: string): string | null {
  if (BLOCK_START.test(text)) return "starts with Markdown block syntax";
  if (INLINE.test(text)) return "has inline Markdown (`, *, _ emphasis, <, >, \\, |, or a link)";
  return null;
}

/** The blocks of a structured text and its problems (empty when it is well formed). Plain text has no
 * problems and is one paragraph. */
export function parseStructured(text: string): { blocks: Block[]; problems: string[] } {
  if (!isStructured(text)) return { blocks: [{ kind: "paragraph", text }], problems: [] };
  const problems: string[] = [];
  const lines = text.split("\n");
  const at = (i: number) => `line ${i + 1}`;
  const blocks: Block[] = [];
  let list: Extract<Block, { kind: "list" }> | null = null;
  lines.forEach((line, i) => {
    const next = lines[i + 1];
    const prev = i > 0 ? lines[i - 1]! : null;
    if (/[\t\r]/.test(line)) problems.push(`${at(i)}: has a tab or carriage return`);
    if (line !== line.trimEnd()) problems.push(`${at(i)}: has trailing spaces`);
    if (line === "") {
      if (i === 0 || i === lines.length - 1) problems.push(`${at(i)}: a blank line is only allowed between blocks`);
      else if (prev === "") problems.push(`${at(i)}: two blank lines in a row`);
      list = null;
      return;
    }
    const bullet = BULLET.exec(line);
    const nested = NESTED.exec(line);
    if (bullet || nested) {
      const body = (bullet ?? nested)![1]!;
      const p = inlineProblem(body);
      if (p) problems.push(`${at(i)}: the bullet ${p}`);
      if (i === 0) { problems.push(`${at(i)}: the first line must be the question, not a bullet`); return; }
      if (nested) {
        if (!list || list.items.length === 0) { problems.push(`${at(i)}: a nested bullet must follow a bullet`); return; }
        list.items[list.items.length - 1]!.items.push(body);
        return;
      }
      if (!list) {
        // A list starts after a blank line, or after the heading line directly above it.
        if (prev === "") list = { kind: "list", heading: null, items: [] };
        else problems.push(`${at(i)}: a list must follow a blank line or a heading (a short line ending in ":")`);
        if (list) blocks.push(list);
      }
      list?.items.push({ text: body, items: [] });
      return;
    }
    if (/^\s/.test(line)) { problems.push(`${at(i)}: indented line that is not a nested bullet ("  - ")`); return; }
    const p = inlineProblem(line);
    if (p) problems.push(`${at(i)}: the line ${p}`);
    if (prev !== null && prev !== "") {
      problems.push(`${at(i)}: a paragraph or heading must follow a blank line (one line per paragraph; end a list with a blank line)`);
    }
    list = null;
    const headsList = next !== undefined && BULLET.test(next);
    if (headsList && i > 0) {
      if (!line.endsWith(":")) problems.push(`${at(i)}: a line directly above a list is a heading and must end with ":"`);
      if (line.length > HEADING_MAX) problems.push(`${at(i)}: a heading is at most ${HEADING_MAX} characters`);
      list = { kind: "list", heading: line, items: [] };
      blocks.push(list);
      return;
    }
    if (headsList) problems.push(`${at(i)}: the first line must be the question, followed by a blank line`);
    blocks.push({ kind: "paragraph", text: line });
  });
  return { blocks, problems };
}
