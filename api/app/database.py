from sqlalchemy import create_engine, MetaData, Table
from app.config import SQLALCHEMY_DATABASE_URI_FORMAT

engine = create_engine(SQLALCHEMY_DATABASE_URI_FORMAT, convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)