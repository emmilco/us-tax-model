// Integration checks invoke the command-line backend, including negative cases.
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { loadCases } from "./fixtures.js";
import type { CanonicalData, Inputs } from "./types.js";

export function integrationChecks(): void {
  const dir=mkdtempSync(join(tmpdir(),"stage2-integration-"));
  let checks=0;
  const cli=(args:string[],ok=true):any=>{
    const p=spawnSync(process.execPath,[resolve(import.meta.dirname,"main.js"),...args],{encoding:"utf8"});
    assert.equal(p.status===0,ok,`${args.join(" ")}: ${p.stderr || p.stdout}`);
    checks++;
    return ok ? JSON.parse(p.stdout) : null;
  };
  const evaluate=(inputs:Inputs,ok=true,target="f1040.line31")=>{
    const path=join(dir,"inputs.json");writeFileSync(path,JSON.stringify(inputs));
    return cli(["eval","--inputs",path,"--target",target,"--json"],ok);
  };
  try {
    const fixture=loadCases().cases.find(c=>c.id==="ss.multi")!;
    const inputs=fixture.inputs;
    const log=join(dir,"answers.jsonl");
    let state=cli(["interview","start","--log",log]);
    const answer=(key:string,value:unknown)=>cli(["interview","answer","--log",log,"--input",key,"--value",JSON.stringify(value)]);
    assert.equal(state.question.input,"f1040.status");
    state=answer("f1040.status",null);
    assert.equal(state.status,"incomplete");assert.equal(state.question.helpRequested,true);
    let steps=0;
    while(state.status==="incomplete"&&steps++<30){
      const key=state.question.input;assert.ok(key in inputs,key);
      state=answer(key,inputs[key]);
    }
    assert.equal(state.status,"complete");
    assert.deepEqual(state.values["f1040.line31"].value,{kind:"money",cents:148180});
    assert.match(state.sheet,/\$1,481\.80/);assert.match(state.sheet,/sha|482e9c|i1040gi/);
    const before=readFileSync(log,"utf8");
    state=answer("person[taxpayer].w2[a].box4",1091821);
    assert.equal(state.status,"refused");assert.match(state.refusal.remedy,/Form 843/);
    assert.ok(readFileSync(log,"utf8").startsWith(before));
    state=answer("person[taxpayer].w2[a].box4",620000);assert.equal(state.status,"complete");
    state=answer("$w2@person[taxpayer]",["a"]);assert.equal(state.values["f1040.line31"].value.cents,0);
    state=answer("$w2@person[taxpayer]",["a","b"]);assert.equal(state.status,"complete");
    cli(["interview","start","--log",log],false); // never overwrite a log
    const early={...inputs};delete early["person[taxpayer].w2[b].box4"];
    delete early["person[taxpayer].w2[a].box3"];early["person[taxpayer].w2[a].box4"]=1091821;
    assert.equal(evaluate(early).values["f1040.line31"].value.kind,"refusal");
    const missing={...inputs};delete missing["$w2@person[taxpayer]"];
    for(const k of Object.keys(missing))if(k.includes(".w2["))delete missing[k];
    assert.equal(evaluate(missing).values["f1040.line31"].value.kind,"unknown");
    for(const bad of [-1,0.5,"100",Number.MAX_SAFE_INTEGER+1]) evaluate({...inputs,"person[taxpayer].w2[a].box4":bad},false);
    evaluate({...inputs,"$w2@person[taxpayer]":["a","a"]},false);
    evaluate({...inputs,"person[taxpayer].w2[ghost].box4":1},false);
    evaluate({...inputs,"person[taxpayer].w2[a].box3":Number.MAX_SAFE_INTEGER,"person[taxpayer].w2[a].box7":1},false);
    const htmlPath=join(dir,"html-input.json");writeFileSync(htmlPath,JSON.stringify(inputs));
    const html=spawnSync(process.execPath,[resolve(import.meta.dirname,"main.js"),"eval","--inputs",htmlPath,"--target","f1040.line31","--html"],{encoding:"utf8"});
    assert.equal(html.status,0);assert.match(html.stdout,/<!doctype html>/);assert.match(html.stdout,/\$1,481\.80/);checks++;
    const checksData=loadCanonical();
    const badData=(change:(d:CanonicalData)=>void)=>{
      const d=structuredClone(checksData);change(d);const path=join(dir,"bad.json");writeFileSync(path,JSON.stringify(d));cli(["check",path],false);
    };
    const line=(d:CanonicalData,id:string)=>d.forms.flatMap(f=>f.lines).find(l=>l.id===id)!;
    badData(d=>{line(d,"person.over").expr={op:"test",eq:["person.over",{const:true}]};});
    badData(d=>{line(d,"person.credit").expr={op:"choose",alternatives:[{guard:{op:"test",eq:["person.credit",{const:0}]},then:"person.zero"}]};});
    badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"w2.over"};});
    badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"f1040.line15"};});
    badData(d=>{line(d,"s3.line11").expr={op:"sum_over",collection:"w2",field:"w2.box4"};});
    badData(d=>{line(d,"person.employers").expr={op:"sum_over",collection:"w2",field:"w2.one",where:{op:"test",eq:["missing.field",{const:true}]}};});
    badData(d=>{line(d,"person.over").expr={op:"test",gt:["person.overcount",{const:0}]};});
    // A filter edge back to the aggregate must not escape the cycle walk.
    badData(d=>{line(d,"w2.over").expr={op:"test",gt:["person.overcount",{const:0,type:"Count"}]};});
    console.log(`integration: ${checks} CLI invocations passed (interview, corrections, early refusals, invalid inputs, graph/type failures)`);
  } finally {rmSync(dir,{recursive:true,force:true});}
}
