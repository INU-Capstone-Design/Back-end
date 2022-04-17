import logging
import pymysql
from .config import db
from flask import request, json  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Resource, Namespace  # Api 구현을 위한 Api 객체 import

User = Namespace('User')

# ----회원 정보 관리----
@User.route('')
class UserCreate(Resource):
    # 모든 회원 GET
    def get(self):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                port=db["port"],
                database=db["database"],
                charset=db["charset"]
            )

            # 모든 회원 정보 검색
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users"
                cur.execute(query)
                result = json.dumps(cur.fetchall(), ensure_ascii=False, default=str)

            return {
                'state': 1,
                'result': result
            }

        except:
            logging.error("모든 회원 검색 실패.")
            return {
                'state': 0,
                'result': 'Bad Request'
            }
        
        finally:
            connection.close()

    # 회원 CREATE
    def post(self):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                port=db["port"],
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
                    return {
                        'state': 0,
                        'result': "중복되는 회원이 존재합니다."
                        }

            # 회원 정보 DB에 추가
            with connection.cursor() as cur:
                query = f"INSERT INTO Users(username, password, name, email) \
                          VALUES('{username}', '{password}', '{name}', '{email}')"
                cur.execute(query)
                connection.commit()

            return {
                'state': 1,
                'result': '회원 생성 성공.'
            }

        except:
            logging.error("회원 생성 실패.")
            return {
                'state': 0,
                'result': 'Bad Request'
            }
        
        finally:
            connection.close()
        
@User.route('/<int:userid>')
class UserManage(Resource):
    # 회원 READ
    def get(self, userid: int):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                port=db["port"],
                database=db["database"],
                charset=db["charset"]
            )

            # userid로 DB에 쿼리 입력
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users WHERE userid={userid}"
                cur.execute(query)
                result = json.dumps(cur.fetchone(), default=str)
            
            # 검색되지 않으면 DB에 유저의 정보가 없는 것으로 반환
            # 있으면 그 유저의 정보 반환
            if (result != "null"):
                return {
                    'state': 1,
                    'result': result
                }
            else:
                return {
                    'state': 0,
                    'result': '회원이 존재하지 않습니다.'
                }

        except:
            logging.error("User GET Response failed.")
            return {
                'state': 0,
                'result': 'Bad Request'
            }
        
        finally:
            connection.close()

    # 회원 UPDATE
    def put(self, userid: int):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                port=db["port"],
                database=db["database"],
                charset=db["charset"]
            )
            
            # DB에 userid의 유저 있는지 확인
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users WHERE userid={userid}"
                cur.execute(query)
                result = cur.fetchone()
                
                if not result:
                    return {
                        'state': 0,
                        'result': '회원이 존재하지 않습니다.'
                    }

                else: # 프론트에서 넘겨준 json 파일의 데이터 저장
                    username = request.json.get('username', result[1]) # 유저 ID
                    password = request.json.get('password', result[2]) # 비밀번호
                    name = request.json.get('name', result[3])         # 이름
                    email = request.json.get('email', result[4])       # 이메일주소
            
            # DB에서 유저 정보 업데이트
            with connection.cursor() as cur:
                query = f"UPDATE Users \
                          SET username='{username}', password='{password}', name='{name}', email='{email}' \
                          WHERE userid={userid}"
                cur.execute(query)
                connection.commit()
            
            return {
                'state': 1,
                'result': '회원 정보 업데이트 성공.'
            }
        except:
            logging.error("회원 정보 업데이트 실패.")
            return {
                'state': 0,
                'result': 'Bad Request'
            }
        
        finally:
            connection.close()
    
    # 회원 DELETE
    def delete(self, userid: int):
        try:
            # DB connection 생성
            connection = pymysql.connect(
                user=db["user"],
                passwd=db["password"],
                host=db["host"],
                port=db["port"],
                database=db["database"],
                charset=db["charset"]
            )
            
            # DB에 userid의 유저 있는지 확인
            with connection.cursor() as cur:
                query = f"SELECT * FROM Users WHERE userid={userid}"
                cur.execute(query)
                result = cur.fetchone()
                
                if not result:
                    return {
                        'state': 0,
                        'result': '회원이 존재하지 않습니다.'
                    }
            
            # DB에서 유저 정보 업데이트
            with connection.cursor() as cur:
                query = f"DELETE FROM Users WHERE userid={userid}"
                cur.execute(query)
                connection.commit()
            
            return {
                'state': 1,
                'result': '회원 정보 삭제 성공.'
            }
        except:
            logging.error("회원 정보 삭제 실패.")
            return {
                'state': 0,
                'result': 'Bad Request'
            }
        
        finally:
            connection.close()