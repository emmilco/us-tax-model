# Schedule K-1 (Form 1120-S), Shareholder's Share of Income, Deductions, Credits, etc., one per S corporation

- Document: `k1s` (form, tax year 2025)
- Collection: keyed entries within person; [i1120ssk] p. 1, General Instructions, "The corporation uses Schedule K-1 to report your share of" (2025; sha256 fb6194da)
- Note: One entry per Schedule K-1 (Form 1120-S) a person received. Boxes 1 to 5b, 7 to 8c, 13 code O, 16 codes A to D and 17 code V are entered; each box 1, 2 and 3 is one activity. Box 1 is passive or nonpassive by material participation tests 1, 3, 5 and 6; box 2 is in Form 8582 Part IV with active participation. Losses are limited by stock basis on the K-1's Form 7203 (collection f7203); the passive activity limitation (Form 8582) is applied by the return-level forms from the lines exposed here. Boxes 6, 9 to 12, 13 (other codes), 14, 15, 16 E and F and 17 (other codes), more than one activity, a disposition of stock, at-risk amounts, losses carried from earlier years by basis or at-risk limits and the other material participation tests are refused.

## (helper) — `k1s.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1120ssk] p. 1, Part III, "Ordinary business income (loss)" (2025; sha256 104ac7b1)

## (helper) — `k1s.no`

- **Authored helper label:** Year parameter s3.no (false)
- **Encoded (Bool):** Enter false (s3.no).
- Expr: `{"op":"param","ref":"s3.no"}`
- Cite: [i1120ssk] p. 6, Specific Instructions, "If you are an individual, and the above limitations don’t apply to the amounts shown on your Schedule K-1, take the amounts shown and report them on the appropriate lines of your tax return" (2025; sha256 fb6194da)

## 18, 19 — `k1s.multi`

- **IRS:** Box 18 or box 19 is checked (more than one activity for at-risk or passive activity purposes)
- **Encoded (Bool):** Input — Is box 18 or box 19 of this Schedule K-1 checked (the corporation has more than one activity)?
- Expr: `{"op":"input","source":"Is box 18 or box 19 of this Schedule K-1 checked (the corporation has more than one activity)?"}`
- Cite: [i1120ssk] p. 19, Box 18. More Than One Activity for At-Risk Purposes, "When the corporation has more than one activity for at-risk purposes, it will check this box and attach a statement"; p. 19, Box 19. More Than One Activity for Passive Activity Purposes, "When the corporation has more than one activity for passive activity purposes, it will check this box and attach a statement" (2025; sha256 fb6194da)

## (screen) — `k1s.disposed`

- **Authored helper label:** Sold or otherwise disposed of stock of the corporation in 2025, or had stock redeemed
- **Encoded (Bool):** Input — In 2025, did you sell, give away or otherwise dispose of any of your shares in this corporation, or did it buy any back from you?
- Expr: `{"op":"input","source":"In 2025, did you sell, give away or otherwise dispose of any of your shares in this corporation, or did it buy any back from you?"}`
- Cite: [i7203] p. 1, Who Must File, "Disposed of stock in an S corporation (whether or not gain is recognized)"; i7203 p. 3, Line 13, "If a portion of your stock is redeemed, sold, or otherwise disposed of during the year, attach two" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## 1 — `k1s.box1_any`

- **IRS:** Box 1 (ordinary business income (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 1 of this Schedule K-1 (ordinary business income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 1 of this Schedule K-1 (ordinary business income or loss) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Ordinary business income (loss)" (2025; sha256 104ac7b1)

## 2 — `k1s.box2_any`

- **IRS:** Box 2 (net rental real estate income (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 2 of this Schedule K-1 (net rental real estate income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 2 of this Schedule K-1 (net rental real estate income or loss) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Net rental real estate income (loss)" (2025; sha256 104ac7b1)

## 3 — `k1s.box3_any`

- **IRS:** Box 3 (other net rental income (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 3 of this Schedule K-1 (other net rental income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 3 of this Schedule K-1 (other net rental income or loss) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Other net rental income (loss)" (2025; sha256 104ac7b1)

## 4 — `k1s.box4_any`

- **IRS:** Box 4 (interest income) shows an amount
- **Encoded (Bool):** Input — Does box 4 of this Schedule K-1 (interest income) show an amount?
- Expr: `{"op":"input","source":"Does box 4 of this Schedule K-1 (interest income) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Interest income" (2025; sha256 104ac7b1)

## 5a — `k1s.box5_any`

- **IRS:** Box 5a (ordinary dividends) shows an amount
- **Encoded (Bool):** Input — Does box 5a of this Schedule K-1 (ordinary dividends) show an amount?
- Expr: `{"op":"input","source":"Does box 5a of this Schedule K-1 (ordinary dividends) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Ordinary dividends" (2025; sha256 104ac7b1)

## 1 — `k1s.box1`

- **IRS:** Ordinary business income (loss)
- **Encoded (Dollars):** Input — What amount is in box 1 (ordinary business income or loss)? Enter a loss as a negative number.
- Expr: `{"op":"input","source":"What amount is in box 1 (ordinary business income or loss)? Enter a loss as a negative number."}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (gate) — `k1s.box1_if_any`

- **Authored helper label:** Box 1, asked only when box 1 shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 1 (k1s.box1_any) = true → line 1 (k1s.box1)] [line 1 (k1s.box1_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box1_any",{"const":true}],"op":"test"},"then":"k1s.box1"},{"guard":{"eq":["k1s.box1_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## 2 — `k1s.box2`

- **IRS:** Net rental real estate income (loss)
- **Encoded (Dollars):** Input — What amount is in box 2 (net rental real estate income or loss)? Enter a loss as a negative number.
- Expr: `{"op":"input","source":"What amount is in box 2 (net rental real estate income or loss)? Enter a loss as a negative number."}`
- Cite: [i1120ssk] p. 6, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all shareholders" (2025; sha256 fb6194da)

## (gate) — `k1s.box2_if_any`

- **Authored helper label:** Box 2, asked only when box 2 shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 2 (k1s.box2_any) = true → line 2 (k1s.box2)] [line 2 (k1s.box2_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box2_any",{"const":true}],"op":"test"},"then":"k1s.box2"},{"guard":{"eq":["k1s.box2_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all shareholders" (2025; sha256 fb6194da)

## 3 — `k1s.box3`

- **IRS:** Other net rental income (loss)
- **Encoded (Dollars):** Input — What amount is in box 3 (other net rental income or loss)? Enter a loss as a negative number.
- Expr: `{"op":"input","source":"What amount is in box 3 (other net rental income or loss)? Enter a loss as a negative number."}`
- Cite: [i1120ssk] p. 7, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all shareholders" (2025; sha256 fb6194da)

## (gate) — `k1s.box3_if_any`

- **Authored helper label:** Box 3, asked only when box 3 shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 3 (k1s.box3_any) = true → line 3 (k1s.box3)] [line 3 (k1s.box3_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box3_any",{"const":true}],"op":"test"},"then":"k1s.box3"},{"guard":{"eq":["k1s.box3_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all shareholders" (2025; sha256 fb6194da)

## 4 — `k1s.box4`

- **IRS:** Interest income
- **Encoded (NonNegDollars):** Input — What amount is in box 4 (interest income)?
- Expr: `{"op":"input","source":"What amount is in box 4 (interest income)?"}`
- Cite: [i1120ssk] p. 7, Box 4. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 fb6194da)

## (gate) — `k1s.box4_if_any`

- **Authored helper label:** Box 4, asked only when box 4 shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [line 4 (k1s.box4_any) = true → line 4 (k1s.box4)] [line 4 (k1s.box4_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box4_any",{"const":true}],"op":"test"},"then":"k1s.box4"},{"guard":{"eq":["k1s.box4_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 4. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 fb6194da)

## 5a — `k1s.box5a`

- **IRS:** Ordinary dividends
- **Encoded (NonNegDollars):** Input — What amount is in box 5a (ordinary dividends)?
- Expr: `{"op":"input","source":"What amount is in box 5a (ordinary dividends)?"}`
- Cite: [i1120ssk] p. 7, Box 5a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 fb6194da)

## (gate) — `k1s.box5a_if_any`

- **Authored helper label:** Box 5a, asked only when box 5a shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [line 5a (k1s.box5_any) = true → line 5a (k1s.box5a)] [line 5a (k1s.box5_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box5_any",{"const":true}],"op":"test"},"then":"k1s.box5a"},{"guard":{"eq":["k1s.box5_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 5a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 fb6194da)

## 5b — `k1s.box5b`

- **IRS:** Qualified dividends
- **Encoded (NonNegDollars):** Input — What amount is in box 5b (qualified dividends)? Enter 0 if it is empty.
- Expr: `{"op":"input","source":"What amount is in box 5b (qualified dividends)? Enter 0 if it is empty."}`
- Cite: [i1120ssk] p. 7, Box 5b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 fb6194da)

## (gate) — `k1s.box5b_if_any`

- **Authored helper label:** Box 5b, asked only when box 5a shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [line 5a (k1s.box5_any) = true → line 5b] [line 5a (k1s.box5_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box5_any",{"const":true}],"op":"test"},"then":"k1s.box5b"},{"guard":{"eq":["k1s.box5_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 5b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 fb6194da)

## 6 — `k1s.box6`

- **IRS:** Box 6 (royalties) shows an amount
- **Encoded (Bool):** Input — Does box 6 of this Schedule K-1 (royalties) show an amount?
- Expr: `{"op":"input","source":"Does box 6 of this Schedule K-1 (royalties) show an amount?"}`
- Cite: [i1120ssk] p. 7, Box 6. Royalties, "Report royalties on Schedule E (Form 1040), line 4" (2025; sha256 fb6194da)

## 7 — `k1s.box7_any`

- **IRS:** Box 7 (net short-term capital gain (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 7 of this Schedule K-1 (net short-term capital gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 7 of this Schedule K-1 (net short-term capital gain or loss) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Net short-term capital gain (loss)" (2025; sha256 104ac7b1)

## 8a — `k1s.box8_any`

- **IRS:** Box 8a, 8b or 8c (long-term capital gain (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 8a, 8b or 8c of this Schedule K-1 (long-term capital gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 8a, 8b or 8c of this Schedule K-1 (long-term capital gain or loss) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Net long-term capital gain (loss)" (2025; sha256 104ac7b1)

## 9 — `k1s.box9`

- **IRS:** Box 9 (net section 1231 gain (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 9 of this Schedule K-1 (net section 1231 gain or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 9 of this Schedule K-1 (net section 1231 gain or loss) show an amount?"}`
- Cite: [i1120ssk] p. 7, Box 9. Net Section 1231 Gain (Loss), "The amount in box 9 is generally passive if it is from a" (2025; sha256 fb6194da)

## 10 — `k1s.box10`

- **IRS:** Box 10 (other income (loss)) shows an amount
- **Encoded (Bool):** Input — Does box 10 of this Schedule K-1 (other income or loss) show an amount?
- Expr: `{"op":"input","source":"Does box 10 of this Schedule K-1 (other income or loss) show an amount?"}`
- Cite: [i1120ssk] p. 8, Box 10. Other Income (Loss), "Losses reported in box 10 may be limited" (2025; sha256 fb6194da)

## 11, 12 — `k1s.box11_12`

- **IRS:** Box 11 (section 179 deduction) or box 12 (other deductions) shows an amount
- **Encoded (Bool):** Input — Does box 11 (section 179 deduction) or box 12 (other deductions) of this Schedule K-1 show an amount?
- Expr: `{"op":"input","source":"Does box 11 (section 179 deduction) or box 12 (other deductions) of this Schedule K-1 show an amount?"}`
- Cite: [i1120ssk] p. 9, Box 11. Section 179 Deduction, "Use this amount, along with the total cost of section 179 property placed in service during the year from other sources, to complete Part I of Form 4562"; p. 9, Box 12. Other Deductions, "Deductions reported in box 12 may be limited" (2025; sha256 fb6194da)

## 7 — `k1s.box7`

- **IRS:** Net short-term capital gain (loss)
- **Encoded (Dollars):** Input — What amount is in box 7 (net short-term capital gain or loss)? Enter a loss as a negative number.
- Expr: `{"op":"input","source":"What amount is in box 7 (net short-term capital gain or loss)? Enter a loss as a negative number."}`
- Cite: [i1120ssk] p. 7, Box 7. Net Short-Term Capital Gain (Loss), "report the net short-term capital gain (loss) on Schedule D (Form 1040), Capital Gains and Losses, line 5" (2025; sha256 fb6194da)

## (gate) — `k1s.box7_if_any`

- **Authored helper label:** Box 7, asked only when box 7 shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 7 (k1s.box7_any) = true → line 7 (k1s.box7)] [line 7 (k1s.box7_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box7_any",{"const":true}],"op":"test"},"then":"k1s.box7"},{"guard":{"eq":["k1s.box7_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 7. Net Short-Term Capital Gain (Loss), "report the net short-term capital gain (loss) on Schedule D (Form 1040), Capital Gains and Losses, line 5" (2025; sha256 fb6194da)

## 8a — `k1s.box8a`

- **IRS:** Net long-term capital gain (loss)
- **Encoded (Dollars):** Input — What amount is in box 8a (net long-term capital gain or loss)? Enter a loss as a negative number, and 0 if it is empty.
- Expr: `{"op":"input","source":"What amount is in box 8a (net long-term capital gain or loss)? Enter a loss as a negative number, and 0 if it is empty."}`
- Cite: [i1120ssk] p. 7, Box 8a. Net Long-Term Capital Gain (Loss), "report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 fb6194da)

## (gate) — `k1s.box8a_if_any`

- **Authored helper label:** Box 8a, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 8a (k1s.box8_any) = true → line 8a (k1s.box8a)] [line 8a (k1s.box8_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box8_any",{"const":true}],"op":"test"},"then":"k1s.box8a"},{"guard":{"eq":["k1s.box8_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8a. Net Long-Term Capital Gain (Loss), "report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 fb6194da)

## 8b — `k1s.box8b`

- **IRS:** Collectibles (28%) gain (loss)
- **Encoded (Dollars):** Input — What amount is in box 8b (collectibles (28%) gain or loss)? Enter a loss as a negative number, and 0 if it is empty.
- Expr: `{"op":"input","source":"What amount is in box 8b (collectibles (28%) gain or loss)? Enter a loss as a negative number, and 0 if it is empty."}`
- Cite: [i1120ssk] p. 7, Box 8b. Collectibles (28%) Gain (Loss), "report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 fb6194da)

## (gate) — `k1s.box8b_if_any`

- **Authored helper label:** Box 8b, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)
- **Encoded (Dollars):** Choose — [line 8a (k1s.box8_any) = true → line 8b] [line 8a (k1s.box8_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box8_any",{"const":true}],"op":"test"},"then":"k1s.box8b"},{"guard":{"eq":["k1s.box8_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8b. Collectibles (28%) Gain (Loss), "report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 fb6194da)

## 8c — `k1s.box8c`

- **IRS:** Unrecaptured section 1250 gain
- **Encoded (NonNegDollars):** Input — What amount is in box 8c (unrecaptured section 1250 gain)? Enter 0 if it is empty.
- Expr: `{"op":"input","source":"What amount is in box 8c (unrecaptured section 1250 gain)? Enter 0 if it is empty."}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "Report unrecaptured section 1250 gain from the sale or exchange of the corporation’s business assets on line 5" (2025; sha256 fb6194da)

## (gate) — `k1s.box8c_if_any`

- **Authored helper label:** Box 8c, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [line 8a (k1s.box8_any) = true → line 8c] [line 8a (k1s.box8_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box8_any",{"const":true}],"op":"test"},"then":"k1s.box8c"},{"guard":{"eq":["k1s.box8_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "Report unrecaptured section 1250 gain from the sale or exchange of the corporation’s business assets on line 5" (2025; sha256 fb6194da)

## (screen) — `k1s.box8_stmt`

- **Authored helper label:** Box 8c refers to an attached statement of unrecaptured section 1250 gain of other types
- **Encoded (Bool):** Input — Does box 8c say STMT, or point to an attached statement, instead of showing only an amount?
- Expr: `{"op":"input","source":"Does box 8c say STMT, or point to an attached statement, instead of showing only an amount?"}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "If it reports the other two types of unrecaptured gain, it will provide an attached statement that shows the amount for each type of unrecaptured section 1250 gain" (2025; sha256 fb6194da)

## (gate) — `k1s.box8_stmt_if_any`

- **Authored helper label:** Box 8c statement, asked only when box 8a, 8b or 8c shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 8a (k1s.box8_any) = true → helper "Box 8c refers to an attached statement of unrecaptured section 1250 gain of other types"] [line 8a (k1s.box8_any) = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box8_any",{"const":true}],"op":"test"},"then":"k1s.box8_stmt"},{"guard":{"eq":["k1s.box8_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "If it reports the other two types of unrecaptured gain, it will provide an attached statement that shows the amount for each type of unrecaptured section 1250 gain" (2025; sha256 fb6194da)

## 13 O — `k1s.box13o_any`

- **IRS:** Box 13 shows code O (backup withholding)
- **Encoded (Bool):** Input — Does box 13 of this Schedule K-1 show code O (backup withholding)?
- Expr: `{"op":"input","source":"Does box 13 of this Schedule K-1 show code O (backup withholding)?"}`
- Cite: [i1120ssk] p. 13, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 fb6194da)

## 13 — `k1s.box13_other`

- **IRS:** Box 13 shows a code other than O (credits)
- **Encoded (Bool):** Input — Does box 13 of this Schedule K-1 (credits) show any code other than O?
- Expr: `{"op":"input","source":"Does box 13 of this Schedule K-1 (credits) show any code other than O?"}`
- Cite: [i1120ssk] p. 12, Box 13. Credits, "If you have credits that are passive activity credits to you, you must complete Form 8582-CR in addition to the credit forms identified below" (2025; sha256 fb6194da)

## 14 — `k1s.box14`

- **IRS:** Box 14 is checked (Schedule K-3 attached)
- **Encoded (Bool):** Input — Is box 14 of this Schedule K-1 checked (a Schedule K-3 is attached)?
- Expr: `{"op":"input","source":"Is box 14 of this Schedule K-1 checked (a Schedule K-3 is attached)?"}`
- Cite: [i1120ssk] p. 14, Box 14. International Transactions, "If the S corporation checked the box, see the attached Schedule K-3 with respect to items of international tax relevance" (2025; sha256 fb6194da)

## 15 — `k1s.box15`

- **IRS:** Box 15 (alternative minimum tax (AMT) items) shows an amount
- **Encoded (Bool):** Input — Does box 15 of this Schedule K-1 (alternative minimum tax items) show an amount?
- Expr: `{"op":"input","source":"Does box 15 of this Schedule K-1 (alternative minimum tax items) show an amount?"}`
- Cite: [i1120ssk] p. 14, Box 15. Alternative Minimum Tax (AMT) Items, "See List of Codes, later" (2025; sha256 fb6194da)

## 16 — `k1s.box16_any`

- **IRS:** Box 16 (items affecting shareholder basis) shows an amount
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 (items affecting shareholder basis) show an amount?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 (items affecting shareholder basis) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Items affecting shareholder basis" (2025; sha256 104ac7b1)

## 17 — `k1s.box17_any`

- **IRS:** Box 17 (other information) shows an amount
- **Encoded (Bool):** Input — Does box 17 of this Schedule K-1 (other information) show an amount?
- Expr: `{"op":"input","source":"Does box 17 of this Schedule K-1 (other information) show an amount?"}`
- Cite: [f1120ssk] p. 1, Part III, "Other information" (2025; sha256 104ac7b1)

## 13 O — `k1s.box13o`

- **IRS:** Backup withholding (box 13, code O)
- **Encoded (NonNegDollars):** Input — What amount is shown in box 13 with code O (backup withholding)?
- Expr: `{"op":"input","source":"What amount is shown in box 13 with code O (backup withholding)?"}`
- Cite: [i1120ssk] p. 13, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 fb6194da)

## (gate) — `k1s.box13o_if_any`

- **Authored helper label:** Box 13 code O, asked only when box 13 shows code O (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [line 13 O (k1s.box13o_any) = true → line 13 O (k1s.box13o)] [line 13 O (k1s.box13o_any) = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box13o_any",{"const":true}],"op":"test"},"then":"k1s.box13o"},{"guard":{"eq":["k1s.box13o_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 13, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 fb6194da)

## 16 A — `k1s.box16a_any`

- **IRS:** Box 16 shows code A (tax-exempt interest income)
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 show code A (tax-exempt interest income)?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 show code A (tax-exempt interest income)?"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## (gate) — `k1s.box16a_any_if_16`

- **Authored helper label:** Box 16 code A, asked only when box 16 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 16 = true → line 16 A (k1s.box16a_any)] [line 16 = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16_any",{"const":true}],"op":"test"},"then":"k1s.box16a_any"},{"guard":{"eq":["k1s.box16_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## 16 B — `k1s.box16b_any`

- **IRS:** Box 16 shows code B (other tax-exempt income)
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 show code B (other tax-exempt income)?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 show code B (other tax-exempt income)?"}`
- Cite: [i1120ssk] p. 15, Code B. Other tax-exempt income, "Generally, you must increase the basis of your stock by the amount shown, but don’t include it in income on your tax return" (2025; sha256 fb6194da)

## (gate) — `k1s.box16b_any_if_16`

- **Authored helper label:** Box 16 code B, asked only when box 16 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 16 = true → line 16 B (k1s.box16b_any)] [line 16 = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16_any",{"const":true}],"op":"test"},"then":"k1s.box16b_any"},{"guard":{"eq":["k1s.box16_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code B. Other tax-exempt income, "Generally, you must increase the basis of your stock by the amount shown, but don’t include it in income on your tax return" (2025; sha256 fb6194da)

## 16 C — `k1s.box16c_any`

- **IRS:** Box 16 shows code C (nondeductible expenses)
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 show code C (nondeductible expenses)?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 show code C (nondeductible expenses)?"}`
- Cite: [i1120ssk] p. 15, Code C. Nondeductible expenses, "Generally, you must decrease the basis of your stock by this amount" (2025; sha256 fb6194da)

## (gate) — `k1s.box16c_any_if_16`

- **Authored helper label:** Box 16 code C, asked only when box 16 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 16 = true → line 16 C (k1s.box16c_any)] [line 16 = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16_any",{"const":true}],"op":"test"},"then":"k1s.box16c_any"},{"guard":{"eq":["k1s.box16_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code C. Nondeductible expenses, "Generally, you must decrease the basis of your stock by this amount" (2025; sha256 fb6194da)

## 16 D — `k1s.box16d_any`

- **IRS:** Box 16 shows code D (distributions)
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 show code D (distributions)?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 show code D (distributions)?"}`
- Cite: [i1120ssk] p. 15, Code D. Distributions, "Reduce the basis of your stock (as explained earlier) by distributions" (2025; sha256 fb6194da)

## (gate) — `k1s.box16d_any_if_16`

- **Authored helper label:** Box 16 code D, asked only when box 16 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 16 = true → line 16 D (k1s.box16d_any)] [line 16 = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16_any",{"const":true}],"op":"test"},"then":"k1s.box16d_any"},{"guard":{"eq":["k1s.box16_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code D. Distributions, "Reduce the basis of your stock (as explained earlier) by distributions" (2025; sha256 fb6194da)

## 16 E, F — `k1s.box16ef`

- **IRS:** Box 16 shows code E (repayment of loans from shareholders) or code F (foreign taxes paid or accrued)
- **Encoded (Bool):** Input — Does box 16 of this Schedule K-1 show code E (repayment of loans from you) or code F (foreign taxes paid or accrued)?
- Expr: `{"op":"input","source":"Does box 16 of this Schedule K-1 show code E (repayment of loans from you) or code F (foreign taxes paid or accrued)?"}`
- Cite: [i1120ssk] p. 15, Code E. Repayment of loans from shareholders, "the repayments must be allocated in part to a return of your basis in the loan and in part to the receipt of income" (2025; sha256 fb6194da)

## (gate) — `k1s.box16ef_if_16`

- **Authored helper label:** Box 16 code E or F, asked only when box 16 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 16 = true → line 16 E, F] [line 16 = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16_any",{"const":true}],"op":"test"},"then":"k1s.box16ef"},{"guard":{"eq":["k1s.box16_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code E. Repayment of loans from shareholders, "the repayments must be allocated in part to a return of your basis in the loan and in part to the receipt of income" (2025; sha256 fb6194da)

## 16 A — `k1s.box16a`

- **IRS:** Tax-exempt interest income
- **Encoded (NonNegDollars):** Input — What amount is shown in box 16 with code A (tax-exempt interest income)?
- Expr: `{"op":"input","source":"What amount is shown in box 16 with code A (tax-exempt interest income)?"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## (gate) — `k1s.box16a_if_any`

- **Authored helper label:** Box 16 code A, asked only when box 16 shows code A (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 16 code A, asked only when box 16 shows an amount (false otherwise)" = true → line 16 A (k1s.box16a)] [helper "Box 16 code A, asked only when box 16 shows an amount (false otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16a_any_if_16",{"const":true}],"op":"test"},"then":"k1s.box16a"},{"guard":{"eq":["k1s.box16a_any_if_16",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## 16 B — `k1s.box16b`

- **IRS:** Other tax-exempt income
- **Encoded (NonNegDollars):** Input — What amount is shown in box 16 with code B (other tax-exempt income)?
- Expr: `{"op":"input","source":"What amount is shown in box 16 with code B (other tax-exempt income)?"}`
- Cite: [i1120ssk] p. 15, Code B. Other tax-exempt income, "Generally, you must increase the basis of your stock by the amount shown, but don’t include it in income on your tax return" (2025; sha256 fb6194da)

## (gate) — `k1s.box16b_if_any`

- **Authored helper label:** Box 16 code B, asked only when box 16 shows code B (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 16 code B, asked only when box 16 shows an amount (false otherwise)" = true → line 16 B (k1s.box16b)] [helper "Box 16 code B, asked only when box 16 shows an amount (false otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16b_any_if_16",{"const":true}],"op":"test"},"then":"k1s.box16b"},{"guard":{"eq":["k1s.box16b_any_if_16",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code B. Other tax-exempt income, "Generally, you must increase the basis of your stock by the amount shown, but don’t include it in income on your tax return" (2025; sha256 fb6194da)

## 16 C — `k1s.box16c`

- **IRS:** Nondeductible expenses
- **Encoded (NonNegDollars):** Input — What amount is shown in box 16 with code C (nondeductible expenses)?
- Expr: `{"op":"input","source":"What amount is shown in box 16 with code C (nondeductible expenses)?"}`
- Cite: [i1120ssk] p. 15, Code C. Nondeductible expenses, "Generally, you must decrease the basis of your stock by this amount" (2025; sha256 fb6194da)

## (gate) — `k1s.box16c_if_any`

- **Authored helper label:** Box 16 code C, asked only when box 16 shows code C (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 16 code C, asked only when box 16 shows an amount (false otherwise)" = true → line 16 C (k1s.box16c)] [helper "Box 16 code C, asked only when box 16 shows an amount (false otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16c_any_if_16",{"const":true}],"op":"test"},"then":"k1s.box16c"},{"guard":{"eq":["k1s.box16c_any_if_16",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code C. Nondeductible expenses, "Generally, you must decrease the basis of your stock by this amount" (2025; sha256 fb6194da)

## 16 D — `k1s.box16d`

- **IRS:** Distributions
- **Encoded (NonNegDollars):** Input — What amount is shown in box 16 with code D (distributions)?
- Expr: `{"op":"input","source":"What amount is shown in box 16 with code D (distributions)?"}`
- Cite: [i1120ssk] p. 15, Code D. Distributions, "Reduce the basis of your stock (as explained earlier) by distributions" (2025; sha256 fb6194da)

## (gate) — `k1s.box16d_if_any`

- **Authored helper label:** Box 16 code D, asked only when box 16 shows code D (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Box 16 code D, asked only when box 16 shows an amount (false otherwise)" = true → line 16 D (k1s.box16d)] [helper "Box 16 code D, asked only when box 16 shows an amount (false otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box16d_any_if_16",{"const":true}],"op":"test"},"then":"k1s.box16d"},{"guard":{"eq":["k1s.box16d_any_if_16",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code D. Distributions, "Reduce the basis of your stock (as explained earlier) by distributions" (2025; sha256 fb6194da)

## 17 V — `k1s.box17v_any`

- **IRS:** Box 17 shows code V (section 199A information)
- **Encoded (Bool):** Input — Does box 17 of this Schedule K-1 show code V (section 199A information)?
- Expr: `{"op":"input","source":"Does box 17 of this Schedule K-1 show code V (section 199A information)?"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "The S corporation will provide the information you need to figure your deduction" (2025; sha256 fb6194da)

## (gate) — `k1s.box17v_any_if_17`

- **Authored helper label:** Box 17 code V, asked only when box 17 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 17 (k1s.box17_any) = true → line 17 V (k1s.box17v_any)] [line 17 (k1s.box17_any) = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box17_any",{"const":true}],"op":"test"},"then":"k1s.box17v_any"},{"guard":{"eq":["k1s.box17_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "The S corporation will provide the information you need to figure your deduction" (2025; sha256 fb6194da)

## 17 — `k1s.box17_other`

- **IRS:** Box 17 shows a code other than A, B, V or AC
- **Encoded (Bool):** Input — Does box 17 of this Schedule K-1 show any code other than A, B, V or AC?
- Expr: `{"op":"input","source":"Does box 17 of this Schedule K-1 show any code other than A, B, V or AC?"}`
- Cite: [i1120ssk] p. 15, Box 17. Other Information, "Code A. Investment income. Report this amount on Form 4952, line 4a"; p. 18, Code AC. Gross receipts for section 448(c), "Use the gross receipts amount to figure the business interest expense you can deduct, if applicable" (2025; sha256 fb6194da)

## (gate) — `k1s.box17_other_if_17`

- **Authored helper label:** Box 17 other codes, asked only when box 17 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 17 (k1s.box17_any) = true → line 17 (k1s.box17_other)] [line 17 (k1s.box17_any) = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box17_any",{"const":true}],"op":"test"},"then":"k1s.box17_other"},{"guard":{"eq":["k1s.box17_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Box 17. Other Information, "Code A. Investment income. Report this amount on Form 4952, line 4a"; p. 18, Code AC. Gross receipts for section 448(c), "Use the gross receipts amount to figure the business interest expense you can deduct, if applicable" (2025; sha256 fb6194da)

## 17 V — `k1s.qbi_stmt`

- **IRS:** Qualified business income (loss) on the box 17, code V statement
- **Encoded (Dollars):** Input — What qualified business income (QBI) or loss does the statement for box 17, code V show? Enter a loss as a negative number.
- Expr: `{"op":"input","source":"What qualified business income (QBI) or loss does the statement for box 17, code V show? Enter a loss as a negative number."}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "When determining QBI or qualified PTP income, you must include only those items that are qualified items of income, gain, deduction, and loss included or allowed in determining taxable income for the tax year" (2025; sha256 fb6194da)

## (gate) — `k1s.qbi_stmt_if_any`

- **Authored helper label:** QBI from the code V statement, asked only when box 17 shows code V (zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Box 17 code V, asked only when box 17 shows an amount (false otherwise)" = true → line 17 V (k1s.qbi_stmt)] [helper "Box 17 code V, asked only when box 17 shows an amount (false otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box17v_any_if_17",{"const":true}],"op":"test"},"then":"k1s.qbi_stmt"},{"guard":{"eq":["k1s.box17v_any_if_17",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "When determining QBI or qualified PTP income, you must include only those items that are qualified items of income, gain, deduction, and loss included or allowed in determining taxable income for the tax year" (2025; sha256 fb6194da)

## 17 V — `k1s.v_other`

- **IRS:** The code V statement shows section 199A dividends or qualified PTP income
- **Encoded (Bool):** Input — Does the code V statement also show section 199A (REIT) dividends or qualified PTP income?
- Expr: `{"op":"input","source":"Does the code V statement also show section 199A (REIT) dividends or qualified PTP income?"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "Section 199A dividends. The amount reported reflects your pro rata share of the S corporation’s net section 199A dividends" (2025; sha256 fb6194da)

## (gate) — `k1s.v_other_if_any`

- **Authored helper label:** Section 199A dividends or PTP income on the statement, asked only when box 17 shows code V (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 17 code V, asked only when box 17 shows an amount (false otherwise)" = true → line 17 V (k1s.v_other)] [helper "Box 17 code V, asked only when box 17 shows an amount (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box17v_any_if_17",{"const":true}],"op":"test"},"then":"k1s.v_other"},{"guard":{"eq":["k1s.box17v_any_if_17",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "Section 199A dividends. The amount reported reflects your pro rata share of the S corporation’s net section 199A dividends" (2025; sha256 fb6194da)

## (screen) — `k1s.work`

- **Authored helper label:** You or your spouse worked in the corporation's business in 2025
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) work in this corporation's business?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) work in this corporation's business?"}`
- Cite: [i1120ssk] p. 4, Work counted toward material participation, "Generally, any work that you or your spouse does in connection with an activity held through an S corporation (where you own your stock at the time the work is done) is counted toward material participation" (2025; sha256 fb6194da)

## (gate) — `k1s.work_if_b1`

- **Authored helper label:** Worked in the business, asked only when box 1 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 1 (k1s.box1_any) = true → helper "You or your spouse worked in the corporation's business in 2025"] [line 1 (k1s.box1_any) = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box1_any",{"const":true}],"op":"test"},"then":"k1s.work"},{"guard":{"eq":["k1s.box1_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 4, Work counted toward material participation, "Generally, any work that you or your spouse does in connection with an activity held through an S corporation (where you own your stock at the time the work is done) is counted toward material participation" (2025; sha256 fb6194da)

## (screen) — `k1s.hours500`

- **Authored helper label:** Material participation test 1: more than 500 hours in 2025
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) work more than 500 hours in it in 2025, counting both of you together?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) work more than 500 hours in it in 2025, counting both of you together?"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (gate) — `k1s.hours500_if_work`

- **Authored helper label:** More than 500 hours, asked only when you or your spouse worked in the business (false otherwise)
- **Encoded (Bool):** Choose — [helper "Worked in the business, asked only when box 1 shows an amount (false otherwise)" = true → helper "Material participation test 1: more than 500 hours in 2025"] [helper "Worked in the business, asked only when box 1 shows an amount (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.work_if_b1",{"const":true}],"op":"test"},"then":"k1s.hours500"},{"guard":{"eq":["k1s.work_if_b1",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (helper) — `k1s.under500`

- **Authored helper label:** Worked in the business, but not more than 500 hours
- **Encoded (Bool):** helper "Worked in the business, asked only when box 1 shows an amount (false otherwise)" = true and helper "More than 500 hours, asked only when you or your spouse worked in the business (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1s.work_if_b1",{"const":true}],"op":"test"},{"eq":["k1s.hours500_if_work",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (screen) — `k1s.most_hours`

- **Authored helper label:** Material participation test 3: more than 100 hours, and not less than any other individual
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) work more than 100 hours in it in 2025, with no one else, employees included, working more?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) work more than 100 hours in it in 2025, with no one else, employees included, working more?"}`
- Cite: [i1120ssk] p. 4, Individuals, "You participated in the activity for more than 100 hours during the tax year, and your participation in the activity for the tax year wasn’t less than the participation in the activity of any other individual" (2025; sha256 fb6194da)

## (gate) — `k1s.most_hours_if_under`

- **Authored helper label:** More than 100 hours and no one more, asked only when you worked in it but not more than 500 hours (false otherwise)
- **Encoded (Bool):** Choose — [helper "Worked in the business, but not more than 500 hours" = true → helper "Material participation test 3: more than 100 hours, and not less than any other individual"] [helper "Worked in the business, but not more than 500 hours" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.under500",{"const":true}],"op":"test"},"then":"k1s.most_hours"},{"guard":{"eq":["k1s.under500",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 4, Individuals, "You participated in the activity for more than 100 hours during the tax year, and your participation in the activity for the tax year wasn’t less than the participation in the activity of any other individual" (2025; sha256 fb6194da)

## (helper) — `k1s.mp_now`

- **Authored helper label:** Material participation by test 1 or test 3
- **Encoded (Bool):** (helper "More than 500 hours, asked only when you or your spouse worked in the business (false otherwise)" = true or helper "More than 100 hours and no one more, asked only when you worked in it but not more than 500 hours (false otherwise)" = true)
- Expr: `{"any":[{"eq":["k1s.hours500_if_work",{"const":true}],"op":"test"},{"eq":["k1s.most_hours_if_under",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (helper) — `k1s.past_ask`

- **Authored helper label:** Box 1 shows an amount and neither test 1 nor test 3 is met
- **Encoded (Bool):** line 1 (k1s.box1_any) = true and helper "Material participation by test 1 or test 3" = false
- Expr: `{"all":[{"eq":["k1s.box1_any",{"const":true}],"op":"test"},{"eq":["k1s.mp_now",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (screen) — `k1s.past_years`

- **Authored helper label:** Material participation test 5 or 6: earlier years
- **Encoded (Bool):** Input — In at least 5 of the years 2015 to 2024 (or any 3 earlier years, if it is a personal service business), did you (or, on a joint return, your spouse) materially participate in this business (its income or loss was nonpassive on your return)?
- Expr: `{"op":"input","source":"In at least 5 of the years 2015 to 2024 (or any 3 earlier years, if it is a personal service business), did you (or, on a joint return, your spouse) materially participate in this business (its income or loss was nonpassive on your return)?"}`
- Cite: [i1120ssk] p. 4, Individuals, "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year"; "The activity was a personal service activity and you materially participated in the activity for any 3 tax years (whether or not consecutive) preceding the tax year" (2025; sha256 fb6194da)

## (gate) — `k1s.past_years_if_ask`

- **Authored helper label:** Earlier years, asked only when box 1 shows an amount and test 1 or 3 is not met (false otherwise)
- **Encoded (Bool):** Choose — [helper "Box 1 shows an amount and neither test 1 nor test 3 is met" = true → helper "Material participation test 5 or 6: earlier years"] [helper "Box 1 shows an amount and neither test 1 nor test 3 is met" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.past_ask",{"const":true}],"op":"test"},"then":"k1s.past_years"},{"guard":{"eq":["k1s.past_ask",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 4, Individuals, "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year"; "The activity was a personal service activity and you materially participated in the activity for any 3 tax years (whether or not consecutive) preceding the tax year" (2025; sha256 fb6194da)

## (helper) — `k1s.other_ask`

- **Authored helper label:** Worked in the business in 2025, and no test of 1, 3, 5 or 6 is met
- **Encoded (Bool):** helper "Worked in the business, asked only when box 1 shows an amount (false otherwise)" = true and helper "Material participation by test 1 or test 3" = false and helper "Earlier years, asked only when box 1 shows an amount and test 1 or 3 is not met (false otherwise)" = false
- Expr: `{"all":[{"eq":["k1s.work_if_b1",{"const":true}],"op":"test"},{"eq":["k1s.mp_now",{"const":false}],"op":"test"},{"eq":["k1s.past_years_if_ask",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below"; p. 4, Individuals, "You participated in the activity for more than 500 hours during the tax year" (2025; sha256 fb6194da)

## (screen) — `k1s.mp_other`

- **Authored helper label:** Material participation by test 2, 4 or 7
- **Encoded (Bool):** Input — Did you do nearly all the work done in it, or work over 100 hours in it and over 500 hours in all such businesses together, or meet another test of material participation?
- Expr: `{"op":"input","source":"Did you do nearly all the work done in it, or work over 100 hours in it and over 500 hours in all such businesses together, or meet another test of material participation?"}`
- Cite: [i1120ssk] p. 4, Individuals, "Your participation in the activity for the tax year constituted substantially all the participation in the activity of all individuals"; "The activity was a significant participation activity for the tax year, and you participated in all significant participation activities (including activities outside the corporation) during the year for more than 500 hours" (2025; sha256 fb6194da)

## (gate) — `k1s.mp_other_if_ask`

- **Authored helper label:** Other tests, asked only when you worked in it and no test of 1, 3, 5 or 6 is met (false otherwise)
- **Encoded (Bool):** Choose — [helper "Worked in the business in 2025, and no test of 1, 3, 5 or 6 is met" = true → helper "Material participation by test 2, 4 or 7"] [helper "Worked in the business in 2025, and no test of 1, 3, 5 or 6 is met" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.other_ask",{"const":true}],"op":"test"},"then":"k1s.mp_other"},{"guard":{"eq":["k1s.other_ask",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 4, Individuals, "Your participation in the activity for the tax year constituted substantially all the participation in the activity of all individuals"; "The activity was a significant participation activity for the tax year, and you participated in all significant participation activities (including activities outside the corporation) during the year for more than 500 hours" (2025; sha256 fb6194da)

## (gate) — `k1s.material`

- **Authored helper label:** Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)
- **Encoded (Bool):** (helper "Material participation by test 1 or test 3" = true or helper "Earlier years, asked only when box 1 shows an amount and test 1 or 3 is not met (false otherwise)" = true)
- Expr: `{"any":[{"eq":["k1s.mp_now",{"const":true}],"op":"test"},{"eq":["k1s.past_years_if_ask",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 5, Effect of determination, "Income (loss), deductions, and credits from an activity are nonpassive if you determine that"; p. 4, Material participation, "Material participation standards for shareholders who are individuals are listed below" (2025; sha256 fb6194da)

## (screen) — `k1s.active`

- **Authored helper label:** Actively participated in the corporation's rental real estate activity
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) help make management decisions for its rental real estate, such as approving tenants, rents or repairs?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) help make management decisions for its rental real estate, such as approving tenants, rents or repairs?"}`
- Cite: [i1120ssk] p. 5, Special allowance for a rental real estate activity, "You may be treated as actively participating if you participated, for example, in making management decisions or arranging for others to provide services (such as repairs) in a significant and bona fide sense" (2025; sha256 fb6194da)

## (gate) — `k1s.active_if_b2`

- **Authored helper label:** Management decisions, asked only when box 2 shows an amount (false otherwise)
- **Encoded (Bool):** Choose — [line 2 (k1s.box2_any) = true → helper "Actively participated in the corporation's rental real estate activity"] [line 2 (k1s.box2_any) = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.box2_any",{"const":true}],"op":"test"},"then":"k1s.active"},{"guard":{"eq":["k1s.box2_any",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 5, Special allowance for a rental real estate activity, "You may be treated as actively participating if you participated, for example, in making management decisions or arranging for others to provide services (such as repairs) in a significant and bona fide sense" (2025; sha256 fb6194da)

## (screen) — `k1s.tenth`

- **Authored helper label:** Your and your spouse's interest was at least 10% (by value) all year
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) own at least a tenth of this corporation's stock, by value, all through 2025?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) own at least a tenth of this corporation's stock, by value, all through 2025?"}`
- Cite: [i1120ssk] p. 5, Special allowance for a rental real estate activity, "You aren’t considered to actively participate in a rental real estate activity if, at any time during the tax year, your interest (including your spouse’s interest) in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 fb6194da)

## (gate) — `k1s.tenth_if_active`

- **Authored helper label:** At least a tenth all year, asked only when you helped make management decisions (false otherwise)
- **Encoded (Bool):** Choose — [helper "Management decisions, asked only when box 2 shows an amount (false otherwise)" = true → helper "Your and your spouse's interest was at least 10% (by value) all year"] [helper "Management decisions, asked only when box 2 shows an amount (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.active_if_b2",{"const":true}],"op":"test"},"then":"k1s.tenth"},{"guard":{"eq":["k1s.active_if_b2",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 5, Special allowance for a rental real estate activity, "You aren’t considered to actively participate in a rental real estate activity if, at any time during the tax year, your interest (including your spouse’s interest) in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 fb6194da)

## (gate) — `k1s.part4`

- **Authored helper label:** Box 2 activity with active participation (Form 8582 Part IV)
- **Encoded (Bool):** helper "Management decisions, asked only when box 2 shows an amount (false otherwise)" = true and helper "At least a tenth all year, asked only when you helped make management decisions (false otherwise)" = true
- Expr: `{"all":[{"eq":["k1s.active_if_b2",{"const":true}],"op":"test"},{"eq":["k1s.tenth_if_active",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (screen) — `k1s.prior_any`

- **Authored helper label:** A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)
- **Encoded (Bool):** Input — Was a loss from this corporation held back on your 2024 return by the passive activity rules (Form 8582)?
- Expr: `{"op":"input","source":"Was a loss from this corporation held back on your 2024 return by the passive activity rules (Form 8582)?"}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (screen) — `k1s.basis_carry`

- **Authored helper label:** Losses or deductions from this corporation not allowed in an earlier year because of the basis limitation
- **Encoded (Bool):** Input — Was a loss or deduction from this corporation held back on an earlier return because your basis in it was too low?
- Expr: `{"op":"input","source":"Was a loss or deduction from this corporation held back on an earlier return because your basis in it was too low?"}`
- Cite: [i7203] p. 4, Part III. Shareholder Allowable Loss and Deduction Items, "Column (b). Enter any loss or deduction items disallowed due to basis limitations in prior years that were carried forward" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (screen) — `k1s.risk_carry`

- **Authored helper label:** A loss from this corporation not allowed in an earlier year because of the at-risk limitation
- **Encoded (Bool):** Input — Was a loss from this corporation held back on an earlier return by the at-risk rules (Form 6198)?
- Expr: `{"op":"input","source":"Was a loss from this corporation held back on an earlier return by the at-risk rules (Form 6198)?"}`
- Cite: [i1120ssk] p. 3, At-Risk Limitations, "Any loss from a section 465 activity not allowed for this tax year will be treated as a deduction allocable to the activity in the next tax year" (2025; sha256 fb6194da)

## (c) — `k1s.b1_prior`

- **Authored helper label:** Prior-year unallowed loss of the box 1 activity (2024 Form 8582, Part VII, column (c))
- **Encoded (NonNegDollars):** Input — How much of the loss from its box 1 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none.
- Expr: `{"op":"input","source":"How much of the loss from its box 1 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none."}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (gate) — `k1s.b1_prior_if_any`

- **Authored helper label:** Prior-year unallowed loss of the box 1 activity, asked only when a loss was held back (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = true → column (c) (k1s.b1_prior)] [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.prior_any",{"const":true}],"op":"test"},"then":"k1s.b1_prior"},{"guard":{"eq":["k1s.prior_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (c) — `k1s.b2_prior`

- **Authored helper label:** Prior-year unallowed loss of the box 2 activity (2024 Form 8582, Part VII, column (c))
- **Encoded (NonNegDollars):** Input — How much of the loss from its box 2 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none.
- Expr: `{"op":"input","source":"How much of the loss from its box 2 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none."}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (gate) — `k1s.b2_prior_if_any`

- **Authored helper label:** Prior-year unallowed loss of the box 2 activity, asked only when a loss was held back (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = true → column (c) (k1s.b2_prior)] [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.prior_any",{"const":true}],"op":"test"},"then":"k1s.b2_prior"},{"guard":{"eq":["k1s.prior_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (c) — `k1s.b3_prior`

- **Authored helper label:** Prior-year unallowed loss of the box 3 activity (2024 Form 8582, Part VII, column (c))
- **Encoded (NonNegDollars):** Input — How much of the loss from its box 3 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none.
- Expr: `{"op":"input","source":"How much of the loss from its box 3 activity was held back on your 2024 Form 8582 (Part VII, column (c))? Enter 0 if none."}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (gate) — `k1s.b3_prior_if_any`

- **Authored helper label:** Prior-year unallowed loss of the box 3 activity, asked only when a loss was held back (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = true → column (c) (k1s.b3_prior)] [helper "A loss from this corporation was not allowed on the 2024 Form 8582 (prior-year unallowed passive loss)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.prior_any",{"const":true}],"op":"test"},"then":"k1s.b3_prior"},{"guard":{"eq":["k1s.prior_any",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (gate) — `k1s.former_passive`

- **Authored helper label:** A prior-year unallowed passive loss of the box 1 activity, which is not passive this year
- **Encoded (Bool):** helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = true and helper "Prior-year unallowed loss of the box 1 activity, asked only when a loss was held back (zero otherwise)" > $0
- Expr: `{"all":[{"eq":["k1s.material",{"const":true}],"op":"test"},{"gt":["k1s.b1_prior_if_any",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)

## (helper) — `k1s.gain1`

- **Authored helper label:** Box 1 income (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 1, asked only when box 1 shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.box1_if_any","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss1`

- **Authored helper label:** Box 1 loss, as a positive amount (zero for income)
- **Encoded (NonNegDollars):** Subtract helper "Box 1, asked only when box 1 shows an amount (zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.box1_if_any"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.gain2`

- **Authored helper label:** Box 2 income (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 2, asked only when box 2 shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.box2_if_any","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss2`

- **Authored helper label:** Box 2 loss, as a positive amount (zero for income)
- **Encoded (NonNegDollars):** Subtract helper "Box 2, asked only when box 2 shows an amount (zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.box2_if_any"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.gain3`

- **Authored helper label:** Box 3 income (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 3, asked only when box 3 shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.box3_if_any","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss3`

- **Authored helper label:** Box 3 loss, as a positive amount (zero for income)
- **Encoded (NonNegDollars):** Subtract helper "Box 3, asked only when box 3 shows an amount (zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.box3_if_any"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.gain7`

- **Authored helper label:** Box 7 gain (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 7, asked only when box 7 shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.box7_if_any","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss7`

- **Authored helper label:** Box 7 loss, as a positive amount (zero for a gain)
- **Encoded (NonNegDollars):** Subtract helper "Box 7, asked only when box 7 shows an amount (zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.box7_if_any"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.gain8`

- **Authored helper label:** Box 8a gain (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 8a, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.box8a_if_any","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss8`

- **Authored helper label:** Box 8a loss, as a positive amount (zero for a gain)
- **Encoded (NonNegDollars):** Subtract helper "Box 8a, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.box8a_if_any"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.loss_items`

- **Authored helper label:** Total of the losses in boxes 1, 2, 3, 7 and 8a, as a positive amount
- **Encoded (NonNegDollars):** Add helper "Box 1 loss, as a positive amount (zero for income)", helper "Box 2 loss, as a positive amount (zero for income)", helper "Box 3 loss, as a positive amount (zero for income)", helper "Box 7 loss, as a positive amount (zero for a gain)", and helper "Box 8a loss, as a positive amount (zero for a gain)".
- Interpretation: amb.2025.f7203_capital_lines
- Expr: `{"of":["k1s.loss1","k1s.loss2","k1s.loss3","k1s.loss7","k1s.loss8"],"op":"sum"}`
- Cite: [i7203] p. 2, Line 3, "Reminder. Enter only positive amounts from Schedule K-1 (Form 1120-S) on line 3. Negative amounts (decreases to stock basis) are entered in Part III" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (gate) — `k1s.f7203_required`

- **Authored helper label:** Form 7203 is required: a loss or deduction item, or a distribution (box 16, code D)
- **Encoded (Bool):** (helper "Total of the losses in boxes 1, 2, 3, 7 and 8a, as a positive amount" > $0 or helper "Box 16 code D, asked only when box 16 shows code D (zero otherwise)" > $0)
- Interpretation: amb.2025.f7203_required
- Expr: `{"any":[{"gt":["k1s.loss_items",{"const":0}],"op":"test"},{"gt":["k1s.box16d_if_any",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i7203] p. 1, Who Must File, "Are claiming a deduction for their share of an aggregate loss from an S corporation"; "Received a non-dividend distribution from an S corporation" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.allowed1`

- **Authored helper label:** Box 1 loss allowed by stock basis (Form 7203 line 35, column (c))
- **Encoded (NonNegDollars):** Add f7203.c35 over every confirmed f7203 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f7203","field":"f7203.c35","op":"sum_over"}`
- Cite: [i7203] p. 5, Column (e), "The allowable losses and deductions from columns (c) and (d) should be reported on the appropriate areas of your return (subject to any additional limitations)" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.allowed2`

- **Authored helper label:** Box 2 loss allowed by stock basis (Form 7203 line 36, column (c))
- **Encoded (NonNegDollars):** Add f7203.c36 over every confirmed f7203 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f7203","field":"f7203.c36","op":"sum_over"}`
- Cite: [i7203] p. 5, Column (e), "The allowable losses and deductions from columns (c) and (d) should be reported on the appropriate areas of your return (subject to any additional limitations)" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.allowed3`

- **Authored helper label:** Box 3 loss allowed by stock basis (Form 7203 line 37, column (c))
- **Encoded (NonNegDollars):** Add f7203.c37 over every confirmed f7203 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f7203","field":"f7203.c37","op":"sum_over"}`
- Cite: [i7203] p. 5, Column (e), "The allowable losses and deductions from columns (c) and (d) should be reported on the appropriate areas of your return (subject to any additional limitations)" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.basis_carry_out`

- **Authored helper label:** Losses carried to 2026 by the basis limitation (Form 7203 line 47, column (e))
- **Encoded (NonNegDollars):** Add f7203.e47 over every confirmed f7203 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f7203","field":"f7203.e47","op":"sum_over"}`
- Cite: [i7203] p. 5, Column (e), "The allowable losses and deductions from columns (c) and (d) should be reported on the appropriate areas of your return (subject to any additional limitations)" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.f7203_n`

- **Authored helper label:** One Form 7203 for this corporation, screened
- **Encoded (Count):** Add f7203.one over every confirmed f7203 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f7203","field":"f7203.one","op":"sum_over"}`
- Cite: [i7203] p. 1, Purpose of Form, "Use Form 7203 to figure potential limitations of your share of the S corporation's deductions, credits, and other items that can be deducted on your return" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (screen) — `k1s.not_at_risk`

- **Authored helper label:** Some of the stock or loan basis is not at risk (nonrecourse, guaranteed, borrowed from an owner, or similar)
- **Encoded (Bool):** Input — Did you pay for your shares, or for loans to the corporation, with money borrowed on terms that protect you from loss (a loan you are not personally liable for, or one someone guarantees for you), or borrowed from another owner of the corporation or someone related to one?
- Expr: `{"op":"input","source":"Did you pay for your shares, or for loans to the corporation, with money borrowed on terms that protect you from loss (a loan you are not personally liable for, or one someone guarantees for you), or borrowed from another owner of the corporation or someone related to one?"}`
- Cite: [i1120ssk] p. 3, At-Risk Limitations, "you will have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 fb6194da)

## (helper) — `k1s.has_loss`

- **Authored helper label:** A loss in box 1, 2, 3, 7 or 8a
- **Encoded (Bool):** helper "Total of the losses in boxes 1, 2, 3, 7 and 8a, as a positive amount" > $0
- Expr: `{"gt":["k1s.loss_items",{"const":0}],"op":"test"}`
- Cite: [i1120ssk] p. 3, At-Risk Limitations, "you will have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 fb6194da)

## (gate) — `k1s.not_at_risk_if_loss`

- **Authored helper label:** Not at risk, asked only when a box shows a loss (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss in box 1, 2, 3, 7 or 8a" = true → helper "Some of the stock or loan basis is not at risk (nonrecourse, guaranteed, borrowed from an owner, or similar)"] [helper "A loss in box 1, 2, 3, 7 or 8a" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.has_loss",{"const":true}],"op":"test"},"then":"k1s.not_at_risk"},{"guard":{"eq":["k1s.has_loss",{"const":false}],"op":"test"},"then":"k1s.no"}],"op":"choose"}`
- Cite: [i1120ssk] p. 3, At-Risk Limitations, "you will have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 fb6194da)

## (gate) — `k1s.ok`

- **Authored helper label:** This Schedule K-1 passes every screen and its Form 7203 is supported
- **Encoded (Bool):** helper "One Form 7203 for this corporation, screened" = 1 (a count)
- **Refusal:** when k1s.multi is true, cannot complete Schedule K-1 (Form 1120-S) with more than one activity (box 18 or 19). A corporation with more than one activity reports each on an attached statement, and each activity's income and losses are limited separately; that is outside this tool. Cite: [i1120ssk] p. 19, Box 19. More Than One Activity for Passive Activity Purposes, "Use the information in the attached statement to correctly determine your passive activity limitations" (2025; sha256 fb6194da)
- **Refusal:** when k1s.disposed is true, cannot complete Form 7203 for a disposition of S corporation stock, and Form 8949. A sale or other disposition of S corporation stock, or a redemption, needs the stock basis at the date of sale (two Forms 7203) and the gain or loss on Form 8949; that is outside this tool. Cite: [i7203] p. 3, Line 13, "If a portion of your stock is redeemed, sold, or otherwise disposed of during the year, attach two" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)
- **Refusal:** when k1s.box6 is true, cannot complete Schedule E (Form 1040), line 4 (royalties from a Schedule K-1). Royalties from an S corporation are reported on Schedule E line 4, which this tool does not prepare for a Schedule K-1. Cite: [i1120ssk] p. 7, Box 6. Royalties, "Report royalties on Schedule E (Form 1040), line 4" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box8_stmt_if_any is true, cannot complete Unrecaptured section 1250 gain from an attached statement. Unrecaptured section 1250 gain of the other two types is reported from the corporation's statement on other lines of the worksheet; that is outside this tool. Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "If it reports the other two types of unrecaptured gain, it will provide an attached statement that shows the amount for each type of unrecaptured section 1250 gain" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box9 is true, cannot complete Form 4797 (net section 1231 gain or loss from a Schedule K-1). Section 1231 gain or loss is reported on Form 4797, which this tool does not prepare. Cite: [i1120ssk] p. 7, Box 9. Net Section 1231 Gain (Loss), "The amount in box 9 is generally passive if it is from a" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box10 is true, cannot complete Schedule K-1 (Form 1120-S), box 10 (other income (loss)). The items of box 10 go to forms and lines this tool does not prepare. Cite: [i1120ssk] p. 8, Box 10. Other Income (Loss), "Losses reported in box 10 may be limited" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box11_12 is true, cannot complete Schedule K-1 (Form 1120-S), boxes 11 and 12 (section 179 and other deductions). Section 179 and the other deductions of box 12 are limited and reported on forms this tool does not prepare. Cite: [i1120ssk] p. 9, Box 12. Other Deductions, "Deductions reported in box 12 may be limited" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box13_other is true, cannot complete Credits from a Schedule K-1 (Form 1120-S), box 13 (Form 3800, Form 8582-CR). The credits of box 13, other than backup withholding, are figured on forms this tool does not prepare. Cite: [i1120ssk] p. 12, Box 13. Credits, "If you have credits that are passive activity credits to you, you must complete Form 8582-CR in addition to the credit forms identified below" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box14 is true, cannot complete Schedule K-3 (Form 1120-S) (international items). Items of international tax relevance reported on Schedule K-3 are outside this tool. Cite: [i1120ssk] p. 14, Box 14. International Transactions, "If the S corporation checked the box, see the attached Schedule K-3 with respect to items of international tax relevance" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box15 is true, cannot complete Form 6251 (alternative minimum tax items from a Schedule K-1). Alternative minimum tax items are figured on Form 6251, which this tool does not prepare. Cite: [i1120ssk] p. 14, Box 15. Alternative Minimum Tax (AMT) Items, "See List of Codes, later" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box16ef_if_16 is true, cannot complete Form 7203 Part II (loan repayments) or Form 1116 (foreign taxes from a Schedule K-1). A repayment of a loan you made to the corporation, and foreign taxes it paid, are figured on forms this tool does not prepare. Cite: [i1120ssk] p. 15, Code E. Repayment of loans from shareholders, "the repayments must be allocated in part to a return of your basis in the loan and in part to the receipt of income" (2025; sha256 fb6194da)
- **Refusal:** when k1s.box17_other_if_17 is true, cannot complete Schedule K-1 (Form 1120-S), box 17 (other information). The codes of box 17 other than A, B, V and AC go to forms this tool does not prepare. Cite: [i1120ssk] p. 15, Box 17. Other Information, "Code A. Investment income. Report this amount on Form 4952, line 4a"; p. 18, Code AC. Gross receipts for section 448(c), "Use the gross receipts amount to figure the business interest expense you can deduct, if applicable" (2025; sha256 fb6194da)
- **Refusal:** when k1s.v_other_if_any is true, cannot complete Form 8995, lines 6 to 9 (section 199A dividends and qualified PTP income). Section 199A dividends and qualified PTP income from an S corporation are outside this tool. Cite: [i1120ssk] p. 17, Code V. Section 199A information, "Section 199A dividends. The amount reported reflects your pro rata share of the S corporation’s net section 199A dividends" (2025; sha256 fb6194da)
- **Refusal:** when k1s.mp_other_if_ask is true, cannot complete Schedule E (Form 1040), Part II, with material participation by test 2, 4 or 7. Material participation by these tests is outside this tool. Cite: [i1120ssk] p. 4, Individuals, "Your participation in the activity for the tax year constituted substantially all the participation in the activity of all individuals"; "The activity was a significant participation activity for the tax year, and you participated in all significant participation activities (including activities outside the corporation) during the year for more than 500 hours" (2025; sha256 fb6194da)
- **Refusal:** when k1s.former_passive is true, cannot complete Form 8582 (prior-year unallowed loss of an activity that is not passive this year). A prior-year unallowed loss of an activity in which you now materially participate is allowed under special rules that are outside this tool. Cite: [i8582] p. 10, Column (c), "Enter the prior-year unallowed losses for each activity" (2025; sha256 76787e11)
- **Refusal:** when k1s.basis_carry is true, cannot complete Form 7203, Part III, column (b), and Schedule E (Form 1040), line 27. A loss or deduction carried from an earlier year by the basis limitation is outside this tool. Cite: [i7203] p. 4, Part III. Shareholder Allowable Loss and Deduction Items, "Column (b). Enter any loss or deduction items disallowed due to basis limitations in prior years that were carried forward" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)
- **Refusal:** when k1s.risk_carry is true, cannot complete Form 6198 (At-Risk Limitations). A loss carried from an earlier year by the at-risk limitation is figured on Form 6198, which this tool does not prepare. Cite: [i1120ssk] p. 3, At-Risk Limitations, "Any loss from a section 465 activity not allowed for this tax year will be treated as a deduction allocable to the activity in the next tax year" (2025; sha256 fb6194da)
- **Refusal:** when k1s.not_at_risk_if_loss is true, cannot complete Form 6198 (At-Risk Limitations). A loss with amounts not at risk is figured on Form 6198, which this tool does not prepare. Cite: [i1120ssk] p. 3, At-Risk Limitations, "you will have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity" (2025; sha256 fb6194da)
- Expr: `{"eq":["k1s.f7203_n",{"const":1,"type":"Count"}],"op":"test"}`
- Cite: [i1120ssk] p. 6, Specific Instructions, "If any of the above limitations apply, adjust the amounts on Schedule K-1 before you report them on your return" (2025; sha256 fb6194da)

## (helper) — `k1s.b1_net`

- **Authored helper label:** Box 1 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))
- **Encoded (Dollars):** Subtract helper "Box 1 loss allowed by stock basis (Form 7203 line 35, column (c))" from helper "Box 1 income (zero for a loss)".
- Expr: `{"from":"k1s.gain1","op":"subtract","take":"k1s.allowed1"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "report your box 1 income (loss) as instructed after applying the basis and at-risk limitations on losses" (2025; sha256 fb6194da)

## (helper) — `k1s.b2_net`

- **Authored helper label:** Box 2 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))
- **Encoded (Dollars):** Subtract helper "Box 2 loss allowed by stock basis (Form 7203 line 36, column (c))" from helper "Box 2 income (zero for a loss)".
- Expr: `{"from":"k1s.gain2","op":"subtract","take":"k1s.allowed2"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "report your box 1 income (loss) as instructed after applying the basis and at-risk limitations on losses" (2025; sha256 fb6194da)

## (helper) — `k1s.b3_net`

- **Authored helper label:** Box 3 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))
- **Encoded (Dollars):** Subtract helper "Box 3 loss allowed by stock basis (Form 7203 line 37, column (c))" from helper "Box 3 income (zero for a loss)".
- Expr: `{"from":"k1s.gain3","op":"subtract","take":"k1s.allowed3"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "report your box 1 income (loss) as instructed after applying the basis and at-risk limitations on losses" (2025; sha256 fb6194da)

## (gate) — `k1s.basis_cut`

- **Authored helper label:** Some loss of this K-1 is carried to 2026 by the basis limitation
- **Encoded (Bool):** helper "Losses carried to 2026 by the basis limitation (Form 7203 line 47, column (e))" > $0
- Expr: `{"gt":["k1s.basis_carry_out",{"const":0}],"op":"test"}`
- Cite: [i7203] p. 4, Part III. Shareholder Allowable Loss and Deduction Items, "Loss and deductions in excess of basis are suspended and carried forward indefinitely and the character of the loss and deduction items is retained" (Rev. December 2022 (Instructions for Form 7203; the current irs-pdf edition; no 2025 revision exists); sha256 f2a4a124)

## (helper) — `k1s.b1_np`

- **Authored helper label:** Box 1 after basis when materially participated (nonpassive; zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = true → helper "Box 1 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))"] [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.material",{"const":true}],"op":"test"},"then":"k1s.b1_net"},{"guard":{"eq":["k1s.material",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.b1_passive`

- **Authored helper label:** Box 1 after basis when not materially participated (passive; zero otherwise)
- **Encoded (Dollars):** Choose — [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = false → helper "Box 1 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))"] [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = true → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.material",{"const":false}],"op":"test"},"then":"k1s.b1_net"},{"guard":{"eq":["k1s.material",{"const":true}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you didn’t materially participate as follows" (2025; sha256 fb6194da)

## 28 (k) — `k1s.col_k`

- **IRS:** Schedule E line 28, column (k): nonpassive income (box 1, materially participated)
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Nonpassive box 1 income"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.np_income"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.np_income`

- **Authored helper label:** Nonpassive box 1 income
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 1 after basis when materially participated (nonpassive; zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.b1_np","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.np_loss`

- **Authored helper label:** Nonpassive box 1 loss allowed by basis, as a positive amount
- **Encoded (NonNegDollars):** Subtract helper "Box 1 after basis when materially participated (nonpassive; zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.b1_np"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## 28 (i) — `k1s.col_i`

- **IRS:** Schedule E line 28, column (i): nonpassive loss allowed (box 1, materially participated), as a positive amount
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Nonpassive box 1 loss allowed by basis, as a positive amount"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.np_loss"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p1_income`

- **Authored helper label:** Passive box 1 income
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 1 after basis when not materially participated (passive; zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"k1s.b1_passive","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p1_loss`

- **Authored helper label:** Passive box 1 loss after basis, as a positive amount
- **Encoded (NonNegDollars):** Subtract helper "Box 1 after basis when not materially participated (passive; zero otherwise)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.b1_passive"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p2_income`

- **Authored helper label:** Box 2 income (passive)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 2 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))". If zero or less, enter -0-.
- Expr: `{"from":"k1s.b2_net","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p2_loss`

- **Authored helper label:** Box 2 loss after basis, as a positive amount (passive)
- **Encoded (NonNegDollars):** Subtract helper "Box 2 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.b2_net"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p3_income`

- **Authored helper label:** Box 3 income (passive)
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Box 3 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))". If zero or less, enter -0-.
- Expr: `{"from":"k1s.b3_net","op":"subtract_floor0","take":"k1s.zero"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p3_loss`

- **Authored helper label:** Box 3 loss after basis, as a positive amount (passive)
- **Encoded (NonNegDollars):** Subtract helper "Box 3 after the basis limitation: the income, or the loss allowed (Form 7203, Part III, column (c))" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"k1s.zero","op":"subtract_floor0","take":"k1s.b3_net"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.passive_income`

- **Authored helper label:** Passive income of boxes 1, 2 and 3
- **Encoded (NonNegDollars):** Add helper "Passive box 1 income", helper "Box 2 income (passive)", and helper "Box 3 income (passive)".
- Expr: `{"of":["k1s.p1_income","k1s.p2_income","k1s.p3_income"],"op":"sum"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## 28 (h) — `k1s.col_h`

- **IRS:** Schedule E line 28, column (h): passive income
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Passive income of boxes 1, 2 and 3"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.passive_income"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.p4_income_raw`

- **Authored helper label:** Box 2 income with active participation (Form 8582 Part IV, column (a))
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Box 2 income (passive)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.p2_income"},{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p4_loss_raw`

- **Authored helper label:** Box 2 loss with active participation (Form 8582 Part IV, column (b))
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Box 2 loss after basis, as a positive amount (passive)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.p2_loss"},{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p4_prior_raw`

- **Authored helper label:** Prior-year unallowed loss of the box 2 activity with active participation (Form 8582 Part IV, column (c))
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Prior-year unallowed loss of the box 2 activity, asked only when a loss was held back (zero otherwise)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.b2_prior_if_any"},{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p5_b2_income`

- **Authored helper label:** Box 2 income without active participation
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Box 2 income (passive)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.p2_income"},{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p5_b2_loss`

- **Authored helper label:** Box 2 loss without active participation
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Box 2 loss after basis, as a positive amount (passive)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.p2_loss"},{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p5_b2_prior`

- **Authored helper label:** Prior-year unallowed loss of the box 2 activity without active participation
- **Encoded (NonNegDollars):** Choose — [helper "Box 2 activity with active participation (Form 8582 Part IV)" = false → helper "Prior-year unallowed loss of the box 2 activity, asked only when a loss was held back (zero otherwise)"] [helper "Box 2 activity with active participation (Form 8582 Part IV)" = true → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.part4",{"const":false}],"op":"test"},"then":"k1s.b2_prior_if_any"},{"guard":{"eq":["k1s.part4",{"const":true}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p4_income`

- **Authored helper label:** Form 8582 Part IV, column (a): net income
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 2 income with active participation (Form 8582 Part IV, column (a))"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p4_income_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p4_loss`

- **Authored helper label:** Form 8582 Part IV, column (b): net loss
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 2 loss with active participation (Form 8582 Part IV, column (b))"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p4_loss_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p4_prior`

- **Authored helper label:** Form 8582 Part IV, column (c): prior-year unallowed loss
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Prior-year unallowed loss of the box 2 activity with active participation (Form 8582 Part IV, column (c))"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p4_prior_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `k1s.p5_income_raw`

- **Authored helper label:** Passive income outside Part IV (boxes 1, 3 and box 2 without active participation)
- **Encoded (NonNegDollars):** Add helper "Passive box 1 income", helper "Box 2 income without active participation", and helper "Box 3 income (passive)".
- Expr: `{"of":["k1s.p1_income","k1s.p5_b2_income","k1s.p3_income"],"op":"sum"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p5_loss_raw`

- **Authored helper label:** Passive losses outside Part IV
- **Encoded (NonNegDollars):** Add helper "Passive box 1 loss after basis, as a positive amount", helper "Box 2 loss without active participation", and helper "Box 3 loss after basis, as a positive amount (passive)".
- Expr: `{"of":["k1s.p1_loss","k1s.p5_b2_loss","k1s.p3_loss"],"op":"sum"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p1_prior_passive`

- **Authored helper label:** Prior-year unallowed loss of the box 1 activity when it is passive this year
- **Encoded (NonNegDollars):** Choose — [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = false → helper "Prior-year unallowed loss of the box 1 activity, asked only when a loss was held back (zero otherwise)"] [helper "Materially participated in the corporation's trade or business activity (tests 1, 3, 5 or 6)" = true → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.material",{"const":false}],"op":"test"},"then":"k1s.b1_prior_if_any"},{"guard":{"eq":["k1s.material",{"const":true}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p5_prior_raw`

- **Authored helper label:** Prior-year unallowed losses outside Part IV
- **Encoded (NonNegDollars):** Add helper "Prior-year unallowed loss of the box 1 activity when it is passive this year", helper "Prior-year unallowed loss of the box 2 activity without active participation", and helper "Prior-year unallowed loss of the box 3 activity, asked only when a loss was held back (zero otherwise)".
- Expr: `{"of":["k1s.p1_prior_passive","k1s.p5_b2_prior","k1s.b3_prior_if_any"],"op":"sum"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p5_income`

- **Authored helper label:** Form 8582 Part V, column (a): net income (sum over this K-1's Part V activities)
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Passive income outside Part IV (boxes 1, 3 and box 2 without active participation)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p5_income_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p5_loss`

- **Authored helper label:** Form 8582 Part V, column (b): net loss (sum over this K-1's Part V activities)
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Passive losses outside Part IV"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p5_loss_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.p5_prior`

- **Authored helper label:** Form 8582 Part V, column (c): prior-year unallowed loss (sum over this K-1's Part V activities)
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Prior-year unallowed losses outside Part IV"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.p5_prior_raw"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `k1s.int`

- **Authored helper label:** Interest income (box 4), for Form 1040 line 2b
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 4, asked only when box 4 shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box4_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 4. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 fb6194da)

## (helper) — `k1s.ord_div`

- **Authored helper label:** Ordinary dividends (box 5a), for Form 1040 line 3b
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 5a, asked only when box 5a shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box5a_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 5a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 fb6194da)

## (helper) — `k1s.qual_div`

- **Authored helper label:** Qualified dividends (box 5b), for Form 1040 line 3a
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 5b, asked only when box 5a shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box5b_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 5b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 fb6194da)

## (helper) — `k1s.st`

- **Authored helper label:** Net short-term capital gain (loss) (box 7), for Schedule D line 5
- **Encoded (Dollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 7, asked only when box 7 shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box7_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 7. Net Short-Term Capital Gain (Loss), "report the net short-term capital gain (loss) on Schedule D (Form 1040), Capital Gains and Losses, line 5" (2025; sha256 fb6194da)

## (helper) — `k1s.lt`

- **Authored helper label:** Net long-term capital gain (loss) (box 8a), for Schedule D line 12
- **Encoded (Dollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 8a, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box8a_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8a. Net Long-Term Capital Gain (Loss), "report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 fb6194da)

## (helper) — `k1s.g28`

- **Authored helper label:** Collectibles (28%) gain (loss) (box 8b), for the 28% Rate Gain Worksheet line 4
- **Encoded (Dollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 8b, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box8b_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8b. Collectibles (28%) Gain (Loss), "report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 fb6194da)

## (helper) — `k1s.u1250`

- **Authored helper label:** Unrecaptured section 1250 gain (box 8c), for the Unrecaptured Section 1250 Gain Worksheet line 5
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 8c, asked only when box 8a, 8b or 8c shows an amount (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box8c_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "Report unrecaptured section 1250 gain from the sale or exchange of the corporation’s business assets on line 5" (2025; sha256 fb6194da)

## (helper) — `k1s.backup`

- **Authored helper label:** Backup withholding (box 13, code O), for Form 1040 line 25c
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 13 code O, asked only when box 13 shows code O (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box13o_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 13, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 fb6194da)

## (helper) — `k1s.taxexempt`

- **Authored helper label:** Tax-exempt interest (box 16, code A), for Form 1040 line 2a
- **Encoded (NonNegDollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 16 code A, asked only when box 16 shows code A (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.box16a_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## (helper) — `k1s.nonpassive`

- **Authored helper label:** Nonpassive trade or business income (loss) after basis (box 1, materially participated)
- **Encoded (Dollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "Box 1 after basis when materially participated (nonpassive; zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.b1_np"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (gate) — `k1s.qbi_cut`

- **Authored helper label:** A qualified business loss on a K-1 whose losses are partly carried to 2026 by the basis limitation
- **Encoded (Bool):** helper "QBI from the code V statement, asked only when box 17 shows code V (zero otherwise)" < $0 and helper "Some loss of this K-1 is carried to 2026 by the basis limitation" = true
- Interpretation: amb.2025.k1s_qbi_basis
- Expr: `{"all":[{"lt":["k1s.qbi_stmt_if_any",{"const":0}],"op":"test"},{"eq":["k1s.basis_cut",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "When determining QBI or qualified PTP income, you must include only those items that are qualified items of income, gain, deduction, and loss included or allowed in determining taxable income for the tax year" (2025; sha256 fb6194da)

## (helper) — `k1s.qbi`

- **Authored helper label:** Qualified business income (loss) from this K-1 before the passive activity limitation (box 17, code V)
- **Encoded (Dollars):** Choose — [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = true → helper "QBI from the code V statement, asked only when box 17 shows code V (zero otherwise)"] [helper "This Schedule K-1 passes every screen and its Form 7203 is supported" = false → helper "Year parameter sales.zero"]
- **Refusal:** when k1s.qbi_cut is true, cannot complete Form 8995 with a qualified business loss limited by stock basis. When a loss is partly carried forward by the basis limitation, only the allowed part of the qualified business loss counts this year; working out that part is outside this tool. Cite: [i1120ssk] p. 17, Code V. Section 199A information, "When determining QBI or qualified PTP income, you must include only those items that are qualified items of income, gain, deduction, and loss included or allowed in determining taxable income for the tax year" (2025; sha256 fb6194da)
- Expr: `{"alternatives":[{"guard":{"eq":["k1s.ok",{"const":true}],"op":"test"},"then":"k1s.qbi_stmt_if_any"},{"guard":{"eq":["k1s.ok",{"const":false}],"op":"test"},"then":"k1s.zero"}],"op":"choose"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "When determining QBI or qualified PTP income, you must include only those items that are qualified items of income, gain, deduction, and loss included or allowed in determining taxable income for the tax year" (2025; sha256 fb6194da)

## (helper) — `k1s.one`

- **Authored helper label:** One Schedule K-1
- **Encoded (Count):** Enter 1 (ss.one).
- Expr: `{"op":"param","ref":"ss.one"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `k1s.sche_any`

- **Authored helper label:** Box 1, 2 or 3 of this K-1 shows an amount (a row on Schedule E, line 28)
- **Encoded (Bool):** (line 1 (k1s.box1_any) = true or line 2 (k1s.box2_any) = true or line 3 (k1s.box3_any) = true)
- Expr: `{"any":[{"eq":["k1s.box1_any",{"const":true}],"op":"test"},{"eq":["k1s.box2_any",{"const":true}],"op":"test"},{"eq":["k1s.box3_any",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)
