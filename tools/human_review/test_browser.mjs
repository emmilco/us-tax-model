// SPDX-License-Identifier: Apache-2.0
// Smoke test using a separately launched headless Chrome on port 9227.
// Screenshots use the real packet; invented verdicts are saved ONLY in a temp repo.
import assert from "node:assert/strict";
import { execFileSync, spawn } from "node:child_process";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "../..");
const wait = ms => new Promise(r => setTimeout(r, ms));
const pages = await fetch("http://127.0.0.1:9227/json/list").then(r => r.json());
const page = pages.find(p => p.url === "about:blank") ?? pages.find(p => p.type === "page" && p.url.startsWith("http://127.0.0.1:"));
assert(page, "launch a separate headless Chrome on port 9227 first");
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((resolve, reject) => { ws.addEventListener("open", resolve); ws.addEventListener("error", reject); });
let id = 0;
const pending = new Map(), errors = [];
ws.addEventListener("message", e => {
  const msg = JSON.parse(e.data);
  if (msg.id) {
    const task = pending.get(msg.id); pending.delete(msg.id);
    if (msg.error) task.reject(new Error(JSON.stringify(msg.error))); else task.resolve(msg.result);
  } else if (msg.method === "Runtime.exceptionThrown") errors.push(msg.params.exceptionDetails.text);
});
function cdp(method, params = {}) {
  return new Promise((resolve, reject) => { const n = ++id; pending.set(n, { resolve, reject }); ws.send(JSON.stringify({ id: n, method, params })); });
}
async function evaluate(expression) {
  const r = await cdp("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true });
  assert(!r.exceptionDetails, JSON.stringify(r.exceptionDetails));
  return r.result.value;
}
async function navigate(url) {
  await cdp("Page.navigate", { url });
  for (let i = 0; i < 100; i++) {
    if (await evaluate("document.readyState==='complete' && !!document.querySelector('.pages.active')")) return;
    await wait(100);
  }
  throw new Error("packet did not finish loading");
}
async function screenshot(path) {
  const result = await cdp("Page.captureScreenshot", { format: "png" });
  writeFileSync(path, Buffer.from(result.data, "base64"));
}
async function click(selector) {
  const point=await evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});
    e.scrollIntoView({block:'center',behavior:'instant'});const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);
  await cdp("Input.dispatchMouseEvent", {type:"mousePressed",button:"left",clickCount:1,...point});
  await cdp("Input.dispatchMouseEvent", {type:"mouseReleased",button:"left",clickCount:1,...point});
}

const sandbox = mkdtempSync(join(tmpdir(), "tax-review-browser-"));
let server, serverOutput = "";
try {
  await cdp("Page.enable"); await cdp("Runtime.enable");
  await cdp("Emulation.setDeviceMetricsOverride", { width: 1600, height: 1200, deviceScaleFactor: 1, mobile: false });
  await navigate("http://127.0.0.1:8790/2.html");
  const structure = await evaluate(`(async()=>{
    const imgs=[...document.querySelectorAll('.pages.active img')];
    await Promise.all(imgs.map(i=>{i.loading='eager';return i.decode();}));
    return {cards:document.querySelectorAll('.line[data-ref]').length,
      ref:document.querySelector('.line.active').dataset.ref,
      visible:[...document.querySelectorAll('.line[data-ref]')].filter(l=>getComputedStyle(l).display!=='none').length,
      readingWords:document.querySelector('.line.active .reading').innerText.trim().split(/\s+/).length,
      images:imgs.length,broken:imgs.filter(i=>!i.naturalWidth).length,
      empty:[...document.querySelectorAll('select,textarea')].every(i=>!i.value),
      overflow:document.documentElement.scrollWidth>innerWidth};
  })()`);
  assert.equal(structure.cards, 14); assert.equal(structure.visible, 1); assert.equal(structure.ref, "sa.standardbase");
  assert(structure.readingWords < 50); assert(structure.images >= 1); assert.equal(structure.broken, 0); assert.equal(structure.empty, true);
  assert.equal(structure.overflow, false);
  await screenshot("/private/tmp/tax-human-review-desktop.png");
  await cdp("Emulation.setDeviceMetricsOverride", { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
  assert.equal(await evaluate("document.documentElement.scrollWidth>innerWidth"), false);
  assert.equal(await evaluate("getComputedStyle(document.querySelector('.source-pane')).display"), "none");
  await evaluate("document.querySelector('#mobile-tabs button[data-pane=sources]').click()");
  assert.equal(await evaluate("getComputedStyle(document.querySelector('.review-pane')).display"), "none");
  await evaluate("document.querySelector('#mobile-tabs button[data-pane=reading]').click()");
  await screenshot("/private/tmp/tax-human-review-mobile.png");

  execFileSync("python3", ["tools/human_review/test_review.py", "--prepare-browser", sandbox], { cwd: root });
  server = spawn("python3", [join(sandbox, "tools/human_review/serve.py"), "--port", "0"], { cwd: sandbox, stdio: ["ignore", "pipe", "pipe"] });
  server.stdout.on("data", data => { serverOutput += data; });
  server.stderr.on("data", data => { serverOutput += data; });
  let ready = false, testOrigin;
  for (let i = 0; i < 100; i++) {
    testOrigin = serverOutput.match(/http:\/\/127\.0\.0\.1:\d+/)?.[0];
    try { if (testOrigin) { const r = await fetch(testOrigin + "/2.html"); if (r.ok) { ready = true; break; } } } catch {}
    await wait(100);
  }
  assert(ready, "isolated review server did not start: " + serverOutput);
  await cdp("Emulation.setDeviceMetricsOverride", { width: 1600, height: 1200, deviceScaleFactor: 1, mobile: false });
  await navigate(testOrigin + "/2.html");
  // Exercise actual pointer clicks with missing fields, not just a prefilled
  // programmatic happy path. A failed validation must be visible beside the button.
  await click('#save-next');
  assert.match(await evaluate("document.getElementById('save-feedback').textContent"), /Choose a verdict/);
  assert.equal(await evaluate("document.activeElement.tagName"), "SELECT");
  await evaluate("document.querySelector('.line.active select').value='MATCH'");
  await click('#save-next');
  assert.match(await evaluate("document.getElementById('save-feedback').textContent"), /brief reason/);
  assert.equal(await evaluate("document.activeElement.tagName"), "TEXTAREA");
  await evaluate("document.querySelector('.line.active textarea').value='Synthetic browser test only. No real human review is claimed.'");
  await click('#save-next');
  assert.match(await evaluate("document.getElementById('save-feedback').textContent"), /Enter your name/);
  assert.equal(await evaluate("document.activeElement.id"), "reader");
  assert.equal(await evaluate("document.querySelector('.line.active').dataset.ref"), "sa.standardbase");
  await evaluate(`document.getElementById('reader').value='Review Test Reader';
    document.querySelector('textarea').value='Synthetic browser test only. No real human review is claimed.';
    document.querySelector('textarea').dispatchEvent(new Event('input',{bubbles:true}));`);
  await click('#save-next');
  for(let i=0;i<100;i++){
    if(await evaluate("document.getElementById('status').textContent.startsWith('Saved.')"))break;
    await wait(100);
  }
  assert.match(await evaluate("document.getElementById('status').textContent"), /^Saved\./);
  assert.equal(await evaluate("document.querySelector('.line.active').dataset.ref"), "sa.extra");
  // A rejected receipt must leave the reader's writing and question in place.
  await evaluate(`{const l=document.querySelector('.line.active');l.dataset.validSubject=l.dataset.subject;l.dataset.subject='0'.repeat(64);
    l.querySelector('select').value='MATCH';l.querySelector('textarea').value='Synthetic note to retain after a rejected save.';}`);
  await click('#save-next');
  for(let i=0;i<100;i++){
    if(await evaluate("document.getElementById('save-feedback').textContent.startsWith('Not saved:')"))break;
    await wait(100);
  }
  assert.match(await evaluate("document.getElementById('save-feedback').textContent"), /packet changed/);
  assert.equal(await evaluate("document.querySelector('.line.active').dataset.ref"), "sa.extra");
  assert.match(await evaluate("document.querySelector('.line.active textarea').value"), /note to retain/);
  await evaluate(`{const l=document.querySelector('.line.active');l.dataset.subject=l.dataset.validSubject;
    l.querySelector('select').value='';l.querySelector('textarea').value='';draft();}`);
  await cdp("Page.reload");
  await wait(500);
  assert.equal(await evaluate("document.querySelector('select').value"), "MATCH");
  assert.match(await evaluate("document.querySelector('textarea').value"), /^Synthetic browser test/);
  const before = execFileSync("node", ["engine/dist/main.js", "evidence"], { cwd: sandbox, encoding: "utf8" });
  assert.match(before, /H \(human source reading\): 0/);
  execFileSync("git", ["add", "reviews"], { cwd: sandbox });
  execFileSync("git", ["commit", "--quiet", "-m", "Synthetic browser review test"], { cwd: sandbox });
  const base = execFileSync("node", ["engine/dist/main.js", "evidence"], { cwd: sandbox, encoding: "utf8" });
  assert.match(base, /H \(human source reading\): 0/); // A parameter reading cannot approve a calculation.
  await evaluate(`activate('sa.standardraw');const l=document.querySelector('.line.active');
    l.querySelector('select').value='MATCH';l.querySelector('textarea').value='Synthetic check of the sum only.';save()`);
  execFileSync("git", ["add", "reviews"], { cwd: sandbox });
  execFileSync("git", ["commit", "--quiet", "-m", "Synthetic review of one computation"], { cwd: sandbox });
  const after = execFileSync("node", ["engine/dist/main.js", "evidence"], { cwd: sandbox, encoding: "utf8" });
  assert.match(after, /H \(human source reading\): 1,/);
  assert.match(after, /B \(human worked values\): 0/);
  // A UI update may invalidate an old receipt, but it must not discard the person's notes.
  await evaluate(`const saved=state();saved.lines[0].subject='old-receipt';
    saved.lines[0].reason='Synthetic notes from before an update.';localStorage.setItem(KEY,JSON.stringify(saved));`);
  await cdp('Page.reload');await wait(750);
  assert.equal(await evaluate("document.querySelector('select').value"), '');
  assert.match(await evaluate("document.querySelector('textarea').value"), /notes from before an update/);
  assert.deepEqual(errors, []);
  console.log("Browser passed: actual Save & next clicks; visible missing-field errors and focus; failed-save note preservation; save/advance/reload; stale-draft note recovery; scoped evidence; desktop/mobile layout.");
  console.log("Screenshots: /private/tmp/tax-human-review-desktop.png, /private/tmp/tax-human-review-mobile.png");
  await navigate("http://127.0.0.1:8790/2.html");
} finally {
  server?.kill(); ws.close();
  rmSync(sandbox, { recursive: true, force: true });
}
