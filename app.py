from flask import Flask           # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api       # Api 구현을 위한 Api 객체 import
from api.user import User
from api.workspace import Workspace

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

api.add_namespace(User, '/users')
api.add_namespace(Workspace, '/workspaces')


if __name__ == "__main__":
    app.run(debug=True, port=5000)