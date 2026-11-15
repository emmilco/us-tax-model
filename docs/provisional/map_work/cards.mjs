// Scratch: the vetting cards (asking order, gate questions) as JSON.
import { loadContext } from "../../../engine/dist/interview-rules.js";
import { vettingCards } from "../../../engine/dist/vetting.js";
import { writeFileSync } from "node:fs";
const ctx = loadContext();
const cards = vettingCards(ctx.data, ctx.configs[process.argv[2] ?? "full"]);
writeFileSync(new URL("./cards.json", import.meta.url), JSON.stringify(cards, null, 1));
console.log(cards.length, JSON.stringify(cards[30]).slice(0, 1500));
