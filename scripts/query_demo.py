#!/usr/bin/env python
import pickle, sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 1. 加载之前构建好的 TF-IDF 索引
vec, X, docs = pickle.load(open("outputs/tfidf_index.pkl", "rb"))

# 2. 获取用户输入的查询
q = " ".join(sys.argv[1:]) or input("Query> ")
q_vec = vec.transform([q])

# 3. 计算与所有文档的余弦相似度，取 Top-5
sims = cosine_similarity(q_vec, X).ravel()
top5 = np.argsort(-sims)[:5]

# 4. 打印结果
for idx in top5:
    print(f"{sims[idx]:.3f} | {docs[idx][:80]}")
