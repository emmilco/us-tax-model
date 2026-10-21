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
    const p=spawnSync(process.execPath,[resolve(import.meta.dirname,"main.js"),...args],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
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
    const html=spawnSync(process.execPath,[resolve(import.meta.dirname,"main.js"),"eval","--inputs",htmlPath,"--target","f1040.line31","--html"],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
    assert.equal(html.status,0);assert.match(html.stdout,/<!doctype html>/);assert.match(html.stdout,/\$1,481\.80/);checks++;
    // Entry sections: a business, its implicit Form 4562 after it, and each asset with only the
    // lines Form 4562 reports it on (a listed asset on 25 and 26, the other on 14 and 19).
    {
      const fx=JSON.parse(readFileSync(resolve(import.meta.dirname,"../../fixtures/2025/stage14.json"),"utf-8")) as {cases:{id:string;inputs:Record<string,unknown>}[]};
      const assetCase=fx.cases.find(c=>c.id==="stage14.asset.listed_and_not")!;
      const sheetPath=join(dir,"sheet-input.json");writeFileSync(sheetPath,JSON.stringify(assetCase.inputs));
      const sheet=spawnSync(process.execPath,[resolve(import.meta.dirname,"main.js"),"eval","--inputs",sheetPath],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
      assert.equal(sheet.status,0);
      const section=(entry:string)=>{const parts=sheet.stdout.split(/\n(?=== )/);const s=parts.find(p=>p.split("\n")[0]!.endsWith(`— ${entry} ==`));assert.ok(s,`no section for ${entry}`);return s!;};
      const order=sheet.stdout.indexOf("— person[taxpayer].sc[d] =="), f4562=sheet.stdout.indexOf("— person[taxpayer].sc[d].f4562[form] ==");
      assert.ok(order>=0&&f4562>order,"the Form 4562 section follows its Schedule C");checks++;
      const printed=(s:string)=>s.split("\n").slice(1).filter(l=>/^ {2}\S/.test(l)).map(l=>l.trim().split(/\s+/)[0]);
      const cam=printed(section("person[taxpayer].sc[d].asset[cam]")), pc=printed(section("person[taxpayer].sc[d].asset[pc]"));
      assert.ok(cam.includes("25")&&cam.includes("26(h)")&&!cam.includes("14")&&!cam.includes("19(g)"),`listed asset lines: ${cam.join(",")}`);checks++;
      assert.ok(pc.includes("14")&&pc.includes("19(g)")&&!pc.includes("25")&&!pc.includes("26(h)"),`other asset lines: ${pc.join(",")}`);checks++;
    }
    const checksData=loadCanonical();
    const badData=(change:(d:CanonicalData)=>void)=>{
      const d=structuredClone(checksData);change(d);const path=join(dir,"bad.json");writeFileSync(path,JSON.stringify(d));cli(["check",path],false);
    };
    const line=(d:CanonicalData,id:string)=>d.forms.flatMap(f=>f.lines).find(l=>l.id===id)!;
    badData(d=>{line(d,"person.over").expr={op:"test",eq:["person.over",{const:true}]};});
    // shown_when must name a Bool line of the same document; an implicit collection needs a parent.
    badData(d=>{line(d,"asset.bonus").shown_when="asset.cost";});
    badData(d=>{const f=d.forms.find(x=>x.id==="f4562")!;f.collection={implicit:"form",cite:f.collection!.cite};});
    badData(d=>{line(d,"person.credit").expr={op:"choose",alternatives:[{guard:{op:"test",eq:["person.credit",{const:0}]},then:"person.zero"}]};});
    badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"w2.over"};});
    badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"f1040.line15"};});
    badData(d=>{line(d,"s3.line11").expr={op:"sum_over",collection:"w2",field:"w2.box4"};});
    badData(d=>{line(d,"person.employers").expr={op:"sum_over",collection:"w2",field:"w2.one",where:{op:"test",eq:["missing.field",{const:true}]}};});
    badData(d=>{line(d,"person.over").expr={op:"test",gt:["person.overcount",{const:0}]};});
    // A filter edge back to the aggregate must not escape the cycle walk.
    badData(d=>{line(d,"w2.over").expr={op:"test",gt:["person.overcount",{const:0,type:"Count"}]};});
    // Sales profile: complete, corrected refusal, restored roster, and early digital refusal.
    for (const id of ["sales.official.basis", "sales.official.two_aggregate", "sales.refuse.digital.G", "sales.select.sdtw.election"]) {
      const sales = loadCases().cases.find(c=>c.id===id)!;
      const salesLog=join(dir,id+".jsonl");
      let salesState=cli(["interview","start","--profile","sales","--log",salesLog]);
      let count=0;
      while(salesState.status==="incomplete" && count++<150) {
        const key=salesState.question.input;
        assert.ok(key in sales.inputs, `missing sales input ${key}`);
        salesState=cli(["interview","answer","--log",salesLog,"--input",key,"--value",JSON.stringify(sales.inputs[key])]);
      }
      assert.equal(salesState.status, id.includes("refuse") ? "refused" : "complete");
      if (id==="sales.official.basis") {
        assert.equal(salesState.values["f1040.line7a"].value.cents,90000);
        const correction=(input:string,value:unknown)=>cli(["interview","answer","--log",salesLog,"--input",input,"--value",JSON.stringify(value)]);
        salesState=correction("sales[a].box","G"); assert.equal(salesState.status,"refused");
        salesState=correction("sales[a].box","A"); assert.equal(salesState.status,"complete");
        salesState=correction("$sales",[]); assert.equal(salesState.values["f1040.line7a"].value.cents,0);
        salesState=correction("$sales",["a"]); assert.equal(salesState.values["f1040.line7a"].value.cents,90000);
        cli(["interview","advance","--profile","social-security","--log",salesLog],false);
      }
    }
    const sale=loadCases().cases.find(c=>c.id==="sales.official.basis")!.inputs;
    evaluate({...sale,"$sales":["a","a"]},false,"f1040.line7a");
    evaluate({...sale,"sales[a].wash_loss":-1},false,"f1040.line7a");
    evaluate({...sale,"sales[a].box":"Z"},false,"f1040.line7a");
    assert.equal(evaluate({...sale,"$sales":["a","missing"]},true,"f1040.line7a").values["f1040.line7a"].value.kind,"unknown");
    badData(d=>{line(d,"sd.limited_loss").expr={op:"larger_of",of:["sd.limited_loss","sd.loss_limit"]};});
    for(const id of ["stage4.base","stage4.sdtw.special_rates","stage4.refuse.scope.schedule1"]) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const path=join(dir,id+".jsonl");
      let state=cli(["interview","start","--profile","stage4","--log",path]);
      for(let step=0;state.status==="incomplete"&&step<150;step++) {
        const key=state.question.input;assert.ok(key in fixture.inputs,`missing ${key}`);
        state=cli(["interview","answer","--log",path,"--input",key,"--value",JSON.stringify(fixture.inputs[key])]);
      }
      assert.equal(state.status,id.includes("refuse")?"refused":"complete");
      if(id==="stage4.sdtw.special_rates")assert.equal(state.values["f1040.line16"].value.cents,6166300);
      if(id==="stage4.base") {
        assert.equal(state.values["sa.deduction"].value.cents,1575000);
        state=cli(["interview","answer","--log",path,"--input","sa.line8a","--value","2000000"]);
        assert.equal(state.values["sa.deduction"].value.cents,2000000);
        cli(["interview","answer","--log",path,"--input","f8959.line18","--value","1"],false);
      }
    }
    for(const id of ["stage5.return.owed","stage5.return.refund"]) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const path=join(dir,id+".jsonl");
      let state=cli(["interview","start","--profile","full","--log",path]);
      for(let step=0;state.status==="incomplete"&&step<200;step++) {
        const key=state.question.input;assert.ok(key in fixture.inputs,`missing ${key}`);
        state=cli(["interview","answer","--log",path,"--input",key,"--value",JSON.stringify(fixture.inputs[key])]);
      }
      assert.equal(state.status,"complete");
      if(id==="stage5.return.owed")assert.equal(state.values["f1040.line37"].value.cents,150000);
      if(id==="stage5.return.refund")assert.equal(state.values["f1040.line34"].value.cents,173300);
    }
    console.log(`integration: ${checks} CLI invocations passed (interview, corrections, early refusals, invalid inputs, graph/type failures)`);
  } finally {rmSync(dir,{recursive:true,force:true});}
}
