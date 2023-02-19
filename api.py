from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from db import DB
from models import Country , City


app = FastAPI()
db = DB("Country.db")

# app.curr_id = 1 
# app.country: List[Country] = []


@app.get("/")
def root():
    return "Hello"
    
@app.get("/country")
def get_country():
    get_country_query = """
    SELECT * FROM country
    """
    data = db.call_db(get_country_query)
    country = []
    for element in data:
        id, country_name, country_code = element
        country.append(Country(id=id, country_name=country_name, country_code=country_code))
    print(data)
    return country

@app.get("/city")
def get_city():
    get_city_query = """
    SELECT * FROM city
    """
    data = db.call_db(get_city_query)
    city = []
    for element in data:
        id, city_name, country_id = element
        city.append(City(id=id, city_name=city_name, country_id=country_id))
    print(data)
    return city

# @app.get("/country/{id}")
# def get_country(id: int):
#     return "Returns a single task with id " + str(id)

@app.get("/countries/{id}")
def get_countries_by_id(id: int):
    # Construct the SELECT query to retrieve the country data
    query = "SELECT * FROM country WHERE id = " + str(id)

    # Execute the query and retrieve the data from the database
    data = db.call_db(query)

    if data:
        # If the country is found, return it as a JSON response
        return {"id": data[0][0], "country_name": data[0][1], "country_code": data[0][2]}
    else:
        # If the country is not found, return a 404 Not Found error
        return {"error": "Country not found"}

@app.get("/cities/{id}")
def get_cities_by_id(id: int):
    # Construct the SELECT query to retrieve the city data
    query = "SELECT * FROM city WHERE id = " + str(id)

    # Execute the query and retrieve the data from the database
    data = db.call_db(query)

    if data:
        # If the city is found, return it as a JSON response
        return {"id": data[0][0], "city_name": data[0][1], "country_id": data[0][2]}
    else:
        # If the city is not found, return a 404 Not Found error
        return {"error": "City not found"}
    
# @app.post("/add_country")
# def add_country(country: Country):
#     insert_query = """
#     INSERT INTO country (country_name, country_code)
#     VALUES ( ?, ? )
#     """
#     db.call_db(insert_query, country.country_name, country.country_code)

#     print(country)
#     # country.id = app.curr_id
#     # app.country.append(country)
#     # app.curr_id += 1
#     return "Adds a task"

@app.post("/add_country")
def add_country(country: Country):
    insert_query = """
    INSERT INTO country (country_name, country_code)
    VALUES ( ?, ? )
    """
    db.call_db(insert_query, country.country_name, country.country_code)

    select_query = """
    SELECT * FROM country WHERE country_name = ? AND country_code = ?
    """
    data = db.call_db(select_query, country.country_name, country.country_code)

    print(country)
    return data

# @app.delete("/delete_country/{id}")
# def delete_country(id: int):
#     delete_query = """
#     DELETE FROM country WHERE id = ?
#     """
#     db.call_db(delete_query, id)
#     # app.country = list(filter(lambda x: x.id != id, app.country))
#     return True

@app.delete("/delete_country/{id}")
def delete_country(id: int):
    select_query = """
    SELECT * FROM country WHERE id = ?
    """
    data = db.call_db(select_query, id)
    delete_query = """
    DELETE FROM country WHERE id = ?
    """
    db.call_db(delete_query, id)
    return data

# @app.put("/update_country/{id}")
# def update_country(id: int, new_country: Country):
#     update_country_query = """
#     UPDATE country
#     SET country_name = ?, country_code = ?
#     WHERE id = ?
#     """

#     db.call_db(update_country_query, new_country.country_name, new_country.country_code, id)
#     # for country in app.country:
#     #     if country.id == id:
#     #         country.country_name = new_country.country_name
#     #         country.country_code = new_country.country_code
#     return TRUE


@app.put("/update_country/{id}")
def update_country(id: int, new_country: Country):
    update_country_query = """
    UPDATE country
    SET country_name = ?, country_code = ?
    WHERE id = ?
    """

    # Execute the update query to update the country in the database
    db.call_db(update_country_query, new_country.country_name, new_country.country_code, id)

    # Retrieve the updated country data from the database
    get_country_query = "SELECT * FROM country WHERE id = " + str(id)
    data = db.call_db(get_country_query)

    if data:
        # If the country is found, construct a new Country object and return it as a JSON response
        id, country_name, country_code = data[0]
        updated_country = Country(id=id, country_name=country_name, country_code=country_code)
        print(data)
        return updated_country
    else:
        # If the country is not found, return a 404 Not Found error
        print( "Country not found")
        return {"error": "Country not found"}
