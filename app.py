import logging
import pymysql
from config import db
from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

# Login REST API
@api.route('/login')  # 데코레이터 이용, '/login' 경로에 클래스 등록
class Login(Resource):
    def post(self):
        userid = request.json.get('userid')
        password = request.json.get('password')

        # DB connection 생성
        try:
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )
            cursor = connection.cursor()
        except:
            logging.error("DB connection failed")
            return {"result": "DB 연결 실패"}
        
        query = f"SELECT * FROM Users WHERE userid='{userid}' and password='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if (result is not None):
            return {"result": "success"}
        else:
            return {"result": "fail"}

# Overlap checking REST API
@api.route('/login/<string:username>')
class OverlapCheck(Resource):
    def get(self, username: str):
        # DB connection 생성
        try:
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )
            cursor = connection.cursor()
        except:
            logging.error("DB connection failed")
            return {"result": "DB 연결 실패"}
        
        query = f"SELECT * FROM Users WHERE username='{username}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if (result is not None):
            return {"result": "overlap"}
        else:
            return {"result": "No overlap"}

# Register REST API
@api.route('/register')
class Register(Resource):
    def post(self):
        userid = request.json.get('userid')
        password = request.json.get('password')
        name = request.json.get('name')
        email = request.json.get('email')

        # DB connection 생성
        try:
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )
            cursor = connection.cursor()
        except:
            logging.error("DB connection failed")
            return {"result": "DB 연결 실패"}
        
        query = f"INSERT INTO Users(userid, password, name, email) \
                  VALUES('{userid}', '{password}', '{name}', '{email}')"
        
        # query 실행
        try:
            cursor.execute(query)
            # query 성공 시 commit으로 DB에 반영
            connection.commit()
            return {'result': 'success'}
        except:
            logging.error("INSERT fail")
            return {"result": "fail"}


@api.route('/workspace/create')
class WorkspaceCreate(Resource):
    def post(self):
        pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)