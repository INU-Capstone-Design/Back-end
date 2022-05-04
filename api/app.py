import os
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from settings.config import config
from user.auth import Auth
from workspace.workspace import Workspace
from user.user import User
from model.predict import Model
from flask_cors import CORS

try:
    CONFIG = os.environ["CONFIG"]
    HOST = os.environ["HOST"]
    PORT = int(os.environ["PORT"])
except:
    CONFIG = "dev"
    HOST = "localhost"
    PORT = 80

app = Flask(__name__)
CORS(app)
app.config.from_object(config[CONFIG])
jwt = JWTManager(app)
api = Api(app)

api.add_namespace(Auth, '/auth')
api.add_namespace(Workspace, '/workspace')
api.add_namespace(User, '/user')
api.add_namespace(Model, '/predict')

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)