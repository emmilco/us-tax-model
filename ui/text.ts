// What the pages of the web UI share: building elements, the question text as blocks and paragraphs, and the call
// to the server's JSON API. Every piece of text becomes a text node, never markup.

export function el(tag: string, attrs: Record<string, string> = {}, ...children: (Node | string | null | undefined)[]): HTMLElement {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") e.className = v; else e.setAttribute(k, v);
  }
  for (const c of children) if (c !== null && c !== undefined) e.append(c);
  return e;
}
export function button(label: string | Node, attrs: Record<string, string> = {}, onclick?: () => void): HTMLButtonElement {
  const b = el("button", { type: "button", ...attrs }, label) as HTMLButtonElement;
  if (onclick) b.onclick = onclick;
  return b;
}

/** Structured text (the build-checked subset of engine/src/text.ts: one-line paragraphs separated by blank lines, a
 * heading, a line ending in ":", directly above a list, "- " bullets and "  - " nested bullets) as its blocks: <p>,
 * and <h4> or <ul> for a list and its heading. Every piece of text is a text node, never markup. Plain text (no line
 * break) is one <p>. */
export function textBlocks(text: string): HTMLElement[] {
  const blocks: HTMLElement[] = [];
  for (const chunk of text.split("\n\n")) {
    const lines = chunk.split("\n");
    const head = lines[0]!.startsWith("- ") ? null : lines.shift()!;
    if (lines.length === 0) { blocks.push(el("p", {}, head ?? "")); continue; }
    const list = el("ul");
    let item: HTMLElement | null = null;
    for (const line of lines) {
      if (line.startsWith("  - ") && item) {
        const sub = item.querySelector(":scope > ul") ?? item.appendChild(el("ul"));
        sub.append(el("li", {}, line.slice(4)));
      } else list.append(item = el("li", {}, line.replace(/^- /, "")));
    }
    // A heading stays with its list, so a fold never separates them.
    blocks.push(head === null ? list : el("div", { class: "text-list" }, el("h4", {}, head), list));
  }
  return blocks;
}
/** A label as HTML: plain text is one `tag` element, as always; structured text is `tag` (a <p> becomes a <div>)
 * holding its blocks. */
export function richText(tag: string, attrs: Record<string, string>, text: string): HTMLElement {
  if (!text.includes("\n")) return el(tag, attrs, text);
  return el(tag === "p" ? "div" : tag, { ...attrs, class: `${attrs.class ?? ""} structured`.trim() }, ...textBlocks(text));
}

// ---- long text ----
// Question text is reviewed form data and is shown word for word, always in full. A long text is broken into
// paragraphs at sentence ends; a very long explanation shows its opening and an explicit control for the rest.

const ABBREV = /(?:\b(?:e\.g|i\.e|etc|p|pp|No|Nos|U\.S|St|vs|Inc|Corp|Co|Jr|Sr|Mr|Ms|Dr|sec|Sec|Pub|Rev|Proc|Reg|Regs|ch|art|cl|par|para|approx|v)\.)$/;
function sentences(text: string): string[] {
  const out: string[] = [];
  let start = 0;
  const re = /[.?!]["”’)]?\s+(?=["“(]?[A-Z0-9])/g;
  for (const m of text.matchAll(re)) {
    const end = m.index! + m[0].trimEnd().length;
    if (ABBREV.test(text.slice(start, m.index! + 1))) continue;
    out.push(text.slice(start, end));
    start = m.index! + m[0].length;
  }
  out.push(text.slice(start));
  return out.filter((s) => s !== "");
}
function paragraphs(text: string, target = 420): string[] {
  const out: string[] = [];
  let cur = "";
  for (const s of sentences(text)) {
    if (cur && cur.length + s.length > target) { out.push(cur); cur = s; } else cur = cur ? `${cur} ${s}` : s;
  }
  if (cur) out.push(cur);
  return out;
}
const LONG = 900;
const OPENING = 520;
/** A text as paragraphs (structured text as its blocks); with `fold`, past LONG characters, the opening paragraphs or
 * blocks and a control that shows the rest. */
export function longText(text: string, cls: string, id: string, what: string, fold: boolean): HTMLElement {
  const box = el("div", { class: cls });
  const rest = el("div", { class: "rest", id: `${id}-rest`, hidden: "" });
  let shown = 0;
  if (text.includes("\n")) {
    box.classList.add("structured");
    const blocks = textBlocks(text);
    if (!fold || text.length <= LONG) { box.append(...blocks); return box; }
    blocks.forEach((b, i) => {
      const n = (b.textContent ?? "").length;
      if (i === 0 || shown + n <= OPENING) { box.append(b); shown += n; } else rest.append(b);
    });
  } else {
    const paras = paragraphs(text);
    if (!fold || text.length <= LONG) { box.append(...paras.map((p) => el("p", {}, p))); return box; }
    paras.forEach((p, i) => {
      if (i === 0 && p.length > LONG) {
        // One sentence longer than the limit: its opening words, then the remainder in the expandable part.
        const cut = p.lastIndexOf(" ", OPENING);
        box.append(el("p", {}, p.slice(0, cut), el("span", { class: "continues", "aria-hidden": "true" }, " …")));
        rest.append(el("p", { class: "continued" }, p.slice(cut + 1)));
        shown = OPENING;
      } else if (i === 0 || shown + p.length <= OPENING) { box.append(el("p", {}, p)); shown += p.length; }
      else rest.append(el("p", {}, p));
    });
  }
  if (!rest.childElementCount) return box;
  const remaining = text.length - shown;
  const label = `Read the rest of the ${what} (about ${(Math.max(1, Math.round(remaining / 100)) * 100).toLocaleString("en-US")} more characters)`;
  const toggle = button(label, { class: "expander", "aria-expanded": "false", "aria-controls": `${id}-rest` });
  toggle.onclick = () => {
    const open = rest.hidden === true;
    rest.hidden = !open;
    box.querySelector(".continues")?.toggleAttribute("hidden", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? `Show less of the ${what}` : label;
  };
  box.append(rest, toggle);
  return box;
}

export async function api<T>(method: string, path: string, body?: unknown): Promise<T> {
  const r = await fetch(path, { method, headers: body === undefined ? {} : { "Content-Type": "application/json" }, body: body === undefined ? null : JSON.stringify(body) });
  const payload = await r.json() as T & { error?: string };
  if (!r.ok) throw new Error(payload.error ?? `${r.status}`);
  return payload;
}
