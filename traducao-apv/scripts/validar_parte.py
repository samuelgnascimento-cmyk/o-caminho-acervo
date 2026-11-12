"""Confere uma parte traduzida: todos os versículos do trecho, âncoras presentes, tipos válidos, campos completos.
Uso: python3 scripts/validar_parte.py <pasta fontes> traducao/partes/<Livro>_<ini>-<fim>.json"""
import json, os, re, sys
fontes, arq = sys.argv[1:3]
m = re.match(r'(\w+)_(\d+)-(\d+)\.json$', os.path.basename(arq))
livro, ini, fim = m.group(1), int(m.group(2)), int(m.group(3))
vs = json.load(open(os.path.join(fontes, f'{livro}.json'), encoding='utf-8'))
esperados = [r for r in vs if ini <= int(r.split('.')[1]) <= fim]
d = json.load(open(arq, encoding='utf-8'))
erros = []
for r in esperados:
    if r not in d: erros.append(f'{r}: falta'); continue
    v = d[r]
    if not v.get('t', '').strip(): erros.append(f'{r}: texto vazio')
    for i, n in enumerate(v.get('n', [])):
        for k in ('tipo', 'ancora', 'termo', 'titulo', 'texto'):
            if not n.get(k): erros.append(f'{r} nota {i}: campo {k} vazio')
        if n.get('tipo') not in ('tn', 'tc', 'sn'): erros.append(f"{r} nota {i}: tipo {n.get('tipo')}")
        if n.get('ancora') and n['ancora'] not in v['t']: erros.append(f"{r} nota {i}: âncora fora do texto: {n['ancora']}")
for r in d:
    if r not in esperados: erros.append(f'{r}: versículo fora do trecho')
notas = sum(len(v.get('n', [])) for v in d.values())
print(f'{livro} {ini}-{fim}: {len(d)}/{len(esperados)} versículos, {notas} notas, {len(erros)} erro(s)')
for e in erros[:60]: print(' ', e)
sys.exit(1 if erros else 0)
