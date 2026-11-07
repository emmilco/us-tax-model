// SPDX-License-Identifier: Apache-2.0
// Smoke test of the web UI in a separately launched headless Chrome on port 9227, run by hand (not in check-all):
//   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --remote-debugging-port=9227 \
//     --user-data-dir="$(mktemp -d)" about:blank &
//   npm run compile && node ui/test_browser.mjs
// It starts `serve` on a temporary returns directory and walks a synthetic New York return (the fixture
// ny.refuse.part_year_state) through the page: every answer through the page's widgets, a blank amount refused
// without writing, an earlier answer corrected, a derivation opened and followed to the answer it depends on, and the
// provisional refusal becoming final once nothing is pending. Screenshots go to /private/tmp/tax-ui-*.png.
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const { loadCanonical } = await import(join(root, "engine/dist/canonical.js"));
const { resolveInputs } = await import(join(root, "engine/dist/fixture-inputs.js"));
const fixture = JSON.parse(readFileSync(join(root, "fixtures/ny/2025/it201.json"), "utf8")).cases.find(c => c.id === "ny.refuse.part_year_state");
const inputs = resolveInputs(fixture.inputs, loadCanonical().params, fixture.id);

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
let origin, rosterShot = false;
const served = () => fetch(`${origin}/api/returns/smoke`).then(r => r.json());

/** Answers the question on the page with the fixture's `value` through its widget and waits for the page to move on. */
async function answer(input, value) {
  const before = logLines();
  const kind = await evaluate("document.querySelector('.widget [data-choice]') ? 'choice' : document.querySelector('.widget #roster') ? 'roster' : document.querySelector('.widget [data-answer]') ? 'bool' : document.querySelector('.widget select') ? 'enum' : 'text'");
  if (kind === "bool") await click(`.widget [data-answer=${value ? "yes" : "no"}]`);
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
    if (input === "$w2@person[taxpayer]" && !rosterShot) { await screenshot("/private/tmp/tax-ui-roster.png"); rosterShot = true; }
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
    source:document.querySelector('.question .source').innerText})`);
  assert.deepEqual(firstQ.choices, ["Just me", "Me and my spouse (joint return)"]);
  assert.equal(firstQ.inputs, 0, "no text box on the first question");
  assert.doesNotMatch(firstQ.text, /\[|taxpayer|JSON|cents|true or false/, "no entry syntax or keys on the first question");
  assert.match(firstQ.source, /^Source — the form line or instruction this question comes from: f1040/);
  await screenshot("/private/tmp/tax-ui-first.png");
  assert.match(await banner(), /Incomplete/);

  // A blank amount is refused on the page and nothing is written; a help request leaves the question pending.
  let answered = 0, correctedAt = null, sawProvisional = false, derivationOpened = false, blankRefused = false;
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
    await answer(input, inputs[fx(input)]);
    answered++;
    // Correct an earlier answer: the first amount answered, through the answered list, then back to the fixture's value.
    if (!correctedAt) {
      const money = await evaluate(`[...document.querySelectorAll('#answered button[data-input]')].map(b=>b.dataset.input).find(k=>/\\.w2\\[[^\\]]+\\]\\.box1$/.test(k)) ?? null`);
      if (money && inputs[fx(money)] > 0) {
        await click(`#answered button[data-input="${money}"]`);
        await until(`document.querySelector('.question[data-input]')?.dataset.input === ${JSON.stringify(money)} && !!document.querySelector('.correcting')`, "the reopened question");
        await type("#answer-input", ((inputs[fx(money)] + 12345) / 100).toFixed(2));
        await click("#answer-submit");
        await until(`[...document.querySelectorAll('#answered li')].some(li=>li.querySelector('button').dataset.input===${JSON.stringify(money)} && li.querySelector('.value').textContent===${JSON.stringify(fmtMoney(inputs[fx(money)] + 12345))})`, "the corrected answer");
        assert(await evaluate("document.querySelectorAll('#sheet tr.changed').length > 0"), "the lines the correction changed are highlighted");
        await screenshot("/private/tmp/tax-ui-corrected.png");
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
      await click('#sheet tr[data-key="f1040.line1a"]');
      await until("!document.getElementById('derivation').hidden", "the derivation");
      const shown = await evaluate(`({text:document.getElementById('derivation').innerText, operands:document.querySelectorAll('#derivation button[data-ref]').length,
        deps:[...document.querySelectorAll('#depends-on button[data-input]')].map(b=>b.dataset.input)})`);
      assert.match(shown.text, /operation/); assert(shown.operands > 0, "operands are links");
      assert(shown.deps.includes(correctedAt), `the corrected answer ${correctedAt} is among the answers line 1a depends on: ${shown.deps}`);
      await click("#derivation button[data-ref]");
      await until("document.querySelectorAll('#derivation .bar button').length === 2", "an operand's derivation with a Back button");
      await click("#derivation .bar button"); // back
      await screenshot("/private/tmp/tax-ui-derivation.png");
      await click(`#depends-on button[data-input="${correctedAt}"]`);
      await until(`document.querySelector('.question[data-input]')?.dataset.input === ${JSON.stringify(correctedAt)} && !!document.querySelector('.correcting')`, "the question a derivation links to");
      await click(".actions button:nth-child(2)"); // back to the next question
      await until("!document.querySelector('.correcting')", "the next question");
      derivationOpened = true;
    }
    const b = await banner();
    if (/provisional/.test(b)) {
      if (!sawProvisional) {
        assert.match(b, /provisional: later answers may clear it/);
        await click('.tabs [data-sheet="newYork"]');
        await until("[...document.querySelectorAll('#sheet .tag')].some(t=>t.textContent==='refused, provisional')", "a provisional refused line on the New York sheet");
        await screenshot("/private/tmp/tax-ui-provisional.png");
        await click('.tabs [data-sheet="federal"]');
      }
      sawProvisional = true;
    }
  }
  assert(blankRefused, "a blank amount was refused on the page");
  // Labels: two employers whose labels give the same key got distinct keys, and the page shows labels, not keys.
  const finalState = await served();
  assert.deepEqual(finalState.answered.find(a => a.input === "$w2@person[taxpayer]").value, ["acme_corp", "acme_corp_2"], "the colliding label got a numeric suffix");
  assert.equal(finalState.entryLabels["person[taxpayer]"], "You");
  const shown = await evaluate(`({answered:document.getElementById('answered').innerText, headings:[...document.querySelectorAll('#sheet h3')].map(h=>h.textContent)})`);
  assert.match(shown.answered, /Just me/); assert.match(shown.answered, /Acme Corp\., Acme Corp/);
  assert.match(shown.answered, /person\[You\]\.w2\[Acme Corp\.\]\.box1/);
  assert.doesNotMatch(shown.answered, /acme_corp|\[taxpayer\]/, "no entry keys in the answered list");
  await click('.tabs [data-sheet="federal"]');
  await until("[...document.querySelectorAll('#sheet h3')].some(h=>h.textContent.endsWith('— You › Acme Corp.'))", "an entry heading on the sheet shown by its labels");
  // An entry's question names the entry it is about.
  await click(`#answered button[data-input="person[taxpayer].w2[acme_corp_2].box1"]`);
  await until("document.querySelector('.question .about')?.textContent === 'About: You › Acme Corp'", "the entry a question is about");
  await click(".actions button:nth-child(2)");
  assert(correctedAt, "an earlier answer was corrected");
  assert(derivationOpened, "a derivation was opened");
  assert(sawProvisional, "the refusal was shown as provisional while questions were pending");
  assert.match(await banner(), /Refused \(final\)/);
  assert.match(await banner(), /Form IT-203/);
  assert.equal(await question(), null);
  await click('.tabs [data-sheet="newYork"]');
  await until("[...document.querySelectorAll('#sheet .tag')].some(t=>t.textContent==='refused')", "a final refused line on the New York sheet");
  await screenshot("/private/tmp/tax-ui-final.png");
  // A reload keeps the state.
  await cdp("Page.reload");
  await until("/Refused \\(final\\)/.test(document.getElementById('status-banner').textContent)", "the reloaded page");
  assert.deepEqual(errors, []);
  console.log(`Browser passed: the person selector with no entry syntax, ${answered} answers through the page's widgets, labelled roster entries (a colliding label suffixed; labels in the answered list, a sheet heading and a question's entry), a help request, a refused blank amount, a correction through the answered list, a derivation with operand links and the answer it depends on, a provisional refusal that became final, a reload.`);
  console.log("Screenshots: /private/tmp/tax-ui-first.png, tax-ui-roster.png, tax-ui-corrected.png, tax-ui-derivation.png, tax-ui-provisional.png, tax-ui-final.png");
} finally {
  server?.kill(); ws.close();
  rmSync(dir, { recursive: true, force: true });
}
