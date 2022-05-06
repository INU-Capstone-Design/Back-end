from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import text
from settings.database import engine

User = Namespace(
    name='User',
    description="유저 관리를 위한 API"
)

jwt_fields = User.model('JWT', {
    'authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="Bearer eyJ0e~~~~~~~~~")
})

@User.route('')
class UserManage(Resource):
    # 유저 READ
    @User.expect(jwt_fields)
    @User.doc(responses={200: 'Success'})
    @User.doc(responses={500: 'User info get fail'})
    @jwt_required(optional=True)
    def get(self):
        identity = get_jwt_identity()
        
        if not identity:
            return {
                "message": "Please insert JWT in your header"
            }, 500
        
        try:
            stmt = text(f"SELECT u.username, u.name, u.email, g.workspaceid\
                        FROM Users as u\
                        LEFT JOIN Groupings as g ON u.username=g.username\
                        WHERE u.username='{identity}'")
            
            with engine.begin() as conn:
                result = conn.execute(stmt).fetchall()

            return {
                "name": result[0]["name"],
                "email": result[0]["email"],
                "workspaceid": [i['workspaceid'] for i in result]
            }, 200
            
        except:
            return {
                "message": "유저를 찾는데 실패하였습니다."
            }, 500