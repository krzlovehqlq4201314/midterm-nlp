#!/usr/bin/env python
"""Clean raw TapTap reviews and save tokenized text."""
import re, jieba, pandas as pd, pathlib

# 1. 加载停用词
STOP = set(pathlib.Path("stopwords_zh.txt").read_text(encoding="utf-8").splitlines())

def clean_text(t: str) -> str:
    """只保留中英文及数字，分词并过滤停用词/单字"""
    t = re.sub(r"[^\u4e00-\u9fa5A-Za-z0-9]", " ", t)
    words = [w for w in jieba.cut(t) if w not in STOP and len(w) > 1]
    return " ".join(words)

# 2. 找 data/raw 下的 CSV
src = pathlib.Path("data/raw")
csv_files = list(src.glob("*.csv"))
if not csv_files:
    raise SystemExit("❌ No csv found in data/raw. Run download_taptap.py first.")

# 3. 读入并清洗 review 列
df = pd.read_csv(csv_files[0], encoding="utf-8")
df['clean'] = df['review'].astype(str).apply(clean_text)

# 4. 保存到 data/clean/comments.txt
out_dir = pathlib.Path("data/clean")
out_dir.mkdir(parents=True, exist_ok=True)
df['clean'].to_csv(out_dir / "comments.txt", index=False, header=False, encoding="utf-8")

print(f"✅ Saved cleaned text to {out_dir / 'comments.txt'}")
