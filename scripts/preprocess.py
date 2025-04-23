#!/usr/bin/env python
"""Clean raw TapTap reviews and save tokenized text."""

import re, jieba, pandas as pd, pathlib

# 配置
SRC_DIR = pathlib.Path("data/raw")
OUT_DIR = pathlib.Path("data/clean")
TEXT_COL = "review"
STOP_FILE = pathlib.Path("stopwords_zh.txt")

# 加载停用词
STOP = set(STOP_FILE.read_text(encoding="utf-8").splitlines())

def clean_text(t: str) -> str:
    t = re.sub(r"[^\u4e00-\u9fa5A-Za-z0-9]", " ", t)
    return " ".join(w for w in jieba.cut(t) if w not in STOP and len(w) > 1)

# 1. 找到 CSV
csv_files = list(SRC_DIR.glob("*.csv"))
if not csv_files:
    raise SystemExit("❌ No csv found in data/raw. Run download_taptap.py first.")
df = pd.read_csv(csv_files[0], encoding="utf-8")

# 2. 清洗 TEXT_COL 列
if TEXT_COL not in df.columns:
    raise SystemExit(f"❌ Column '{TEXT_COL}' not found! Available: {list(df.columns)}")
df = df.dropna(subset=[TEXT_COL])
df["clean"] = df[TEXT_COL].astype(str).apply(clean_text)

# 3. 保存结果
OUT_DIR.mkdir(parents=True, exist_ok=True)
out_file = OUT_DIR / "comments.txt"
df["clean"].to_csv(out_file, index=False, header=False, encoding="utf-8")
print(f"✅ Saved cleaned text to {out_file}")
