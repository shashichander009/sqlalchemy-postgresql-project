import json
import os
from sqlalchemy import and_, func, between
from add_data import session
from create_db import RegionData, Union


def get_union_list(name):

    union_qry = session.query(Union.country_id)
    union_qry = union_qry.filter(Union.name == name)

    return [i[0] for i in union_qry.all()]

# This function prepares a Bar Plot of India's population vs. years.


def india_data_process():
    india_data = {}  # dict to store values

    qry = session.query(RegionData.year, RegionData.population)

    qry = qry.filter(RegionData.country == "India")

    for row in qry.all():
        population_in_crores = round(row[1] / 10000, 2)
        india_data[row.year] = population_in_crores

    with open('./json/data1.json', 'w') as fs:
        fs.write(json.dumps(india_data))


# This function prepares the Bar Chart of population of ASEAN countries in 2014


def asean_data_process():

    asean_countries = get_union_list("asean")

    asean_data = {}

    qry = session.query(RegionData.country, RegionData.population)

    qry = qry.filter(and_(RegionData.year == 2014,
                          RegionData.code.in_(asean_countries)))

    for row in qry.all():
        population_in_crores = round(row[1] / 10000, 2)
        asean_data[row[0]] = population_in_crores

    with open('./json/data2.json', 'w') as fs:
        fs.write(json.dumps(asean_data))


# TOTAL population of SAARC countries over the past years


def saarc_data_process():

    saarc_countries = get_union_list("saarc")

    saarc_data = {}

    qry = session.query(RegionData.year, func.sum(
        RegionData.population))

    qry = qry.filter(RegionData.code.in_(saarc_countries))

    qry = qry.group_by(RegionData.year)

    qry = qry.order_by(RegionData.year)



    

    for row in qry.all():
        pop_in_crore = round(row[1] / 10000, 2)
        saarc_data[row[0]] = pop_in_crore

    with open('./json/data3.json', 'w') as fs:
        fs.write(json.dumps(saarc_data))


# Grouped Bar Chart - ASEAN population vs. years

def asean_group_data_process():

    asean_countries = get_union_list("asean")

    asean_grp_data = {}

    qry = session.query(RegionData.country,
                        RegionData.year,
                        RegionData.population)

    qry = qry.filter(
        and_(between(RegionData.year, 2011, 2015),
             RegionData.code.in_(asean_countries)))

    for row in qry.all():
        country = str(row[0])
        current_year = str(row[1])
        population_in_crores = round(float(row[2]) / 10000, 2)

        if asean_grp_data.get(country) is None:
            asean_grp_data[country] = {
                current_year: population_in_crores}
        else:
            nation_object = asean_grp_data[country]
            nation_object[current_year] = population_in_crores

    with open('./json/data4.json', 'w') as fs:
        fs.write(json.dumps(asean_grp_data))


def main():
    if not os.path.exists('json'):
        os.makedirs('json')

    india_data_process()
    asean_data_process()
    saarc_data_process()
    asean_group_data_process()

    print("JSON Prepared..")


if __name__ == '__main__':
    main()
