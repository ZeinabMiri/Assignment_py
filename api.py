from typing import List
from fastapi import FastAPI


from db import DB
from models import Country , City


app = FastAPI()
db = DB("Country.db")



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



@app.get("/countries/{id}")
def get_countries_by_id(id: int):
    
    query = "SELECT * FROM country WHERE id = " + str(id)

    data = db.call_db(query)

    if data:
        return {"id": data[0][0], "country_name": data[0][1], "country_code": data[0][2]}
    else: 
        return {"error": "Country not found"}


@app.get("/cities/{id}")
def get_cities_by_id(id: int):
  
    query = "SELECT * FROM city WHERE id = " + str(id)

    data = db.call_db(query)

    if data:
        return {"id": data[0][0], "city_name": data[0][1], "country_id": data[0][2]}
    else:
        return {"error": "City not found"}


@app.get("/countries/name/{name}")
def get_countries_by_name(name: str):
   
    query = f"""SELECT * FROM country WHERE country_name = '{name}'"""

    data = db.call_db(query)

    if data:
        return {"id": data[0][0], "country_name": data[0][1], "country_code": data[0][2]}
    else:
        return {"error": "Country not found"}



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


@app.post("/add_city")
def add_city(city: City):
    insert_query = """
    INSERT INTO city (city_name, country_id)
    VALUES ( ?, ? )
    """
    db.call_db(insert_query, city.city_name, city.country_id)

    select_query = """
    SELECT * FROM city WHERE city_name = ? AND country_id = ?
    """
    data = db.call_db(select_query, city.city_name, city.country_id)

    print(city)
    return data


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


@app.put("/update_country/{id}")
def update_country(id: int, new_country: Country):
    update_country_query = """
    UPDATE country
    SET country_name = ?, country_code = ?
    WHERE id = ?
    """

    db.call_db(update_country_query, new_country.country_name, new_country.country_code, id)

    get_country_query = "SELECT * FROM country WHERE id = " + str(id)
    data = db.call_db(get_country_query)

    if data:
        id, country_name, country_code = data[0]
        updated_country = Country(id=id, country_name=country_name, country_code=country_code)
        print(data)
        return updated_country
    else:
        print( "Country not found")
        return {"error": "Country not found"}
