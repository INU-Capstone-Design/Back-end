from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import text
from settings.database import engine

User = Namespace(
    name='User',
    description="유저 관리를 위한 API"
)

jwt_fields = User.model('JWT', {
    'Authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="eyJ0e~~~~~~~~~")
})

@User.route('')
class UserManage(Resource):
    # 유저 READ
    @User.expect(jwt_fields)
    @User.doc(responses={200: 'Success'})
    @User.doc(responses={500: 'User info get fail'})
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        try:
            stmt = text(f"SELECT u.username, u.name, u.email, g.workspaceid\
                        FROM Users as u\
                        LEFT JOIN Groupings as g ON u.username=g.username\
                        WHERE u.username='{username}'")
            
            with engine.begin() as conn:
                result = conn.execute(stmt).fetchall()

            return {
                "name": result[0]["name"],
                "email": result[0]["email"],
                "workspaceid": [i['workspaceid'] for i in result]
            }, 200
            
        except:
            return {
                "message": "User reading fail"
            }, 500