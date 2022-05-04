from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import text
from settings.database import engine, Workspaces, Groupings

Workspace = Namespace(
    name='Workspace',
    description="워크스페이스 관리를 위한 API"
)

workspace_fields = Workspace.model('Workspace', {  # Model 객체 생성
    'title': fields.String(description='Title', required=True, example="example"),
    'mindmap': fields.String(description='Mindmap info', required=True, example="example HTML, JSON, XML, ...")
})

jwt_fields = Workspace.model('JWT', {
    'Authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="eyJ0e~~~~~~~~~")
})

# ----워크스페이스 관리----
@Workspace.route('')
class WorkspaceCreate(Resource):
    # 워크스페이스 CREATE
    @Workspace.expect(workspace_fields)
    @Workspace.doc(responses={200: 'Success'})
    @Workspace.doc(responses={500: 'Create fail'})
    @jwt_required()
    def post(self):
        try:
            title = request.json['title']
            mindmap = request.json['mindmap']
            master = get_jwt_identity()

            with engine.begin() as conn:
                conn.execute(Workspaces.insert(), master=master, title=title, mindmap=mindmap)
                workspaceid = conn.execute(text('SELECT LAST_INSERT_ID()')).fetchone()[0]
                conn.execute(Groupings.insert(), username=master, workspaceid=workspaceid)
            
            return {
                    "message": "Workspace create success"
                }, 200
                
        except:
            return {
                    "message": "Workspace create fail"
                }, 500
        

@Workspace.route('/<int:workspaceid>')
class WorkspaceManage(Resource):
    # 워크스페이스 READ
    @Workspace.expect(jwt_fields)
    @Workspace.doc(responses={200: 'Success'})
    @Workspace.doc(responses={500: 'Search fail'})
    @jwt_required()
    def get(self, workspaceid: int):
        result = Workspaces.select().where(Workspaces.c.workspaceid==workspaceid).execute().first()
        if result:
            return {
                "master": result["master"],
                "title": result["title"],
                "mindmap": result["mindmap"]
            }, 200
        else:
            return {
                "message": f"Failed to search workspace={workspaceid}"
            }, 500
    
    # 워크스페이스 UPDATE
    @Workspace.expect(workspace_fields)
    @Workspace.doc(responses={200: 'Success'})
    @Workspace.doc(responses={500: 'Update fail'})
    @jwt_required()
    def put(self, workspaceid: int):
        try:
            title = request.json["title"]
            mindmap = request.json["mindmap"]
            Workspaces.update().where(Workspaces.c.workspaceid==workspaceid).values(title=title, mindmap=mindmap).execute()
            return {
                "message": "Workspace update success"
            }, 200
            
        except:
            return {
                "message": "Workspace update fail"
            }, 500
    
    # 워크스페이스 DELETE
    @Workspace.expect(jwt_fields)
    @Workspace.doc(responses={200: 'Success'})
    @Workspace.doc(responses={500: 'Delete fail'})
    @jwt_required()
    def delete(self, workspaceid: int):
        try:
            Workspaces.delete().where(Workspaces.c.workspaceid==workspaceid).execute()
            return {
                "message": "Workspace delete success"
            }, 200
            
        except:
            return {
                "message": "Workspace delete fail"
            }, 500