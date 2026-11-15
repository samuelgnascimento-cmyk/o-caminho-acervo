"""Expande códigos morfológicos para português.
Hebraico/aramaico: códigos ETCBC/OSHB usados no TAHOT (ex.: Hc/Vqw3ms).
Grego: códigos Robinson usados no TAGNT (ex.: V-PAI-3S)."""
import re

G = {'m': 'masc.', 'f': 'fem.', 'b': 'ambos gên.', 'c': 'comum', 'n': 'neutro'}
NUM = {'s': 'sing.', 'p': 'pl.', 'd': 'dual'}
EST = {'a': 'absoluto', 'c': 'construto', 'd': 'determinado'}
TRONCO_H = dict(q='qal', N='nifal', p='piel', P='pual', h='hifil', H='hofal', t='hitpael', o='polel', O='polal',
    r='hitpolel', m='poel', M='poal', k='palel', K='pulal', Q='qal passivo', l='pilpel', L='polpal', f='hitpalpel',
    D='nitpael', j='pealal', i='pilel', u='hotpaal', c='tifil', v='hishtafel', w='nitpalel', y='nitpoel', z='hitpoel')
TRONCO_A = dict(q='peal', Q='peil', u='hitpeel', p='pael', P='itpaal', M='hitpaal', a='afel', h='hafel', s='safel',
    e='shafel', H='hofal', i='itpeel', t='hishtafel', v='ishtafel', w='hitafel', o='polel', z='itpoel', r='hitpolel',
    f='hitpalpel', b='hefal', c='tifel', m='poel', l='palpel', L='itpalpel', O='itpolel', G='itafal')
CONJ = dict(p='perfeito', q='perfeito consecutivo', i='imperfeito', w='imperfeito consecutivo', h='coortativo',
    j='jussivo', v='imperativo', r='particípio ativo', s='particípio passivo', a='infinitivo absoluto',
    c='infinitivo construto')
POS_H = dict(C='conjunção', D='advérbio', R='preposição', T='partícula')
TIPO_T = dict(a='de afirmação', d='artigo definido', e='exortativa', i='interrogativa', j='interjeição',
    m='demonstrativa', n='negação', o='marca de objeto direto', r='relativa')
TIPO_P = dict(d='demonstrativo', f='indefinido', i='interrogativo', p='pessoal', r='relativo')
TIPO_S = dict(d='he direcional', h='he paragógico', n='nun paragógico', p='sufixo pronominal')

def _pgn(s):
    out = []
    for ch in s:
        if ch in '123': out.append(ch + 'ª p.')
        elif ch in G: out.append(G[ch])
        elif ch in NUM: out.append(NUM[ch])
    return ' '.join(out)

def _gne(s):
    out = []
    if len(s) > 0 and s[0] in G: out.append(G[s[0]])
    if len(s) > 1 and s[1] in NUM: out.append(NUM[s[1]])
    if len(s) > 2 and s[2] in EST: out.append(EST[s[2]])
    return ' '.join(out)

def hebraico(cod):
    if not cod: return ''
    lang = 'aram.' if cod[0] == 'A' else ''
    partes = []
    for i, seg in enumerate(cod.split('/')):
        if i == 0 and seg[:1] in 'HA': seg = seg[1:]
        if not seg: continue
        p, r = seg[0], seg[1:]
        if p == 'V':
            tr = (TRONCO_A if lang else TRONCO_H).get(r[:1], r[:1])
            cj = CONJ.get(r[1:2], r[1:2])
            resto = r[2:]
            d = f'verbo {tr} {cj}'
            if cj.startswith('infinitivo') and len(resto) == 1:
                pass  # o TAHOT repete a letra do infinitivo; não há estado a acrescentar
            elif cj.startswith('particípio') or cj.startswith('infinitivo'):
                d += (' ' + _gne(resto)) if resto else ''
            else:
                d += (' ' + _pgn(resto)) if resto else ''
            partes.append(d.strip())
        elif p == 'N':
            t = {'c': 'subst.', 'g': 'gentílico', 'p': 'nome próprio'}.get(r[:1], 'subst.')
            partes.append((t + ' ' + _gne(r[1:])).strip())
        elif p == 'A':
            t = {'a': 'adj.', 'c': 'numeral cardinal', 'g': 'adj. gentílico', 'o': 'numeral ordinal'}.get(r[:1], 'adj.')
            partes.append((t + ' ' + _gne(r[1:])).strip())
        elif p == 'P':
            partes.append(('pron. ' + TIPO_P.get(r[:1], '') + ' ' + _pgn(r[1:])).strip())
        elif p == 'S':
            partes.append((TIPO_S.get(r[:1], 'sufixo') + ' ' + _pgn(r[1:])).strip())
        elif p == 'T':
            partes.append(('partícula ' + TIPO_T.get(r[:1], '')).strip())
        elif p == 'R':
            partes.append('preposição' + (' + artigo' if r == 'd' else ''))
        elif p == 'c':
            partes.append('conjunção')
        else:
            partes.append(POS_H.get(p, seg))
    return (lang + ' ' if lang else '') + ' / '.join(partes)

CASO = dict(N='nom.', G='gen.', D='dat.', A='acus.', V='voc.')
GEN_G = dict(M='masc.', F='fem.', N='neutro')
NUM_G = dict(S='sing.', P='pl.')
TEMPO = {'P': 'presente', 'I': 'imperfeito', 'F': 'futuro', 'A': 'aoristo', 'R': 'perfeito', 'L': 'mais-que-perfeito',
         '2A': 'aoristo 2º', '2F': 'futuro 2º', '2R': 'perfeito 2º', '2L': 'mais-que-perf. 2º', '2P': 'presente'}
VOZ = dict(A='ativo', M='médio', P='passivo', E='médio/passivo', D='médio depoente', O='passivo depoente',
           N='médio/passivo depoente', Q='impessoal ativo', X='sem voz')
MODO = dict(I='indicativo', S='subjuntivo', O='optativo', M='imperativo', N='infinitivo', P='particípio')
POS_G = {'N': 'subst.', 'A': 'adj.', 'T': 'artigo', 'P': 'pron. pessoal', 'R': 'pron. relativo',
         'C': 'pron. recíproco', 'D': 'pron. demonstrativo', 'K': 'pron. correlativo', 'I': 'pron. interrogativo',
         'X': 'pron. indefinido', 'Q': 'pron. correlativo/interrog.', 'F': 'pron. reflexivo', 'S': 'pron. possessivo'}
INV = {'ADV': 'advérbio', 'CONJ': 'conjunção', 'COND': 'conjunção condicional', 'PRT': 'partícula',
       'PREP': 'preposição', 'INJ': 'interjeição', 'ARAM': 'palavra aramaica', 'HEB': 'palavra hebraica',
       'PRT-N': 'partícula negativa', 'PRT-I': 'partícula interrogativa', 'ADV-I': 'advérbio interrogativo',
       'ADV-N': 'advérbio negativo', 'CONJ-N': 'conjunção negativa', 'ADV-C': 'advérbio comparativo',
       'ADV-S': 'advérbio superlativo', 'COND-K': 'condicional + καί', 'CONJ-K': 'conjunção + καί'}

def _cng(s):
    out = []
    for i, ch in enumerate(s):
        if i == 0 and ch in CASO: out.append(CASO[ch])
        elif ch in NUM_G and i == 1: out.append(NUM_G[ch])
        elif ch in GEN_G: out.append(GEN_G[ch])
    return ' '.join(out)

def grego(cod):
    if not cod: return ''
    if cod in INV: return INV[cod]
    p = cod.split('-')
    if p[0] == 'V':
        m = re.match(r'(2?[A-Z])([A-Z])([A-Z])', p[1])
        if not m: return cod
        t, v, md = m.groups()
        d = f'verbo {TEMPO.get(t, t)} {VOZ.get(v, v)} {MODO.get(md, md)}'
        if len(p) > 2:
            x = p[2]
            if md == 'P': d += ' ' + _cng(x)
            else: d += f' {x[0]}ª p. ' + NUM_G.get(x[1:2], '')
        return d.strip()
    if p[0] == 'S' and len(p) > 1:
        x = p[1]
        d = f'pron. possessivo {x[0]}ª p. ' + NUM_G.get(x[1:2], '')
        return (d + (' ' + _cng(x[2:]) if len(x) > 2 else '')).strip()
    if p[0] in POS_G:
        d = POS_G[p[0]]
        for x in p[1:]:
            if x[:1] in '123': d += f' {x[0]}ª p.' + (' ' + _cng(x[1:]) if len(x) > 1 else '')
            elif x == 'PRI': d += ' indeclinável'
            elif x == 'NUI': d = 'numeral indeclinável'
            elif x == 'P': d += ' (nome próprio)'
            elif x == 'L': d += ' (lugar)'
            elif x == 'T': d += ' (título)'
            elif x == 'C': d += ' comparativo'
            elif x == 'S': d += ' superlativo'
            elif x[:1] in CASO: d += ' ' + _cng(x)
        return d.strip()
    return INV.get(cod, cod)

if __name__ == '__main__':
    for c in ['Hc/Vqw3ms', 'HR/Ncmpc', 'HTd/Vqrmpa', 'HNcfsc/Sp3fs', 'HVqcc', 'ANcmsd']:
        print(c, '->', hebraico(c))
    for c in ['V-PAI-3S', 'N-NSM-P', 'T-GSF', 'V-2AAP-NPM', 'P-1GS', 'CONJ', 'S-1SNSM', 'A-NSM-C', 'V-AAN']:
        print(c, '->', grego(c))
