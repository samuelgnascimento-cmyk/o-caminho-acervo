"""Monta as três camadas de um livro e a lista de triagem para revisão humana.

Uso: python3 scripts/montar.py <pasta fontes> <Livro>
Lê traducao/<Livro>.json (camada 1 + notas editoriais), glossario/*.tsv (camada 2) e as fontes.
Gera saida/<Livro>.json (três camadas), saida/<Livro>.md (leitura com notas) e saida/<Livro>.triagem.md.
"""
import json, os, re, sys, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from morfologia import hebraico, grego
from regras import base_nt, base_at

fontes, livro = sys.argv[1:3]
subprocess.run([sys.executable, os.path.join(AQUI, 'preparar.py'), fontes, livro, '/tmp/apv-trab'], check=True,
               stdout=subprocess.DEVNULL)
auto = json.load(open(f'/tmp/apv-trab/{livro}.auto.json', encoding='utf-8'))
vs = json.load(open(os.path.join(fontes, f'{livro}.json'), encoding='utf-8'))
trad = json.load(open(os.path.join(RAIZ, 'traducao', f'{livro}.json'), encoding='utf-8'))
meta = trad.pop('_livro')
glos = {}
for f in ('hebraico.tsv', 'grego.tsv'):
    for linha in open(os.path.join(RAIZ, 'glossario', f), encoding='utf-8'):
        if linha.startswith('#') or '\t' not in linha: continue
        k, v = linha.rstrip('\n').split('\t', 1)
        glos[k] = v

def glosa(strong):
    partes = []
    for s in re.findall(r'[HG]\d+[A-Za-z]?', strong):
        g = glos.get(s) or glos.get(re.sub(r'[A-Za-z]$', '', s))
        if g is None: return None
        if g in '-|.¶': continue
        partes.append(g)
    return ' + '.join(partes)

NT = 'edicoes' in next(iter(vs.values()))[0]
saida, faltas, triagem = {'livro': meta, 'versiculos': []}, set(), []
for ref, ws in vs.items():
    if ref not in trad:
        triagem.append(f'- {ref}: SEM TRADUÇÃO'); continue
    base = base_nt(ws)[0] if NT else base_at(ws)
    espelho = []
    for w in base:
        g = glosa(w['strong'])
        if g is None: faltas.add(w['lema'])
        espelho.append({'orig': w['orig'].replace('/', '').replace('\\', ''), 'translit': w['translit'].replace('/', ''),
                        'lema': w.get('lema_heb') or w.get('lema_grc'), 'strong': w['lema'], 'glosa': g or '?',
                        'morf': grego(w['morf']) if NT else hebraico(w['morf']), 'cod': w['morf']})
    t = trad[ref]
    revisar = [n['texto'] for n in t['n'] if n.get('revisar')]
    for a in auto[ref]['alertas']:
        triagem.append(f'- {ref}: palavra rara {a}')
    for r in revisar:
        triagem.append(f'- {ref}: {r}')
    saida['versiculos'].append({'ref': ref, 'texto': t['t'], 'espelho': espelho, 'notas': t['n'],
                                'aparato': auto[ref]['notas']})

os.makedirs(os.path.join(RAIZ, 'saida'), exist_ok=True)
json.dump(saida, open(os.path.join(RAIZ, 'saida', f'{livro}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

md, cap_atual, nota_n, rodape = [f"# {meta['nome']}\n", f"*Ancient Paths Version (APV), tradução em português. Base: {meta['base']}. Estado: {meta['estado']}.*\n"], None, 0, []
for v in saida['versiculos']:
    _, c, n = v['ref'].split('.')
    if c != cap_atual:
        if rodape: md += ['', *rodape]; rodape = []
        md.append(f'\n## {meta["nome"]} {c}\n'); cap_atual = c
    marcas = ''
    for nota in v['notas']:
        nota_n += 1
        marcas += f'[^{nota_n}]'
        rodape.append(f'[^{nota_n}]: {c}:{n} ({nota["tipo"]}) {nota["texto"]}')
    md.append(f'<sup>{n}</sup> {v["texto"]}{marcas}')
md += ['', *rodape]
open(os.path.join(RAIZ, 'saida', f'{livro}.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
open(os.path.join(RAIZ, 'saida', f'{livro}.triagem.md'), 'w', encoding='utf-8').write(
    f'# Triagem para revisão humana: {meta["nome"]}\n\nPontos que um revisor com hebraico/grego deve conferir antes de o texto ser considerado final.\n\n'
    + '\n'.join(triagem) + '\n')
print(livro, len(saida['versiculos']), 'versículos;', len(triagem), 'itens de triagem;',
      'glosas faltando:', ' '.join(sorted(faltas)) or 'nenhuma')
