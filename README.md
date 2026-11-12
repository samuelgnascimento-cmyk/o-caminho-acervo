# Acervo do O Caminho

Arquivos baixados sob demanda pelo app [O Caminho](https://github.com/samuelgnascimento-cmyk/o-caminho).
O catálogo de cada pasta fica dentro do app (`public/data/acervo.json` e `public/data/acervo-biblias.json`).

- `livros/<n>.json.gz`: livros cristãos do [Projeto Gutenberg](https://www.gutenberg.org), de autores falecidos até 1955
  (domínio público no Brasil, Lei 9.610/98, art. 41). O número é o do livro no Gutenberg. Capítulos e parágrafos;
  as referências bíblicas estão marcadas como `⟦JHN.3.16|John 3:16⟧`. Gerado por `scripts/build_acervo.py`.
- `biblias/<id>.json.gz`: Bíblias e Novos Testamentos do [eBible.org](https://ebible.org), somente os marcados como
  de distribuição livre (domínio público ou licenças Creative Commons). A licença de cada uma vai no campo `license`.
  Convertidos do USFM sem alterar o texto. Gerado por `scripts/build_biblias.ts`.

Os textos pertencem ao domínio público ou aos seus detentores, conforme indicado em cada arquivo.
