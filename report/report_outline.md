# 전통 NLP 모델 비교 실험 보고서 (Outline)

**학생**: 이름 / 학번  
**날짜**: 2025‑04‑23

## 1. 실험 목적
- Chinese TapTap 리뷰에서 CBOW와 TF‑IDF 성능 비교

## 2. 데이터셋
- TapTap Reviews (320k rows)
- 전처리: 특수문자 제거, jieba 분할, 불용어 제거

## 3. 방법
### 3.1 CBOW
- gensim Word2Vec, window=5, vector_size=200
### 3.2 TF‑IDF
- scikit‑learn TfidfVectorizer, 1‑2gram

## 4. 평가 지표
- CBOW: Top‑1 / Top‑3 Accuracy, Perplexity
- TF‑IDF: Precision@5, MAP, 속도

## 5. 결과
| Model | Metric | Score |
|-------|--------|-------|
| CBOW | Top‑1 | _ |  
|  | Top‑3 | _ |
| TF‑IDF | P@5 | _ |

## 6. 결론
- 모델별 장단점
- 개선 아이디어
