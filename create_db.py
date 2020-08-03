from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import csv

# username shashi and password shashi is for test only

DATABASE_URL = "postgresql://shashi:shashi@localhost:5432/undata"


engine = create_engine(DATABASE_URL)

Base = declarative_base()


class RegionData(Base):
    __tablename__ = 'country'
    id = Column('id', Integer, primary_key=True)
    country = Column('region', String)
    code = Column('code', Integer)
    year = Column('year', Integer)
    population = Column('population', String)


Session = sessionmaker(bind=engine)

session = Session()


def main():
    if not database_exists(engine.url):

        print("Database Not Present. Creating.....")

        create_database(engine.url)
        Base.metadata.create_all(bind=engine)

        with open('data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                regiondata = RegionData()
                regiondata.country = line[0]
                regiondata.code = line[1]
                regiondata.year = line[2]
                regiondata.population = str(line[3])
                session.add(regiondata)
        session.commit()
        session.close()

        print("Database Created.....")

    else:
        print("Database already exists")


if __name__ == '__main__':
    main()
