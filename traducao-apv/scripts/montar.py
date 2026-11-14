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
        b = re.sub(r'[A-Za-z]$', '', s)
        g = glos.get(s) or glos.get(b) or next((glos[k] for k in sorted(glos) if k[:-1] == b and k[-1].isalpha()), None)
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
    revisar = [f"{n['titulo']}: {n['texto']}" for n in t['n'] if n.get('revisar')]
    for a in auto[ref]['alertas']:
        triagem.append(f'- {ref}: palavra rara {a}')
    for r in revisar:
        triagem.append(f'- {ref}: {r}')
    saida['versiculos'].append({'ref': ref, 'texto': t['t'], 'espelho': espelho, 'notas': t['n'],
                                'aparato': auto[ref]['notas']})

def marcar(v):
    """Dá a cada nota uma marca no padrão NET (tn 1.2, tc 1.2, tn 1.2b) e a posição da âncora no texto."""
    _, c, n = v['ref'].split('.')
    vistos = {}
    for nota in v['notas']:
        k = nota['tipo']; vistos[k] = vistos.get(k, 0) + 1
        suf = '' if vistos[k] == 1 else chr(ord('a') + vistos[k] - 1)
        nota['marca'] = f"{k} {c}.{n}{suf}"
        pos = v['texto'].find(nota['ancora'])
        nota['pos'] = pos + len(nota['ancora']) if pos >= 0 else len(v['texto'])

def com_marcas(v, fmt):
    t, extra = v['texto'], 0
    for nota in sorted(v['notas'], key=lambda x: x['pos']):
        m = fmt(nota); t = t[:nota['pos'] + extra] + m + t[nota['pos'] + extra:]; extra += len(m)
    return t

for v in saida['versiculos']: marcar(v)
os.makedirs(os.path.join(RAIZ, 'saida'), exist_ok=True)
json.dump(saida, open(os.path.join(RAIZ, 'saida', f'{livro}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

NOMES = {'tn': 'nota de tradução', 'tc': 'crítica textual', 'sn': 'nota de estudo'}
md = [f"# {meta['nome']} — Ancient Paths Version (APV)\n",
      f"**Texto-base:** {meta['base']}. **Estado:** {meta['estado']}.\n",
      "| Sigla | Significado |", "| :--- | :--- |",
      "| **[tn]** | Nota de tradução: por que esta palavra ou frase foi traduzida assim, e as alternativas |",
      "| **[tc]** | Crítica textual: variantes entre manuscritos e edições, e qual leitura foi seguida |",
      "| **[sn]** | Nota de estudo: contexto histórico, eco bíblico ou ponto teológico |",
      "| **TM / LXX** | Texto Massorético / Septuaginta |",
      "| **TR / Byz / NA28 / SBLGNT** | Textus Receptus / Texto Bizantino (Majoritário) / Nestle-Aland 28 / SBL Greek New Testament |", "\n---"]
caps = {}
for v in saida['versiculos']: caps.setdefault(v['ref'].split('.')[1], []).append(v)
for c, vs in caps.items():
    md.append(f"\n## {meta['nome']} {c}\n\n### Texto\n")
    for v in vs:
        md.append(f"**{v['ref'].split('.')[2]}** " + com_marcas(v, lambda x: f" **[{x['marca']}]**").replace('  ', ' ') + '  ')
    md.append(f"\n### Notas ({meta['nome']} {c})\n")
    for v in vs:
        for x in v['notas']:
            md.append(f"- **[{x['marca']}] {x['titulo']}** ({x['termo']}): {x['texto']}" + (' *(em triagem)*' if x.get('revisar') else ''))
    md.append('\n---')
open(os.path.join(RAIZ, 'saida', f'{livro}.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
open(os.path.join(RAIZ, 'saida', f'{livro}.triagem.md'), 'w', encoding='utf-8').write(
    f'# Triagem para revisão humana: {meta["nome"]}\n\nPontos que um revisor com hebraico/grego deve conferir antes de o texto ser considerado final.\n\n'
    + '\n'.join(triagem) + '\n')
print(livro, len(saida['versiculos']), 'versículos;', len(triagem), 'itens de triagem;',
      'glosas faltando:', ' '.join(sorted(faltas)) or 'nenhuma')
