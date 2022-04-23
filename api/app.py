from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from config import config
from auth import Auth
from workspace import Workspace

app = Flask(__name__)
app.config.from_object(config["dev"])
jwt = JWTManager(app)
api = Api(app)

api.add_namespace(Auth, '/auth')
api.add_namespace(Workspace, '/workspace')



if __name__ == "__main__":
    app.run()