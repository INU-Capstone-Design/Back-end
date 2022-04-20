import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://{USER}:{PASSWORD}@{ADDR}:{PORT}/{NAME}?charset=utf8")
SQLALCHEMY_DATABASE_URI_FORMAT = SQLALCHEMY_DATABASE_URI.format(
    USER="root",
    PASSWORD="1234",
    ADDR="127.0.0.1",
    PORT=3306,
    NAME="test"
)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_FORMAT


class ProductionConfig(Config):
    DEBUG = False
    NAME = "PROD"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    NAME = "DEV"


class TestingConfig(Config):
    TESTING = True
    NAME = "TEST"
    
config = {"test": TestingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}