"""Junta as partes traduzidas de um livro em traducao/<Livro>.json e as glosas novas em glossario/<lingua>.tsv.
Uso: python3 scripts/juntar.py <pasta fontes> <Livro> [<Livro> ...]
     python3 scripts/juntar.py --glosas            (só as glosas de glossario/partes/*.tsv)"""
import glob, json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMES = {'Mat': 'Mateus', 'Mrk': 'Marcos', 'Luk': 'Lucas', 'Jhn': 'João', 'Act': 'Atos', 'Rom': 'Romanos',
         '1Co': '1 Coríntios', '2Co': '2 Coríntios', 'Gal': 'Gálatas', 'Eph': 'Efésios', 'Php': 'Filipenses',
         'Col': 'Colossenses', '1Th': '1 Tessalonicenses', '2Th': '2 Tessalonicenses', '1Ti': '1 Timóteo',
         '2Ti': '2 Timóteo', 'Tit': 'Tito', 'Phm': 'Filemom', 'Heb': 'Hebreus', 'Jas': 'Tiago', '1Pe': '1 Pedro',
         '2Pe': '2 Pedro', '1Jn': '1 João', '2Jn': '2 João', '3Jn': '3 João', 'Jud': 'Judas', 'Rev': 'Apocalipse'}
BASE_NT = 'SBL Greek New Testament (via TAGNT/STEPBible), com aparato de NA28, THGNT, Textus Receptus e Texto Bizantino'

def glosas():
    for lingua, pref in (('grego', 'G'), ('hebraico', 'H')):
        alvo = os.path.join(RAIZ, 'glossario', f'{lingua}.tsv')
        linhas = open(alvo, encoding='utf-8').read().rstrip('\n').split('\n')
        tem = {l.split('\t')[0] for l in linhas if '\t' in l and not l.startswith('#')}
        novas = 0
        for p in sorted(glob.glob(os.path.join(RAIZ, 'glossario', 'partes', '*.tsv'))):
            for l in open(p, encoding='utf-8'):
                l = l.rstrip('\n')
                if l.startswith('#') or '\t' not in l: continue
                k, g = l.split('\t')[:2]
                if k.startswith(pref) and k not in tem and g.strip():
                    linhas.append(f'{k}\t{g.strip()}'); tem.add(k); novas += 1
        cab = [l for l in linhas if l.startswith('#')]
        corpo = sorted((l for l in linhas if not l.startswith('#')), key=lambda l: l.split('\t')[0])
        open(alvo, 'w', encoding='utf-8').write('\n'.join(cab + corpo) + '\n')
        print(f'{lingua}.tsv: +{novas} glosas ({len(corpo)} no total)')

def livro(fontes, lv):
    vs = json.load(open(os.path.join(fontes, f'{lv}.json'), encoding='utf-8'))
    partes = sorted(glob.glob(os.path.join(RAIZ, 'traducao', 'partes', f'{lv}_*.json')),
                    key=lambda p: int(re.search(r'_(\d+)-', p).group(1)))
    junto = {}
    for p in partes:
        d = json.load(open(p, encoding='utf-8'))
        for r in d:
            if r in junto: print(f'  aviso: {r} repetido em {os.path.basename(p)}')
        junto.update(d)
    alvo = os.path.join(RAIZ, 'traducao', f'{lv}.json')
    meta = json.load(open(alvo, encoding='utf-8'))['_livro'] if os.path.exists(alvo) else {
        'id': lv, 'nome': NOMES.get(lv, lv), 'base': BASE_NT,
        'estado': 'rascunho com revisão cruzada; aguarda revisão humana'}
    saida = {'_livro': meta}
    faltam = [r for r in vs if r not in junto]
    for r in vs:
        if r in junto: saida[r] = junto[r]
    json.dump(saida, open(alvo, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{lv}: {len(partes)} parte(s), {len(saida) - 1}/{len(vs)} versículos'
          + (f', faltam {len(faltam)}: {", ".join(faltam[:8])}' if faltam else ''))
    return not faltam

if sys.argv[1] == '--glosas':
    glosas()
else:
    ok = all([livro(sys.argv[1], lv) for lv in sys.argv[2:]])
    sys.exit(0 if ok else 1)
