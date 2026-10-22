# Class M hand-work — dcprov

`Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | e16d355204dcfa391c54f7477fd8727a43e9a59929c8cb7be9048a7d0b6b21df |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i2441 | 2025 | 2, 3 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 2, 3 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p503 | For use in preparing 2025 returns | 8 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 8 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### case classm.dcprov.1 — prompt sha256 a6668a6c65f8bbf29e6e3186630901966397665dc07b9b8f44406f8212638ada; branches: dcprov.household:false, dcprov.related:false, dcprov.see_statement:false

### classm.dcprov.1 — dcprov[prov_a].see_statement — Column (c) reads "See Attached Statement"
Status: **AGREE**

Value: no

## Raw responses

### classm.dcprov.1

```yaml
lines:
  - printed: "dcprov[prov_a].see_statement"
    value: "no"
    work: "Under Due Diligence, you enter 'See Attached Statement' only for information the provider didn't give you. This provider gave an identifying number (tin), so column (c) gets that number instead."
```
