"""Regras do texto-base, compartilhadas pelos scripts.
AT: Texto Massorético de Leningrado, seguindo o Qere (tipos L, Q, R do TAHOT); Ketiv e leituras da LXX vão para o aparato.
NT: SBL Greek New Testament (palavras marcadas SBL no TAGNT); se o versículo não existe no SBLGNT, usa-se o NA28."""
import re

def eds(s):
    return [re.sub(r'[»(].*', '', e) for e in s.split('+') if e]

VAR_RE = re.compile(r'(\S+) \((?:[a-z]=)?([^)]*)\).*? - ([GH]\d+[A-Za-z]?)=(\S+) in: (\S+)')

def variante_de(w, chave):
    """Se a edição `chave` lê outra palavra neste lugar (coluna de variantes de sentido do TAGNT), devolve essa palavra."""
    for parte in (w.get('var_sentido') or '').split(';'):
        m = VAR_RE.search(parte.strip())
        if m and chave in eds(m.group(5)):
            orig, translit, strong, morf, ed = m.groups()
            return dict(w, orig=orig, translit=translit, strong=strong, lema=re.sub(r'[A-Z]$', '', strong),
                        lema_grc='', morf=morf, edicoes=ed, var_sentido='', subst=w['orig'])
    return None

def base_nt(ws):
    tem_sbl = any('SBL' in eds(w['edicoes']) or variante_de(w, 'SBL') for w in ws)
    chave = 'SBL' if tem_sbl else 'NA28'
    base = []
    for w in ws:
        if chave in eds(w['edicoes']): base.append(w)
        else:
            v = variante_de(w, chave)
            if v: base.append(v)
    return base, chave

def base_at(ws):
    return [w for w in ws if w['tipo'][:1] in 'LQR']
