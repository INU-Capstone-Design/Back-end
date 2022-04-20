from sqlalchemy import create_engine, MetaData, Table
from config import SQLALCHEMY_DATABASE_URI_FORMAT

engine = create_engine(SQLALCHEMY_DATABASE_URI_FORMAT, convert_unicode=True)
metadata = MetaData(bind=engine)

Users = Table('Users', metadata, autoload_with=engine)
Workspaces = Table('Workspaces', metadata, autoload_with=engine)
Groupings = Table('Groupings', metadata, autoload_with=engine)