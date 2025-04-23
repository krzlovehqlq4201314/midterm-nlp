#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
预处理 TapTap Review 数据：
1. 读取 data/raw/*.csv
2. 仅保留 'review' 列（评论正文）
3. 清洗文本：去特殊符号 → jieba 分词 → 去停用词
4. 保存到 data/clean/comments.txt（一行一条）
"""
import re
import jieba
import pandas as pd
import pathlib

# ========= 配置 ========= #
SRC_DIR   = pathlib.Path("data/raw")
OUT_DIR   = pathlib.Path("data/clean")
TEXT_COL  = "review"            # <-- 这里改成真正的列名
STOP_FILE = pathlib.Path("stopwords_zh.txt")
# ======================== #

# 1. 读取 CSV
csv_files = list(SRC_DIR.glob("*.csv"))
if not csv_files:
    raise SystemExit("❌  data/raw 目录下未找到 CSV 文件，请先下载数据")
csv_path = csv_files[0]
df = pd.read_csv(csv_path)

if TEXT_COL not in df.columns:
    raise SystemExit(f"❌  列名 '{TEXT_COL}' 不存在！实际列: {list(df.columns)}")

# 2. 预处理函数
STOP = set(STOP_FILE.read_text(encoding="utf-8").splitlines())

def clean_text(text: str) -> str:
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9]", " ", str(text))
    words = [w for w in jieba.cut(text) if w not in STOP and len(w) > 1]
    return " ".join(words)

# 3. 执行清洗
df = df.dropna(subset=[TEXT_COL])           # 去掉缺失
df["clean"] = df[TEXT_COL].apply(clean_text)

# 4. 保存
OUT_DIR.mkdir(parents=True, exist_ok=True)
out_file = OUT_DIR / "comments.txt"
df["clean"].to_csv(out_file, index=False, header=False, encoding="utf-8")

print(f"✅  Saved cleaned text to {out_file}")
