# fit된 모델 불러오기
# 모델 바탕으로 선호도 계산하기

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import os

def recommend(user_input, top_n=10):
    # 코사인 유사도 계산

    tfidfvectorizer = joblib.load('model/vectorizer.pkl')
    preference_vector = tfidfvectorizer.transform([user_input]).toarray().tolist()
    #sim_scores = cosine_similarity(preference_vector, tfidf_matrix).flatten()
    
    # 유사도 점수를 기준으로 정렬하여 가장 유사한 문서의 인덱스 찾기
    #top_indices = np.argsort(sim_scores)[::-1][:top_n]
    user = {user_input : preference_vector}
    return user
