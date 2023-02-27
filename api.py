from typing import List
from fastapi import FastAPI

from db import DB
from models import Country , City


app = FastAPI()
db = DB("Country.db")

app.curr_id = 1
app.countries: List[Country] = []


@app.get("/")
def root():
    return "Hello"
    

@app.get("/countries")
def get_country():
    get_country_query = """
    SELECT * FROM country
    """
    data = db.call_db(get_country_query)
    countries = []
    for element in data:
        id, country_name, country_code = element
        countries.append(Country(id=id, country_name=country_name, country_code=country_code))
    print(data)
    # return app.countries
    return countries



@app.get("/country/{id}")
def get_countries_by_id(id: int):
    return "Returns a single task with id " + str(id)


@app.post("/add_country")
def add_country(country: Country):
    insert_query = """
    INSERT INTO country (country_name, country_code)
    VALUES ( ?, ? )
    """
    db.call_db(insert_query, country.country_name, country.country_code)
    # print(country)
    # country.id = app.curr_id
    # app.countries.append(country)
    # app.curr_id += 1
    return "Adds a task"
   
@app.delete("/delete_country/{id}")
def delete_country(id: int):

    delete_query = """
    DELETE FROM country WHERE id = ?
    """
    db.call_db(delete_query, id)
    # app.countries = list(filter(lambda x: x.id != id, app.countries))
    return True


@app.put("/update_country/{id}")
def update_country(id: int, new_country: Country):
    update_country_query = """
    UPDATE country
    SET country_name = ?, country_code = ?
    WHERE id = ?
    """

    db.call_db(update_country_query, new_country.country_name, new_country.country_code, id)
    # for country in app.countries:
    #     if country.id == id:
    #         country.country_name = new_country.country_name
    #         country.country_code = new_country.country_code
    return True
   