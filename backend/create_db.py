from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from cred import username, password

# username shashi and password shashi is for test only

DATABASE_URL = "postgresql://"+username+":"+password+"@localhost: 5432/undata"

engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()


class RegionData(Base):
    __tablename__ = 'countries'
    id = Column('id', Integer, primary_key=True)
    country = Column('country', String)
    code = Column('code', Integer)
    year = Column('year', Integer)
    population = Column('population', Float)


class Union(Base):
    __tablename__ = 'unions'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    country_id = Column('country_id', Integer)


def main():
    if not database_exists(engine.url):

        print("Database Not Present. Creating.....")
        # Create DB undata
        create_database(engine.url)

        # Create Table countries
        Base.metadata.create_all(bind=engine)

        print("Database Created.....")

    else:
        print("Database already exists")


if __name__ == '__main__':
    main()
