from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/login')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        if (username == "mungiyo" and password == "1234"):
            return {"result": "success", "username": username, "password": password}
        else:
            return {"result": "fail"}

if __name__ == "__main__":
    app.run(debug=True, port=80)