"""Prepara a folha de trabalho de um livro e as notas automáticas (camada 3).

Uso: python3 scripts/preparar.py <pasta fontes> <Livro> <pasta saída>
Gera:
  <saída>/<Livro>.folha.md   folha de trabalho do tradutor (texto-base, análise e alertas)
  <saída>/<Livro>.auto.json  variantes e alertas de raridade por versículo
"""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from morfologia import hebraico, grego
from regras import eds, base_nt, base_at

fontes, livro, out = sys.argv[1:4]
vs = json.load(open(os.path.join(fontes, f'{livro}.json'), encoding='utf-8'))
freq = json.load(open(os.path.join(fontes, 'frequencia.json'), encoding='utf-8'))
NT = any('edicoes' in w for w in next(iter(vs.values())))
SIG_H = dict(K='Ketiv (texto escrito)', A='Códice de Alepo', B='BHS', C='Códice do Cairo', D='Qumran / Deserto da Judeia',
             E='emenda erudita', F='outra divisão/pontuação', H='Bíblia Rabínica (Ben Chaim)', P='pontuação alternativa',
             S='tradição escribal (Tiqqune Sopherim)', X='Septuaginta (via BHS/BHK)', V='outras versões antigas')
ED = {'NA28': 'NA28', 'NA27': 'NA27', 'Tyn': 'THGNT', 'SBL': 'SBLGNT', 'WH': 'Westcott-Hort', 'Treg': 'Tregelles',
      'TR': 'Textus Receptus', 'Byz': 'Bizantino/Majoritário', 'KJV': 'KJV'}


def raridade(w):
    f = freq.get(w['lema'], 0)
    if w['lema'].startswith(('H9', 'G9')) or not w['lema']: return None
    m = w['morf']
    if re.search(r'(^|/)[HA]?Np|-[PLT]$|-PRI$', m): return None  # nomes próprios não entram no alerta
    if f <= 1: return 'hapax'
    if f <= 3: return f'raro ({f}x)'
    return None

auto, linhas = {}, [f'# Folha de trabalho: {livro}\n']
for ref, ws in vs.items():
    notas, alertas = [], []
    if NT:
        base, chave = base_nt(ws)
        if chave != 'SBL': notas.append({'tipo': 'variante', 'texto': 'Versículo ausente do SBLGNT; o texto segue o NA28 (entre colchetes duplos nas edições críticas).'})
        fora = [w for w in ws if w not in base]
        if fora:
            grupos = {}
            for w in fora: grupos.setdefault(w['edicoes'], []).append(w['orig'])
            for e, pal in grupos.items():
                notas.append({'tipo': 'variante', 'texto': f"{' '.join(pal)}: presente em {', '.join(ED.get(x, x) for x in eds(e))}; ausente do texto-base."})
        omit = {}
        for w in base:
            falta = [x for x in ('TR', 'Byz') if x not in eds(w['edicoes'])]
            if falta: omit.setdefault(tuple(falta), []).append(w['orig'])
        for falta, pal in omit.items():
            notas.append({'tipo': 'variante', 'texto': f"{' '.join(pal)}: ausente em {' e '.join(ED[x] for x in falta)}."})
    else:
        base = base_at(ws)
        for w in ws:
            t = w['tipo']
            if t[:1] == 'K': notas.append({'tipo': 'variante', 'texto': f"Ketiv {w['orig']}: o texto segue o Qere."})
            elif t[:1] == 'X': notas.append({'tipo': 'variante', 'texto': f"{w['orig']}: palavra preservada na Septuaginta (reconstruída em BHS/BHK), ausente do TM; não incluída no texto."})
            m = re.search(r'\(([^)]*)\)', t)
            if m and t[:1] in 'LQR':
                for s in m.group(1).split('+'):
                    if s and s.isupper():
                        notas.append({'tipo': 'variante', 'texto': f"{w['orig']}: há variante significativa em {', '.join(SIG_H.get(ch, ch) for ch in s)}."})
    for w in base:
        r = raridade(w)
        if r: alertas.append(f"{w['orig']} ({w.get('lema_heb') or w.get('lema_grc')}, {w['lema']}): {r}")
    auto[ref] = {'notas': notas, 'alertas': alertas}
    linhas.append(f"\n## {ref}\n" + ' '.join(w['orig'] for w in base))
    for w in base:
        mf = grego(w['morf']) if NT else hebraico(w['morf'])
        lem = w.get('lema_heb') or w.get('lema_grc')
        linhas.append(f"- {w['orig']} | {w['translit']} | {lem} {w['lema']} | {mf}")
    for n in notas: linhas.append(f"  * VARIANTE: {n['texto']}")
    for a in alertas: linhas.append(f"  * RARIDADE: {a}")

os.makedirs(out, exist_ok=True)
open(os.path.join(out, f'{livro}.folha.md'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
json.dump(auto, open(os.path.join(out, f'{livro}.auto.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(livro, len(vs), 'versículos;', sum(len(a['notas']) for a in auto.values()), 'notas de variante;',
      sum(len(a['alertas']) for a in auto.values()), 'alertas de raridade')
