# Class M hand-work — ny_it2

`Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e0fbd910bf8f10143578331902ebb8bb7ca5de5c735669e9dd2fd269945d0fda |
| cases | 1 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it2 | Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26 | 1, 2 | whole document | 4884d0d4403f8d1f3bd71a6834951e51fca1ca288ff3ecbab3c6866a286c10b8 | 2 | a6e61a9d7a0cd5464a36232dae9d0f4d5ca5380323f1117a2077f7e621049739 |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 17, 21 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 17, 21 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### case classm.ny_it2.1 — prompt sha256 c451e99e248e97d765c8c0fb37d1da9f1c0c2bf729805db3d2d8bf16337fc038; branches: ny_it2.yonkers_gate:false

### classm.ny_it2.1 — ny_it2[w0].state_whole — NYS income tax withheld, in whole dollars
Status: **AGREE**

Value: $0.00

### classm.ny_it2.1 — ny_it2[w0].city_whole — Local income tax withheld (New York City), in whole dollars
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.ny_it2.1

```yaml
lines:
  - printed: "ny_it2[w0].state_whole"
    value: "0.00"
    work: "Box 17a: $0.00 rounded to whole dollars (drop under 50 cents) = $0"
  - printed: "ny_it2[w0].city_whole"
    value: "0.00"
    work: "Box 19 NYC: $0.00 rounded to whole dollars (drop under 50 cents) = $0"
```
