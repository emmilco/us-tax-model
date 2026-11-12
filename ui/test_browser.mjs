// SPDX-License-Identifier: Apache-2.0
// Smoke test of the web UI in a separately launched headless Chrome on port 9227, run by hand (not in check-all):
//   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --remote-debugging-port=9227 \
//     --user-data-dir="$(mktemp -d)" about:blank &
//   npm run compile && node ui/test_browser.mjs
// It starts `serve` on a temporary returns directory and walks a synthetic New York return (the fixture
// ny.refuse.part_year_state) through the page: every answer through the page's widgets, a blank amount refused
// without writing, an earlier answer corrected, a derivation opened and followed to the answer it depends on, and the
// provisional refusal becoming final once nothing is pending. The answered list, the values sheets and the scope and
// notices are tabs; a refusal's details open in a dialog. A question that names forms lists them under its
// explanation, each with its title and quoted purpose. Screenshots of each view go to /private/tmp/tax-ui-design-*.png,
// and of the forms a question names to /private/tmp/tax-ui-glosses.png. A second return, written as a log, has
// conflicting Form 8889 month answers: it is shown as a conflict with links to the answers involved, not as a
// refusal (screenshot /private/tmp/tax-ui-conflict.png). Every question shows its id: in the answered list and under
// the current question (screenshots /private/tmp/tax-ui-design-{answered-ids,question-id}.png).
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const { loadCanonical } = await import(join(root, "engine/dist/canonical.js"));
const { loadFixtureCases } = await import(join(root, "engine/dist/fixture-inputs.js"));
const canonical = loadCanonical();
const { inputs } = loadFixtureCases("ny", canonical).find(c => c.id === "ny.refuse.part_year_state");

const wait = ms => new Promise(r => setTimeout(r, ms));
const fmtMoney = c => { const d = Math.floor(Math.abs(c) / 100).toLocaleString("en-US"), r = Math.abs(c) % 100; return `${c < 0 ? "-" : ""}$${d}${r ? "." + String(r).padStart(2, "0") : ""}`; };
const pages = await fetch("http://127.0.0.1:9227/json/list").then(r => r.json());
const page = pages.find(p => p.type === "page");
assert(page, "launch a separate headless Chrome on port 9227 first");
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((ok, fail) => { ws.addEventListener("open", ok); ws.addEventListener("error", fail); });
let id = 0;
const pending = new Map(), errors = [];
ws.addEventListener("message", e => {
  const msg = JSON.parse(e.data);
  if (msg.id) {
    const task = pending.get(msg.id); pending.delete(msg.id);
    if (msg.error) task.reject(new Error(JSON.stringify(msg.error))); else task.resolve(msg.result);
  } else if (msg.method === "Runtime.exceptionThrown") errors.push(msg.params.exceptionDetails.exception?.description ?? msg.params.exceptionDetails.text);
});
const cdp = (method, params = {}) => new Promise((ok, fail) => { const n = ++id; pending.set(n, { resolve: ok, reject: fail }); ws.send(JSON.stringify({ id: n, method, params })); });
async function evaluate(expression) {
  const r = await cdp("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true });
  assert(!r.exceptionDetails, JSON.stringify(r.exceptionDetails));
  return r.result.value;
}
async function until(expression, what) {
  for (let i = 0; i < 200; i++) { if (await evaluate(expression)) return; await wait(50); }
  throw new Error(`timed out waiting for ${what}`);
}
async function click(selector) {
  const point = await evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});if(!e)return null;
    e.scrollIntoView({block:'center',behavior:'instant'});const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);
  assert(point, `no element ${selector}`);
  await cdp("Input.dispatchMouseEvent", { type: "mousePressed", button: "left", clickCount: 1, ...point });
  await cdp("Input.dispatchMouseEvent", { type: "mouseReleased", button: "left", clickCount: 1, ...point });
}
async function type(selector, text) {
  await evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});e.focus();e.value='';})()`);
  await cdp("Input.insertText", { text });
}
async function screenshot(path) {
  const r = await cdp("Page.captureScreenshot", { format: "png" });
  writeFileSync(path, Buffer.from(r.data, "base64"));
}
const view = async name => { await click(`#tab-${name}`); await until(`!document.getElementById('panel-${name}').hidden`, `the ${name} view`); };
const shot = name => screenshot(`/private/tmp/tax-ui-design-${name}.png`);
const question = () => evaluate("document.querySelector('.question[data-input]')?.dataset.input ?? null");
const banner = () => evaluate("document.getElementById('status-banner').textContent");
const logLines = () => readFileSync(join(dir, "smoke.jsonl"), "utf8").trim().split("\n").length;

/** Answers the question on the page with `value` through its widget and waits for the page to move on. */
// The page derives entry keys from the labels typed, so its keys differ from the fixture's: pathMap maps each fixture
// entry path to the page's, and fx() turns a page input key back into the fixture's.
const pathMap = new Map();
const fx = key => { let k = key; for (const [f, p] of [...pathMap].sort((a, b) => b[1].length - a[1].length)) k = k.split(p + "]").join(f + "]").split(p + ".").join(f + "."); return k; };
const entryPath = (roster, key) => { const [coll, parent] = roster.slice(1).split("@"); return `${parent ? parent + "." : ""}${coll}[${key}]`; };
const labelsFor = (roster, keys) => roster === "$w2@person[taxpayer]" ? ["Acme Corp.", "Acme Corp"].slice(0, keys.length).concat(keys.slice(2).map((_, i) => `Acme ${i + 3}`)) : keys.map((_, i) => `Entry ${i + 1}`);
let origin, docTitles, docDesignations, rosterShot = false, longShot = false;
const served = () => fetch(`${origin}/api/returns/smoke`).then(r => r.json());

/** Answers the question on the page with the fixture's `value` through its widget and waits for the page to move on. */
async function answer(input, value) {
  const before = logLines();
  const kind = await evaluate("document.querySelector('.widget [data-choice]') ? 'choice' : document.querySelector('.widget [data-value]') ? 'value' : document.querySelector('.widget #roster') ? 'roster' : document.querySelector('.widget [data-answer]') ? 'bool' : document.querySelector('.widget select') ? 'enum' : 'text'");
  if (kind === "bool") await click(`.widget [data-answer=${value ? "yes" : "no"}]`);
  else if (kind === "value") await click(`.widget [data-value="${value}"]`);
  else if (kind === "enum") { await evaluate(`document.querySelector('.widget select').value=${JSON.stringify(value)}`); await click("#answer-submit"); }
  else if (kind === "choice") {
    const q = (await served()).pending.find(p => p.input === input);
    const i = q.choices.findIndex(c => JSON.stringify(c.value) === JSON.stringify(value.map(k => pathMap.get(entryPath(input, k))?.match(/\[([^\]]+)\]$/)[1] ?? k)));
    assert(i >= 0, `${input}: no choice for ${JSON.stringify(value)}`);
    await click(`.widget [data-choice="${i}"]`);
  } else if (kind === "roster") {
    const labels = labelsFor(input, value);
    await evaluate("document.querySelectorAll('#roster .roster-row').forEach(r=>r.remove())");
    for (let i = 0; i < value.length; i++) { await click("#roster-add"); await type(`#roster .roster-row:nth-child(${i + 1}) input`, labels[i]); }
    if (input === "$w2@person[taxpayer]" && !rosterShot) { await shot("roster"); rosterShot = true; }
    await click("#answer-submit");
  } else {
    const money = await evaluate("document.getElementById('answer-input').inputMode === 'decimal'");
    await type("#answer-input", money ? (value / 100).toFixed(2) : String(value));
    await click("#answer-submit");
  }
  for (let i = 0; i < 400 && logLines() === before; i++) {
    const err = await evaluate("document.getElementById('field-error')?.textContent ?? ''");
    assert(!err, `${input}: ${err}`);
    await wait(25);
  }
  assert.equal(logLines(), before + 1, `${input}: the answer was not written`);
  await until(`document.querySelector('.question[data-input]')?.dataset.input !== ${JSON.stringify(input)} || !document.querySelector('.question[data-input]')`, `the page after ${input}`);
  if (input.startsWith("$") && Array.isArray(value)) {
    const keys = (await served()).answered.find(a => a.input === input).value;
    assert.equal(keys.length, value.length, `${input}: entries saved`);
    value.forEach((k, i) => pathMap.set(entryPath(input, k), entryPath(input, keys[i])));
  }
}

const dir = mkdtempSync(join(tmpdir(), "tax-ui-browser-"));
let server, out = "";
try {
  server = spawn(process.execPath, [join(root, "engine/dist/main.js"), "serve", "--dir", dir, "--port", "0"], { stdio: ["ignore", "pipe", "pipe"] });
  server.stdout.on("data", d => { out += d; }); server.stderr.on("data", d => { out += d; });
  for (let i = 0; i < 300 && !/http:\/\/127\.0\.0\.1:\d+\//.test(out); i++) await wait(50);
  origin = out.match(/http:\/\/127\.0\.0\.1:\d+/)?.[0];
  assert(origin, "the server did not start: " + out);
  ({ docTitles, docDesignations } = await fetch(`${origin}/api/returns`).then(r => r.json()));
  await cdp("Page.enable"); await cdp("Runtime.enable");
  await cdp("Emulation.setDeviceMetricsOverride", { width: 1600, height: 1100, deviceScaleFactor: 1, mobile: false });
  await cdp("Page.navigate", { url: origin + "/" });
  await until("document.readyState==='complete' && document.getElementById('notices').textContent.includes('Not tax or legal advice')", "the page");
  assert.match(await evaluate("document.getElementById('scope').textContent"), /New York Form IT-201/);

  // A new return through the page.
  await type("#new-name", "smoke");
  await click("#new-return button");
  await until("document.querySelector('.question[data-input]')?.dataset.input === '$person'", "the first question");
  // The first question is a selector in plain terms, with no entry syntax, and its citation is shown as its source.
  const firstQ = await evaluate(`({choices:[...document.querySelectorAll('.widget [data-choice]')].map(b=>b.textContent),
    text:document.querySelector('.question').innerText, inputs:document.querySelectorAll('.widget input').length,
    source:document.querySelector('.question .source').innerText,
    beside:(()=>{const a=document.querySelector('.question .ask').getBoundingClientRect(),b=document.querySelector('.question .source').getBoundingClientRect();return b.left>=a.right&&b.top<a.bottom;})()})`);
  assert.deepEqual(firstQ.choices, ["Just me", "Me and my husband or wife, together on one return"]);
  assert.match(firstQ.text, /^Who is this tax return for\?/);
  assert.equal(firstQ.inputs, 0, "no text box on the first question");
  assert.doesNotMatch(firstQ.text, /\[|taxpayer|JSON|cents|true or false/, "no entry syntax or keys on the first question");
  assert.match(firstQ.source, /^Source\s+Form 1040 \u2014 U\.S\. Individual Income Tax Return\s/);
  assert.match(firstQ.source, /Your first name and middle initial/);
  assert(firstQ.beside, "the source is beside the question on a wide window");
  await shot("question");
  assert.match(await banner(), /In progress/);
  // The first question, in plain words, names no form.
  assert.equal(await evaluate("document.querySelectorAll('.forms-mentioned .form-gloss').length"), 0, "the first question names no form");

  // A blank amount is refused on the page and nothing is written; a help request leaves the question pending.
  let answered = 0, correctedAt = null, sawProvisional = false, derivationOpened = false, blankRefused = false, sawFolded = false, sawGlosses = false, sawStatus = false;
  for (let step = 0; step < 400; step++) {
    const input = await question();
    if (!input || !(fx(input) in inputs)) break;
    if (answered === 0) {
      await click("#need-help");
      await until("!!document.querySelector('.question .note')", "the help request");
      assert.equal(await question(), "$person");
      assert.equal(logLines(), 2);
    }
    if (!blankRefused) {
      const kind = await evaluate("document.getElementById('answer-input')?.inputMode ?? ''");
      if (kind === "decimal") {
        blankRefused = true;
        const before = logLines();
        await type("#answer-input", "");
        await click("#answer-submit");
        await until("document.getElementById('field-error').textContent.includes('Enter an amount')", "the blank-amount message");
        assert.equal(logLines(), before, "a blank amount is never sent");
      }
    }
    // Every question is shown in full, word for word, and its source by the document's designation and title, not its id.
    const q = (await served()).pending.find(p => p.input === input) ?? null;
    if (q) {
      // Paragraphs, headings and list items alike: a structured question's bullets are part of the question.
      const shown = await evaluate(`({prompt:document.querySelector('.prompt-text').innerText,
        folds:document.querySelectorAll('.prompt-text .expander, .prompt-text [hidden]').length, doc:document.querySelector('.source .doc').textContent})`);
      assert.equal(shown.folds, 0, `${input}: the question is never folded`);
      const words = (t) => t.replace(/^\s*- /gm, "").replace(/\s+/g, " ").trim();
      assert.equal(words(shown.prompt), words(q.prompt), `${input}: the question is shown word for word`);
      const title = docTitles[q.cite.doc], designation = docDesignations[q.cite.doc];
      assert.equal(shown.doc, designation && !title.includes(designation) ? `${designation} \u2014 ${title}` : title, `${input}: the source is named by its designation and title`);
      // The forms it names: one item per served form, open when there are at most two, each purpose quoted in full.
      const forms = await evaluate(`[...document.querySelectorAll('.forms-mentioned .form-gloss')].map(li=>({open:li.querySelector('details')?.open ?? null,
        quote:li.querySelector('blockquote')?.textContent ?? null}))`);
      assert.equal(forms.length, q.forms.length, `${input}: one item per form named`);
      forms.forEach((f, i) => {
        const purpose = q.forms[i].purpose;
        assert.equal(f.open, purpose ? q.forms.length <= 2 : null, `${input}: ${q.forms[i].designation} is open only when at most two forms are named`);
        if (purpose) assert.equal(f.quote.replace(/[\u201c\u201d\s•]/g, ""), purpose.text.replace(/[\u201c\u201d\s•]/g, ""),
          `${input}: ${q.forms[i].designation}'s purpose is quoted word for word`);
      });
      if (q.forms.length > 2) sawFolded = true;
      // The first question that names one or two forms with a purpose: under the explanation, each by designation and
      // title; a purpose, quoted with its source, shown open. The question itself is unchanged.
      if (!sawGlosses && q.forms.length >= 1 && q.forms.length <= 2 && q.forms.some(f => f.purpose)) {
        const glosses = await evaluate(`({heading:document.getElementById('forms-heading')?.textContent,
          items:[...document.querySelectorAll('.forms-mentioned .form-gloss')].map(li=>({name:li.querySelector('.form-name').textContent,
            open:li.querySelector('details')?.open ?? null, quote:li.querySelector('blockquote')?.innerText ?? '', meta:li.querySelector('.meta')?.textContent ?? ''})),
          below:(()=>{const h=document.querySelector('.question .help') ?? document.querySelector('.question .widget'),f=document.querySelector('.forms-mentioned');return !!h&&!!f&&f.getBoundingClientRect().top>=h.getBoundingClientRect().bottom;})(),
          inAsk:!!document.querySelector('.question .ask .forms-mentioned')})`);
        assert.equal(glosses.heading, "Forms mentioned");
        assert.deepEqual(glosses.items.map(i => i.name), q.forms.map(f => f.title && !f.title.includes(f.designation) ? `${f.designation} \u2014 ${f.title}` : f.title ?? f.designation), `${input}: each form by designation and title`);
        const withPurpose = q.forms.findIndex(f => f.purpose);
        assert.equal(glosses.items[withPurpose].open, true, "with at most two forms, a purpose is shown open");
        assert.match(glosses.items[withPurpose].quote, /^\u201c/);
        assert.match(glosses.items[withPurpose].meta, /, p\. \d+$/, "a purpose names its source and page");
        assert(glosses.below && glosses.inAsk, "the forms are listed under the explanation, in the question's column");
        await evaluate("document.querySelector('.forms-mentioned').scrollIntoView({block:'center',behavior:'instant'})");
        await screenshot("/private/tmp/tax-ui-glosses.png");
        await evaluate("window.scrollTo(0, 0)");
        sawGlosses = true;
      }
      // The filing status, asked of one person: its labelled options one to a line in the bank's order, without the
      // joint status, which only the couple's choice of the first question records.
      if (input === "f1040.status") {
        const options = await evaluate("[...document.querySelectorAll('.widget .choices.stacked [data-value]')].map(b=>[b.dataset.value,b.textContent])");
        assert.deepEqual(options.map(o => o[0]), ["mfs", "qss", "hoh", "single"]);
        assert.deepEqual(options.map(o => o[1]), ["mfs", "qss", "hoh", "single"].map(v => q.value_labels[v]));
        assert.deepEqual(q.withheld, ["mfj"]);
        assert.equal(await evaluate("document.querySelectorAll('.widget select').length"), 0, "a labelled enum is not a drop-down");
        await shot("status");
        sawStatus = true;
      }
      if (input === "scope.other_line16") {
        assert(q.prompt.length > 900, "scope.other_line16 is a long question");
        await shot("long");
        longShot = true;
      }
    }
    await answer(input, inputs[fx(input)]);
    answered++;
    // Correct an earlier answer: the first amount answered, through the answered list, then back to the fixture's value.
    if (!correctedAt) {
      const money = await evaluate(`[...document.querySelectorAll('#answered button[data-input]')].map(b=>b.dataset.input).find(k=>/\\.w2\\[[^\\]]+\\]\\.box1$/.test(k)) ?? null`);
      if (money && inputs[fx(money)] > 0) {
        await view("answered");
        await click(`#answered button[data-input="${money}"]`);
        await until(`document.querySelector('.question[data-input]')?.dataset.input === ${JSON.stringify(money)} && !!document.querySelector('.correcting') && document.getElementById('panel-answered').hidden`, "the reopened question");
        await type("#answer-input", ((inputs[fx(money)] + 12345) / 100).toFixed(2));
        await click("#answer-submit");
        await until(`[...document.querySelectorAll('#answered li')].some(li=>li.querySelector('button').dataset.input===${JSON.stringify(money)} && li.querySelector('.value').textContent===${JSON.stringify(fmtMoney(inputs[fx(money)] + 12345))})`, "the corrected answer");
        assert(await evaluate("document.querySelectorAll('#sheet tr.changed').length > 0"), "the lines the correction changed are highlighted");
        assert(await evaluate("document.getElementById('saved').textContent.includes('Saved:')"), "the saved answer is acknowledged");
        await view("answered");
        await shot("answered");
        await click(`#answered button[data-input="${money}"]`);
        await until("!!document.querySelector('.correcting')", "the reopened question");
        await type("#answer-input", (inputs[fx(money)] / 100).toFixed(2));
        await click("#answer-submit");
        await until("!document.querySelector('.correcting')", "the restored answer");
        correctedAt = money;
      }
    }
    // Open a derivation once wages are computed: its operation, operands and the answers it depends on.
    if (correctedAt && !derivationOpened && await evaluate("!!document.querySelector('#sheet tr[data-key=\"f1040.line1a\"]')")) {
      await view("return");
      await click('#sheet tr[data-key="f1040.line1a"] .line-open');
      await until("!document.getElementById('derivation').hidden", "the derivation");
      const shown = await evaluate(`({text:document.getElementById('derivation').innerText, operands:document.querySelectorAll('#derivation button[data-ref]').length,
        deps:[...document.querySelectorAll('#depends-on button[data-input]')].map(b=>b.dataset.input)})`);
      assert.match(shown.text, /Operation/); assert(shown.operands > 0, "operands are links");
      assert(shown.deps.includes(correctedAt), `the corrected answer ${correctedAt} is among the answers line 1a depends on: ${shown.deps}`);
      await click("#derivation button[data-ref]");
      await until("!!document.getElementById('derivation-back')", "an operand's derivation with a Back button");
      await click("#derivation-back");
      await until("!document.getElementById('derivation-back') && document.querySelector('#sheet tr.open')?.dataset.key === 'f1040.line1a'", "line 1a's derivation again");
      await evaluate("window.scrollTo(0, 0)");
      await shot("return");
      await click(`#depends-on button[data-input="${correctedAt}"]`);
      await until(`document.querySelector('.question[data-input]')?.dataset.input === ${JSON.stringify(correctedAt)} && !!document.querySelector('.correcting')`, "the question a derivation links to");
      await click("#back-next");
      await until("!document.querySelector('.correcting')", "the next question");
      derivationOpened = true;
    }
    const b = await banner();
    if (/provisional/.test(b)) {
      if (!sawProvisional) {
        assert.match(b, /provisional: later answers may clear it/);
        await click("#refusal-open");
        await until("document.getElementById('refusal-dialog').open", "the refusal details");
        assert.match(await evaluate("document.getElementById('refusal-dialog').innerText"), /Refused, provisional[\s\S]*Later answers may clear it[\s\S]*Source/);
        await shot("refusal-provisional");
        await evaluate("document.getElementById('refusal-dialog').close()");
        await view("return");
        await click('.tabs [data-sheet="newYork"]');
        await until("[...document.querySelectorAll('#sheet .tag')].some(t=>t.textContent==='refused, provisional')", "a provisional refused line on the New York sheet");
        await click('.tabs [data-sheet="federal"]');
        await view("question");
      }
      sawProvisional = true;
    }
  }
  assert(blankRefused, "a blank amount was refused on the page");
  // Labels: two employers whose labels give the same key got distinct keys, and the page shows labels, not keys.
  const finalState = await served();
  assert.deepEqual(finalState.answered.find(a => a.input === "$w2@person[taxpayer]").value, ["acme_corp", "acme_corp_2"], "the colliding label got a numeric suffix");
  assert.equal(finalState.entryLabels["person[taxpayer]"], "You");
  await view("answered");
  // The answered list's own words: each question's id, the one place an entry key is shown, is left out.
  const shown = await evaluate(`({answered:[...document.querySelectorAll('#answered li')].map(li=>{const c=li.cloneNode(true);c.querySelectorAll('.qid').forEach(e=>e.remove());return c.textContent;}).join('\\n'),
    headings:[...document.querySelectorAll('#sheet h3')].map(h=>h.textContent)})`);
  assert.match(shown.answered, /Just me/); assert.match(shown.answered, /Acme Corp\., Acme Corp/);
  // On a return with one person the answered list names the employer alone; the sheet's entry headings keep the person.
  assert.match(shown.answered, /Acme Corp\./);
  assert.doesNotMatch(shown.answered, /You › Acme Corp\./);
  assert.doesNotMatch(shown.answered, /acme_corp|\[taxpayer\]/, "no entry keys in the answered list, but in each question's id");
  await view("return");
  await click('.tabs [data-sheet="federal"]');
  await until("[...document.querySelectorAll('#sheet h3')].some(h=>h.textContent.endsWith('— You › Acme Corp.'))", "an entry heading on the sheet shown by its labels");
  // The sheet shows the return first, then its schedules, the other forms, and worksheets and helper sections last.
  const groups = async () => evaluate(`[...document.querySelectorAll('#sheet h3')].map(h=>h.textContent)`);
  const rank = t => /^Form (1040|IT-201)\b/.test(t) ? 0 : t.startsWith("Schedule ") ? 1 : t.startsWith("Form ") ? 2 : 3;
  for (const tab of ["federal", "newYork"]) {
    await click(`.tabs [data-sheet="${tab}"]`);
    const heads = await groups();
    assert.match(heads[0], tab === "federal" ? /^Form 1040 / : /^Form IT-201 /, `${tab}: the return comes first`);
    assert(heads.every((h, i) => i === 0 || rank(heads[i - 1]) <= rank(h)), `${tab}: sections in order: ${heads.join(" | ")}`);
    if (tab === "federal") assert(heads.some(h => rank(h) === 1) && heads.some(h => rank(h) === 3), "the federal sheet has schedules and worksheets");
  }
  await evaluate("window.scrollTo(0, 0)");
  await click('.tabs [data-sheet="federal"]');
  await shot("sheet-order");
  // An entry's question names the entry it is about.
  await view("answered");
  await click(`#answered button[data-input="person[taxpayer].w2[acme_corp_2].box1"]`);
  // On a return with one person the entry is the employer alone; the person is every question's subject.
  await until("document.querySelector('.question .about')?.textContent === 'About: Acme Corp'", "the entry a question is about");
  await click("#back-next");
  assert(correctedAt, "an earlier answer was corrected");
  assert(sawGlosses, "a question naming a form with a purpose was shown");
  assert(sawStatus, "the filing status was asked");
  assert(derivationOpened, "a derivation was opened");
  assert(sawProvisional, "the refusal was shown as provisional while questions were pending");
  assert.match(await banner(), /Refused \(final\)/);
  assert.match(await banner(), /Form IT-203/);
  assert.equal(await question(), null);
  await click("#refusal-open");
  await until("document.getElementById('refusal-dialog').open", "the final refusal details");
  assert.match(await evaluate("document.getElementById('refusal-dialog').innerText"), /Refused \(final\)[\s\S]*IT-203/);
  await shot("refusal");
  await evaluate("document.getElementById('refusal-dialog').close()");
  await view("return");
  await click('.tabs [data-sheet="newYork"]');
  await until("[...document.querySelectorAll('#sheet .tag')].some(t=>t.textContent==='refused')", "a final refused line on the New York sheet");
  await shot("refused-sheet");
  await view("about");
  assert.match(await evaluate("document.getElementById('standing').textContent"), /not tax or legal advice/);
  await shot("about");
  // A narrow window: the source drops below the explanation.
  await view("answered");
  await click(`#answered button[data-input="person[taxpayer].w2[acme_corp_2].box1"]`);
  await until("!!document.querySelector('.question .source')", "a question to show narrow");
  await cdp("Emulation.setDeviceMetricsOverride", { width: 760, height: 1100, deviceScaleFactor: 1, mobile: false });
  assert(await evaluate("(()=>{const a=document.querySelector('.question .ask').getBoundingClientRect(),b=document.querySelector('.question .source').getBoundingClientRect();return b.top>=a.bottom;})()"), "the source is below the question on a narrow window");
  await shot("narrow");
  await cdp("Emulation.setDeviceMetricsOverride", { width: 1600, height: 1100, deviceScaleFactor: 1, mobile: false });
  await click("#back-next");
  // A reload keeps the state.
  await cdp("Page.reload");
  await until("/Refused \\(final\\)/.test(document.getElementById('status-banner').textContent)", "the reloaded page");
  assert.equal(await evaluate("document.querySelectorAll('.conflict').length"), 0, "a scope refusal shows no conflict");

  // Conflicting answers are shown as a conflict, not as a refusal: Form 8889 with self-only coverage on December 1 and
  // every eligible month a family month (stage11.hsa.self_full_year, its month answers changed), written as a log.
  const hsaCase = loadFixtureCases("federal", canonical).find(c => c.id === "stage11.hsa.self_full_year");
  const hsa = "person[taxpayer].f8889[hsa].";
  const hsaInputs = { ...hsaCase.inputs, [`${hsa}dec_coverage`]: "self_only", [`${hsa}months_eligible`]: 12, [`${hsa}months_family`]: 12 };
  writeFileSync(join(dir, "conflict.jsonl"), [{ version: 1, tax_year: 2025, profile: "ny" }, ...Object.entries(hsaInputs).map(([input, value]) => ({ input, value }))]
    .map(e => JSON.stringify(e)).join("\n") + "\n", { mode: 0o600 });
  await cdp("Page.navigate", { url: origin + "/#conflict" });
  await until("/These answers conflict/.test(document.getElementById('status-banner').textContent)", "the conflict in the status line");
  await view("question");
  await until("!!document.querySelector('#conflict')", "the conflict on the question page");
  const conflictText = await evaluate("document.getElementById('conflict').innerText");
  assert.match(conflictText, /These answers conflict[\s\S]*December 1 coverage do not fit together/);
  assert.doesNotMatch(await banner() + conflictText, /cannot prepare|provisional|Refused/, "a conflict is neither unsupported nor provisional");
  const links = await evaluate("[...document.querySelectorAll('#conflict button[data-input]')].map(b=>b.dataset.input)");
  assert.deepEqual([...links].sort(), ["coverage_year", "dec_coverage", "months_eligible", "months_family"].map(k => hsa + k), "the conflict links the four answers it reads");
  const conflictShown = Object.fromEntries(await evaluate("[...document.querySelectorAll('#conflict li')].map(l=>[l.querySelector('button').dataset.input,l.querySelector('.conflict-value').textContent])"));
  assert.deepEqual({ ...conflictShown, [`${hsa}coverage_year`]: undefined }, { [`${hsa}coverage_year`]: undefined, [`${hsa}dec_coverage`]: "Self-only HDHP coverage", [`${hsa}months_eligible`]: "12", [`${hsa}months_family`]: "12" }, "each answer is shown beside its question");
  assert.ok(conflictShown[`${hsa}coverage_year`], "the coverage answer is shown too");
  assert.deepEqual(await evaluate("[...document.querySelectorAll('#conflict li')].map(l=>l.querySelector('.qid-key').textContent).sort()"), [...links].sort(), "each conflicting answer shows its id");
  await evaluate("window.scrollTo(0, 0)");
  await screenshot("/private/tmp/tax-ui-conflict.png");
  await click(`#conflict button[data-input="${hsa}months_family"]`);
  await until(`document.querySelector('.question[data-input]')?.dataset.input === ${JSON.stringify(hsa + "months_family")}`, "the conflicting question reopened");
  assert(await evaluate("!!document.querySelector('.correcting') && !!document.getElementById('conflict')"), "the reopened question is a correction, with the conflict still shown above it");
  await view("return");
  assert(await evaluate("[...document.querySelectorAll('#sheet .tag')].some(t=>t.textContent==='conflicting answers') && ![...document.querySelectorAll('#sheet .tag')].some(t=>/^refused/.test(t.textContent))"),
    "the lines the conflict stops are tagged as conflicting answers");
  // The ids: in the answered list and with the current question.
  await cdp("Page.navigate", { url: origin + "/#smoke" });
  await until("document.querySelectorAll('#answered .qid-key').length > 0", "the answered list with its ids");
  await view("answered");
  const listed = await evaluate("[...document.querySelectorAll('#answered li')].map(li=>[li.querySelector('button[data-input]').dataset.input, li.querySelector('.qid-key').textContent])");
  assert(listed.length > 5 && listed.every(([input, id]) => input === id), "each answered question shows its id, an entry's with its entry keys");
  assert(listed.some(([input]) => /^person\[taxpayer\]\.w2\[/.test(input)), "a per-entry id is among them");
  assert(await evaluate("[...document.querySelectorAll('#answered button[data-input]')].every(b=>!b.querySelector('.qid-key') && !b.title)"), "the id is outside the question's button, so it is no part of the button's name");
  await evaluate("window.scrollTo(0, 0)");
  await shot("answered-ids");
  await click(`#answered button[data-input="person[taxpayer].w2[acme_corp_2].box1"]`);
  await until("document.getElementById('question-id')?.querySelector('.qid-key')?.textContent === 'person[taxpayer].w2[acme_corp_2].box1'", "the current question's id");
  assert.equal(await evaluate("getComputedStyle(document.querySelector('#question-id .qid-key')).userSelect"), "all", "one click selects the whole id");
  assert(await evaluate("(()=>{const a=document.querySelector('.prompt-text'),b=document.getElementById('question-id');return !!(a.compareDocumentPosition(b)&Node.DOCUMENT_POSITION_FOLLOWING) && !document.getElementById('prompt-heading').contains(b);})()"), "the id follows the question and is no part of its heading");
  assert(await evaluate("!!document.getElementById('question-id-copy') && !document.querySelector('.source .key')"), "the id has its copy control, and the source no longer repeats it");
  await shot("question-id");
  assert.deepEqual(errors, []);
  console.log(`Browser passed: the person selector with no entry syntax, ${answered} answers through the page's widgets, labelled roster entries (a colliding label suffixed; labels in the answered list, a sheet heading and a question's entry), a help request, a refused blank amount, a correction through the answered list, a derivation with operand links and the answer it depends on, a provisional refusal that became final, a reload, conflicting answers shown as a conflict with links that reopen them.`);
  assert(longShot, "the long question scope.other_line16 was shown in full");
  assert(sawFolded, "a question naming more than two forms was shown with each form folded to one line");
  console.log("Screenshots: /private/tmp/tax-ui-design-{answered-ids,question-id}.png, /private/tmp/tax-ui-design-{question,status,long,roster,answered,return,sheet-order,refusal-provisional,refusal,refused-sheet,about,narrow}.png, /private/tmp/tax-ui-glosses.png, /private/tmp/tax-ui-conflict.png");
} finally {
  server?.kill(); ws.close();
  rmSync(dir, { recursive: true, force: true });
}
