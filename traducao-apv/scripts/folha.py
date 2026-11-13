"""Folha de trabalho compacta de um trecho, para o tradutor.
Uso: python3 scripts/folha.py <pasta fontes> <Livro> <cap_ini> <cap_fim>
Mostra, por versículo: texto-base, cada palavra (original | lema | Strong | morfologia em PT | glosa inglesa do STEPBible,
só como apoio, nunca copiada para a saída), as variantes e os alertas de raridade."""
import json, os, re, sys, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
from morfologia import hebraico, grego
from regras import base_nt, base_at
fontes, livro, ini, fim = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
tmp = f'/tmp/apv-trab-{os.getpid()}'
subprocess.run([sys.executable, os.path.join(AQUI, 'preparar.py'), fontes, livro, tmp], check=True, stdout=subprocess.DEVNULL)
auto = json.load(open(f'{tmp}/{livro}.auto.json', encoding='utf-8'))
vs = json.load(open(os.path.join(fontes, f'{livro}.json'), encoding='utf-8'))
NT = 'edicoes' in next(iter(vs.values()))[0]
for ref, ws in vs.items():
    c = int(ref.split('.')[1])
    if not ini <= c <= fim: continue
    base, chave = base_nt(ws) if NT else (base_at(ws), "")
    print(f'\n## {ref}\n' + ' '.join(w['orig'].replace('/', '').replace('\\', '') for w in base))
    for w in base:
        print(f"  {w['orig']} | {w.get('lema_grc') or w.get('lema_heb')} {w['lema']} | {grego(w['morf']) if NT else hebraico(w['morf'])} | en: {w.get('en','')}")
    if NT:
        for w in base:
            m = re.search(r'(?:^|\+)' + chave + r'([«»]\d+)', w.get('edicoes', ''))
            if m: print(f"  ORDEM: no {chave}, {w['orig']} fica em outra posição (marca {m.group(1)} do TAGNT); confira a ordem nas edições impressas")
    for n in auto[ref]['notas']: print('  VARIANTE:', n['texto'])
    for a in auto[ref]['alertas']: print('  RARIDADE:', a)
