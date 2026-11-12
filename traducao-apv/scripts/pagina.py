"""Gera a página de leitura (HTML) a partir de saida/*.json. Uso: python3 scripts/pagina.py <molde.html> <saída.html> Livro..."""
import json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
molde, destino, *livros = sys.argv[1:]
dados = {}
for l in livros:
    d = json.load(open(os.path.join(RAIZ, 'saida', f'{l}.json'), encoding='utf-8'))
    for v in d['versiculos']:
        for e in v['espelho']: e.pop('cod', None)
    dados[l] = d
html = open(molde, encoding='utf-8').read().replace('__DADOS__', json.dumps(dados, ensure_ascii=False).replace('</', '<\\/'))
open(destino, 'w', encoding='utf-8').write(html)
print(destino, round(len(html.encode()) / 1024), 'KB')
