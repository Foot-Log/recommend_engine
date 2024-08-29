import joblib
from flask import Flask, jsonify, request, make_response
import get_preference

app = Flask(__name__)

@app.route("/api/course/recommend", methods=['GET'])
def model():
    # input parameter - 입력값 str으로 %20 구분해서 연결한 값
    input = request.args.get('input')
    if input:
        input = ''.join(input.split('%20'))
        prediction = get_preference.recommend(user_input=input)
        # json 형식으로 변환
    else:
        prediction = {}
    return make_response(prediction, 200)

if __name__=='__main__':
    app.run(debug=True)