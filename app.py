import logging
import pymysql
from config import db
from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource, resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

# ----회원 정보 관리----
# 회원 CREATE
@api.route('/members')
class CreateUser(Resource):
    def post(self):
        username = request.json.get('username')
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
        
        # 중복 되는 회원 있는지 확인
        try:
            query = f"SELECT * FROM Users WHERE username='{username}'"
            cursor.execute(query)
            if cursor.fetchone():
                return {"result": "user is overlapping"}
        except:
            logging.error("Users select query fail")
            return {"result": "회원 중복 체크 실패"}

        # 회원 정보 DB에 추가
        try:
            query = f"INSERT INTO Users(userid, password, name, email) \
                  VALUES('{username}', '{password}', '{name}', '{email}')"
            cursor.execute(query)
            connection.commit()
            return {'result': 'user create success'}
        except:
            logging.error("Users insert query fail")
            return {"result": "회원 DB 추가 실패"}


# 특정 회원 정보 READ
@api.route('/members/<int:userid>')
class ReadUser(Resource):
    def get(self, userid):
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
            return {"result": "DB connect fail"}
        
        try:
            query = f"SELECT * FROM Users WHERE userid={userid}"
            cursor.execute(query)
        except:
            logging.error("Users select query failed")
            return {"result": "회원 정보 검색 실패"}

        result = cursor.fetchone()
        connection.close()
        cursor.close()

        if (result is not None):
            return {
                "result": "success",
                "userid": result[0],
                "username": result[1],
                "password": result[2],
                "name": result[3],
                "email": result[4],
                "create_time": str(result[5])
            }
        else:
            return {"result": "No User"}


# ----워크스페이스 관리----
# Workspace create REST API
@api.route('/workspace/create')
class WorkspaceCreate(Resource):
    def post(self):
        pass

# Workspace read REST API
@api.route('/workspace/read')
class WorkspaceRead(Resource):
    def post(self):
        pass

# Workspace update REST API
@api.route('/workspace/update')
class WorkspaceUpdate(Resource):
    def post(self):
        pass

# Workspace delete REST API
@api.route('/workspace/delete')
class WorkspaceDelete(Resource):
    def post(self):
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)