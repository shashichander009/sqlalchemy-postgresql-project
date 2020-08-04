from sqlalchemy.orm import sessionmaker
import csv
from create_db import RegionData
from create_db import engine


Session = sessionmaker(bind=engine)
session = Session()


def main():
    print("Adding Data. Wait for few seconds.....")
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            regiondata = RegionData()
            regiondata.country = line[0]
            regiondata.code = line[1]
            regiondata.year = line[2]
            regiondata.population = line[3]
            session.add(regiondata)

    session.commit()
    session.close()
    print("Data Added.....")


if __name__ == '__main__':
    main()
