# Onda 1 (tradutores; revisão depois via SendMessage)
Mat_1-7 ad8256ea86a87e1d9
Mat_8-12 a0d5faa6ef2519ed4
Mrk_1-5 ae14e4f1a4bb9314b
Luk_1-4 ab5f3c1211ca922af
Jhn_1-5 ac8a6a877a92e26cc
Act_1-6 ab0a4861d8e23ec44
Rom_1-8 a3e2dac545b24d093
1Co_1-9 ac3b948a52d1cce95
Gal+Eph a0ae4d448142a54ae
Heb_1-7 aee5dd41ebc46a844
# Glossário (sonnet)
lote1 ac2a84e0d5f1aad83 / lote2 adfaad1325a6044a5 / lote3 ab5c2e313c35e5d12 / lote4 ac9fd98e9992d285b
# Fila (onda 2+): Mat 13-18, 19-23, 24-28; Mrk 6-9, 10-13, 14-16; Luk 5-8, 9-12, 13-18, 19-22, 23-24; Jhn 6-9, 10-14, 15-21; Act 7-11, 12-17, 18-23, 24-28; Rom 9-16; 1Co 10-16; 2Co 1-13; Col+Phm+1Th+2Th; 1Ti+2Ti+Tit; Heb 8-13; Jas+1Pe; 2Pe+1Jn+2Jn+3Jn+Jud; Rev 1-11, 12-22
# Prompts: /tmp/claude-0/prompt_tradutor.txt, prompt_glosas.txt
# Concluídos (tradutor → revisor): Mat_1-7 ad8256ea86a87e1d9 → a8170e4b7e87c6fe7; Mat_8-12 a0d5faa6ef2519ed4 → a60b0240c48547307; Mrk_1-5 ae14e4f1a4bb9314b → a9c7ff7892858bf72; Luk_1-4 ab5f3c1211ca922af → aa93fcf92f769ed95; Jhn_1-5 ac8a6a877a92e26cc → a5323df920bf75c51; Heb_1-7 aee5dd41ebc46a844 → a3af474dbb2066a24; Gal a0ae4d448142a54ae → a7d526eab07b7162d; Act_1-6 ab0a4861d8e23ec44 → a598999af6ae401d9
# Onda 2: Mat_13-18 abb906e052e625759; Mrk_6-9 a7a79441c22b73518; Luk_5-8 a5ced19e7ae170821; Jhn_6-9 a05d1bc694eadddd9; Act_7-11 a86fb096a48686906; Heb_8-13 a02b2640dc2dc97dc
# Fila restante: Mat 19-23, 24-28; Mrk 10-13, 14-16; Luk 9-12, 13-18, 19-22, 23-24; Jhn 10-14, 15-21; Act 12-17, 18-23, 24-28; Rom 9-16; 1Co 10-16; 2Co; Col+Phm+1Th+2Th; 1Ti+2Ti+Tit; Jas+1Pe; 2Pe+1Jn+2Jn+3Jn+Jud; Rev 1-11, 12-22
# Fluxo: revisor grava revisao/partes/<parte>.json → SendMessage ao tradutor para decidir item a item (campo "decisao" em cada item) e regravar
# Rev Rom_1-8: ver próximo spawn
Rev Rom_1-8 ae37456e92a8e5b27; Finais (rev aplicada): Mat_1-7, Mat_8-12, Mrk_1-5, Gal. Eph pronto sem revisão.
Rev Eph a2a538c3a7366042e (tradutor a0ae4d448142a54ae). Final: Luk_1-4.
Rev 1Co_1-9 a565c70a8951ff128 (tradutor ac3b948a52d1cce95). Final: Jhn_1-5.
