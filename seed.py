import json
from db import DB

db = DB("Country.db")

create_country = """
INSERT INTO country (
id, 
country_name,
country_code
) VALUES (
?, ?, ?
)
"""
create_city = """
INSERT INTO city (
id, 
city_name,
country_id
) VALUES (
?, ?,?
)
"""
create_travelagency = """
INSERT INTO travelagency (
id, 
travelagency_name,
travelagency_code
city_id
) VALUES (
?, ?,?,?
)
"""
with open("seed.json", "r") as seed:
    data = json.load(seed)
    print(data)
    for country in data["country"]:
        db.call_db(create_country, country["id"], country["country_name"],country["country_code"])

    for city in data["city"]:
        db.call_db(create_city,  city["id"], city["city_name"], city["country_id"])
    

    
    for travelagency in data["travelagency"]:
        db.call_db(create_travelagency,  travelagency["id"], travelagency["travelagency_name"], travelagency["travelagency_code"], travelagency["city_id"])