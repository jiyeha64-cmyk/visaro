"""src/ 의 템플릿·데이터·번역을 합쳐 index.html 을 만듭니다.  사용: python build.py"""
import glob, pathlib
s = pathlib.Path('src')
t = (s/'template.html').read_text(encoding='utf-8')
d = ''.join(pathlib.Path(f).read_text(encoding='utf-8') for f in sorted(glob.glob('src/data/0*.js')))
t = t.replace('/*DATA*/', d).replace('/*STR*/', (s/'strings.json').read_text(encoding='utf-8')).replace('/*TR*/', (s/'tr.json').read_text(encoding='utf-8'))
pathlib.Path('index.html').write_text(t, encoding='utf-8')
print('index.html 생성 완료')
