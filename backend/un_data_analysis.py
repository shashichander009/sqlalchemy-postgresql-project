import json
from add_data import session
from create_db import RegionData
from sqlalchemy import and_
from sqlalchemy import func

ASEAN_COUNTRIES = [
    'Brunei Darussalam',
    'Cambodia',
    'Indonesia',
    "Lao People's Democratic Republic",
    'Malaysia',
    'Myanmar',
    'Philippines',
    'Singapore',
    'Thailand',
    'Viet Nam',
]

SAARC_COUNTRIES = [
    'Afghanistan',
    'Bangladesh',
    'Bhutan',
    'India',
    'Maldives',
    'Nepal',
    'Pakistan',
    'Sri Lanka',
]


# PROBLEM NO 1
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


# PROBLEM NO 2
# This function prepares the Bar Chart of population of ASEAN countries in 2014
# ASEAN is a collection of South East Asian countries.

def asean_data_process():
    asean_data = {}

    qry = session.query(RegionData.country, RegionData.population)

    qry = qry.filter(and_(RegionData.year == 2014,
                          RegionData.country.in_(ASEAN_COUNTRIES)))

    for row in qry.all():
        population_in_crores = round(row[1] / 10000, 2)
        asean_data[row[0]] = population_in_crores

    with open('./json/data2.json', 'w') as fs:
        fs.write(json.dumps(asean_data))


# PROBLEM NO 3
# TOTAL population of SAARC countries over the past years
# In this case for each year we have to calculate total
# population of all SAARC countries.
# Then plot a BAR CHART of Total SAARC population vs. year.

def saarc_data_process():

    saarc_data = {}

    qry = session.query(RegionData.year, func.sum(
        RegionData.population))

    qry = qry.filter(RegionData.country.in_(SAARC_COUNTRIES))

    qry = qry.group_by(RegionData.year)

    qry = qry.order_by(RegionData.year)

    for row in qry.all():
        pop_in_crore = round(row[1] / 10000, 2)
        saarc_data[row[0]] = pop_in_crore

    with open('./json/data3.json', 'w') as fs:
        fs.write(json.dumps(saarc_data))


# PROBLEM NO 4
# Grouped Bar Chart - ASEAN population vs. years
# We will plot population of ASEAN countries as
# groups over the years 2011 - 2015.

def asean_group_data_process():
    asean_grp_data = {}
    # In this dictionary we will store data of asean countries population
    # The key will be concat of Year + Country
    # The value will be population

    qry = session.query(RegionData.country,
                        RegionData.year,
                        RegionData.population)

    qry = qry.filter(
        and_(RegionData.year >= 2011, RegionData.year <= 2015,
             RegionData.country.in_(ASEAN_COUNTRIES)))

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
    india_data_process()
    asean_data_process()
    saarc_data_process()
    asean_group_data_process()
    print("JSON Prepared..")


if __name__ == '__main__':
    main()
