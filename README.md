# Midterm NLP Assignment

**Title**: Traditional NLP Models on TapTap Game Reviews  
Author: _Your Name_ (Student ID)

## Project Brief
We compare two classic NLP methods—**CBOW** and **TF‑IDF**—on a Chinese game‑review corpus from TapTap (≈320k rows).
The goal is to evaluate:
1. Center‑word prediction accuracy (CBOW)
2. Similar‑review ranking quality (TF‑IDF)

## Installation
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run
```bash
# 1. Download raw data (needs Kaggle API key)
python scripts/download_taptap.py

# 2. Clean & tokenize
python scripts/preprocess.py

# 3. Open notebooks and run cells in order:
#    EDA → train_cbow → eval_cbow → tfidf_rank → error_analysis
```

## Key Features
* Automated data download & preprocessing
* CBOW word‑embedding training with gensim
* TF‑IDF sparse index & cosine‑similarity search
* Jupyter notebooks for reproducibility
* Unit test for text cleaner

## License
MIT
