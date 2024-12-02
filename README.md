## Directory Structure

```
📦src
 ┣ 📂data
 ┃ ┣ 📜course.json
 ┃ ┗ 📜data_with_contentid.csv
 ┣ 📂model
 ┃ ┣ 📜matrix.npy # 각 코스의 vector representation을 저장합니다.
 ┃ ┗ 📜vectorizer.pkl # 사용자의 선호도를 vectorize하는 모델입니다.
 ┣ 📂modeling
 ┃ ┗ 📜tf-idf.ipynb
 ┣ 📜app.py
 ┣ 📜get_preference.py
 ┗ 📜wsgi.py
```
