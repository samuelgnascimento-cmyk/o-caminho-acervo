"""Grava as notas ancoradas de notas/<Livro>.py em traducao/<Livro>.json (campo n) e confere as âncoras.
Uso: python3 scripts/aplicar_notas.py Livro"""
import sys, os, json, importlib.util
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
livro = sys.argv[1]
spec = importlib.util.spec_from_file_location('n', os.path.join(RAIZ, 'notas', f'{livro}.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
p = os.path.join(RAIZ, 'traducao', f'{livro}.json')
d = json.load(open(p, encoding='utf-8'))
erros = []
for ref, v in d.items():
    if ref.startswith('_'): continue
    novas = []
    for t in m.N.get(ref, []):
        tipo, ancora, termo, titulo, texto, *rev = t
        if tipo not in ('tn', 'tc', 'sn'): erros.append(f'{ref}: tipo {tipo}')
        if ancora not in v['t']: erros.append(f'{ref}: âncora não encontrada: {ancora}')
        nota = {'tipo': tipo, 'ancora': ancora, 'termo': termo, 'titulo': titulo, 'texto': texto}
        if rev and rev[0]: nota['revisar'] = True
        novas.append(nota)
    v['n'] = novas
for ref in m.N:
    if ref not in d: erros.append(f'{ref}: versículo inexistente')
if erros: sys.exit('\n'.join(erros))
open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(livro, sum(len(v) for v in m.N.values()), 'notas aplicadas')
