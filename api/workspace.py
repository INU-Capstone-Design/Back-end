import logging
import pymysql
from config import db
from flask import request, json  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Resource, Namespace  # Api 구현을 위한 Api 객체 import

Workspace = Namespace('Workspace')

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