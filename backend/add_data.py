from sqlalchemy.orm import sessionmaker
import csv
from create_db import RegionData, Union
from create_db import engine


UNION_DICT = {
    "saarc": [
        4,
        50,
        64,
        356,
        462,
        524,
        586,
        144
    ],
    "asean": [
        96,
        116,
        360,
        418,
        458,
        104,
        608,
        702,
        764,
        704
    ]
}


Session = sessionmaker(bind=engine)
session = Session()


def add_population_data():

    print("Adding Population Data. Wait for few seconds.....")

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

    print("Country Data Added.....")


def add_union_data():

    print("Adding Union Data. Wait for few seconds.....")

    for union_entry in UNION_DICT:
        country_ids = UNION_DICT[union_entry]
        for country in country_ids:
            union = Union()
            union.name = union_entry
            union.country_id = country
            session.add(union)

    session.commit()
    session.close()

    print("Unioon Data Added.....")


def main():
    add_population_data()
    add_union_data()


if __name__ == '__main__':
    main()
