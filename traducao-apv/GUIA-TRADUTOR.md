# Guia do tradutor da Ancient Paths Version (APV)

Leia este guia inteiro antes de traduzir. Ele vale para toda parte da Bíblia traduzida em paralelo, para que o texto fique uniforme.

## 1. O que você entrega

Um arquivo JSON por parte, em `traducao/partes/<Livro>_<capIni>-<capFim>.json`, assim:

```json
{
 "Mat.1.1": {
  "t": "Registro da genealogia de Jesus Cristo, filho de Davi, filho de Abraão.",
  "n": [
   {"tipo": "tn", "ancora": "Registro da genealogia", "termo": "Βίβλος γενέσεως (biblos geneseōs)",
    "titulo": "“registro da genealogia”",
    "texto": "Lit. “livro da origem”. ... Por que esta escolha, quais as alternativas e por que foram deixadas."}
  ]
 }
}
```

- `t`: o texto principal (camada 1) em português.
- `n`: as notas de estudo (camada 3). Cada nota tem:
  - `tipo`: `tn` (nota de tradução), `tc` (crítica textual) ou `sn` (nota de estudo: contexto, eco bíblico, teologia).
  - `ancora`: a palavra ou frase **exata** do seu texto `t` à qual a nota se refere. Tem de aparecer literalmente em `t` (o validador confere). Prefira âncoras curtas e únicas: a palavra ou expressão traduzida, não o versículo inteiro.
  - `termo`: o original (grego ou hebraico) com transliteração entre parênteses.
  - `titulo`: título curto da nota, como o leitor vai vê-lo.
  - `texto`: a explicação.
  - `revisar: true` quando a decisão é incerta e precisa de um revisor humano (hápax de sentido duvidoso, texto difícil, ponto teológico disputado). Não escreva “Revisão humana” no texto da nota; use o campo.

A camada 2 (espelho palavra por palavra) é gerada pelos scripts. Você não a escreve.

Use uma subpasta só sua para rascunhos e scripts (ex.: `/tmp/claude-0/-home-user/ba9b32b8-ba3a-598f-8152-bf4666dcb6e0/scratchpad/<Livro>_<ini>-<fim>/`), com nomes de arquivo que incluam o livro: outros tradutores trabalham ao mesmo tempo na mesma máquina.

Grave o arquivo **capítulo por capítulo** enquanto avança (leia o JSON, acrescente o capítulo, grave de novo), para não perder trabalho. Use Python para gravar JSON, nunca edição manual de texto com aspas soltas.

## 2. Como trabalhar

1. Para cada capítulo, gere a folha de trabalho:
   `python3 scripts/folha.py /tmp/claude-0/fontes <Livro> <cap> <cap>`
   (execute de dentro de `/home/user/o-caminho-acervo/traducao-apv`). A folha mostra o texto-base, cada palavra com lema, número Strong, morfologia em português e uma glosa inglesa do STEPBible (só apoio; nunca copie), as variantes entre edições e os alertas de raridade.
2. Traduza **do grego ou do hebraico da folha**, versículo por versículo. Nunca parta de outra tradução. Você pode lembrar como Almeida (ARC 1911) ou outras traduzem uma palavra para explicar numa nota por que a APV escolheu diferente, citando no máximo a palavra ou expressão, nunca frases inteiras de traduções protegidas (ARA, NVI, NAA, NVT, ESV, NIV etc.).
3. Escreva as notas no mesmo passo, enquanto a decisão está fresca.
4. Ao fim de cada capítulo, valide:
   `python3 scripts/validar_parte.py /tmp/claude-0/fontes traducao/partes/<Livro>_<ini>-<fim>.json`
   (durante o trabalho ele acusará os versículos que ainda faltam; no fim tem de dar 0 erro).

## 3. Texto-base

- **NT:** SBL Greek New Testament (palavras marcadas SBL no TAGNT). A folha já mostra só o texto-base; as palavras de outras edições aparecem como VARIANTE.
- **Versículos ausentes do texto crítico** (ex.: Mt 17:21; 18:11; 23:14; Mc 7:16; 9:44, 46; 11:26; 15:28; Lc 17:36; 23:17; Jo 5:4; At 8:37; 15:34; 24:7; 28:29; Rm 16:24): a folha mostra o texto-base vazio e as palavras do TR/Bizantino como VARIANTE. Traduza essas palavras entre colchetes duplos ⟦ ⟧ e escreva uma nota `tc` explicando que o versículo não está nos manuscritos mais antigos nem no texto crítico, e de onde vem.
- **Passagens longas em disputa** (Mc 16:9-20; Jo 7:53-8:11): traduza o texto inteiro, entre ⟦ ⟧ no início e no fim, com uma nota `tc` completa na primeira palavra.
- **Variantes dentro do versículo** (ex.: 1Jo 5:7-8, o “Comma Joanino”): o texto segue o crítico; a forma do TR vai em nota `tc` traduzida.
- **AT:** Texto Massorético de Leningrado (TAHOT), seguindo o Qere. Ketiv, Qumran, Septuaginta e emendas vão para notas `tc`.

## 4. Filosofia de tradução

Equivalência ótima: literal sempre que a clareza permite; idiomático só onde a forma literal esconderia o sentido. Quando trocar a forma pelo sentido, diga a forma literal na nota (“Lit. ...”).

- Português do Brasil atual, culto e fluente, para ser lido em voz alta na igreja.
- Mantenha os conectivos lógicos do grego (pois, portanto, porque, mas) e as frases-chave de Paulo; divida períodos longos só quando o português ficaria ininteligível, sem perder a relação lógica.
- Não acrescente palavras de interpretação ao texto. Se precisar acrescentar algo para o sentido, faça-o com parcimônia e registre em nota quando for relevante.
- Não suavize afirmações duras (juízo, inferno, escravidão) nem fortaleça o que o texto deixa aberto.

## 5. Termos fixos (use sempre assim)

| Original | APV | Observação |
|---|---|---|
| Χριστός | Cristo | “o Cristo” quando é título com artigo nos Evangelhos e Atos; na primeira ocorrência de cada livro, nota `tn` explicando “Messias, Ungido” |
| κύριος | Senhor | quando cita texto do AT em que o hebraico tem YHWH, nota `sn` dizendo isso |
| πνεῦμα ἅγιον / τὸ πνεῦμα (de Deus) | Espírito Santo / Espírito | maiúscula para o Espírito de Deus; minúscula para o espírito humano; nota quando for ambíguo |
| βασιλεία τοῦ θεοῦ / τῶν οὐρανῶν | Reino de Deus / Reino dos céus | |
| ὁ υἱὸς τοῦ ἀνθρώπου | o Filho do Homem | nota na primeira ocorrência de cada Evangelho (Dn 7:13) |
| ἐκκλησία | igreja | nota na primeira ocorrência de cada livro: “assembleia, comunidade convocada” |
| δοῦλος | servo | nota na primeira ocorrência de cada livro: literalmente “escravo” |
| εὐαγγέλιον | evangelho | “boas notícias” só em nota |
| δικαιοσύνη / δικαιόω | justiça / justificar | |
| πίστις / πιστεύω | fé / crer | “fidelidade” quando o contexto pedir, com nota |
| χάρις | graça | |
| σάρξ | carne | “corpo” ou “natureza humana” só quando é claramente físico ou humano, com nota |
| μετανοέω / μετάνοια | arrepender-se / arrependimento | |
| βαπτίζω | batizar | |
| ἅγιοι (crentes) | santos | |
| ἀμὴν λέγω ὑμῖν | Em verdade lhes digo | |
| ἐγώ εἰμι absoluto (Jo 8:58 etc.) | Eu Sou | nota `sn` (Êx 3:14; Is 43:10) |
| λόγος (Jo 1:1, 14; 1Jo 1:1; Ap 19:13) | a Palavra | nota `tn` explicando a escolha e a tradição “o Verbo” |
| μονογενής | único | nota `tn`: “unigênito” na tradição |
| ἱλαστήριον / ἱλασμός | propiciação | nota `tn` (expiação, sacrifício que afasta a ira) |
| Ἰουδαῖοι (em João) | judeus | nota `sn` sobre o sentido (muitas vezes as autoridades de Jerusalém) |
| ἀδελφοί (comunidade) | irmãos | nota na primeira ocorrência de cada livro: inclui as irmãs |
| ᾅδης / γέεννα | Hades / inferno | nota na primeira ocorrência: γέεννα = vale de Hinom |
| ἄγγελος | anjo / mensageiro | conforme o contexto, com nota quando ambíguo (Ap 2-3) |

Nomes próprios: a forma tradicional das Bíblias em português (Pedro, Tiago, Jerusalém, Cafarnaum).

**Tratamento:** entre pessoas, “você/vocês”. Em oração dirigida a Deus, “tu”. Jesus falando com o Pai: “tu”. Pessoas falando com Jesus nas narrativas: “o senhor” quando o chamam de κύριε, senão “você”; em louvor ou oração dirigidos a Jesus (At 7:59-60; Ap 5:9), “tu”.

**Decisões da onda 1 (valem para todos):**
- Mandamentos do AT citados na 2ª pessoa do singular (οὐ φονεύσεις, ἀγαπήσεις): imperativo com “você” (“Não mate”, “Ame o seu próximo”), com nota na primeira ocorrência de cada livro lembrando a forma tradicional (“Não matarás”).
- Deus Pai falando ao Filho (voz do céu, Sl 2:7 e 110:1 citados): “tu”. Deus falando a pessoas: “você/vocês”.
- τελώνης: “cobrador de impostos” (nota na primeira ocorrência de cada livro: “publicano”).
- Σίμων ὁ Καναναῖος: “Simão, o Zelote”, com nota (aramaico qan’ana; não é “cananeu” de Canaã). Ζηλωτής em Lucas e Atos: “o Zelote”.
- μακάριος: “bem-aventurado”.
- δοῦλος / δουλεύω / δουλόω: “escravo”, “ser escravo”, “escravizar” quando o texto contrasta com livre, liberto ou senhor de escravos como condição social ou figura dela (1Co 7:21-23; Rm 6:16-22; Gl 4); nos demais casos, “servo”. Nota na primeira ocorrência de cada livro.
- ἅρπαξ: “extorsor” (distinto de κλέπτης, “ladrão”).

**Versaletes:** no NT não use SENHOR em versaletes; o grego tem κύριος.

## 6. Notas: o que o leitor precisa

Siga o modelo das notas de Filipenses (`notas/Php.py`) e Rute (`notas/Rut.py`). A nota explica **por que esta palavra ou frase foi traduzida assim**, quais eram as alternativas e por que foram deixadas. Não repita o versículo inteiro.

Escreva nota sempre que:
- a tradução se afasta da forma literal (diga o literal);
- a palavra tem mais de um sentido possível e a escolha muda a leitura;
- a folha marca RARIDADE (hápax ou até 3 ocorrências): explique a base do sentido escolhido; se for incerto, `revisar: true`;
- há VARIANTE que muda o sentido ou a tradução, sobretudo entre Texto Crítico, Textus Receptus e Texto Majoritário (`tc`). Diferenças só de grafia, ordem ou artigo que não mudam a tradução podem ficar sem nota (o aparato automático já as registra);
- há citação ou eco do AT (`sn`, com a referência; diga se segue a Septuaginta ou o hebraico);
- há ponto teológico debatido: siga a leitura mais provável do texto e apresente as outras posições sérias, com nomes de estudiosos quando souber com segurança.

Média esperada: uma a duas notas por versículo, mais nos trechos densos, menos nas listas e narrativas simples.

**Rigor nas fontes:**
- Afirme sobre edições (NA28, SBLGNT, THGNT, Westcott-Hort, Tregelles, TR, Bizantino) só o que a folha mostra.
- Cite manuscritos (𝔓46, ℵ, A, B, D...) só quando tiver certeza; na dúvida, fale de “manuscritos mais antigos” e “maioria dos manuscritos”.
- Cite obras só se tiver certeza de que existem e dizem aquilo (ex.: Metzger, *A Textual Commentary on the Greek New Testament*, 2ª ed., 1994; BDAG). Nada de números de página inventados.
- Não invente dados arqueológicos, estatísticas ou datas.

**Linha teológica:** ortodoxa (credos Apostólico, Niceno, Calcedônia), continuísta, Escritura como autoridade final, aberta a mostrar as posições sérias em pontos secundários. Não force o texto para confirmar doutrina; deixe a nota mostrar o debate.

**Estilo das notas:** português claro e direto, frases curtas, sem jargão desnecessário. Termos técnicos (aoristo, genitivo, hápax) podem ser usados quando ajudam, explicados em poucas palavras na primeira vez de cada parte.

## 7. Glosas da camada 2

Se o validador de montagem acusar lemas sem glosa, não se preocupe: há um trabalho separado para o glossário. Você não precisa editar `glossario/`.

## 8. Ao terminar

Rode o validador e só dê a parte por concluída com 0 erro. Responda com: número de versículos, número de notas, quantas marcadas `revisar`, e os 3 a 5 pontos mais difíceis da parte (uma linha cada).
