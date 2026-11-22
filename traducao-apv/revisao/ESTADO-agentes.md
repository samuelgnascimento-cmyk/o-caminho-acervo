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
Onda 2: Mat_13-18 traduzido (223/223, 457 notas) → rev ac5a73ec7711933f4. Nota: TAGNT sem 'οὐ μὴ τιμήσει τὸν πατέρα αὐτοῦ' em Mt 15:6 (está no SBLGNT); tradutor incluiu.
Onda 2: Mrk_6-9 traduzido (181, 313 notas) → rev aff11f41800a0b6a9. Luk_5-8 traduzido (194, 353 notas) → rev (ver spawn).
Onda 2: Jhn_6-9 traduzido (224 incl. 7:53, 244 notas) → rev (ver spawn). Scripts: regras.EXTRAS={'Jhn.7.53'} usado por validar/juntar/montar.
# PAUSA 2026-11-15 15:15 UTC (Samuel: 'Pausa'). Todos parados. Para retomar: SendMessage a cada id. Act_7-11 a86fb096a48686906 (tradução interrompida); revisores interrompidos, respawnar: Mat_13-18, Mrk_6-9, Luk_5-8, Jhn_6-9. Tradutores prontos esperando revisão: Mat abb906e052e625759, Mrk a7a79441c22b73518, Luk a5ced19e7ae170821, Jhn a05d1bc694eadddd9. Commit/push bloqueado pelo classificador: pedir autorização ao Samuel.
# RETOMADA 2026-11-16 02:02 UTC. Revisores: Mat_13-18 a6a60b2c59f957e38; Mrk_6-9 a2e38d826581a9228; Luk_5-8 a835a9079ce1207d5; Jhn_6-9 a557168c79c97178e. Act_7-11 a86fb096a48686906 retomado. Commit ainda bloqueado.
Revisões prontas: Mrk_6-9 (22) → decisão a7a79441c22b73518; Mat_13-18 (13) → decisão abb906e052e625759; Luk_5-8 (17) → decisão a5ced19e7ae170821. Act_7-11 traduzido (221, 368 notas) → rev ab677d7e7a3fae5d9. SBLGNT oficial: /tmp/claude-0/data/sblgnt/data/sblgnt/text/<Book>.txt
Rev Jhn_6-9 (15) → decisão a05d1bc694eadddd9.
Final: Mrk_6-9 (15 aceitos, 7 em parte). Onda 3: Mrk_10-13 a0c628ff3513e869d.
Final: Jhn_6-9 (10/4/1). Onda 3: Jhn_10-14 a0d34f4a44f609461.
Final: Mat_13-18 (9/4/0).
Final: Luk_5-8 (14/3/0). PENDENTE harmonizar Mt 8:9 (servo) com Lc 7:8 (escravo). Onda 3: Mat_19-23 a7a762d622bb91915; Luk_9-12 (ver spawn).
Rev Act_7-11 (18) → decisão a86fb096a48686906. Regra GUIA: não citar 'a folha' nas notas (Jhn_6-9 corrigido à mão).
Final: Act_7-11 (14/2/2). Tirei de At 9:2 a frase sobre o app (a tradução fica independente).
Onda 3: Act_12-17 aa23a80f8a26078ca.
Mrk_10-13 traduzido (166, 335 notas) → rev (ver spawn).
# HARMONIZAR (passada final por livro): δοῦλος Mt 8:9 (servo) x Lc 7:2-10 (escravo); Mc 9:35 nota x Mc 10:44 "escravo de todos"; ἐγώ εἰμι "Sou eu" em Mc 6:50, 13:6, 14:62, Jo 6:20 (guia diz "Eu Sou" em uso absoluto) → decidir regra no GUIA.
Jhn_10-14 traduzido (218, 320 notas) → rev ab49974493a8ba2bf. GUIA: decisões da onda 2 (parákletos=Advogado provisório; κύριε; sem app/folha).
Rev Mrk_10-13 (16) → decisão a0c628ff3513e869d. Atenção: TAGNT pode errar a leitura do NA28 (Mc 10:28, 11:32) — conferir aparato SBLGNT.
Mat_19-23 traduzido (195, 419 notas) → rev (ver spawn).
Luk_9-12 traduzido (217, 334 notas) → rev (ver spawn).
Final: Mrk_10-13 (10/4/2; 12:2 e 13:34 aguardam harmonização δοῦλος). Onda 3: Mrk_14-16 (ver spawn).
# PAUSA 3: 2026-11-16 12:09 UTC (Samuel, via coordenador: "Pause a tradução ate que termine as demandas novas"). Todos parados.
Ao retomar: respawnar revisores de Mat_19-23, Luk_9-12, Jhn_10-14 (interrompidos; tradutores com contexto: Mat a7a762d622bb91915, Luk a6644c01d701d285a, Jhn a0d34f4a44f609461). Retomar tradutores: Act_12-17 aa23a80f8a26078ca, Mrk_14-16 a1bbce93fda8de14d (mal começou).
# RETOMADA 2026-11-17 02:09 UTC (Samuel: 'Continue'). Revisores: Mat_19-23 ac14c80ff81c0d90b; Luk_9-12 a28405903d3df9b9d; Jhn_10-14 a2a089a466a3058c1. Tradutores retomados: Act_12-17 aa23a80f8a26078ca; Mrk_14-16 a1bbce93fda8de14d. Commit/push autorizado pelo Samuel (2026-11-16).
Rev Luk_9-12 (17) → decisão a6644c01d701d285a. Act_12-17 traduzido (220, 362 notas) → rev aa367d1a3e00bbe98.
Rev Mat_19-23 (18; 19:29 γυναῖκα perdida no TAGNT) → decisão a7a762d622bb91915.
Rev Jhn_10-14 (23) → decisão a0d34f4a44f609461.
Final: Luk_9-12 (15/2/0).
Onda 4: Luk_13-18 a2fcafa0131f973e5.
Final: Mat_19-23 (16/1/1).
Onda 4: Mat_24-28 a961b6a980bae0260.
Final: Jhn_10-14 (22/1/0). Onda 4: Jhn_15-21 (ver spawn).
Mrk_14-16 traduzido (139, 290 notas) → rev (ver spawn). HARMONIZAR: ναός='santuário' x ἱερόν='templo' (Mc 14:58; 15:29,38) — conferir partes anteriores.
Rev Act_12-17 (30) → decisão aa23a80f8a26078ca. GUIA: regra NA28 TAGNT x aparato.
# PASSADA FINAL (antes de montar cada livro): conferir notas tc que citam NA28 contra o aparato SBLGNT nas partes antigas (At 1-11 sobretudo); harmonizar δοῦλος, ἐγώ εἰμι, ναός.
Rev Mrk_14-16 (13) → decisão a1bbce93fda8de14d.
Final: Act_12-17 (27/3/0).
Onda 4: Act_18-23 a65d73a74f7f22479.
Final: Mrk_14-16 (11/2/0). MARCOS COMPLETO: juntado+montado, na página (versão 4). Onda 4: Rom_9-16 a92e23dfe9590a855.
Luk_13-18 traduzido (213, 305 notas) → rev a7987d10a388dd673. Template revisor: /tmp/claude-0/prompt_revisor2.txt
# PAUSA 4: Samuel escreveu "Pause" em 2026-11-18 03:00 UTC (lido em 2026-11-22 15:02; agentes já parados pelo limite semanal desde 2026-11-17 08:15).
Ao retomar: Luk_13-18 traduzido, revisor a7987d10a388dd673 interrompido (respawnar com /tmp/claude-0/prompt_revisor2.txt); tradutores parciais: Mat_24-28 a961b6a980bae0260, Jhn_15-21 a92e3f1b73fe57b8e, Act_18-23 a65d73a74f7f22479, Rom_9-16 a92e23dfe9590a855.
