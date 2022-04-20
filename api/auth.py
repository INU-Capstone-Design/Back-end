import bcrypt, jwt
from flask import request
from database import engine, Users
from flask_restx import Resource, Namespace, fields

Auth = Namespace(
    name="Auth",
    description="사용자 인증을 위한 API"
)

user_fields = Auth.model('User', {  # Model 객체 생성
    'username': fields.String(description='Username', required=True, example="capstone"),
    'password': fields.String(description='Password', required=True, example="password")
})

user_fields_auth = Auth.inherit('User Auth', user_fields, {
    'name': fields.String(description='Name', required=False, example="HongGilDong"),
    'email': fields.String(description='Email', required=False, example="example@gmail.com")
})

jwt_fields = Auth.model('JWT', {
    'Authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="eyJ0e~~~~~~~~~")
})

@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(user_fields)
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
                'Authorization': jwt.encode({'userid': user['userid']}, "secret", algorithm="HS256") # str으로 반환하여 return
            }, 200

@Auth.route('/register')
class AuthRegister(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={404: 'User Not Found'})
    @Auth.doc(responses={500: 'Auth Failed'})
    def post(self):
        try:
            # 프론트에서 넘겨준 json 파일의 데이터 저장
            username = request.json['username'] # 유저 ID
            password = request.json['password'] # 비밀번호
            name = request.json['name']         # 이름
            email = request.json['email']       # 이메일주소
            

            # 중복 되는 회원 있는지 확인
            result = Users.select().where(Users.c.username == username).execute().first()
            if result:
                return {
                    "message": "User already exists."
                }, 404

            else:
            # 회원 정보 DB에 추가
                with engine.connect() as con:
                    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    con.execute(Users.insert(), username=username, password=password, name=name, email=email)
                    user = Users.select().where(Users.c.username == username).execute().first()
                    
                    return {
                        'Authorization': jwt.encode({'userid': user['userid']}, "secret", algorithm="HS256")
                    }, 200

        except:
            return {
                "message": "Auth Failed"
            }, 500

@Auth.route('/get')
class AuthGet(Resource):
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={404: 'Login Failed'})
    def get(self):
        header = request.headers.get('Authorization')  # Authorization 헤더로 담음
        if header == None:
            return {"message": "Please Login"}, 404
        data = jwt.decode(header, "secret", algorithms="HS256")
        return data, 200