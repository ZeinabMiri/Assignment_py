from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from db import DB
from models import Country
from models import City
import json

app = FastAPI()
db = DB("Country_api.db")




# @app.get("/")
# # async def read_root():
#     with open("seed.json","r") as f:
#             seed_data = f.read()
#             print(seed_data)
#             seed_data = json.load(f)
#             print(seed_data)
#     db = DB ("Country_api.db")
#     for table, records in seed_data.items():
#         for record in records:
#             db.insert(table= table, fields=record)
#     return {"Ddatabase seed successfully"}


@app.get("/")
def root():
    return("hello")


@app.get("/countries")
def get_countries():
    data = db.get(table="country")
    return data


@app.post("/create_country")
def create_country(country: Country):
    print(country)
    db.insert(table="country", fields={"country_name": country.country_name, "country_code": country.country_code})
    return "Successfully created"

@app.post("/create_city")
def create_city(city: City):
    print(city)
    db.insert(table="city", fields={"city_name": city.city_name, "country_id": str(city.country_id)})
    return "Successfully created"

@app.get("/countries/{id}")
def get_countries_by_id(id: int):
    data = db.get(table="country", where=("id", str(id)))
    return data




@app.get("/cities/{id}")
def get_cities_by_id(id: int):
    data = db.get(table="city", where=("id", str(id)))
    return data

@app.get("/cities")
def get_cities():
    data = db.get(table="city")
    return data



@app.delete("/delete_country/{id}")
def delete_country(id):
    db.delete(table="country", id=id)



@app.put("/update_country")
def update_country(country: Country):
    data = db.update(
        table="country",
        fields={"country_name":country.country_name, "country_code":country.country_code},
        where=("id", str(country.id)),
    )
    return data


