import logging
import pymysql
import sys
from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

@api.route('/login')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class Login(Resource):
    def post(self):
        # DB 정보
        host = "localhost"
        port = 3306
        database = "mind_db"
        username = "mungiyo"
        password = "102489"

        # DB connection 생성
        try:
            conn = pymysql.connect(
                host=host,
                user=username,
                passwd=password,
                database=database,
                port=port,
                use_unicode=True,
                charset='utf8'
            )
            cursor = conn.cursor
        except:
            logging.error("DB connection failed")
            sys.exit()
        

        userid = request.form['username']
        password = request.form['password']

        query = f"SELECT * FROM Users WHERE userid='{userid}' and password='{password}'"
        # query = f"SELECT * FROM Users"
        cursor.execute(query)
        result = cursor.fetchone()

        if (result is not None):
            return {"result": "success"}
        else:
            return {"result": "fail"}

if __name__ == "__main__":
    app.run(debug=True, port=80)