"""Confere o texto-base do NT extraído do TAGNT contra o SBLGNT oficial (contagem de palavras por versículo).
Uso: python3 scripts/conferir_nt.py <pasta fontes> <pasta SBLGNT data/sblgnt/text> [Livro...]
Diferenças vêm de versificação, crase ou palavras que o TAGNT registra como variante; devem ser vistas antes de traduzir."""
import sys, os, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regras import base_nt
AB = {'Matt':'Mat','Mark':'Mrk','Luke':'Luk','John':'Jhn','Acts':'Act','Rom':'Rom','1Cor':'1Co','2Cor':'2Co','Gal':'Gal',
      'Eph':'Eph','Phil':'Php','Col':'Col','1Thess':'1Th','2Thess':'2Th','1Tim':'1Ti','2Tim':'2Ti','Titus':'Tit','Phlm':'Phm',
      'Heb':'Heb','Jas':'Jas','1Pet':'1Pe','2Pet':'2Pe','1John':'1Jn','2John':'2Jn','3John':'3Jn','Jude':'Jud','Rev':'Rev'}
fontes, sbldir, *livros = sys.argv[1:]
sbl = {}
for f in glob.glob(os.path.join(sbldir, '*.txt')):
    for l in open(f, encoding='utf-8'):
        m = re.match(r'(\S+) (\d+):(\d+)\t(.*)', l.strip())
        if m: sbl[f'{AB[m.group(1)]}.{m.group(2)}.{m.group(3)}'] = [x for x in re.sub(r'[⸀⸁⸂⸃⸄⸅]', '', m.group(4)).split() if x != '—']
livros = livros or sorted(set(AB.values()))
tot = 0
for b in livros:
    for r, ws in json.load(open(os.path.join(fontes, f'{b}.json'), encoding='utf-8')).items():
        if r in sbl and len(base_nt(ws)[0]) != len(sbl[r]):
            tot += 1; print(r, 'TAGNT', len(base_nt(ws)[0]), 'SBLGNT', len(sbl[r]))
print(tot, 'versículo(s) com diferença')
