# Image-grounded audit of the archived text layers

Tesseract tesseract 5.5.2 over pages rendered at 300 dpi with pdftoppm (tools/ocr_audit.py). Per page, words of at least three characters that the image reading has and the text layer lacks, and the reverse; a word is explained by a text-layer word within edit similarity 0.85, by two or three adjacent words read as one, by leader dots read as letters, or by being a bare number. OCR noise is expected; each listed page is adjudicated once against the page image.

| document | pages | words in layer | words in image | pages with image-only words | pages with layer-only words |
| --- | --- | --- | --- | --- | --- |
| f1040 | 2 | 1609 | 1649 | 2 | 2 |
| f1040s2 | 2 | 796 | 812 | 2 | 2 |
| f1040s3 | 1 | 470 | 466 | 1 | 1 |
| f1040s8812 | 2 | 985 | 989 | 2 | 2 |
| f1040sa | 1 | 620 | 616 | 1 | 1 |
| f1040sb | 1 | 528 | 523 | 1 | 1 |
| f1040sd | 2 | 1064 | 1077 | 2 | 2 |
| f1099div | 6 | 1966 | 1979 | 2 | 1 |
| f1099int | 7 | 2644 | 2658 | 4 | 2 |
| f4952 | 4 | 2363 | 2363 | 3 | 2 |
| f8283 | 2 | 1476 | 1462 | 2 | 1 |
| f8949 | 2 | 1242 | 1251 | 2 | 2 |
| f8959 | 1 | 611 | 601 | 1 | 1 |
| f8960 | 1 | 539 | 531 | 1 | 1 |
| f8995 | 1 | 427 | 432 | 1 | 0 |
| f8995a | 2 | 853 | 862 | 2 | 1 |
| fw2 | 11 | 3713 | 3613 | 6 | 7 |
| i1040gi | 126 | 128115 | 127788 | 75 | 68 |
| i1040s8812 | 9 | 4902 | 5047 | 4 | 5 |
| i1040sb | 3 | 2365 | 2370 | 2 | 3 |
| i1040sca | 18 | 19681 | 19726 | 10 | 14 |
| i1040sd | 16 | 15474 | 15526 | 8 | 6 |
| i1099div | 5 | 4547 | 4543 | 1 | 4 |
| i1099int | 8 | 8736 | 8735 | 3 | 5 |
| i1116 | 26 | 23781 | 24020 | 10 | 9 |
| i8283 | 12 | 11177 | 11185 | 2 | 3 |
| i8949 | 13 | 13549 | 13545 | 4 | 2 |
| i8959 | 4 | 3379 | 3384 | 2 | 2 |
| i8960 | 25 | 18981 | 19145 | 21 | 12 |
| i8995 | 11 | 7394 | 7411 | 6 | 2 |
| i8995a | 12 | 10816 | 10833 | 7 | 2 |
| iw2w3 | 35 | 33837 | 33935 | 15 | 15 |
| p505-2026 | 48 | 39201 | 39840 | 25 | 23 |
| p526 | 40 | 30616 | 30827 | 8 | 8 |
| p550 | 117 | 103514 | 103918 | 14 | 18 |
| p561 | 16 | 18931 | 19007 | 4 | 3 |
| rp-2024-40 | 27 | 7224 | 7279 | 4 | 3 |

## Per page

## f1040

- p. 1: image only ['acp', 'aoc', 'cies', 'dit', 'eermanentiy', 'eulktime', 'eulntime', 'eulstime', 'fulktime', 'gas', 'ila', 'lit', 'loe', 'palf', 'rere'] …; layer only ['ira', 'qcd', 'student', 'totally', 'type', 'with', 'yyyy']
- p. 2: image only ['18a', 'addiines', 'addlines19and20', 'addlinesi6and17', 'aecsumtammbey', 'boe', 'gont', 'inate', 'mawied', 'suniven', 'tod', 'wwe']; layer only ['12b', '12c', '12d', '25b', 'account', 'earned', 'gross', 'head', 'single', 'surviving', 'through']

## f1040s2

- p. 1: image only ['addlinestathroughiy', 'line2qa', 'lines5and6', 'lineta', 'o25', 'reservedforfutureuse', 'was']; layer only ['future', 'not', 'reserved', 'through', 'use']
- p. 2: image only ['lagigg', 'toe']; layer only ['17l', '17o']

## f1040s3

- p. 1: image only ['2adt', 'loe']; layer only ['13c', 'iii']

## f1040s8812

- p. 1: image only ['1oby5', 'aco', 'addlinesland2d', 'addliness5and7', 'cok', 'foe', 'loe', 'multiplyline6by', 'wee']; layer only ['excluded']
- p. 2: image only ['20o0rline25', 'addilines21and22', 'eclami', 'jamie', 'l6aorline', 'laaif', 'loe']; layer only ['add', 'future', 'less']

## f1040sa

- p. 1: image only ['addlines11throughi3', 'addlines5athrough5c', 'addlines5eand6', 'addlines8eand9', 'carryoverfromprioryear', 'deduston', 'loe', 'loko', 'o07', 'oko', 'rai', 'reservedforfutureuse']; layer only ['address', 'carryover', 'future', 'prior', 'reserved', 'rules', 'special', 'year']

## f1040sb

- p. 1: image only ['addtheamountsonline1', 'ill', 'loe', 'o25', 'tae0o74']; layer only ['iii']

## f1040sd

- p. 1: image only ['dlj', 'fomis', 'illonthe', 'ljno', 'loe', 'ouacnment']; layer only ['attachment']
- p. 2: image only ['leis']; layer only ['iii', 'part']

## f1099div

- p. 1: image only []; layer only ['attention']
- p. 2: image only ['pres']; layer only []
- p. 4: image only ['099div']; layer only []

## f1099int

- p. 1: image only []; layer only ['attention']
- p. 2: image only ['099int']; layer only []
- p. 3: image only ['099int', 'voip']; layer only ['void']
- p. 4: image only ['099int']; layer only []
- p. 6: image only ['099int']; layer only []

## f4952

- p. 1: image only ['4efromline4d', 'o25', 'ome', 'tees', 'toe']; layer only ['iii', 'omb']
- p. 3: image only ['iil']; layer only []
- p. 4: image only ['abies', 'mabie']; layer only ['caution', 'iii', 'tip']

## f8283

- p. 1: image only ['2l00']; layer only []
- p. 2: image only ['iif', "laai'a"]; layer only ['iii']

## f8949

- p. 1: image only ['o25', 'umn']; layer only ['part']
- p. 2: image only ['umn']; layer only ['part']

## f8959

- p. 1: image only ['amountfromline4', 'andgotoparttv', 'enterhereandgotopartlv', 'entertheamountfromline1', 'fata', 'gotopartill', 'loe', 'lok', 'muti', 'o25', 'toe', 'tok', 'waa']; layer only ['iii', 'loss']

## f8960

- p. 1: image only ['addlines9dand10', 'combinelines4aand4b', 'enterthesmallerofline12orline15', 'loe', 'ofline18corline19c', 'toe']; layer only ['add', 'iii', 'less']

## f8995

- p. 1: image only ['good', 'loe']; layer only []

## f8995a

- p. 1: image only ['een', 'line3orline10', 'loe', 'o25', 'ofline11orline12']; layer only ['reported']
- p. 2: image only ['ill', 'itz', 'loe', 'toe']; layer only []

## fw2

- p. 1: image only []; layer only ['attention']
- p. 2: image only ['peoes', 'reign', 'reti', 'voo']; layer only ['12b', 'official', 'omb', 'only', 'party', 'pay', 'retirement', 'sick', 'statutory', 'void']
- p. 3: image only ['poecs', 'reti']; layer only ['12b', 'party', 'pay', 'retirement', 'sick', 'statutory']
- p. 4: image only ['corm']; layer only ['12b', 'party', 'pay', 'retirement', 'sick', 'statutory', 'third']
- p. 6: image only []; layer only ['12b', 'department', 'party', 'pay', 'retirement', 'sick', 'statutory', 'third', 'treasury']
- p. 7: image only ['eon']; layer only []
- p. 8: image only ['poecs', 'reti']; layer only ['12b', 'party', 'pay', 'retirement', 'sick', 'statutory']
- p. 10: image only ['poecs']; layer only ['12a', '12b', '12d']

## i1040gi

- p. 1: image only ['fri', 'zaav']; layer only []
- p. 2: image only ['irs']; layer only ['new', 'owe', "what's"]
- p. 4: image only ['jmprovelrs', 'jrs']; layer only ['improveirs']
- p. 6: image only ['jrs']; layer only []
- p. 8: image only ['jax', 'ong', 'zax']; layer only ['caution']
- p. 9: image only ['cng', 'didn', 'don', 'isn', 'jrs', 'vel']; layer only ['caution', "didn't", "don't", "isn't"]
- p. 12: image only []; layer only ['tip']
- p. 13: image only ['jrs']; layer only []
- p. 14: image only ['ntt', 'uss', 'zest']; layer only ['caution']
- p. 15: image only []; layer only ['tip']
- p. 16: image only ['cnt']; layer only ['caution']
- p. 17: image only ['geeeeb']; layer only ['tip']
- p. 18: image only ['gsez3', 'gsezed', 'uss']; layer only ['stop']
- p. 19: image only ['ding', 'geeed', 'geszd', 'inclu']; layer only ['stop']
- p. 20: image only ['gro']; layer only ['stop']
- p. 21: image only []; layer only ['iii']
- p. 23: image only ['gmt']; layer only ['caution']
- p. 24: image only ['mee', 'zax']; layer only ['caution']
- p. 25: image only ['zax']; layer only ['caution', 'tip']
- p. 27: image only ['cnty', 'ocd']; layer only ['caution', 'iii', 'tip']
- p. 28: image only ['omt']; layer only ['caution', 'tip']
- p. 29: image only ['anamountonline5b', 'gotoline6', 'gror', 'numberonline3', 'ofline5orline7', 'subtractline6fromline2']; layer only ['stop']
- p. 30: image only ['mtt']; layer only ['caution', 'tip']
- p. 31: image only []; layer only ['tip']
- p. 32: image only ['cent', 'cette', 'eas', 'eect', 'een', 'eens', 'ence', 'ene', 'eneees', 'enees', 'ete', 'etn', 'ror', 'saps', 'spp'] …; layer only ['stop', 'tip']
- p. 33: image only ['uss']; layer only []
- p. 34: image only ['ntt']; layer only ['caution']
- p. 35: image only ['cnet', 'eet', 'isn', 'sinel', 'tenes']; layer only ["can't", "isn't"]
- p. 37: image only ['cence', 'cette', 'cnet', 'eeaes', 'eect', 'eens', 'eet', 'ence', 'enn', 'ete', 'neeeeeee', 'teen']; layer only ['caution']
- p. 38: image only ['addlinessand9', 'ato', 'cence', 'cette', 'eect', 'eens', 'eet', 'ence', 'ene', 'enn', 'ent', 'nett', 'nnn', 'teens', 'tence'] …; layer only []
- p. 39: image only ['cnet', 'cti', 'mtt', 'won']; layer only ['caution']
- p. 40: image only ['ged', 'gse', 'jater', 'mei', 'won']; layer only ['caution', 'stop', 'tip']
- p. 41: image only ['can', 'ged', 'gsezb', 'jater']; layer only ['caution', "didn't", 'stop', 'tip']
- p. 42: image only ['fromlinel']; layer only ['caution', 'stop', 'tip']
- p. 43: image only ['gsd']; layer only []
- p. 44: image only []; layer only ['iii', 'tip']
- p. 46: image only ['memiee', 'woe']; layer only ['10o4r0', 'caution', 'stop']
- p. 47: image only ['12b']; layer only ['stop']
- p. 48: image only ['4ni0', 'ernee', 'ory', 'pein', 'pvt', 'so62']; layer only ['10o4r0', 'answered', 'caution', 'stop']
- p. 50: image only ['fe2']; layer only ['least']
- p. 51: image only []; layer only ['but', 'least', 'less']
- p. 52: image only ['fe2']; layer only []
- p. 54: image only ['fe2']; layer only ['least']
- p. 55: image only []; layer only ['but', 'least', 'less']
- p. 56: image only ['fe2']; layer only ['least']
- p. 58: image only ['fe2']; layer only []
- p. 59: image only ['aii']; layer only []
- p. 60: image only ['fe2']; layer only []
- p. 61: image only ['can', 'cei', 'mot', 'won']; layer only ["can't", 'caution']
- p. 62: image only ['cmg', 'cnty', 'jrs']; layer only ['caution', 'jointly']
- p. 63: image only ['mtt', 'sby']; layer only ['tip']
- p. 64: image only ['jrs', 'zax']; layer only ['1040tm']
- p. 65: image only []; layer only ['iii']
- p. 66: image only ['jrs', 'omt']; layer only ['caution', 'tip']
- p. 68: image only ['att', 'axabie', 'eno', 'ies', 'tos']; layer only []
- p. 81: image only ['jrs']; layer only []
- p. 82: image only ['fic', 'jrs', 'ldentitvtheft']; layer only []
- p. 83: image only ['jrs', 'urs', 'uss', 'zax']; layer only []
- p. 84: image only ['jrs']; layer only ['caution']
- p. 85: image only ['gmt', 'jrs', 'net']; layer only ['caution']
- p. 86: image only ['jrs']; layer only []
- p. 87: image only ['jrs']; layer only []
- p. 89: image only ['cnty', 'nee']; layer only ['caution', 'tip']
- p. 90: image only ['een', 'eene', 'eet', 'ete', 'ink', 'nee']; layer only ['stop']
- p. 91: image only ['82z', 'cng', 'mee']; layer only ['caution']
- p. 92: image only ['jrs', 'ney']; layer only ['caution', 'irs']
- p. 93: image only ['ney', 'otp', 'zax']; layer only ['caution']
- p. 94: image only ['doesn', 'farned', 'tencc']; layer only ['caution', "doesn't", 'officer']
- p. 95: image only ['zax']; layer only ['tip']
- p. 96: image only []; layer only ['tip']
- p. 97: image only ['ete', 'teen', 'wine9']; layer only ['stop']
- p. 98: image only ['lla', 'llb', 's90']; layer only ['caution']
- p. 99: image only ['cence', 'coa', 'eens', 'eet', 'ete', 'etn', 'nee', 'nen', 'tenn', 'tnt']; layer only ['etc']
- p. 101: image only ['jater', 'mee', 'ney', 'sms']; layer only ['caution']
- p. 103: image only ['jrs']; layer only ['irs']
- p. 104: image only ['nib']; layer only []
- p. 106: image only ['moo', 'omt', 'vet']; layer only ['caution', 'iii']
- p. 108: image only ['nib']; layer only []
- p. 110: image only ['moti', 'vli']; layer only ['caution']
- p. 112: image only ['jrs', 'mtt']; layer only ['caution', 'eci']
- p. 114: image only ['cng']; layer only ['17l', '17o', 'caution']
- p. 115: image only ['c11', 'jrs', 'tules', 'zax']; layer only ['irs', 'rules']
- p. 116: image only ['ill', 'zax']; layer only ['17z', 'caution']
- p. 118: image only []; layer only ["child's"]
- p. 122: image only ['lebt', 'meat']; layer only ['debt', 'estate']
- p. 126: image only []; layer only ['caution', 'tip']

## i1040s8812

- p. 1: image only ['yan', 'zo025']; layer only []
- p. 2: image only []; layer only ['tip']
- p. 3: image only []; layer only ['tip']
- p. 4: image only ['teens']; layer only ['total']
- p. 5: image only []; layer only ['add']
- p. 8: image only ['cence', 'coddeq', 'eeeenes', 'eens', 'eet', 'ence', 'ene', 'eneeas', 'linn', 'nee', 'teen', 'tenes', 'tenet', 'tent']; layer only []
- p. 9: image only ['dod', 'od00000000000000000000000000', 'sulsweerlme', 'tom']; layer only ['subtract']

## i1040sb

- p. 1: image only ['sami']; layer only ['caution', 'tip']
- p. 2: image only ['ill', 'old']; layer only ['iii', 'tip']
- p. 3: image only []; layer only ['caution', 'irs']

## i1040sca

- p. 1: image only ['omens', 'yan', 'zo025']; layer only ['caution']
- p. 2: image only ['rip']; layer only []
- p. 3: image only []; layer only ['tip']
- p. 4: image only ['jrs', 'lee']; layer only ['caution', 'that', 'tip']
- p. 6: image only []; layer only ['caution']
- p. 7: image only ['subtractline5fromline4']; layer only ['stop', 'tip']
- p. 8: image only []; layer only ['caution', 'tip']
- p. 9: image only ['mun']; layer only ['irs', 'tip']
- p. 10: image only []; layer only ['tip']
- p. 11: image only ['moray']; layer only []
- p. 13: image only []; layer only ['more']
- p. 14: image only ['lowa']; layer only ['iowa', 'more']
- p. 15: image only ['s51']; layer only ['more']
- p. 16: image only []; layer only ['more']
- p. 17: image only ['aco', 'e1o0000', 'lied', 'ology', 'sas', 'si0', 'sot', 'tog', 'tos']; layer only ['applied', 'more']
- p. 18: image only ['louisi']; layer only ['more', 'niagara']

## i1040sd

- p. 1: image only ['snl', 'zo025']; layer only ['24331i', 'tip']
- p. 2: image only ['jest']; layer only ['tip']
- p. 3: image only ['ill', 'jest']; layer only ['iii']
- p. 7: image only []; layer only ['least', 'tip']
- p. 9: image only []; layer only ['caution']
- p. 10: image only ['tees']; layer only []
- p. 12: image only ['siep']; layer only []
- p. 13: image only ['cooand', 'etree', 'frwdnd', 'sche', 'tenes', 'ule']; layer only []
- p. 14: image only []; layer only ['tip']
- p. 15: image only ['14orline16', '18orline20', 'addlines6gand9', 'ato', 'cette', 'marriedfilingjointlyor', 'tee', 'teen', 'teens']; layer only []
- p. 16: image only ['cette', 'eae', 'eens', 'eet', 'nett', 'teen', 'teens', 'tenet', 'tent', 'tte']; layer only []

## i1099div

- p. 1: image only []; layer only ['caution', 'tip']
- p. 2: image only []; layer only ['tip']
- p. 4: image only ['wry']; layer only ['tip']
- p. 5: image only []; layer only ['caution']

## i1099int

- p. 1: image only ['old']; layer only []
- p. 2: image only []; layer only ['tip']
- p. 3: image only []; layer only ['irs']
- p. 4: image only []; layer only ['caution']
- p. 5: image only ['mme']; layer only []
- p. 6: image only []; layer only ['tip']
- p. 7: image only ['old']; layer only ['caution']

## i1116

- p. 1: image only ['yam', 'zo025']; layer only []
- p. 3: image only ['fart', 'jrs']; layer only ['irs']
- p. 7: image only ['eens', 'ene', 'ill', 'nee', 'teen']; layer only ['iii']
- p. 8: image only []; layer only ['iii']
- p. 9: image only ['ill']; layer only ['iii']
- p. 12: image only ['4byline6', 'cette', 'teens']; layer only ['income']
- p. 15: image only ['eect', 'eens', 'eet', 'ene', 'hore', 'tenes']; layer only ['income']
- p. 16: image only ['50rline6', 'addlines12and13', 'amoune', 'een', 'eens', 'eet', 'ene', 'ent', 'ete', 'ett', 'nce', 'neeaes', 'nes', 'netted', 'teen'] …; layer only []
- p. 17: image only ['iil']; layer only ['iii']
- p. 18: image only ['cex', 'eens', 'inc', 'tenet']; layer only []
- p. 23: image only ['eens', 'ett', 'tee', 'teenies', 'teens', 'teetetee']; layer only ['add']
- p. 25: image only []; layer only ['13z', 'iii']

## i8283

- p. 1: image only ['sami']; layer only []
- p. 7: image only []; layer only ['irs']
- p. 10: image only []; layer only ['iii']
- p. 12: image only ['lawortheform']; layer only ['iii']

## i8949

- p. 1: image only ['yan', 'zo025']; layer only []
- p. 3: image only ['irbenot']; layer only []
- p. 11: image only ['costorotherbasis']; layer only ['less']
- p. 12: image only ['65000o50000500000500000000000000000550000000500005', 'iomims', 'oaak0kdgookkkgoook', 'popiitesseweig', 'suiswecilina']; layer only ['add', 'subtract']

## i8959

- p. 1: image only ['sami']; layer only []
- p. 3: image only []; layer only ['iii']
- p. 4: image only ['iil', 'ill']; layer only ['iii']

## i8960

- p. 1: image only ['nil', 'sami']; layer only []
- p. 3: image only ['nil']; layer only ['tip']
- p. 4: image only ['nil']; layer only []
- p. 5: image only ['nil']; layer only []
- p. 6: image only ['nil']; layer only []
- p. 7: image only ['nil']; layer only []
- p. 8: image only ['ill', 'moray', 'nil']; layer only ['caution', 'iii', 'tip']
- p. 9: image only ['nil']; layer only []
- p. 10: image only ['amans', 'amas', 'cap', 'gotoline2', 'ital', 'mumber', 'nil', 'resse']; layer only ['passive']
- p. 11: image only ['gad', 'ing', 'nil', 'peletred', 'seyi']; layer only ['combine', 'deferred', 'tip']
- p. 12: image only ['nil']; layer only []
- p. 13: image only ['5b5', 'nil']; layer only ['tip']
- p. 14: image only ['nil']; layer only []
- p. 15: image only ['eens', 'eneeaee', 'ent', 'gorline', 'nde', 'nett', 'nil', 'teen', 'teens', 'tenet']; layer only ['less', 'tip']
- p. 17: image only ['nil']; layer only []
- p. 18: image only ['teen']; layer only ['caution', 'tip']
- p. 19: image only ['ill']; layer only ['all', 'iii', 'items']
- p. 20: image only ['eens', 'ene', 'innccomee', 'nee', 'teens']; layer only ['expense', 'expenses', 'gambling', 'interest', 'medical', 'tip']
- p. 21: image only ['ill']; layer only []
- p. 22: image only []; layer only ['tip']
- p. 23: image only ['eens', 'nil']; layer only ['tip']
- p. 24: image only ['lawortheform']; layer only ['irs', 'tip']

## i8995

- p. 1: image only ['yan', 'zo025']; layer only []
- p. 2: image only ['ecl']; layer only ['eci']
- p. 6: image only ['noy']; layer only []
- p. 7: image only ['noy']; layer only []
- p. 8: image only ['tjaand']; layer only []
- p. 10: image only ['ainin', 'ena', 'giiii', 'givi', 'kiiii', 'rem']; layer only ['part']

## i8995a

- p. 1: image only ['fanlrs']; layer only []
- p. 3: image only ['ltems']; layer only ['irs']
- p. 5: image only ['ill']; layer only ['iii']
- p. 8: image only ['ney', 'noy']; layer only []
- p. 9: image only ['noy', 'qbl']; layer only []
- p. 10: image only ['giii']; layer only []
- p. 11: image only ['anmoag', 'giiii', 'ill', 'kiiii', 'yfano']; layer only []

## iw2w3

- p. 1: image only ['sami']; layer only []
- p. 5: image only ['mens']; layer only ['caution']
- p. 6: image only ['moray', 'mura']; layer only ['caution', 'tip']
- p. 7: image only ['mens']; layer only ['caution']
- p. 8: image only ['jrs', 'rata']; layer only []
- p. 10: image only []; layer only ['caution']
- p. 11: image only []; layer only ['caution']
- p. 13: image only ['mui']; layer only ['caution']
- p. 14: image only ['jrs']; layer only ['caution']
- p. 15: image only ['mys']; layer only ['caution']
- p. 19: image only []; layer only ['caution']
- p. 20: image only []; layer only ['12d', 'tip']
- p. 21: image only ['cosi', 'ierm']; layer only ['tip']
- p. 22: image only ['jrs', 'qgehra']; layer only ['irs']
- p. 27: image only ['s3c']; layer only []
- p. 28: image only ['mors']; layer only []
- p. 29: image only ['2v1', '83c', '8ss']; layer only ['2vi']
- p. 30: image only ['moray']; layer only ['caution', 'irs']
- p. 34: image only []; layer only ['itin']
- p. 35: image only ['www']; layer only []

## p505-2026

- p. 1: image only ['1x2', 'espanol', 'infor', 'mation', 'pycckui']; layer only ['espa']
- p. 4: image only []; layer only ['caution']
- p. 5: image only []; layer only ['tip']
- p. 6: image only ['wee']; layer only ['caution']
- p. 7: image only ['jrs']; layer only []
- p. 8: image only []; layer only ['caution']
- p. 10: image only []; layer only ['ira']
- p. 11: image only ['a4r', 'fa2026']; layer only ['caution']
- p. 14: image only ['fpf', 'ona', 'tenes', 'won']; layer only ['larger', 'limit']
- p. 15: image only ['addlines4and5', 'teens', 'tees', 'tenes', 'totalonline9', 'toured']; layer only []
- p. 17: image only ['morene']; layer only []
- p. 18: image only ['wee']; layer only ['caution']
- p. 19: image only ['cette', 'ene', 'ent', 'ete', 'eyyi', 'hppa', 'opin', 'tee', 'tees', 'tte']; layer only []
- p. 20: image only ['jota']; layer only ['tip']
- p. 21: image only []; layer only ['caution', 'tip']
- p. 22: image only []; layer only ['caution']
- p. 23: image only ['wry']; layer only ['caution']
- p. 24: image only []; layer only ['caution']
- p. 26: image only ['eens']; layer only []
- p. 27: image only []; layer only ['17l', '17o', 'caution', 'tip']
- p. 29: image only []; layer only ['1040tm', 'taxtm']
- p. 31: image only []; layer only ['caution']
- p. 32: image only ['2dfromline1', 'ene', 'ent', 'fine', 'lino', 'nee', 'ofline12aor12b', 'pin', 'tenes']; layer only []
- p. 33: image only ['eens', 'eet', 'ett', 'lene', 'lente', 'ornsneet', 'teen', 'teens', 'tees', 'tenes', 'very', 'yoo']; layer only ['rico', 'year']
- p. 34: image only ['3orline7', 'eae', 'eevee', 'ete', 'eteeteeveeeeeey', 'veeeeteetevieeeeeey']; layer only []
- p. 35: image only ['gotoline3', 'nena', 'tenet']; layer only []
- p. 36: image only ['5fromline3', 'addlines1and2', 'cette', 'eteeteeeaes', 'tent']; layer only ['add', 'subtract']
- p. 37: image only ['1ines5', 'een', 'ene', 'ete', 'nent', 'tee', 'teens', 'ttt']; layer only []
- p. 38: image only ['0r13c', '3orline6', '3orline7', '8fromline4', 'addlines4and', 'addliness5and6', 'ato', 'bbe', 'bebe', 'bet', 'bette', 'cena', 'eect', 'eeeteenes', 'een'] …; layer only ['13b', '13c']
- p. 39: image only ['eens', 'ketene', 'tee']; layer only []
- p. 40: image only ['15fromline14', '4byline5', 'andskiptoline7', 'ofline6orline7']; layer only ['skip', 'that']
- p. 42: image only ['18aor18c', '1orlineq', '3orline7', '8fromline4', 'addlines14and15', 'addlinessand6', 'ato', 'cette', 'cote', 'eect', 'eens', 'ene', 'ete', 'gotoline37', 'ofline3orline6'] …; layer only ['13b', '13c', 'loss', 'net', 'rate']
- p. 43: image only ['ena', 'enue', 'lfline', 'teeta']; layer only []
- p. 44: image only ['eons', 'mp9']; layer only ['caution', 'mp3']
- p. 45: image only ['jrs']; layer only []

## p526

- p. 1: image only ['espariol', 'pycckui']; layer only ['chinese', 'espa', 'korean', 'russian', 'spanish', 'vietnamese']
- p. 4: image only ['lsrael']; layer only []
- p. 9: image only []; layer only ['irs']
- p. 21: image only ['4fromline1', 'addlines4and7', 'amountonline1', 'line2by2', 'subtractline9fromline1']; layer only ['add']
- p. 27: image only ['0r29', '13fromline10', 'addlines9and10', 'addlinessand7', 'eens', 'liin', 'ling', 'tenes']; layer only ['add']
- p. 28: image only ['addlines4and6', 'eeeeenee', 'eens', 'eet', 'ene', 'ete', 'ett', 'nett', 'teen', 'teeta', 'ttt']; layer only []
- p. 33: image only ['ltems']; layer only []
- p. 34: image only []; layer only ['irs']
- p. 35: image only []; layer only ['caution']
- p. 36: image only ['jrs', 'mp9']; layer only ['mp3']
- p. 37: image only []; layer only ['caution']
- p. 39: image only ['iss']; layer only []

## p550

- p. 1: image only ['eae', 'eens', 'espafol', 'fnl', 'pycckui']; layer only ['espa', 'loss']
- p. 3: image only ['ooocodo']; layer only []
- p. 17: image only ['lke']; layer only []
- p. 19: image only ['olld']; layer only []
- p. 21: image only []; layer only ['irs']
- p. 26: image only ['1o99', '1o9o']; layer only []
- p. 35: image only []; layer only ['irs']
- p. 41: image only ['jrs']; layer only []
- p. 54: image only []; layer only ['irs']
- p. 68: image only ['luo']; layer only ['ljo']
- p. 69: image only []; layer only ['irs']
- p. 72: image only []; layer only ['irs']
- p. 76: image only ['insiru']; layer only ['instru']
- p. 81: image only ['jrs']; layer only []
- p. 92: image only []; layer only ['iii']
- p. 97: image only []; layer only ['used']
- p. 100: image only ['hlj']; layer only ['hij']
- p. 101: image only []; layer only ['iii']
- p. 102: image only ['addlines4and6', 'cic', 'ete', 'nnn', 'tees', 'teeta', 'ten', 'tenes']; layer only ['add']
- p. 105: image only ['irbhrev']; layer only []
- p. 106: image only []; layer only ['caution']
- p. 107: image only ['jrs', 'mp9']; layer only ['mp3']
- p. 108: image only ['muy']; layer only ['caution']
- p. 113: image only []; layer only ['limit']
- p. 114: image only []; layer only ['int', 'misc']

## p561

- p. 1: image only ['espanol', 'pycckni']; layer only ['espa']
- p. 8: image only []; layer only ['irs']
- p. 13: image only ['eons', 'fam', 'mp9']; layer only ['caution', 'mp3']
- p. 14: image only ['wns']; layer only []
- p. 16: image only ['onal', 'reicoe']; layer only []

## rp-2024-40

- p. 1: image only ['cccccccccccececeeeeeeeenaeeeeeeeeeeeesecenceeaeeeeeeeeeseseeencaeeeeeeeeeeeeseeneaes', 'cccccccecccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeereeeeeretereeeeeeeeetes', 'cccccceesccceceeeeeeeeeeeceeaeeeceeeeesesecensaeeeeeeeeeseeseeeeaes', 'cccccecccccceceeececeeneeeeeeeeeeeeeceeceaeeeeeeeeesececeeceeeeeeeeeeseseseneenieeeeeeeeees', 'ccccceccceeccecececeeeeeeeceeneaeeeeeeeeesececneaeaeeeeeeeseseececeeaeeeeeeeeeseesesesaneees']; layer only []
- p. 2: image only ['accoums', 'cccccccccccceceeeeeeeeceeceeeeeeesececeeeeaeeeeeeeeesesesencaeaeeeeeeeeeseeseeenserseeseeeees', 'cccccccccecececeeeeeceeeeeeeeeeeeeeeeeeaeaeaeaeaeaeaeaeaeaeananas', 'ccccccccceceeceeceeeeeeeeeeeceneaeeaeeeeeeeeesececeeaeaeeeeeeesesesseseeneeeeeeeeees', 'ccccccccececeeeeeeeeceeeeeeesessesneeseeeeeeeeeeeeeees', 'cccccccceeeeeeeeeenececeeeeeseeeeennneeeeeeteeeeees', 'ccccccceceeececeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesaeaeseaeaeaeanaeaeanas', 'ccccccceceeeeeeeeneeceeeeeeeeeseeesssneeeeees', 'cccccceeceeeeeeeeeeeeeeeeeeeeeeeeeeaeaeanaeananes', 'cccccceeeeceeeeeeeeeeeeeeeeeeeeaeaeaeaeaeaeaeaeaeaeaeaeanaeaeaeaees', 'cccccceeeeeeeeeeeeceeeeeeeeeeseeeeeesnenneees', 'ccccceccceeceeceeeeeeeeeeeeceeeeeeeeeeeeeeseseeencaeseeeeeeeeeeees', 'cccccecceceeeeeeececeeeeeeeeeeenaeeeeeeeeeeeeees', 'ccccceceeeeeeeeeceececeeeeesesesseneeeeeeeess', 'ccccceceeeeeeeeeneeeeeeeeeeeeeecenaeaeeeeeeeeeeeeeesensaneeeeeeeess'] …; layer only ['accounts', 'kiddie']
- p. 3: image only ['0ccccccccccccccceeeccceeeeecceeeceeeceeeueeeeeeeeeeeeeeeeeaneess', 'ccccccccccceceeeceeeeeeecececaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaesaeanaeananes', 'cccccccccceececececeeeeeeeeeeeeeeeeeeeeaeeeanaeees', 'cccccccccecceecececeeeeeeeeeeeeeeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaaaanas', 'cccccccccececeeeeeeeeeeeeeeeeeeeeaeaeaeaeaeaeaeaeananaeaes', 'ccccccccecccecececeeeeeeeeeeeeeeeeeeeeaeaeaeceaeaeaeseaeaeaeaeaeaeaeaeaeaeeananas', 'cccccccecececeeeeeeeeeeeeeeaeeeaeaeaeaeaeaeaeaeaeaeaeaeees', 'cccccccececeeceeeeneeceeeeeeeeeececeeeaeeeeeeeeeeesecsccaeaeeeeeeeeseeseseseneeees', 'ccccccceeeeeeeeeeneceeeeeeeeeeseeennneeeeeeeeeeeseseesaes', 'ccccccceesecceceeeeeeeeeeeeeeeeaeeeeeeeseseeseeenneees', 'ccccccceeseeeeceeceeeeeeeseseeeenceeeeeeeeeeeeseseeees', 'cccccceeeeeeeeeeneececeeeeeeeeseceecaeaeeeeeeesesessesenaeeeees', 'ccccceeeceeeeceececeeeeeeeeeeeneaaeeeeeeeeeeesesensnnaeeeeeeeeess', 'ecccceceeeeeeeeeeneeeeeeeeeeeeesesseees', 'eceeeeeeceeeeeeeeteees'] …; layer only []
- p. 23: image only []; layer only ['30th']
- p. 25: image only ['go50h', 'go50k', 'rrect']; layer only ['30th', '6050h']

## Adjudication (2026-10-17)

Read against the page images by the session that built the audit; no human reading is claimed.

**Image-only words** (what the image reading has and the text layer lacks): 229 word-like
tokens over the 37 documents, 172 distinct. By kind, from the ranked list:

- Dotted leaders on worksheet and form lines read as letters: `teens`, `tenes`, `cette`,
  `tenet`, `cence`, `eens` and the like, concentrated on worksheet pages. Checked on
  i1040gi p. 38 (the Qualified Dividends and Capital Gain Tax Worksheet): every
  image-only token on that page sits on a leader; the page's words are all in the layer.
- Two to four words set tightly on a form line read as one: `reservedforfutureuse`,
  `lawortheform`, `carryoverfromprioryear`, `addlinestathroughiy`.
- Misreads of small type on the forms: `eulktime` (Full-time), `mawied` (Married),
  `suniven` (surviving), `ltems` (Items), `jater` (later), `giiii` (G(iii)).
- Non-Latin cover text the tokenizer skips in the layer and Tesseract latinises:
  `pycckui` (Русский), `espanol` (Español).
- `moray` on i1040sca p. 11: checked against the page; no such word is printed, and the
  layer has every word the page shows (the nearest printed text is the link "or more").

**Layer-only words** (what the text layer has and the image reading lacks): 362
tokens, 101 distinct, led by the margin icon labels `caution` (77) and `tip` (56) set
in a small face, `iii` in Part headings, `stop`, and the W-2 and Form 1040 box labels in
small type (`statutory`, `retirement`, `sick`, `party`). The pages with most such words
are form pages, not instruction pages, and none shows a run of words with no printed
counterpart, which is what hidden or duplicated text in the layer would look like.

**Conclusion, with its limits.** At the word level, above the OCR noise floor, the audit
found no text drawn as graphics that the text layer lacks and no text in the layer
that the page does not show. It cannot see a loss that Tesseract also misses, and it
compares words, not their order or their line. It is a one-time reading of the 2025
archive; a refetch reruns it.
