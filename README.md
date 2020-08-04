# UN Population Data Analysis

Do you want to understand how the world population has grown over the years? This project will show you the world population growth story through beautiful charts.  

## Data

We are using data released by [United Nations]( https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv) to understand the population growth.

## Language and Libraries

This project is built with 

Backend : Python 3.7.4
Frontend : HTML, CSS, JavaScript
Database : PostgresSQL
Charting : Highcharts


## Installation

clone this repo

create a virtual environment and activate it (if you need help,please refer to this [link]( https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/))

install all dependencies

```bash
pip install -r requirements.txt
```


## Usage

### DATABASE SETTING UP

Go to the "backend" folder 

First check if data.csv is present. If you can't find "data.csv" in the folder, download it from this [link]( https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv) and place it in the root folder with the name "data.csv"


Go to cred.py and change your username and password 

 To create our PostgreSQL database, run this command 

```bash
python3 create_db.py
```

### ADDING DATA TO OUR DATABASE 

To load all csv values in PostgresSQL database. Run this 

```bash
python3 add_data.py
```

### JSON DATA PREPARATION 

To prepare JSON values for charting, run the program. 

```bash
python3 un_data_analysis.py
```

### TO VIEW CHARTS 

To Serve the html, js and json files with python http.server we need to run this 

```bash
python3 -m http.server
```

Now go the root folder then to the frontened folder.

Open index.html 


### TO DELETE DATABASE 

Once you are done viewing charts, go to the backend folder and run 

```bash
python3 delete_db.py
```








## Deployment
No Deployment. Run this from your system