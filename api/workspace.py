import bcrypt, jwt
from flask import request
from database import engine, Users
from flask_restx import Resource, Namespace, fields

Workspace = Namespace(
    name='Workspace',
    description="워크스페이스 관리를 위한 API"
)

# ----워크스페이스 관리----
@Workspace.route('')
class WorkspaceCreate(Resource):
    # 워크스페이스 CREATE
    def post(self):
        pass

@Workspace.route('/<int:id>')
class WorkspaceManage(Resource):
    # 워크스페이스 READ
    def get(self, workspaceid: int):
        pass
    
    # 워크스페이스 UPDATE
    def put(self, workspaceid: int):
        pass
    
    # 워크스페이스 DELETE
    def delete(self, workspaceid: int):
        pass