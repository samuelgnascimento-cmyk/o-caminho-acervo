# Ancient Paths Version (APV)

Tradução original da Bíblia para o português, feita como projeto independente do app [O Caminho](https://github.com/samuelgnascimento-cmyk/o-caminho). Só entra no app depois de concluída.

**Nome.** *Ancient Paths* vem de Jeremias 6:16: “Ponham-se nos caminhos e olhem; perguntem pelas veredas antigas, qual é o bom caminho, e andem por ele.” As veredas antigas são o texto hebraico, aramaico e grego; o bom caminho liga a tradução ao nome do app (At 9:2).

## Estado

| Livro | Versículos | Camadas | Revisão cruzada | Revisão humana |
|---|---|---|---|---|
| Rute | 85 | 1, 2 e 3 | feita | pendente |
| Filipenses | 104 | 1, 2 e 3 | feita | pendente |
| Demais 64 livros | ~31.000 | pendente | pendente | pendente |

O texto é um rascunho produzido com IA dentro do pipeline abaixo. Não é final enquanto um revisor com domínio de hebraico e grego não passar pela lista de triagem de cada livro (`saida/<Livro>.triagem.md`).

## As três camadas

1. **Texto principal** (`traducao/<Livro>.json`, campo `t`): equivalência ótima. Literal sempre que a clareza permite; idiomático só onde a forma literal esconderia o sentido. Português do Brasil contemporâneo.
2. **Espelho formal-morfológico** (gerado em `saida/<Livro>.json`, campo `espelho`): cada palavra do original com transliteração, lema, número Strong estendido, glosa em português (`glossario/*.tsv`) e análise morfológica por extenso (`scripts/morfologia.py`).
3. **Aparato de notas** (campo `n`, mais o campo `aparato` gerado): notas de tradução, forma literal, crítica textual, contexto e teologia, no estilo da NET Bible. O `aparato` lista mecanicamente toda diferença entre edições registrada no STEPBible.

## Texto-base

- **Antigo Testamento:** Texto Massorético do Códice de Leningrado, como amalgamado no TAHOT (STEPBible). Segue-se o Qere; o Ketiv, as leituras de Alepo, Cairo, BHS, Qumran e Septuaginta registradas no TAHOT vão para o aparato.
- **Novo Testamento:** SBL Greek New Testament, por meio do TAGNT (STEPBible), que marca palavra por palavra a presença no NA27/28, THGNT, SBLGNT, Westcott-Hort, Tregelles, Textus Receptus e Texto Bizantino. Toda divergência relevante entre Texto Crítico, Textus Receptus e Texto Majoritário vira nota. Versículos ausentes do SBLGNT seguem o NA28 e recebem nota.

## Guia de estilo

- O nome divino YHWH é “o SENHOR” (versaletes no app). Adonai é “Senhor”; Elohim é “Deus”; Shaddai é “Todo-Poderoso”, com nota.
- Entre pessoas usa-se “você/vocês”. Na fala dirigida a Deus, “tu”.
- Termos de aliança recebem tradução fixa e nota na primeira ocorrência de cada livro: hesed = “bondade leal”; go’el = “resgatador”; doulos = “servo” (nota: “escravo”); episkopos = “supervisor” (nota: “bispo”).
- Palavras acrescentadas para o sentido não são marcadas em itálico no texto; a forma literal vai em nota quando a diferença importa.
- Pontos teológicos debatidos: o texto segue a leitura mais provável do original, e a nota apresenta as outras posições sérias, com autores.

## Pipeline (anti-desvio)

1. `scripts/extrair_fontes.py`: lê TAHOT/TAGNT e gera um JSON por livro e a frequência de cada lema.
2. `scripts/preparar.py`: folha de trabalho do tradutor (texto-base, análise em português), variantes e **bloqueio de raridade**: toda palavra com até 3 ocorrências (hápax e raras), exceto nomes próprios, é marcada para revisão.
   `scripts/conferir_nt.py` confere o texto-base do NT contra o SBLGNT oficial, versículo por versículo (Filipenses: 0 diferenças; NT inteiro: 75 de 7.939 versículos a examinar, quase todos de versificação).
3. Tradução da camada 1 e das notas, versículo por versículo, sempre a partir do original e da análise, nunca de outra tradução.
4. `scripts/montar.py`: junta as três camadas e gera `saida/<Livro>.json`, `saida/<Livro>.md` (leitura com notas de rodapé) e a lista de triagem.
5. **Julgamento cruzado:** outro modelo revisa cada versículo contra o original e aponta erro de sentido, omissão, acréscimo, nota errada ou viés. As correções aceitas entram no texto; as recusadas ficam registradas em `revisao/`.
6. `scripts/pagina.py` gera a página de leitura com as três camadas.
7. **Triagem humana:** os itens de `saida/<Livro>.triagem.md` (palavras raras, passagens difíceis, notas com “Revisão humana”) precisam de aprovação de um revisor.

Para regenerar tudo:

```sh
git clone --depth 1 https://github.com/STEPBible/STEPBible-Data.git /tmp/step
python3 scripts/extrair_fontes.py "/tmp/step/Translators Amalgamated OT+NT" /tmp/apv-fontes
python3 scripts/montar.py /tmp/apv-fontes Rut
```

## Licenças

- Dados de origem: [STEPBible-Data](https://github.com/STEPBible/STEPBible-Data) (Tyndale House, Cambridge), CC BY 4.0. O TAHOT inclui o Westminster Leningrad Codex (domínio público) e a morfologia derivada do ETCBC; o TAGNT inclui o SBLGNT (CC BY 4.0). As glosas em inglês do STEPBible não são usadas na saída.
- Não se usam dados sob licença não comercial (ETCBC BHSA/DSS, CC BY-NC) nem textos de traduções protegidas (NA28 impresso, ARA, NVI, NAA, ESV etc.).
- A tradução, as glosas em português, as notas e os scripts da APV: CC BY 4.0, para que o texto possa circular livremente, inclusive em outros apps, com atribuição.
