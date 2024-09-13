import joblib
from flask import Flask, jsonify, request, make_response, abort
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, create_refresh_token, jwt_refresh_token_required,
# )
import get_preference

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
    if request.method == "POST":
#        user = get_jwt_identity()
        app.logger.info("request: ", request.method, request.path, request.headers)
        payload = request.get_json()
        app.logger.info(payload)
        
        input_list = payload['firstKeyword'].extend(payload['secondKeyword']).extend(payload['thirdKeyword'])
        #input = request.args.get('input')
        if input_list:
            input = ''.join(input_list.split('%20'))
            prediction = {'course_id':get_preference.recommend(user_input=input)}

        # else:
        #     prediction = {'course_id': ['2547514', '2547399', '2549270', '2547444', '2547535', '2549163', '2549164', '2549273', '2549170', '2508718']}
        
    return make_response(prediction, 200)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
