from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from config import config
from auth import Auth
from workspace import Workspace
from user import User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(config["dev"])
jwt = JWTManager(app)
api = Api(app)

api.add_namespace(Auth, '/auth')
api.add_namespace(Workspace, '/workspace')
api.add_namespace(User, '/user')

if __name__ == "__main__":
    app.run(port=80)