// Run from the repository root after applying BUG-0111.patch in an isolated copy.
import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
import { loadCanonical } from '../../engine/dist/canonical.js';
import { evaluate } from '../../engine/dist/eval.js';
const data=loadCanonical();
const fixture=JSON.parse(readFileSync('fixtures/2025/stage15.json','utf8')).cases.find(c=>c.id==='stage15.f2441.s8');
const key='dependent[a].dc_line2c';
const variants=[
  {name:'age12-disabled',age:12,incapable:true,expected:false},
  {name:'age13-before-birthday',age:13,incapable:true,care:false,expected:false},
  {name:'age13-after-birthday',age:13,incapable:true,care:true,expected:true},
  {name:'age13-unanswered-timing',age:13,incapable:true,expected:'unknown'},
  {name:'age13-not-disabled',age:13,incapable:false,expected:false},
  {name:'age14-disabled',age:14,incapable:true,expected:true},
];
for(const v of variants){
 const inputs={...fixture.inputs,'dependent[a].age':v.age,'dependent[a].dc_incapable':v.incapable,'dependent[a].dc_under13':true};
 if(v.care!==undefined)inputs['dependent[a].dc_over12_care']=v.care;
 const result=evaluate(data,inputs,[key,...Object.keys(fixture.expect)]);
 const answer=result.values.get(key);
 if(v.expected==='unknown'){
   assert.equal(answer.kind,'unknown');assert.equal(answer.input,'dependent[a].dc_over12_care');
 }else assert.deepEqual(answer,{kind:'bool',value:v.expected});
 for(const [line,value] of Object.entries(fixture.expect))assert.deepEqual(result.values.get(line),value,`${v.name}: ${line}`);
 console.log('ok',v.name);
}
