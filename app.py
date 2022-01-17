import logging
import pymysql
from config import db
from flask import Flask, request, json  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

# ----회원 정보 관리----
# 회원 정보 전체 조회
@api.route('/users')
class AllUser(Resource):
    def get(self):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )

            # 테이블의 모든 정보 json으로 변환
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users"
                cur.execute("set name utf8")
                cur.execute(query)
                result = json.dumps(cur.fetchall())
            
            # 데이터가 있으면 그 데이터 반환
            # 없으면 없다고 반환
            if (result is not None):
                return result
            else:
                return {"result": "No User"}

        except:
            logging.error("DB connection failed")
            return {"result": "DB connect fail"}
        
        finally:
            connection.close()

# 회원 CREATE
@api.route('/users')
class CreateUser(Resource):
    def post(self):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )

            # 프론트에서 넘겨준 json 파일의 데이터 저장
            username = request.json.get('username') # 유저 ID
            password = request.json.get('password') # 비밀번호
            name = request.json.get('name')         # 이름
            email = request.json.get('email')       # 이메일주소

            # 중복 되는 회원 있는지 확인
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users WHERE username='{username}'"
                cur.execute(query)
                if cur.fetchone():
                    return {"result": "user is overlapping"}

            # 회원 정보 DB에 추가
            with connection.cursor() as cur:
                query = f"INSERT INTO Users(username, password, name, email) \
                          VALUES('{username}', '{password}', '{name}', '{email}')"
                cur.execute(query)
                connection.commit()

            return {'result': 'user create success'}

        except:
            logging.error("Error !!")
            return {"result": "fail"}
        
        finally:
            connection.close()
        
# 특정 회원 정보 READ
@api.route('/users/<int:userid>')
class ReadUser(Resource):
    def get(self, userid: int):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                database=db["database"],
                charset=db["charset"]
            )

            # userid로 DB에 쿼리 입력
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users WHERE userid={userid}"
                cur.execute(query)
                result = json.dumps(cur.fetchone(), ensure_ascii=False)
            
            # 검색되지 않으면 DB에 유저의 정보가 없는 것으로 반환
            # 있으면 그 유저의 정보 반환
            if (result != "null"):
                return result
            else:
                return {"result": "No User"}

        except:
            logging.error("DB connection failed")
            return {"result": "DB connect fail"}
        
        finally:
            connection.close()

# 회원 정보 업데이트
@api.route('/users')
class UpdateUser(Resource):
    def put(self):
        pass

# 회원 정보 삭제
@api.route('/users')
class DeleteUser(Resource):
    def delete(self):
        pass

# ----워크스페이스 관리----
# Workspace create REST API
@api.route('/workspaces')
class WorkspaceCreate(Resource):
    def post(self):
        pass

# Workspace read REST API
@api.route('/workspaces/<int:id>')
class WorkspaceRead(Resource):
    def get(self, id):
        pass

# Workspace update REST API
@api.route('/workspaces')
class WorkspaceUpdate(Resource):
    def put(self):
        pass

# Workspace delete REST API
@api.route('/workspaces')
class WorkspaceDelete(Resource):
    def delete(self):
        pass


if __name__ == "__main__":
    app.run(debug=True, port=5000)