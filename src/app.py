import joblib
from flask import Flask, jsonify, request, make_response, abort
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, create_refresh_token, jwt_refresh_token_required,
# )
import get_preference
import json

app = Flask(__name__)

# app.config["JWT_SECRET_KEY"] = "super-secret"
# jwt = JWTManager(app)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('app_server.log')
    app.logger.addHandler(file_handler)
    

@app.route("/")
def root():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/recommend/course", methods=['GET', 'POST'])
#@jwt_required()
def model():
    # input parameter - 입력값 str으로 %20 구분해서 연결한 값
    prediction = {}
    app.logger.info("request 이전")

    if request.method == "POST":
#        # 요청 정보 로깅 (f-string 사용)
        app.logger.info(f"Request: Method={request.method}, Path={request.path}, Headers={request.headers}")

        payload = request.get_json()
        if payload:
            app.logger.info(f"Payload: {payload}")
        else:
            app.logger.info("No JSON payload or unable to parse JSON")
        input_list = []
        for item in payload.values():
            input_list.extend(item)

        #input = request.args.get('input')
        if input_list:
            input = ' '.join(input_list)
            print(input)
            prediction = {'course_id':get_preference.recommend(user_input=input)}

    return make_response(prediction, 200)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
