"""Extrai TAHOT/TAGNT (STEPBible-Data, CC BY 4.0) para JSON por livro.

Uso: python3 scripts/extrair_fontes.py <pasta "Translators Amalgamated OT+NT"> fontes/
Gera fontes/<Livro>.json  {"ref": [palavra, ...]} e fontes/frequencia.json (lema -> ocorrências).
"""
import json, re, sys, glob, os, collections

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
livros = collections.OrderedDict()
freq = collections.Counter()
ref_re = re.compile(r'^([1-3]?[A-Za-z]{2,3})\.(\d+)\.(\d+)(?:[(\[][^)\]]*[)\]])?#(\d+)=(\S+)')

def strongs_principal(s):
    m = re.search(r'\{([HG]\d+[A-Za-z]?)\}', s)
    if m: return m.group(1)
    m = re.search(r'([HG]\d+[A-Za-z]?)', s)
    return m.group(1) if m else ''

for f in sorted(glob.glob(os.path.join(src, 'TAHOT*.txt'))):
    for linha in open(f, encoding='utf-8'):
        m = ref_re.match(linha)
        if not m: continue
        c = linha.rstrip('\n').split('\t')
        livro, cap, vers, n, tipo = m.groups()
        ref = f'{livro}.{cap}.{vers}'
        lema = strongs_principal(c[4])
        lexico = re.search(r'\{' + re.escape(lema) + r'=([^=]*)=', c[11]) if lema else None
        p = {'n': int(n), 'tipo': tipo, 'orig': c[1], 'translit': c[2], 'strong': c[4],
             'lema': lema, 'lema_heb': lexico.group(1) if lexico else '', 'morf': c[5], 'en': c[3],
             'var_sentido': c[6], 'var_grafia': c[7]}
        livros.setdefault(livro, collections.OrderedDict()).setdefault(ref, []).append(p)
        if tipo.startswith('L') or 'L' in tipo: freq[lema] += 1

for f in sorted(glob.glob(os.path.join(src, 'TAGNT*.txt'))):
    for linha in open(f, encoding='utf-8'):
        m = ref_re.match(linha)
        if not m: continue
        c = linha.rstrip('\n').split('\t')
        livro, cap, vers, n, tipo = m.groups()
        ref = f'{livro}.{cap}.{vers}'
        g = re.match(r'(.*?)\s*\((.*)\)', c[1])
        strong, _, morf = c[3].partition('=')
        lema_grc, _, _ = c[4].partition('=')
        p = {'n': int(n), 'tipo': tipo, 'orig': g.group(1) if g else c[1], 'translit': g.group(2) if g else '',
             'strong': strong, 'lema': re.sub(r'[A-Z]$', '', strong) if strong.startswith('G') else strong,
             'lema_grc': lema_grc, 'morf': morf, 'en': c[2], 'edicoes': c[5], 'var_sentido': c[6], 'var_grafia': c[7]}
        livros.setdefault(livro, collections.OrderedDict()).setdefault(ref, []).append(p)
        if 'SBL' in c[5]: freq[p['lema']] += 1

for livro, vs in livros.items():
    json.dump(vs, open(os.path.join(out, f'{livro}.json'), 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(freq, open(os.path.join(out, 'frequencia.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print(len(livros), 'livros;', sum(len(v) for v in livros.values()), 'versículos;', len(freq), 'lemas')
