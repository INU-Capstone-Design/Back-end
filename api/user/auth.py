import bcrypt
from datetime import timedelta
from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
from settings.database import engine, Users

Auth = Namespace(
    name="Auth",
    description="사용자 인증을 위한 API"
)

user_fields_auth = Auth.model('User Auth', {  # Model 객체 생성
    'username': fields.String(description='Username', required=True, example="capstone"),
    'password': fields.String(description='Password', required=True, example="password")
})

user_fields = Auth.inherit('User', user_fields_auth, {
    'name': fields.String(description='Name', required=False, example="HongGilDong"),
    'email': fields.String(description='Email', required=False, example="example@example.com")
})

jwt_fields = Auth.model('JWT', {
    'authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="Bearer eyJ0e~~~~~~~~~")
})

@Auth.route('/login', methods=["POST"])
class AuthLogin(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={500: 'Register Failed'})
    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = Users.select().where(Users.c.username == username).execute().first()

        if not user:
            return {
                "message": "User Not Found"
            }, 404
        elif not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):  # 비밀번호 일치 확인
            return {
                "message": "Auth Failed"
            }, 500
        else:
            return {
                'Authorization': create_access_token(identity=username, expires_delta=timedelta(hours=3))
            }, 200

@Auth.route('/register', methods=["POST"])
class AuthRegister(Resource):
    @Auth.expect(user_fields)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={404: 'User Not Found'})
    @Auth.doc(responses={500: 'Auth Failed'})
    def post(self):
        try:
            # Request JSON 데이터 저장
            username = request.json['username']     # 유저 ID
            password = request.json['password']     # 비밀번호
            name = request.json['name']             # 이름
            email = request.json['email']           # 이메일주소
            
            # 중복 되는 회원 있는지 확인
            result = Users.select().where(Users.c.username == username).execute().first()
            if result:
                return {
                    "message": "User already exists."
                }, 404
            
            else:   # 회원 정보 DB에 추가
                with engine.begin() as conn:
                    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    conn.execute(Users.insert(), username=username, password=password, name=name, email=email)
                    return {
                        'Authorization': create_access_token(identity=username, expires_delta=timedelta(hours=3))
                    }, 200
            
        except:
            return {
                "message": "Auth Failed"
            }, 500

@Auth.route('', methods=["GET"])
class AuthGet(Resource):
    @Auth.expect(jwt_fields)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={404: 'Login Failed'})
    @jwt_required(optional=True)
    def get(self):
        identity = get_jwt_identity()
        
        if not identity:
            return {
                "message": "Please insert JWT in your header"
            }, 500
            
        return {"username": identity}, 200