// Scratch: walk the minimal return (full profile) as the page does and print the questions asked, in order.
import { loadContext, minimalAnswers } from "../../../engine/dist/interview-rules.js";
import { pageWalk, words } from "../../../engine/dist/interview-words.js";
const ctx = loadContext();
const config = ctx.configs["full"];
const w = pageWalk(ctx.data, config, minimalAnswers(ctx.data, config, "full", null));
let n = 0, tot = 0;
for (const s of w.shown) { n++; const k = words(s.prompt); tot += k; console.log(`${n}\t${s.order}\t${k}\t${s.input}\t${s.type}`); }
console.log(w.status, n, tot);
