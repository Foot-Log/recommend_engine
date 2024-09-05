import joblib
from flask import Flask, jsonify, request, make_response
import get_preference

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/api/course/recommend", methods=['GET', 'POST'])
def model():
    # input parameter - 입력값 str으로 %20 구분해서 연결한 값
    input = request.args.get('input')
    if input:
        input = ''.join(input.split('%20'))
        prediction = get_preference.recommend(user_input=input)
        print(prediction)
        # json 형식으로 변환
    else:
        prediction = {'산%이색체험%바다%계곡': ['2547514', '2547399', '2549270', '2547444', '2547535', '2549163', '2549164', '2549273', '2549170', '2508718']}
    
    return make_response(prediction, 200)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
