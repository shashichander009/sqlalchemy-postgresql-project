# UN Population Data Analysis

Do you want to understand how the world population has grown over the years? This project will show you the world population growth story through beautiful charts.  

## Data

We are using data released by [United Nations]( https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv) to understand the population growth.

## Language and Libraries

This project is built with HTML, CSS, JavaScript and Python 3.7.4. For charting, we have used [highcharts]( https://www.highcharts.com/)


## Installation

clone this repo

create a virtual environment and activate it (if you need help,please refer to this [link]( https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/))

install all dependencies

```bash
pip install -r requirements.txt
```


## Usage

This project assumes that data is already there in the project. If you can't find "data.csv" in the root folder, download it from this [link]( https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv) and place it in the root folder with the name "data.csv"


Start by running create_db.py. This will create a database and load all csv values in PostgresSQL database

```bash
python3 create_db.py
```

Next Step, run the program. This will prepare JSON values for charting

```bash
python un_data_analysis.py
```

To view charts, open index.html 

Final step, run delete_db.py to remove database

```bash
python3 delete_db.py
```








## Deployment
No Deployment. Run this from your system