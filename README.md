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

---

## Tech Stack

| Role                 | Stack                                                                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Framework            | ![Scikit-Learn](https://img.shields.io/badge/scikit%20learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white) |
| Programming Language | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)                                                                                                                       |
| Version Control      | ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)             |
| Deploy               | ![Deploy](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=for-the-badge)                                                                                                                          |
