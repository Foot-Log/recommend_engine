# fit된 모델 불러오기
# 모델 바탕으로 선호도 계산하기

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import json
import os

def recommend(user_input, top_n=10):
    # 코사인 유사도 계산
    print()
    tfidf_matrix = np.load(os.getcwd()+'/src/model/matrix.npy')
    tfidfvectorizer = joblib.load(os.getcwd()+'/src/model/vectorizer.pkl')
    
    preference_vector = tfidfvectorizer.transform([user_input]).toarray().tolist()
    sim_scores = cosine_similarity(preference_vector, tfidf_matrix).flatten()
    
    # 유사도 점수를 기준으로 정렬하여 가장 유사한 문서의 인덱스 찾기
    top_indices = np.argsort(sim_scores)[::-1][:top_n].tolist()

    json_file_path = os.getcwd() + '/src/data/course.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    result_list = [json_data[str(idx)] for idx in top_indices if str(idx) in json_data]

    return result_list
