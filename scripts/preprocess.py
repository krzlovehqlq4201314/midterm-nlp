"""Clean raw TapTap reviews and save tokenized text."""
import re, jieba, pandas as pd, pathlib

STOP = set(pathlib.Path('stopwords_zh.txt').read_text(encoding='utf-8').splitlines())

def clean_text(t: str) -> str:
    t = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', ' ', t)
    words = [w for w in jieba.cut(t) if w not in STOP and len(w) > 1]
    return ' '.join(words)

src = pathlib.Path('data/raw')
csv_files = list(src.glob('*.csv'))
if not csv_files:
    raise SystemExit('❌ No csv found in data/raw. Run download_taptap.py first.')

df = pd.read_csv(csv_files[0])
df['clean'] = df['comment'].astype(str).apply(clean_text)

out_dir = pathlib.Path('data/clean')
out_dir.mkdir(parents=True, exist_ok=True)
df['clean'].to_csv(out_dir / 'comments.txt', index=False, header=False)
print(f'✅  Saved cleaned text to {out_dir / "comments.txt"}')
