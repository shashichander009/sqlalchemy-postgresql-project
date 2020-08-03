from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database
from create_db import DATABASE_URL

engine = create_engine(DATABASE_URL)

if database_exists(engine.url):
    drop_database(engine.url)


if not database_exists(engine.url):
    print("Database has been deleted.....")
