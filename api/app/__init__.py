from flask import Flask
from app import auth
from app.config import config

def create_app(env):
    app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
    app.config.from_object(config[env])
    
    app.register_blueprint(auth.bp)
    # app.register_blueprint(workspace.bp)

    return app