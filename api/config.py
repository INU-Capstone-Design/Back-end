import os

basedir = os.path.abspath(os.path.dirname(__file__))

USER="root"
PASSWORD="1234"
try:
    ADDR=os.environ["DATABASE"]
except:
    ADDR="localhost"
PORT=3306
NAME="minders"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{ADDR}:{PORT}/{NAME}?charset=utf8"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-secret"
    JWT_SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False
    NAME = "PROD"


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    NAME = "DEV"


class TestingConfig(Config):
    TESTING = True
    NAME = "TEST"
    
config = {"test": TestingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}